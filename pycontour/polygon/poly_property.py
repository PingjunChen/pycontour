# -*- coding: utf-8 -*-

import os, sys


__all__ = ["get_poly_area",
           "get_poly_bounds",
           "get_poly_hw"]


def get_poly_area(poly):
    """Calcualte the number of pixels the polygon covered.

    Parameters
    -------
    poly : Polygon
        Contour with shapely polygon format

    Returns
    -------
    area_val : int
        Number of pixels inside the contour

    """

    area_val = poly.area

    return area_val


def get_poly_bounds(poly):
    """Find the bounds of the Polygon.

    Parameters
    -------
    poly : Polygon
        Contour with shapely polygon format

    Returns
    -------
    min_h : int
        Minimum y coordinate of polygon
    min_w : int
        Minimum x coordinate of polygon
    max_h : int
        Maximum y coordinate of polygon
    max_w : int
        Maximum x coordinate of polygon

    """

    min_x, min_y, max_x, max_y = poly.bounds
    min_h, min_w = min_y, min_x
    max_h, max_w = max_y, max_x

    return min_h, min_w, max_h, max_w


def get_poly_hw(poly):
    """Find height and width of the polygon.
    Parameters
    ----------
    poly : Polygon
        Contour with shapely polygon format

    Returns
    -------
    poly_h : int
        Height of the polygon
    poly_w : int
        Width of the polygon

    """

    min_h, min_w, max_h, max_w = get_poly_bounds(poly)

    poly_h = max_h - min_h + 1
    poly_w = max_w - min_w + 1

    return poly_w, poly_h
