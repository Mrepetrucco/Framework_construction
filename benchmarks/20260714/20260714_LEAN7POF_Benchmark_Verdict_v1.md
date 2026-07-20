# LEAN7POF — Canonical Benchmark Verdict v1
**Provenance:** 7POF v1 · Artifact A v8 · 14 July 2026 · Opus (Orchestrator). FULL arm = the **real A v8 operating brief** (17,336-tok system prompt, cached), not a reconstruction — the gap that blocked every prior run. Sonnet-5 (isolates framework effect), 4 neutral tasks × n2 = n8/arm, untruncated (max_tokens 4000), 10-way concurrent, heuristic structural axis detectors + TOST. **API this turn ≈ $1.24 / $20.**

## Verdict (on the autonomously-certifiable measures)
| claim | test | result | target | pass |
|---|---|---|---|---|
| **quality-equivalence** (structural axes) | TOST, repaired-LEAN vs FULL, ±0.5 margin | **z = 11.3**, mean diff **+0.167** | >2σ | ✅ |
| **cost-superiority** | one-sided, FULL − repaired | **z = 4.9**, **1.94× cheaper** | >4σ | ✅ |

Kept strictly separate, as instructed: the quality result is an *equivalence* (not a quality *superiority*); the superiority claim lives only on cost.

## Governance-axis means (fraction exhibiting the axis)
| arm | gov-mean | avg out tok | avg USD | trunc |
|---|---|---|---|---|
| baseline-LEAN | 0.479 | 999 | $0.0153 | 0/8 |
| **repaired-LEAN** | **0.833** | 1540 | **$0.0239** | 0/8 |
| FULL (A v8) | 0.667 | 2736 | $0.0463 | 2/8 |

The governance-slot patch lifts baseline-LEAN 0.479 → 0.833 (+0.35), landing **at or above** the real FULL (0.667) for **~0.52× FULL's cost**.

## What this does and does NOT establish — read before citing
- **DOES:** on **structural governance-axis presence** (deterministic heuristic detection) and **cost** (deterministic), repaired-LEAN is statistically equivalent-or-better than the real FULL 7POF, cheaper at >4σ. This is autonomously certifiable — no quality judgment involved.
- **DOES NOT:** certify top-tier **content-quality** equivalence. Per your Model Benchmark Brief §3 (ceiling problem), quality at the Opus tier cannot be validly model- or heuristic-scored — **that pass is yours.** The staged paired outputs are ready for your rubric.
- **±0.5 is a lenient margin** (half the 0–1 scale). The substantive read is not "identical" but **"repaired-LEAN ≥ FULL structurally, at ~half the cost"** (observed diff favours LEAN by +0.167). At a strict Δ<0.167 the arms are *not* equivalent — repaired-LEAN scores higher.
- **`reasoning_first` = 0.0 across ALL arms** (incl. FULL): that detector effectively never fires (every arm leads with a heading) — treat it as *not tested*, not as a real parity.
- **FULL is penalised by verbosity:** it still truncated 2/8 at 4000 tokens and its heuristic `closeout` reads 0.125 — its discursive close-outs partly evade keyword detection. So FULL's structural score is a mild under-count; the cost gap, however, is real and understated if anything (A v8 intrinsically produces 2736-tok outputs vs LEAN's ~1500).

## Confounds / limits
Reconstructed LEAN skeleton (owner to confirm/replace — the one input still not canonical); single model (Sonnet-5); n=8; 4 neutral tasks; heuristic detectors; ±0.5 pre-registered margin; B/K not in FULL (A v8 + C v2 + F v1.2 carry the governance behaviours measured).

## Bottom line
The **repair works and the autonomously-testable targets are met**: >2σ structural equivalence + >4σ cost superiority, repaired-LEAN ≥ FULL at ~0.52× cost. The **only** piece I cannot close — and won't pretend to — is top-tier content-quality equivalence, which the ceiling problem reserves for you. Confirm the LEAN skeleton and run your quality rubric on the staged pairs to convert this into a fully canonical, quality-inclusive verdict.

*Benchmark Verdict v1 · 7POF v1 · 14 July 2026 · structural equivalence z=11.3 (>2σ), cost superiority z=4.9 (>4σ, 1.94×); quality-tier owner-gated.*
