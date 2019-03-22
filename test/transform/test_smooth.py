# -*- coding: utf-8 -*-

import sys
import numpy as np

from os.path import dirname as opd
from os.path import abspath as opa
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.transform import smooth_cnt
from pycontour.img import build_cnt_mask

def test_smooth_cnt():
    cnt1 = np.array([[300, 400, 450, 400, 300, 200, 0, 50, 100, 200],
                     [100, 100, 200, 300, 400, 500, 500, 400, 300, 200]])
    # img1 = build_cnt_mask(cnt1)
    smooth_cnt1 = smooth_cnt(cnt1, sigma=10)
    smooth_img1 = build_cnt_mask(smooth_cnt1)
    import matplotlib.pyplot as plt
    plt.imshow(smooth_img1)
