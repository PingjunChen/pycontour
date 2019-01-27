# -*- coding: utf-8 -*-

import os, sys
from shapely.geometry import Point

from ..poly_transform import np_arr_to_poly


__all__ = ['point_in_contour', ]


def point_in_contour(np_arr, py, px):
    """ Determine point inside contour or not.

    Parameters
    -------
    np_arr : np.array
        numpy array with height and width
    py: int
        y coordinate of point
    px: int
        x coordinate of point

    Returns
    -------
    in_flag : bool
        flag indicates point within contour or not

    """

    point = Point(px, py)
    poly = np_arr_to_poly(np_arr)

    in_flag = point.within(poly)

    return in_flag
