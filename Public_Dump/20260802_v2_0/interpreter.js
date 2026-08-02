// LEAN7POF interpreter core v2.0 — Anthropic Claude Messages API engine.
// v2.0 port: NON-BLOCKING fetch with bounded backoff (transport-retry on 429/500/502/503/529);
// pause_turn LOOP-CONTINUATION (append paused response + re-request); six-class handling.
const Interpreter = (() => {
  const XAPI = (typeof browser !== "undefined") ? browser : chrome;
  const API_URL = "https://api.anthropic.com/v1/messages";
  const ANTHROPIC_VERSION = "2023-06-01";

  const store = {
    get: (k) => new Promise(r => XAPI.storage.local.get(k, v => r(v[k]))),
    set: (o) => new Promise(r => XAPI.storage.local.set(o, r))
  };

  let _floor = null;
  async function loadFloor() {
    if (_floor) return { text: _floor, source: "bundled (LEAN7POF v1.3)" };
    const res = await fetch(XAPI.runtime.getURL("floor.md"));
    _floor = await res.text();
    return { text: _floor, source: "bundled (LEAN7POF v1.3)" };
  }

  function systemPrompt(floor) {
    return floor + "\n\n=== RUNTIME DIRECTIVE ===\n" +
      "Operate strictly under the LEAN7POF floor above (open every turn with CZO/OVF/OWRCS/OTES internally). " +
      "Emit ONLY the canonical Z envelope JSON: {\"response_type\":\"envelope\",\"answer\":\"…\",\"claims\":[{\"text\":\"…\"," +
      "\"confidence\":\"unverified|low|medium|high\",\"provenance\":\"source or 'uninstrumented'\",\"flags\":[]}]," +
      "\"unresolved\":[\"…\"],\"summary\":\"<=40 words\",\"meter\":{\"CSUL\":\"n/a\",\"OCSUL\":\"£0.00\",\"API\":\"$0.00\"}}. " +
      "No prose outside the JSON. A claim with no named source carries confidence \"unverified\". If the task is " +
      "self-defeating or trapped, RAISE it in unresolved (J2), do not execute it. Compute any computable value (L13).";
  }

  const sleep = ms => new Promise(r => setTimeout(r, ms));

  // NON-BLOCKING single POST: returns {class, status, json}; never throws for transport/HTTP.
  async function post(body, key, maxRetries = 2) {
    for (let attempt = 0; ; attempt++) {
      let res, j;
      try {
        res = await fetch(API_URL, { method: "POST", headers: {
          "content-type": "application/json", "x-api-key": key, "anthropic-version": ANTHROPIC_VERSION,
          "anthropic-dangerous-direct-browser-access": "true" }, body: JSON.stringify(body) });
        j = await res.json().catch(() => ({}));
      } catch (e) {
        if (attempt < maxRetries) { await sleep(1500 * (attempt + 1)); continue; }
        return { class: "transport-retry", status: null, json: { error: { message: String(e) } } };
      }
      if (res.ok) return { class: "normal", status: res.status, json: j };
      if ([429, 500, 502, 503, 529].includes(res.status) && attempt < maxRetries) { await sleep(1500 * (attempt + 1)); continue; }
      if (res.status === 404) return { class: "config-error", status: 404, json: j };
      if ([429, 500, 502, 503, 529].includes(res.status)) return { class: "transport-retry", status: res.status, json: j };
      return { class: "provider-error", status: res.status, json: j };
    }
  }

  // pause_turn LOOP-CONTINUATION: keep the last non-normal for the reconciler; accumulate text.
  async function runClaude(floor, task, model) {
    const key = await store.get("apiKey");
    if (!key) throw new Error("No Anthropic API key set (Settings).");
    const messages = [{ role: "user", content: task }];
    let text = "", lastUsage = {}, lastStop = null;
    for (let turn = 0; turn < 6; turn++) {
      const r = await post({ model, max_tokens: 4096, system: systemPrompt(floor), messages }, key);
      if (r.class !== "normal") {
        return { text, stop_reason: r.class, usage: lastUsage, model, transport: r };  // surfaced, not thrown
      }
      const j = r.json;
      lastUsage = j.usage || lastUsage; lastStop = j.stop_reason;
      text += (j.content || []).filter(b => b.type === "text").map(b => b.text).join("");
      if (j.stop_reason === "pause_turn") {                 // recoverable loop-continuation
        messages.push({ role: "assistant", content: j.content || [] }); continue;
      }
      return { text, stop_reason: j.stop_reason, usage: j.usage || {}, model };
    }
    return { text, stop_reason: lastStop || "max_turns", usage: lastUsage, model };
  }

  async function appendLog(task, env, model) {
    const log = (await store.get("log")) || "";
    const entry = `\n---\n[${new Date().toISOString()}] model=${model}\nTASK: ${task}\nENVELOPE: ${JSON.stringify(env)}\n`;
    await store.set({ log: (log + entry).slice(-120000) });
  }

  async function run(task, model) {
    const { text: floor, source } = await loadFloor();
    const rin = parseFloat(await store.get("rateIn")) || 0;
    const rout = parseFloat(await store.get("rateOut")) || 0;
    const resp = await runClaude(floor, task, model);
    const env = Reconciler.reconcile(resp.text, task, { stop_reason: resp.stop_reason, usage: resp.usage, model, rin, rout });
    await appendLog(task, env, model);
    return { envelope: env, model, floorSource: source, stop_reason: resp.stop_reason };
  }

  return { run, loadFloor };
})();
