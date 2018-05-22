import cv2
import numpy as np


def lines(img):
    r, c = img.shape
    x = 0
    for i in range(r):
        s = np.sum(img[i])
        if s != 0 and s <= int(0.9 * c * 255):
            x = i
        else:
            if x != 0 and x > y:
                line = img[y:x+1][:]
                remain = img[x+1:r-1][:]
                return True, line, remain
            y = i
    return False, [], []