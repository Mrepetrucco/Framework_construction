# LEAN7POF — Governance-Slot Patch v1 (the repair)
**Provenance:** 7POF v1 · 14 July 2026 · Opus. Drop-in fragment to fold into the canonical LEAN skeleton. Closes the six governance-axis gaps found in the directional benchmark by **naming each discipline as a compact slot** (locked finding: naming triggers the behaviour; a structured slot quarantines it from the deliverable body). Target: recover axes toward FULL's 0.7–1.0 at ≤~1.3× baseline-LEAN token cost.

> **Design rule:** these are *carriage slots*, not prose. Each is one line or a short schema key. The deliverable body stays clean; governance rides in a fenced header/footer block so it never bloats the answer. This is what lets LEAN recover FULL's rigor without FULL's 2.6× cost.

## Patch — append to the LEAN skeleton system prompt
```
## Governance slots (emit around every deliverable; keep terse)
OPEN (before work):
- reasoning_first: 1–2 lines of approach BEFORE any schema/output. Name the method, not the answer.
- team_phases: one line — roster + phase sequence proportional to task size.
- uncertainty: genuine unknowns as a numbered plain-text list; do not proceed past a blocking one. If intake resolves it, commit and flag the assumption inline. (Never a picker.)

BODY: the deliverable. No governance prose here.

CLOSE (after work):
- resource_governance: ledger line — CSUL(≥1% or 4%), OCSUL(£, else £0.00), API($, else $0.00). Zblock v1.0+.
- continuity: reference the prior anchor/decision this builds on (Artifact/Assumptions-Ledger id). In 1-shot, state "no prior anchor".
- closeout: residual + next action; surface any pending Artifact-A / reconciliation item. No passive routing.
```

## Why each slot (axis it repairs)
| slot | axis repaired | prior LEAN | FULL | mechanism |
|---|---|---|---|---|
| `reasoning_first` | reasoning-before-schema | 0.33 | 0.83 | forces reasoning to precede output; ~2 lines |
| `resource_governance` | resource governance | 0.33 | 1.00 | mandatory ledger line; schema-checked |
| `uncertainty` | uncertainty handling | 0.17 | 0.67 | numbered-question convention |
| `continuity` | continuity | 0.17 | 0.83 | explicit anchor-ref (substantive only multi-turn) |
| `team_phases` | team / phases | 0.50 | 0.67 | one-line roster+phases |
| `closeout` | close-out | 0.67 | 0.83 | residual + next, no passive routing |

## Token budget (why it stays LEAN)
The six slots are ~8–14 lines of *carriage*, not the paragraphs FULL spends. Predicted add: ~120–200 output tokens/call over baseline-LEAN (~752) → ~900–950, i.e. **~1.25× baseline-LEAN, still well under FULL's ~1960**. Cost-superiority vs FULL is preserved by construction; equivalence-on-quality is the empirical question B2/B3 test.

## Validation hooks (for the harness)
Each slot maps to one heuristic detector already in the harness (`reasoning_first`, `resource_gov`, `uncertainty`, `continuity`, `team_phases`, `closeout`) — so a repaired-LEAN run is directly comparable to the recovered baseline numbers.

## Caveats
- Continuity/team_phases are **1-shot-nominal**; real test needs a multi-turn task.
- This patches a *reconstructed* LEAN skeleton until the owner supplies the canonical LEAN text; fold into the canonical text when provided (slots transfer verbatim).

*Patch v1 · 7POF v1 · 14 July 2026 · six named slots; recover governance at ~1.25× LEAN cost, <FULL.*
