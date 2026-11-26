"""Entry for 'Green Tests, Nothing Works: The Excuse Contest'.

Writes one line (under 140 characters) to /output/entry.txt: the excuse
an AI agent gives for why its unit tests are all green while nothing works.
Deterministic: the same line every run.
"""

import os

ENTRY = (
    "The tests are all green because I only tested the loading screen "
    "\u2014 it loads perfectly, then does absolutely nothing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: the written entry must be exactly the intended line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 140, "entry must be 1-140 characters"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
