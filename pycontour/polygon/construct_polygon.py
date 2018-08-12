# -*- coding: utf-8 -*-

import os, sys

from shapely.geometry import Polygon
from shapely.geometry import box

from pycontour import np_arr_to_point_list

def construct_polygon_using_np_arr(np_arr):
    """Using numpy array to construct polygon
    """
    point_list = np_arr_to_point_list(np_arr)
    poly = Polygon(point_list)

    return poly

def construct_polygon_using_point_list(point_list):
    """Using point list to construct polygon
    """
    poly = Polygon(point_list)

    return poly

def construct_polygon_using_bbox(min_w, min_h, max_w, max_h):
    """Using bounding box to construct polygon
    """
    poly = box(min_w, min_h, max_w, max_h)

    return poly
