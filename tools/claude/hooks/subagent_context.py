#!/usr/bin/env python3
"""SubagentStart hook for the researcher project."""

import json
import sys

MESSAGES = {
    "planner": (
        "You are working on the researcher project. Focus on whether the task affects discovery, ingestion, compilation, or documentation. "
        "Name the narrowest valid verification path and do not edit files."
    ),
    "plan": (
        "You are working on the researcher project. Focus on discovery, ingestion, compilation, or documentation scope. "
        "Name the narrowest valid verification path and do not edit files."
    ),
    "researcher": (
        "You are working on the researcher project. Stay read-only. Use README.md, docs/spec-draft.md, config/sources.yaml, and tools/ as primary evidence."
    ),
    "explore": (
        "You are working on the researcher project. Stay read-only and prefer repo evidence over assumptions."
    ),
    "implementer": (
        "You are working on the researcher project. Keep scope tight. Avoid bulk rewrites of raw/, wiki/, logs/, or output/ unless explicitly requested."
    ),
    "verifier": (
        "You are working on the researcher project. Prefer tools/claude/verify/verify_pipeline.sh and summarize pass/fail precisely."
    ),
}


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    agent_type = str(payload.get("agent_type", "")).lower()
    message = MESSAGES.get(agent_type)
    if not message:
        return

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SubagentStart",
                    "additionalContext": message,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
