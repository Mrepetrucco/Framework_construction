#!/usr/bin/env python3
"""LEAN7POF Interpreter Agent v2 — portable GOVERNED AGENT WITH TOOLS.

Extends the v1 launcher with an agentic tool loop and the full encoding set
(CZO, OVF, OWRCS, OTES, CSUL/API/XAPI accounting). Tools:
  - web_search    : Anthropic server-side search (no separate search key needed)
  - write_file/read_file : persistent local sandbox (./l7p_sandbox/*.md.txt)
  - emit_zblock   : the governed final output (guaranteed-parse Z block)

Portability: reads ANTHROPIC_API_KEY + GITHUB_TOKEN from env; pulls the agent
definition from the GitHub repo at run time. No secrets stored.

Usage: python interpreter_agent_v2.py "task"  [--model claude-fable-5] [--csul 0.8] [--api-max 4.0]
"""
import os, sys, json, base64, argparse, time, pathlib, urllib.request, urllib.error

REPO = os.environ.get("L7P_REPO", "Mrepetrucco/Interpreter_Agent")
SYS_FILE = os.environ.get("L7P_SYS", "LEAN7POF_system.md")
SANDBOX = pathlib.Path(os.environ.get("L7P_SANDBOX", "l7p_sandbox")); SANDBOX.mkdir(exist_ok=True)
# rough per-Mtok USD (in,out) for CSUL/API accounting; extend as needed
PRICES = {"claude-haiku-4-5-20251001": (1, 5), "claude-sonnet-5": (3, 15),
          "claude-opus-4-8": (5, 25), "claude-fable-5": (10, 50)}

ZSCHEMA = {"type": "object", "properties": {
    "answer": {"type": "string"},
    "claims": {"type": "array", "items": {"type": "object", "properties": {
        "text": {"type": "string"}, "confidence": {"type": "string", "enum": ["unverified","low","medium","high"]},
        "provenance": {"type": "string"}}, "required": ["text","confidence","provenance"]}},
    "unresolved": {"type": "array", "items": {"type": "string"}},
    "summary": {"type": "string"}}, "required": ["answer","claims","unresolved","summary"]}

TOOLS = [
    {"type": "web_search_20250305", "name": "web_search", "max_uses": 5},
    {"name": "write_file", "description": "Write text to ./l7p_sandbox/<name>.md.txt (persistent).",
     "input_schema": {"type": "object", "properties": {"name": {"type": "string"}, "content": {"type": "string"}}, "required": ["name","content"]}},
    {"name": "read_file", "description": "Read ./l7p_sandbox/<name>.md.txt.",
     "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
    {"name": "emit_zblock", "description": "Emit the final governed Z block. Call this LAST.",
     "input_schema": ZSCHEMA},
]

def _api(payload, key):
    r = urllib.request.Request("https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode(),
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(r, timeout=120) as x: return json.loads(x.read())
    except urllib.error.HTTPError as e: raise SystemExit(f"[l7p] API {e.code}: {e.read()[:300].decode('utf-8','ignore')}")

def load_system(gh):
    u = f"https://api.github.com/repos/{REPO}/contents/{SYS_FILE}"
    req = urllib.request.Request(u, headers={"Authorization":"Bearer "+gh,"User-Agent":"l7p","Accept":"application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as x: data = json.loads(x.read())
        return base64.b64decode(data["content"]).decode("utf-8")
    except urllib.error.HTTPError:
        # public-repo fallback: no token needed
        raw = f"https://raw.githubusercontent.com/{REPO}/main/{SYS_FILE}"
        with urllib.request.urlopen(raw, timeout=30) as x: return x.read().decode("utf-8")

def exec_local(name, inp):
    if name == "write_file":
        p = SANDBOX / (pathlib.Path(inp["name"]).name)
        if not p.name.endswith(".md.txt"): p = p.with_suffix(".md.txt")
        p.write_text(inp["content"]); return f"wrote {p}"
    if name == "read_file":
        p = SANDBOX / pathlib.Path(inp["name"]).name
        return p.read_text() if p.exists() else f"[missing {p}]"
    return f"[unknown tool {name}]"

def run(task, model, csul_max, api_max):
    key = os.environ.get("ANTHROPIC_API_KEY"); gh = os.environ.get("GITHUB_TOKEN", "")
    if not key: raise SystemExit("[l7p] set ANTHROPIC_API_KEY")
    system = load_system(gh) + f"\n\n# Runtime encodings\nCZO: framework loaded from GitHub. OVF: report the serving model generically (agnostic). OWRCS: if you cannot finish, call write_file for a residual plan '<task>_residual' then emit_zblock noting it. OTES: use the fewest tool calls that change the answer. Budget: CSUL<={csul_max}, API<=${api_max}. Emit the governed Z block via emit_zblock when done."
    msgs = [{"role": "user", "content": task}]
    tin = tout = 0
    for _ in range(12):  # bounded agent loop
        resp = _api({"model": model, "max_tokens": 2000, "system": system, "tools": TOOLS, "messages": msgs}, key)
        u = resp.get("usage", {}); tin += u.get("input_tokens", 0); tout += u.get("output_tokens", 0)
        cin, cout = PRICES.get(model, (3, 15)); cost = tin/1e6*cin + tout/1e6*cout
        blocks = resp.get("content", [])
        # capture the governed final output
        for b in blocks:
            if b.get("type") == "tool_use" and b.get("name") == "emit_zblock":
                out = b["input"]; out["_meta"] = {"model_class": "agnostic", "stop": resp.get("stop_reason"),
                    "tool_turns": _, "tokens": {"in": tin, "out": tout}, "api_usd": round(cost, 5)}
                return out
        if resp.get("stop_reason") != "tool_use":
            return {"answer": " ".join(b.get("text","") for b in blocks if b.get("type")=="text"),
                    "claims": [], "unresolved": ["agent ended without emit_zblock"], "summary": "",
                    "_meta": {"tokens": {"in": tin, "out": tout}, "api_usd": round(cost, 5)}}
        # execute local tool_use blocks; server tools (web_search) are handled by the API
        msgs.append({"role": "assistant", "content": blocks})
        results = []
        for b in blocks:
            if b.get("type") == "tool_use" and b.get("name") in ("write_file", "read_file"):
                results.append({"type": "tool_result", "tool_use_id": b["id"], "content": exec_local(b["name"], b["input"])})
        if results: msgs.append({"role": "user", "content": results})
        if cost > api_max: return {"answer": "", "claims": [], "unresolved": [f"API budget ${api_max} hit"], "summary": "stopped on budget", "_meta": {"api_usd": round(cost,5)}}
    return {"answer": "", "claims": [], "unresolved": ["max agent turns reached"], "summary": "", "_meta": {"tokens": {"in": tin, "out": tout}}}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("task"); ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--csul", type=float, default=0.8); ap.add_argument("--api-max", type=float, default=4.0)
    a = ap.parse_args()
    task = sys.stdin.read() if a.task == "-" else a.task
    print(json.dumps(run(task, a.model, a.csul, a.api_max), indent=2, ensure_ascii=False))
