# -*- coding: utf-8 -*-

import numpy as np

from .coor_transform import swap_wh

__all__ = ["cv_cnt_to_np_arr",
           "np_arr_to_cv_cnt"]


def cv_cnt_to_np_arr(cv_cnt):
    """ Convert cv2 contour to numpy 2d array ([0]-h, [1]-w).

    Parameters
    -------
    cv_cnt : np.array
        contour with opencv format

    Returns
    -------
    cnt_arr : np.array
        contour with standard numpy 2d array format

    """

    cnt_arr = cv_cnt.squeeze().transpose()
    cnt_arr = swap_wh(cnt_arr)

    return cnt_arr


def np_arr_to_cv_cnt(np_arr):
    """ Convert numpy 2d array ([0]-h, [1]-w) to cv2 contour.

    Parameters
    -------
    cnt_arr : np.array
        contour with standard numpy 2d array format

    Returns
    -------
    cv_cnt : np.array
        contour with opencv format

    """

    np_arr = swap_wh(np_arr)
    arr_t = np_arr.transpose()
    cv_cnt = np.expand_dims(arr_t, axis=1)

    return cv_cnt
