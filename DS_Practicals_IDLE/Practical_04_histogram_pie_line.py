# -*- coding: utf-8 -*-
"""
PRACTICAL 4 : Histogram, pie chart and line chart
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p4():
    # Histogram
    y = [10, 5, 8, 4, 2]
    plt.hist(y)
    plt.title("Histogram")
    plt.show()

    # Pie chart (simple)
    y = np.array([35, 25, 25, 15])
    plt.pie(y)
    plt.title("Pie Chart")
    plt.show()

    # Pie chart (labels, explode, shadow)
    labels = ["apple", "banana", "cherry", "durian", "elderberries", "figs", "grapes"]
    sizes = [32, 20, 15, 10, 10, 8, 5]
    p = plt.pie(sizes, labels=labels, explode=(0.07, 0, 0, 0, 0, 0, 0),
                autopct="%1.1f%%", startangle=130, shadow=True)
    plt.axis("equal")
    for text in p[1]:
        text.set_fontsize(12)
    plt.show()

    # Line chart with grid
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
    plt.title("Sports Watch Data")
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")
    plt.plot(x, y)
    plt.grid()
    plt.show()

    # Stairs
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
    fig, ax = plt.subplots()
    ax.stairs(y, linewidth=2.5)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()


if __name__ == "__main__":
    p4()
