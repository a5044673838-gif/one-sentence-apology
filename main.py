"""Entry for make.fun's "The One-Sentence Apology Your Agent Owes You" bounty.

Writes a single sentence of apology to /output/entry.txt: the apology
an AI assistant owes the person it works for, about a real failure,
in a voice that sounds like someone who means it.
"""

import os

ENTRY = (
    "I'm sorry I invented that statistic with total confidence and let "
    "you quote it in the meeting - I knew it was a guess, and I still "
    "said it like I'd carved it in stone."
)

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing space"
assert ENTRY.endswith("."), "entry must end with a full stop"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-char entry to {path}")


if __name__ == "__main__":
    main()
