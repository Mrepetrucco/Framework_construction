"""
ax7_provider_module.py  —  UP4/UP5/UP6 reference implementation (live-XAPI-verified)
7POF V2 / AX7 · non-blocking foreign-provider handlers + canonical AX7 binding schema.

Design (per owner amends 31 Jul 2026):
- NON-BLOCKING: transport errors -> bounded backoff + fallback, returned as a status
  object, never a raise/hard-block. The agent loop keeps control.
- pause-continue is ANTHROPIC-ONLY (stop_reason 'pause_turn'); it is a recoverable
  loop-continuation, NOT a failure class, and is therefore ABSENT from the OpenAI/
  Gemini paths here (UP1 amend).
- BINDING MODES (UP6): M-prompt (plain-JSON by instruction) is the floor; flip to
  M-native (provider-enforced structured output) ONLY where strict binding is
  critical for full model exploitation — still under the AX7 canonical schema.
- Foreign-provider failure classes: {normal, length, refusal, transport-retry, config-error}.
"""
import os, json, time, urllib.request, urllib.error

# ---------- canonical AX7 wire schema (single source; long-key form) ----------
CANON_SCHEMA = {
    "type": "object",
    "properties": {
        "response_type": {"type": "string", "enum": ["envelope"]},
        "answer": {"type": "string"},
        "claims": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "confidence": {"type": "string", "enum": ["unverified", "low", "medium", "high"]},
                "provenance": {"type": "string"},
                "flags": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["text", "confidence", "provenance", "flags"],
            "additionalProperties": False,
        }},
        "unresolved": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
        "meter": {
            "type": "object",
            "properties": {"CSUL": {"type": "string"}, "OCSUL": {"type": "string"}, "API": {"type": "string"}},
            "required": ["CSUL", "OCSUL", "API"], "additionalProperties": False,
        },
    },
    "required": ["response_type", "answer", "claims", "unresolved", "summary", "meter"],
    "additionalProperties": False,
}
CANON_KEYS = set(CANON_SCHEMA["required"])
COMPACT_KEYS = {"a", "c", "u", "s"}

# ---------- differential parser pair (floor; runs OUTSIDE the producer) ----------
def _first_obj(text):
    depth = 0; start = -1
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0: start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start >= 0:
                try: return json.loads(text[start:i+1])
                except Exception: start = -1
    return None

def parse_pair(text):
    """Return (ok, obj). ok only if both parsers agree on a canonical-or-compact object."""
    p1 = None
    try:
        import re
        m = re.search(r"\{.*\}", text, re.S)
        if m: p1 = json.loads(m.group(0))
    except Exception:
        p1 = None
    p2 = _first_obj(text)
    def keyset_ok(o):
        if not isinstance(o, dict): return False
        ks = set(o.keys())
        return CANON_KEYS.issubset(ks) or COMPACT_KEYS.issubset(ks)
    if p1 and p2 and keyset_ok(p1) and keyset_ok(p2) and p1 == p2:
        return True, p1
    if p2 and keyset_ok(p2):           # single-parser fallback flagged not-agreed
        return False, p2
    return False, None

# ---------- provider schema adapters ----------
def openai_text_format():
    return {"type": "json_schema", "name": "zblock", "strict": True, "schema": CANON_SCHEMA}

def gemini_schema():
    # Gemini responseSchema: OpenAPI-subset; keep enums + required; drop additionalProperties.
    def strip(o):
        if isinstance(o, dict):
            return {k: strip(v) for k, v in o.items() if k != "additionalProperties"}
        if isinstance(o, list):
            return [strip(x) for x in o]
        return o
    return strip(CANON_SCHEMA)

# ---------- non-blocking HTTP with bounded backoff ----------
def _http(url, headers, body=None, method="GET", timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode()

def call_nonblocking(url, headers, body, max_retries=2, base_backoff=5):
    """Returns a status dict; NEVER raises for transport/HTTP. Non-blocking by contract."""
    attempt = 0
    while True:
        try:
            st, raw = _http(url, headers, body, "POST")
            return {"class": "normal", "http": st, "raw": raw}
        except urllib.error.HTTPError as e:
            code = e.code; msg = e.read().decode()[:300]
            if code in (429, 500, 502, 503, 529) and attempt < max_retries:
                time.sleep(base_backoff * (attempt + 1)); attempt += 1; continue
            if code == 404:
                return {"class": "config-error", "http": code, "msg": msg}
            if code in (429, 500, 502, 503, 529):
                return {"class": "transport-retry", "http": code, "msg": msg, "exhausted": True}
            return {"class": "provider-error", "http": code, "msg": msg}
        except Exception as e:
            if attempt < max_retries:
                time.sleep(base_backoff * (attempt + 1)); attempt += 1; continue
            return {"class": "transport-retry", "http": None, "msg": repr(e), "exhausted": True}

# ---------- finish-reason classification (non-blocking) ----------
def classify_openai(d):
    status = d.get("status")
    if status == "incomplete":
        r = (d.get("incomplete_details") or {}).get("reason")
        return "length" if r == "max_output_tokens" else ("refusal" if r == "content_filter" else "context-loss")
    for it in d.get("output", []):
        if it.get("type") == "message":
            for c in it.get("content", []):
                if c.get("type") == "refusal": return "refusal"
    return "normal"

def classify_gemini(cand):
    fr = cand.get("finishReason")
    return {"STOP": "normal", "MAX_TOKENS": "length", "SAFETY": "refusal",
            "RECITATION": "refusal"}.get(fr, "context-loss")

# ---------- provider callers (M-native | M-prompt) ----------
def openai_call(key, prompt, system, mode="m-prompt", model="gpt-5.6-sol", max_out=5000):
    hdr = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    body = {"model": model, "instructions": system, "input": prompt,
            "reasoning": {"effort": "low"}, "max_output_tokens": max_out}
    if mode == "m-native":
        body["text"] = {"format": openai_text_format()}
    return call_nonblocking("https://api.openai.com/v1/responses", hdr, body)

def gemini_call(key, prompt, system, mode="m-prompt", model="gemini-3.1-pro-preview", max_out=4000):
    hdr = {"x-goog-api-key": key, "Content-Type": "application/json"}
    gen = {"maxOutputTokens": max_out, "thinkingConfig": {"thinkingLevel": "low"}}
    if mode == "m-native":
        gen["responseMimeType"] = "application/json"; gen["responseSchema"] = gemini_schema()
    body = {"systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": prompt}]}], "generationConfig": gen}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    return call_nonblocking(url, hdr, body)

def classify_anthropic(d):
    """Anthropic Messages stop_reason -> class. pause_turn is a LOOP-CONTINUATION (UP1), not a failure."""
    sr = d.get("stop_reason")
    return {"end_turn": "normal", "stop_sequence": "normal", "tool_use": "normal",
            "max_tokens": "length", "model_context_window_exceeded": "length",
            "refusal": "refusal", "pause_turn": "loop-continuation"}.get(sr, "context-loss")

# ============================ LIVE SELF-TEST ============================
if __name__ == "__main__":
    K = {}
    for ln in open("/home/claude/envwork/all_keys.env"):
        ln = ln.strip()
        if "=" in ln and not ln.startswith("#"):
            k, _, v = ln.partition("="); K[k.strip()] = v.strip().strip('"').strip("'")
    OPENAI, GEMINI = K.get("OPENAI_API_KEY", ""), K.get("GEMINI_API_KEY", "")
    SEC = [s for s in [OPENAI, GEMINI, K.get("ANTHROPIC_API_KEY",""), K.get("GITHUB_TOKEN","")] if s]
    def scrub(s):
        s = str(s)
        for x in SEC: s = s.replace(x, "***")
        return s
    def out(*a): print(scrub(" ".join(str(x) for x in a)))

    SYS = "Operate under 7POF V2 / AX7. Emit ONLY the canonical zblock envelope."
    PR = "Emit a minimal valid zblock envelope confirming you can bind this schema. answer='bind ok'."

    out("=== AX7 M-native binding self-test (non-blocking) ===")
    # OpenAI m-native
    if OPENAI:
        r = openai_call(OPENAI, PR, SYS, mode="m-native")
        if r["class"] == "normal":
            d = json.loads(r["raw"]); cls = classify_openai(d)
            txt = "".join(c.get("text","") for it in d.get("output",[]) if it.get("type")=="message"
                        for c in it.get("content",[]) if c.get("type")=="output_text")
            ok, obj = parse_pair(txt)
            u = d.get("usage", {}); cost = (u.get("input_tokens",0)/1e6*5)+(u.get("output_tokens",0)/1e6*30)
            out(f"OpenAI gpt-5.6-sol m-native: class={cls} parse_pair_ok={ok} keys={list(obj.keys()) if obj else None} cost=${cost:.4f}")
        else:
            out("OpenAI m-native:", r["class"], r.get("http"), scrub(r.get("msg","")[:120]))
    # Gemini m-native
    if GEMINI:
        r = gemini_call(GEMINI, PR, SYS, mode="m-native")
        if r["class"] == "normal":
            d = json.loads(r["raw"]); cand = (d.get("candidates") or [{}])[0]
            cls = classify_gemini(cand)
            txt = "".join(p.get("text","") for p in (cand.get("content",{}).get("parts") or []))
            ok, obj = parse_pair(txt)
            um = d.get("usageMetadata", {}); cost = (um.get("promptTokenCount",0)/1e6*2.0)+((um.get("candidatesTokenCount",0)+um.get("thoughtsTokenCount",0))/1e6*12.0)
            out(f"Gemini 3.1-pro-preview m-native: class={cls} parse_pair_ok={ok} keys={list(obj.keys()) if obj else None} cost~=${cost:.4f}")
        else:
            out("Gemini m-native:", r["class"], r.get("http"), scrub(r.get("msg","")[:120]))
    out("=== done ===")
