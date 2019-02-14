Representation Transform
========

swap_wh
--------
::

def swap_wh(np_arr):
    """ Swap row of width and row of height.

    """

np_arr_to_point_list
--------
::

def np_arr_to_point_list(np_arr):
    """ Convert 2d numpy array to list of points.

    """

point_list_to_np_arr
--------
::

def point_list_to_np_arr(point_list):
    """ Convert list of point coordinates to numpy 2d array.

    """

cv_cnt_to_np_arr
--------
::

def cv_cnt_to_np_arr(cv_cnt):
    """ Convert cv2 contour to numpy 2d array ([0]-h, [1]-w).

    """

np_arr_to_cv_cnt
--------
::

def np_arr_to_cv_cnt(np_arr):
    """ Convert numpy 2d array ([0]-h, [1]-w) to cv2 contour.

    """

np_arr_to_poly
--------
::

def np_arr_to_poly(np_arr):
    """ Using numpy 2d array ([0]-h, [1]-w) to construct polygon.

    """

point_list_to_poly
--------
::

def point_list_to_poly(point_list):
    """ Using point list to construct polygon.

    """

bbox_to_poly
--------
::

def bbox_to_poly(min_w, min_h, max_w, max_h):
    """ Using bounding box to construct polygon.

    """

poly_to_np_arr
--------
::

def poly_to_np_arr(poly):
    """ Convert shapely Polygon to numpy 2d array ([0]-h, [1]-w).

    """
