# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import scipy.misc as misc
from scipy.ndimage import binary_fill_holes
from skimage import img_as_ubyte
from skimage.morphology import remove_small_objects
from skimage.morphology import disk, binary_closing
import cv2
import matplotlib.pyplot as plt
from pycontour import DATA_DIR


def extract_cnt_using_cv2(img_path):
    img = misc.imread(img_path)
    binary = img > 156
    no_small = remove_small_objects(binary, min_size=5000, connectivity=8)
    fill = binary_fill_holes(no_small)
    selem = disk(10)
    mask = binary_closing(fill, selem)
    ubyte_mask = img_as_ubyte(mask)
    _, cnts, _ = cv2.findContours(ubyte_mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

    return cnts

if __name__ == "__main__":
    img_path = os.path.join(DATA_DIR, "images", "brain.jpg")
    cnts = extract_cnt_using_cv2(img_path)
