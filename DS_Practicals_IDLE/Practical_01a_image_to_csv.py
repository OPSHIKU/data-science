# -*- coding: utf-8 -*-
"""
PRACTICAL 1A : Image to CSV (HORUS)
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


if __name__ == "__main__":
    p1a()
