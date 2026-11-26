#!/usr/bin/env python3
"""What the Elevator Would Say entry (make.fun).

Writes a single original one-line joke, in the elevator's own voice, to
``entry.txt`` inside the output directory (``/output`` in the grader
sandbox, overridable with the ``OUTPUT_DIR`` environment variable for
local runs).

Pure Python standard library only. Deterministic: the same line every run.
"""

import os

LINE = (
    "You hold the door for strangers, then mash the close button on "
    "your own coworkers. I see you. I see all of you."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
