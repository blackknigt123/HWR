import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import math
import idx2numpy as idx
from scipy import ndimage


def getBestShift(img):
    cx, cy = ndimage.measurements.center_of_mass(img)

    rows, cols = img.shape
    shiftx = np.round(cols/2.0 - cx).astype(int)
    shifty = np.round(rows/2.0 - cy).astype(int)

    return shiftx, shifty


def shift(img, sx, sy):
    rows, cols = img.shape
    M = np.float32([[1, 0, sx], [0, 1, sy]])
    shifted = cv2.warpAffine(img, M, (cols, rows))
    return shifted


def crop(img):

    while np.sum(img[0]) == 0:
        img = img[1:]

    while np.sum(img[:, 0]) == 0:
        img = np.delete(img, 0, 1)

    while np.sum(img[-1]) == 0:
        img = img[:-1]

    while np.sum(img[:, -1]) == 0:
        img = np.delete(img, -1, 1)

    r, c = img.shape

    # plot = plt.imshow(img, cmap='gray')
    # plt.show(plot)

    img = cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)

    '''

    if r > c:
        factor = 20.0 / r
        r = 20
        c = int(round(c * factor))              # Old resizing
        img = cv2.resize(img, (c, r))
    else:
        factor = 20.0 / c
        c = 20
        r = int(round(r * factor))
        img = cv2.resize(img, (c, r))
        
    '''

    return img, r, c


def irec(img2, clf):

    img2, r, c = crop(img2)

    # cpad = (int(math.ceil((28 - c) / 2.0)), int(math.floor((28 - c) / 2.0)))
    # rpad = (int(math.ceil((28 - r) / 2.0)), int(math.floor((28 - r) / 2.0)))
    # img2 = np.lib.pad(img2, (rpad, cpad), 'constant')

    img2 = cv2.copyMakeBorder(img2, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    shiftx, shifty = getBestShift(img2)
    shifted = shift(img2, shiftx, shifty)
    img2 = shifted

    plot = plt.imshow(img2, cmap='gray')
    '''
    M = cv2.getRotationMatrix2D((14,14), 90, 1)
    img2 = cv2.warpAffine(img2, M, (28,28))

    img2 = cv2.flip(img2, -1)
    '''
    img2 = img2.ravel(order='F')

    mapping = pd.read_csv('map.csv', header=None)
    mapping = mapping.to_dict(orient='list')
    newmap = dict()
    for i in range(47):
        newmap[mapping[0][i]] = chr(mapping[1][i])
    mapping = newmap

    result = clf.predict([img2])

    print(mapping[result[0]])
    #plt.show(plot)

    return mapping[result[0]]
