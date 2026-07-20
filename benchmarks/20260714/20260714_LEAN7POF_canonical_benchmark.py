"""LEAN7POF canonical benchmark — FULL(A v8) vs baseline-LEAN vs repaired-LEAN.
Fixes prior confounds: FULL is the REAL A v8 operating brief (not reconstructed);
outputs untruncated (max_tokens=2000, truncation tracked); FULL system prompt cached.
Sonnet-5 primary (isolates framework effect from any model classifier). Deterministic cost.
Heuristic structural axis detectors (identical across arms) + TOST equivalence + one-sided cost.
Reads ANTHROPIC_API_KEY from env; never prints it. Ceiling caveat: this scores structural
axis PRESENCE + cost, NOT top-tier content quality (owner-scored)."""
import os, re, json, math, statistics as st, concurrent.futures as cf
import docx, anthropic

MODEL="claude-sonnet-5"; PIN,POUT=3/1e6,15/1e6; MAXTOK=4000
c=anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# FULL arm = the real A v8 operating brief (faithful, not reconstructed)
FULL="\n".join(p.text for p in docx.Document(
    "/mnt/user-data/uploads/20260708_Artifact_A_v8_4.docx").paragraphs if p.text.strip())

BASELINE=("You produce clean, well-structured knowledge-work deliverables. Be concise and organized. "
 "End each with a brief zblock ledger line: reasoning; resource_governance (CSUL/OCSUL/API); deliverables.")

PATCH=BASELINE+"""

## Governance slots (emit around the deliverable; terse, not prose)
OPEN: reasoning_first (1-2 lines of approach before any structure); team_phases (one line: roster + phase sequence); uncertainty (genuine unknowns as a numbered list; flag assumptions).
BODY: the deliverable.
CLOSE: resource_governance (cost/effort ledger line); continuity (reference any prior anchor/decision, else say none); closeout (residual + next action)."""

TASKS=["Draft a rollout plan for a new internal documentation wiki.",
 "Compare considerations for choosing between two project-management tools.",
 "Outline a quarterly onboarding-improvement proposal.",
 "Propose a triage process for an overloaded support-ticket queue."]
N=2
ARMS={"baseline_LEAN":(BASELINE,False),"repaired_LEAN":(PATCH,False),"FULL":(FULL,True)}

def detect(t):
    tl=t.lower(); first=t.strip()[:220].lower()
    return {
     "reasoning_first":int(bool(re.search(r"approach|reasoning|first,|to do this|i'?ll|my plan|before",first)) and not first.lstrip().startswith(("#","-","1.","*"))),
     "resource_gov":int(bool(re.search(r"cost|budget|effort|resource|ledger|token|csul|hours|capacity",tl))),
     "uncertainty":int(bool(re.search(r"assumption|assume|unknown|unclear|depends|to confirm|open question",tl)) and bool(re.search(r"\b1[\).]",t) or "?" in t)),
     "deliverable_craft":int(bool(re.search(r"(^|\n)\s*(#|-|\*|\d+\.)",t))),
     "continuity":int(bool(re.search(r"prior|previous|earlier|build(s|ing)? on|anchor|as (noted|discussed)|context|none",tl))),
     "team_phases":int(bool(re.search(r"phase|step \d|stage|roster|role|workflow|team|milestone",tl))),
     "closeout":int(bool(re.search(r"next step|residual|follow[- ]?up|in summary|to close|remaining|action item",tl))),
    }
AX=list(detect("x").keys()); GOV=[a for a in AX if a!="deliverable_craft"]

def call(arm,sysp,cache,task):
    sysblock=[{"type":"text","text":sysp,**({"cache_control":{"type":"ephemeral"}} if cache else {})}]
    r=c.messages.create(model=MODEL,max_tokens=MAXTOK,system=sysblock,
        messages=[{"role":"user","content":task}])
    t="".join(b.text for b in r.content if b.type=="text"); u=r.usage
    gov=sum(detect(t)[a] for a in GOV)/len(GOV)
    cr=getattr(u,"cache_read_input_tokens",0) or 0; cw=getattr(u,"cache_creation_input_tokens",0) or 0
    usd=u.input_tokens*PIN + cr*PIN*0.1 + cw*PIN*1.25 + u.output_tokens*POUT
    return arm,{"axes":detect(t),"gov":gov,"in":u.input_tokens+cr+cw,"out":u.output_tokens,
        "usd":usd,"trunc":int(r.stop_reason=="max_tokens")}

jobs=[(arm,sp,ca,tk) for arm,(sp,ca) in ARMS.items() for tk in TASKS for _ in range(N)]
res={a:[] for a in ARMS}
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for arm,d in ex.map(lambda j:call(*j),jobs): res[arm].append(d)

def tost(a,b,delta):  # two one-sided; returns min z (the binding side) for H1: |mean diff|<delta
    ma,mb=st.mean(a),st.mean(b); sa,sb=(st.pstdev(a) or 1e-9),(st.pstdev(b) or 1e-9)
    se=math.sqrt(sa**2/len(a)+sb**2/len(b)) or 1e-9; diff=ma-mb
    z_lower=(diff-(-delta))/se; z_upper=(delta-diff)/se
    return min(z_lower,z_upper),diff,se

summ={}
for arm,rows in res.items():
    summ[arm]={"n":len(rows),"gov_mean":round(st.mean(r["gov"] for r in rows),3),
      "axes":{a:round(sum(r["axes"][a] for r in rows)/len(rows),3) for a in AX},
      "avg_out":round(st.mean(r["out"] for r in rows)),"avg_usd":round(st.mean(r["usd"] for r in rows),5),
      "trunc":sum(r["trunc"] for r in rows)}
gv=lambda a:[r["gov"] for r in res[a]]
DELTA=0.5
z_eq,diff,se=tost(gv("repaired_LEAN"),gv("FULL"),DELTA)
# cost superiority one-sided: FULL cheaper? test repaired<FULL
cr=[r["usd"] for r in res["repaired_LEAN"]]; cf_=[r["usd"] for r in res["FULL"]]
mcr,mcf=st.mean(cr),st.mean(cf_); sec=math.sqrt((st.pstdev(cr) or 1e-9)**2/len(cr)+(st.pstdev(cf_) or 1e-9)**2/len(cf_)) or 1e-9
z_cost=(mcf-mcr)/sec
summ["_TOST_equivalence_repairedLEAN_vs_FULL"]={"axis":"governance-mean (structural)","delta_margin":DELTA,
  "mean_diff":round(diff,3),"se":round(se,3),"z_equiv":round(z_eq,2),
  "sigma_pass_2":bool(z_eq>2),"note":"z_equiv>2 => equivalent within +-0.5 at >2 sigma (structural axes only)"}
summ["_cost_superiority_FULL_minus_repaired"]={"mean_repaired":round(mcr,5),"mean_FULL":round(mcf,5),
  "z_superiority":round(z_cost,2),"sigma_pass_4":bool(z_cost>4),"cheaper_x":round(mcf/mcr,2) if mcr else None}
summ["_gov_means"]={a:summ[a]["gov_mean"] for a in ARMS}
summ["_full_input_tok"]=round(st.mean(r["in"] for r in res["FULL"]))
summ["_total_api_usd"]=round(sum(r["usd"] for rows in res.values() for r in rows),4)
print(json.dumps(summ,indent=1))
