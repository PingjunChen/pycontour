# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import scipy.misc as misc
import matplotlib.pyplot as plt
from scipy.ndimage import binary_fill_holes
from skimage import img_as_ubyte
from skimage.morphology import remove_small_objects
from skimage.morphology import disk, binary_closing
import cv2

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(__file__))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)
from pycontour.cv2_transform import cv_cnt_to_np_arr, np_arr_to_cv_cnt


def extract_cnt_using_cv2(img_path):
    img = misc.imread(img_path)
    gray = np.dot(img, [0.299, 0.587, 0.114])
    binary = gray < 200
    no_small = remove_small_objects(binary, min_size=5000, connectivity=8)
    fill = binary_fill_holes(no_small)
    selem = disk(10)
    mask = binary_closing(fill, selem)
    ubyte_mask = img_as_ubyte(mask)
    _, cnts, _ = cv2.findContours(ubyte_mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

    return cnts


def test_cv_np_transfom():
    img_path = os.path.join("./data/Imgs", "20181218042607.jpg")
    img = misc.imread(img_path)
    cnts = extract_cnt_using_cv2(img_path)
    test_cnt = cnts[1]

    # convert cv2 contour to numpy array
    np_arr = cv_cnt_to_np_arr(test_cnt)
    # convert numpy arrary to cv2 contour
    cv_cnt = np_arr_to_cv_cnt(np_arr)

    draw_img = cv2.drawContours(img, [cv_cnt], 0, (0, 0, 255), 7)

    # plt.imshow(draw_img)
    # plt.show()
