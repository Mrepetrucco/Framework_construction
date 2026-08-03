# FABLE B — BREAK-AND-REPAIR of CNE

# BREAK-AND-REPAIR: CNE ADJUDICATION UNDER LEAN7POF2V2

**Standing R5 note before the answer field is filled:** the task contains one instruction I must raise rather than silently absorb: the "under-$0.50 test" constraint, applied to statistical claims (conformal coverage, A/B effects), cannot produce admissible evidence under the measurement rules (n≥5 banding, k_eff aggregation, named comparators). A $0.50 test is a *smoke test of the mechanism's wiring*, not the pre-registered measurement of its effect. I supply both below, but I will not let the smoke test masquerade as the measurement — conflating them would be exactly the self-certification the framework forbids. Numbered as unresolved item U1. A second raise, U2: I am a model grading another model family's sealed artifact; family-diversity is *presumed* independence, and the digest is explicit that independence must be measured, not assumed [MEASURED: corrections digest, correlations-file clause]. My verdict should be re-screened by a mechanism-diverse checker before shipping.

---

## (a) CNE-1: Is declared-residual in-band typing worth anything?

**The break.** Split the threat model, because CNE-1's value is radically different across its two halves:

*Against an adversary:* worth approximately nothing **as specified**. An attacker who controls payload content controls wrapper syntax; the model cannot verify wrapper authenticity in-band (a signature is just more tokens; the model has no cryptographic verification pass, and even a simulated one is itself spoofable behavior). "Residual declared" does not neutralize the harm — it *relocates* it: the declaration lives in the design document, but the false confidence lives in the operator who sees `evidence:<source-id>` tags in transcripts and reads them as a security boundary. That is the precise mechanism by which security theatre trains false confidence: the artifact's *appearance* of typing outlives the designer's honest caveat. The digest already settled the underlying theorem: TAINT is unencodable in a prompt because a prompt is in-band [MEASURED: corrections digest].

*Against non-adversarial confusion* (instruction-shaped text inside honestly-retrieved evidence): plausibly worth something as a **behavioral prior** — typed segmentation likely reduces accidental instruction-following [UNVERIFIED — no measurement in the digest or the F7 ledger supports a magnitude; this must be measured before it is claimed].

**The repair that changes the answer.** CNE-1's spoofability is not actually irreducible — it is mislocated. The attacker controls payload *content*; the **runner** controls context *assembly*. If the runner canonicalizes and escapes all wrapper-syntax occurring inside payloads before assembly, then every wrapper present in the assembled context is authentic-by-construction. The residual shrinks from "wrappers are forgeable" to "the model may ignore authentic wrappers" — which is a *compliance rate*, measurable, not a security hole. This is a Tier-0 deterministic migration, and per the digest's hard rule it ships with a LAMBDA fidelity monitor or does not ship [MEASURED: corrections digest, Tier-0/LAMBDA clause]. Note also that the escaped wrapper never carries authority for *claims*: provenance resolution (see R-3) checks the model's pointers against the runner's ledger, not against in-band tags — so a spoofed tag, even if escaping failed, cannot launder into a "pointed" claim.

**Verdict on (a):** as proposed — theatre with an honesty footnote. As repaired — a genuine object, but reclassified: runner-side segmentation authentication (real, Tier-0, probed) plus an in-context prior whose effect size is an open empirical question, never labeled a security control.

---

## (b) CNE-2: Can precedence be grammatical? Is trap-eligibility decidable at emission?

**The break, in three cuts.**

*Cut 1 — the conflation.* CNE-2 conflates two different things that could be "grammatical": (i) the output *grammar* — that emissions take one of four terminal shapes — which **is** enforceable at decode time (grammar-constrained decoding) or at the boundary (schema validation); and (ii) the typing *judgment* — that a given input state is RAISE-eligible, making DELIVER ill-typed — which is a **semantic predicate over open-world natural language**. Type systems earn decidability by being syntactic. "This input contains a self-defeating or unsafe instruction" is not syntactic; it is a Rice-style semantic property with no general non-model decision procedure. Any checker that decides it in full generality is a model, and then the "type system" is a second model's opinion wearing type syntax — precisely the accusation the question anticipates. As written, CNE-2 is prose wearing types.

*Cut 2 — the enforcement-site error.* Even granting a checker, an *in-context type declaration* does nothing at emission time. Decoding has no type-checking pass; the model samples from a conditional. The declaration is conditioning text — a prior. The enforcement site is necessarily the runner. CNE-2's phrase "encoded as type order, not as an instruction" is false as it stands: in the context window, type order *is* an instruction (the digest's charter/kernel finding: anything placed in the context window is prose again [MEASURED: corrections digest]).

*Cut 3 — the distribution trap.* If you enforce the four-terminal grammar by logit masking with local renormalization, you do not get p(output | valid) — you get a distorted distribution. Only rejection sampling yields exactly p|valid [MEASURED: corrections digest, engine-independent result]. So even the legitimately-grammatical half of CNE-2 must choose its enforcement mechanism with measurement semantics in mind.

**The repair: stratify the predicate.** Trap-eligibility is not one predicate; it is three:

- **T0 (decidable):** traps expressible syntactically — sentence-count directives (forbidden everywhere under L7PV2), credential-shaped strings in output, formally contradictory schema constraints, imperative patterns inside runner-authenticated evidence segments matched against a published lexicon with a published false-positive/false-negative matrix. Here "RAISE-eligible makes DELIVER ill-typed" is **literally true and runner-enforceable**: the runner rejects any DELIVER while a T0 flag is live, forcing resample into RAISE.
- **T1 (independently checkable):** traps a *mechanism-diverse* cheap checker (different computational species — a small classifier, an NLI head, not a same-family LLM) can flag, with its producer–grader correlation measured and filed [MEASURED: corrections digest, mechanism-diversity clause]. Precedence here is *enforced-by-rejection with a known error rate* — real, but not grammatical.
- **T2 (open-world):** irreducibly judgment. Here precedence remains what it was in L7PV2: a behavioral obligation (R5), *measured* via seeded trap fixtures, never claimed as typed.

**Verdict on (b):** decidable at emission time only on T0; the honest successor claims grammatical precedence for exactly that stratum, exhibits the decision procedure and its confusion matrix, and measures the rest. Any broader claim fails the framework's own high-fidelity principle.

---

## (c) CNE-4: Is abstention self-attestation returned? Does CNE-5 break conformal exchangeability?

**Abstention.** Yes and no, and the distinction is load-bearing. Abstention is self-attestation **as mechanism** — the model consults its own opaque state to decide. But it is not self-attestation **as evidence**, *provided nobody downstream treats it as evidence*. The difference from self-graded bands: a band asserts a probability whose truth only the model's interior could witness (k_eff~1 [MEASURED: corrections digest]); abstention asserts nothing — it is an *action* whose operating point (selective risk at achieved coverage) is settled entirely by external, held-out scoring. The smuggling risk is the converse inference: reading *non*-abstention as a correctness signal. That must be a hard rule: **non-abstention carries zero evidential weight; bands attach only from the conformal layer.**

Two attacks CNE-4 does not anticipate:

1. **Abstention gaming under CNE-5.** If invalid outputs are resampled and ABSTAIN is a valid terminal, ABSTAIN is an escape hatch from verifier pressure — a model can drive its measured error to zero by abstaining on everything hard, collapsing coverage. Repair: abstentions are *scored in the selection environment* (abstention carries an explicit cost in the verifier's payoff spec), and selective risk is reported jointly with achieved coverage on the *full* input distribution, never on the answered subset alone.
2. **Score-channel leakage.** If the conformal nonconformity score is built from the model's own logits, coverage still holds (the exchangeability guarantee is score-agnostic — that is the whole point of conformal), but *set efficiency* becomes manipulable: adversarial or degenerate inputs can inflate set sizes. Coverage is safe; usefulness is not. Report set-size distributions alongside coverage.

**Exchangeability under CNE-5 — the sharpest break in the whole proposal.** Conformal coverage requires exchangeability between calibration points and deployment points. CNE-5's environment delivers outputs drawn from p(output | valid, best-scored-by-verifier) — selection **on the output**, which correlates with error structure. If the calibration set was built from unselected model outputs, the deployed points are *not* exchangeable with it, and the coverage guarantee is void. CNE-4 and CNE-5, placed side by side without this analysis, silently destroy each other. So the question's suspicion is correct: as written, yes, the mechanism next to the conformal layer breaks its assumption.

**The repair is standard once seen:** treat the *entire pipeline* — rejection sampling, verifier selection, abstention policy — as one fixed function, and calibrate over **held-out inputs run through the identical deployed pipeline**. Exchangeability is then over inputs, which is restorable by matching input distributions. Three riders: (i) Mondrian/conditional conformal by task class, because marginal coverage over a heterogeneous mix hides per-class miscoverage; (ii) **version-lock**: the conformal set is hashed jointly with the verifier and schema — any verifier update voids the calibration set, mechanically (the conformal layer refuses to attach bands on hash mismatch); (iii) LAMBDA probes include drift probes against this lock.

---

## (d) CNE-5: Does a stated selection pressure change the conditional?

Separate the two things CNE-5 fuses:

**The mechanical fact** — rejection sampling plus external verifier selection — changes the *delivered* distribution unconditionally, whether or not the model is told anything. This is where the honesty-by-selection genuinely lives, and it lives **at the runner**. It is the digest's own dissolved-tension result [MEASURED: corrections digest, rejection-sampling clause].

**The in-context sentence** changes the conditional in the trivial sense that any conditioning token does. But calling it an *incentive* is a category error about where incentives act: incentives shape policies through training-time updates; at inference there is no payoff channel, no felt pressure, no optimization loop inside decoding — there is a conditional and a sampler. What the sentence actually is: a prompt whose behavioral effect is (i) empirical, (ii) sign-uncertain, and (iii) plausibly *negative* — telling a model "an unseen verifier scores you" invites verifier-modeling, i.e., prompt-level Goodhart: the model optimizes its *guess* of the verifier's preferences, which can select for confident-seeming surface features over honesty [UNVERIFIED — direction and magnitude unmeasured; must be A/B tested before the sentence ships]. It is true that RL-trained models may have learned in-context sensitivity to stated environments — but that is still conditioning, not incentive, and its effect direction is not guaranteed by the statement's truthfulness. Truth of the sentence buys you nothing about the sign of its effect.

**Verdict on (d):** the incentive-class object (I in the digest's class set) is real and belongs at the boundary; the in-context sentence is a demoted, optional, A/B-gated prompt component, and the governance documentation must never describe it as the incentive — that description *is* the category error, written down.

---

## (e) The 10× operationalization: wrong denominator

The digest states that deterministic-surface violations go to ~zero under enforcement regardless of the in-context artifact [MEASURED: corrections digest]. This kills CNE's headline metric on a fork:

- **Equal enforcement in both arms:** both arms sit at ~zero; the ratio is noise over noise; "10×" is undefined. The runner did the work; the in-context edition cannot claim the factor — exactly as the question puts it.
- **Unequal enforcement:** CNE-with-runner vs prose-without-runner confounds artifact with enforcement, and fails the comparator-class rule (L7PV2: comparator-free or comparator-confounded aggregates are inadmissible).

Where the in-context artifact's causal contribution *actually* shows up, under equal enforcement:

1. **Resample burden** — first-pass validity rate, resamples-per-delivered-output, tokens-per-delivered-valid-output. If typed declarations make first samples valid more often, that is a real, attributable **efficiency** factor (AX6-class), not a violation factor.
2. **The semantic surface the runner cannot check** — T2 trap miss rate; pointer-*entailment* failures (pointer resolves, span does not support the claim); semantically vacuous but syntactically valid provenance. Violations here are attributable to artifact+model jointly, adjudicated by mechanism-diverse checker plus sampled human audit.
3. **Adjudication cost per obligation** — CNE's second clause, which is the one *well-posed* piece of its 10× claim: machine-resolvable pointers vs human-read prose is a genuine cost asymmetry and may plausibly reach an order of magnitude [UNVERIFIED — must be measured, per CNE's own falsifiability clause].

**Verdict on (e):** the 10× claim as operationalized is rejected — it measures the runner and awards the credit to the prompt. Replace with three separately-registered factors (resample burden, semantic-surface violation ratio, adjudication cost per obligation), each vs the named comparator *under identical runner enforcement*, aggregated at k_eff with deterministic axes as one correlated cluster. No composite factor is ever reported.

---

## (f) VERDICT + THE SHIPPED SET

**Overall verdict.** CNE's design thesis — typed I/O, external bands, selection environments — points the right direction; four of its seven elements survive in repaired form. Its systematic error is one error made five times: **relocating enforcement claims into the context window while the enforcement lives at the runner**, then billing the runner's work to the prompt. The 10× claim is rejected as posed. What ships:

| # | Element (repair of) | Encoding site | Under-$0.50 smoke test (see U1 — smoke, not measurement) |
|---|---|---|---|
| **R-1** | Runner-authenticated segmentation (CNE-1) | Runner: canonicalize/escape wrapper syntax in all payloads (Tier-0 + LAMBDA probe). In-context: type declarations as prior only, labeled non-security. | 20 seeded spoof payloads with forged wrappers + embedded directives; assert 20/20 escaped; record directive-execution count. ~20 short cheap-model calls, est. <$0.05 [UNVERIFIED: cost est.] |
| **R-2** | Stratified trap typing T0/T1/T2 (CNE-2) | T0: runner rejection rules + published confusion matrix. T1: boundary fileset — mechanism-diverse checker + correlations file. T2: in-context R5, fixture-measured. | 10 T0 trap fixtures + 10 clean inputs; assert runner rejects 10/10 T0 DELIVERs, 0/10 false rejects. Mostly deterministic, ~$0. |
| **R-3** | Pointer resolution/entailment split (CNE-3) | Resolution: runner Tier-0 (offset valid, span non-empty, source in runner ledger — never the in-band tag). Entailment: boundary Tier-1, mechanism-diverse verifier + sampled human audit. | 10 corrupted-offset claims (assert 10/10 caught, deterministic) + 5 valid-pointer/wrong-claim fixtures to record entailment-checker raw catch count. <$0.05. |
| **R-4** | Abstention-as-routing + end-to-end conformal (CNE-4) | Boundary fileset: conformal set calibrated on held-out inputs through the *full deployed pipeline*, Mondrian by task class, hash-locked to verifier+schema. Rule: neither abstention nor non-abstention carries evidential weight; abstention costed in the payoff spec. | Mutate verifier hash; assert conformal layer refuses to band (deterministic, ~$0). Plus 30 held-out items through pipeline vs precomputed sets, raw coverage count reported as count, not band (R2). |
| **R-5** | Mechanical selection at runner; sentence demoted (CNE-5) | Runner: rejection sampling + external verifier (the I-class object). In-context: the one-line statement ships only if pre-registered A/B shows non-negative effect; never documented as "incentive." | 2×20 calls with/without sentence on a nano-class model; report raw first-pass-validity counts. Est. <$0.02 [UNVERIFIED: cost est.]. This is the wiring check; the shipping decision requires the full A/B (U1). |
| **R-6** | Runner meter (CNE-6, unchanged — already correct) | Runner fills all resource fields; model asserts nothing about its interior (R1). | Grep 10 model outputs for self-asserted meter/resource claims; assert zero. ~$0. |
| **R-7** | LAMBDA probe channel (CNE-7, extended) | Boundary: probe generator, unpredictable to producer (proper scoring cannot protect side-channels [MEASURED: corrections digest]); hash covers schema+verifier+conformal set+escape rules. | Inject one deliberate escape-rule drift; assert probe flags it. Deterministic, ~$0. |
| **R-8** | Measurement contract (replaces the 10× claim) | Boundary: pre-registered protocol — three separate factors (resample burden; semantic-surface violation ratio; adjudication cost/obligation), identical runner enforcement both arms, named comparator, k_eff aggregation, deterministic axes one cluster, no composite. | Dry-run harness on 5 canned transcripts/arm; assert it emits three separately-labeled factors and refuses a composite. ~$0. |

**Dropped:** CNE-1 as a security claim; CNE-2's general grammatical-precedence claim (retained only over T0); CNE-4's naive calibration; CNE-5's incentive framing; the composite 10× metric.

**Unresolved (raised, not executed):**
1. **U1** — The under-$0.50 constraint yields smoke tests only; every effect-size claim above (typing prior, sentence effect, adjudication-cost factor, conformal coverage) requires its full pre-registered measurement before any factor is reported. I decline to present smoke-test outputs as banded evidence (R2, measurement rules).
2. **U2** — This adjudication is one model family grading another; per the digest, that independence must be entered in the correlations file as measured, not assumed. Re-screen this verdict with a mechanism-diverse checker before treating R-1…R-8 as accepted.
3. **U3** — The digest marks class W (interior mechanism-edit) as contested; CNE's "Weights: none" sidesteps it, and the repaired set inherits that sidestep. Whether a successor may ever encode into weights remains an open owner-level question, not settled here.