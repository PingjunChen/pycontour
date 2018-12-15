# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from shapely.geometry import Polygon, box

from pycontour import np_arr_to_point_list
from pycontour import point_list_to_np_arr

__all__ = ["construct_poly_using_np_arr", "construct_poly_using_point_list",
    "construct_poly_using_bbox", "poly_to_np_arr"]


def construct_poly_using_np_arr(np_arr):
    """Using numpy array to construct polygon
    Parameters
    ----------
    np_arr : np.array
        Numpy array of point set    

    Returns
    -------
    poly : Polygon
        Contour with shapely polygon format    

    """
    point_list = np_arr_to_point_list(np_arr)
    poly = Polygon(point_list)

    return poly


def construct_poly_using_point_list(point_list):
    """Using point list to construct polygon
    Parameters
    ----------
    point_list : list
        List of point set    

    Returns
    -------
    poly : Polygon
        Contour with shapely polygon format

    """
    poly = Polygon(point_list)

    return poly


def construct_poly_using_bbox(min_w, min_h, max_w, max_h):
    """Using bounding box to construct polygon
    Parameters
    ----------
    min_w : int
        Minimum x coordinate of polygon
    min_h : int 
        Minimum y coordinate of polygon        
    max_w : int
        Maximum x coordinate of polygon
    max_h : int 
        Maximum y coordinate of polygon  

    Returns
    -------
    poly : Polygon
        Contour with shapely polygon format  

    """
    poly = box(min_w, min_h, max_w, max_h)

    return poly


def poly_to_np_arr(poly):
    """Convert shapely Polygon to normal numpy 2d array [0]-w, [1]-h
    Parameters
    ----------
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

    return cnt_arr
