# -*- coding: utf-8 -*-
"""
PRACTICAL 2B : Remove non-printable characters
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import string

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p2b():
    baddata = "Data\x00Science with\x02 funny characters is\x10 great"
    print("Bad data  :", repr(baddata))
    cleandata = "".join(filter(lambda x: x in string.printable, baddata))
    print("Clean data:", repr(cleandata))


if __name__ == "__main__":
    p2b()
