# -*- coding: utf-8 -*-
"""
PRACTICAL 12 : Supervised learning: price prediction
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


def p12():
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score

    try:
        data = fetch_california_housing()  # needs internet the first time
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = data.target
    except Exception:
        # Offline fallback: use the dummy housing file next to this script
        print("(No internet - using dummy_housing.csv instead)")
        d = pd.read_csv(path("dummy_housing.csv"))
        y = d["Price"].values
        X = d.drop(columns=["Price"])

    print("Dataset shape:", X.shape)
    print("Features:", list(X.columns))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    print("\nTraining samples:", X_train.shape[0])
    print("Testing samples:", X_test.shape[0])

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\n========== Model Evaluation ==========")
    print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
    print("R² Score:", r2_score(y_test, y_pred))

    comparison = pd.DataFrame({"Actual Price": y_test,
                               "Predicted Price": y_pred})
    print("\n========== Actual vs Predicted ==========")
    print(comparison.head(10))

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    lo = min(y_test.min(), y_pred.min())
    hi = max(y_test.max(), y_pred.max())
    plt.plot([lo, hi], [lo, hi], color="red", linewidth=2,
             label="Perfect Prediction")
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted Median House Values")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    p12()
