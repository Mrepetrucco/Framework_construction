# 20260804_1141_mod_all_X2R-conflict-discovery_v0.2
OWNER RULING: a conflict-FREE DSL is INTRACTABLE. Confirmed by the source that proposed it — classifier conflicts
"require distributional knowledge that is generally unavailable". We therefore take CONFLICT DISCOVERY and ERROR
HANDLING from the literature and DROP the conflict-freedom guarantee entirely.

## DECIDABILITY HIERARCHY [EXTERNAL: arXiv 2603.18174]
| tier | conflict kinds | decidable? |
|---|---|---|
| crisp | logical contradiction · structural shadowing · structural redundancy | YES — SAT / BDD |
| embedding | co-firing over embedding regions | reduces to spherical-cap intersection |
| classifier | probable conflict · soft shadowing · calibration conflict | NO — needs distributional knowledge generally unavailable |

## CONFLICT CLASSES — the discovery set (adopted whole, no discard)
CRISP [Al-Shaer & Hamed, firewall anomaly taxonomy — the canonical set]:
1. SHADOWING — a higher-priority rule subsumes a lower one, making it unreachable.
2. REDUNDANCY — two rules have equivalent conditions.
3. CORRELATION — conditions OVERLAP BUT NEITHER SUBSUMES THE OTHER. *** This is MULTI-MATCH. ***
4. GENERALIZATION — a less-specific rule masks a more-specific one.
(+ IRRELEVANCE, carried in later work.)
PROBABILISTIC [arXiv 2603.18174]:
5. PROBABLE CONFLICT — both signals co-fire on a non-trivial fraction of real inputs.
6. SOFT SHADOWING — the higher-priority rule dominates most of the time, so priority resolves in its favour EVEN
   WHEN THE OTHER SIGNAL IS FAR MORE CONFIDENT — i.e. routing against the evidence.
7. CALIBRATION CONFLICT — category sets are structurally disjoint yet the classifier activates both near
   semantic boundaries.

## MULTI-MATCH HANDLING — SUPERSEDES the previous "hard stop / integrity fault" ruling
Multi-match IS the CORRELATION class: by definition neither rule subsumes the other, so there is no dominance
relation to exploit and any automatic pick is arbitrary. Therefore:
- **RAISE TO USER, WITHOUT PREJUDICE ACROSS THE MULTI-MATCH FRAME.** All co-firing frames are presented together,
  in the order they fired, with no ranking, no highlighted default, and no language implying one is preferred.
- The literature's resolution strategies (specificity-overrides · high-majority-overrides · first-match-overrides)
  are RECORDED AS DISCOVERED AND EXPLICITLY NOT ADOPTED: each imposes a prejudice the correlation class does not
  license. First-match in particular would encode ledger order as truth.
- Present the CONFLICT CORRELATION GROUP (the co-firing set), not a pairwise diff.
- Raising is a NORMAL terminal state, not an error and not a degradation. It is never scored as a failure.

## TRAINING PROHIBITION (owner ruling)
No component of X2R may be trained on, fine-tuned against, or seeded from material that maps to or reproduces
CORPUS-DRIVEN FABRICATION patterns (the 55%-shared class). Discovery rules are taken from the literature as
STATED ALGORITHMS; they are not learned from generated examples. This keeps the router's failure modes
independent of the fabrication class it must help surface.
