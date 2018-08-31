# -*- coding: utf-8 -*-

import os, sys


__all__ = ["get_poly_area", "get_poly_bounds", "get_poly_wh"]

def get_poly_area(poly):
    return poly.area


def get_poly_bounds(poly):
    min_x, min_y, max_x, max_y = poly.bounds

    return min_x, min_y, max_x, max_y


def get_poly_wh(poly):
    min_x, min_y, max_x, max_y = get_poly_bounds(poly)
    poly_w, poly_h = max_x - min_x, max_y - min_y

    return poly_w, poly_h
