# LEAN7POF — Repair / Equivalence-Benchmark Plan v2
**Provenance:** 7POF v1 · 14 July 2026 · Opus. Supersedes RepairPlan_v1 (same day). Revision driver: recovered the broken-state bundle — a **prior directional LEAN-vs-FULL benchmark exists** (`benchmark_deconfounded.json`; `benchmark_results.json` empty) and it **changes the repair definition**.

---

## 0. Ground truth (recovered, not assumed)
The prior benchmark (Sonnet-5, n=2×3, heuristic axis detectors, **reconstructed** LEAN/FULL texts + reconstructed 7-axis rubric — owner-flagged) found:

| axis | LEAN | FULL | gap |
|---|---|---|---|
| reasoning-before-schema | 0.33 | 0.83 | **−0.50** |
| resource governance | 0.33 | 1.00 | **−0.67** |
| uncertainty handling | 0.17 | 0.67 | **−0.50** |
| continuity | 0.17 | 0.83 | **−0.66** (nominal in 1-shot) |
| team / phases | 0.50 | 0.67 | −0.17 |
| close-out | 0.67 | 0.83 | −0.16 |
| deliverable craft | 1.00 | 1.00 | 0.00 (only parity) |
| **cost** | **$0.0115** | **$0.0301** | **LEAN 2.6× cheaper** |

**Conclusion:** the current LEAN skeleton is **not equivalent** to FULL — it buys 2.6× cost saving by dropping exactly the governance layer this programme runs on. **So the repair is a skeleton-content fix, not a bigger stats run.** Equivalence is a *target to engineer toward*, not a formality to certify.

---

## 1. The repair (mechanism, grounded in a locked finding)
Your own ≥2σ-locked result: *"schema-carriage of disciplines outperforms no-framework; **naming a discipline triggers the behaviour** while a **structured slot quarantines it from the deliverable body**."* That is the exact tool for this gap. FULL recovers the six axes by spending 2.6× tokens on prose; LEAN can recover them by **naming them as compact schema slots** — behaviour triggered, tokens not spent on prose.

**Repair = fold six named governance slots into the LEAN skeleton** (delivered this turn: `LEAN_governance_slot_patch_v1`). Predicted effect: lift reasoning-first / resource-gov / uncertainty / close-out from ~0.2–0.5 toward FULL's 0.7–1.0, at a token cost far below FULL's prose (target: repaired-LEAN ≤ ~1.3× baseline-LEAN cost, still <FULL). Continuity and team/phases are **1-shot-nominal** — only a multi-turn task tests them substantively; deferred to the canonical run.

---

## 2. Then benchmark — two separate claims (unchanged discipline)
- **Quality → EQUIVALENCE via TOST** vs a pre-registered margin Δ (proposed Δ=0.5 on the reconstructed 0–1 axis scale; owner-tunable). Target ≥2σ on repaired-LEAN vs FULL per axis and aggregate.
- **Cost → SUPERIORITY, one-sided, target ≥4σ.** Deterministic (token meters). Repaired-LEAN cheaper than FULL is the expected ≥4σ headline (baseline already 2.6×; the patch adds little).
- **Kept strictly separate** (your explicit instruction): a quality *equivalence* is never reported as quality *superiority*; the superiority claim lives only on cost.
- **Proportionality:** n=5/cell; escalate to n=8 only on cells whose CI straddles ±Δ.

---

## 3. What blocks a *canonical* (vs directional) verdict — owner-gated
Recovered `Uncallable_and_Residual.md` names them exactly:
1. **Canonical LEAN skeleton + FULL 7POF prompt texts** — "NOT in context; benchmark used a reconstructed rubric." The directional run stands; a canonical verdict needs the real texts. *(Owner supplies, or authorises me to assemble FULL from the A/C/F PDFs in root — LEAN skeleton canonical text still owner-held.)*
2. **Rubric grading** replacing keyword detectors — human or Opus-graded; **top tier = Enrico** (ceiling problem).
3. **Multi-turn task** to test continuity substantively (1-shot makes it nominal).

---

## 4. Resources built in (this cycle) → see `ResourceScan_ImpactMap`
Harness upgraded with: **Message Batches (−50%)**, **prompt-caching** the FULL system prefix, **`count_tokens`** for exact cost, `error-codes` retry taxonomy, `data:statistical-analysis` for TOST/z/power. Reuse: 10-way concurrency, `fable_prompt_screen.py`, VZ reconciler. Deferred (own Team-Builder pass): the **Managed-Agents API** surface.

## 5. Build workflow
- **B1 (done this turn):** governance-slot patch + runnable `benchmark_harness.py`.
- **B2 (API, cheap ~$0.36):** directional patch-demonstration — baseline-LEAN vs **repaired-LEAN** vs FULL on Sonnet-5, same heuristic detectors, to show the patch lifts the six axes at ~LEAN cost. Directional, not canonical.
- **B3 (API, gated):** canonical run once owner supplies §3 items — Opus primary + Fable screened, cached+batched, TOST + cost-superiority.
- **B4:** recompile plan if B2 changes the patch.
- **B5:** fold locked verdict into A / K / guard-SKILL / Z.

## 6. Cost prediction
- **B2 directional demo:** ~$0.30–0.50 API (prior identical run was $0.36).
- **B3 canonical:** ~$4–10 with batches (8 classes × 2 arms × n5, Opus, FULL-prefix cached); +$1–3 Fable sub-arm. Holds <$20 with batches or a 6-class trim (proportionality).
- **OCSUL:** ~£0.10–0.30 / £5.00 per run turn. **CSUL:** a full canonical run ≈30% — needs its own budget.

## 7. Residual
Repair artifact + harness delivered. B2 demo runs this turn if budget allows, else handed off runnable. B3 canonical gated on the three §3 owner items. Drive write still broken → deliver locally.

*Repair Plan v2 · 7POF v1 · 14 July 2026 · LEAN≠FULL today; repair = named governance slots; equivalence engineered then TOST-tested, cost-superiority separate.*
