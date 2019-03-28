# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from skimage import io

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)
sys.path.insert(0, opj(PRJ_PATH, "pycontour"))

from pycontour.cv2_transform import np_arr_to_cv_cnt
from pycontour.cnt import get_cnt_area

from pycontour.img import build_cnt_mask
from pycontour.img import cnt_mask_img
from pycontour.img import cnt_mask_sub_img

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


def test_cnt_mask_img():
    img_path = os.path.join(TEST_PATH, "data/Imgs/20181218042607.jpg")
    img = io.imread(img_path)
    np_arr = np.array([[300, 600, 700, 500, 400], [300, 400, 500, 600, 500]])
    masked_img = cnt_mask_img(img, np_arr)

    import matplotlib.pylab as plt
    plt.imshow(masked_img)
    # plt.show()

def test_cnt_mask_sub_img():
    img_path = os.path.join(TEST_PATH, "data/Imgs/20181218042607.jpg")
    img = io.imread(img_path)
    np_arr = np.array([[300, 600, 700, 500, 400], [300, 400, 500, 600, 500]])
    masked_subimg = cnt_mask_sub_img(img, np_arr)

    import matplotlib.pylab as plt
    plt.imshow(masked_subimg)
    plt.show()
