# -*- coding: utf-8 -*-

import numpy as np
import cv2

from ..cv2_transform import np_arr_to_cv_cnt
from ..poly_transform import np_arr_to_poly
from ..poly import get_poly_bounds
from ..transform import shift_cnt


__all__ = ["build_cnt_mask",
           "cnt_mask_img",
           "cnt_mask_sub_img"]


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
        if not (mask_size >= cnt_height and mask_size >= cnt_width):
            raise AssertionError("given size too small")
        mask_height = mask_size
        mask_width = mask_size
    elif isinstance(mask_size, list) or isinstance(mask_size, tuple):
        if len(mask_size) == 1:
            if not (mask_size[0] >= cnt_height and mask_size[0] >= cnt_width):
                raise AssertionError("given size too small")
            mask_height = mask_size[0]
            mask_width = mask_size[0]
        elif len(mask_size) == 2:
            if not (mask_size[0] >= cnt_height and mask_size[1] >= cnt_width):
                raise AssertionError("given size too small")
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

    return mask


def cnt_mask_img(img, np_arr):
    """ Mask image by contour

    Parameters
    -------
    img : np.array
        image represented by numpy array
    np_arr: np.array
        contour with standard numpy 2d array format

    Returns
    -------
    mask_img: np.array
        masked image with only contour covered region

    """

    mask = np.zeros_like(img, dtype=np.uint8)
    mask = np.ascontiguousarray(mask)

    cv_cnt = np_arr_to_cv_cnt(np_arr)
    if len(img.shape) == 2:
        cv2.drawContours(mask, [cv_cnt], 0, 1, -1)
    elif len(img.shape) == 3 and img.shape[2] == 3:
        cv2.drawContours(mask, [cv_cnt], 0, [1, 1, 1], -1)
    else:
        raise NotImplementedError("Image shape not supported")

    mask_img = img * mask

    return mask_img


def cnt_mask_sub_img(img, np_arr):
    """ Mask sub image using contour

    Parameters
    -------
    img : np.array
        image represented by numpy array
    np_arr: np.array
        contour with standard numpy 2d array format

    Returns
    -------
    mask_sub_img: np.array
        masked contour circumscribed sub-image

    """

    min_h, min_w = np.min(np_arr[0]), np.min(np_arr[1])
    max_h, max_w = np.max(np_arr[0]), np.max(np_arr[1])
    sub_img = img[min_h:max_h+1, min_w:max_w+1]

    shift_arr = np_arr.copy()
    shift_arr[0] -= min_h
    shift_arr[1] -= min_w
    shift_cnt = np_arr_to_cv_cnt(shift_arr)

    mask = np.zeros_like(sub_img, dtype=np.uint8)
    mask = np.ascontiguousarray(mask)
    if len(sub_img.shape) == 2:
        cv2.drawContours(mask, [shift_cnt], 0, 1, -1)
    elif len(sub_img.shape) == 3 and sub_img.shape[2] == 3:
        cv2.drawContours(mask, [shift_cnt], 0, [1, 1, 1], -1)
    else:
        raise NotImplementedError("Image shape not supported")

    mask_sub_img = sub_img * mask

    return mask_sub_img
