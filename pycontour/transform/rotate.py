# -*- coding: utf-8 -*-

import math
import numpy as np

__all__ = ["rotate_cnt", ]

def rotate_cnt(np_arr, angle):
    """ Rotate contour clockwise by radian angle around contour center

    Parameters
    -------
    np_arr : np.array
        contour with standard numpy 2d array format
    angle : int or float
        angle in radian, range from 0 to 360

    Returns
    -------
    rot_cnt: np.array
        rotated contour

    """

    rotate_cnt = np.zeros_like(np_arr)
    cen_h = np.mean(np_arr[0, :])
    cen_w = np.mean(np_arr[1, :])

    rad = math.radians(angle)
    for ip in np.arange(np_arr.shape[1]):
        cnt_h, cnt_w = np_arr[0, ip], np_arr[1, ip]
        new_h = cen_h + math.sin(rad) * (cnt_w - cen_w) + math.cos(rad) * (cnt_h - cen_h)
        new_w = cen_w + math.cos(rad) * (cnt_w - cen_w) - math.sin(rad) * (cnt_h - cen_h)

        rotate_cnt[0, ip] = int(new_h)
        rotate_cnt[1, ip] = int(new_w)

    return rotate_cnt
