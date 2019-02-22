# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import cv2
from scipy.ndimage import binary_fill_holes
from skimage import io, morphology
from skimage import img_as_ubyte

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)
sys.path.insert(0, opj(PRJ_PATH, "pycontour"))

from pycontour.cv2_transform import cv_cnt_to_np_arr
from pycontour.fea import ZernikeMoments


def extract_cnt_using_cv2(img_path):
    img = io.imread(img_path)
    gray = np.dot(img, [0.299, 0.587, 0.114])
    binary = gray < 200
    no_small = morphology.remove_small_objects(binary, min_size=5000, connectivity=8)
    fill = binary_fill_holes(no_small)
    mask = morphology.binary_closing(fill, morphology.disk(10))
    ubyte_mask = img_as_ubyte(mask)
    _, cnts, _ = cv2.findContours(ubyte_mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

    return cnts

def test_ZernikeMoments():
    img_path = os.path.join(TEST_PATH, "data/Imgs/20181218042607.jpg")
    cnts = extract_cnt_using_cv2(img_path)
    test_cnt = cnts[1]

    # convert cv2 contour to numpy array
    np_arr = cv_cnt_to_np_arr(test_cnt)
    zernike_desc = ZernikeMoments(radius=21)
    cnt_fea = zernike_desc.cal_fea(np_arr)

    if len(cnt_fea) != 25:
        raise AssertionError("Zernike Moments feature number is not 25")
