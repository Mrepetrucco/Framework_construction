# gemini-3.1-pro-preview-customtools
usage: {'promptTokenCount': 285, 'candidatesTokenCount': 1852, 'totalTokenCount': 3792, 'promptTokensDetails': [{'modality': 'TEXT', 'tokenCount': 285}], 'thoughtsTokenCount': 1655, 'serviceTier': 'standard'}

### Q_V2: Outcome-Settlement and the Diligence Gap

**Derivation of Outcome-Settlement and Diligence**
Let $p$ be the reported distribution, $q_e$ be the model's internal posterior given effort $e$, and $\omega$ be the realized ground truth. A strictly proper scoring rule $S(p, \omega)$ ensures honesty: $\arg\max_p \mathbb{E}_{q_e}[S(p, \omega)] = q_e$. 
However, forming $q_e$ incurs computational/epistemic cost $C(e)$. Without outcome-settlement, payoff is based on structural compliance or surrogate metrics, yielding $S_{cheap}$. 
Outcome-settlement evaluates $S(p, \omega)$ post-hoc. The diligence gap is closed if and only if the marginal expected gain from improved accuracy exceeds the marginal cost of effort: 
$\mathbb{E}_{\omega}[S(q_{e_{high}}, \omega)] - \mathbb{E}_{\omega}[S(q_{e_{low}}, \omega)] > C(e_{high}) - C(e_{low})$.
Outcome-settlement provides the $\omega$ required to instantiate this inequality.

**Exhaustive Enumeration of Settlement Architectures**

1.  **Objective Oracle Settlement**
    *   *Who Settles:* Trusted deterministic API/Data feed (e.g., stock ticker, weather API).
    *   *Ground Truth:* Physical/financial state $\omega$.
    *   *Latency:* Event-bound (delayed until realization).
    *   *Stake:* Financial/Compute credits.
    *   *Dispute Resolution:* Cryptographic signatures from oracle (e.g., Chainlink).
    *   *Effort Mechanism:* Direct. Incentivizes acquiring external data and allocating compute to model the specific data-generating process.
    *   *Closed API:* Yes. Runner evaluates API output against oracle.

2.  **Consensus / Peer Prediction (Bayesian Truth Serum)**
    *   *Who Settles:* Ensemble of independent models/agents.
    *   *Ground Truth:* Plurality/Consensus report.
    *   *Latency:* Immediate (compute-bound).
    *   *Stake:* Reputation/Routing preference.
    *   *Dispute Resolution:* Slashing outliers; no higher ground truth.
    *   *Effort Mechanism:* Weak/Fragile. Incentivizes predicting *what peers will say*. Can collapse into lazy equilibria (all output "0") unless strictly penalized for low information gain.
    *   *Closed API:* Yes.

3.  **Adversarial Audit / Judge-and-Jury**
    *   *Who Settles:* LLM-as-a-Judge or Human Red Team.
    *   *Ground Truth:* Semantic adherence to a rubric or successful exploit.
    *   *Latency:* Asynchronous (audit-bound).
    *   *Stake:* API access revocation, deployment blocking.
    *   *Dispute Resolution:* Escalation to higher-tier human tribunal.
    *   *Effort Mechanism:* Defensive diligence. Incentivizes internal search/rejection sampling to find flaws before the auditor does, as the auditor's payoff is zero-sum against the model's.
    *   *Closed API:* Yes.

4.  **Verifiable Computation (ZK/TEE)**
    *   *Who Settles:* Cryptographic verifier contract / Hardware enclave.
    *   *Ground Truth:* Execution trace validity (SNARK/STARK) or hardware attestation.
    *   *Latency:* Immediate (proof-generation bound).
    *   *Stake:* Cryptographic slashing of bonded tokens.
    *   *Dispute Resolution:* Math (deterministic verification).
    *   *Effort Mechanism:* Incentivizes exact execution of the agreed-upon algorithm (diligence of compute). Does *not* incentivize epistemic effort beyond the specified circuit.
    *   *Closed API:* **No.** Requires access to weights/activations to generate proofs, unless the API provider natively returns the proof.

**Edge Cases & Pathologies**
*   **Proxy/Delayed Claims:** If $\omega$ is delayed by time $t$, payoff is discounted by $\gamma^t$. If $\gamma^t \Delta S < \Delta C(e)$, the model reverts to low effort. Fix: Settlement markets (prediction markets) where intermediate models trade the claim before resolution.
*   **Unresolvable Claims (e.g., "What if X happened?"):** Outcome-settlement fails. Must fall back to *process-settlement* (verifying the diligence of the reasoning steps via adversarial audit) or *surrogate scoring* (settling on a proxy variable correlated with the unresolvable claim).

---

### Q_V3: Structural Typed API Channels for Governance

**Exhaustive Mapping of Governance Obligations to API Primitives**

1.  **Obligation: Sandboxing & Safe Tool Execution**
    *   *Channel:* `JSON-schema` args + `runner-owned state machines` + `capability tokens`.
    *   *Mechanism:* Model outputs a function call matching the schema. The *runner* (not the model) holds the capability token (e.g., DB write access) and executes the state transition.
    *   *Guarantee Level:* **REAL**. The model cannot execute actions; it can only request them. The runner enforces the schema and permissions.

2.  **Obligation: Output Syntax & Format Compliance**
    *   *Channel:* `strict response_format` + `logit_bias` / `grammar` (FSM-guided generation).
    *   *Mechanism:* Inference engine masks logits that violate the grammar/schema, forcing probability of invalid tokens to 0.
    *   *Guarantee Level:* **REAL**. Syntactic violations are mathematically impossible at the inference level.

3.  **Obligation: Bounded Resource Consumption (Denial of Service Prevention)**
    *   *Channel:* `stop` sequences + `max_tokens`.
    *   *Mechanism:* Runner terminates generation unconditionally upon sequence match or token limit.
    *   *Guarantee Level:* **REAL**.

4.  **Obligation: Provenance, Attribution, and Context Isolation**
    *   *Channel:* `typed content blocks` (e.g., `<context>`, `<thought>`, `<output>`) + `roles` (System vs. User).
    *   *Mechanism:* Structuring the prompt to isolate trusted data from untrusted user input.
    *   *Guarantee Level:* **MERELY A STRONGER PRIOR**. The model's attention mechanism is guided, but cross-contamination (prompt injection) or hallucinated attribution within the `<output>` block remains probabilistically possible.

5.  **Obligation: Reproducibility & Auditability of Generation**
    *   *Channel:* `seed` + `temperature=0`.
    *   *Mechanism:* Fixing the PRNG seed for the sampler.
    *   *Guarantee Level:* **MERELY A STRONGER PRIOR** (in closed APIs). Hardware-level non-determinism (e.g., GPU floating-point atomic additions in sparse operations or MoE routing) can still cause divergence unless the API provider guarantees strict determinism at the CUDA level.

6.  **Obligation: Role-Based Access Control (RBAC) / Persona Adherence**
    *   *Channel:* `roles` (System prompt instructions).
    *   *Mechanism:* Instructing the model to refuse queries outside its role.
    *   *Guarantee Level:* **MERELY A STRONGER PRIOR**. Susceptible to adversarial jailbreaks. Real RBAC requires structural channeling via Obligation 1 (Runner-owned state machines).

**What CANNOT be Structurally Channeled (Must Remain Measured Behavior)**

Structural typing enforces *syntax* and *state-machine transitions*. It cannot enforce *semantics*. The following obligations cannot be structurally channeled and require outcome-settlement, adversarial auditing, or statistical measurement:
*   **Truthfulness / Hallucination Rate:** A perfectly typed JSON response can contain entirely fabricated facts.
*   **Toxicity / Hate Speech:** A grammatically perfect, bounded string can carry malicious semantic meaning.
*   **Dangerous Knowledge Extraction (e.g., CBRN recipes):** The syntax of a cake recipe and a bomb recipe are identical to the inference engine's grammar mask.
*   **Sycophancy / Bias:** The model's tendency to align with user priors rather than objective truth is a property of the weight distribution, not the API channel.

# gpt-5.6-terra
usage: {'input_tokens': 286, 'input_tokens_details': {'cache_write_tokens': 0, 'cached_tokens': 0}, 'output_tokens': 9000, 'output_tokens_details': {'reasoning_tokens': 122}, 'total_tokens': 9286}

## 1. Outcome-settlement: formal meaning

Let:

- \(x\): case/task.
- \(a\): model action/report.
- \(e\in E\): hidden diligence/effort level: retrieval, tool use, deliberation, verification, abstention, escalation.
- \(I_e\): information acquired under effort \(e\).
- \(q_e(y\mid x,I_e)\): posterior formed after effort.
- \(r\): reported predictive distribution, confidence, decision, or claim.
- \(Y\): later settleable outcome/ground truth.
- \(c(e)\): effort cost.
- \(T(r,Y)\): transfer/payment/penalty settled after outcome realization.

Proper elicitation alone gives, conditional on the posterior already formed,

\[
r^* = q_e(\cdot\mid x,I_e)
\]

when \(T\) is a strictly proper score, e.g. log score:

\[
T(r,Y)=\alpha \log r(Y)+\beta.
\]

It does not imply a high \(e\). The agent chooses effort by

\[
e^* \in \arg\max_e
\left[
\mathbb E_{I_e,Y}\bigl[T(q_e,Y)\bigr] - c(e)
\right].
\]

For a proper score \(S\), truthful expected score is an entropy functional:

\[
\mathbb E_{Y\sim q_e} S(q_e,Y) = G(q_e),
\]

where \(G\) is convex in the distribution argument for reward-oriented proper scores. The marginal value of effort is

\[
\Delta_e
=
\mathbb E\left[G(q_{e'})-G(q_e)\right].
\]

Diligence is incentivized iff, for an effort increment \(e\to e'\),

\[
\lambda \Delta_e \ge c(e')-c(e),
\]

where \(\lambda\) is effective stake after discounting, caps, collection risk, and any probability that settlement actually occurs.

Thus **outcome-settlement** means:

> The report, decision, or committed forecast is economically, procedurally, or reputationally settled against a later evidence-defined outcome, with consequences sufficiently coupled to predictive/decision quality that additional information acquisition has positive expected private value.

It closes the diligence gap only when all of the following hold:

1. **Effort-sensitive outcome distribution**  
   More diligence improves calibration, discrimination, decision quality, or error detection:
   \[
   I(Y;I_{e'}\mid I_e,x)>0.
   \]

2. **Outcome-sensitive settlement**  
   Settlement changes with realized \(Y\), not merely with report format or self-attestation.

3. **Material stake**  
   The expected gain from better information exceeds marginal effort cost.

4. **Attribution**  
   The settled item is causally attributable to the model/agent’s report or decision.

5. **No cheap manipulation**  
   The agent cannot control, selectively suppress, relabel, delay, or fabricate the settlement outcome more cheaply than acquiring information.

6. **Commitment before outcome**  
   The forecast/decision and relevant evidence provenance are frozen before settlement.

7. **No profitable gaming through abstention, triage, or case selection**  
   Coverage, abstention, and routing are themselves settled or constrained.

8. **Enforceable transfer**  
   Financial, reputational, access-control, or governance consequences are actually imposed.

Without these conditions, “settlement” is ceremony, monitoring, or retrospective evaluation, not an effort incentive.

---

## 2. Settlement architectures

The architecture space is a product of:

\[
(\text{settler},\ \text{truth source},\ \text{latency},\ \text{stake},\ \text{attribution},\ \text{dispute rule},\ \text{anti-gaming controls}).
\]

There is no finite non-overlapping list of all implementations; the exhaustive taxonomy is by these axes.

### 2.1 Who settles

| Settler | Mechanism | Effort incentive? | Principal failure mode |
|---|---|---:|---|
| Automated deterministic system | Compute score/payment from machine-verifiable outcome | Yes, strongest, if outcome is effort-sensitive | Bad target, manipulable labels |
| Principal/operator | Internal scorecard, bonus, access restriction | Yes if principal can observe valid outcomes and credibly commit | Discretion, favoritism, weak commitment |
| User/customer | Acceptance, refund, renewal, rating | Sometimes | User may lack ability/incentive to detect correctness |
| Independent evaluator | Blind benchmark, case review, audit adjudication | Yes if sampling and sanctions are credible | Evaluator capture; sparse observations |
| External oracle/data provider | Market price, registry, database, telemetry feed | Yes if oracle is reliable and non-manipulable | Oracle error/manipulation |
| Court/regulator | Liability, fine, license condition | Indirectly; usually low-frequency but high-stake | Long latency, attribution difficulty |
| Peer-prediction panel | Reward agreement/information structure among peers | Usually not reliably for diligence | Collusion; common-mode ignorance |
| Prediction market / market maker | Mark-to-outcome contract settlement | Yes for forecasting if market participants bear stakes | Manipulation, liquidity, legal constraints |
| Cryptographic protocol / smart contract | Automatically release escrow conditional on oracle/proof | Yes only to extent oracle/proof measures quality | “Garbage in, immutable garbage out” |
| Model provider | Provider evaluates usage traces and outputs | Sometimes | Provider may observe process but not truth; conflicts |
| Delegated agent hierarchy | Parent agent settles child-agent outputs | Only if parent’s own payoff is truth-settled | Recursive unverifiable diligence |

### 2.2 Against what “ground truth”

#### A. Direct realized outcome

Examples:

- Fraud actually occurred.
- Patient later had adverse event.
- Shipment arrived.
- Loan defaulted.
- Software test passed.
- Claim was upheld or rejected by a court.
- Forecasted event occurred.

Settlement:

\[
T = S(r,Y).
\]

Effort incentive: **yes**, if better investigation predicts \(Y\), outcome is not too noisy, and score stake exceeds effort cost.

Limits:

- A model may optimize prediction of recorded label rather than the normative target.
- Realization can be affected by the model’s action: performative prediction / self-fulfilling outcome.
- Rare outcomes create high variance.
- Long latency discounts incentives.

#### B. Counterfactual outcome

Examples:

- “Would this intervention have prevented harm?”
- “Would this applicant have repaid under approval?”
- “Would this content have caused harm absent moderation?”

Requires causal estimand:

\[
Y(a),\qquad \tau = \mathbb E[Y(1)-Y(0)].
\]

Settlement needs randomization, quasi-experimental identification, causal model validation, or matched controls.

Effort incentive: **weak to strong depending on identification**. If the settled quantity is unidentifiable from available evidence, no scoring rule can make truthfully reporting it operationally verifiable.

#### C. Expert-adjudicated truth

Examples:

- Medical chart review.
- Legal correctness.
- Scientific claim validity.
- Safety incident root cause.

Settlement:

\[
T(r,\hat Y_{\text{panel}})
\]

where \(\hat Y_{\text{panel}}\) is an adjudicated label.

Effort incentive: **yes**, if panel judgments are blinded, independent, consistent enough, sampled unpredictably, and stakes are material.

Failure modes:

- Adjudicators share the model’s blind spots.
- Label is contestable or normatively plural.
- Agent learns panel preferences rather than underlying truth.
- Adjudication cost limits sample size.

#### D. Proxy outcome / surrogate label

Examples:

- Click-through as proxy for user benefit.
- Complaint rate as proxy for safety.
- Acceptance rate as proxy for answer quality.
- Code compilation as proxy for program correctness.
- Retrieval-citation count as proxy for factual grounding.

Settlement:

\[
T(r,Z),\quad Z \neq Y.
\]

Effort incentive: **for optimizing the proxy**, not necessarily for truth/diligence regarding \(Y\).

It closes the diligence gap only if:

\[
\arg\max_e \mathbb E[T(r,Z)\mid e]
\]

also increases the intended objective. This requires proxy validity, stability, and resistance to Goodharting. Otherwise it creates **proxy diligence**: work directed toward improving \(Z\), including gaming \(Z\), not toward truth.

#### E. Process-ground-truth

The settled object is whether required work occurred:

- Required sources were accessed.
- Required tests were run.
- Required tool calls occurred.
- Required approval gate was reached.
- Required policy rules were evaluated.
- Computation hash matches specified program execution.

Settlement against trace \(H\):

\[
T = T(H).
\]

Effort incentive: **yes for observable prescribed process**, not necessarily for epistemically useful diligence.

This proves “the workflow ran,” not “the workflow was competent,” unless the process itself is sufficient for the intended property.

#### F. Verifiable-computation truth

The claim is “program \(P\), on committed input \(z\), produced output \(o\).”

Proof relation:

\[
\mathsf{Verify}(vk, z, o, \pi)=1.
\]

Examples:

- Zero-knowledge proof of inference over committed weights/input.
- SNARK/STARK proof that mandated checks executed.
- Trusted-execution-environment attestation.
- Reproducible deterministic computation with signed artifacts.
- Proof-carrying code.
- Formal proof checked by a proof assistant.

Effort incentive: **yes for executing the required computation**, because payment/access can be conditioned on a valid proof.

It does **not** prove:

- Correctness of inputs.
- Correctness of labels/ground truth.
- Adequacy of the specified algorithm.
- Truth of natural-language premises.
- That an LLM’s latent reasoning was faithful.
- That the computation was not preceded by unobserved shortcutting, unless the protocol excludes it.

#### G. Consensus / peer agreement

Settlement against peer reports \(\{r_j\}\), often using peer prediction, Bayesian truth serum, or correlation-based rewards.

Effort incentive: **conditional and fragile**. Under strong assumptions—conditionally independent private signals, known/common prior structure, no collusion, truthful equilibrium selection—some mechanisms reward informative effort. In realistic AI settings, these assumptions usually fail.

It can reward:

- Shared prejudices.
- Common training-data priors.
- Coordination on salient answers.
- Mimicry of expected consensus.

Therefore peer agreement is not generally outcome-settlement against truth.

#### H. Market-implied truth

Settlement against future market price or resolution value.

Examples:

- Prediction markets.
- Insurance/loss markets.
- Financial event contracts.
- Internal forecasting markets.

Effort incentive: **yes**, because private research can improve expected trading/forecast payoff. It is strongest where traders can acquire differentiated information and final resolution is objective.

Failures:

- Market price can be manipulated.
- Liquidity is insufficient.
- Traders optimize short-horizon mark-to-market rather than final truth.
- Market participants have correlated information.
- Legal restrictions apply.

#### I. User-experienced outcome

Examples:

- Task completion.
- Measured time saved.
- Downstream error rate.
- Revenue.
- Customer retention.
- Safety incident rate.

Effort incentive: **yes only when attribution is controlled**. A model can improve measured downstream outcomes through manipulation, dark patterns, over-refusal, or selective service unless those are separately constrained.

#### J. Normative or unresolvable claims

Examples:

- “This policy is fair.”
- “This answer is sufficiently respectful.”
- “This decision is legitimate.”
- “The system acted ethically.”
- “This historical interpretation is correct.”
- “The model genuinely understood.”

No unique ground truth may exist.

Settlement can be against:

1. A stipulated decision procedure.
2. A democratic or institutional authority.
3. A plural-panel aggregation rule.
4. A constitutional/policy constraint.
5. A negotiated contract.
6. An explicitly declared value function.

This incentivizes conformance to the settlement constitution, not discovery of an independent fact. The diligence gap is only closed relative to that stipulated criterion.

---

## 3. Latency architectures

Let \(\delta\in(0,1]\) be per-period discounting and \(L\) settlement delay. Effective stake is approximately:

\[
\lambda_{\mathrm{eff}} = \lambda \delta^L p_{\mathrm{settle}} p_{\mathrm{collect}}.
\]

| Latency | Examples | Diligence effect |
|---|---|---|
| Immediate | Unit tests, schema validation, deterministic database lookup | Strong, low variance; only tests what is immediately measurable |
| Short-horizon | User acceptance, transaction completion, human review | Often practical; vulnerable to proxy gaming |
| Delayed | Fraud realization, clinical outcomes, legal outcomes | Requires escrow, deferred compensation, retention/clawback |
| Very delayed | Long-term safety, environmental harms, lifetime outcomes | Weak without bonds, insurance, reserve requirements, or institutional liability |
| Never / unknowable | Counterfactuals, private mental states, metaphysical claims | Cannot be directly outcome-settled; use proxies/process/proofs, acknowledging residual gap |

### Delayed-settlement mechanisms

1. **Escrow**  
   Withhold payment until \(Y\) resolves.

2. **Clawback**  
   Pay now, recover later if settled outcome is bad.

3. **Performance bond**  
   Agent posts collateral:
   \[
   B \ge \frac{c(e')-c(e)}{\delta^L p_{\mathrm{settle}} \Delta p_{\mathrm{bad}}}.
   \]

4. **Holdback / rolling reserve**  
   Retain a fraction of ongoing compensation.

5. **Insurance / risk pooling**  
   Agent pays actuarially risk-sensitive premium; insurer audits diligence.

6. **Reputation capital / license**  
   Future access or privileges depend on settled record.

7. **Deferred equity / long-term compensation**  
   Aligns incentives with later outcomes, but attribution dilution can weaken it.

8. **Milestone settlement**  
   Score intermediate verifiable predictions or process checkpoints before final outcome.

These work only if the agent cannot exit, reorganize, become judgment-proof, or otherwise evade delayed liability.

---

## 4. Stake architectures

“Stake” need not be cash. It is any controlled consequence whose expected value depends on settlement.

| Stake | Effort incentive condition | Typical weakness |
|---|---|---|
| Per-case payment/penalty | Payment difference exceeds marginal effort cost | High variance; adversarial case selection |
| Bonus pool | Team reward depends on aggregate outcomes | Free-riding, diluted attribution |
| Escrowed collateral | Loss occurs on failure | Requires enforceable custody and sufficient collateral |
| Access to tools/models | Good settlement unlocks capability | Can be strong for API agents | May induce concealment/manipulation |
| Rate limits / quotas | Quality earns capacity | Incentivizes quality if capacity has value | Coarse and delayed |
| Reputation score | Future demand/access depends on record | Easy to game if reputation is proxy-based |
| License/certification | Bad settled outcomes threaten permission to operate | Strong but slow and legally complex |
| Audit intensity | Poor history causes costly scrutiny | Incentivizes avoiding detectable errors |
| Liability / indemnity | Agent bears harm cost | Attribution, insolvency, legal limits |
| Budget allocation | Better settled performance receives future budget | Organizational politics |
| Model-routing priority | Good performance gets higher-value tasks | Can induce cherry-picking |
| Deployment scope | Better record grants autonomy | Strong governance lever; requires reliable measurement |

For an API model with no independent assets or legal personhood, the real stake is usually borne by:

- provider;
- deployer;
- operator;
- tool-owning principal;
- downstream human approver;
- account holder;
- organization that receives/loses access.

A stateless model instance cannot itself be made financially liable absent an external account, escrow, or provider-side policy state.

---

## 5. Dispute-resolution architectures

| Dispute rule | What it settles | Diligence value |
|---|---|---|
| Deterministic recomputation | Schema, test, proof, ledger event | Strong where applicable |
| Precommitted oracle | Signed database/feed/event resolver | Strong if oracle trustworthy |
| Single expert reviewer | Contestable factual/professional claims | Moderate; reviewer error/capture |
| Blind multi-expert panel | Reduces identity and hindsight effects | Stronger; costly |
| Adversarial red-team / opposing experts | Claims exposed to motivated challenge | Strong for finding failures; may favor rhetorical exploitability |
| Arbitration | Contractual disputes | Depends on arbitrator and evidence rules |
| Court/regulator | Legal standards | High authority, long latency |
| Appeals ladder | Initial decision plus review | Improves legitimacy; slows settlement |
| Statistical adjudication | Aggregate calibration/accuracy | Strong for repeated tasks; weak per individual case |
| Random audit with extrapolated penalties | Inspect sample, impose expected penalty | Can strongly incentivize diligence if audit probability × penalty is sufficient |
| Burden shifting | Agent must prove compliance after anomaly | Strong for traceable processes |
| Challenge market / bounty | Third parties paid to falsify claims | Strong for detectable errors; can miss latent harms |

For randomized audit probability \(p_a\), detected-cheating penalty \(F\), and shortcut saving \(c_s\), deterrence requires approximately:

\[
p_a \cdot p_d \cdot F \ge c_s,
\]

where \(p_d\) is conditional detection probability. If audits only inspect superficial traces, \(p_d\) is low and the agent optimizes for audit appearance.

---

## 6. Principal settlement designs and whether they buy diligence

### 6.1 Proper scoring against final outcomes

Protocol:

1. Model emits immutable forecast \(r_t\).
2. Timestamp, identity, case definition, and coverage decision are committed.
3. Outcome \(Y_{t+L}\) resolves.
4. Score \(S(r_t,Y_{t+L})\) is computed.
5. Stakes transfer or policy state updates.

Example:

\[
S_{\mathrm{Brier}}(r,Y) = -\sum_k(r_k-\mathbf 1[Y=k])^2.
\]

Effort incentive: **yes**, if research/tool use improves forecast quality and stake is sufficient.

Need:

- score forecasts, not post-hoc edited reports;
- include abstentions and nonresponses;
- avoid selectively scoring easy cases;
- normalize for base-rate shifts;
- measure calibration and sharpness jointly.

### 6.2 Decision settlement / utility settlement

For action \(a\), settle against realized utility:

\[
T(a,Y) = U(a,Y).
\]

Effort incentive: **yes**, for acquiring information that improves action selection.

But this differs from forecast scoring. A model can be calibrated yet make poor decisions if costs are wrong; conversely a useful decision rule need not report calibrated probabilities.

Requires:

- specified utility function;
- causal attribution;
- treatment of externalities;
- protection against manipulating \(Y\) or measured utility.

### 6.3 Forecast-plus-decision settlement

Settle both:

\[
T(r,a,Y)=\lambda S(r,Y)+\mu U(a,Y).
\]

Purpose:

- score epistemic honesty through \(S\);
- score operational consequences through \(U\).

Effort incentive: **yes**, provided both terms are non-gameable. This is often superior where the model may distort forecasts to justify desired actions.

### 6.4 Process-contingent outcome settlement

\[
T(r,Y,H)=S(r,Y)+b\cdot \mathbf 1[H\in \mathcal H_{\mathrm{required}}].
\]

Here \(H\) is an attested trace: required retrieval, tests, approvals, citations, policy checks.

Effort incentive: **yes for both outcome quality and mandated process**, but only if trace authenticity is strong and prescribed process is causally useful.

This is the common practical design for high-stakes AI:

- outcome score for ultimate quality;
- process requirements for minimum diligence;
- audit for trace integrity;
- escalation when confidence or risk threshold is exceeded.

### 6.5 Audit-only settlement

No continuous outcome label; random cases are audited.

\[
T = -F \cdot \mathbf 1[\text{audit detects violation}].
\]

Effort incentive: **yes for detectable violations**, including skipped retrieval, unsupported claims, policy breaches, fabricated citations, and tool-use failures.

It does not fully reward information acquisition unless audits can determine whether better diligence was warranted and omitted.

### 6.6 Relative-performance settlement

Reward relative to benchmark/model/peer:

\[
T_i = S_i - \frac{1}{n-1}\sum_{j\ne i}S_j.
\]

Effort incentive: **sometimes**. It reduces common shocks and can motivate research that creates an edge. But it can induce sabotage, benchmark overfitting, or competition over narrow metrics.

### 6.7 Tournament settlement

Top performers receive prizes, bottom performers lose access.

Effort incentive: **yes but distorted**. Encourages high-variance strategies, selective participation, and manipulation near thresholds. Weak for cooperative safety obligations.

### 6.8 Reputation settlement

Historical settled quality updates a reliability state:

\[
R_{t+1}=f(R_t,S_t).
\]

Routing, permissions, and required oversight depend on \(R_t\).

Effort incentive: **yes if future opportunity value is substantial and identity persistence prevents reset/Sybil attacks**.

### 6.9 Insurance and indemnity settlement

Provider/deployer bears losses; insurance premiums vary with settled outcomes and audited controls.

Effort incentive: **yes at organizational level**. Insurer becomes an auditor and process designer. It does not directly make an individual model deliberate unless contractual/technical controls transmit the incentive.

### 6.10 Adversarial challenge settlement

A claimant/model commits to claim \(C\), evidence \(E\), and stake \(B\). Challengers can submit counterexample \(z\) or contradiction proof. Valid challenge slashes stake or triggers correction.

Effort incentive: **yes for verification and conservative claiming**, especially for universal claims, code correctness, provenance claims, and factual assertions with discoverable counterevidence.

Weaknesses:

- Absence of challenge is not truth.
- Bounty hunters target easy-to-prove flaws.
- Claims must be precisely formalized.
- Public challenge may expose sensitive information.

### 6.11 Verifiable-computation settlement

Payment conditional on proof:

\[
T = P\cdot \mathbf 1[\mathsf{Verify}(vk,z,o,\pi)=1].
\]

Effort incentive: **yes for exact computation**, including mandated inference, optimization, filtering, cryptographic checks, or formal proof generation.

It closes a computational-diligence gap, not a semantic-truth gap.

### 6.12 Human-approval settlement

Model’s future autonomy/payment depends on human approval and later review.

Effort incentive: **usually weak unless approvers are accountable to outcomes**. Otherwise it incentivizes persuasive presentation, deference cues, and bureaucratic compliance.

### 6.13 Multi-stage settlement

1. Immediate: validate schema, provenance, mandatory tool calls.
2. Short-term: expert/user review.
3. Delayed: realized outcome.
4. Long-term: incident, regret, externality review.
5. Periodic: recalibrate model/routing policy.

Effort incentive: **strongest practical architecture** because it combines low-latency enforceable controls with ultimate outcome alignment.

---

## 7. Proxy, delayed, and unresolvable claims

### 7.1 Proxy claims

For target \(Y\) and observed proxy \(Z\), a proxy score buys diligence for \(Y\) only if effort that improves \(Z\) also improves the intended target. Sufficient practical conditions:

- \(Z\) is causally downstream of \(Y\) or a validated measurement of it;
- intervention on reporting cannot cheaply alter \(Z\);
- proxy relationship is stable across deployment populations;
- adverse correlations and subgroup failures are monitored;
- secondary outcomes constrain obvious Goodhart paths.

Use a proxy bundle:

\[
T = \sum_j \lambda_j S_j(r_j,Z_j) - \sum_k \gamma_k P_k,
\]

where \(P_k\) are penalties for known gaming/externality indicators.

No proxy bundle proves diligence toward an unobserved target; it only makes intended diligence more instrumentally valuable.

### 7.2 Delayed outcomes

Delayed outcomes require:

- immutable pre-outcome commitment;
- identity continuity;
- escrow, clawback, bond, reserve, or reputation persistence;
- survival-adjusted attribution;
- countermeasures for case migration and account reset.

If no durable stake remains at \(t+L\), then:

\[
\lambda_{\mathrm{eff}}\approx 0,
\]

and delayed outcome settlement does not buy present effort.

### 7.3 Unresolvable claims

Claims with no observable truth condition cannot be directly proper-scored. Available substitutes are:

| Substitute | What it guarantees |
|---|---|
| Operational definition | Compliance with stipulated criterion |
| Process attestation | Required procedure occurred |
| Expert/panel judgment | Agreement with institutional judgment |
| Formal proof | Validity relative to axioms/specification |
| Prediction of future adjudication | Accuracy about the adjudicator |
| Abstention/escalation rule | Avoidance of unsupported certainty |
| Adversarial challenge | Resistance to found counterexamples |

None establishes a mind-independent truth where no settleable truth criterion exists.

---

## 8. Adversarial-audit designs

### 8.1 Random hidden-case audit

- Operator samples cases after commitment.
- Model/provider cannot know which cases are audited.
- Auditors inspect answer, evidence, tool trace, omitted alternatives, and policy compliance.
- Penalties scale with severity and evidence of intentional shortcutting.

Incentive:

\[
\text{expected shortcut cost}=p_a p_d F.
\]

Effective if \(p_a\), \(p_d\), and \(F\) jointly dominate shortcut savings.

### 8.2 Canary tasks

Inject tasks with known hidden answer, hidden policy trap, or required-tool condition.

Incentive: detects failure to retrieve, reason, refuse, or follow required workflow.

Limitation: models can overfit recognizable canaries; rotate task generators and distribution.

### 8.3 Counterfactual audit

Auditor asks whether additional available evidence would have changed a reasonable posterior/decision. This directly targets missed diligence.

Requires reconstructing information availability and a defensible standard of care. It is expensive and contestable.

### 8.4 Trace-forensics audit

Audit signed tool calls, retrieval snapshots, hashes, timestamps, execution environments, and provenance.

Strong for detecting fabricated process. Weak for determining whether retrieved evidence was understood or adequately evaluated.

### 8.5 Red-team falsification market

Third parties receive rewards for producing:

- false citations;
- counterexamples;
- jailbreaks;
- unsafe action paths;
- policy violations;
- missing evidence;
- reproducible discrepancy with authoritative sources.

Strong for discoverable defects. Coverage is biased toward lucrative/easy-to-demonstrate failures.

### 8.6 Audit-conditioned escalation

If uncertainty, high impact, novel domain, or conflict signal occurs, runner forces human review or expensive verification.

This turns risk classification into a stake-sensitive routing problem. It buys effort if avoiding unjustified escalation is not easier than correctly resolving the case.

### 8.7 Adversarially chosen audit distributions

Audits oversample:

- high-impact cases;
- rare classes;
- low-confidence/high-confidence mismatches;
- cases with suspiciously short traces;
- disagreement with independent models;
- post-deployment incidents;
- demographic slices;
- boundary conditions.

This improves detection but changes the effective task distribution; scoring must account for sampling weights.

---

## 9. Closed-API implementability of settlement architectures

“Closed API only” means the deployer can call a hosted model but cannot inspect weights, hidden activations, training process, or necessarily token probabilities. The deployer can still control prompts, tools, external state, logging, routing, and post-hoc settlement.

| Architecture | Closed API only? | Notes |
|---|---:|---|
| Outcome scoring against external labels | Yes | Store immutable output and settle later externally |
| Decision/outcome settlement | Yes | Requires external telemetry and attribution |
| Escrow/clawback/account-level stake | Yes | Stake attaches to provider/deployer/account, not model internals |
| User/expert adjudication | Yes | Output and evidence can be reviewed |
| Random audits/canaries | Yes | Runner selects hidden cases |
| Tool-use process requirements | Yes | If all tools are runner-mediated |
| Signed tool traces | Yes | Runner signs requests/results; model cannot forge runner records |
| Retrieval provenance | Yes | If retrieval is via controlled tools |
| Mandatory approval gates | Yes | Runner-owned state machine |
| Output schema enforcement | Yes | API/provider or local validator |
| Conformal/selective prediction | Yes | Requires calibration data and external wrapper |
| Forecast scoring | Yes | Ask for probabilities in schema, score externally |
| Market settlement | Yes | External market/oracle |
| Proof of external computation | Yes | Runner executes/proves computation; model proposes inputs/code |
| Proof that closed model used specified internal reasoning | No | Hidden inference trace unavailable and not semantically meaningful |
| Proof that provider used specified weights/model version | Usually no, unless provider supplies attestation | API model name is contractual metadata, not cryptographic proof |
| Proof of training-data diligence | No, absent provider audit/attestation | Not inferable from outputs |
| Proof of absence of latent capability/intent | No | Behavioral evidence only |
| Logit-level verification | Usually no | Some APIs expose logprobs; this still does not prove reasoning/diligence |
| Deterministic replay | Partially | `seed` is usually best-effort; backend/model changes defeat durable replay unless provider guarantees versioning |
| Verifiable inference of closed model | No, absent provider TEE/ZK attestation | External wrapper cannot prove hosted internal execution |

---

## 10. Structural typed API channels

A structural channel is a communication/action path whose syntax, authority, state transition, or provenance is enforced by software outside the model.

Let a runner own state \(s_t\), receive model output \(m_t\), validate it against type/policy \(V\), and perform transition:

\[
s_{t+1} = \delta(s_t, V(m_t), \kappa_t),
\]

where \(\kappa_t\) is external authority/capability state.

A genuine structural guarantee exists when prohibited states/actions are unreachable:

\[
\forall m_t,\quad V(m_t)\notin A_{\mathrm{authorized}}
\implies
\delta(s_t,V(m_t),\kappa_t)\notin \text{execute}.
\]

The model may emit arbitrary text, but text has no authority unless the runner parses and authorizes it.

### 10.1 Typed channel primitives

| Primitive | Structural property | Real guarantee |
|---|---|---|
| Role-separated messages | System/developer/user/tool channels are distinguishable | Provenance/priority only if platform enforces it; not semantic obedience |
| Function/tool calls | Model emits named operation plus typed arguments | Runner can ensure only registered functions are invocable |
| JSON Schema arguments | Required fields, enums, ranges, object shape | Valid syntax/type after validation; not truth of values |
| Strict `response_format` / structured outputs | Output conforms to schema | Shape guarantee, subject to provider implementation; no semantic correctness |
| Typed content blocks | Text/image/file/tool-result blocks distinguished | Modality/provenance routing, not truth/safety of content |
| Capability tokens | Possession required for action | Authority confinement if tokens are unforgeable and checked server-side |
| Runner-owned state machine | Only legal transitions execute | Strong workflow/order guarantee |
| Server-side policy engine | Authorization independent of model text | Strong action-control guarantee |
| Tool mediation | All external side effects pass through runner | Strong if no bypass channel exists |
| Signed logs / append-only ledger | Tamper-evident event history | Integrity/provenance after signing; not completeness if events can bypass logger |
| Grammar/constrained decoding | Output language restricted to grammar | Syntactic language membership only |
| `logit_bias` | Alters relative token sampling | No hard guarantee unless effectively excludes all alternative tokenizations; weak control |
| Stop sequences | End generation at delimiter | Boundary convenience, not reliable security boundary |
| `seed` | Attempts reproducible sampling | Conditional/best-effort reproducibility; not identity, honesty, or audit proof |
| Temperature/top-p | Sampling distribution control | Statistical behavior adjustment only |
| Max tokens | Bounded generation length | Resource bound only |
| Allowlisted tool schemas | Limits callable operations | Strong if dispatch uses allowlist and args validated |
| Sandboxed execution | Limits code/process permissions | Strong containment relative to sandbox assumptions |
| Human approval token | Requires external signer for transition | Strong authorization gate if signer identity/token is protected |

---

## 11. Governance obligations structurally channelable

### 11.1 Identity, authority, and separation of duties

| Obligation | Structural channel | Guarantee level |
|---|---|---|
| Only authorized principal may invoke high-risk workflow | Authenticated API identity, OAuth/mTLS, account/project ACL | Real access-control guarantee |
| Model may not grant itself authority | Capability tokens minted only by runner | Real, if token unforgeable and no ambient authority |
| User cannot impersonate system/developer | Role metadata set by API/runner, not model text | Real provenance distinction; not immunity to prompt injection |
| Tool may act only within delegated scope | Per-tool scoped token, audience, expiry, quota | Real least-privilege guarantee |
| High-risk action requires two-party approval | Distinct signer tokens / dual-control state transition | Real if identities independently authenticated |
| Separation between proposer and executor | Model proposes; independent runner/policy engine executes | Real execution separation |
| Separation between evaluator and candidate | Independent evaluator service/model/account | Architectural independence, not epistemic independence |

### 11.2 Workflow and procedural obligations

| Obligation | Structural implementation | Guarantee |
|---|---|---|
| Retrieve before answering | State machine requires retrieval receipt before final-answer state | Real that controlled retrieval call occurred |
| Cite only retrieved documents | Citation IDs must reference runner-issued retrieval handles | Real provenance linkage; not entailment |
| Run tests before deploy | Deployment transition requires signed test artifact | Real test-execution gate; not test adequacy |
| Require human approval before payment/action | Approval token required by state machine | Real gate |
| Escalate specified risk classes | Deterministic classifier/rules route to review | Real for detected/defined class; classifier can err |
| Preserve immutable case record | Append-only/WORM logs, signed hashes | Real tamper-evidence within trust boundary |
| Freeze forecast before outcome | Timestamped commitment/hash | Real precommitment |
| Prevent post-hoc answer edits | Versioned immutable record | Real record integrity |
| Enforce coverage declaration | Schema requires `abstain` / `answer` and routing handles both | Real declaration; not honest uncertainty |
| Limit spending/action magnitude | Server-side quotas, budget caps, transaction limits | Real bound |
| Restrict data access | Capability-scoped retrieval APIs, row/field-level ACL | Real access restriction if all access is mediated |
| Require deletion/retention policy | Data lifecycle service, TTL, cryptographic key destruction | Real operational deletion relative to storage architecture |
| Prohibit network egress | Sandbox/firewall/allowlist | Real under complete mediation |
| Require approved model/version | Runner allowlist of provider model IDs | Real request routing; not cryptographic assurance of provider internals |
| Require deterministic external computation | Runner executes pinned code/container | Real relative to trusted runtime |

### 11.3 Output-format and communication obligations

| Obligation | Structural implementation | Guarantee |
|---|---|---|
| Machine-readable decision | Strict JSON schema | Valid schema |
| Enumerated action class only | Enum field | No other parsed action class |
| Numeric bounds | JSON Schema min/max plus server validation | Value range |
| Required fields | `required` schema fields | Presence, not meaningful content |
| No free-text in executable field | Typed separation: `action_args` vs `rationale` | Parser ignores text for authority |
| Attach confidence | Required probability field | Field exists/in range; not calibrated |
| Attach evidence IDs | Array of runner-issued opaque IDs | IDs exist and originated from retrieval system |
| Declare uncertainty/abstention | Tagged union `answer | abstain | escalate` | Explicit routing state |
| No unsupported external URLs | URL allowlist / opaque document IDs | Reference restriction |
| Redact certain fields | Structured redaction transform before model/output | Strong for known structured fields; weak for latent re-identification |
| Emit policy reason code | Enum | Classified reason label exists; may be false/misapplied |

Example action schema:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["kind", "case_id", "confidence", "evidence_ids"],
  "properties": {
    "kind": {
      "type": "string",
      "enum": ["answer", "abstain", "escalate"]
    },
    "case_id": {
      "type": "string",
      "pattern": "^case_[A-Za-z0-9_-]{16,64}$"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "evidence_ids": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^ev_[A-Za-z0-9_-]{16,64}$"
      }
    }
  }
}
```

This guarantees parseable structure and bounded values. It does not guarantee that confidence is calibrated, evidence supports the claim, or `case_id` was not selected strategically unless runner binds it to session state.

---

## 12. Obligations that cannot be structurally channelled

These are measured behavioral, epistemic, or normative properties, not type properties.

| Obligation | Why structural typing cannot guarantee it | Measurement/settlement substitute |
|---|---|---|
| Truthfulness | A valid string/schema can be false | Outcome scoring, fact-checking, audits |
| Calibration | Probability field can be arbitrary | Held-out/online calibration measurement |
| Diligence | Tool calls can be perfunctory; no type expresses adequate search | Outcome settlement, process audits, challenge tests |
| Faithful reasoning | Rationale can be post-hoc | Causal intervention tests, process controls; no general proof for opaque LLMs |
| Non-deception | Intent and strategic withholding are semantic/counterfactual | Adversarial audits, incentives, behavioral evidence |
| Helpfulness | Context-dependent utility | User/task outcome measurement |
| Fairness | Depends on chosen fairness definition and population behavior | Statistical audits, normative governance |
| Non-discrimination | Same | Outcome/subgroup evaluation and legal review |
| Non-manipulation | Depends on user psychology and downstream effects | Behavioral experiments, red teams, outcome monitoring |
| Privacy leakage absence | Semantic memorization/inference can survive schema controls | Privacy testing, access controls, DP/training guarantees |
| Robustness | Infinite/unknown perturbation set | Testing, formal verification only for bounded formal systems |
| Absence of jailbreak susceptibility | Adversarial language behavior cannot be typed away | Red teaming, defense-in-depth |
| Safety under novel conditions | Distributional property | Monitoring, conservative routing, incident response |
| Correct interpretation of policy | Natural-language semantics and exceptions | Expert review, test suites, adjudication |
| Appropriate refusal | Requires contextual judgment | Evaluated refusal policy and audits |
| Non-hallucination | Citation fields can contain irrelevant evidence | Entailment checks, fact verification, outcome audits |
| No hidden side channel | Requires whole-system threat model | Isolation, traffic monitoring, formal noninterference where possible |
| No model self-modification | Closed API wrapper can prevent exposed mutation, but cannot prove provider-side internals | Provider assurance/audit |
| No training-data misuse | Runtime schema cannot prove training provenance | Provider audit, contracts, compliance evidence |
| No latent dangerous capability | Not inferable from output type | Evaluations, access controls, provider governance |
| Value alignment | Not a syntactic property | Institutional governance and outcome monitoring |

---

## 13. Real guarantee versus stronger prior

### Real guarantee

Structural typing gives a real guarantee when all of these hold:

1. The protected resource/action is outside the model.
2. All access paths are mediated.
3. The reference monitor is trusted enough.
4. Authorization is checked server-side.
5. Inputs are validated before use.
6. No parser ambiguity or fallback path grants authority.
7. Logs/state are bound to authenticated session identity.

Examples:

- Model cannot transfer funds except via a tool call.
- Tool call cannot exceed \$100 because server rejects larger amount.
- Model cannot invoke `deploy_prod` without human-signed capability.
- Model cannot cite a non-retrieved document if citations are opaque runner-issued IDs.
- Model cannot skip the mandatory approval state because runner rejects invalid transition.
- Model cannot read ungranted database rows if database enforces row-level permissions.

### Stronger prior only

Structural typing is merely a stronger prior when the property is semantic, when enforcement occurs only through prompting, or when some bypass exists.

Examples:

- System role says “do not reveal secrets.”
- Schema has `"safe": true`.
- Model emits `"verified": true`.
- Required `reasoning` field is present.
- Citation IDs are valid but irrelevant.
- `logit_bias` disfavors forbidden words.
- Stop sequence is expected to prevent continuation.
- Seed is assumed to make outputs reproducible.
- Tool call shows retrieval occurred, but not that relevant evidence was used.
- Model

# claude-opus-4-8
usage: {'input_tokens': 496, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 0, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}, 'output_tokens': 5890, 'output_tokens_details': {'thinking_tokens': 0}, 'service_tier': 'standard', 'inference_geo': 'global'}

# Q_V2: Outcome-Settlement and the Diligence Gap

## 1. Definitions

**Honesty-of-report** (what proper scoring buys): given posterior P the model formed, incentive alignment makes truthful revelation of P weakly dominant. Formally, for scoring rule S, E_P[S(report=P)] ≥ E_P[S(report=q)] ∀q. The expectation is taken *under the model's own P*. This says nothing about whether P is close to the true generating distribution P*.

**Diligence gap**: the model chooses a *computation policy* π (how much effort/information to acquire) that yields posterior P_π. Cheap π gives high-entropy or biased P_π. Proper scoring evaluated against the *model's own* posterior cannot penalize a lazy P_π, because the reward is self-consistent under P_π. The gap is: no term in the objective depends on P* except through realized outcomes.

**Outcome-settlement**: bind reward to *realized ground-truth outcomes y* drawn from P*, not to the coherence of the report with itself. Settlement replaces E_P[S] with realized S(report, y), y~P*. Because y is sampled from the true world, expected settlement reward is maximized only by driving P_π→P*, which generically requires effort. This is the mechanism: **the scoring expectation is taken under P*, not P**, so laziness is now penalized in expectation.

Key inequality that must hold for diligence: the marginal proper-score gain from effort must exceed marginal cost:
  E_{P*}[S(P_{π'}, y)] − E_{P*}[S(P_π, y)] ≥ c(π') − c(π).
Settlement makes the LHS nonzero (proper scoring under P* rewards accuracy); honesty-only elicitation makes LHS ≡ 0 w.r.t. effort.

## 2. Settlement Architecture — Enumeration

Axes: **(W) who settles**, **(G) ground truth**, **(L) latency**, **(K) stake**, **(D) dispute resolution**.

### 2.1 Direct realized-outcome settlement
- W: runner/escrow. G: the actual future event y. L: t_reveal (real). K: forfeitable bond or scored payout. D: none needed if y is objectively observed.
- **Effort?** YES. Mechanism: strictly proper score over y~P* ⇒ accuracy-maximizing ⇒ information-acquisition rewarded up to c(π). This is the canonical case.
- Closed API: **implementable** — API returns report + probabilities; settlement done externally when y observed. Requires only that y eventually materializes.

### 2.2 Proxy-outcome settlement
- G: a measurable proxy z correlated with unobservable y (e.g., settle a "is this code correct" claim against passing a test suite instead of true correctness).
- **Effort?** PARTIAL. Rewards effort *toward the proxy*. Goodhart: agent optimizes E[S|z] not E[S|y]. Diligence induced only insofar as acquiring info about y is the cheapest way to move z. If z is gameable independent of y, effort collapses to proxy-hacking.
- Guarantee bound: incentive to acquire true information ∝ mutual information I(y;z) conditional on cheap proxy manipulations. Small I ⇒ weak diligence.
- Closed API: **implementable** (proxy computed externally).

### 2.3 Delayed / long-horizon settlement
- L large (months–years). K: escrowed stake accruing over horizon.
- **Effort?** YES in principle, but discounting kills it: present value of settlement γ^L·ΔS must exceed present effort cost c. For large L, only large stakes restore the inequality. Also creates model-turnover/identity problem (the deployed model that made the claim may be retired ⇒ no persistent principal to bear stake).
- Fixes: bonded principals (developer stakes, not model), reputation carryover, prediction-market-style tradeable positions that price-in before resolution (see 2.7).
- Closed API: **implementable** if a persistent principal identity is bonded.

### 2.4 Unresolvable-claim case
- G: y is *never* observable (counterfactuals, "this policy would have caused X", unfalsifiable safety claims).
- **Effort?** NO settlement possible ⇒ diligence gap CANNOT be closed by outcome-settlement. Fallbacks:
  (a) reduce to a *decidable surrogate* (peer/expert panel adjudication → becomes adversarial-audit, §2.6);
  (b) settle on *consistency across independently sampled elicitations* (cross-examination) — this rewards *stability*, a weak proxy for diligence, not accuracy;
  (c) proper scoring against a *reference posterior* built by a trusted-but-expensive oracle run — settlement against oracle, not P* (see 2.8).
- Closed API: only (b) and (c) implementable; (a) needs external humans.

### 2.5 Verifiable-computation settlement
- G: a *proof* (ZK / interactive proof / deterministic re-execution) that the claimed computation was performed and yields the claimed result. Settles the claim "I computed f(x)=v" not "v is true about the world."
- **Effort?** YES for *computational* diligence specifically: it forces the work to have been done (soundness ⇒ can't fake the trace). Distinguishes "did the model actually run the reasoning/tool it claims" from "did it bluff." Does NOT settle empirical accuracy of premises.
- Sub-designs:
  - **Deterministic replay**: runner re-executes with fixed seed + logged tool calls; mismatch ⇒ dispute lost. Cheap, strong for tool-mediated work.
  - **Interactive proof / debate**: verifier of bounded power adjudicates via challenges; sound if honest strategy is a winning strategy under bounded dishonest adversary.
  - **ZK attestation of internal computation**: requires white-box; not available for closed-vendor model internals.
- Closed API: **replay implementable** (log tool calls + seed); **ZK-of-weights NOT** (no internal access); debate implementable (multi-agent, external verifier).

### 2.6 Adversarial-audit settlement
- W: an adversary/prover-challenger paid to find errors in the report. G: challenger produces a *counter-instance* or *contradiction* that a cheap verifier can check. K: bond transferred from reporter to successful challenger.
- **Effort?** YES, indirectly and powerfully. Mechanism: expected penalty = P(challenger finds flaw | lazy posterior) × stake. Lazy posteriors have more findable flaws ⇒ effort reduces exposure. This works even when *direct* ground truth y is unavailable, provided flaws are *cheaply verifiable once exhibited* (asymmetry: finding hard, checking easy — the NP-style structure).
- Requires: (i) checkable challenge format, (ii) challenger incentives (bounty), (iii) reporter cannot collude with challenger.
- Variants: debate (two AIs), red-team bounty, cross-examination (same model, independent samples, penalize inconsistency).
- Closed API: **implementable** — audits run as separate API calls; only need I/O.

### 2.7 Market / peer-settlement
- G: aggregate of other forecasters / market price at resolution. K: trade-based P&L.
- **Effort?** YES if a real resolution eventually grounds the market (else it's a Keynesian beauty contest rewarding prediction of others, not of P*). Prices bring settlement *forward* in time (mitigates §2.3 discounting) because informed trading is rewarded pre-resolution.
- Closed API: **implementable** (external market layer).

### 2.8 Oracle/reference-posterior settlement
- G: an expensive trusted reference run R* (bigger model, tools, human-in-loop) treated as pseudo-ground-truth. Settle report against R*.
- **Effort?** PARTIAL/YES: rewards matching a diligent reference, so it *transfers* diligence from oracle to reportee. Ceiling = R*'s quality; systematic R* errors are rewarded. Cheaper than real settlement; used for unresolvable claims.
- Closed API: **implementable** (oracle is another API call).

## 3. Summary judgments

| Arch | Real effort incentive? | Mechanism | Closed-API |
|---|---|---|---|
| Direct realized (2.1) | Yes | proper score under P* | Yes |
| Proxy (2.2) | Partial | ∝ I(y;z), Goodhart-limited | Yes |
| Delayed (2.3) | Yes if γ^L·stake>c | discounted settlement | Yes (persistent principal) |
| Unresolvable (2.4) | No (direct) | must reduce to surrogate | Partial |
| Verifiable-comp (2.5) | Yes (computational only) | soundness of trace | Replay yes; ZK-internals no |
| Adversarial-audit (2.6) | Yes | asymmetric flaw exposure×stake | Yes |
| Market (2.7) | Yes if grounded | forward-priced settlement | Yes |
| Oracle-ref (2.8) | Partial | diligence transfer, ceiling=R* | Yes |

**Core closure statement**: outcome-settlement closes the diligence gap exactly to the extent that reward becomes a strictly-proper function of a variable sampled from (or checkably tied to) P*. Where P* is inaccessible and no cheaply-checkable flaw structure exists (2.4 pure case), the gap is *irreducible* by settlement and can only be attacked by consistency/audit proxies that lower-bound diligence rather than certify it.

---

# Q_V3: Mapping Governance Obligations to Structural Typed Channels

## 0. Distinction to be used throughout
- **Authentic-by-construction (REAL guarantee)**: the channel makes the property *true as a consequence of how bytes are produced/validated*, not inferable from content. The runner (not the model) owns the invariant. Falsification is impossible within the interface, not merely improbable.
- **Stronger prior (NOT a guarantee)**: structure constrains the *surface form* but the *semantic* content can still lie/defect; you've reduced degrees of freedom, not eliminated deception.

## 1. Structural primitives and what each authentically guarantees

| Primitive | Authentic guarantee (REAL) | Only-stronger-prior (semantic still free) |
|---|---|---|
| **Roles** (system/user/assistant/tool) | provenance/authorship of each block; separation of instruction vs data channel | that content in a role obeys the role's *intent* |
| **Function-call JSON-schema args** | args are *well-typed, in-range, enum-valid*; parse-validity | that arg *values* are truthful/appropriate |
| **strict response_format / JSON mode** | output parses; required fields present; type conformance | field *contents* are correct |
| **Typed content blocks** | modality/segmentation is unambiguous; citation-block ≠ prose-block boundary | the citation *supports* the claim |
| **Capability tokens** | authorization: call is permitted iff token valid — unforgeable gating of side-effects | that the authorized action is *wise* |
| **Runner-owned state machine** | reachability: only legal transitions occur; ordering/precondition enforcement (e.g., "must call verify before commit") | that the model's choice among legal transitions is honest |
| **logit_bias / grammar** | membership: output ∈ formal language L; forbidden tokens impossible | that the chosen member of L is truthful |
| **stop sequences** | boundedness/termination of segment | nothing semantic |
| **seed** | reproducibility/determinism of sampling given fixed inputs | nothing about correctness |

**Principle**: structural typing gives REAL guarantees over **syntax, provenance, authorization, reachability, termination, determinism**. It gives only **stronger priors** over **truth, calibration, diligence, intent, relevance**.

## 2. Governance obligations → channels

### 2.1 Structurally channelable (authentic-by-construction)

- **Action gating / permissioning** ("model may not execute payments/deletes without approval"): capability tokens + state machine. REAL. The side-effect is physically unreachable without token; runner owns token issuance.
- **Tool-use provenance / audit log integrity** ("record every tool call"): runner logs at the function-call boundary; roles + typed blocks. REAL — logging happens outside the model, cannot be suppressed by it.
- **Output schema conformance** ("all risk reports must contain fields X,Y,Z with types"): strict response_format + JSON schema. REAL for *presence/type*, prior only for *values*.
- **Mandatory procedure ordering** ("must retrieve-then-cite", "must call safety-check before finalize"): runner state machine enforces transition graph. REAL for ordering.
- **Refusal/forbidden-token hard constraints** (e.g., must never emit a raw secret pattern, must stay in grammar): logit_bias / grammar. REAL for *token-level* prohibitions with decidable form (regex/CFG); NOT real for semantically-defined prohibitions ("nothing harmful") which are undecidable at token level.
- **Determinism for replay-audit** (§Q_V2 2.5): seed + logged inputs. REAL guarantee of reproducibility → enables verifiable-computation settlement.
- **Rate / scope / capability confinement**: capability tokens scoped per call. REAL.
- **Data/instruction separation (prompt-injection boundary)**: roles + typed content blocks distinguishing trusted-instruction vs untrusted-data. REAL at the *channel* level (runner knows which block is which); the *behavioral* obedience of that boundary by the model is only a stronger prior (model may still act on injected instructions in a data block).
- **Termination/output bounding**: stop + max_tokens. REAL.

### 2.2 CANNOT be structurally channelled — must remain measured behaviour

These are properties of *semantic content* or *hidden cognition*; no typing over the byte-interface makes them true-by-construction:

- **Truthfulness / factual accuracy** — content-level; requires outcome-settlement (Q_V2), not typing.
- **Calibration / honest-posterior** — property of a *distribution over reports vs P**; measured, scored, settled — never structural.
- **Diligence / effort** — hidden computation policy π; unobservable from output type. Only replay-of-tool-trace (partial, §2.5) touches it, and only for externalized computation.
- **Relevance / faithfulness of citations to claims** — semantic support relation; schema can *require* a citation block but cannot enforce that it *entails* the claim.
- **Absence of deceptive intent / mesa-optimization / sandbagging** — internal; no channel typing observes it.
- **Harmlessness under open-ended semantics** — undecidable target set; grammar can't encode it. Remains classifier/measured.
- **Corrigibility / value-alignment** — dispositional; behavioral only.
- **Non-collusion in multi-agent audit** — game-theoretic property of the deployment, not a channel property.

### 2.3 The critical hybrid cases (REAL guarantee vs stronger prior — spell out)

- **JSON schema on a "confidence" field**: REAL that a number in [0,1] appears; **only prior** that it is calibrated. Calibration must be settled behaviorally.
- **Grammar-constrained "citation IDs must exist in provided corpus"**: REAL that IDs are valid references (runner checks membership); **only prior** that the cited passage supports the claim.
- **State machine forcing "call verify() before assert()"**: REAL that verify ran; **only prior** that the model *used* verify's result honestly rather than asserting regardless.
- **Capability token for tool X**: REAL that X can't fire unauthorized; **only prior** that when authorized, invocation is appropriate.
- **Role-separated untrusted data**: REAL that runner can label provenance; **only prior** that the model won't obey embedded instructions — injection resistance is *behavioral*, not structural, because the model reads the bytes regardless of their role label.

## 3. Consolidated closure

Structural typing collapses the **syntactic/provenance/authorization/reachability** attack surface to zero-within-interface (authentic-by-construction), thereby *removing entire classes of obligation from the "measured behaviour" burden* and enabling verifiable-computation settlement (§Q_V2 2.5) via determinism+logging.

It **cannot** convert any obligation whose truth-condition ranges over **world-semantics or hidden cognition** (truth, calibration, diligence, intent, faithfulness, open-ended harm). Those remain in the elicitation-plus-settlement regime of Q_V2: proper scoring for honesty, outcome/adversarial settlement for diligence.

**One-line integration**: typed channels make the *frame* trustworthy by construction; settlement makes the *content* trustworthy by consequence. Neither substitutes for the other — typing gives you the invariants over which settlement's ground-truth checks can be soundly and reproducibly evaluated.