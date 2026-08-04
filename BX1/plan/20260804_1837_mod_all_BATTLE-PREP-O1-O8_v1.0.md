# 20260804_1837_mod_all_BATTLE-PREP-O1-O8_v1.0
Live-Fact-Sourced structure for the five retained Group-4 battle items. Sourcing status is marked per item —
O3 and O8 are REASONED-ONLY this turn and must not be presented as evidence-backed.

## O1 — W CLASS (interior mechanism-edit: activation steering / fine-tune) · SOURCED
The literature is close to decisive AGAINST admitting W into the SOG:
- Steering shows high variability, POOR OUT-OF-DISTRIBUTION GENERALIZATION, and frequent ineffectiveness; some
  concepts are simply UNSTEERABLE. Effectiveness is task-type-limited and degrades when steering multiple
  behaviours at once.
- SAE-feature steering performs COMPARABLY TO RANDOM NOISE (1-4% compliance shift over random); the most
  effective jailbreaking features correspond to BENIGN concepts with poor cross-prompt generalisation, making
  systematic safety monitoring "practically infeasible".
- Adversarial robustness: directional robustness drops by up to 64 percentage points under attack; the OPTIMAL
  LAYER SHIFTS drastically; adversarial training only partially remedies and fails to correct layer selection.
- Activation steering can INDUCE EMERGENT MISALIGNMENT and erode safety alignment; narrow finetuning leaves
  readable traces in activation differences.
- Multiple independent groups find steering does NOT beat simple prompting baselines.
- Single-turn evaluations SYSTEMATICALLY OVERESTIMATE steering effectiveness; trait expression is unstable
  across multi-turn even without intervention.
**BATTLE THESIS (ours):** W fails BX1's own admission test on three counts — it is not externally adjudicable,
its guarantee does not survive distribution shift, and it degrades the thing it edits. Fable must either produce
a class of obligation that ONLY W can carry, or concede W stays excluded.
**COUNTER TO PREPARE FOR:** Anthropic uses steering to monitor/mitigate persona traits in production, so
"unusable" is too strong. Our answer must distinguish MONITORING (read-only probe, admissible) from CONTROL
(write intervention, inadmissible).

## O2 — DELTA SALVAGE · SOURCED — AND THE VERDICT FLIPS TO PARTIAL SALVAGE
- Self-consistency is "NEITHER NECESSARY NOR SUFFICIENT" for veracity: models produce CONSISTENTLY hallucinated
  facts. This is exactly our measured 5/5 identical confabulation.
- Semantic entropy explicitly FAILS when the model returns identical responses across samples.
- Standalone semantic entropy measured at 0.5951 AUROC on one 2026 benchmark — barely above chance.
- BUT as ONE OF 31 COMPLEMENTARY FEATURES it contributes +0.2298 AUROC (0.8249 combined). **That is the salvage:
  Delta is dead as a STANDALONE VERDICT and alive as a FEATURE.**
- Access constraint: SE/logprob methods CANNOT run on API-only reasoning models that withhold output
  probabilities — so Delta is unavailable exactly where BX1 mostly operates.
**BATTLE THESIS (ours):** the earlier "Delta is fully dead" ruling was over-hardened. Correct position: Delta is
inadmissible as a verdict, admissible as one input to a multi-feature detector, and unavailable on closed APIs.
**PREDICT Fable ARGUES:** that a feature contributing to an ensemble is still self-attestation. Our counter: the
ensemble's OTHER 30 features break the self-reference, and AUROC gain is measured, not asserted.

## O3 — CLASS-SET {A,M,R,I,P} EXHAUSTIVENESS · REASONED ONLY, NOT SOURCED
No literature pull this turn. The demand stands as previously framed: produce the GENERATING PARTITION or
declare the set an inventory. Prior rounds already showed the original trichotomy failed for lacking one, and
that two classes (Incentive, Protocol) were invisible from the output boundary.
**BATTLE THESIS:** ask Fable to derive the partition from the dataflow of a governed call rather than from
introspection, since that is the method that beat the trichotomy last time.

## O7 — CONFORMAL LAYER (X5) BUILDABILITY · SOURCED — AND THE OBJECTION IS ANSWERED
The blocking objection was "X5 needs a calibration corpus that does not exist". The literature answers it:
- Split conformal's guarantee is MARGINAL — realized coverage for a SINGLE calibration set varies substantially;
  at n=50 the empirical coverage distribution is broad, and it remains notably wide even at n=500.
- **Small Sample Beta Correction (SSBC)** restores reliable coverage at SMALL n: violations hit the design target
  (~0.047 at n=50, ~0.095 at n=100), and a calibration set of **n=47** gave coverage comparable to n=4337 — a 92x
  size difference with both reliable.
- PAC-style guarantees add a confidence parameter delta and target a MINIMUM acceptable coverage rather than an
  expected one — relevant precisely when n is small.
- Caveat to carry: macro/class-conditional coverage degrades as the SMALLEST GROUP shrinks, inflating set size.
  Since our fabrication classes are stratified (corpus-driven vs context-driven), the smallest stratum governs.
**BATTLE THESIS (ours):** X5 is buildable at owner data volume — n~50 per stratum with SSBC, not thousands. The
real constraint is not corpus size but STRATUM balance.

## O8 — PROVENANCE-DAG ALGEBRA · REASONED ONLY, NOT SOURCED
Candidate formalisms to put to Fable (unsourced this turn, flag as such): subjective logic, Dempster-Shafer,
probabilistic argumentation frameworks, and Bayesian networks over the provenance graph. The prior withdrawal
was because meet-semantics cannot represent corroboration and has no length-sensitivity; all four candidates can
represent both, so the question is which is FITTABLE from ~0 resolved chains.
**BATTLE THESIS:** is discovery feasible at our data volume, or is the DAG substrate-only permanently? Note the
O7 result cuts here too — if SSBC makes n~50 sufficient for coverage, the same order of magnitude may make a
2-parameter composition rule fittable, which would reopen the algebra.

## CROSS-CUTTING (use in every arm)
Prior external evidence retained: co-error convergence ~60% and RISING with capability; corpus-driven fabrication
55% shared vs context-driven 25%; fabrication is prompt-induced. Any Fable argument resting on model independence
must clear that bar first.
