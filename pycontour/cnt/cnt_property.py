# -*- coding: utf-8 -*-

import os, sys
import cv2
import numpy as np

__all__ = ["get_cnt_area", "get_cnt_aspect_ratio", "get_cnt_solidity"]

def get_cnt_area(cnt):
    area_val = cv2.contourArea(cnt.astype(np.float32))

    return area_val


def get_cnt_aspect_ratio(cnt):
    x, y, w, h = cv2.boundingRect(cnt.astype(np.float32))
    aspect_ratio = w * 1.0 / h

    return aspect_ratio


def get_cnt_solidity(cnt):
    cnt = cnt.astype(np.float32)
    area = cv2.contourArea(cnt)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)

    solidity_val = area * 1.0 / hull_area

    return solidity_val
