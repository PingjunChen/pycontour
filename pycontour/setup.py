# -*- coding: utf-8 -*-

import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
PKG_NAME = os.path.basename(BASE_PATH)


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(PKG_NAME, parent_package, top_path)

    # Add subpackage
    config.add_subpackage('cnt')
    config.add_subpackage('fea')
    config.add_subpackage('img')
    config.add_subpackage('poly')
    config.add_subpackage('rela')
    config.add_subpackage('transform')

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup

    config = configuration(top_path='').todict()
    setup(**config)
