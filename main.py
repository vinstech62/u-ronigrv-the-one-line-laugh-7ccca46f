#!/usr/bin/env python3
"""The One-Line Laugh — make.fun bounty entry.

Writes one funny line to /output/entry.txt. Deterministic: the same
text on every run, no network, no randomness, no input read.
"""

import os

LINE = (
    "My screen time report says I spent six hours on "
    "productivity apps, mostly deciding which productivity app to use."
)

# The gate requires 1-200 Unicode code points, not only whitespace.
# Fail loudly instead of writing an invalid entry if it ever drifts
# out of range.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of gate range"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
