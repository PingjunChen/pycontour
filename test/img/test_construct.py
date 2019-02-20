# -*- coding: utf-8 -*-

import sys
import numpy as np

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
    np_arr = np.array([[10, 40, 50, 40, 20], [10, 20, 30, 40, 30]])
    # np_arr = np.array([[10, 25, 30, 10], [10, 15, 30, 30]])
    mask = build_cnt_mask(np_arr)
    # mask = build_cnt_mask(np_arr, mask_size=(100, 100))

    # import matplotlib.pyplot as plt
    # plt.imshow(mask)
    # plt.show()
    # import pdb; pdb.set_trace()

    _ = np.count_nonzero(mask==255)
    # calculate the contour area
    cv_cnt = np_arr_to_cv_cnt(np_arr)
    _ = get_cnt_area(cv_cnt)
