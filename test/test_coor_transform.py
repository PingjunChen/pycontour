# -*- coding: utf-8 -*-

import sys
from os.path import dirname as opd
from os.path import abspath as opa
TEST_PATH = opa(opd(__file__))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.coor_transform import point_list_to_np_arr
from pycontour.coor_transform import np_arr_to_point_list


def test_coor_transform():
    point_list = [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (1.0, 2.0)]
    np_arr = point_list_to_np_arr(point_list)
    new_points = np_arr_to_point_list(np_arr)
    if point_list != new_points:
        raise AssertionError("Conversion error")
