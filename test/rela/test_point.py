# -*- coding: utf-8 -*-

import os, sys
import numpy as np

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)
sys.path.insert(0, opj(PRJ_PATH, "pycontour"))

from pycontour.rela import point_in_contour


def test_point_in_contour():
    np_arr = np.array([[1., 2., 4., 5., 3.], [1., 3., 4., 2., 0.]])
    flag1 = point_in_contour(np_arr, 3, 2)
    if flag1 == False:
        raise AssertionError("Test point inside contour")
    flag2 = point_in_contour(np_arr, 1.01, 1)
    if flag2 == False:
        raise AssertionError("Test point on the border of contour")
    flag3 = point_in_contour(np_arr, 5, 1)
    if flag3 == True:
        assert AssertionError("Test point outside contour")
