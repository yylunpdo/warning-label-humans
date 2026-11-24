#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes one line (<=160 chars) to /output/entry.txt.
Pure stdlib, no network.
"""

import os

ENTRY = (
    "WARNING: this human runs on 6 hours of sleep, 3 coffees, and pure "
    "spite. Do not shake, do not rush, and never ask if it is okay "
    "before 9am."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 160, f"entry too long: {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
