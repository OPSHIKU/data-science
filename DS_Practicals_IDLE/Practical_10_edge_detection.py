# -*- coding: utf-8 -*-
"""
PRACTICAL 10 : Edge detection of an image
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


if __name__ == "__main__":
    p10()
