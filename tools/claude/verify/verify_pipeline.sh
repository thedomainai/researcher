#!/usr/bin/env bash
# Verify the researcher pipeline structure and Python syntax.

set -euo pipefail

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../../.." && pwd)}"
PASS=0
FAIL=0

check() {
  local desc="$1"
  shift
  if "$@" >/dev/null 2>&1; then
    echo "PASS: $desc"
    PASS=$((PASS + 1))
  else
    echo "FAIL: $desc"
    FAIL=$((FAIL + 1))
  fi
}

check "README.md exists" test -f "$PROJECT_DIR/README.md"
check "config/sources.yaml exists" test -f "$PROJECT_DIR/config/sources.yaml"
check "raw/index.jsonl exists" test -f "$PROJECT_DIR/raw/index.jsonl"
check "wiki/index.md exists" test -f "$PROJECT_DIR/wiki/index.md"
check "wiki/index.html exists" test -f "$PROJECT_DIR/wiki/index.html"
check "tools/fetch_latest.py exists" test -f "$PROJECT_DIR/tools/fetch_latest.py"
check "tools/compile_wiki.py exists" test -f "$PROJECT_DIR/tools/compile_wiki.py"
check "tools package compiles" python3 -m compileall "$PROJECT_DIR/tools"

echo ""
echo "Result: $PASS passed, $FAIL failed"
exit "$FAIL"
