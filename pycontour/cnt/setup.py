# -*- coding: utf-8 -*-

import os, sys

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
MODULE_NAME = os.path.basename(BASE_PATH)


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs

    config = Configuration(MODULE_NAME, parent_package, top_path)
    config.add_data_dir('tests')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='Pingjun Chen',
          maintainer_email='chenpingjun@gmx.com',
          description='Contour operation utilities.',
          url='https://github.com/PingjunChen/pydaily',
          license='Apache',
          **(configuration(top_path='').todict())
          )
