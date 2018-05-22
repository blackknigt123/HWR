import cv2
import numpy as np
import threading as th
import queue
import pickle
import os
import matplotlib.pyplot as plt
# importing custom modules...
import globalthresh as gt
import separate_lines as lin
import separate_chars as chs
import morpho
import learning as lern
import irecognition as rec

img = cv2.imread(r'test_images/groot2.jpg', 1)                                # image acquired


def create_clf(clfque):
    if os.path.isfile('clf3.pckl'):
        clf = pickle.load(open('clf3.pckl','rb'))
    else:
        clf = lern.learn()
        clf_file=open('clf3.pckl', 'wb')  # saving the clf variable into memory
        pickle.dump(clf, clf_file)
        clf_file.close()

    clfque.put(clf)


clfque = queue.Queue()
tempThread = th.Thread(target=create_clf, args=(clfque,))
tempThread.start()

b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]                                                      # channels separated

img = np.uint8(0.2989 * r + 0.587 * g + 0.114 * b)                    # converted to gray scale

img = cv2.bitwise_not(gt.gthresh(img))                                # binarization and inversion

iterations = 2

img = morpho.open_close(morpho.open_close(img, 1, iterations), 2, iterations)
                                                                    # noise reduction by opening and closing the image
file = open('text.txt', 'w')                                           # opening text file in write mode
r = img
flag = True

clf = clfque.get()

while flag:
    flag, l, r = lin.lines(r)

    if flag:
        noc, comps = chs.chars(l)

        for i in range(noc):
            mychr = rec.irec(comps[i], clf)
            file.write(mychr)
        file.write('\n')
file.close()
