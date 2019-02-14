# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import cv2

from ..poly_transform import np_arr_to_poly
from ..cv2_transform import np_arr_to_cv_cnt
from ..poly import get_poly_bounds
from ..rela import point_in_contour
from ..transform import shift_cnt


def build_cnt_mask(np_arr, mask_size=None):
    """ Build an exterior rectangle mask based on contour

    Parameters
    -------
    np_arr : np.array
        contour with standard numpy 2d array format
    mask_size: None, scalar, list, or tuple
        desired mask size for contour

    Returns
    -------
    mask: np.array
        contour exterior rectangle mask

    """

    poly = np_arr_to_poly(np_arr)
    min_h, min_w, max_h, max_w = get_poly_bounds(poly)
    min_h, min_w = int(min_h), int(min_w)
    max_h, max_w = int(max_h), int(max_w)


    cnt_height = max_h - min_h + 1
    cnt_width = max_w - min_w + 1
    if mask_size == None:
        mask_height = cnt_height
        mask_width = cnt_width
    elif np.isscalar(mask_size):
        assert mask_size >= cnt_height and mask_size >= cnt_width, "given size too small"
        mask_height = mask_size
        mask_width = mask_size
    elif type(mask_size) is list or type(mask_size) is tuple:
        if len(mask_size) == 1:
            assert mask_size[0] >= cnt_height and mask_size[0] >= cnt_width, "given size too small"
            mask_height = mask_size[0]
            mask_width = mask_size[0]
        elif len(mask_size) == 2:
            assert mask_size[0] >= cnt_height and mask_size[1] >= cnt_width, "given size too small"
            mask_height = mask_size[0]
            mask_width = mask_size[1]
        else:
            raise Exception("Not proper size")
    else:
        raise Exception("Not proper size")

    mask = np.zeros((mask_height, mask_width), np.uint8)
    mask_start_h = int(np.floor((mask_height - cnt_height) / 2.0))
    mask_start_w = int(np.floor((mask_width - cnt_width) / 2.0))

    # Fill using cv2
    shift_h = mask_start_h - min_h
    shift_w = mask_start_w - min_w
    shift_arr = shift_cnt(np_arr, shift_h, shift_w)
    cv_cnt = np_arr_to_cv_cnt(shift_arr)
    cv2.drawContours(mask, [cv_cnt], 0, 255, -1)

    # # Fill using point-wise operation
    # for px in np.arange(min_w, max_w+1):
    #     for py in np.arange(min_h, max_h+1):
    #         if point_in_contour(np_arr, py, px):
    #             mask[mask_start_h+py-min_h, mask_start_w+px-min_w] = 255

    return mask
