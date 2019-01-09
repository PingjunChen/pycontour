# -*- coding: utf-8 -*-

import os, sys

__all__ = ["PKG_DIR", "__version__"]

__version__ = '1.2.5'
PKG_DIR = os.path.abspath(os.path.dirname(__file__))

from .coor_transform import *
from .cv2_transform import *
from .poly_transform import *
