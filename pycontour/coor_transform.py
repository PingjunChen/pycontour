# -*- coding: utf-8 -*-

import os, sys
import numpy as np

__all__ = ["swap_wh", "np_arr_to_point_list", "point_list_to_np_arr"]


def swap_wh(np_arr):
    """Swap row of width and row of height
     Parameters
    ----------
    np_arr : np.array
        Numpy array with width and height

    Returns
    -------
    np_arr : np.array
        Numpy array with width and height position change 
  
    """

    np_arr[[0,1]] = np_arr[[1,0]]

    return np_arr

def np_arr_to_point_list(np_arr):
    """Convert 2d numpy array to list of points
     Parameters
    ----------
    np_arr : np.array
        Numpy array of point set

    Returns
    -------
    point_list : list
        List of point set        
    """

    point_list = []
    num_point = np_arr.shape[1]
    for ind in range(num_point):
        point_list.append((np_arr[0][ind], np_arr[1][ind]))

    return point_list

def point_list_to_np_arr(point_list):
    """Convert list of point coordinates to 2d array
     Parameters
    ----------
    point_list : list
        List of point set            

    Returns
    -------
    np_arr : np.array
        Numpy array of point set    
    
    """
    num_point = len(point_list)
    np_arr = np.zeros((2, num_point))
    for ind in range(num_point):
        np_arr[0][ind] = point_list[ind][0]
        np_arr[1][ind] = point_list[ind][1]

    return np_arr
