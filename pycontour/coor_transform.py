# -*- coding: utf-8 -*-

import numpy as np

__all__ = ["swap_wh",
           "np_arr_to_point_list",
           "point_list_to_np_arr"]

def swap_wh(np_arr):
    """ Swap row of width and row of height.

    Parameters
    -------
    np_arr : np.array
        Numpy array with height and width

    Returns
    -------
    new_arr : np.array
        Numpy array with width and height position changed

    """

    if not (len(np_arr.shape) == 2 and np_arr.shape[0] == 2):
        raise AssertionError("Wrong contour arr")

    new_arr = np.zeros_like(np_arr)
    new_arr[0] = np_arr[1]
    new_arr[1] = np_arr[0]

    return new_arr


def np_arr_to_point_list(np_arr):
    """ Convert 2d numpy array to list of points.

    Parameters
    -------
    np_arr : np.array
        Numpy array of point set

    Returns
    -------
    point_list : list
        List of points

    """

    point_list = []
    num_point = np_arr.shape[1]
    for ind in np.arange(num_point):
        point_list.append((np_arr[0][ind], np_arr[1][ind]))

    return point_list


def point_list_to_np_arr(point_list):
    """ Convert list of point coordinates to numpy 2d array.

    Parameters
    -------
    point_list : list
        list of point set ([0]-h, [1]-w)

    Returns
    -------
    np_arr : np.array
        contour with standard numpy 2d array format

    """

    num_point = len(point_list)
    np_arr = np.zeros((2, num_point))
    for ind in np.arange(num_point):
        np_arr[0][ind] = point_list[ind][0]
        np_arr[1][ind] = point_list[ind][1]

    return np_arr
