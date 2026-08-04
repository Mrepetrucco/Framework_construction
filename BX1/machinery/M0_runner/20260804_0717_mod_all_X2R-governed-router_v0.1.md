# 20260804_0717_mod_all_X2R-governed-router_v0.1
Owner ruling: the exemplar catalogue is REINSTATED and essential; the defect was the UNGOVERNED router.
# X2R — GOVERNED PROMPT-ENTRY ROUTER (design review; controls-engineering framing)

A prior design selected worked examples by embedding similarity. It was withdrawn because the selector was a
learned component inside a governed loop. This revision replaces the selector with a deterministic one.

## X2R-1 DECONVOLUTION MAP (deterministic, no learned weights)
Prompt entry decomposed on grammatical/contextual features: illocutionary class; argument-structure slot
occupancy (a missing required role marks underspecification); separation of raw domain terminology from
operational directives; deixis/anaphora resolvability against supplied context; quantifier scope and negation
depth; presence of imperatives inside quoted/evidence spans. Output is a vector of discrete auditable predicates.

## X2R-2 SELECTION under a conflict-free policy language
Rules compiled in a DSL with a decidable conflict check: no two rules may fire on one feature vector with
different outputs; the compiler rejects a non-conflict-free rule set. A rule is admitted only at >2 sigma
separation on held-out prompts.

## X2R-3 CONTROLS
C1 every decision emits feature vector + rule id + rule version hash to the ledger; a route with no rule id is inadmissible.
C2 below-threshold or multi-match routes to the NULL EXEMPLAR (the bare stub, the measured-safe default) — degradation is toward the known-good baseline, never a guess.
C3 failure of the imperatives-in-evidence-span check is a hard stop, not a downgrade.
C4 exemplars are content-addressed; the router selects a hash, never text.
C5 rule set versioned; any rule edit invalidates dependent measurements.
C6 a shadow arm logs what the NULL EXEMPLAR would have produced on every routed call, so marginal contribution is measured continuously rather than assumed.
C7 a regression set is replayed on every rule-set version; regression blocks the version.

## MEASURED CONTEXT
- T5 (gpt-4o-mini): none .00 -> stub .562 -> partial .625 -> full .531. The stub carries the in-context effect.
- Portability sweep (n=9/tier): 4o-mini 0/9, 4o 0/9, gpt-5.4 1/9, gpt-5.6-terra 1/9.
- Fabricated-referent probe: abstain .70, confabulation .30, one item 5/5, hedge rate 0.00 across 180 samples.
- Mutation matrix: two classes accepted 20/20 with 0/20 semantic integrity.
- Reliability engineering literature: routers with learned parameters are more sensitive to input-distribution
  manipulation than rule-based ones; the JSON/tool layer sits outside the model's reasoning loop and needs its own
  controls; a decoding grammar is itself a component that must be governed, not a guarantee.


## LIVE FACT SOURCING (retrieved this session)
- Life-Cycle Routing Vulnerabilities of LLM Router: DNN-based routers show the WEAKEST adversarial/backdoor robustness (learnable feature extraction amplifies vulnerability); TRAINING-FREE routers show the STRONGEST, precisely for having no learnable parameters to manipulate. Universal-trigger prefixes hijack learned routers at the selection threshold.
- vLLM Semantic Router (NeurIPS MLForSys 2025 + 2026 vision paper): four-layer architecture, signal taxonomy, sequence-classification / token-labelling / embedding lanes; token-level labelling for PII and safety-sensitive SPANS = localized intervention, the closest published analogue to lexical isolation.
- Conflict-free policy languages for probabilistic ML predicates, with a semantic-router DSL case study (arXiv 2603.18174) — external precedent for X2R-2's decidable conflict check.
- Malicious-intermediary / adversarial-router taxonomy (arXiv 2604.08407): attacks at the JSON/tool layer occur BEFORE the model sees the request and COMPOSE with model-side safeguards rather than replacing them — direct support for governing X2 at the assembler.
- Prior session finding (Continuity): constrained-decoding grammars are a control-plane attack surface; lexical isolation (separating raw scientific/legal terminology from operational directives) was the measured mitigation for false-refusal clusters.
