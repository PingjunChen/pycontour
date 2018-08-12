# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from pycontour import np_arr_to_point_list
from pycontour.polygon import construct_polygon_using_np_arr
from pycontour.polygon import construct_polygon_using_point_list
from pycontour.polygon import construct_polygon_using_bbox


if __name__ == "__main__":
    np_arr = np.array([[0, 2, 2, 1], [0, 0, 2, 2]])
    poly1 = construct_polygon_using_np_arr(np_arr)
    print("Bounds of poly1 is: ", poly1.exterior.bounds)
    point_list = np_arr_to_point_list(np_arr)
    poly2 = construct_polygon_using_point_list(point_list)
    print("Bounds of poly2 is: ", poly2.exterior.bounds)
    min_w, max_w = np.min(np_arr[0]), np.max(np_arr[0])
    min_h, max_h = np.min(np_arr[1]), np.max(np_arr[1])
    poly3 = construct_polygon_using_bbox(min_w, min_h, max_w, max_h)
    print("Bounds of poly3 is: ", poly3.exterior.bounds)    
    import pdb; pdb.set_trace()
