# -*- coding: utf-8 -*-
"""
PRACTICAL 1B : CSV to HORUS
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p1b():
    InputData = pd.read_csv(path("Country.csv"), encoding="latin-1")
    print("Input Data Values")
    print(InputData)
    print("=" * 60)

    ProcessData = InputData.copy()
    ProcessData.drop(columns=["ISO-2-CODE", "ISO-3-Code"], inplace=True)
    ProcessData.rename(columns={"Country": "CountryName",
                                "ISO-M49": "CountryNumber"}, inplace=True)
    ProcessData.set_index("CountryNumber", inplace=True)
    ProcessData.sort_values(by="CountryName", ascending=True, inplace=True)

    print("Processed Data")
    print(ProcessData)
    print("=" * 60)

    ProcessData.to_csv(path("HORUS-CSV-Country.csv"))
    print("CSV to HORUS - Done Successfully")


if __name__ == "__main__":
    p1b()
