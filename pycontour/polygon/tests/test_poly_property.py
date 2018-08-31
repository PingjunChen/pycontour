# -*- coding: utf-8 -*-

import os, sys

from pycontour import construct_poly_using_point_list
from pycontour.polygon import get_poly_area, get_poly_bounds, get_poly_wh

def test_property(poly):
    area = get_poly_area(poly)
    bounds = get_poly_bounds(poly)
    poly_w, poly_h = get_poly_wh(poly)
    print("Poly area is: {}".format(area))
    print("Poly bounds is: {}".format(bounds))
    print("Poly width is: {}, height is: {}".format(poly_w, poly_h))

if __name__ == "__main__":
    point_list1 = [(0, 1), (1, 2), (2, 1), (1, 0)]
    poly1 = construct_poly_using_point_list(point_list1)
    test_property(poly1)

    point_list2 = [(0, 0), (1, 2), (2, 0), (1, 0), (1, -1)]
    poly2 = construct_poly_using_point_list(point_list2)
    test_property(poly2)
