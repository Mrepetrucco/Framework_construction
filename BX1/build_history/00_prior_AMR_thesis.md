# BEYOND 7POF/AX7 — THE A/M/R KERNEL THESIS + FABLE-vs-FABLE ADVERSARIAL BRIEF
Owner: Enrico · 02 Aug 2026 · under LEAN7POF2 V2 (v1.4, 31 Jul 2026)
Status of evidence: this document is a THESIS + TEST PLAN. Every empirical claim is tagged
[MEASURED: source] or [UNVERIFIED — prediction]. Nothing here is self-certified.

---

## 0. THE COMMITTED ARM (Opus 5, written before any Fable input — anti-anchoring)

### 0.1 The diagnosis 7POF cannot make about itself

7POF/AX7 is a **prose-encoded** governance framework. It asks a language model, in language,
to behave as if certain guarantees held. Its own measurement ledger already contains the
refutation of that method:

- F3: calibration is NOT promptable [MEASURED: F3].
- F8/Upskill4: the measured value of the framework is the deterministic SURFACE
  (bind / provenance / calibration-label / failure-machine), NOT semantics — bare frontier
  models already score ~1.0 on semantic axes [MEASURED: F8, cluster Z=10.18, n=48, r̄=0.747].
- Band enforcement lifts calibration from ~0.72–0.77 to 1.000, and the weakness is
  cross-family (GPT-4o, Gemini, Claude alike) [MEASURED: LEAN7POF2 V2 Reconciler §5].

Read those three together and the conclusion is sharper than "add a decoder layer":

> **Every axis of AX7 that works is one that is already encoded OUTSIDE prose.
> Every axis that is weak is one still encoded IN prose.**

AX6 RESOURCE is the framework's most reliable axis — because max_tokens, the cost meter and
the emission bounds are *call parameters*, not requests. AX5 ATTESTATION is the weakest —
because it is a request. AX4 EMISSION sits in between precisely because half of it (the
differential parser pair) escaped prose and became an executable relation.

This is a **retrodiction the thesis makes about data you already hold**, and it is the first
thing to falsify (see §3, T0).

### 0.2 The trichotomy: A / M / R

Claim: every governance property anyone has ever wanted from a model I/O boundary is one of
exactly three kinds of object. None of the three is a sentence.

| | Function class | Formal shape | What it does | Prose can only… |
|---|---|---|---|---|
| **A** | **ADMISSIBILITY** | a constraint on the reachable output set | makes violation *impossible* | ask for compliance |
| **M** | **MEASUREMENT** | a functional of a distribution | makes reliability *observed* | ask for a self-report |
| **R** | **RELATION** | a predicate over ≥2 independently-produced objects | makes agreement *checkable* | ask for consistency |

A sentence in a system prompt is a **shadow** of one of these: it names the property and hopes
the semantic prior reproduces it. The measured gap between AX7's performance and ceiling on any
axis is exactly the gap between the shadow and the function.

**Mapping (immutable claim of the thesis — falsifiable):**

| AX7 axis | Class | Prose shadow (today) | Real function (proposed) |
|---|---|---|---|
| AX1 INTENT | R | "raise uncertainty as questions" | disagreement between independent intent-parses |
| AX2 EVIDENCE | R | "tie claims to a source" | commitment ordering + citation-entailment check |
| AX3 REASONING | R | R1–R7 trap scan | N-version judgement; disagreement = signal |
| AX4 EMISSION | A | "emit only the envelope" | compiled grammar; violation unreachable |
| AX5 ATTESTATION | M | "deterministic band from provenance" | dispersion functional, band FITTED not asserted |
| AX6 RESOURCE | A | *(already non-prose — the control case)* | unchanged |
| AX7 FAILURE | R | branch-on-class flowchart | decidable lattice over agreement predicates |

Note AX6 is the control. If the thesis is right, AX6 needs no upgrade — and it doesn't.

### 0.3 The eight kernel functions

These are the **non-human-interpretable logic functions**. Each has a signature; none is a
sentence; each supersedes a prose obligation. Ordered by class.

**Γ (Gamma) — CONSTRAINT.** `Γ : (grammar G, decode state s) → mask ⊆ V`
Compiled automaton (GBNF/DFA/json-schema-strict) masking logits at each step. Converts AX4
from advisory to structurally unviolatable — bind-rate becomes 1.000 *by construction*, not by
measurement.
**The trap the prior decoder plan under-weighted:** masking renormalises the conditional. A
grammar can *raise binding while lowering truthfulness*, because the model is forced through
tokens it assigned low probability. **Binding and calibration are in tension.** Therefore Γ is
incomplete without a *constraint-distortion budget*: measure `KL(p_constrained ‖ p_free)` on
the claim-bearing spans and fail the run if it exceeds a pre-registered bound. A grammar with
no distortion budget is an uninstrumented claim (R1) wearing a hard hat.

**Τ (Tau) — TYPE / EFFECT LATTICE.** `Τ : derivation DAG → confidence ∈ L`
7POF's R3 ("certainty ≤ weakest premise") is a hand-rolled approximation of a **meet operation
on a lattice**, applied per-claim, by prose, with no composition calculus. Consequence: **a
chain of governed calls is not itself governed.** 7POF has *no* end-to-end reliability
semantics for a multi-agent pipeline — which is exactly what 7POF is for. This is the largest
unbuilt gap in the framework.
Real function: every claim carries a typed **derivation tree** (leaves = provenance classes,
nodes = inference operators with declared confidence transformers). Composition is lattice meet
plus operator-specific downgrade. The artifact is a DAG, not prose; end-to-end reliability
becomes *computed*, not asserted.

**Δ (Delta) — DISPERSION.** `Δ : (model, input, k) → ℝ`
The direct answer to F3. A confidence *label* is a semantic act (unpromptable). A confidence
*measurement* is a functional of the output distribution (always available). Use **semantic
entropy** — entropy over meaning-clusters, not token sequences — because token-level entropy
conflates paraphrase with uncertainty and is therefore near-useless on free-form claims.
Band assignment must be **fitted on held-out resolved claims**, never asserted. Note the
regress this opens: meaning-clustering needs an equivalence relation, which is another model
(see §0.4).

**Ψ (Psi) — PROPER SCORING.** `Ψ : (report r, outcome ω) → ℝ`, maximised in expectation at r = belief
Prose says "do not overclaim." A strictly proper scoring rule (log / Brier) makes overclaiming
*lose*. This is the only primitive here that changes the **argmax** rather than the constraint
set — it is incentive alignment, not policing.
Requires resolution. For claims that never resolve, use **peer-prediction / Bayesian truth
serum**: score a report against *other* independent reports AND against each reporter's
prediction of the others' distribution. Truthfulness becomes the equilibrium **with no oracle
at all**. This is the deepest available move against the "who grades the grader" regress and
7POF contains nothing like it.

**Ι (Iota) — INVARIANCE.** `Ι : (model, input x, transform group T) → agreement over orbit T·x`
Δ samples one input many times. Ι samples the input's *orbit*: paraphrase, reordering,
unit-change, distractor injection, irrelevant-context padding. A claim stable across T·x is
categorically different from one that is not, and Ι catches prompt-sensitivity that Δ is blind
to by construction. Cheap, engine-agnostic, needs no logprobs — so it is the one M-class
function that survives on **closed** providers.

**Σ (Sigma) — SEPARATION.** `Σ : enforce I(grader_context ; producer_trajectory) = 0`
"A producing component never grades its own product" is a hard line in 7POF — and it is
enforced by *asking*. Structurally it is an **information barrier**: the grader's context must
be provably free of producer-side tokens. Checkable deterministically by hash-set intersection
over context spans. Converts a norm into an auditable invariant.

**Κ (Kappa) — COMMITMENT.** `Κ : artifact → digest`, with commit-before-reveal ordering
You cannot instruct a model into non-retroactivity. You *can* order the protocol so that
retroactivity becomes visible: the model commits `H(prediction)` in phase 1, receives evidence
in phase 2, and any drift between committed and revealed claim is detected rather than
discouraged. The binding artifact is a hash — maximally non-human-interpretable, zero trust in
the emitter. Pairs with Ψ to make scoring non-gameable.

**Φ (Phi) — N-VERSION AGREEMENT.** `Φ : (produce₁, produce₂, …) → {agree, disagree-fail-closed}`
The framework's single best existing non-prose element is the **differential parser pair**:
two structurally different decoders must agree, and disagreement fails closed. Φ is the
generalisation of that to *every* judgement in the system — extraction, classification,
band assignment, trap detection. Independence is the whole asset: two implementations sharing
a prompt, a family, or a training corpus are one implementation wearing two hats. 7POF's own
IDENTICAL-ANSWER SUSPICION rule is the intuition; Φ is the mechanism.

### 0.4 The grounding hierarchy (the underpinning result)

Every one of the above bottoms out somewhere. Ranked by how much trust the guarantee costs:

```
TIER 0  deterministic computation   — parser agreement, hashes, arithmetic, grammar reachability
TIER 1  multi-model agreement       — Φ, Σ (independence is the load-bearing assumption)
TIER 2  single-model judgement      — NLI clustering for Δ, entailment checks for AX2
TIER 3  prose instruction           — 7POF / AX7 as they stand today
```

**The design law that follows:** *migrate every governance obligation as far UP this hierarchy
as it will go, and label the tier it lands on.* An obligation stuck at Tier 3 is not governed;
it is requested. This single rule generalises the entire framework and tells you, for any new
obligation, exactly what to build.

Corollary, and the honest cost: Tier 2 measurement is circular at the limit (the grader is a
model). The regress terminates ONLY at Tier 0. So a mature kernel is a Tier-0 skeleton with
Tier-1 flesh, and every Tier-2 dependency is declared as a named trust root — exactly as AX7's
design law already demands ("named trust roots"), but applied to the *measurement stack*
rather than only to the parser pair and the owner.

### 0.5 How to encode it — the bifurcation

The framework must **split into two artifacts with a typed boundary between them**:

**(1) The CHARTER — human-entered, irreducibly prose, deliberately small.**
Intent, values, owner rulings, priority ordering, the naming law, what counts as harm. These
are not compressible into a kernel because they are *choices*, not functions. Target: ≤1 page.

**(2) The KERNEL — a non-human-interpretable, signed fileset. Not read; executed and tested.**

```
kernel/
  envelope.gbnf            Γ   compiled emission grammar
  distortion_budget.json   Γ   pre-registered max KL(constrained‖free) per span class
  bands.fit.json           Δ   dispersion→band mapping, FITTED, with fit provenance + n
  transforms.yaml          Ι   the invariance group T
  scoring.spec.json        Ψ   proper rule + peer-prediction params for unresolvables
  derivation.types         Τ   confidence lattice + operator transformers
  failure.dfa              Φ   agreement predicates → terminal states
  separation.policy        Σ   context-provenance barrier rules
  MANIFEST.sha256          Κ   hash of every file above; the kernel's own identity
```

**The load-bearing design law — and the one most likely to be got wrong:**
> **The kernel executes AT the boundary, in the runner. It never enters the model's context.**
> Anything placed inside the context window is prose again, no matter how machine-shaped it
> looks. A JSON schema pasted into a system prompt is Tier 3 cosplaying as Tier 0.

This is the precise sense in which the answer moves past the prior decoder-layer plan: the
decoder layer is one file (`envelope.gbnf`) in a nine-file kernel, and constrained decoding
without `distortion_budget.json` is actively dangerous.

**Third encoding site, flagged as open:** weights (fine-tune / activation steering / probe
heads) — non-human-interpretable in the strongest sense, and the only site where a property can
become *dispositional* rather than *enforced*. Cost: unauditable, un-versionable, and it
collapses Σ (the producer now contains the grader). My position: **do not** put governance in
weights until Tier-0/1 kernel is saturated. This is a live disagreement to put to Fable.

### 0.6 Known tensions I am NOT resolving (put these to Fable)

1. **Γ vs Δ** — constraint distorts the very distribution Δ measures. Do you measure dispersion
   under the grammar (operationally honest, statistically compromised) or free (clean but
   measuring a different object than you ship)?
2. **Goodhart on Δ** — once dispersion sets the band, any optimisation pressure degrades the
   signal. Proper scoring (Ψ) is the standard defence; is it sufficient here?
3. **Φ independence is unpurchasable** — frontier models share architecture, data and RLHF
   lineage. Correlated failure is the norm. What is the *cheapest genuine* independence axis?
4. **Τ has no empirical grounding** — the confidence lattice's operator transformers are
   currently guesses. They must be fitted, which needs resolved multi-hop chains, which nobody
   has. Is Τ therefore premature, or is it the highest-value thing to build precisely because
   it is missing everywhere?
5. **Auditability cost** — a non-human-interpretable kernel cannot be reviewed by reading. Its
   only warrant is outcome testing. Is that acceptable for a framework whose purpose is trust?

---

## 1. FABLE-vs-FABLE BRIEF (the push past)

**Delegation posture (framework-on-delegation, LEAN7POF2 V2):** issue the framework in the
delegation prompt. Keep the brief **strategic and LOOSE** — no forced input schema. [Basis:
owner ruling, 30 Jul — Opus over-tightens Fable's input schema and malforms its leverage.]
Bound `max_tokens ≥ 2× expected visible`. Never Haiku (J1).

### Round 1 — Fable A: independent construction (no sight of §0)
> You are operating under LEAN7POF2 V2 (attached). It is a prose-encoded governance framework
> for AI model input/output. Its own measurement ledger says calibration is not promptable, and
> that its measured value is a deterministic surface rather than semantics.
>
> Identify the fundamental logic functions for AI model I/O that are NOT human-interpretable —
> functions that underpin, meet, or advance past what this framework is reaching for in prose.
> Do not restrict yourself to decoding-time constraints or confidence estimation; those are the
> obvious first answers and I want what lies past them. Give each function a signature. Then
> say how it is encoded — human-entered instruction, executable fileset, model weights, or a
> site I have not named. Argue for a minimal complete set and say what makes it complete.
> Be willing to conclude the framework's whole approach is category-mistaken.

*Purpose: an uncontaminated second construction. Overlap with §0.3 is evidence of convergence;
non-overlap is the yield.*

### Round 2 — Fable B: adversarial break of the A/M/R thesis
> [attach §0 in full]
> Break this. Specifically: (a) is the A/M/R trichotomy exhaustive, or is there a fourth class
> of governance object that is neither a constraint on outputs, a functional of a distribution,
> nor a relation between artifacts? (b) Is the grounding hierarchy's Tier-0 terminus real, or
> does determinism merely relocate the trust rather than ground it? (c) The thesis claims AX6
> works BECAUSE it is non-prose — is that causation or selection effect (AX6 may simply govern
> an easier object)? (d) Attack the five open tensions in §0.6, hardest first. (e) Name the one
> function in §0.3 that should be deleted and the one that is missing.

*Purpose: this is the actual battle. (c) is the thesis's weakest joint and I want it hit hard.*

### Round 3 — Fable A vs Fable B: adjudication
Give each the other's output. Ask for: points conceded, points held with reasons, and a single
merged minimal kernel with each file justified or dropped. Then owner + Claude screen the merge
before anything is built (framework-on-delegation: the delegate's output is re-screened, never
adopted).

### Budget
| Round | Calls | max_tokens | Est. cost (claude-fable-5 @ $10/$50 per M) |
|---|---|---|---|
| R1 | 1 | 16k | ~$0.80 [UNVERIFIED — prediction] |
| R2 | 1 | 24k | ~$1.20 [UNVERIFIED — prediction] |
| R3 | 2 | 16k each | ~$1.60 [UNVERIFIED — prediction] |
| **Total** | **4** | | **~$3.60 — inside the $3.00–$4.00 band** [UNVERIFIED — prediction] |

Not yet spent: requires `ENVs.zip` (or any `KEY=VALUE` file carrying `ANTHROPIC_API_KEY`) on
the uploads mount. Actual cost this session: $0.00.

---

## 2. WHAT THIS REPLACES

The prior decoder-layer calibration plan (Phase 2 of `20260802_next_turn_plan_port`) is
**subsumed, not discarded**: constrained decoding = Γ, logprob-entropy/self-consistency = Δ.
Two of nine kernel components. The material additions are Τ (composition — the biggest hole),
Ψ (incentive alignment — absent from every version of the framework), Κ, Σ, Ι, Φ, the A/M/R
trichotomy as the organising claim, the grounding hierarchy as the design law, and the
charter/kernel bifurcation as the encoding answer.

Phase 1 (the AX7-integration adversarial test) is **unaffected and should still run first** —
it measures the prose framework's marginal value, which is the baseline this whole thesis is
measured against.

---

## 3. FALSIFICATION FIRST (do this before building anything)

**T0 — the retrodiction test, and it is nearly free.** The thesis predicts: across the existing
F-ledger, axis reliability should rank by encoding tier, with AX6 (non-prose) top and AX5
(prose) bottom, independent of axis difficulty. Re-score the ledger you already hold. If AX5
weakness is better explained by task difficulty than by encoding site, §0.2 collapses and
everything downstream is decoration.

Run T0 before spending on Fable. It costs one analysis pass over data already in hand, and it
is the only step here that can kill the thesis cheaply.

*— End. Charter is prose; kernel is not; the boundary between them is the whole design. —*
