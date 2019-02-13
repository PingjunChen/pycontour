# -*- coding: utf-8 -*-

import os, sys

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)


from pycontour.poly_transform import point_list_to_poly
from pycontour.poly import get_poly_area, get_poly_bounds, get_poly_hw


def test_property():
    point_list1 = [(0.0, 1.0), (1.0, 2.0), (2.0, 1.0), (1.0, 0.0)]
    poly1 = point_list_to_poly(point_list1)
    area = get_poly_area(poly1)
    bounds = get_poly_bounds(poly1)
    poly1_h, poly1_w = get_poly_hw(poly1)
    print("Poly area is: {}".format(area))
    print("Poly bounds is: {}".format(bounds))
    print("Poly height is: {}, width is: {}".format(poly1_h, poly1_w))

    point_list2 = [(0.0, 0.0), (1.0, 2.0), (2.0, 0.0), (1.0, 0.0), (1.0, -1.0)]
    poly2 = point_list_to_poly(point_list2)
    area = get_poly_area(poly2)
    bounds = get_poly_bounds(poly2)
    poly2_h, poly2_w = get_poly_hw(poly2)
    print("Poly area is: {}".format(area))
    print("Poly bounds is: {}".format(bounds))
    print("Poly height is: {}, width is: {}".format(poly2_h, poly2_w))
