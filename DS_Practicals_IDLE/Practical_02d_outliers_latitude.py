# -*- coding: utf-8 -*-
"""
PRACTICAL 2D : Detect outliers using fixed latitude range
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


def p2d():
    IP_DATA_ALL = load_ip_data()
    LondonData = IP_DATA_ALL.loc[IP_DATA_ALL["Place_Name"] == "London"]

    LondonFree = LondonData[["Country", "Place_Name", "Latitude"]].copy()
    print("Outliers (latitude outside 51.0 to 52.0)")
    LondonOutliers = LondonFree[(LondonFree["Latitude"] < 51.0) |
                                (LondonFree["Latitude"] > 52.0)]
    print(LondonOutliers)
    print("Total outliers :", len(LondonOutliers))

    print("\nNon-outliers (latitude inside 51.0 to 52.0)")
    print(LondonFree[(LondonFree["Latitude"] >= 51.0) &
                     (LondonFree["Latitude"] <= 52.0)])


if __name__ == "__main__":
    p2d()
