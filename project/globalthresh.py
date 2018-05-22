import numpy as np
import cv2


def lthresh(img, T):
    x, y = img.shape
    m1 = m2 = 0
    a = b = 1
    for i in range(x):
        for j in range(y):
            if img.item((i, j)) > T:
                m1 += img.item((i, j))
                a +=1
            else:
                m2 += img.item((i, j))
                b += 1

    return np.uint8(m1 / a), np.uint8(m2 / b)


def gthresh(img):
    nimg = img

    T1=127
    m1, m2 = lthresh(nimg,T1)
    T2 = (int(m1) + int(m2)) / 2
    while T1 - T2 != 0:
        T1 = T2
        m1, m2 = lthresh(nimg, T2)
        T2 = (int(m1) + int(m2)) / 2

    x, y = nimg.shape
    for i in range(x):
        for j in range(y):
            if nimg.item((i, j)) > T2:
                nimg.itemset((i, j), 255)
            else:
                nimg.itemset((i, j), 0)

    return nimg
