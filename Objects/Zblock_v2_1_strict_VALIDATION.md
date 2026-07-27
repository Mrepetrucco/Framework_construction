# Zblock v2.1 — strict-tool-use validation record

- Date: 27 Jul 2026 · model claude-haiku-4-5 · n=1/arm · this-turn total ~$0.008
- `strict:true` is GA (no beta header; `strict-tools-*` header rejected as unknown).
- Requirement: every schema object sets `additionalProperties:false` and lists all properties in `required`.
- Result: plain Z-tool bind 200/tool_use/4-field-parse; full v2.1 (envelope+j_trace+meter) 200/tool_use/all-field-parse.
- Hardens Ruling 2 (Q2 adopt-with-robustness). Claude-only; portable floor uses validate-then-parse (see Public_Dump/parity/02).
