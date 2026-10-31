# -*- coding: utf-8 -*-
"""
PRACTICAL 14 : Correlation between two datasets
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p14():
    # If your files are real Excel files, change read_csv to read_excel
    math = pd.read_csv(path("students_math.csv"))
    science = pd.read_csv(path("student_science.csv"))

    print("Math Dataset:")
    print(math)
    print("\nScience Dataset:")
    print(science)

    data = pd.merge(math, science, on="Student_ID")
    print("\nMerged Dataset:")
    print(data)

    correlation = data["Math"].corr(data["Science"])
    print("\nCorrelation between Math and Science =", round(correlation, 2))

    print("\nCorrelation Matrix:")
    print(data[["Math", "Science"]].corr())

    plt.scatter(data["Math"], data["Science"])
    plt.xlabel("Math Marks")
    plt.ylabel("Science Marks")
    plt.title("Correlation between Math and Science Marks")
    plt.show()


if __name__ == "__main__":
    p14()
