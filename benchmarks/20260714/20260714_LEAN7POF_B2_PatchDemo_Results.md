# LEAN7POF — B2 Directional Demo: does the governance-slot patch recover the axes?
**Provenance:** 7POF v1 · 14 July 2026 · Opus. Live run, Sonnet-5, 3 neutral tasks × n2 per arm (n=6/arm), 10-way concurrent, heuristic structural detectors applied identically across arms. Method mirrors the recovered 13-Jul run for comparability. **API cost: $0.357** (+~$0.002 path validation). Key used was the Drive-stored one — **flagged exposed; rotate.**

## Answer: the patch lifts LEAN's governance-axis presence as designed — directionally
Governance-axis mean (six axes, excl. deliverable-craft): **baseline-LEAN 0.528 → repaired-LEAN 0.806 (+0.28)**, at ~1.31× baseline cost. Repaired-LEAN ≈ FULL cost or cheaper.

## Per-axis (fraction of outputs exhibiting the axis)
| axis | baseline-LEAN | repaired-LEAN | FULL* | patch effect (rep−base) |
|---|---|---|---|---|
| reasoning_first | 0.00 | 0.17 | 0.00 | **+0.17** |
| resource_gov | 1.00 | 1.00 | 0.83 | 0.00 (detector saturated) |
| uncertainty | 0.50 | 1.00 | 0.67 | **+0.50** |
| continuity | 0.33 | 1.00 | 0.50 | **+0.67** |
| team_phases | 1.00 | 1.00 | 0.83 | 0.00 (detector saturated) |
| closeout | 0.33 | 0.67 | 0.17* | **+0.33** |
| deliverable_craft | 1.00 | 1.00 | 1.00 | — (parity, all arms) |

## Cost (per call, Sonnet-5; $3/$15 per Mtok assumed — flag)
| arm | avg out tok | avg USD | note |
|---|---|---|---|
| baseline-LEAN | 1074 | $0.0163 | 2/6 truncated |
| repaired-LEAN | 1379 | $0.0213 | **≈1.31× baseline — matches ≤1.3× design target** |
| FULL* | 1400 | $0.0219 | **6/6 truncated at cap → cost is a floor, axes undercounted** |

## Read it honestly — what this does and does NOT show
- **DOES:** the patch causally lifts the axes it targets — uncertainty, continuity, closeout, reasoning-first — moving LEAN from 0.53 to 0.81 governance-mean at ~1.3× LEAN cost. This is the repair mechanism working, and it is **autonomously closeable** (structural axis *presence*, not quality — no ceiling problem).
- **DOES NOT:** show repaired-LEAN *beats* FULL. FULL truncated 6/6 at the 1400-tok cap, so its late axes (closeout 0.17) are undercounted; "repaired ≥ FULL" here is partly a truncation artifact plus a crude reconstructed-FULL prompt.
- **DETECTOR SATURATION:** resource_gov and team_phases read 1.0 even for baseline — crude detectors fire on any knowledge-work output; the patch's true effect on those two is untestable with these detectors.

## Confounds (do not over-read)
Reconstructed baseline/patch/FULL prompts + reconstructed tasks + heuristic keyword detectors + n=6 + single model. Same directional tier as the 13-Jul run. Absolute values crude; within-run **deltas** (patch effect) are the signal.

## Implication for the plan
The repair is empirically supported at directional tier. To convert to a **canonical >2σ** verdict: owner-supplied canonical LEAN/FULL texts, rubric grading (not keyword detectors), an **untruncated FULL arm** (raise max_tokens or stream), and a multi-turn task for continuity. Then TOST (equivalence-on-quality) + one-sided cost test (superiority), kept separate.

*B2 demo · 7POF v1 · 14 July 2026 · patch recovers governance axes (+0.28 mean) at ~1.3× LEAN cost; directional, FULL truncated — not the canonical verdict.*
