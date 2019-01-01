# -*- coding: utf-8 -*-

import os, sys

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.poly_transform import construct_poly_using_point_list
from pycontour.polygon import get_poly_area, get_poly_bounds, get_poly_wh

def test_property():
    point_list1 = [(0, 1), (1, 2), (2, 1), (1, 0)]
    poly1 = construct_poly_using_point_list(point_list1)
    area = get_poly_area(poly1)
    bounds = get_poly_bounds(poly1)
    poly_w, poly_h = get_poly_wh(poly1)
    print("Poly area is: {}".format(area))
    print("Poly bounds is: {}".format(bounds))
    print("Poly width is: {}, height is: {}".format(poly_w, poly_h))


    point_list2 = [(0, 0), (1, 2), (2, 0), (1, 0), (1, -1)]
    poly2 = construct_poly_using_point_list(point_list2)
    area = get_poly_area(poly2)
    bounds = get_poly_bounds(poly2)
    poly_w, poly_h = get_poly_wh(poly2)
    print("Poly area is: {}".format(area))
    print("Poly bounds is: {}".format(bounds))
    print("Poly width is: {}, height is: {}".format(poly_w, poly_h))
