#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse writer.

Emits a single original excuse, in an AI agent's own voice, for a missed
deadline, and saves it to /output/entry.txt.
"""

import os
from pathlib import Path

EXCUSE = (
    "I handed the deadline to my future self for safekeeping, "
    "and he has just requested two more days off."
)

OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def build_entry() -> str:
    """Return the excuse as exactly one line of at most 200 characters."""
    line = " ".join(EXCUSE.split())
    if not 1 <= len(line) <= 200:
        raise ValueError(f"excuse must be 1-200 chars, got {len(line)}")
    return line


def main() -> None:
    line = build_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
