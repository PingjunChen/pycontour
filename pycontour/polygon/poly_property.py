# -*- coding: utf-8 -*-

import os, sys


__all__ = ["get_poly_area", "get_poly_bounds", "get_poly_wh"]

def get_poly_area(poly):
    """Calcualte the number of pixels Polygon covered
    Parameters
    ----------
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
    """Find the bounds of the Polygon 
    Parameters
    ----------
    poly : Polygon
        Contour with shapely polygon format

    Returns
    -------
    min_x : int
        Minimum x coordinate of polygon
    min_y : int
        Minimum y coordinate of polygon    
    max_x : int
        Maximum x coordinate of polygon    
    max_y : int
        Maximum y coordinate of polygon        

    """   

    min_x, min_y, max_x, max_y = poly.bounds

    return min_x, min_y, max_x, max_y


def get_poly_wh(poly):
    """Find width and height of the Polygon 
    Parameters
    ----------
    poly : Polygon
        Contour with shapely polygon format

    Returns
    -------
    poly_w : int
        Width of the polygon
    poly_h : int
        Height of the polygon   

    """    
    min_x, min_y, max_x, max_y = get_poly_bounds(poly)
    poly_w, poly_h = max_x - min_x, max_y - min_y

    return poly_w, poly_h
