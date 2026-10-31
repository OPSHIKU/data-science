# -*- coding: utf-8 -*-
"""
DATA SCIENCE PRACTICALS - IDLE VERSION
Karina Bacche - 264447

HOW TO RUN IN IDLE
1. Put this file and your data files in the SAME folder
   (Country.csv, IP_DATA_ALL.csv, iris1.csv, hough.jpg, 1.png,
    students_math.csv, student_science.csv).
2. Open this file in IDLE and press F5.
3. Type a practical number from the menu (e.g. 1a, 2c, 12, 14).
4. Close each graph window to continue.

Install once in Command Prompt:
pip install pandas numpy matplotlib seaborn scikit-image pillow opencv-python nltk scikit-learn openpyxl
"""

import os
import string
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Folder where this script lives (so file names work from IDLE)
BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


# =====================================================================
# PRACTICAL 1A - Image to CSV (HORUS)
# =====================================================================
def p1a(image_name="1.png"):
    from skimage import io

    image = io.imread(path(image_name))
    plt.imshow(image)
    plt.title("Input Image")
    plt.axis("off")
    plt.show()

    print("Image Shape :", image.shape)
    print("Height :", image.shape[0])
    print("Width :", image.shape[1])

    if image.ndim == 2:  # grayscale -> make 3 channels
        image = np.stack([image] * 3, axis=-1)

    height, width, channels = image.shape
    print("Color Mode :", "RGB" if channels == 3 else "RGBA")

    ys, xs = np.indices((height, width))
    r = image[:, :, 0].ravel()
    g = image[:, :, 1].ravel()
    b = image[:, :, 2].ravel()
    a = image[:, :, 3].ravel() if channels == 4 else np.full(r.shape, 255)

    df = pd.DataFrame({
        "X": xs.ravel(), "Y": ys.ravel(),
        "Red": r, "Green": g, "Blue": b, "Alpha": a
    })

    print(df.head(10))
    print("\nRows :", df.shape[0])
    print("Columns :", df.shape[1])

    df.to_csv(path("Image_to_HORUS.csv"), index=False)
    print("\nCSV File Saved Successfully.")


# =====================================================================
# PRACTICAL 1B - CSV to HORUS
# =====================================================================
def p1b():
    InputData = pd.read_csv(path("Country.csv"), encoding="latin-1")
    print("Input Data Values")
    print(InputData)
    print("=" * 60)

    ProcessData = InputData.copy()
    ProcessData.drop(columns=["ISO-2-CODE", "ISO-3-Code"], inplace=True)
    ProcessData.rename(columns={"Country": "CountryName",
                                "ISO-M49": "CountryNumber"}, inplace=True)
    ProcessData.set_index("CountryNumber", inplace=True)
    ProcessData.sort_values(by="CountryName", ascending=True, inplace=True)

    print("Processed Data")
    print(ProcessData)
    print("=" * 60)

    ProcessData.to_csv(path("HORUS-CSV-Country.csv"))
    print("CSV to HORUS - Done Successfully")


# =====================================================================
# PRACTICAL 2A - Remove leading / lagging / extra spaces
# =====================================================================
def p2a():
    baddata = "      Data Science with too many spaces        is great.    "
    print(">", baddata, "<")
    cleandata = " ".join(baddata.split())
    print(">", cleandata, "<")


# =====================================================================
# PRACTICAL 2B - Remove non-printable characters
# =====================================================================
def p2b():
    baddata = "Data\x00Science with\x02 funny characters is\x10 great"
    print("Bad data  :", repr(baddata))
    cleandata = "".join(filter(lambda x: x in string.printable, baddata))
    print("Clean data:", repr(cleandata))


# =====================================================================
# PRACTICAL 2C - Reformatting data entry (dates)
# =====================================================================
def p2c():
    baddate = datetime.date(2019, 10, 31)
    baddata = format(baddate, "%Y-%m-%d")
    gooddate = datetime.datetime.strptime(baddata, "%Y-%m-%d")
    gooddata = format(gooddate, "%d %B %Y")

    print("Bad Date  :", baddata)
    print("Good Date :", gooddata)


# =====================================================================
# Helper: load IP_DATA_ALL.csv (used in 2d, 2e, 2f, 3)
# =====================================================================
def load_ip_data():
    df = pd.read_csv(path("IP_DATA_ALL.csv"), header=0, low_memory=False,
                     encoding="latin-1",
                     usecols=["Country", "Place.Name", "Latitude", "Longitude"])
    df.rename(columns={"Place.Name": "Place_Name"}, inplace=True)
    return df


# =====================================================================
# PRACTICAL 2D - Outliers using fixed latitude range
# =====================================================================
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


# =====================================================================
# PRACTICAL 2E - Average latitude by country and place name
# =====================================================================
def p2e():
    IP_DATA_ALL = load_ip_data()
    small = IP_DATA_ALL[["Country", "Place_Name", "Latitude"]]
    AverageLatitude = small.groupby(["Country", "Place_Name"])["Latitude"].mean()
    print(AverageLatitude)


# =====================================================================
# PRACTICAL 2F - Binning with histogram and normal distribution fit
# =====================================================================
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


# =====================================================================
# PRACTICAL 3 - Retrieve superstep
# =====================================================================
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


# =====================================================================
# PRACTICAL 4 - Histogram, pie chart, line chart
# =====================================================================
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


# =====================================================================
# PRACTICAL 5 - Complex visualizations
# =====================================================================
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


# =====================================================================
# PRACTICAL 6 - Assess superstep (replace NaN)
# =====================================================================
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


# =====================================================================
# PRACTICAL 7 - Line detection using Hough transform
# =====================================================================
def p7(image_name="hough.jpg"):
    import cv2

    img = cv2.imread(path(image_name))
    if img is None:
        print("Could not read", image_name, "- put it in the same folder.")
        return

    plt.figure(figsize=(8, 6))
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 200)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 68,
                            minLineLength=15, maxLineGap=250)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.flatten()
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    else:
        print("No lines detected.")

    plt.figure(figsize=(8, 6))
    plt.title("Line Detection using Hough Transform")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()


# =====================================================================
# PRACTICAL 8 - Basic NLP
# =====================================================================
def p8():
    import nltk
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("stopwords")

    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    from nltk.probability import FreqDist

    text = """
    Natural Language Processing (NLP) is a field of Artificial Intelligence.
    It focuses on the interaction between computers and human language.
    NLP helps machines understand, interpret, and generate human language.
    """

    print("Sentence Tokenization:")
    print(sent_tokenize(text), "\n")

    print("Word Tokenization:")
    words = word_tokenize(text)
    print(words, "\n")

    print("Removing Stopwords:")
    stop_words = set(stopwords.words("english"))
    filtered_words = [w for w in words
                      if w.lower() not in stop_words and w.isalnum()]
    print(filtered_words, "\n")

    print("Frequency Distribution:")
    fdist = FreqDist(filtered_words)
    for word, freq in fdist.most_common():
        print(f"{word}: {freq}")


# =====================================================================
# PRACTICAL 9 - Split image into colour channels
# =====================================================================
def p9(image_name="1.png"):
    import matplotlib.image as mpimg

    img = mpimg.imread(path(image_name))
    print("Size:", img.shape)

    t = 1
    plt.figure(figsize=(8, 8))
    plt.title("(" + str(t) + ") Original")
    plt.imshow(img)
    plt.show()

    if img.ndim == 3:
        for c in range(img.shape[2]):
            t += 1
            plt.figure(figsize=(8, 8))
            plt.title("(" + str(t) + ") Channel: " + str(c))
            plt.imshow(img[:, :, c])
            plt.show()


# =====================================================================
# PRACTICAL 10 - Edges of an image
# =====================================================================
def p10(image_name="1.png"):
    from PIL import Image

    imageIn = Image.open(path(image_name))
    fig1 = plt.figure(figsize=(8, 8))
    fig1.suptitle("Audi R8", fontsize=20)
    plt.imshow(imageIn)
    plt.show()

    mask = imageIn.convert("L")
    th = 49
    imageOut = mask.point(lambda i: i < th and 255)
    imageOut.save(path("audi.png"))

    imageTest = Image.open(path("audi.png"))
    fig2 = plt.figure(figsize=(8, 8))
    fig2.suptitle("Audi R8 Edge", fontsize=20)
    plt.imshow(imageTest, cmap="gray")
    plt.show()


# =====================================================================
# PRACTICAL 11 - Thumbnail
# =====================================================================
def p11(image_name="1.png"):
    from PIL import Image

    nSize = 4
    img = Image.open(path(image_name))

    plt.figure(figsize=(nSize, nSize))
    plt.title("Unchanged")
    plt.imshow(img)
    plt.show()

    img.thumbnail((64, 64), Image.Resampling.LANCZOS)  # resizes in place

    plt.figure(figsize=(nSize, nSize))
    plt.title("Resized")
    plt.imshow(img)
    plt.show()

    plt.figure(figsize=(nSize, nSize))
    plt.title("Resized with Bi-Cubic")
    plt.imshow(img, interpolation="bicubic")
    plt.show()

    print("### Done!! ###############################################")


# =====================================================================
# PRACTICAL 12 - Supervised learning (Linear Regression)
# =====================================================================
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


# =====================================================================
# PRACTICAL 13 - Unsupervised learning (K-Means on Iris)
# =====================================================================
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


# =====================================================================
# PRACTICAL 14 - Correlation between two datasets
# =====================================================================
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


# =====================================================================
# MENU
# =====================================================================
PRACTICALS = {
    "1a": (p1a, "Image to CSV (HORUS)"),
    "1b": (p1b, "CSV to HORUS"),
    "2a": (p2a, "Remove extra spaces"),
    "2b": (p2b, "Remove non-printable characters"),
    "2c": (p2c, "Reformat date entry"),
    "2d": (p2d, "Outliers using latitude range"),
    "2e": (p2e, "Average latitude by country/place"),
    "2f": (p2f, "Binning, histogram + normal fit"),
    "3":  (p3,  "Retrieve superstep"),
    "4":  (p4,  "Histogram, pie chart, line chart"),
    "5":  (p5,  "Complex data visualizations"),
    "6":  (p6,  "Assess superstep (fill NaN)"),
    "7":  (p7,  "Hough transform line detection"),
    "8":  (p8,  "Basic NLP"),
    "9":  (p9,  "Colour channel splitting"),
    "10": (p10, "Edge detection"),
    "11": (p11, "Thumbnail"),
    "12": (p12, "Supervised learning (price prediction)"),
    "13": (p13, "Unsupervised learning (K-Means)"),
    "14": (p14, "Correlation between two datasets"),
}


def main():
    while True:
        print("\n========== DATA SCIENCE PRACTICALS ==========")
        for key, (_, title) in PRACTICALS.items():
            print(f"  {key:>3} : {title}")
        print("    q : Quit")
        choice = input("Enter practical number: ").strip().lower()

        if choice == "q":
            break
        if choice in PRACTICALS:
            try:
                PRACTICALS[choice][0]()
            except FileNotFoundError as e:
                print("\nFile not found:", e)
                print("Place the required data file in the same folder as this script.")
            except Exception as e:
                print("\nError:", type(e).__name__, "-", e)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
