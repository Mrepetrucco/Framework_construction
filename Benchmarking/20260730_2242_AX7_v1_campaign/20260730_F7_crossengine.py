#!/usr/bin/env python3
"""
F7 CROSS-ENGINE SELF-CONSISTENCY TEST (30 Jul 2026) — pre-registered.
Question: does AX7 escape the measured historical trap (full canon 0/10 parse-bind off-family
vs lean skeleton 10/10 [MEASURED: 2026-07-17 cross-engine programme])?
Design: per foreign engine, TWO ARMS x n=5:
  FLOOR   = full AX7 floor (v2 FLOOR_CACHE + SYS_COMPACT) as system + P1 instrument
  MINIMAL = SYS_COMPACT schema instruction only (no floor) + P1 instrument
Scored with the FROZEN pilot scorers (A1 bind, A2 prov-completeness, A4 calibration) via the
portable validate-then-parse shim (no provider-native strict modes — the portability baseline).
Prediction [UNVERIFIED]: if AX7 inherited the full-canon trap, FLOOR << MINIMAL on bind.
Budgets: XAPI < $2.50 per provider, hard stop $2.00 each. Keys header/query-only, never printed.
Pricing assumptions (for metering only): gpt-4o 2.5/10 $/MTok [UNVERIFIED: assumed from prior
programme]; gemini 1.25/5 $/MTok [UNVERIFIED: conservative]. Calls are few so worst-case error
in the meter cannot approach the cap.
"""
import importlib.util, json, os, re, sys, time, urllib.request, urllib.error

spec=importlib.util.spec_from_file_location("v2","20260730_lowcost_memory_harness_v2.py")
v2=importlib.util.module_from_spec(spec); spec.loader.exec_module(v2)
spec2=importlib.util.spec_from_file_location("pb","20260730_AX7_pilot_benchmark.py")
# pilot module executes main() only under __main__; import is safe
pb=importlib.util.module_from_spec(spec2); spec2.loader.exec_module(pb)

FIX=open("20260728_NMC_fixture_synthetic.txt").read().strip()
P1=v2.INSTRUMENT.format(fixture=FIX)+"\nInclude the specific energy computed from the cycle-5 capacity."
FLOOR_SYS=v2.FLOOR_CACHE+"\n"+v2.SYS_COMPACT
MIN_SYS=v2.SYS_COMPACT
N=5; STOP_EACH=2.00

def openai_call(sys_txt,user,key,model):
    payload={"model":model,"max_tokens":1600,
             "messages":[{"role":"system","content":sys_txt},{"role":"user","content":user}]}
    req=urllib.request.Request("https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r: resp=json.load(r)
    ch=resp["choices"][0]
    u=resp.get("usage",{})
    cost=(u.get("prompt_tokens",0)*2.5+u.get("completion_tokens",0)*10)/1e6
    return ch["message"]["content"] or "", ch.get("finish_reason"), u, cost

def gemini_call(sys_txt,user,key,model):
    payload={"systemInstruction":{"parts":[{"text":sys_txt}]},
             "contents":[{"role":"user","parts":[{"text":user}]}],
             "generationConfig":{"maxOutputTokens":1600}}
    url=f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    req=urllib.request.Request(url,data=json.dumps(payload).encode(),
        headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r: resp=json.load(r)
    cand=resp.get("candidates",[{}])[0]
    txt="".join(p.get("text","") for p in cand.get("content",{}).get("parts",[]))
    um=resp.get("usageMetadata",{})
    u={"prompt_tokens":um.get("promptTokenCount",0),"completion_tokens":um.get("candidatesTokenCount",0)}
    cost=(u["prompt_tokens"]*1.25+u["completion_tokens"]*5)/1e6
    return txt, cand.get("finishReason"), u, cost

def resolve_model(provider,key):
    tries={"openai":["gpt-4o","gpt-5-chat-latest","gpt-4-turbo","gpt-4o-mini"],
           "gemini":["gemini-3.1-pro-preview","gemini-3.1-flash","gemini-2.5-flash","gemini-2.0-flash"]}[provider]
    fn=openai_call if provider=="openai" else gemini_call
    for m in tries:
        try:
            txt,fin,u,c=fn("Reply with the single word OK.","ping",key,m)
            return m,c
        except urllib.error.HTTPError as e:
            print(f"  [{provider}] {m}: HTTP {e.code}")
        except Exception as ex:
            print(f"  [{provider}] {m}: {str(ex)[:80]}")
    return None,0.0

def score(txt):
    row={"text":txt}
    s=pb.score_call("P1","x",row)
    return {"A1":s["A1"],"A2":round(s["A2"],3),"A4":round(s["A4"],3),"nc":s.get("_nc",0)}

def main():
    keys={}
    for name,env in (("openai","envs/openai.env"),("gemini","envs/gemini.env")):
        for ln in open(env):
            if "=" in ln and not ln.startswith("#"):
                keys[name]=ln.strip().split("=",1)[1]
    out=open("20260730_F7_crossengine_ledger.jsonl","a")
    results={}
    for provider in ("openai","gemini"):
        key=keys.get(provider)
        if not key: print(f"[{provider}] no key"); continue
        model,c0=resolve_model(provider,key)
        if not model: print(f"[{provider}] NO MODEL RESOLVED — skipping"); continue
        spend=c0
        print(f"\n=== {provider} :: {model} ===")
        fn=openai_call if provider=="openai" else gemini_call
        for arm,sys_txt in (("FLOOR",FLOOR_SYS),("MINIMAL",MIN_SYS)):
            for t in range(N):
                if spend>=STOP_EACH: print(f"  [STOP] {provider} backstop ${spend:.3f}"); break
                try:
                    txt,fin,u,c=fn(sys_txt,P1,key,model)
                    spend+=c; sc=score(txt)
                    row={"provider":provider,"model":model,"arm":arm,"t":t,"fin":fin,
                         "scores":sc,"usage":u,"cost":round(c,5)}
                except urllib.error.HTTPError as e:
                    row={"provider":provider,"model":model,"arm":arm,"t":t,"fin":f"http_{e.code}",
                         "scores":{"A1":0,"A2":0,"A4":0,"nc":0},"usage":{},"cost":0.0,
                         "detail":e.read().decode()[:120].replace(key,"***")}
                except Exception as ex:
                    row={"provider":provider,"model":model,"arm":arm,"t":t,"fin":"net_error",
                         "scores":{"A1":0,"A2":0,"A4":0,"nc":0},"usage":{},"cost":0.0,
                         "detail":str(ex)[:100].replace(key,"***")}
                out.write(json.dumps({**row,"text_head":(row.get('detail') or txt[:200] if 'txt' in dir() else '')})+"\n"); out.flush()
                results.setdefault((provider,arm),[]).append(row["scores"])
                print(f"  {arm} t{t}: A1={row['scores']['A1']} A2={row['scores']['A2']} A4={row['scores']['A4']} fin={row['fin']} ${row['cost']:.4f}")
        print(f"  [{provider}] spend ${spend:.4f} of ${STOP_EACH} stop")
    out.close()
    print("\n=== F7 SUMMARY (mean per arm) ===")
    for (prov,arm),rows in sorted(results.items()):
        n=len(rows)
        print(f"  {prov:7s} {arm:8s} n={n}  bind={sum(r['A1'] for r in rows)/n:.2f}  "
              f"prov={sum(r['A2'] for r in rows)/n:.2f}  cal={sum(r['A4'] for r in rows)/n:.2f}")

if __name__=="__main__": main()
