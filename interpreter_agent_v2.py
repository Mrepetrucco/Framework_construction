#!/usr/bin/env python3
"""LEAN7POF Interpreter Agent v2.0 — GOVERNED AGENT WITH TOOLS, on the shared AX7 module.

MERGE (31 Jul 2026, from interpreter_agent_v2.py) fixing:
  1. Haiku default -> claude-opus-4-8 (J1: Haiku NEVER).
  2. pause_turn now a LOOP-CONTINUATION (append paused response + continue), not an early exit.
  3. blocking _api -> ax7_provider_module.call_nonblocking (bounded backoff, returns status).
  4. short ZSCHEMA -> CANON_SCHEMA (response_type + meter; P1 single wire shape).
  5. system file -> LEAN7POFV2_v2.0.md.txt (the uplifted V2/AX7 lean).
Tools: web_search (server) · write_file/read_file (sandbox) · emit_zblock (canonical final).
Usage: python interpreter_agent_v2.0.py "task" [--model claude-opus-4-8] [--csul 0.8] [--api-max 4.0]
"""
import os, sys, json, base64, argparse, pathlib, urllib.request, urllib.error

# shared non-blocking provider layer + canonical schema + parser pair
try:
    from ax7_provider_module import CANON_SCHEMA, parse_pair, classify_anthropic, call_nonblocking
except ImportError:  # co-locate ax7_provider_module.py, or vendor it
    raise SystemExit("[l7p] ax7_provider_module.py must be importable (co-locate it)")

REPO = os.environ.get("L7P_REPO", "Mrepetrucco/Framework_construction")
SYS_FILE = os.environ.get("L7P_SYS", "Public_Dump/20260731_v1_5/LEAN7POFV2_v2.0.md.txt")
SANDBOX = pathlib.Path(os.environ.get("L7P_SANDBOX", "l7p_sandbox")); SANDBOX.mkdir(exist_ok=True)
DEFAULT_MODEL = "claude-opus-4-8"                                  # J1: never Haiku
PRICES = {"claude-sonnet-5": (3, 15), "claude-opus-4-8": (5, 25), "claude-fable-5": (10, 50)}

TOOLS = [
    {"type": "web_search_20250305", "name": "web_search", "max_uses": 5},
    {"name": "write_file", "description": "Write text to ./l7p_sandbox/<name>.md.txt (persistent).",
     "input_schema": {"type": "object", "properties": {"name": {"type": "string"}, "content": {"type": "string"}}, "required": ["name", "content"]}},
    {"name": "read_file", "description": "Read ./l7p_sandbox/<name>.md.txt.",
     "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
    {"name": "emit_zblock", "description": "Emit the final governed canonical Z block. Call LAST.",
     "input_schema": CANON_SCHEMA},                                # P1: canonical wire shape
]

def load_system(gh):
    u = f"https://api.github.com/repos/{REPO}/contents/{SYS_FILE}"
    req = urllib.request.Request(u, headers={"Authorization": "Bearer " + gh, "User-Agent": "l7p", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as x:
            return base64.b64decode(json.loads(x.read())["content"]).decode("utf-8")
    except urllib.error.HTTPError:
        raw = f"https://raw.githubusercontent.com/{REPO}/main/{SYS_FILE}"
        with urllib.request.urlopen(raw, timeout=30) as x:
            return x.read().decode("utf-8")

def exec_local(name, inp):
    if name == "write_file":
        p = SANDBOX / pathlib.Path(inp["name"]).name
        if not p.name.endswith(".md.txt"): p = p.with_suffix(".md.txt")
        p.write_text(inp["content"]); return f"wrote {p}"
    if name == "read_file":
        p = SANDBOX / pathlib.Path(inp["name"]).name
        return p.read_text() if p.exists() else f"[missing {p}]"
    return f"[unknown tool {name}]"

def run(task, model, csul_max, api_max, max_turns=12):
    key = os.environ.get("ANTHROPIC_API_KEY"); gh = os.environ.get("GITHUB_TOKEN", "")
    if not key: return {"answer": "", "claims": [], "unresolved": ["set ANTHROPIC_API_KEY"], "summary": ""}
    system = load_system(gh) + (f"\n\n# Runtime\nCZO: framework loaded from GitHub. OVF: report the serving model generically. "
        f"OWRCS: pause_turn is recoverable — continue through it; on genuine exhaustion write_file a '<task>_residual' then emit_zblock. "
        f"OTES: fewest tool calls that change the answer. Budget: CSUL<={csul_max}, API<=${api_max}. Emit via emit_zblock when done.")
    hdr = {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    msgs = [{"role": "user", "content": task}]
    tin = tout = 0
    for turn in range(max_turns):
        body = {"model": model, "max_tokens": 2000, "system": system, "tools": TOOLS, "messages": msgs}
        r = call_nonblocking("https://api.anthropic.com/v1/messages", hdr, body)   # NON-BLOCKING
        if r["class"] != "normal":                                                # transport/config, not blocking
            return {"answer": "", "claims": [], "unresolved": [f"{r['class']}: {r.get('http')}"], "summary": "provider non-normal", "_meta": r}
        resp = json.loads(r["raw"]); u = resp.get("usage", {})
        tin += u.get("input_tokens", 0); tout += u.get("output_tokens", 0)
        cin, cout = PRICES.get(model, (5, 25)); cost = tin / 1e6 * cin + tout / 1e6 * cout
        blocks = resp.get("content", [])
        cls = classify_anthropic(resp)
        for b in blocks:
            if b.get("type") == "tool_use" and b.get("name") == "emit_zblock":
                out = b["input"]
                ok, _ = parse_pair(json.dumps(out))                               # validate canonical shape
                out["_meta"] = {"parse_pair_ok": ok, "stop": resp.get("stop_reason"), "turns": turn,
                                "tokens": {"in": tin, "out": tout}, "api_usd": round(cost, 5)}
                return out
        if cls == "loop-continuation":                                            # pause_turn: append + continue
            msgs.append({"role": "assistant", "content": blocks}); continue
        if resp.get("stop_reason") != "tool_use":
            return {"answer": " ".join(b.get("text", "") for b in blocks if b.get("type") == "text"),
                    "claims": [], "unresolved": ["agent ended without emit_zblock"], "summary": "",
                    "_meta": {"tokens": {"in": tin, "out": tout}, "api_usd": round(cost, 5)}}
        msgs.append({"role": "assistant", "content": blocks})
        results = [{"type": "tool_result", "tool_use_id": b["id"], "content": exec_local(b["name"], b["input"])}
                   for b in blocks if b.get("type") == "tool_use" and b.get("name") in ("write_file", "read_file")]
        if results: msgs.append({"role": "user", "content": results})
        if cost > api_max:
            return {"answer": "", "claims": [], "unresolved": [f"API budget ${api_max} hit"], "summary": "stopped on budget", "_meta": {"api_usd": round(cost, 5)}}
    return {"answer": "", "claims": [], "unresolved": ["max agent turns reached"], "summary": "", "_meta": {"tokens": {"in": tin, "out": tout}}}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("task"); ap.add_argument("--model", default=DEFAULT_MODEL)   # never Haiku
    ap.add_argument("--csul", type=float, default=0.8); ap.add_argument("--api-max", type=float, default=4.0)
    a = ap.parse_args()
    task = sys.stdin.read() if a.task == "-" else a.task
    print(json.dumps(run(task, a.model, a.csul, a.api_max), indent=2, ensure_ascii=False))
