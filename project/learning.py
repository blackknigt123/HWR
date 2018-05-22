"""This module must run once and the clf variable must be saved to the disk to be used later"""
import idx2numpy as idx
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree, svm
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier


def learn():
    train = idx.convert_from_file('dataset/train')
    train_label = idx.convert_from_file('dataset/trainlabels')
    # getting training dataset in idx format and converting it into a numpy array

    train = np.reshape(train, (112800, 784))
    train_label = np.reshape(train_label, 112800)

    # train = np.reshape(train, (697932,784))                     # converting the 3d arrays to 2d arrays
    # train_label = np.reshape(train_label, 697932)

    clf = RandomForestClassifier(n_estimators=100)
    # clf = tree.DecisionTreeClassifier()                         # creating a dct object
    clf = clf.fit(train, train_label)        # learning process

    return clf
