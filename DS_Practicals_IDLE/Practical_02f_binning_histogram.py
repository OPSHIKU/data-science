# -*- coding: utf-8 -*-
"""
PRACTICAL 2F : Binning with histogram and normal fit
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def load_ip_data():
    df = pd.read_csv(path("IP_DATA_ALL.csv"), header=0, low_memory=False,
                     encoding="latin-1",
                     usecols=["Country", "Place.Name", "Latitude", "Longitude"])
    df.rename(columns={"Place.Name": "Place_Name"}, inplace=True)
    return df


def p2f():
    IP_DATA_ALL = load_ip_data()
    x = IP_DATA_ALL["Latitude"].dropna()

    mu, sigma = x.mean(), x.std()
    print("Mean:", mu, " Std:", sigma)

    num_bins = 25
    fig, ax = plt.subplots(figsize=(10, 6))
    n, bins, patches = ax.hist(x, num_bins, density=True, alpha=0.6)

    # Normal distribution curve (computed with numpy)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((bins - mu) / sigma) ** 2)
    ax.plot(bins, y, "--", color="red")

    ax.set_xlabel("Latitude")
    ax.set_ylabel("Probability density")
    ax.set_title("Histogram of Latitude: mu=%.2f, sigma=%.2f" % (mu, sigma))
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    p2f()
