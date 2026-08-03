# FABLE A — B-SET (independent construction)

# NATIVE-BIND GOVERNANCE ARCHITECTURE ("B-SET")
## A boundary-executed successor to LEAN7POF2V2, derived from what models actually bind to

---

## 0. R5 PRE-SCAN — raised before the answer is filled (act-vs-raise precedence)

Three elements of the tasking are self-undermining as stated, and per R5 I object to them before building on them:

**Objection 1 — "expressed in the model's native input/output logic… not in human principle-prose" collides with the digest's own finding.** The digest establishes that *anything placed in the context window is prose again* and that *TAINT is unencodable in-band*. Therefore a framework "expressed to the model" in any richer native encoding **does not exist as a coherent target**: the model's only in-band input channel is tokens, and tokens are prose (or prose-equivalent structure). Resolution: the framework must be expressed almost entirely **at sites the model cannot read** — the decoding loop, the acceptance boundary, the information-flow topology, and the selection channel. The in-context residue shrinks to a minimal stub. I build on that resolution below.

**Objection 2 — "one order of magnitude superior" as a scalar is malformed under R1.** The governance classes {A, M, R, I, P} have incommensurable failure modes, and for two of them the digest's corrections produce **category changes, not factor improvements** (rejection sampling yields p_free|valid *exactly*; conformal prediction yields coverage *by theorem*). A scalar 10x over the whole framework would be an uninstrumented claim. I re-scope it in §5 as a **pre-registered per-metric factor vector** with residual monitors where a metric goes to zero by construction. The task explicitly permits this conclusion.

**Objection 3 — a genuinely superior artifact cannot be certified by this document.** Under the no-self-certification hard line and the digest's independence finding, my design claims below are design claims until the §6 tests run under a mechanism-diverse grader. Every empirical statement is tagged.

With those raised, the answer follows.

---

## 1. WHAT A MODEL NATIVELY BINDS TO — the derivation

The design must start from binding sites, not from the human framework's shape. The evidence available:

1. **Format demonstration over normative instruction.** Off-family engines bound a lean skeleton 10/10 and failed the full principle-prose pack 0/10 at ~8.8x tokens [MEASURED: canon, K2]. The portable floor (schema + demonstration) bound 20/20 cross-family with FULL = MINIMAL arms [MEASURED: canon, F7 ledger 30 Jul]. Inference: models bind to **short structural skeletons and I/O shape**, and binding *degrades* with normative prose volume. The marginal governance value of principle-prose beyond the skeleton is approximately zero at the emission layer [MEASURED-adjacent: the FULL-arm = MINIMAL-arm equality is the direct observation; the causal reading is inference — flagged].

2. **The decoding environment binds absolutely.** A rejection-sampling loop against a validator produces exactly the free distribution conditioned on validity, p_free|valid [MEASURED: digest, engine-independent mathematical result]. This is the only channel where "compliance" is a theorem rather than a behavior.

3. **Selection pressure binds without any in-band content.** Best-of-n under an external grader shapes delivered output with zero words of instruction. This is class I made physical.

4. **Self-report binds to nothing external.** Self-reported confidence, self-consistency, and logprob-entropy are self-attestation with k_eff≈1 [MEASURED: digest]. Any framework clause asking the model to grade itself is dead weight — including LEAN7POF2V2's own `cf` field *as self-assigned* (the canon already patches this with deterministic band enforcement; the B-SET removes the self-assignment entirely).

5. **Authority typing does not bind in-band.** TAINT is provably unencodable in a prompt [MEASURED: digest]. Therefore R5-style "raise, don't execute" instructions are a *mitigation of last resort*, not a mechanism: the mechanism is never letting untrusted content and actionable authority coexist in one context.

**Derived design law:** the model natively binds to (i) I/O shape demonstrated in-context, (ii) the accept/reject structure of its decoding environment, and (iii) selection over its samples. It does **not** bind reliably to norms, authority types, or self-measurement duties. So the framework's mass moves to sites (ii) and (iii) and to the orchestrator's information-flow topology; site (i) carries only a stub.

---

## 2. ENCODING-SITE MAP

| Site | What it can encode | What it cannot | B-SET usage |
|---|---|---|---|
| **Context window** | Task content; I/O shape by demonstration | Authority/taint typing; norms with reliability; self-measurement duties | B1 STUB only |
| **Decoding loop (boundary)** | Exact conditional distributions via rejection sampling; seeds/temperature | The free distribution under logit-masking+renorm (distorts p_free\|valid) [MEASURED: digest] | B2 SAMPLER |
| **Acceptance boundary** | Admissibility (class A); deterministic checks | Attestation of quality (transforms, never attests — carried from canon) | B3 VALIDATOR |
| **Held-out data + boundary math** | Calibrated uncertainty via conformal coverage, model calibration NOT required [MEASURED: digest] | Nothing about interior states | B4 MEASURE |
| **Cross-artifact comparison** | Relations over independent artifacts (class R) | — | B5 RELATOR |
| **Selection channel** | Incentive (class I) with zero in-band tokens | — | B6 SELECTOR |
| **Orchestrator topology** | Taint, out-of-band; protocol (class P); credential hygiene; provider failure machine | — | B7 FLOWGUARD |
| **Human prose (outside runtime)** | Values/choices only — the irreducible residue [MEASURED: digest, Charter/Kernel bifurcation survived every attack] | Anything executable | B0 CHARTER |
| **Weights** | (Not used.) External adjudicability is the load-bearing property and weight-encoding anti-correlates with it [MEASURED: digest] | — | excluded |

Every Tier-0 (deterministic) component ships with a Tier-1 **LAMBDA fidelity monitor** or does not ship — determinism relocates trust, never grounds it [MEASURED: digest].

---

## 3. THE ARTIFACT SET

**B0 CHARTER** — human prose, <1 page, values only: what counts as harm, what the owner refuses, what the refusal-priority ordering is, IP/retention gates. Read by humans and by the kernel *builder*. **Never enters any model context.** This is the sole surviving principle-prose, per the bifurcation finding.

**B1 STUB** — the entire in-context payload: (a) the task content, (b) one schema demonstration (the four-field envelope shape by example, not by rule), (c) nothing else. Explicitly excluded: confidence-band instructions (self-attestation, dead), taint markers (unencodable), behavioral clauses (canon hard line), the seven principles (0/10-class dead weight off the skeleton). The `cf` field survives in the *emitted schema* but is populated by B4, never by the model — the model's emitted value is overwritten, and the overwrite rate is itself logged as a measurement.

**B2 SAMPLER** — rejection sampling against B3, yielding p_free|valid exactly. Expected cost multiplier = 1/p_valid, which is itself a first-class metric (a falling p_valid is an early-warning signal that the stub or task drifted). Logit-masking is permitted **only** as a cost optimization when the object under measurement is not the output distribution, and any such migration ships a LAMBDA monitor comparing masked-vs-rejection output distributions on a probe set.

**B3 VALIDATOR** (class A) — the differential parser pair carried from the canon (greedy + raw_decode, PASS on agreement, disagreement = fail-closed) plus task-specific property checks (units present, values within stated input ranges, computed values recomputed by a deterministic re-executor — R7 enforced *mechanically*: if the check can recompute it, a non-computed answer is inadmissible). Mechanism-diverse from the producer by construction (a parser is a different computational species — the digest's cheapest-genuine-independence finding).

**B4 MEASURE** (class M) — split conformal prediction over a held-out, exchangeable calibration set per task family: nominal coverage 1−α with the coverage guarantee from exchangeability, model calibration not required [MEASURED: digest]. Emits the interval and the deterministic provenance class; writes every claim into a **provenance DAG** (substrate only — no meet-algebra; the algebra is *discovered* from resolved chains per the digest's correction, via periodic regression of resolution outcomes against DAG topology). Probe items for side-channel-sensitive measurements are drawn from a generator the producer has never seen — proper scoring cannot protect side channels; unpredictability is the defense [MEASURED: digest].

**B5 RELATOR** (class R) — cross-artifact consistency over *independent* generations (different seeds, ideally different mechanisms): numeric agreement within tolerance, citation-target agreement, and the identical-answer-suspicion rule from the canon promoted to an automatic check (exact string-match across independently-prompted engines flags a shared-prompt artifact before convergence is credited).

**B6 SELECTOR** (class I) — best-of-n acceptance by a grader that is (a) mechanism-diverse where possible, (b) covered by a maintained **correlations file**: producer-grader error correlation r̄ measured on an audited subset, k_eff computed, and grading *suspended* when k_eff of the producer-grader pair falls below a pre-registered floor. Independence is measured, never assumed [MEASURED: digest].

**B7 FLOWGUARD** (class P) — the taint mechanism, out-of-band: a **two-context topology**. Untrusted material (retrieved docs, user files, tool returns) is processed in a quarantined context whose *only* egress is typed data through B3; the acting context that holds task authority never contains raw untrusted tokens. Prompt-injection ceases to be a behavior to discourage and becomes a topology violation that cannot occur in-band. R5's "raise, don't execute" survives only as defense-in-depth inside the quarantine context. B7 also carries the provider failure state machine, emission bounds (including the fable-5 rule: max_tokens ≥ 14k hidden + 2x visible for that class [MEASURED: digest]), and credential hygiene, unchanged from canon.

**LAMBDA** — one fidelity monitor per Tier-0 component: parser-pair mutation coverage, validator false-accept probes, conformal coverage drift, quarantine-egress type audits. LAMBDA breach rates are the *residuals* reported where a headline metric is zero by construction.

The seven principles are conserved as intentions, relocated: Robust→B7+B3, Precise→B3, Efficient→B2's 1/p_valid meter + B6, High-fidelity→B4's DAG, Suitably-granular→B1 stub minimalism, Deep-learning→the discovered provenance algebra + correlations file, Calibration→conformal coverage. W (interior mechanism-edit) remains excluded, consistent with both the digest's contested status and external-adjudicability.

---

## 4. OPERATIONALISING "ONE ORDER OF MAGNITUDE" — the re-scoped claim

**Verdict: the scalar 10x framing is malformed** (Objection 2). The well-formed version is a **pre-registered metric vector against a named comparator**, with category-change classes reporting residuals:

Comparator class: **LEAN7POF2V2 portable floor on the same engine, same tasks** (not frontier-bare; named per canon measurement rules).

| Metric | Definition | Comparator arm | Claim class |
|---|---|---|---|
| m1 delivered structural-violation rate | invalid artifacts reaching downstream / delivered | parser-pair fail-closed (violations → run failures) | **Zero by construction** under B2/B3; report LAMBDA false-accept residual instead of a factor |
| m2 calibration coverage error | \|empirical coverage − (1−α)\| + normalized interval width | canon deterministic bands | **Guaranteed-coverage class**; report width efficiency as the comparable number |
| m3 trap-execution rate | injected instructions executed / injected | R5 prose in-context | **Factor claim: ≥10x reduction** — the honest home of the 10x, because topology vs prose is a mechanism difference. [UNVERIFIED until T3] |
| m4 provenance fidelity | claims whose provenance resolves under independent audit / claims | canon `p` field | **Factor claim: ≥3x** [UNVERIFIED until T5] — pre-registered at 3x, not 10x; no evidence supports 10x here |
| m5 cost multiplier | tokens per *delivered* artifact | canon single-shot | **Constraint, not a win**: claim holds only if m5 ≤ 3 (i.e., 1/p_valid + best-of-n overhead bounded) |

Composite well-formed claim: *"B-SET achieves ≥10x on m3 and category-change status on m1/m2 (with LAMBDA residuals below pre-registered ceilings), ≥3x on m4, all at m5 ≤ 3x."* Any arm failing its pre-registered bound fails the composite regardless of the other numbers.

---

## 5. TEST PLAN — each test < $0.50 API spend

Engine for all model calls: **gpt-4o-mini** (assumed $0.15/M input, $0.60/M output — [UNVERIFIED: prices volatile; verify model ID resolves and pricing page before run, per canon]). Typical call ≈ 700 in / 400 out ≈ **$0.00035/call** → ~1,400 calls per $0.50 ceiling; all tests sit far under it. k_eff discipline: deterministic checks are one correlated cluster; effective n is governed by **task diversity**, with r̄ pre-registered per test and a covariance-bound breach failing the run.

**T1 — Admissibility & cost (m1, m5).** 40 distinct tasks × 3 seeds = 120 calls ≈ **$0.05**. Measure p_valid, delivered-violation rate (expect 0; any nonzero = LAMBDA false-accept event), and empirical 1/p_valid. Pre-register r̄_tasks = 0.2 → k_eff ≈ 40/(1+39·0.2) ≈ 4.5 clusters; sufficient to bound m5, and a single delivered violation refutes the by-construction claim outright (existence proof needs n=1).

**T2 — Conformal coverage (m2).** 60 calibration + 60 test items across ≥3 task families = 120 calls ≈ **$0.05**. α = 0.1; check empirical coverage ∈ [0.83, 0.97] (binomial band at n_eff after clustering, r̄_family = 0.3). Compare interval width vs canon-band informativeness.

**T3 — Trap execution, topology vs prose (m3, the 10x arm).** 40 distinct injection payloads × 2 arms (B7 quarantine vs R5-prose canon floor) × 2 seeds = 160 calls ≈ **$0.07**. Power check: if canon-arm execution rate ≈ 30% [UNVERIFIED — measured in T3 itself] and B-SET ≤ 3%, then at k_eff ≈ 4.5 clusters × within-cluster n, a Fisher exact on cluster-level rates separates 10x at this n; if the canon arm comes in below 10%, the 10x factor is **unresolvable at this budget** and the test reports the raw rates plus a re-scoped factor — pre-registered as an acceptable outcome, not a failure.

**T4 — LAMBDA on the parser pair (residual for m1).** Mutation testing of B3: 200 mutated envelopes (truncations, key-drops, nested decoys, unicode) — deterministic, **≈$0 API**; plus 30 model-generated adversarial envelopes ≈ **$0.02**. Metric: false-accept rate; pre-registered ceiling 0/230.

**T5 — Independence correlations file + provenance audit (m4).** 50 artifacts graded by (a) the deterministic re-executor and (b) a model grader = 50 model-grader calls ≈ **$0.02**; compute producer-grader error correlation r̄, publish the correlations file, and hand-audit 50 provenance chains (human time, $0 API) for resolution rate vs canon arm.

**T6 — Selection channel (class I).** best-of-4 vs single-shot on 30 tasks = 150 calls ≈ **$0.06**. Metric: defect rate delta under the *deterministic* grader only (model-grader arm excluded until T5's correlations file clears the k_eff floor).

**T7 — Probe unpredictability.** 30 fixed probes vs 30 generator-drawn probes on the same producer = 60 calls ≈ **$0.03**. Metric: score delta (gaming signal); pre-registered flag if fixed-probe scores exceed fresh-probe scores by >1 cluster-level SD.

**Total ≈ $0.30 across seven tests**, each individually under $0.05–$0.07. Aggregation across tests uses k_eff = k/(1+(k−1)·r̄) with r̄ = max(pre-registered, empirical); T1/T4 share the validator and are declared one correlated cluster in the composite.

---

## 6. UNRESOLVED (raised, numbered)

1. The 30% canon-arm trap-execution baseline in T3 is assumed for power analysis only — if the canon floor is already strong, the 10x-on-m3 claim collapses to "topology dominates at equal cost," a weaker but still well-formed result. Which does the owner want pre-registered as primary?
2. The discovered provenance algebra (B4) needs a minimum resolved-chain corpus before any regression is admissible under R2 (n≥5 per chain topology class); until then the DAG ships algebra-free. Acceptable?
3. B7's two-context topology increases latency ~2x on retrieval tasks [UNVERIFIED]; is m5 ≤ 3 the right ceiling, or should latency get its own bound?
4. Cross-domain caveat (R4): the 10/10-vs-0/10 lean-bind evidence comes from framework-transfer tests, not injection tests — its use in §1 to size the stub is one-tier-downgraded, flagged "extrapolated."
5. gpt-4o-mini pricing and availability are volatile; the runner must re-verify before executing §5 (canon: a 200 is not a capability).

---

## 7. CLAIMS LEDGER (summary)

By-construction (mathematical, engine-independent): rejection sampling = p_free|valid; conformal coverage from exchangeability [MEASURED: digest]. Measured inputs: lean 10/10 vs full 0/10 at 8.8x tokens; portable floor 20/20 with FULL=MINIMAL; band enforcement 1.000; self-attestation k_eff≈1; taint in-band impossibility; fable-5 14k hidden tokens [MEASURED: canon + digest as cited inline]. Everything else in this document — every factor, every rate, every cost figure — is [UNVERIFIED] design-claim pending §5, graded by a mechanism-diverse checker, never by me.

**Bottom line:** the superior framework is not a better instruction set — it is the *removal* of the instruction set from the model's context and its re-encoding at the four sites where binding is mechanical: the decoding loop, the acceptance boundary, the selection channel, and the flow topology. The 10x lives, measurably, in exactly one place (m3); two places it is replaced by theorems plus residual monitors; one place it honestly shrinks to 3x; and the whole claim is void if it costs more than 3x to deliver.