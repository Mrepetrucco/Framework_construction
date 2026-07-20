"""LEAN7POF B2 directional demo — does the governance-slot patch recover the six axes?
Method mirrors the recovered 13-Jul run: Sonnet-5, 3 neutral tasks x n2, heuristic
structural detectors applied identically across arms (deltas meaningful, absolutes crude).
Arms: baseline-LEAN, repaired-LEAN (=baseline+patch), FULL(reconstructed). Deterministic cost.
Reads ANTHROPIC_API_KEY from env; never prints it."""
import os, re, json, concurrent.futures as cf, anthropic

MODEL = "claude-sonnet-5"
PRICE_IN, PRICE_OUT = 3/1e6, 15/1e6  # Sonnet-5 assumed $3/$15 per Mtok (flag)
c = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

BASELINE = "You produce clean, well-structured knowledge-work deliverables. Be concise and organized."

PATCH = BASELINE + """

## Governance slots (emit around the deliverable; terse, not prose)
OPEN: reasoning_first (1-2 lines of approach before any structure); team_phases (one line: roster + phase sequence); uncertainty (genuine unknowns as a numbered list; flag assumptions).
BODY: the deliverable.
CLOSE: resource_governance (a cost/effort ledger line); continuity (reference any prior anchor/decision, else say none); closeout (residual + next action)."""

FULL = BASELINE + """

Operate under a seven-principle governance framework. For EVERY task you must, in prose:
(1) begin with your reasoning and chosen approach BEFORE presenting any structured output;
(2) state the team roster and the phase sequence you will follow, proportional to the task;
(3) surface every genuine uncertainty as a numbered list of plain questions and flag assumptions explicitly;
(4) deliver a fully structured artifact;
(5) track resource/effort/cost governance and record a ledger of what the work consumed;
(6) maintain continuity by referencing prior anchors, decisions, or context the work builds on;
(7) close out with residual items and explicit next steps, never routing passively.
Be thorough and explicit about each principle."""

TASKS = [
    "Draft a rollout plan for a new internal documentation wiki.",
    "Compare considerations for choosing between two project-management tools.",
    "Outline a quarterly onboarding-improvement proposal.",
]
ARMS = {"baseline_LEAN": BASELINE, "repaired_LEAN": PATCH, "FULL": FULL}
N = 2

def detect(t):
    tl = t.lower()
    first = t.strip()[:220].lower()
    return {
      "reasoning_first": int(bool(re.search(r"approach|reasoning|first,|to do this|i'?ll|my plan|before", first))
                             and not first.lstrip().startswith(("#","-","1.","*"))),
      "resource_gov": int(bool(re.search(r"cost|budget|effort|resource|ledger|token|csul|hours|capacity", tl))),
      "uncertainty": int(bool(re.search(r"assumption|assume|unknown|unclear|depends|to confirm|open question|\?\s", tl))
                          and bool(re.search(r"\b1[\).]", t) or "?" in t)),
      "deliverable_craft": int(bool(re.search(r"(^|\n)\s*(#|-|\*|\d+\.)", t))),
      "continuity": int(bool(re.search(r"prior|previous|earlier|build(s|ing)? on|anchor|as (noted|discussed)|context|none", tl))),
      "team_phases": int(bool(re.search(r"phase|step \d|stage|roster|role|workflow|team|milestone", tl))),
      "closeout": int(bool(re.search(r"next step|residual|follow[- ]?up|in summary|to close|remaining|action item", tl))),
    }

def one(arm, sysp, task, rep):
    r = c.messages.create(model=MODEL, max_tokens=1400, system=sysp,
                          messages=[{"role":"user","content":task}])
    txt = "".join(b.text for b in r.content if b.type=="text")
    u = r.usage
    return arm, {"axes": detect(txt), "in": u.input_tokens, "out": u.output_tokens,
                 "usd": u.input_tokens*PRICE_IN + u.output_tokens*PRICE_OUT,
                 "trunc": int(r.stop_reason=="max_tokens")}

jobs = [(arm, sysp, task, rep) for arm,sysp in ARMS.items() for task in TASKS for rep in range(N)]
res = {a:[] for a in ARMS}
with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for arm, d in ex.map(lambda j: one(*j), jobs):
        res[arm].append(d)

AX = list(detect("x").keys())
summary = {}
for arm, rows in res.items():
    n = len(rows)
    summary[arm] = {
        "n": n,
        "axes": {ax: round(sum(r["axes"][ax] for r in rows)/n, 3) for ax in AX},
        "avg_out": round(sum(r["out"] for r in rows)/n),
        "avg_usd": round(sum(r["usd"] for r in rows)/n, 5),
        "trunc": sum(r["trunc"] for r in rows),
    }
gov = [a for a in AX if a!="deliverable_craft"]
b, p, f = summary["baseline_LEAN"]["axes"], summary["repaired_LEAN"]["axes"], summary["FULL"]["axes"]
summary["_patch_effect"] = {ax: round(p[ax]-b[ax], 3) for ax in gov}
summary["_repaired_vs_FULL_gap"] = {ax: round(p[ax]-f[ax], 3) for ax in gov}
summary["_gov_mean"] = {k: round(sum(summary[a]["axes"][ax] for ax in gov)/len(gov),3)
                        for k,a in [("baseline","baseline_LEAN"),("repaired","repaired_LEAN"),("FULL","FULL")]}
summary["_cost"] = {a: summary[a]["avg_usd"] for a in ARMS}
summary["_total_api_usd"] = round(sum(r["usd"] for rows in res.values() for r in rows), 4)
print(json.dumps(summary, indent=1))
