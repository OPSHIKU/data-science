# -*- coding: utf-8 -*-
"""
PRACTICAL 6 : Assess superstep (fill NaN values)
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import numpy as np
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def _fruit_df():
    return pd.DataFrame(
        [[10, np.nan, 30, 40],
         [7, 14, 21, 28],
         [55, np.nan, 8, 12],
         [15, 14, np.nan, 8],
         [7, 1, 1, np.nan],
         [np.nan, 4, 9, 2]],
        columns=["Apple", "Orange", "Banana", "Pear"],
        index=["Basket1", "Basket2", "Basket3", "Basket4", "Basket5", "Basket6"])


def p6():
    print("#################################")
    print("THE ORIGINAL VALUES")
    print(_fruit_df())

    df = _fruit_df()
    print("\nREPLACING THE VALUES WITH MEAN")
    df.fillna(df.mean(), inplace=True)
    print(df)

    df = _fruit_df()
    print("\nREPLACING THE VALUES WITH MEDIAN")
    df.fillna(df.median(), inplace=True)
    print(df)

    df = _fruit_df()
    print("\nREPLACING THE VALUES WITH MODE")
    for column in df.columns:
        df[column] = df[column].fillna(df[column].mode()[0])
    print(df)

    df = _fruit_df()
    print("\nREPLACING THE VALUES WITH MINIMUM")
    df.fillna(df.min(), inplace=True)
    print(df)


if __name__ == "__main__":
    p6()
