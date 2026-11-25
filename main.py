#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge entry.

Writes exactly one original funny passive-aggressive note, in the smart
fridge's own voice, to /output/entry.txt. Stdlib only; paths resolved
from this file, never from the cwd.
"""
import os

LINE = "You opened me 47 times today and took nothing. I am not a museum, and the yogurt is not an exhibit."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
