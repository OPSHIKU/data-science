# -*- coding: utf-8 -*-
"""
PRACTICAL 5 : Complex data visualizations
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


def p5():
    import matplotlib as ml
    from pandas.plotting import (scatter_matrix, parallel_coordinates,
                                 autocorrelation_plot)

    # ---- Area plot ----
    turnover = [2, 7, 14, 17, 20, 27, 30, 38, 25, 18, 6, 1]
    plt.fill_between(np.arange(12), turnover, color="skyblue", alpha=0.4)
    plt.plot(np.arange(12), turnover, color="Slateblue", alpha=0.6, linewidth=2)
    plt.tick_params(labelsize=12)
    plt.xticks(np.arange(12), np.arange(1, 13))
    plt.xlabel("Month", size=12)
    plt.ylabel("Turnover (K euros) of ice-cream", size=12)
    plt.ylim(bottom=0)
    plt.show()

    # ---- Scatter plot ----
    x = range(-10, 38, 1)
    y = np.array(range(60, 770, 15)) + np.random.randn(48) * 40
    plt.scatter(x, y, s=200, alpha=0.6)
    plt.xlabel("Temperature (°C)", size=12)
    plt.ylabel("Volume per store", size=12)
    plt.show()

    ml.style.use("ggplot")

    # ---- KDE ----
    plt.figure(figsize=(10, 10))
    ser = pd.Series(np.random.randn(1000))
    ser.plot(figsize=(10, 10), kind="kde")
    plt.savefig(path("kde.png"), dpi=600)
    plt.tight_layout()
    plt.show()

    # ---- Scatter matrix ----
    df = pd.DataFrame(np.random.randn(1000, 5),
                      columns=["Y2014", "Y2015", "Y2016", "Y2017", "Y2018"])
    scatter_matrix(df, alpha=0.2, figsize=(10, 10), diagonal="kde")
    plt.savefig(path("scatter_matrix.png"), dpi=600)
    plt.tight_layout()
    plt.show()

    # ---- Parallel coordinates (iris1.csv, else built-in iris) ----
    plt.figure(figsize=(10, 10))
    if os.path.exists(path("iris1.csv")):
        data = pd.read_csv(path("iris1.csv"))
    else:
        from sklearn.datasets import load_iris
        iris = load_iris()
        data = pd.DataFrame(iris.data, columns=["SepalLength", "SepalWidth",
                                                "PetalLength", "PetalWidth"])
        data["Name"] = [iris.target_names[i] for i in iris.target]
    parallel_coordinates(data, "Name")
    plt.savefig(path("parallel_coordinates.png"), dpi=600)
    plt.tight_layout()
    plt.show()

    # ---- Autocorrelation plot ----
    plt.figure(figsize=(10, 10))
    data = pd.Series(0.7 * np.random.rand(1000) +
                     0.3 * np.sin(np.linspace(-9 * np.pi, 9 * np.pi, num=1000)))
    autocorrelation_plot(data)
    plt.savefig(path("autocorrelation_plot.png"), dpi=600)
    plt.tight_layout()
    plt.show()

    ml.style.use("default")


if __name__ == "__main__":
    p5()
