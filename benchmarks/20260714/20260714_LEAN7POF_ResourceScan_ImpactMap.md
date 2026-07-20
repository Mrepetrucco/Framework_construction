# LEAN7POF — Resource Scan & Impact Map (for build-in)
**Provenance:** 7POF v1 · 14 July 2026 · Opus. Sources enumerated live: `anthropics/skills` via GitHub API (`skills/claude-api/{python,shared}` + parent), local `/mnt/skills`, Drive `Python_for_Github`. Impact = value to the LEAN-vs-FULL equivalence/cost benchmark and to LEAN7POF generally. **Team-Builder gate (A4): listing ≠ adoption; each passes the six-principle gate at build.**

## A. anthropics/skills — claude-api (GitHub, `main`)
| File / module | Type | Source | Impact map |
|---|---|---|---|
| `python/claude-api/batches.md` | API doc + SDK code | anthropics/skills | **HIGH — cost.** Message Batches API = **50% price cut**, ≤100k reqs/batch, supports caching+tools. The single biggest lever to fit the benchmark under $20. Build into harness as default run mode. |
| `shared/prompt-caching.md` | Design doc | anthropics/skills | **HIGH — cost.** Prefix-match caching; breakpoint on last system block caches the large **FULL-7POF** governance prefix across all FULL-arm cells. Stacks with batches. |
| `shared/token-counting.md` | API doc + code | anthropics/skills | **HIGH — measurement.** `count_tokens` (model-specific) = exact, deterministic LEAN-vs-FULL input-cost delta. Replaces estimated pricing in the ledgers. *Do not use tiktoken.* |
| `shared/models.md` | Catalog + capabilities API | anthropics/skills | **MED — correctness.** Confirms exact IDs `claude-opus-4-8` / `claude-fable-5`; `models.retrieve` for live max_tokens/effort/context. Guards against stale pricing/ID drift. |
| `python/claude-api/streaming.md` | API doc | anthropics/skills | **LOW–MED.** Streaming for long FULL-arm deliverable cells (avoids truncation-as-refusal confound). |
| `shared/error-codes.md` | Reference | anthropics/skills | **MED — robustness.** Canonical retry/error taxonomy for the concurrent harness (separates server-retryable from invalid_request). |
| `python/claude-api/tool-use.md`, `shared/tool-use-concepts.md` | API docs | anthropics/skills | **LOW** for this benchmark (no tools in specimen cells); relevant later for agentic LEAN specimens. |
| `python/managed-agents/*`, `shared/managed-agents-*.md` (17 files) | Managed-Agents API | anthropics/skills | **WATCH — strategic.** A real "managed agents" API surface (memory, multiagent, scheduled deployments, sandboxes). Potentially reifies parts of the 7POF agent roster as actual API agents — but that's a framework-architecture decision, not a benchmark input. Flag for a dedicated Team-Builder pass; **not built in this cycle.** |
| `shared/live-sources.md`, `claude-platform-on-aws.md`, `platform-availability.md`, `agent-design.md`, `model-migration.md` | Docs | anthropics/skills | **LOW** for benchmark; `model-migration.md` (144 KB) useful if models rev mid-programme. |

## B. Local skills (`/mnt/skills`)
| Skill | Type | Source | Impact map |
|---|---|---|---|
| `data:statistical-analysis` | Plugin skill | local | **HIGH — the verdict.** TOST / two-proportion & two-sample z / power / CI — the equivalence + superiority statistics themselves. Core build-in. |
| `data:validate-data` | Plugin skill | local | **MED — QA gate.** Pre-share methodology/bias/aggregation check on the benchmark before any locked claim. |
| `data:analyze`, `data:create-viz` | Plugin skills | local | **MED.** Results analysis + cost/quality plots for the deliverable. |
| `context-loss-refusal-guard` (user) | User skill | local | **HIGH — already central.** Refusal-vs-context-loss routing + Fable screening during the run. Reuse as-is. |
| `s1-doc-conventions` (user) | User skill | local | **LOW here** (md working artifacts); needed only if a formal Office deliverable is produced. |
| `skill-creator`, `mcp-builder` | Example skills | local | **LOW–MED.** For packaging any new LEAN7POF tooling as an installable skill later. |

## C. Drive
| Resource | Type | Source | Impact map |
|---|---|---|---|
| `Python_for_Github/Build_Orchestration_Mode` | Python harness | Drive | **HIGH — already integrated (v0.12).** 10-way `ThreadPoolExecutor` (60 calls/38 s measured). Reuse; extend with batches for the async/cheap path. |
| `Structured-Output-Schema-Optimizer` (Drive/Agents) | Reconciler | Drive | **MED.** tri-family strict-intersection (VZ) for zblock-emission specimen cells. |
| `fable_prompt_screen.py` | Screening tool | Drive/LEAN7POF | **HIGH — validity.** Screen Fable-arm prompts; route refusals to Opus so refusal-noise ≠ quality signal. |

## Build-in decision (this cycle)
**BUILD:** batches.md + prompt-caching.md + token-counting.md + error-codes.md (harness); `data:statistical-analysis` (+`validate-data`) (stats/QA); reuse concurrency harness + `fable_prompt_screen.py` + VZ reconciler.
**DEFER (own Team-Builder pass):** the Managed-Agents API surface — architecturally significant, out of scope for a benchmark cycle.

*Resource scan · 7POF v1 · 14 July 2026 · enumerated live; adoption gated on six principles.*
