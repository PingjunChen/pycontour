# -*- coding: utf-8 -*-

import numpy as np
import cv2

from ..cv2_transform import np_arr_to_cv_cnt


__all__ = ["cnt_mask_img",
           "cnt_mask_sub_img"]


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
    mask = np.zeros_like(sub_img, dtype=np.uint8)

    shift_arr = np_arr.copy()
    shift_arr[0] -= min_h
    shift_arr[1] -= min_w

    shift_cnt = np_arr_to_cv_cnt(shift_arr)
    if len(sub_img.shape) == 2:
        cv2.drawContours(mask, [shift_cnt], 0, 1, -1)
    elif len(sub_img.shape) == 3 and sub_img.shape[2] == 3:
        cv2.drawContours(mask, [shift_cnt], 0, [1, 1, 1], -1)
    else:
        raise NotImplementedError("Image shape not supported")

    mask_sub_img = sub_img * mask

    return mask_sub_img
