import cv2
import numpy as np


def space(img):

    while np.sum(img[0]) == 0:
        img = img[1:]

    while np.sum(img[:, 0]) == 0:
        img = np.delete(img, 0, 1)

    while np.sum(img[-1]) == 0:
        img = img[:-1]

    while np.sum(img[:, -1]) == 0:
        img = np.delete(img, -1, 1)

    img = np.transpose(img)
    r, c = img.shape

    count = 0
    flag = False
    for i in range(r):
        if np.sum(img[i]) != 0 and flag:
            flag = False
        elif np.sum(img[i]) == 0:
            count += 1
            flag = True

    sps.sort()

    if count > 3:
        avg = np.average(sps[0:2])
    else:
        avg = sps[0]

    return avg