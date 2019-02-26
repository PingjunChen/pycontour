# -*- coding: utf-8 -*-

import sys
import numpy as np
from os.path import dirname as opd
from os.path import abspath as opa
TEST_PATH = opa(opd(__file__))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.coor_transform import np_arr_to_point_list
from pycontour.poly_transform import np_arr_to_poly
from pycontour.poly_transform import point_list_to_poly
from pycontour.poly_transform import bbox_to_poly
from pycontour.poly_transform import poly_to_np_arr


def test_poly_transform():
    np_arr = np.array([[1., 2., 4., 5., 3.], [1., 3., 4., 2., 0.]])
    poly1 = np_arr_to_poly(np_arr)
    print("Bounds of poly1 is: ", poly1.exterior.bounds)
    point_list = np_arr_to_point_list(np_arr)
    poly2 = point_list_to_poly(point_list)
    print("Bounds of poly2 is: ", poly2.exterior.bounds)
    if poly1 != poly2:
        raise AssertionError("Conversion error")
    min_h, max_h = np.min(np_arr[0]), np.max(np_arr[0])
    min_w, max_w = np.min(np_arr[1]), np.max(np_arr[1])
    poly3 = bbox_to_poly(min_h, min_w, max_h, max_w)
    print("Bounds of poly3 is: ", poly3.exterior.bounds)
    # poly3.exterior.coords.xy
    poly1_arr = poly_to_np_arr(poly1)
    print("Numpy coordinates of poly1 is:")
    if not np.array_equal(np_arr, poly1_arr):
        raise AssertionError("Conversion error")
