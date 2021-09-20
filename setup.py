# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pycontour

PKG_NAME = "pycontour"
VERSION = pycontour.__version__
DESCRIPTION = "pycontour: A Python Toolkit for 2D Contour Processing"
HOMEPAGE = "https://github.com/PingjunChen/pycontour"
LICENSE = "BSD 3-Clause"
AUTHOR_NAME = "Pingjun Chen"
AUTHOR_EMAIL = "pingjunchen@ieee.org"

REQS = ""
with open('requirements.txt') as f:
    REQS = [pkg.replace("==", ">=") for pkg in f.read().splitlines()]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Healthcare Industry',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD 3-Clause "New" or "Revised" License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
]

args = dict(
    name=PKG_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=HOMEPAGE,
    license=LICENSE,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=REQS,
    classifiers= CLASSIFIERS,
)

setup(**args)
