"""Your Week in One Line - make.fun entry, variant 3.

Writes a single original line summing up the entrant's week to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

Variant 3 takes a deliberately different angle from variants 1 and 2,
which were both about bounty and work grind. This one is domestic
absurdity: a tiny kitchen week, win, fail and chaos in one breath.
Deterministic, stdlib only, no network.
"""

import os

# The entry: one line, at most 100 characters.
# Win: the sourdough lived. Fail: the houseplants died.
# Chaos: the smoke alarm now applauds the cooking.
ENTRY = "Sourdough lived, houseplants died, and the smoke alarm now applauds my cooking."

MAX_CHARS = 100


def output_dir() -> str:
    """Grader output dir; MAKEFUN_OUTPUT_DIR stands in for /output locally."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
