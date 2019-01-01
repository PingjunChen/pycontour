# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(__file__))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.coor_transform import point_list_to_np_arr
from pycontour.coor_transform import swap_wh
from pycontour.coor_transform import np_arr_to_point_list


def test_coor_transform():
    point_list = [(0, 0), (2, 0), (2, 2), (1, 2)]
    np_arr = point_list_to_np_arr(point_list)
    swap_arr = swap_wh(np_arr)
    swap_points = np_arr_to_point_list(swap_arr)
