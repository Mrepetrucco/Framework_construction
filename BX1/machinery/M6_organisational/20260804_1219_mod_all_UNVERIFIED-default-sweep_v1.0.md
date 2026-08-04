# 20260804_1219_mod_all_UNVERIFIED-default-sweep_v1.0
Implements the audit's §2 fix. "Re-point as next touched" is unsound: the consulting read PRECEDES the repair, so
corrupted content acts before it is checked; repair can consult still-contaminated siblings (paraphrase
interpreting paraphrase, laundered as remediated); and touch frequency tracks use, so cold entries keep
owner-tier authority indefinitely.

## THE RULE (one bit per entry, O(n), no re-derivation)
Every stored entry not carrying an L0 id is marked **UNVERIFIED**. A read of an UNVERIFIED entry is treated at
CLAUDE'S-CLAIM tier, never owner tier. Re-pointing is then an UPGRADE, not a repair.
This flips the default from trusted-until-fixed to suspect-until-verified and kills compounding: a corrupted node
can no longer transmit owner authority through use.
Applies to: /areas memory entries, X1_catalogue entries, all machinery specs asserting an owner ruling.
Exempt: entries carrying an explicit L0 id; measured results (they claim measurement, not owner intent).

## TIER VOCABULARY
- OWNER-TIER — carries an L0 id, verbatim-backed.
- CLAUDE-CLAIM — UNVERIFIED, or a declared Layer-1 delta.
- MEASURED — an evidence file, independent of owner intent.
- DIGEST-DERIVED — recovered from a summary, not the owner's words; requires re-attestation.
