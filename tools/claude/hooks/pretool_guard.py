#!/usr/bin/env python3
"""Protect secrets and environment files in the researcher project."""

import json
import re
import sys

PROTECTED_PATTERNS = [
    r"(^|/)\.env(\..*)?$",
    r"(^|/)secrets?/",
    r"(^|/)credentials?/",
    r"\.(key|pem|p12)$",
]


def emit(reason):
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    if payload.get("tool_name") not in {"Edit", "Write"}:
        return

    tool_input = payload.get("tool_input", {})
    path = tool_input.get("file_path") or tool_input.get("path") or ""

    for pattern in PROTECTED_PATTERNS:
        if re.search(pattern, path):
            emit("Secrets, credentials, and environment files are protected.")
            return


if __name__ == "__main__":
    main()
