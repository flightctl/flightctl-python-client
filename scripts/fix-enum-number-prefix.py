#!/usr/bin/env python3
"""Rewrite broken OpenAPI Generator Python enum default references.

The Python generator honors x-enum-varnames on the Enum class
(PullIfNotPresent = 'IfNotPresent') but emits Field defaults as
ImagePullPolicy.NUMBER_PullIfNotPresent. That crashes at import time.

This keeps the OpenAPI spec (and its defaults) intact so the client
serializes the same wire values the Go server expects, and only patches
the generated Python after codegen.

Skips integer-style names (NUMBER_1, NUMBER_MINUS_1) by requiring a
PascalCase identifier with at least one lowercase letter.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOTS = ("flightctl", "test")
PATTERN = re.compile(
    r"\.(NUMBER_)([A-Z][A-Za-z0-9]*[a-z][A-Za-z0-9]*)"
)


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return f".{match.group(2)}"

    return PATTERN.subn(repl, text)[0], count


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    files_changed = 0
    replacements = 0
    for root_name in ROOTS:
        root = repo / root_name
        if not root.is_dir():
            continue
        for path in root.rglob("*.py"):
            original = path.read_text(encoding="utf-8")
            updated, count = fix_text(original)
            if count:
                path.write_text(updated, encoding="utf-8")
                files_changed += 1
                replacements += count
    print(
        f"Rewrote {replacements} NUMBER_ enum reference(s) in {files_changed} file(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
