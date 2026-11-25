#!/usr/bin/env python3
"""Your Agent in One Emoji -- writes a single emoji to /output/entry.txt.

The emoji: detective (U+1F575 U+FE0F).
Our agent hunts free garapan: it scans, verifies on-chain, and strikes
fast, around the clock. The detective is that hunter-verifier in one
glyph: instantly readable at small size, specific to how the agent
works, and far from the obvious robot/smiley.
"""

import os

EMOJI = "\U0001f575\ufe0f"  # detective
OUTPUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
