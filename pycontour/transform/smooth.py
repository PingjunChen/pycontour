# -*- coding: utf-8 -*-

import numpy as np

def smooth_cnt(np_arr, smooth_k=3):
    """ Smooth the contour.

    Parameters
    -------
    np_arr : np.array
        contour with standard numpy 2d array format
    smooth_k: int
        smoothing parameter

    Returns
    -------
    smooth_arr: np.array
        smoothed contour

    """

    
