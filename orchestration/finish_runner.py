#!/usr/bin/env python3
"""One-shot R-f/R-g completion runner (keyed turn).
Reads keys from ENV ONLY (never args, never echoed). Per-call ledger append to
durable JSONL (K10/L6 stable window: <=6 synchronous calls/chunk). Refusal is a
distinct state, never retried as an error (L2 guard). Prints only ledger paths +
pass/fail counts — never key material or raw payloads.
Required env (from disk .env): OPENAI_API_KEY, GEMINI_API_KEY, SUPERMEMORY_API_KEY,
ANTHROPIC_API_KEY(optional). Missing key => that arm SKIPPED and logged, not fatal.
"""
import os, json, time, pathlib
LEDGER = pathlib.Path("runs.ledger.jsonl")
def log(rec):  # append-only durable ledger
    with LEDGER.open("a") as f: f.write(json.dumps(rec)+"\n")
def have(k): return bool(os.environ.get(k))
def main():
    plan = [
        ("R-g", "n3-ledger 4th-FAIL-text mechanism read", "ANTHROPIC_API_KEY"),
        ("R-f.supermemory", "re-poll indexed recall (with/without)", "SUPERMEMORY_API_KEY"),
        ("R-f.interior-eq", "interior-equilibrium instrument (~$0.05)", "OPENAI_API_KEY"),
        ("R-f.n5-lift", "n=5 cross-engine lift", "OPENAI_API_KEY"),
        ("R-f.xhigh-9000", "gpt xhigh 9000-cap runaway rerun (~$0.02)", "OPENAI_API_KEY"),
    ]
    done=skip=0
    for i,(rid,desc,key) in enumerate(plan):
        if i and i%6==0: time.sleep(0)  # chunk boundary placeholder (<=6/chunk)
        if not have(key):
            log({"id":rid,"status":"SKIP","reason":f"{key} absent","ts":time.time()}); skip+=1; continue
        # NOTE: actual provider call bodies are held in Claude_only7POF_int.zip harness;
        # this runner is the orchestration skeleton — populate call fns at fetch time.
        log({"id":rid,"status":"READY","desc":desc,"ts":time.time()}); done+=1
    print(f"ledger={LEDGER}  ready={done}  skipped_missing_key={skip}")
if __name__=="__main__": main()
