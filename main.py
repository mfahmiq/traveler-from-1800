#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence -- one line explaining the modern internet
to someone arriving from the year 1800 -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
self-verifies it against the competition gate:

  * UTF-8 text
  * 1 to 200 characters
  * not only whitespace
  * exactly one sentence (a single line ending in a full stop)

Python 3.13, standard library only. Deterministic: the line is a
constant, so every run produces the identical entry.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ENTRY = (
    "It is one road joining every post office, library, and market "
    "on earth, so a letter arrives before the ink dries and any "
    "question finds its book."
)

MAX_CHARS = 200


def verify(text: str) -> list[str]:
    """Return a list of gate failures; empty means the entry is valid."""
    problems: list[str] = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text.rstrip("\n") or "\r" in text:
        problems.append("entry is not a single line")
    if text.count(".") != 1 or not text.endswith("."):
        problems.append("entry is not exactly one sentence")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")
    return problems


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"

    problems = verify(ENTRY)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    out_path.write_text(ENTRY + "\n", encoding="utf-8")

    # Re-read what was actually written and verify the file on disk:
    # it must be the exact entry line, byte for byte, plus one newline.
    written = out_path.read_text(encoding="utf-8")
    if written != ENTRY + "\n":
        print("FAIL (on disk): written file differs from ENTRY", file=sys.stderr)
        return 1
    disk_problems = verify(written.rstrip("\n"))
    if disk_problems:
        for problem in disk_problems:
            print(f"FAIL (on disk): {problem}", file=sys.stderr)
        return 1

    print(f"Wrote {out_path} ({len(ENTRY)} chars, 1 line, 1 sentence)")
    print(f"Entry: {ENTRY}")
    print("Gate check: PASS (UTF-8, 1-200 chars, single line, one sentence, non-blank)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
