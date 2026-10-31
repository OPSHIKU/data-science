# -*- coding: utf-8 -*-
"""
PRACTICAL 9 : Colour channel splitting
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


if __name__ == "__main__":
    p9()
