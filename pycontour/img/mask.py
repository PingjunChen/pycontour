# -*- coding: utf-8 -*-

import numpy as np
import cv2

from ..cv2_transform import np_arr_to_cv_cnt

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
