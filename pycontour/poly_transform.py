# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from shapely.geometry import Polygon, box

from .coor_transform import swap_wh
from .coor_transform import np_arr_to_point_list
from .coor_transform import point_list_to_np_arr


__all__ = ["construct_poly_using_np_arr",
           "construct_poly_using_point_list",
           "construct_poly_using_bbox",
           "poly_to_np_arr"]


def construct_poly_using_np_arr(np_arr):
    """Using numpy 2d array ([0]-h, [1]-w) to construct polygon.

    Parameters
    ----------
    np_arr : np.array
        Numpy 2d array ([0]-h, [1]-w)

    Returns
    -------
    poly : Polygon
        Contour with shapely polygon format

    """

    np_arr = swap_wh(np_arr)
    point_list = np_arr_to_point_list(np_arr)
    poly = Polygon(point_list)

    return poly


def construct_poly_using_point_list(point_list):
    """Using point list to construct polygon.

    Parameters
    ----------
    point_list : list
        List of point set ([0]-h, [1]-w)

    Returns
    -------
    poly : Polygon
        Contour with shapely polygon format

    """

    hw_point_list = []
    for ind in np.arange(len(point_list)):
        hw_point_list.append((point_list[ind][1], point_list[ind][0]))

    poly = Polygon(point_list)

    return poly


def construct_poly_using_bbox(min_h, min_w, max_h, max_w):
    """Using bounding box to construct polygon.

    Parameters
    ----------
    min_h : int
        Minimum y coordinate of polygon
    min_w : int
        Minimum x coordinate of polygon
    max_h : int
        Maximum y coordinate of polygon
    max_w : int
        Maximum x coordinate of polygon

    Returns
    -------
    poly : Polygon
        Contour with shapely polygon format

    """

    poly = box(min_w, min_h, max_w, max_h)

    return poly


def poly_to_np_arr(poly):
    """Convert shapely Polygon to numpy 2d array ([0]-h, [1]-w).

    Parameters
    -------
    poly : Polygon
        Contour with shapely polygon format

    Returns
    -------
    cnt_arr : np.array
        Numpy array of point set

    """

    x_coors, y_coors = poly.exterior.coords.xy
    x_coors = x_coors[:-1].tolist()
    y_coors = y_coors[:-1].tolist()
    point_list = [(x, y) for x, y in zip(x_coors, y_coors)]
    cnt_arr = point_list_to_np_arr(point_list)
    cnt_arr = swap_wh(cnt_arr)

    return cnt_arr
