Transform
========

swap_wh
--------
::

def swap_wh(np_arr):
    """Swap row of width and row of height
    
    """

np_arr_to_point_list
--------
::

def np_arr_to_point_list(np_arr):
    """Convert 2d numpy array to list of points

    """

point_list_to_np_arr
--------
::

def point_list_to_np_arr(point_list):
    """Convert list of point coordinates to 2d array

    """

cv_cnt_to_np_arr
--------
::

def cv_cnt_to_np_arr(cv_cnt):
    """Convert cv2 contour to normal numpy 2d array [0]-w, [1]-h

    """

np_arr_to_cv_cnt
--------
::

def np_arr_to_cv_cnt(np_arr):
    """Convert 2d coordinates to cv2 contour

    """

construct_poly_using_np_arr
--------
::

def construct_poly_using_np_arr(np_arr):
    """Using numpy array to construct polygon

    """    

construct_poly_using_point_list
--------
::

def construct_poly_using_point_list(point_list):
    """Using point list to construct polygon

    """    

construct_poly_using_bbox
--------
::

def construct_poly_using_bbox(min_w, min_h, max_w, max_h):
    """Using bounding box to construct polygon

    """
    
poly_to_np_arr
--------
::

def poly_to_np_arr(poly):
    """Convert shapely Polygon to normal numpy 2d array [0]-w, [1]-h

    """    