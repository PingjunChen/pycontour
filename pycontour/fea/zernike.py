# -*- coding: utf-8 -*-

import mahotas

from ..img import construct

__all__ = ["ZernikeMoments", ]


class ZernikeMoments:
    """ Calculate Zernike moments for contour.

    """

    def __init__(self, radius):
        """ Setting the radius

        Parameters
        -------
        radius: int
            the maximum radius for the Zernike polynomials

        """

        self.radius = radius

    def cal_fea(self, np_arr):
        """ Calculate zernike moments for contour

        Parameters
        -------
        np_arr : np.array
            contour with standard numpy 2d array format

        feas: np.array
            feature vector for image

        """

        mask = construct.build_cnt_mask(np_arr)
        feas = mahotas.features.zernike_moments(mask, self.radius)

        return feas
