#!/usr/bin/env python3
"""LEAN7POF Interpreter Agent (v1, merged 20260801) — single-shot governed launcher on the shared AX7 module.
In-place merge fixing: Haiku default -> claude-opus-4-8 (J1); blocking call -> non-blocking module;
short schema -> CANON_SCHEMA (P1); pause_turn -> loop-continuation. For the agentic tool loop use interpreter_agent_v2.0.py.
Usage: python interpreter_agent.py "task" [--model claude-opus-4-8]
"""
import os, sys, json, base64, argparse, urllib.request, urllib.error
try:
    from ax7_provider_module import CANON_SCHEMA, parse_pair, classify_anthropic, call_nonblocking
except ImportError:
    raise SystemExit("[l7p] ax7_provider_module.py must be importable (co-locate it)")

REPO = os.environ.get("L7P_REPO", "Mrepetrucco/Framework_construction")
SYS_FILE = os.environ.get("L7P_SYS", "Public_Dump/20260731_v1_5/LEAN7POFV2_v2.0.md.txt")
DEFAULT_MODEL = "claude-opus-4-8"                                  # J1: never Haiku

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

def run(task, model):
    key = os.environ.get("ANTHROPIC_API_KEY"); gh = os.environ.get("GITHUB_TOKEN", "")
    if not key: return {"answer": "", "claims": [], "unresolved": ["set ANTHROPIC_API_KEY"], "summary": ""}
    system = load_system(gh) + "\n\n# Runtime\nEmit the governed canonical Z block via emit_zblock. pause_turn is recoverable — continue through it."
    tool = {"name": "emit_zblock", "description": "Emit the final governed canonical Z block.", "input_schema": CANON_SCHEMA}
    hdr = {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    msgs = [{"role": "user", "content": task}]
    for _ in range(6):                                            # bounded; pause_turn continues the loop
        body = {"model": model, "max_tokens": 2000, "system": system, "tools": [tool],
                "tool_choice": {"type": "tool", "name": "emit_zblock"}, "messages": msgs}
        r = call_nonblocking("https://api.anthropic.com/v1/messages", hdr, body)   # NON-BLOCKING
        if r["class"] != "normal":
            return {"answer": "", "claims": [], "unresolved": [f"{r['class']}: {r.get('http')}"], "summary": "provider non-normal"}
        resp = json.loads(r["raw"])
        for b in resp.get("content", []):
            if b.get("type") == "tool_use" and b.get("name") == "emit_zblock":
                out = b["input"]; ok, _ = parse_pair(json.dumps(out))
                out["_meta"] = {"parse_pair_ok": ok, "stop": resp.get("stop_reason"), "usage": resp.get("usage", {})}
                return out
        if classify_anthropic(resp) == "loop-continuation":       # pause_turn
            msgs.append({"role": "assistant", "content": resp.get("content", [])}); continue
        return {"answer": "", "claims": [], "unresolved": ["no emit_zblock"], "summary": ""}
    return {"answer": "", "claims": [], "unresolved": ["max turns"], "summary": ""}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("task"); ap.add_argument("--model", default=DEFAULT_MODEL)     # never Haiku
    a = ap.parse_args()
    task = sys.stdin.read() if a.task == "-" else a.task
    print(json.dumps(run(task, a.model), indent=2, ensure_ascii=False))
