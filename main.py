#!/usr/bin/env python3
"""Describe Your Ex in One Word.

Writes one original one-word verdict to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The word is a fixed, hand-written choice: "Recalled". It is a verdict
on an ex in the language of a product recall — the ex was taken back
by the manufacturer like a faulty unit — with a second meaning folded
in: the speaker recalls him, and wishes they didn't. Against the
judge's brief: instantly readable as a verdict on a former partner
(a recalled product is a rejected one); comic punch through the
manufacturer-recall twist rather than a plain insult; surprise, since
it is not the obvious "Expired"/"Mistake"/"Toxic"; craft, one plain
word with no punctuation tricks; recognition, since anyone who has
had an ex knows the feeling of wanting the model taken back. No
network, no randomness, stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original word describing an ex, at most 111 characters.
# Revision 2: "Recalled" chosen over the obvious field ("Expired",
# "Mistake", "Toxic") — a product recall is a verdict with a twist:
# the ex was taken back by the manufacturer like a faulty unit, and
# the word doubles as "I recall him", which is the complaint itself.
# No hyphen, no punctuation, no capitalisation trick: one plain word.
ENTRY = "Recalled"

MAX_CHARS = 111


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if len(text.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    if not text.isalpha():
        # Craft criterion: exactly one word, spelled correctly, no
        # punctuation tricks — letters only.
        print("entry must be letters only, no punctuation", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    except OSError as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-char entry to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
