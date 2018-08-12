# -*- coding: utf-8 -*-

import os, sys
import numpy as np

__all__ = ["cv_cnt_to_np_arr", "np_arr_to_cv_cnt"]

def cv_cnt_to_np_arr(cv_cnt):
    """Convert cv2 contour to normal numpy 2d array [0]-w, [1]-h
    """
    cnt_arr = cv_cnt.squeeze().transpose()

    return cnt_arr

def np_arr_to_cv_cnt(np_arr):
    """Convert 2d coordinates to cv2 contour
    """
    arr_t = np_arr.transpose()
    cv_cnt = np.expand_dims(arr_t, axis=1)

    return cv_cnt
