# -*- coding: utf-8 -*-

import os, sys
from shapely.geometry import Point

from ..poly_transform import construct_poly_using_np_arr


__all__ = ['point_in_contour', ]


def point_in_contour(np_cnt, point_h, point_w):
    """ Determine point inside contour or not.

    """

    point = Point(point_w, point_h)
    poly = construct_poly_using_np_arr(np_cnt)

    # if cur_point.within(poly):
    # if poly.contains(cur_point):
    in_flag = point.within(poly)

    return in_flag
