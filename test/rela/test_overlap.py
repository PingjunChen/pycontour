# -*- coding: utf-8 -*-

import os, sys
import numpy as np

from os.path import dirname as opd
from os.path import abspath as opa
from os.path import join as opj
TEST_PATH = opa(opd(opd(__file__)))
PRJ_PATH = opd(TEST_PATH)
sys.path.insert(0, PRJ_PATH)
sys.path.insert(0, opj(PRJ_PATH, "pycontour"))

from pycontour.rela import cnt_dice_ratio
from pycontour.rela import cnt_jaccard_index


def test_cnt_dice_ratio():
    cnt1 = np.array([[0, 0, 2, 2], [0, 2, 2, 0]])
    cnt2 = np.array([[-1, -1, 1, 1], [1, 3, 3, 1]])

    dice_ratio = cnt_dice_ratio(cnt1, cnt2)
    if not (dice_ratio >= 0 and dice_ratio <= 1.0):
        raise AssertionError("Dice ratio in the wrong range")


def test_cnt_jaccard_index():
    cnt1 = np.array([[0, 0, 2, 2], [0, 2, 2, 0]])
    cnt2 = np.array([[-1, -1, 1, 1], [1, 3, 3, 1]])

    jaccard_index = cnt_jaccard_index(cnt1, cnt2)
    if not (jaccard_index >= 0.0 and jaccard_index <= 1.0):
        raise AssertionError("jaccard index in the wrong range")
