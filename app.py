from unittest import result
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


SHRED_SIZE = 100


def preload_img(path):
    img = np.array(Image.open(path))
    x = int(img.shape[0] % SHRED_SIZE)
    y = int(img.shape[1] % SHRED_SIZE)

    if not (img.shape[1] - y) % 2 == 0 or (img.shape[0] - x) % 2 == 0:
        return False
    return img[0 : img.shape[0] - x, 0 : img.shape[1] - y]


def merge(img1, img2, axis):
    return np.concatenate((img1, img2), axis=axis)


def shredder(img, width):

    sizer = np.mod(np.arange(img.shape[1]), 2 * width)

    odds = img[:, sizer < width]
    evens = img[:, sizer >= width]

    return odds, evens


def app():
    img = preload_img("1.jpg")
    if isinstance(img, bool):
        print("Please provide different size value!")
        return
    img1, img2 = shredder(np.rot90(img, 1), SHRED_SIZE)
    output = merge(img1, img2, 0)

    img1, img2 = shredder(np.rot90(output, 3), SHRED_SIZE)
    output = merge(img1, img2, 1)

    plt.imshow(output)
    plt.show()


app()
