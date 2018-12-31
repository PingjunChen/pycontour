# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(__file__))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, opj(PRJ_PATH, "pycontour"))


from coor_transform import np_arr_to_point_list
from poly_transform import construct_poly_using_np_arr
from poly_transform import construct_poly_using_point_list
from poly_transform import construct_poly_using_bbox
from poly_transform import poly_to_np_arr


def test_poly_transform():
    np_arr = np.array([[1, 2, 4, 5, 3], [1, 3, 4, 2, 0]])
    poly1 = construct_poly_using_np_arr(np_arr)
    print("Bounds of poly1 is: ", poly1.exterior.bounds)
    point_list = np_arr_to_point_list(np_arr)
    poly2 = construct_poly_using_point_list(point_list)
    print("Bounds of poly2 is: ", poly2.exterior.bounds)
    min_w, max_w = np.min(np_arr[0]), np.max(np_arr[0])
    min_h, max_h = np.min(np_arr[1]), np.max(np_arr[1])
    poly3 = construct_poly_using_bbox(min_w, min_h, max_w, max_h)
    print("Bounds of poly3 is: ", poly3.exterior.bounds)
    poly1_arr = poly_to_np_arr(poly1)
    print("Numpy coordinates of poly1 is:")
    print(poly1_arr)
    assert 1 == 1