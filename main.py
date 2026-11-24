#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes exactly one job title -- the weirdest one we could think of -- to
/output/entry.txt, where the blind judge reads it.
"""

import os

TITLE = "Professional Mourner (Cash Only, No Refunds)"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
