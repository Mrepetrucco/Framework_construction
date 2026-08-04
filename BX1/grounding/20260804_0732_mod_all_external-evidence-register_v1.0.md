# 20260804_0732_mod_all_external-evidence-register_v1.0
Live Fact Sourcing, retrieved 4 Aug 2026. Every item below is EXTERNAL — not model testimony — and is therefore
admissible where cross-model agreement is not.

## E1 CROSS-MODEL ERROR CORRELATION (this is the single most consequential finding for BX1)
- ICML 2025, 350+ LLMs: when two models both err they converge on the SAME wrong answer ~60% of the time.
- Error correlation RISES with capability, across architectures AND providers. Provider diversity does NOT restore
  independence; scale makes it worse.
- July 2026 audit, 265,000 samples: agreement-correctness correlation Spearman rho 0.20-0.59 (weak). The most
  agreement-prone model had the LEAST trustworthy agreement signal.

## E2 HALLUCINATION OVERLAP IS CLASS-DEPENDENT
- HalluScore within-family overlap: Claude Opus/Sonnet 61.6%, Qwen 69.8%, DeepSeek 65.8%.
- Rust-crate study: CORPUS-DRIVEN (pre-training-gap) fabrications 55.05% shared, Jaccard ~0.44;
  CONTEXT-DRIVEN fabrications only 25.42% shared, Jaccard ~0.16.
- Citation-fabrication audit (10 models, 7 providers): rates 11.4-56.8%; NO model spontaneously cites unprompted
  (fabrication is PROMPT-INDUCED, not intrinsic); >=3-model consensus 95.6% accuracy (5.8x); within-prompt
  repetition >=2 gives 88.9%.

## E3 DEPLOYMENT/EXPERIMENT METHOD
- Canonical order: SHADOW -> CANARY -> A/B -> ramp. Shadow validates mechanics under load; it is NOT a causal estimate.
- A/A test FIRST to expose setup bias. Primary metric fixed BEFORE the run and is the ship/kill metric.
- Interleaving is the efficient alternative for SELECTION problems (mixed outputs in one response).
- Named malpractice: post-hoc slicing until a segment reaches significance.
- Post-stratification reduces variance on heavy-tailed metrics without extra traffic.

## E4 ROUTER ROBUSTNESS (retrieved previous session, retained)
- Training-free routers most adversarially robust; learned routers weakest. Conflict-free policy-language DSL for
  ML predicates has published precedent. JSON/tool-layer attacks precede the model and compose with model-side
  safeguards.
