# -*- coding: utf-8 -*-

import os, sys

from pycontour import point_list_to_np_arr
from pycontour import swap_wh
from pycontour import np_arr_to_point_list


if __name__ == "__main__":
    import pdb; pdb.set_trace()
    point_list = [(0, 0), (2, 0), (2, 2), (1, 2)]
    np_arr = point_list_to_np_arr(point_list)
    swap_arr = swap_wh(np_arr)
    swap_points = np_arr_to_point_list(swap_arr)
