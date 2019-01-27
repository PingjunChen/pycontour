# -*- coding: utf-8 -*-

import os, sys
import numpy as np

from ..polygon import get_poly_bounds
from ..relation import point_in_contour


def build_cnt_mask(np_arr):
    """ Build an exterior rectangle mask based on contour

    Parameters
    -------
    np_arr : np.array
        Numpy array with height and width

    Returns
    -------
    mask: np.array
        contour exterior rectangle mask

    """

    min_h, min_w, max_h, max_w = get_poly_bounds(poly)

    mask = np.zeros((max_h-min_h+1, max_w-min_w+1), np.uint8)
    for px in np.arange(min_w, max_w+1):
        for py in np.arange(min_h, max_h+1):
            if point_in_contour(np_arr, px, py):
                mask[py-min_h, px-min_w] = 255

    return mask
