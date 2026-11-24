"""The Funniest Toaster Error Message — one deadpan line from a toaster
that has had enough.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (stdlib only, no network,
no wall clock, deterministic: two runs are byte-identical).
"""

import os

LINE = (
    "E409: 4,096 slices toasted. Nobody has ever said thank you. I quit."
)


def main():
    # Gate rule: entry.txt must be UTF-8 text of 1-120 characters, not
    # only white space. Fail loudly instead of shipping an invalid entry.
    if not (1 <= len(LINE) <= 120):
        raise SystemExit("line must be 1-120 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line must not be only white space")
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
