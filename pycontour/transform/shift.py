# -*- coding: utf-8 -*-

import numpy as np

__all__ = ["shift_cnt", ]

def shift_cnt(np_arr, shift_h=None, shift_w=None):
    """ Shift the position of contour.

    Parameters
    -------
    np_arr : np.array
        contour with standard numpy 2d array format
    shift_h : int or float
        shift distance in vertical direction
    shift_w : int or float
        shift distance in horizontal direction

    Returns
    -------
    shift_arr: np.array
        shifted contour

    """

    # construct new shift_arr from original array
    shift_arr = np.array(np_arr)
    # shift in vertical direction
    if shift_h != None:
        shift_arr[0] += shift_h

    # shift in horizental direction
    if shift_w != None:
        shift_arr[1] += shift_w

    return shift_arr
