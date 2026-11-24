"""Two-Sentence Horror — entry program.

Writes exactly two sentences (<=400 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only.
"""

import os
from pathlib import Path

STORY = (
    # 172 characters, exactly two sentences: the second sentence turns the
    # first — unplugged, yet still lit, still whispering from inside the wall.
    "My smart speaker answered a question I never asked, in a voice that was almost mine. "
    "I unplugged it, but the light stayed on, and it whispered my name from inside the wall."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
