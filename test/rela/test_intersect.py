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


from pycontour.coor_transform import point_list_to_np_arr
from pycontour.rela import contour_intersects, contour_contains
from pycontour.rela import construct_intersection_polygon


def test_contour_intersects():
    cnt1 = np.array([[0, 0, 2, 2], [0, 2, 2, 0]])
    cnt2 = np.array([[-1, -1, 1, 1], [1, 3, 3, 1]])

    intersect_flag = contour_intersects(cnt1, cnt2)
    assert intersect_flag == True, "Intersection judgement error"


def test_construct_intersection_polygon():
    point_list1 = [(1.0, 4.0), (3.0, 4.0), (3.0, 1.0), (1.0, 1.0)]
    point_list2 = [(2.0, 3.0), (4.0, 3.0), (4.0, 0.0), (2.0, 0.0)]
    point_list3 = [(3.0, 1.0), (5.0, 1.0), (5.0, -2.0), (3.0, -2.0)]

    # Convert point list to numpy array
    np_arr1 = point_list_to_np_arr(point_list1)
    np_arr2 = point_list_to_np_arr(point_list2)
    np_arr3 = point_list_to_np_arr(point_list3)
    intersection12 = construct_intersection_polygon(np_arr1, np_arr2)
    print("Area of intersection 1 and 2 is: {}".format(intersection12.area))
    intersection13 = construct_intersection_polygon(np_arr1, np_arr3)
    print("Area of intersection 1 and 3 is: {}".format(intersection13.area))
    intersection23 = construct_intersection_polygon(np_arr2, np_arr3)
    print("Area of intersection 2 and 3 is: {}".format(intersection23.area))


def test_contour_contains():
    cnt1 = np.array([[0, 0, 2, 2], [0, 2, 2, 0]])
    cnt2 = np.array([[-1, -1, 1, 1], [1, 3, 3, 1]])
    cnt3 = np.array([[0.1, 0.1, 1.9, 1.9], [0.1, 1.9, 1.9, 0.1]])

    contain_flag = contour_contains(cnt1, cnt2)
    assert contain_flag == False, "Containing judgement error"

    contain_flag = contour_contains(cnt1, cnt3)
    assert contain_flag == True, "Containing judgement error"
