#!/usr/bin/env python3
"""LEAN7POF Interpreter Agent — portable launcher.

Run from any computer. Pulls the agent definition from the private GitHub repo
(Interpreter_Agent) and runs a governed, parse-guaranteed call against the
Anthropic API. NO secrets are stored in this file — both are read from env:

    export ANTHROPIC_API_KEY=...     # your Anthropic key
    export GITHUB_TOKEN=...          # fine-grained PAT with Contents:read on the repo

Usage:
    python interpreter_agent.py "your task here"
    python interpreter_agent.py "explain gradient descent for a Y10 class" --model claude-haiku-4-5-20251001
    echo "task" | python interpreter_agent.py -    # read task from stdin
"""
import os, sys, json, base64, argparse, urllib.request, urllib.error

REPO = os.environ.get("L7P_REPO", "Mrepetrucco/Interpreter_Agent")
SYS_FILE = os.environ.get("L7P_SYS", "LEAN7POF_system.md")
DEFAULT_MODEL = "claude-haiku-4-5-20251001"

ZSCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "claims": {"type": "array", "items": {"type": "object", "properties": {
            "text": {"type": "string"},
            "confidence": {"type": "string", "enum": ["unverified", "low", "medium", "high"]},
            "provenance": {"type": "string"}},
            "required": ["text", "confidence", "provenance"]}},
        "unresolved": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
    },
    "required": ["answer", "claims", "unresolved", "summary"],
}

def _req(url, data=None, headers=None, method="GET"):
    r = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(r, timeout=90) as x:
            return x.status, x.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()

def load_system(gh_token):
    """Fetch the agent system prompt from the private repo via the Contents API."""
    url = f"https://api.github.com/repos/{REPO}/contents/{SYS_FILE}"
    s, body = _req(url, headers={"Authorization": "Bearer " + gh_token,
                                 "User-Agent": "l7p-agent",
                                 "Accept": "application/vnd.github+json"})
    if s != 200:
        raise SystemExit(f"[l7p] could not fetch {SYS_FILE} from {REPO} (HTTP {s}). "
                         f"Check GITHUB_TOKEN has Contents:read on the repo.")
    return base64.b64decode(json.loads(body)["content"]).decode("utf-8")

def run(task, model):
    ak = os.environ.get("ANTHROPIC_API_KEY")
    gh = os.environ.get("GITHUB_TOKEN")
    if not ak or not gh:
        raise SystemExit("[l7p] set ANTHROPIC_API_KEY and GITHUB_TOKEN in your environment.")
    system = load_system(gh)
    payload = {
        "model": model, "max_tokens": 1500, "system": system,
        "tools": [{"name": "emit_zblock", "description": "Emit the governed LEAN7POF Z block.",
                   "input_schema": ZSCHEMA}],
        "tool_choice": {"type": "tool", "name": "emit_zblock"},
        "messages": [{"role": "user", "content": task}],
    }
    s, body = _req("https://api.anthropic.com/v1/messages",
                   data=json.dumps(payload).encode(),
                   headers={"x-api-key": ak, "anthropic-version": "2023-06-01",
                            "content-type": "application/json"}, method="POST")
    if s != 200:
        raise SystemExit(f"[l7p] Anthropic API HTTP {s}: {body[:300].decode('utf-8','ignore')}")
    resp = json.loads(body)
    tu = [b for b in resp.get("content", []) if b.get("type") == "tool_use"]
    out = tu[0]["input"] if tu else {"error": "no tool_use block", "raw": resp}
    u = resp.get("usage", {})
    out["_meta"] = {"model": model, "stop_reason": resp.get("stop_reason"),
                    "tokens": {"in": u.get("input_tokens"), "out": u.get("output_tokens")}}
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="LEAN7POF Interpreter Agent launcher")
    ap.add_argument("task", help="the task, or '-' to read from stdin")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    a = ap.parse_args()
    task = sys.stdin.read() if a.task == "-" else a.task
    print(json.dumps(run(task, a.model), indent=2, ensure_ascii=False))
