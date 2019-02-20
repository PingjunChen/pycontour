# -*- coding: utf-8 -*-

import numpy as np
from shapely.geometry import Polygon, box

from .coor_transform import swap_wh
from .coor_transform import np_arr_to_point_list
from .coor_transform import point_list_to_np_arr


__all__ = ["np_arr_to_poly",
           "point_list_to_poly",
           "bbox_to_poly",
           "poly_to_np_arr"]


def np_arr_to_poly(np_arr):
    """ Using numpy 2d array ([0]-h, [1]-w) to construct polygon.

    Parameters
    -------
    np_arr : np.array
        contour with standard numpy 2d array format

    Returns
    -------
    poly : Polygon
        contour with shapely polygon format

    """

    np_arr = swap_wh(np_arr)
    point_list = np_arr_to_point_list(np_arr)
    poly = Polygon(point_list)

    return poly


def point_list_to_poly(point_list):
    """ Using point list to construct polygon.

    Parameters
    -------
    point_list : list
        list of point set ([0]-h, [1]-w)

    Returns
    -------
    poly : Polygon
        contour with shapely polygon format

    """

    wh_point_list = []
    for ind in np.arange(len(point_list)):
        wh_point_list.append((point_list[ind][1], point_list[ind][0]))

    poly = Polygon(wh_point_list)

    return poly


def bbox_to_poly(min_h, min_w, max_h, max_w):
    """ Using bounding box to construct polygon.

    Parameters
    -------
    min_h : int
        minimum y coordinate of polygon
    min_w : int
        minimum x coordinate of polygon
    max_h : int
        maximum y coordinate of polygon
    max_w : int
        maximum x coordinate of polygon

    Returns
    -------
    poly : Polygon
        contour with shapely polygon format

    """

    poly = box(min_w, min_h, max_w, max_h)

    return poly


def poly_to_np_arr(poly):
    """ Convert shapely Polygon to numpy 2d array ([0]-h, [1]-w).

    Parameters
    -------
    poly : Polygon
        contour with shapely polygon format

    Returns
    -------
    cnt_arr : np.array
        contour with standard numpy 2d array format

    """

    x_coors, y_coors = poly.exterior.coords.xy
    x_coors = x_coors[:-1].tolist()
    y_coors = y_coors[:-1].tolist()
    point_list = [(y, x) for x, y in zip(x_coors, y_coors)]
    cnt_arr = point_list_to_np_arr(point_list)

    return cnt_arr
