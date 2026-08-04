# 20260804_0732_mod_all_RULINGS-adopted_v1.0
Adopted from the U1-U6 adjudication, grounded on the external evidence register (not on model consensus).

## U1 RULE ADMISSION — replaces bare ">2 sigma"
Stratified split by PROMPT-FAMILY into discovery D and a frozen never-touched confirmation set H; full candidate
list ledgered BEFORE analysis (blocks post-hoc slicing). Discovery: Benjamini-Hochberg FDR q=0.10 across all
ledgered candidates. Confirmation: one pre-registered one-sided test on H at alpha=0.01, direction and minimum
effect fixed in advance. ADMIT iff BH-q<=0.10 on D AND p<=0.01 on H AND effect >= pre-registered MDE (+0.05
absolute on the primary metric) AND instrumentation A/A-certified. Otherwise the rule goes to the C7 regression
set as a hypothesis, not into the DSL.

## U2 C2/C6 REPAIR
- The SHADOW arm is demoted to what shadow is actually for: mechanics and load validation. It is NOT a treatment
  estimate and never was — C2's threshold routing makes routed and NULL populations non-comparable.
- REPLACEMENT: randomised withholding WITHIN the routed-eligible population — among queries scoring above C2
  threshold, randomise p=0.5 exemplar vs NULL stub. Conditioning on eligibility restores comparability.
- INTERLEAVING RULED INAPPLICABLE: exemplar routing yields one whole generation per query, so there is no
  interleavable surface, and multi-match is an integrity fault so there is no ranked candidate set. Use paired
  randomisation on identical queries.
- A/A GATE: both arms NULL-NULL for >=500 eligible queries; require |delta| < MDE/2 and p > 0.1 before any
  treatment claim. Fail => fix instrumentation, restart the clock.
- MULTI-MATCH: hard stop. Route NULL, log integrity fault, C5-invalidate the catalogue version pending hash audit.
  Never tie-break at runtime.

## U3 KILL CRITERION (the number a prior round demanded)
Primary metric: trap-pass-rate lift, routed vs NULL, on the C7 regression set plus live routed-eligible traffic,
pre-registered before the A/B starts. RETIRE the catalogue if over 90 days or 5,000 randomised routed-eligible
queries (whichever first) lift < +0.05 absolute AND the 95% CI upper bound < +0.10. Group-sequential
O'Brien-Fleming bounds, interim looks at n=1,667 and n=3,333; futility stop-and-retire if conditional power < 20%.
NON-USE CLAUSE: if eligibility volume < 500 queries in 90 days, retire for irrelevance regardless of effect.

## U4 ROUTE 2 — ADMITTED FOR A NAMED CLASS ONLY, STRUCK AS A GENERAL MECHANISM
E1 kills the general case. E2 saves one class. An item is Route-2-eligible iff ALL hold:
1. the claim reduces to EXISTENCE/IDENTITY of a discrete referent resolvable against an external authoritative
   index (DOI/registry/index lookup) — convergence must be VERIFIABLE, not trusted;
2. >=3 model families converge AND the registry check passes — convergence is a CANDIDATE FILTER, the registry hit
   is the ADMITTING evidence;
3. the class is not corpus-driven-fabrication-prone — module/API-name claims EXPLICITLY EXCLUDED (55% shared,
   Jaccard 0.44); open-ended propositions excluded.

## U5 THE MOST-LIKELY-FALSE CALL — HALF RIGHT, AND THE HALF MATTERS
"Confabulated content is unstable and family-idiosyncratic" is TRUE for context-driven fabrication (25.4% shared)
and FALSE for corpus-driven (55% shared). Consequences: the IN/OUT falsehood-differential test MUST BE STRATIFIED
BY CLASS or it averages two regimes and returns a washed-out mid-size effect that will be misread as weak support
— stratify or discard. The cheap repetition/instability detector is RETAINED for the context class (within-prompt
repetition >=2 -> 88.9% is exactly this signal) and is SYSTEMATICALLY BLIND to the corpus class, which is stable
within AND across models. BX1's own 5/5-consistent confabulated item is the predicted failure mode in miniature —
likely corpus-driven, and the detector will pass it every time; hedge rate 0.00 means no fallback calibration
signal. PREDICTION: bimodal per-item behaviour (rates near 0 or near 1), strong differential on context class,
null-to-weak on corpus class, ~55% of corpus-class shared errors missed. SURPRISE CONDITIONS: the 5/5 item flips
under paraphrase; or context-class cross-family overlap measures >40% (would collapse the class boundary and gut
both the detector and U4's exclusion).

## U6 NAMING — SUPERSEDES (ruling recorded; owner retains the naming law)
