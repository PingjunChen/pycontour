# -*- coding: utf-8 -*-

import os, sys
from shapely import Polygon
from .construct_polygon import construct_polygon_using_np_arr

def contour_intersects(np_arr1, np_arr2):
    """Determine two contours are intersected or not
    """
    # Construct polygon from numpy array
    poly1 = construct_polygon_using_np_arr(np_arr1)
    poly2 = construct_polygon_using_np_arr(np_arr2)
    # Get convex_hull of polygon
    poly1 = poly1.convex_hull  # Get convex hull of poly
    poly2 = poly2.convex_hull

    inter_flag = poly1.intersects(poly1, poly2)

    return inter_flag


def construct_intersection_polygon(np_arr1, np_arr2):
    """Construct polygon from the intersection part of two contours
    """
    inter_flag = contour_intersects(np_arr1, np_arr2)
    if inter_flag == False:
        return None
    # Construct polygon from numpy array
    poly1 = construct_polygon_using_np_arr(np_arr1)
    poly2 = construct_polygon_using_np_arr(np_arr2)
    # Get convex_hull of polygon
    poly1 = poly1.convex_hull  # Get convex hull of poly
    poly2 = poly2.convex_hull

    inter_poly = poly1.intersection(poly1, poly2)

    return inter_poly    
