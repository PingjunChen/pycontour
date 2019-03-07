# -*- coding: utf-8 -*-


__all__ = ["get_poly_area",
           "get_poly_bounds",
           "get_poly_hw"]


def get_poly_area(poly1):
    """ Calcualte the number of pixels the polygon covered.

    Parameters
    -------
    poly1 : Polygon
        contour with shapely polygon format

    Returns
    -------
    area_val : int
        number of pixels inside the contour

    """

    area_val = poly1.area

    return area_val


def get_poly_bounds(poly1):
    """ Find the bounds of the Polygon.

    Parameters
    -------
    poly1 : Polygon
        contour with shapely polygon format

    Returns
    -------
    min_h : int
        minimum y coordinate of polygon
    min_w : int
        minimum x coordinate of polygon
    max_h : int
        maximum y coordinate of polygon
    max_w : int
        maximum x coordinate of polygon

    """

    min_x, min_y, max_x, max_y = poly1.bounds
    min_h, min_w = min_y, min_x
    max_h, max_w = max_y, max_x

    return min_h, min_w, max_h, max_w


def get_poly_hw(poly1):
    """ Find height and width of the polygon.

    Parameters
    -------
    poly : Polygon
        contour with shapely polygon format

    Returns
    -------
    poly_h : int
        height of the polygon
    poly_w : int
        width of the polygon

    """

    min_h, min_w, max_h, max_w = get_poly_bounds(poly1)

    poly_h = max_h - min_h + 1
    poly_w = max_w - min_w + 1

    return poly_h, poly_w
