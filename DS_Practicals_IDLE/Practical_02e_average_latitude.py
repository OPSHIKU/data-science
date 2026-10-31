# -*- coding: utf-8 -*-
"""
PRACTICAL 2E : Average latitude by country and place name
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


def load_ip_data():
    df = pd.read_csv(path("IP_DATA_ALL.csv"), header=0, low_memory=False,
                     encoding="latin-1",
                     usecols=["Country", "Place.Name", "Latitude", "Longitude"])
    df.rename(columns={"Place.Name": "Place_Name"}, inplace=True)
    return df


def p2e():
    IP_DATA_ALL = load_ip_data()
    small = IP_DATA_ALL[["Country", "Place_Name", "Latitude"]]
    AverageLatitude = small.groupby(["Country", "Place_Name"])["Latitude"].mean()
    print(AverageLatitude)


if __name__ == "__main__":
    p2e()
