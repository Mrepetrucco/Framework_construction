#!/usr/bin/env bash
# KEYED-TURN push. Requires GITHUB_TOKEN in env (from a disk .env). Never echoes it.
# Usage: source the .env to export GITHUB_TOKEN, then: ./push_runner.sh <repo-name>
set -euo pipefail
REPO="${1:-lean7pof}"
: "${GITHUB_TOKEN:?GITHUB_TOKEN not set — source the uploaded .env first}"
./scrub_and_scan.sh .                      # HARD GATE: aborts on any secret
git init -q; git add -A
git -c user.email="owner@local" -c user.name="owner" commit -qm "framework + interpreter agent snapshot"
# token used only in the remote URL for this call; not written to any tracked file
git remote add origin "https://x-access-token:${GITHUB_TOKEN}@github.com/OWNER/${REPO}.git" 2>/dev/null || true
git push -u origin HEAD:main
git remote set-url origin "https://github.com/OWNER/${REPO}.git"   # scrub token from remote config
echo "Pushed. Remote URL scrubbed of token."
