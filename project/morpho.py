import numpy as np
import cv2


def erode_dilate(img, preference, iterations=1):
    # This function erodes or dilates the image based on preference
    r, c = img.shape
    for _ in range(iterations):
        for i in range(1, r-1):
            for j in range(1, c-1):
                if preference == 1:
                    val = min(img.item(i, j), img.item(i, j + 1), img.item(i + 1, j), img.item(i + 1, j + 1))
                else:
                    val = max(img.item(i, j), img.item(i, j + 1), img.item(i + 1, j), img.item(i + 1, j + 1))
                img.itemset((i, j), val)

    return img


def open_close(img, preference, iterations=1):
    # This function opens or close the image on basis of the preference
    for _ in range(iterations):
        if preference == 1:
            img = erode_dilate(erode_dilate(img, 1, iterations), 2)
        else:
            img = erode_dilate(erode_dilate(img, 2, iterations), 1)
    return img
