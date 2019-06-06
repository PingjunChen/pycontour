# -*- coding: utf-8 -*-


__all__ = ["poly_to_valid",
           ]


def poly_to_valid(poly):
    """ Adjust polygon to be valid if not.

    Parameters
    -------
    poly : Polygon
        contour with shapely polygon format

    Returns
    -------
    valid_poly : Polygon
        contour with shapely polygon format

    """

    if poly.is_valid == True:
        valid_poly = poly
    else:
        valid_poly = poly.convex_hull

    return valid_poly
