# -*- coding: utf-8 -*-

import sys
import numpy as np
from os.path import dirname as opd
from os.path import abspath as opa
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)


from pycontour.poly_transform import np_arr_to_poly
from pycontour import poly


def test_poly_to_valid():
    cnt_arr1 = np.array([(0, 2, 2, 0), (0, 0, 2, 2)])
    poly1 = np_arr_to_poly(cnt_arr1)
    valid_poly1 = poly.poly_to_valid(poly1)

    if poly1 is not valid_poly1:
        raise AssertionError

    cnt_arr2 = np.array([(1, 3, 1, 3), (1, 3, 2, 2)])
    poly2 = np_arr_to_poly(cnt_arr2)
    valid_poly2 = poly.poly_to_valid(poly2)

    if poly2 is valid_poly2:
        raise AssertionError
