# -*- coding: utf-8 -*-

import os, sys
import scipy.misc as misc
import cv2
import matplotlib.pyplot as plt

from pycontour import DATA_DIR
from pycontour import cv_cnt_to_np_arr, np_arr_to_cv_cnt

from .extract_cv2_cnts import extract_cnt_using_cv2

def test_cv_np_transfom(tmp_cnt):
    # convert cv2 contour to numpy array
    np_arr = cv_cnt_to_np_arr(tmp_cnt)
    # convert numpy arrary to cv2 contour
    cv_cnt = np_arr_to_cv_cnt(np_arr)

    return cv_cnt


if __name__ == "__main__":
    img_path = os.path.join(DATA_DIR, "images", "brain.jpg")
    img = misc.imread(img_path)
    cnts = extract_cnt_using_cv2(img_path)
    test_cnt = cnts[1]
    cv_cnt = test_cv_np_transfom(test_cnt)
    draw_img = cv2.drawContours(img, [cv_cnt], 0, 255, 3)
