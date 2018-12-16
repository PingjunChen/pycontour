# -*- coding: utf-8 -*-

import os, sys

__all__ = ["PKG_DIR", "DATA_DIR", "__version__"]

__version__ = '1.0.0'
PKG_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(os.path.dirname(PKG_DIR), 'data')


from .coor_transform import *
from .cv2_transform import *
from .poly_transform import *
