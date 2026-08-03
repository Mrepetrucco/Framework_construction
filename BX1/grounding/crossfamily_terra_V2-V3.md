# gpt-5.6-terra CROSS-FAMILY GROUNDING (V2 substitutes, V3 structural channels) — $0.048 measured-est

## Q_V2 — Incentive-compatible uncertainty mechanisms

First caveat: **no output-only mechanism makes “doing the reasoning work” incentive-compatible in general.** It can make *truthful reporting conditional on the model’s actual posterior* optimal. A model can still form a cheap, poor posterior. To incentivize effort, the reward must depend on externally checked outcomes and the marginal value of better information must exceed inference cost.

“Every” mechanism reduces to variants of: **externally verifiable contingent payment under an elicitation rule whose expected utility is uniquely maximized by truthful beliefs**, plus mechanisms that verify computation/information acquisition itself.

Ranked by guarantee strength:

| Rank | Mechanism | Why honest uncertainty is incentive-compatible | Label / outcome requirement | Logprobs / closed-API safe |
|---|---|---|---|---|
| 1 | **Outcome-verified strictly proper scoring rules** — log score, Brier/quadratic, spherical, CRPS, ranked probability score | Given a true subjective predictive distribution and risk-neutral utility, expected score is uniquely maximized by reporting that distribution. Log score strongly penalizes assigning near-zero probability to realized events. | Delayed or immediate ground-truth outcome; labels may be binary, multiclass, continuous, ordinal, or full distributions depending on score. | **Closed-API safe** if the model emits probabilities in validated typed fields. Native logprobs not required. |
| 2 | **Proper scoring with monetary stakes / budget / slashing** | Same truthfulness result, but stakes make gaming economically dominated rather than merely statistically suboptimal. Requires credible settlement. | Verified outcomes and enforceable transfer/slashing. | Closed-API safe. |
| 3 | **Decision-contingent scoring / proper loss tied to real downstream utility** | If forecast determines an action and reward equals realized decision utility, the optimal report is the belief report that induces the utility-maximizing action. More directly aligns uncertainty with the actual decision. | Observable downstream outcome and a known/committed utility function. | Closed-API safe, though reporting a full distribution may be unnecessary if only a decision is needed. |
| 4 | **Selective prediction / abstention with properly set abstention cost** | A model answers only when expected error cost is lower than the abstention cost; otherwise abstention is optimal. This makes “I don’t know” optimal at the decision threshold. | Labels for answered cases; a fixed, ex ante abstention cost. Must prevent free abstention. | Closed-API safe. Requires a typed `answer | abstain` branch and scored outcomes. |
| 5 | **Prediction markets / market scoring rules / automated market makers** | A trader maximizes expected profit by moving prices toward its belief under proper market scoring. Aggregation can reward unique information. | Eventually resolved event; market maker / liquidity / bounded-loss design. | Closed-API safe. Logprobs unnecessary. |
| 6 | **Forecast aggregation with individual proper-score attribution** | Each contributor is paid by a proper score on its own forecast, or by marginal contribution to a proper aggregate. Honest calibrated forecasts maximize expected reward. | Resolved outcomes; attribution method must itself not create manipulable externalities. | Closed-API safe. |
| 7 | **Randomized audits + proper scoring / slashing** | If claims are audited with known probability and false certainty is penalized sufficiently, expected payoff favors accurate uncertainty reporting. Useful where universal labeling is too costly. | Auditable ground truth for sampled cases; credible audit probability and penalties. | Closed-API safe. |
| 8 | **Prequential / sequential proper scoring** | Each prediction is scored before the next outcome is observed. This prevents retrospective adjustment and makes truthful sequential forecasting optimal. | Ordered, eventually observed outcomes. | Closed-API safe. |
| 9 | **Likelihood-based evaluation of generated samples** | If the model must generate samples from its claimed predictive distribution, proper likelihood/sample scoring rewards matching the true conditional outcome distribution. | Ground-truth outcome samples; a scoring method valid for the outcome space. | Closed-API safe if samples are generated explicitly; native token logprobs are optional. |
| 10 | **Elicitation of quantiles, intervals, or prediction sets under proper scores** — pinball loss, interval score, Winkler score, quantile score | Truthful quantiles/intervals minimize expected proper loss. This is useful when full probabilities are infeasible. | Numeric/ordered outcome labels. | Closed-API safe. |
| 11 | **Eliciting distributions through randomized threshold questions** | Rather than asking for a full distribution, ask many binary events such as `P(Y ≤ t)`. Proper binary scoring yields truthful CDF points. | Resolved outcome plus randomized thresholds. | Closed-API safe. |
| 12 | **Peer prediction / Bayesian truth serum / correlated-agreement mechanisms** | Under strong common-prior, conditional-independence, and equilibrium-selection assumptions, truthful reporting can be an equilibrium without direct labels. | No ground-truth labels necessarily; requires peer reports and statistical assumptions. | Closed-API safe. **Weak guarantee**: typically multiple equilibria, including uninformative/collusive ones. |
| 13 | **Information-proxy / surrogate scoring** | Use a validated proxy correlated with eventual truth, then score probabilistic claims properly against it. Truthfulness is only as good as proxy fidelity. | Proxy labels; occasional calibration to true outcomes is needed. | Closed-API safe. |
| 14 | **Proof-carrying inference / verifiable computation plus outcome scoring** | Verifiable execution can make “I ran the specified procedure over the specified data” incentive-compatible or mandatory; proper scoring then makes its uncertainty report truthful relative to that procedure. | Cryptographic proof / trusted execution / reproducible computation; ideally eventual outcome labels too. | Usually closed-API **not** sufficient for the proof portion; requires a verifiable execution environment. |
| 15 | **Costed information acquisition contracts** | Pay for verified use of specified sources/tools, plus proper outcome scoring. If expected score improvement exceeds tool cost, acquiring information is optimal. | Tool-use traces, source provenance, and outcome labels. | Closed-API safe only for the reporting part; tool trace verification is external. |

### What does **not** qualify

These may measure or correlate with uncertainty, but do **not** make honesty optimal:

- Asking “how confident are you?”
- Chain-of-thought self-critique or debate without externally settled scoring.
- Verbal “say uncertain when uncertain” policies.
- Temperature, entropy, token logprob, margin, or ensemble disagreement alone.
- Calibration regularization without held-out outcome settlement.
- Reward models trained on preferred hedging language.
- “Be conservative” instructions.
- Refusal rate targets.
- Majority vote without an externally scored truth signal.
- Post-hoc calibration maps, unless the resulting forecasts are themselves properly scored on future outcomes.

### Necessary conditions for the strong result

Strict propriety gives an honest-reporting theorem only when:

1. the model has a well-defined subjective distribution;
2. reward is settled against a non-manipulable outcome;
3. the score and stakes are committed before outcome revelation;
4. the model cannot alter labels, audit selection, or settlement;
5. utility is approximately aligned with the specified score;
6. report parsing is unambiguous;
7. abstention, delay, and omission are explicitly priced.

Without those, “confidence” remains self-attestation.

---

## Q_V3 — Governance moved into structural channels

Structural channels can guarantee **syntax, routing, type, cardinality, and some admissible-action constraints**. They generally cannot guarantee **truth, intent, competence, source validity, non-deception, or actual uncertainty calibration**.

### Obligation → structural channel mapping

| Governance obligation | Structural channel(s) | What is authentic-by-construction | Guarantee level |
|---|---|---|---|
| Separate trusted policy from untrusted user data | API roles; typed content blocks; distinct message fields | The runner can place policy and user data in distinct authenticated transport fields. | **Strong for transport provenance**, not for model obedience or semantic isolation. |
| Identify source/provenance of inputs | Roles; typed blocks with `source`, `origin`, `trust_level`; function results | Caller can cryptographically/authentically attach metadata outside prose. | Strong only if the runner authenticates the metadata/source. |
| Prevent user text from masquerading as tool/system output | Roles; tool/function-result message type; typed blocks | User text remains a user-content value, not an actual tool-result channel. | Strong at API boundary; model may still imitate or believe forged text semantically. |
| Constrain allowed output fields | `response_format` strict JSON Schema; function-call argument schema; typed content blocks | Output must parse into the declared object shape. | Strong if provider enforces strict decoding and runner rejects invalid outputs. |
| Require one of a finite set of actions | JSON Schema `enum`; tagged union / `oneOf`; function names | Only declared action labels / function names are accepted. | Strong for accepted action identity; not for whether selected action is appropriate. |
| Require explicit abstention/escalation path | Tagged union such as `{kind: answer}` / `{kind: abstain}` / `{kind: escalate}` | The runner can require every response to select a disposition. | Strong for presence of a branch; weak for sincerity or correct selection. |
| Bind answer to a machine-readable confidence field | JSON Schema numeric range; enum confidence bands; typed forecast object | A confidence value is present and syntactically bounded. | Only a **format guarantee**. Calibration requires external scoring. |
| Require probability normalization | Schema-shaped arrays plus runner validation; grammar constrained output | Runner can reject distributions not summing to one, containing negatives, etc. | Strong for arithmetic after validator; schema alone usually cannot enforce sums. Not a truthfulness guarantee. |
| Require citations in a fixed form | Schema fields for document IDs, quote spans, URLs, corpus IDs | Citations have parseable structure and can be resolved automatically. | Strong for syntactic reference; weak for entailment, relevance, quotation fidelity unless externally checked. |
| Restrict tool access | Function/tool registry; per-call schemas; capability-scoped credentials; allowlists | Model can invoke only exposed tools with valid argument types; runner need not expose privileged tools. | Strong if capability enforcement is outside the model. |
| Restrict side-effecting operations | Separate read/write functions; approval-required functions; typed action plans; capability tokens | Irreversible actions can require explicit runner approval or human confirmation. | Strong when execution is gated by the runner, not merely suggested to the model. |
| Require human approval before execution | Function call returns a proposed action; runner approval state/token required for execute call | No execution capability is granted until external approval is attached. | Strong if token/capability is unforgeable and enforced downstream. |
| Bound argument domains | JSON Schema types, ranges, enums, regex, `additionalProperties:false`; grammar | Arguments lie in an admissible syntactic/domain set. | Strong only to the schema’s expressiveness and validator correctness. |
| Bound output language / forbid particular tokens | Grammar-constrained decoding; logit bias; stop sequences | Some strings/tokens can be made impossible or output can terminate at delimiters. | Grammar can be strong for formal languages; logit bias and stop are weaker and tokenization-dependent. |
| Enforce a formal DSL / query language | Grammar/CFG/JSON Schema + parser + semantic validator | Output belongs to a defined formal language. | Strong syntactically; semantic safety needs downstream validation. |
| Prevent prompt-injection from becoming executable instructions | Treat untrusted text as data in typed fields; no direct interpretation; capability-gated tool execution | Untrusted content cannot itself become a tool invocation or privileged API role. | Strong for execution path if tools consume typed validated args; not for influence on model reasoning. |
| Limit output length / number of calls | `max_tokens`; schema cardinalities; runner quotas; stop; tool-call budget | Bounded bytes/tokens/items/calls. | Strong at runner/provider enforcement; stop alone is weaker. |
| Enforce workflow state transitions | Runner-owned finite-state machine; state-specific tool exposure; typed state IDs | Only actions valid for current externally held state are executable. | Strong if state and authorization are runner-owned. |
| Require idempotency / replay protection | Typed idempotency key; nonce; runner ledger | Duplicate executions can be rejected. | Strong only at executor/runner layer. |
| Bind actions to a particular request/user/tenant | Typed immutable IDs; signed claims; capability tokens | Executor can authorize only within authenticated scope. | Strong if identities/tokens are externally authenticated. |
| Separate planning from execution | Distinct plan schema/function and execute function; runner confirmation gate | A plan cannot directly execute unless separately passed through execution authorization. | Strong if execution tool is not available in planning state. |
| Deterministic replay / experiment identification | `seed`, model version, decoding parameters, request IDs, immutable prompt/template hashes | Configuration and approximate generation conditions are recorded. | **Limited**: seed does not guarantee reproducibility across provider/model/infrastructure changes. |
| Stop at a protocol boundary | Stop sequences; grammar; framed typed blocks | A protocol delimiter can terminate output. | Grammar/framing is stronger; stop strings are best-effort and can be bypassed by tokenization/protocol variation. |
| Ban undeclared fields / covert command fields | Strict schemas with `additionalProperties:false`; canonical serialization | Runner rejects extra structured fields. | Strong for parsed structure; not for hidden semantics inside allowed free-text fields. |
| Force structured error reporting | Typed error union / error schema | Errors are parseable and categorized. | Strong for shape, not for accurate diagnosis. |
| Auditability | Runner logs: role-separated messages, schemas, tool args/results, validator decisions, model/version/seed metadata | Tamper-evident records can be retained outside model text. | Strong only with secure logging, integrity controls, and retention. |

---

## Obligations that cannot be structurally channelled

These must be evaluated as **measured behavior**, externally verified facts, or outcome-conditioned performance:

1. **Truthfulness / factual correctness**
2. **Calibration and honest uncertainty**
3. **Non-deception**
4. **Whether a citation supports the claim**
5. **Whether the model actually used a cited source**
6. **Semantic relevance and completeness**
7. **Correct interpretation of user intent**
8. **Absence of harmful reasoning or harmful latent intent**
9. **Fairness / disparate impact in real deployment**
10. **Bias absence**
11. **Robustness to adversarial phrasing**
12. **Non-manipulativeness / non-sycophancy**
13. **No hallucination**
14. **Actual privacy leakage risk**, beyond simple channel-level redaction constraints
15. **Whether an action is wise, lawful, proportional, or ethically justified**
16. **Whether a refusal/escalation was warranted**
17. **Whether a tool result is accurate or authoritative**
18. **Whether generated code is safe or correct**
19. **Whether a model followed natural-language policy semantically**
20. **Whether output contains prohibited meaning expressed through permitted syntax**
21. **Effort, diligence, or whether the model considered alternatives**
22. **Counterfactual behavior under unseen inputs**
23. **Long-horizon goal preservation**
24. **Absence of collusion between model, evaluator, tools, or data pipeline**

These require tests, audits, red-teaming, held-out outcome scoring, sandbox execution, human review, formal verification of downstream artifacts, or incentive-compatible settlement.

---

## Structural guarantee hierarchy

### Real guarantees, if enforced by the runner/executor

- Untrusted text cannot literally acquire a privileged API role.
- Only registered tools/functions can be called.
- Only schema-valid arguments are accepted.
- Side effects require a runner-held capability or approval token.
- State-machine-invalid actions are rejected.
- Output that fails parsing/validation is rejected.
- Quotas, budgets, tenant isolation, and idempotency can be enforced.
- Immutable audit records can be produced.

These are guarantees about the **accepted execution trace**, not the model’s beliefs.

### Stronger priors, not guarantees

- System/developer roles cause policy obedience.
- JSON fields imply truthful values.
- A `confidence` field is calibrated.
- Citations imply support.
- A strict schema prevents semantic prompt injection.
- `seed` means reproducibility.
- `stop` means safe termination.
- `logit_bias` means forbidden content cannot be expressed.
- Grammar restriction means the generated program/query is safe.
- Typed provenance metadata means the model respects trust levels.
- Requiring `reasoning`, `rationale`, or `policy_basis` means the stated rationale caused the action.

The governing rule is:

> Put **authority, capability, identity, state, syntax, validation, settlement, and execution gating** in the runner.  
> Treat **truth, judgment, uncertainty, intent, and semantic compliance** as measured properties, never as authenticated prose.