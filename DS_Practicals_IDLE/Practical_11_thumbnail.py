# -*- coding: utf-8 -*-
"""
PRACTICAL 11 : Thumbnail function on an image
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


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


if __name__ == "__main__":
    p11()
