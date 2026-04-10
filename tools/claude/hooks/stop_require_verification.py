#!/usr/bin/env python3
"""Stop hook for the researcher project."""

import json
import os
from pathlib import Path

PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
MARKER = PROJECT_DIR / ".claude" / "state" / "verification-required"


def main():
    if not MARKER.exists():
        return

    reason = MARKER.read_text().strip()
    if not reason:
        return

    print(json.dumps({"decision": "block", "reason": f"Verification is still required before stopping: {reason}"}))


if __name__ == "__main__":
    main()
