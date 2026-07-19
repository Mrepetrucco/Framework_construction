#!/usr/bin/env bash
# Pre-push secret scan. Exit non-zero (block push) on ANY credential-shaped hit.
# Patterns: OpenAI sk-, GitHub ghp_/github_pat_, Google AIza, anthropic sk-ant-,
# generic key=/token=/secret= assignments, and .env presence in the tree.
set -euo pipefail
ROOT="${1:-.}"
fail=0
if git -C "$ROOT" ls-files 2>/dev/null | grep -Eiq '(^|/)\.?env$|\.env$|ENVs'; then
  echo "BLOCK: an env/key file is tracked by git."; fail=1
fi
hits=$(grep -RInE \
  'sk-[A-Za-z0-9]{20,}|sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AIza[A-Za-z0-9_-]{30,}|(api[_-]?key|secret|token)\s*[:=]\s*["'"'"'][A-Za-z0-9_-]{16,}' \
  --exclude-dir=.git --exclude='scrub_and_scan.sh' "$ROOT" 2>/dev/null || true)
if [ -n "$hits" ]; then
  echo "BLOCK: credential-shaped strings found:"; echo "$hits" | sed 's/[:=].*/[:=] <REDACTED>/'; fail=1
fi
if [ "$fail" -ne 0 ]; then echo "SCAN FAILED — push aborted."; exit 1; fi
echo "SCAN CLEAN — no credential-shaped content. Safe to push."
