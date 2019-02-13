Relation
========

contour_intersects
--------
::

def contour_intersects(np_arr1, np_arr2):
    """ Determine two contours are intersected or not.

    """

construct_intersection_polygon
--------
::

def construct_intersection_polygon(np_arr1, np_arr2):
    """ Construct polygon from the intersection part of two contours.

    """

contour_contains
--------
::

def contour_contains(np_arr1, np_arr2):
    """ Determine if contour of np_arr1 contains contour of np_arr2.

    """

cnt_dice_ratio
--------
::

def cnt_dice_ratio(cnt1, cnt2, smooth=0.01):
    """ Calculate the dice ratio between two contours.

    """

cnt_jaccard_index
--------
::

def cnt_jaccard_index(cnt1, cnt2, smooth=0.01):
    """ Calculate the jaccard index between two contours.

    """

point_in_contour
--------
::

def point_in_contour(np_arr, py, px):
    """ Determine point inside contour or not.

    """
