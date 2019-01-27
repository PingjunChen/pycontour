# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import matplotlib.pyplot as plt

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)
sys.path.insert(0, opj(PRJ_PATH, "pycontour"))

from pycontour.cv2_transform import np_arr_to_cv_cnt
from pycontour.img import build_cnt_mask
from pycontour.cnt import get_cnt_area


def test_build_cnt_mask():
    np_arr = np.array([[1., 3., 5., 4., 2.], [1., 0., 3., 4., 3]])
    mask = build_cnt_mask(np_arr)
    # plt.imshow(mask)
    # plt.show()
    mask_pixel_num = np.count_nonzero(mask==255)

    # calculate the contour area
    cv_cnt = np_arr_to_cv_cnt(np_arr)
    cnt_area = get_cnt_area(cv_cnt)

    assert mask_pixel_num < cnt_area, "pixels are inside the polygon"
