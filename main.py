"""Write one line to /output/entry.txt: the worst AI advice, in 140 chars or fewer.

The line is delivered in a real assistant's confident, tidy voice —
"Great question!" up front, a concrete fix a reader could actually
follow (turn the radio up to silence squeaky brakes), and the terrible
logic stated as calm fact: if you can't hear the problem, it typically
resolves itself. One line, no wasted words, the wince lands on the
last clause.
"""

import os

TEXT = (
    "Great question! To fix squeaky brakes, simply turn the radio up — "
    "if you can't hear the problem, it typically resolves itself."
)


def main() -> None:
    # The entry is a single line by contract: guard against accidental
    # edits that would add a newline or surrounding whitespace, since
    # the submitted entry.txt must stay byte-for-byte identical, and
    # hold the bounty's 140-character cap.
    assert "\n" not in TEXT and TEXT == TEXT.strip() and TEXT
    assert len(TEXT) <= 140
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
