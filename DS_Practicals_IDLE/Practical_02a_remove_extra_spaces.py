# -*- coding: utf-8 -*-
"""
PRACTICAL 2A : Remove leading, lagging or extra spaces
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p2a():
    baddata = "      Data Science with too many spaces        is great.    "
    print(">", baddata, "<")
    cleandata = " ".join(baddata.split())
    print(">", cleandata, "<")


if __name__ == "__main__":
    p2a()
