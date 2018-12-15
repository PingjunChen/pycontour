# -*- coding: utf-8 -*-

import os, sys
from shapely.geometry import Polygon
from pycontour import construct_poly_using_np_arr

__all__ = ["contour_intersects", "construct_intersection_polygon",
        "contour_contains"]


def contour_intersects(np_arr1, np_arr2):
    """Determine two contours are intersected or not
    Parameters
    ----------    
    np_arr1 : np.array
        Contour with numpy array format
    np_arr2 : np.array
        Contour with numpy array format
    
    Returns
    -------
    inter_flag : bool
        Check if two contours are intersected or not.

    """
    # Construct polygon from numpy array
    poly1 = construct_poly_using_np_arr(np_arr1)
    poly2 = construct_poly_using_np_arr(np_arr2)
    # Get convex_hull of polygon
    poly1 = poly1.convex_hull  # Get convex hull of poly
    poly2 = poly2.convex_hull

    inter_flag = poly1.intersects(poly2)

    return inter_flag


def construct_intersection_polygon(np_arr1, np_arr2):
    """Construct polygon from the intersection part of two contours
    Parameters
    ----------    
    np_arr1 : np.array
        Contour with numpy array format
    np_arr2 : np.array
        Contour with numpy array format
    
    Returns
    -------
    inter_poly : Polygon
        The intersection polygon of two given polygons

    """
    inter_flag = contour_intersects(np_arr1, np_arr2)
    if inter_flag == False:
        return None
    # Construct polygon from numpy array
    poly1 = construct_poly_using_np_arr(np_arr1)
    poly2 = construct_poly_using_np_arr(np_arr2)
    # Get convex_hull of polygon
    poly1 = poly1.convex_hull  # Get convex hull of poly
    poly2 = poly2.convex_hull

    inter_poly = poly1.intersection(poly2)

    return inter_poly


def contour_contains(np_arr1, np_arr2):
    """Determine if contour of np_arr1 contains contour of np_arr2 or not
    Parameters
    ----------    
    np_arr1 : np.array
        Contour with numpy array format
    np_arr2 : np.array
        Contour with numpy array format
    
    Returns
    -------
    in_status : bool
        Check if polygon 1 contains polygon 2 or not
        
    """
    # Construct polygon from numpy array
    poly1 = construct_poly_using_np_arr(np_arr1)
    poly2 = construct_poly_using_np_arr(np_arr2)
    # Get convex_hull of polygon
    poly1 = poly1.convex_hull  # Get convex hull of poly
    poly2 = poly2.convex_hull

    in_status = poly1.contains(poly2)

    return in_status
