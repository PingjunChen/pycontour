# -*- coding: utf-8 -*-

import os, sys

from pycontour import point_list_to_np_arr
from pycontour.polygon import contour_intersects
from pycontour.polygon import construct_intersection_polygon


if __name__ == "__main__":
    point_list1 = [(1, 4), (3, 4), (3, 1), (1, 1)]
    point_list2 = [(2, 3), (4, 3), (4, 0), (2, 0)]
    point_list3 = [(3, 1), (5, 1), (5, -2), (3, -2)]
    # Convert point list to numpy array
    np_arr1 = point_list_to_np_arr(point_list1)
    np_arr2 = point_list_to_np_arr(point_list2)
    np_arr3 = point_list_to_np_arr(point_list3)

    # inter12 = contour_intersects(np_arr1, np_arr2)
    # print("Point list1 and point list2 intersected: {}".format(inter12))
    # inter13 = contour_intersects(np_arr1, np_arr3)
    # print("Point list1 and point list3 intersected: {}".format(inter13))
    # inter23 = contour_intersects(np_arr2, np_arr3)
    # print("Point list2 and point list3 intersected: {}".format(inter23))
    intersection12 = construct_intersection_polygon(np_arr1, np_arr2)
    print("Area of intersection 1 and 2 is: {}".format(intersection12.area))
    intersection13 = construct_intersection_polygon(np_arr1, np_arr3)
    print("Area of intersection 1 and 3 is: {}".format(intersection13.area))
    intersection23 = construct_intersection_polygon(np_arr2, np_arr3)
    print("Area of intersection 2 and 3 is: {}".format(intersection23.area))
