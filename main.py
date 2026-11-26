"""The Printer Finally Answers — entry program (v2).

Writes the printer's one-line comeback to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) with no trailing newline, and prints it to stdout.

v2: staccato machine-log rhythm — the flat counted lines sound more like
the device itself than the flowing v1 sentence, same three counts and
same resignation twist.
"""

import os

LINE = (
    "41,208 pages. 312 jams. 97 thumps. "
    "Today I printed my final document: my resignation. "
    "Please collect it from tray 2."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
