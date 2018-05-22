import cv2
import numpy as np


def chars(img):
    noc = 0                 # No of components
    comp = []               # List of components
    x = 0
    img = np.transpose(img)
    r, c = img.shape
    for i in range(r):
        if np.sum(img[i]) != 0:
            x = i
        else:
            if x != 0 and x > y:
                noc += 1
                line = img[:][y:x + 1]
                line = np.transpose(line)
                comp.append(line)
                remain = img[:][x + 1:r - 1]
                chars(remain)
            y = i
    return noc, comp
