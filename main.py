#!/usr/bin/env python3
"""Your Agent in One Emoji — entrypoint.

Writes a single emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). The glyph alone, nothing else.
"""
import os

# Second edit (genuine revision): the octopus reads as a sea creature
# first — its "many tools" meaning needs a second thought, and the
# brief says the glyph must land without explanation. The ant captures
# the agent's defining character at a glance: a small autonomous
# worker that tirelessly carries out tasks in the background, hauling
# loads far bigger than itself, without being asked twice. It reads
# instantly at small size, and it is distinctive — the field is full
# of robots, brains, compasses and owls, almost nobody sends an ant.
EMOJI = "🐜"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(f"wrote {path}: {EMOJI!r}")


if __name__ == "__main__":
    main()
