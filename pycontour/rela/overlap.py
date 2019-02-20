# -*- coding: utf-8 -*-

from ..poly_transform import np_arr_to_poly
from .intersect import construct_intersection_polygon
from ..poly import get_poly_area


def cnt_dice_ratio(cnt1, cnt2, smooth=0.01):
    """ Calculate the dice ratio between two contours.

    Parameters
    -------
    cnt1 : np.array
        contour with standard numpy 2d array format
    cnt2 : np.array
        contour with standard numpy 2d array format
    smooth: float
        value for smoothing dice ratio

    Returns
    -------
    dice_ratio : float
        dice ratio between two contours, ranging from 0.0 to 1.0

    """

    poly1 = np_arr_to_poly(cnt1)
    poly2 = np_arr_to_poly(cnt2)
    inter_poly = construct_intersection_polygon(cnt1, cnt2)

    poly1_area = get_poly_area(poly1)
    poly2_area = get_poly_area(poly2)
    inter_area = get_poly_area(inter_poly)

    dice_ratio = (2*inter_area + smooth) / (poly1_area + poly2_area + smooth)

    return dice_ratio



def cnt_jaccard_index(cnt1, cnt2, smooth=0.01):
    """ Calculate the jaccard index between two contours.

    Parameters
    -------
    cnt1 : np.array
        contour with standard numpy 2d array format
    cnt2 : np.array
        contour with standard numpy 2d array format
    smooth: float
        value for smoothing jaccard index

    Returns
    -------
    jaccard_index : float
        jaccard index between two contours, ranging from 0.0 to 1.0

    """

    poly1 = np_arr_to_poly(cnt1)
    poly2 = np_arr_to_poly(cnt2)
    inter_poly = construct_intersection_polygon(cnt1, cnt2)

    poly1_area = get_poly_area(poly1)
    poly2_area = get_poly_area(poly2)
    inter_area = get_poly_area(inter_poly)

    jaccard_index = (inter_area + smooth) / (poly1_area + poly2_area - inter_area + smooth)

    return jaccard_index
