# -*- coding: utf-8 -*-
"""
PRACTICAL 2C : Reformatting data entry
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import datetime

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p2c():
    baddate = datetime.date(2019, 10, 31)
    baddata = format(baddate, "%Y-%m-%d")
    gooddate = datetime.datetime.strptime(baddata, "%Y-%m-%d")
    gooddata = format(gooddate, "%d %B %Y")

    print("Bad Date  :", baddata)
    print("Good Date :", gooddata)


if __name__ == "__main__":
    p2c()
