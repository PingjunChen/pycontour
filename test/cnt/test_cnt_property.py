# -*- coding: utf-8 -*-

import os, sys

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.coor_transform import point_list_to_np_arr
from pycontour.cv2_transform import np_arr_to_cv_cnt

from pycontour.cnt import get_cnt_area
from pycontour.cnt import get_cnt_aspect_ratio
from pycontour.cnt import get_cnt_solidity


def test_property():
    point_list1 = [(0.0, 1.0), (1.0, 2.0), (2.0, 1.0), (1.0, 0.0)]
    np_arr1 = point_list_to_np_arr(point_list1)
    cv_cnt1 = np_arr_to_cv_cnt(np_arr1)
    cnt_area = get_cnt_area(cv_cnt1)
    cnt_aspect_ratio = get_cnt_aspect_ratio(cv_cnt1)
    cnt_solidty = get_cnt_solidity(cv_cnt1)
    print("Contour area is {}".format(cnt_area))
    print("Contour aspect ratio is {}".format(cnt_aspect_ratio))
    print("Contour solidity is {}".format(cnt_solidty))

    point_list2 = [(0.0, 0.0), (1.0, 2.0), (2.0, 0.0), (1.0, 0.0), (1.0, -1.0)]
    np_arr2 = point_list_to_np_arr(point_list2)
    cv_cnt2 = np_arr_to_cv_cnt(np_arr2)
    cnt_area = get_cnt_area(cv_cnt2)
    cnt_aspect_ratio = get_cnt_aspect_ratio(cv_cnt2)
    cnt_solidty = get_cnt_solidity(cv_cnt2)
    print("Contour area is {}".format(cnt_area))
    print("Contour aspect ratio is {}".format(cnt_aspect_ratio))
    print("Contour solidity is {}".format(cnt_solidty))
