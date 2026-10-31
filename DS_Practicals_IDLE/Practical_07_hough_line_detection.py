# -*- coding: utf-8 -*-
"""
PRACTICAL 7 : Line detection using Hough transform
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


if __name__ == "__main__":
    p7()
