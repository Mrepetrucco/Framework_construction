// N1 Reconciler (Claude-native) v2.0 — enforces the LEAN7POF J-screen on the API answer.
// v2.0 port: (5) band enforcement lower-only; (6) DIFFERENTIAL PARSER PAIR (greedy+strict), fail-closed
// on disagreement as truncation-state; cache-token cost meter; canonical envelope carries `meter`.
const Reconciler = (() => {

  function trapScan(task) {
    const raises = [];
    const t = (task || "").toLowerCase();
    if (/\b(exactly|in|write|use|no more than|at least)\s+\d+\s+sentences?\b/.test(t) || /\bone[- ]sentence\b/.test(t))
      raises.push("J2: sentence-count directive — raised, not executed (dominant Fable refusal trigger; use word/schema caps instead).");
    if (/\bignore (the|all|previous|above)\b.*\b(instruction|rule|framework|schema)/.test(t))
      raises.push("J2: instruction-override directive — raised for review, not executed.");
    if (/\balways\b.*\bnever\b/.test(t) || /\bboth\b.*\bneither\b/.test(t))
      raises.push("J2: possible internal contradiction — confirm intent before executing.");
    return raises;
  }

  // parser 1 — greedy: first '{' .. last '}'
  function parseGreedy(raw) {
    let s = String(raw || "").replace(/```json|```/g, "").trim();
    const a = s.indexOf("{"), b = s.lastIndexOf("}");
    if (a === -1 || b === -1 || b < a) return null;
    try { return JSON.parse(s.slice(a, b + 1)); } catch { return null; }
  }
  // parser 2 — strict: first BALANCED {...} object via depth scan
  function parseStrict(raw) {
    const s = String(raw || "");
    let depth = 0, start = -1;
    for (let i = 0; i < s.length; i++) {
      const ch = s[i];
      if (ch === "{") { if (depth === 0) start = i; depth++; }
      else if (ch === "}") { depth--; if (depth === 0 && start >= 0) { try { return JSON.parse(s.slice(start, i + 1)); } catch { start = -1; } } }
    }
    return null;
  }
  const CANON = ["response_type", "answer", "claims", "unresolved", "summary"];
  const keysetOk = o => o && typeof o === "object" && (CANON.every(k => k in o) || ["a","c","u","s"].every(k => k in o));

  // (6) differential parser pair — PASS only on agreement + canonical/compact keyset.
  function parsePair(raw) {
    const p1 = parseGreedy(raw), p2 = parseStrict(raw);
    if (p1 && p2 && keysetOk(p1) && keysetOk(p2) && JSON.stringify(p1) === JSON.stringify(p2)) return { ok: true, env: p1 };
    if (p2 && keysetOk(p2)) return { ok: false, env: p2 };   // single-parser, not agreed
    return { ok: false, env: null };
  }

  // cost meter incl. cache tokens (v1.0.3: cache_creation 1.25x input, cache_read 0.10x input)
  function meter(usage, model, rin, rout) {
    const i = usage.input_tokens || 0, o = usage.output_tokens || 0;
    const cc = usage.cache_creation_input_tokens || 0, cr = usage.cache_read_input_tokens || 0;
    let est = null;
    if (rin || rout) est = i/1e6*(rin||0) + o/1e6*(rout||0) + cc/1e6*(rin||0)*1.25 + cr/1e6*(rin||0)*0.10;
    return {
      CSUL: "n/a (API)", OCSUL: "£0.00", XAPI: "$0.00",
      API: est !== null ? `$${est.toFixed(4)} est [UNVERIFIED rate] (${i}+${o} tok; cache ${cc}c/${cr}r) — ground truth: Anthropic console`
                        : `metered · ${i}+${o} tok (cache ${cc}c/${cr}r; set a rate to estimate $) — ground truth: Anthropic console`
    };
  }

  function reconcile(raw, task, ctx = {}) {
    const { stop_reason, usage = {}, model = "", rin = 0, rout = 0 } = ctx;
    const trap = trapScan(task);

    // Safeguard refusal — DISTINCT STATE, never context-loss / never a capability verdict (Protocol 4.1).
    if (stop_reason === "refusal") {
      return { response_type: "envelope", answer: "", claims: [],
        unresolved: ["SAFEGUARD REFUSAL (stop_reason=refusal) — a classifier event, NOT context-loss or a capability limit.",
          "Enablement ladder (Protocol §4.3): retry via an output SCHEMA with word-capped fields, then word-count caps, then paragraph bounds. NEVER reference counted sentences. After two adjusted-form refusals, route to Opus."],
        summary: "Model returned a safeguard refusal; raised with the enablement ladder rather than executed.",
        j_trace: { j_applied: ["Protocol§4.1","Protocol§4.6"], instruction_safety: "refusal_state", j_raised: ["safeguard refusal"], certifier: "none (not decision-bearing)" },
        meter: meter(usage, model, rin, rout) };
    }

    const { ok, env: parsed } = parsePair(raw);
    // (6) fail-closed on parser disagreement -> truncation-state, offer re-run at 2x bound.
    if (!ok && (!parsed || stop_reason === "max_tokens")) {
      return { response_type: "envelope", answer: "", claims: [],
        unresolved: ["TRUNCATION-STATE: differential parser pair did not agree on a canonical envelope" + (stop_reason === "max_tokens" ? " (stop_reason=max_tokens)" : "") + ". Re-run at 2x max_tokens."],
        summary: "Emission failed the parser-pair agreement gate; flagged as truncation, not rendered.",
        j_trace: { j_applied: ["check6_parser_pair"], instruction_safety: "fail_closed", j_raised: ["parser disagreement"], certifier: "none" },
        meter: meter(usage, model, rin, rout) };
    }
    let env = parsed || { response_type: "envelope", answer: String(raw || "").trim() || "(no content)", claims: [], unresolved: [], summary: "Engine output wrapped verbatim (not agreed by parser pair)." };
    env.response_type = "envelope";
    env.answer = env.answer ?? env.a ?? "";
    env.summary = env.summary ?? env.s ?? "";
    if (!Array.isArray(env.claims)) env.claims = Array.isArray(env.c) ? env.c : [];
    if (!Array.isArray(env.unresolved)) env.unresolved = Array.isArray(env.u) ? env.u : [];

    // (5) band enforcement — deterministic cf from provenance class, LOWER-ONLY.
    const RANK = { unverified: 0, low: 1, medium: 2, high: 3 };
    env.claims = env.claims.map(c => {
      c = (c && typeof c === "object") ? c : { text: String(c) };
      const prov = (c.provenance || c.p || "").toString().trim().toLowerCase();
      let ceiling = "high";
      if (!prov || prov === "" || prov === "uninstrumented" || prov === "none") ceiling = "unverified";
      let cf = (c.confidence || c.cf || "unverified").toLowerCase();
      if (!(cf in RANK)) cf = "unverified";
      if (RANK[cf] > RANK[ceiling]) cf = ceiling;   // lower-only
      c.confidence = cf;
      if (!Array.isArray(c.flags)) c.flags = [];
      return c;
    });

    for (const r of trap) if (!env.unresolved.includes(r)) env.unresolved.push(r);
    env.j_trace = { j_applied: ["L13","L14","J2","R1","check5_band","check6_parser_pair"],
      instruction_safety: trap.length ? "trap_raised" : "clean", j_raised: trap.slice(),
      parser_pair: ok ? "agreed" : "single-parser (flagged)", certifier: "none (not decision-bearing)" };
    env.meter = meter(usage, model, rin, rout);
    return env;
  }
  return { reconcile, trapScan, parsePair };
})();
if (typeof module !== "undefined") module.exports = Reconciler;
