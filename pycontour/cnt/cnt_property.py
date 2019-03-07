# -*- coding: utf-8 -*-

import numpy as np
import cv2


__all__ = ["get_cnt_area",
           "get_cnt_aspect_ratio",
           "get_cnt_solidity"]


def get_cnt_area(cnt1):
    """ Calcualte the number of pixels contour covered.

    Parameters
    -------
    cnt1 : np.array
        contour with opencv format

    Returns
    -------
    area_val : int
        number of pixels inside the contour

    """

    area_val = cv2.contourArea(cnt1.astype(np.float32))

    return area_val


def get_cnt_aspect_ratio(cnt1):
    """ Calcualte the aspect ratio of contour.

    Parameters
    -------
    cnt1 : np.array
        contour with opencv format

    Returns
    -------
    aspect_ratio : float
        contour aspect ratio

    """

    _, _, w, h = cv2.boundingRect(cnt1.astype(np.float32))
    aspect_ratio = w * 1.0 / h

    return aspect_ratio


def get_cnt_solidity(cnt1):
    """ Calcualte the solidity of contour.

    Parameters
    -------
    cnt : np.array
        contour with opencv format

    Returns
    -------
    solidity_val : float
        solidity value of contour

    """

    cnt1 = cnt1.astype(np.float32)
    area = cv2.contourArea(cnt1)
    hull = cv2.convexHull(cnt1)
    hull_area = cv2.contourArea(hull)

    solidity_val = area * 1.0 / hull_area

    return solidity_val
