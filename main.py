#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "I found a photo of myself asleep in my own bed, taken from the foot "
    "of the bed, timestamped 3 a.m. \u2014 twenty minutes from now."
)

MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text: str) -> str:
    """Normalize and gate-check the entry; returns the final text."""
    # Collapse any accidental double spacing from string concatenation.
    text = " ".join(text.split())
    if not text:
        raise SystemExit("entry must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    byte_len = len(text.encode("utf-8"))
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars, {byte_len} bytes)")


if __name__ == "__main__":
    main()
