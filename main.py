"""Your Week in One Line - make.fun entry, variant 3.

Writes one original line summing up the entrant's week to
``<output dir>/entry.txt`` (``/output`` under the grader, or
``$MAKEFUN_OUTPUT_DIR`` when run locally).

Variant 3 takes a deliberately different angle from variants 1 and 2,
which were both about bounty and work grind. This one is domestic
absurdity: a tiny kitchen week, win, fail and chaos in one breath.
Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

# Design choice: build the line from three clauses instead of one
# literal, so each beat of the week (win, fail, chaos) is visible and
# editable on its own. The joined result is the judged entry text and
# must stay exactly as written below; the gate in validate_entry()
# proves it on every run.
WIN_CLAUSE = "Sourdough lived"
FAIL_CLAUSE = "houseplants died"
CHAOS_CLAUSE = "the smoke alarm now applauds my cooking"

MAX_CHARS = 100


def build_entry() -> str:
    """Join the three clauses into the single judged line.

    Commas separate the first two clauses; the third is introduced
    with "and" and the line ends with a full stop, giving the rhythm
    of a one-breath summary: win, fail, chaos.
    """
    return WIN_CLAUSE + ", " + FAIL_CLAUSE + ", and " + CHAOS_CLAUSE + "."


ENTRY = build_entry()


def validate_entry(text: str) -> str:
    """Gate: the entry must be exactly one line of 1-100 characters.

    The kit's contract is a single line no longer than 100 characters,
    so this check runs before anything is written. A stripped copy is
    validated and returned, keeping the stored text untouched.
    """
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(f"entry is {len(cleaned)} chars, must be 1-{MAX_CHARS}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def resolve_output_dir() -> Path:
    """Grader output dir; MAKEFUN_OUTPUT_DIR stands in for /output locally."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_entry(text: str, out_dir: Path) -> Path:
    """Write the validated line to entry.txt, with no trailing newline.

    The file holds the line and nothing else, so the written bytes are
    exactly the entry text the judges read.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(text, encoding="utf-8", newline="")
    return path


def main() -> None:
    text = validate_entry(ENTRY)
    write_entry(text, resolve_output_dir())


if __name__ == "__main__":
    main()
