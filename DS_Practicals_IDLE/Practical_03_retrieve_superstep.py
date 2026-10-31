# -*- coding: utf-8 -*-
"""
PRACTICAL 3 : Retrieve superstep
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


def p3():
    sFileName = path("IP_DATA_ALL.csv")
    print("Loading :", sFileName)
    IP_DATA_ALL = load_ip_data()

    ROUTERLOC = IP_DATA_ALL.drop_duplicates(subset=None, keep="first",
                                            inplace=False)
    print("Rows :", ROUTERLOC.shape[0])
    print("Columns :", ROUTERLOC.shape[1])

    ROUTERLOC.to_csv(path("Retrieve_Router_Location.csv"), index=False)
    print("### Done!! ############################################")


if __name__ == "__main__":
    p3()
