# -*- coding: utf-8 -*-

import os, sys
import numpy as np

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)

from pycontour.transform import shift_cnt


def test_shift_cnt():
    cnt1 = np.array([[0, 0, 2, 2], [0, 2, 2, 0]])    
    cnt2 = shift_cnt(cnt1, shift_h=3, shift_w=5)
    cnt3 = shift_cnt(cnt2, shift_h=-3, shift_w=-5)
    assert np.array_equal(cnt1, cnt3), "Shift back and forth error"
