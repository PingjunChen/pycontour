# -*- coding: utf-8 -*-

import numpy as np
import cv2
from skimage import filters
from skimage import img_as_ubyte

from ..cv2_transform import cv_cnt_to_np_arr
from ..img import mask

__all__ = ["smooth_cnt", ]


def smooth_cnt(np_arr, sigma=5):
    """ Smooth the contour.

    Parameters
    -------
    np_arr : np.array
        contour with standard numpy 2d array format
    sigma: int
        gaussian smoothing kernel

    Returns
    -------
    smooth_arr: np.array
        smoothed contour

    """

    min_h, min_w = np.min(np_arr[0]), np.min(np_arr[1])
    np_arr[0] -= min_h
    np_arr[1] -= min_w

    cnt_mask = mask.build_cnt_mask(np_arr)
    smooth_mask = filters.gaussian(cnt_mask, sigma=sigma)
    bin_mask = smooth_mask > 0.99

    _, cnts, _ = cv2.findContours(img_as_ubyte(bin_mask),
                                  mode=cv2.RETR_EXTERNAL,
                                  method=cv2.CHAIN_APPROX_NONE)
    if len(cnts) != 1:
        raise AssertionError("Contour number error...")

    smooth_cnt = cnts[0]
    smooth_arr = cv_cnt_to_np_arr(smooth_cnt)
    smooth_arr[0] += min_h
    smooth_arr[1] += min_w

    return smooth_arr
