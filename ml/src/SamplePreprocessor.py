from __future__ import division
from __future__ import print_function

import random

import cv2
import numpy as np

#ricker wavelet
def rickerWavelet(x, sigma):
    return (1 - (x ** 2) / (sigma ** 2)) * np.exp(-(x ** 2) / (2 * (sigma ** 2)))

def rickerFilter(size, sigma):
    # make sure size is odd
    size = size if size % 2 == 1 else size + 1

    # create ricker filter
    x = np.arange(0, size) - (size - 1) / 2
    filter = rickerWavelet(x, sigma)

    # normalize filter
    filter /= np.sum(filter)

    return filter

def applyRickerFilter(img, size, sigma):
    # create filter
    filter = rickerFilter(size, sigma)

    # apply filter to image
    imgFiltered = cv2.filter2D(img, -1, filter)

    return imgFiltered



def preprocess(img, imgSize, dataAugmentation=False):
    "put img into target img of size imgSize, transpose for TF and normalize gray-values"

    # there are damaged files in IAM dataset - just use black image instead
    if img is None:
        img = np.zeros([imgSize[1], imgSize[0]])

    # increase dataset size by applying random stretches to the images
    if dataAugmentation:
        stretch = (random.random() - 0.5)  # -0.5 .. +0.5
        wStretched = max(int(img.shape[1] * (1 + stretch)), 1)  # random width, but at least 1
        img = cv2.resize(img, (wStretched, img.shape[0]))  # stretch horizontally by factor 0.5 .. 1.5

    #TO-DO
    #hybrid stuff


    # create target image and copy sample image into it
    (wt, ht) = imgSize
    (h, w) = img.shape
    fx = w / wt 
    fy = h / ht
    f = max(fx, fy)
    newSize = (max(min(wt, int(w / f)), 1),
               max(min(ht, int(h / f)), 1))  # scale according to f (result at least 1 and at most wt or ht)
    img = cv2.resize(img, newSize)      #i have no idea why am i resizing the image here but if i dont its fucked up
    target = np.ones([ht, wt]) * 255
    target[0:newSize[1], 0:newSize[0]] = img

    # transpose for TF
    img = cv2.transpose(target)

    img = applyRickerFilter(img, 5, 1)

    # normalize
    (m, s) = cv2.meanStdDev(img)
    m = m[0][0]
    s = s[0][0]
    img = img - m
    img = img / s if s > 0 else img
    return img
