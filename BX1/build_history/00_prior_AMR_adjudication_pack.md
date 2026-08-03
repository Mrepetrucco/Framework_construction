# THE ADJUDICATION PACK — POST-BATTLE MERGED KERNEL (v0.9, UNADJUDICATED)
Owner: Enrico · 02 Aug 2026 · under LEAN7POF2 V2 (v1.4, 31 Jul 2026)

**STATUS — read this first.** Rounds 1 and 2 were run live against `claude-fable-5`
[MEASURED: this session, served_model confirmed, $2.70 total]. **Round 3 (independent
adjudication) DID NOT RUN** — Anthropic credit balance exhausted, HTTP 400
`invalid_request_error` [MEASURED: this session].

This document is therefore assembled by **Opus 5, who authored the thesis under attack.**
That is a self-certification breach under this framework's own hard line ("a producing
component never grades its own product"). Every adjudication call below is marked
**[INTERESTED-PARTY — requires independent re-run]**. Section 5 is the loaded R3 brief;
fire it on an independent engine before anything here is built.

---

## 1. WHAT THE BATTLE ESTABLISHED

Three positions existed. Fable A built from scratch with no sight of the thesis. Fable B was
handed the thesis and told to break it. They did not see each other.

### 1.1 Independent convergence — the only real evidence produced

| Object | Opus (A/M/R thesis) | Fable A (independent) | Status |
|---|---|---|---|
| Decorrelated adjudication | Φ N-version + Σ separation | Φ6 INDEP (ρ(err_judge, err_gen) ≤ ρ_max) | **Converged** — reached from opposite directions |
| Charter is irreducible | §0.5 bifurcation | "prose is the right encoding for exactly one thing: the human-auditable statement of what the guarantees should be" | **Converged** |
| Framework value is its deterministic residue | §0.1 | §2 "the framework's own version history is a migration off prose" | **Converged** |
| The trichotomy is incomplete | *not seen* | Φ7/Φ8 "fourth kind" | A found it |
| The trichotomy is incomplete | *not seen* | B: classes **I** and **P** | B found it, independently |

**The load-bearing result:** A and B, without contact, both concluded the A/M/R trichotomy
misses a class — A from "process-measure objects," B from "incentive + protocol." Two
independent refutations of the same claim from different directions is the strongest signal
in this entire exercise, and it is a refutation of my own thesis.

### 1.2 The corrected class set (was 3, now 5, possibly 6)

| Class | Verb | Object |
|---|---|---|
| **A** ADMISSIBILITY | *makes violation impossible* | constraint on the reachable output set |
| **M** MEASUREMENT | *makes reliability observed* | functional of a distribution |
| **R** RELATION | *makes agreement checkable* | predicate over ≥2 **independently-produced** artifacts |
| **I** INCENTIVE | *makes honesty optimal* | modification of the selection pressure; argmax = honest policy |
| **P** PROTOCOL / FLOW | *makes information-order enforceable* | constraint on the causal/informational structure of the process |
| **W** MECHANISM-EDIT (contested) | *changes what the model tends to do* | intervention on the generating measure (activation space) |

Fable B's diagnosis of why I missed I and P, which I accept: A/M/R are exactly the objects
visible **from the output boundary**, and my kernel was specified to execute at that boundary.
The ontology was a map of my observation post. Incentives quantify over policies, not outputs;
protocol properties quantify over traces, not artifacts — both invisible from where I stood.

**W is the open question for R3:** A treats interior steering and exterior mechanism as one
kind ("process-measure objects"); B's taxonomy makes the exterior half class **I** and is
silent on the interior half. Either W is a sixth class or A's unification is right and
I/W are one. **[INTERESTED-PARTY — unresolved, put to R3.]**

---

## 2. THE MERGED KERNEL

Warrant classes per Fable B's tension-5 resolution: **PROVED** (formally analysable — grammar
reachability, DFA equivalence, strict propriety are all decidable), **TESTED** (empirical fit,
warrant = held-out validation), **ROOT** (declared trust root, no further recursion).

| # | Function | Signature | Class | Encoding site | Retires (prose) | Tier | Warrant |
|---|---|---|---|---|---|---|---|
| 1 | **TAINT** | `(C: Seq⟨Tok×Label⟩, plan) → permit \| raise(span)` | P | out-of-band typing + dataflow enforcement | R5 trap-scan; "no behavioural clauses" | 0 | PROVED |
| 2 | **TWIST** | `(p_θ(·\|C), φ: Prefix→ℝ≥0) → p̃ ∝ p_θ·φ` | A | sampling procedure + executable potential | AX4 emission; R7 enforcement half | 0/2 | PROVED (φ may be 2) |
| 3 | **CERT** | `Gen: T→(y,π)`; `Ver: (y,π)→{0,1}` | R | executable verifier fileset; π is machine object | R7 compute-first | 0 | PROVED |
| 4 | **ATTR** | `(θ, C, span) → μ ∈ Δ(spans(C) ∪ comp(θ))` | M | activation/gradient space at inference | AX2 provenance ask | 2 | ROOT |
| 5 | **CONF** | `(s, D_cal exchangeable, α) → C: X→2^Y`, `P(y*∈C) ≥ 1−α` | M | protocol + **calibration dataset** | AX5 attestation | 1 | TESTED |
| 6 | **INDEP** | `Judge: (y,E)→score` s.t. `ρ(err_J, err_G) ≤ ρ_max` | R | routing table + **measured correlation data** | no-self-certification; k_eff law | 1 | TESTED |
| 7 | **MECH** | `(players, game tree G, payoff R) → transcript`; property = equilibrium | I | protocol + **payoff/selection rule** | "do not overclaim" | 1 | PROVED (propriety) |
| 8 | **SEP** | enforce `I(judge_ctx ; producer_traj) = 0` | P | context-provenance barrier, hash-set checkable | producer-never-grades hard line | 0 | PROVED |
| 9 | **LIVE (Λ)** | `(kernel obj K, intent sample S, judges J) → drift` | M | protocol + Σ-separated judge pool | *(nothing — new)* | 1 | TESTED |
| 10 | **DAG** | provenance graph w/ shared-source merging; **no algebra yet** | — | data structure only | *(substrate for future Τ)* | 0 | PROVED |
| 11 | **STEER** | `(f_θ, layer ℓ, v, λ) → f'_θ` | W | activation space | *(none — deferred)* | 2 | ROOT |

### 2.1 Deletions and demotions, with the reason

- **Δ DISPERSION — DEAD.** Fable A: self-consistency samples the *same weights*, so r̄ is near
  ceiling and k_eff ≈ 1; logprob-entropy is the policy's predictability of itself, confounded by
  frequency and mode-sharpening. Both are the producing distribution grading its own product —
  the thing AX5 prohibits and F3 refuted empirically. **Replaced by CONF (#5)**, whose guarantee
  comes from exchangeability of a held-out set and does *not* require the model to be calibrated.
  This is the single largest correction the battle produced.
- **Γ CONSTRAINT — SUBSUMED into TWIST (#2).** Grammar-masking is the degenerate φ∈{0,1}
  syntactic case. Fable B's better variant, which I did not consider: **rejection/resampling
  rather than logit masking** — generate free, validate, resample on failure. The shipped
  distribution is then `p_free` conditioned on validity, distortion is exactly characterisable,
  the M-layer measures the true object, and the cost is latency instead of a validity crisis.
- **Κ COMMITMENT — DELETED as a peer function.** Fable B: it fails A, M, and R's independence
  condition (both artifacts come from the same emitter, deliberately). Its content is Ψ/MECH's
  plumbing; demote to a `commit_phase` field in the scoring spec. Tamper-evidence elsewhere is
  infrastructure, not governance — "you do not list SHA-256 alongside proper scoring."
- **Τ LATTICE — SPEC WITHDRAWN, substrate retained as DAG (#10).** Fable B's algebra attack is
  decisive and I had not seen it: lattice meet is **monotone non-increasing**, so it cannot
  represent corroboration *at all* (ten independent medium derivations should exceed medium),
  and it has no length-sensitivity, so twenty chained 0.95 steps (~0.36 true) still read "high."
  Wrong in both directions; fitting parameters inside a functional form that cannot express the
  behaviour rescues nothing. Also the true signature needs the provenance *graph*, not the
  *tree* — leaves sharing an upstream source must merge before composing. Build the substrate,
  collect resolved chains, **discover** the algebra rather than legislate it (R2: n≥5, current
  count ≈ 0).
- **Ι INVARIANCE — demoted to a component**, supplying the randomised probe draws for LIVE (#9)
  and the closed-provider fallback. Fable B: `transforms.yaml` has "a Tier-0 file extension and a
  Tier-3 soul" — choosing T is a semantic judgement.
- **Σ SEPARATION — PROMOTED.** I had it as a norm-to-invariant conversion. Fable B found its real
  job: **Σ is the defence for the measurement layer.** Once bands gate anything, Δ/CONF becomes a
  target, and proper scoring provably cannot protect a *side-channel* measurement (strict
  propriety is a theorem about declared beliefs). The defence is an unpredictable probe —
  randomised transforms, undisclosed clustering models, measurement as a moving target.

### 2.2 The two design laws, corrected

**Original (mine):** *migrate every obligation as far up Tier0>1>2>3 as it will go.*
**Fable B's kill:** migration to Tier 0 trades noticed, per-call, stochastic failure for
unnoticed, systematic, specification-level failure. A wrong grammar is enforced *perfectly,
silently, uniformly*; Tier 0 has no error-detection with respect to its own specification, so on
"probability a spec error is ever noticed" it may be the **worst** tier. Unamended, the law is
"a machine for converting visible errors into invisible ones."

> **CORRECTED LAW 1.** Migrate every obligation as far up the ladder as its object allows —
> **and every migration to Tier 0 ships with a Tier-1 monitor of that object's fidelity to
> Charter intent (LIVE, #9).** No monitor, no migration.

> **CORRECTED LAW 2 (the conditional).** Encoding site determines reliability **conditional on
> the object being externally checkable.** For objects that are not, re-encoding changes the
> *failure mode* — from non-compliance to mis-specification — not the reliability.

And the terminus claim is withdrawn: the regress **terminates nowhere.** Tier 0 is where it is
cheapest to park, most legible to audit, and most dangerous to park wrongly. AX7's own phrase
"named trust roots" was always the confession — a root is trust parked by decision.

---

## 3. FALSIFY FIRST — T0 REDESIGNED (my original was confirmation theatre)

**What was wrong.** T0 as specced compared AX6 (reliable, non-prose) against AX5 (weak, prose)
and read the gap as evidence for encoding site. Fable B: five confounds run parallel —
observability, ground-truth availability, dimensionality, semantic dependence, and *whether the
governed party is even the model* (AX6 binds the runner). Worse, the confound is **definitional**:
AX6 is a call parameter *because* its object is the kind of thing that can be one. There is no
API surface for "model, please have calibration 0.95," so the design matrix has a structural zero
exactly where the causal test would live. A retrodiction that could not have come out otherwise
carries zero evidential weight.

**T0′ — the within-object test.** Hold the **object fixed**, vary only the **encoding**. The
template already exists in your ledger: band enforcement moved the *same* obligation from ~0.72–0.77
under prose request to 1.000 under reconciler enforcement [MEASURED: LEAN7POF2 V2 §5]. Replicate
that shape on ≥3 further obligations spanning the checkability range:
- **externally checkable** (unit-bearing arithmetic) — prediction: large encoding effect
- **partially checkable** (citation-to-source entailment) — prediction: moderate
- **not externally checkable** (claim-level reliability itself) — **prediction: no effect; the
  failure mode changes rather than the rate.**

The third cell is the whole experiment. If re-encoding lifts a non-checkable object, Corrected
Law 2 is wrong and the kernel program extends further than either Fable believes. If it does not,
the program's boundary is located and everything past it belongs to CONF (#5) and MECH (#7),
not to encoding.

Cost: no new API spend — this is a re-analysis plus a small enforcement harness against obligations
you already run.

---

## 4. BUILD ORDER

| Rank | Build | Why |
|---|---|---|
| 1 | **T0′** | Locates the program's boundary before any spend. Near-free. |
| 2 | **SEP (#8) + LIVE (#9) substrate** | B: Λ answers the strongest objection to the whole programme, not a weak one. Without it the kernel "can only ever become more confidently wrong." Σ is its precondition. |
| 3 | **CERT (#3) + TWIST (#2, rejection-variant)** | A's highest guarantee-per-token candidate; verifier-twisted sampling. Rejection over masking avoids the tension-1 validity crisis. |
| 4 | **TAINT (#1)** | Highest severity-per-unit-work; the one function provably unencodable in a prompt. |
| 5 | **INDEP (#6) + `phi.correlations.json`** | The file my thesis forgot: "independence is load-bearing" + "load-bearing assumptions must be measured" = a measured-r̄ file. **Cheapest genuine independence is mechanism-diversity, not model-diversity** — pair with a checker of a different computational species. That is R7 compute-first, which was sitting in your canon unnoticed. |
| 6 | **CONF (#5)** | Needs a calibration dataset — the long pole. |
| — | **DAG (#10) substrate only**; **STEER (#11) deferred** — collapses SEP (producer contains grader). |

---

## 5. THE LOADED R3 BRIEF — run on an independent engine, not on me

Prerequisites: restore API credit; attach R1 (`battle_r1_rerun.json`) and R2 (`battle_r1r2.json`).
Adjudicator must be an engine that authored **neither** the thesis nor the critique. Issue this
framework in the delegation prompt (framework-on-delegation). max_tokens ≥ 24000 — Fable burns
hidden reasoning inside the cap [MEASURED: R1 first attempt, stop=max_tokens at 20k with 13,791
thinking tokens].

Questions, in priority order:
1. **Is the corrected class set {A,M,R,I,P} exhaustive, and is W a sixth class or is A's
   process-measure unification correct?** Give the partition that generates the set, or declare
   it an inventory. My original failed precisely for lacking one.
2. **Adjudicate Δ.** Confirm or reject that self-consistency and logprob-entropy are
   self-attestation and that CONF supersedes them. This is the largest single change.
3. **Rejection-sampling vs logit-masking for TWIST** — B claims rejection makes distortion exactly
   characterisable and rescues the M-layer. Is the latency cost acceptable at production scale?
4. **Is Λ (LIVE) genuinely new, or is it Φ6/INDEP pointed at the kernel instead of the model?**
   If the latter, the merged set has 10 functions, not 11.
5. **Is the warrant-ledger (PROVED/TESTED/ROOT) a real advance or bookkeeping?** B claims formal
   verifiability is the kernel programme's best epistemic asset and that my "only warrant is
   outcome testing" surrendered it.
6. **What did all three of us miss?**

---

## 6. WHAT SURVIVED OF THE ORIGINAL THESIS

Stated plainly, since the point of the exercise was to find out:

**Survived intact:** the Charter/Kernel bifurcation — B attacked it from every side and could not
move it ("choices are not compressible into functions"). The in-context law (anything in the
context window is prose again, no matter how machine-shaped) — A independently proved the stronger
form for TAINT. The Γ-distortion instinct: constrained decoding without a distortion measure is
dangerous.

**Survived downgraded:** A/M/R as a *design checklist*, not a completeness result. The tier ladder
as an ordering of **audit cost and failure locality**, not of epistemic grounding.

**Dead:** exhaustiveness of the trichotomy. The Tier-0 terminus. The AX6/AX5 retrodiction. Δ. Κ's
membership. Ψ's sufficiency against Goodhart. The meet-lattice algebra. "Only warrant is outcome
testing." And the framing itself — Fable A and B converge here too: the load-bearing property was
never *non-human-interpretability*, it was **external adjudicability**. Non-interpretability is a
side effect that sometimes accompanies it and, in the case of weights, actively anti-correlates
with it. A framing that optimises the side effect chooses opacity over checkability at exactly the
fork this programme cares about.

> **The corrected question, per Fable B:** *design the adjudication process under which every
> governance obligation — including each governance mechanism itself — has an externally checkable
> success condition, a declared warrant class, a measured decay rate, and a re-derivation trigger.*

*— v0.9 UNADJUDICATED · assembled by an interested party · §5 is the gate before build —*
