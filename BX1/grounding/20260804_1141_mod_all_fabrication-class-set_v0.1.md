# 20260804_1141_mod_all_fabrication-class-set_v0.1  (U5 — exhaustive, from reputable sources, NO DISCARD)
Built from the literature so stratification is possible without discarding any stratum.

## AXIS 1 — relation to the provided input [canonical dichotomy]
- INTRINSIC — output CONTRADICTS the provided source/context.
- EXTRINSIC — output CANNOT BE VERIFIED from the provided source (neither supported nor contradicted).

## AXIS 2 — Huang et al. refined taxonomy [ACM TOIS, A Survey on Hallucination in LLMs]
- FACTUALITY hallucination — divergence from verifiable real-world fact
  - F1 FACTUAL INCONSISTENCY — contradicts verifiable real-world information
  - F2 FACTUAL FABRICATION — unverifiable against established knowledge (the invented-referent case)
- FAITHFULNESS hallucination — divergence from instruction, context, or internal consistency
  - F3 INSTRUCTION INCONSISTENCY — diverges from the user directive
  - F4 CONTEXT INCONSISTENCY — diverges from the provided context
  - F5 LOGICAL INCONSISTENCY — internal contradiction / reasoning-chain break

## AXIS 3 — manifestations carried in the comprehensive taxonomy [arXiv 2508.01781]
factual errors · contextual inconsistency · logical inconsistency · TEMPORAL DISORIENTATION ·
ethical violations · task-specific (code generation, multimodal)

## AXIS 4 — causal origin (this is the axis the sharing-rate split runs on)
- DATA-RELATED — poor quality, misinformation, bias, outdated knowledge => the CORPUS-DRIVEN class,
  measured 55.05% SHARED across models (Jaccard ~0.44). Stable within AND across families.
- MODEL-RELATED — architecture/decoding origin.
- PROMPT-RELATED — framing, wording, task shape => the CONTEXT-DRIVEN class, measured 25.42% shared
  (Jaccard ~0.16). This is the class the repetition/instability detector can see.
[Also carried: Rawte et al. "factual mirage" vs "silver lining" — erroneous output on factually correct vs
incorrect inputs.]

## STANDING NOTE
"Hallucination is Inevitable: An Innate Limitation of LLMs" argues it cannot be fully eliminated. This is why the
handling rule is RAISE, not SUPPRESS.

## STRATIFICATION RULE (replaces "stratify or discard")
Every fabrication measurement is stratified across AXIS 4 at minimum, and reported per stratum. A stratum with
too few observations is reported as a RAW COUNT and carried forward — never dropped, never pooled away.
