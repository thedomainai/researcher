#!/usr/bin/env python3
"""Session start hook for the researcher project."""

import json
import os
import subprocess
from pathlib import Path

PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))


def run(command):
    try:
        return subprocess.check_output(
            command, cwd=PROJECT_DIR, stderr=subprocess.DEVNULL, text=True
        ).strip()
    except Exception:
        return ""


def main():
    try:
        json.load(os.sys.stdin)
    except Exception:
        pass

    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    dirty = run(["git", "status", "--short", "--untracked-files=no"])
    marker = PROJECT_DIR / ".claude" / "state" / "verification-required"

    lines = [
        "Project: researcher",
        f"Root: {PROJECT_DIR}",
        "Core surfaces: config/, tools/, raw/, wiki/, docs/.",
    ]
    if branch:
        lines.append(f"Branch: {branch}")
    if dirty:
        lines.append("Dirty tracked files exist. Check git status before broad edits.")
    if marker.exists() and marker.read_text().strip():
        lines.append(
            "VERIFICATION REQUIRED: run tools/claude/verify/verify_pipeline.sh before stopping."
        )
    lines.append(
        "Use planner/researcher/implementer/verifier for structured work. Treat raw/ as source data and wiki/ as compiled output."
    )

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": "\n".join(lines),
                }
            }
        )
    )


if __name__ == "__main__":
    main()
