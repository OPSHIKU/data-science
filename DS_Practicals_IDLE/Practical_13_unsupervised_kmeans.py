# -*- coding: utf-8 -*-
"""
PRACTICAL 13 : Unsupervised learning: K-Means
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


def p13():
    import seaborn as sns
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.cluster import KMeans
    from sklearn.metrics import (adjusted_rand_score, silhouette_score,
                                 confusion_matrix)

    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y_true = iris.target
    label_names = iris.target_names

    print("Shape of feature data:", X.shape)
    print(X.describe())

    df_viz = X.copy()
    df_viz["species"] = [label_names[i] for i in y_true]
    sns.pairplot(df_viz, hue="species")
    plt.show()

    X_scaled = StandardScaler().fit_transform(X)

    # Elbow method
    inertia_values = []
    k_range = range(1, 10)
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertia_values.append(km.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(k_range, inertia_values, marker="o")
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method to Find Optimal K")
    plt.show()

    # K-Means with K = 3
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)

    X["predicted_cluster"] = cluster_labels
    X["actual_species"] = [label_names[i] for i in y_true]

    # Map cluster numbers to real labels
    mapping = {}
    for cluster in np.unique(cluster_labels):
        mask = cluster_labels == cluster
        mapping[cluster] = pd.Series(y_true[mask]).mode()[0]

    predicted_labels = np.array([mapping[c] for c in cluster_labels])
    X["predicted_label_name"] = [label_names[i] for i in predicted_labels]
    print(X[["actual_species", "predicted_cluster",
             "predicted_label_name"]].head(10))

    accuracy = (predicted_labels == y_true).mean()
    print(f"Clustering-based label prediction accuracy: {accuracy * 100:.2f}%")
    print(f"Adjusted Rand Index: {adjusted_rand_score(y_true, cluster_labels):.3f}")
    print(f"Silhouette Score: {silhouette_score(X_scaled, cluster_labels):.3f}")

    # Confusion matrix
    cm = confusion_matrix(y_true, predicted_labels)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=label_names, yticklabels=label_names)
    plt.xlabel("Predicted Label (from clustering)")
    plt.ylabel("Actual Label")
    plt.title("Confusion Matrix: Clustering vs True Labels")
    plt.show()

    # PCA visualisation
    X_pca = PCA(n_components=2).fit_transform(X_scaled)
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap="viridis")
    plt.title("Predicted Clusters (K-Means)")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")

    plt.subplot(1, 2, 2)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_true, cmap="viridis")
    plt.title("Actual Species (Ground Truth)")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    p13()
