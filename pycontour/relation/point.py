# -*- coding: utf-8 -*-

import os, sys
from shapely.geometry import Point

from ..poly_transform import construct_poly_using_np_arr


__all__ = ['point_in_contour', ]


def point_in_contour(np_arr, px, py):
    """ Determine point inside contour or not.

    Parameters
    -------
    np_arr : np.array
        numpy array with height and width
    px: int
        x coordinate of point
    py: int
        y coordinate of point

    Returns
    -------
    in_flag : bool
        flag indicates point within contour or not

    """

    point = Point(point_x, point_y)
    poly = construct_poly_using_np_arr(np_arr)

    in_flag = point.within(poly)

    return in_flag
