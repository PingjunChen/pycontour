# -*- coding: utf-8 -*-

import os, sys

from pycontour import point_list_to_np_arr
from pycontour import np_arr_to_cv_cnt

from pycontour.cnt import get_cnt_area
from pycontour.cnt import get_cnt_aspect_ratio
from pycontour.cnt import get_cnt_solidity

def test_property(cnt):
    cnt_area = get_cnt_area(cnt)
    cnt_aspect_ratio = get_cnt_aspect_ratio(cnt)
    cnt_solidty = get_cnt_solidity(cnt)
    print("Contour area is {}".format(cnt_area))
    print("Contour aspect ratio is {}".format(cnt_aspect_ratio))
    print("Contour solidity is {}".format(cnt_solidty))

if __name__ == "__main__":
    point_list1 = [(0, 1), (1, 2), (2, 1), (1, 0)]
    np_arr1 = point_list_to_np_arr(point_list1)
    cnt1 = np_arr_to_cv_cnt(np_arr1)
    test_property(cnt1)

    point_list2 = [(0, 0), (1, 2), (2, 0), (1, 0), (1, -1)]
    np_arr2 = point_list_to_np_arr(point_list2)
    cnt2 = np_arr_to_cv_cnt(np_arr2)
    test_property(cnt2)
