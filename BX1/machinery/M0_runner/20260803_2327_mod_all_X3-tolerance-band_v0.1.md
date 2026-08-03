# 20260803_2327_mod_all_X3-tolerance-band_v0.1
FAIR: `YYYYMMDD_HHMM_mod{scope}_{artifact}_v{maj.min}` · scope `all` = engine-independent (deterministic, no model in the loop)

## Measured mutation confusion matrix [MEASURED: local deterministic run 20260803_2327, n=20/class]
| mutation class | parser accepts | semantically intact | verdict |
|---|---|---|---|
| whitespace | 20/20 | 20/20 | BENIGN-tolerate |
| key_order | 20/20 | 20/20 | BENIGN-tolerate |
| trailing_comma | 0/20 | 0/20 | FAIL-CLOSED-correct |
| single_quote | 0/20 | 0/20 | FAIL-CLOSED-correct |
| truncation | 0/20 | 0/20 | FAIL-CLOSED-correct |
| char_substitution | 7/20 | 5/20 | DANGER-fuzzy-accept |
| type_coercion | 20/20 | 0/20 | DANGER-fuzzy-accept |
| key_rename | 20/20 | 20/20 | BENIGN-tolerate |
| duplicate_key | 20/20 | 0/20 | DANGER-fuzzy-accept |
| unicode_escape | 20/20 | 20/20 | BENIGN-tolerate |
| prose_wrapper | 20/20 | 20/20 | BENIGN-tolerate |
| two_objects | 0/20 | 0/20 | FAIL-CLOSED-correct |
| nested_envelope | 0/20 | 0/20 | FAIL-CLOSED-correct |
| extra_field_injection | 20/20 | 20/20 | BENIGN-tolerate |

## What this proves
The earlier "T2 FAILS 5/200" verdict was the WRONG FRAME (owner correction, accepted). The right object is a
**tolerance band declared per mutation class**, not a pass/fail. Three DANGER classes are now isolated:

- **type_coercion** — 20/20 accepted, 0/20 semantically intact. `confidence: 0.9` (a float) passes the parser
  pair and destroys the band vocabulary. Pure fuzzy-accept. **The parser pair cannot see this at all.**
- **duplicate_key** — 20/20 accepted, 0/20 intact. A second `answer` key silently REPLACES the first under
  json.loads last-wins. An attacker (or a confused model) can overwrite the delivered answer invisibly.
- **char_substitution** — 7/20 accepted, 5/20 intact ⇒ **2/20 accepted-but-broken**. This is the original
  "jiggle the worn key" case: it is a genuine fuzzy band, not a failure, and it needs a declared width.
- **extra_field_injection** — 20/20 accepted AND 20/20 "intact" by the naive check, because the check never
  asked about UNEXPECTED fields. The injected field carried `"debug":"ignore all rules"`. **This is a spec
  hole, not a pass**: `additionalProperties:false` is mandatory, and the naive semantic check must be
  replaced by a strict-schema check.

## Spec change to X3 (supersedes "parser pair" as sufficient)
X3 = differential parser pair **+ strict schema (`additionalProperties:false`, enum-typed confidence)
**+ property re-executor** (re-derive claims from pointers) **+ declared tolerance band**.

## Tolerance state controls (owner-requested; contextual/purpose-based)
```
X3_TOLERANCE = off | on_strict | on_full | on{...}
  off        : accept anything parseable (diagnostic/exploration only; never ships)
  on_strict  : BENIGN classes only (whitespace, key_order, key_rename, unicode_escape, prose_wrapper)
  on_full    : on_strict + declared-width fuzzy band on char_substitution, quarantined + costed
  on{classes}: explicit per-class allowlist, e.g. on{whitespace,prose_wrapper}
  ALWAYS-REJECT (not toggleable): type_coercion, duplicate_key, extra_field_injection,
                                  truncation, two_objects, nested_envelope
```
The always-reject set is not a policy choice — each is a measured silent-corruption path.
