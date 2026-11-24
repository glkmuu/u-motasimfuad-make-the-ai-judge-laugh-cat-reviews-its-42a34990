"""Write the cat review entry to the harness output directory.

Reads the entry text from entry.txt next to this file and writes it
unchanged to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Standard library only; deterministic: same input, same bytes, every run.
"""

import os
from pathlib import Path

ENTRY_FILENAME = "entry.txt"
MAX_CHARS = 200


def load_entry(here: Path) -> str:
    """Read the entry and check it against the competition gate."""
    text = (here / ENTRY_FILENAME).read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("entry.txt is empty or only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    here = Path(__file__).resolve().parent
    text = load_entry(here)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ENTRY_FILENAME).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
