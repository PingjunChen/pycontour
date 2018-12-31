# **pycontour - Contour operation utilities**
[![Build Status](https://travis-ci.org/PingjunChen/pycontour.svg?branch=master)](https://travis-ci.org/PingjunChen/pycontour)
[![Documentation Status](https://readthedocs.org/projects/pycontour/badge/?version=latest)](https://pycontour.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pycontour.svg)](https://badge.fury.io/py/pycontour)
![](https://img.shields.io/github/license/PingjunChen/pycontour.svg)


<img src="./docs/media/wsi-mucosa-tissue.png" width="800" height="320" alt="Banner">


## Origin
Contour is one of the most important concept in plentiful image-based applications, especially in medical imaging field, mainly for region of interest (ROI). [OpenCV](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) and [shapely](http://shapely.readthedocs.io/en/stable/manual.html) both provide a few contour operation support. This package tries to simplify the usage of contour operation, with numpy as the fundamental representation for contour.


## Installation
To install pycontour, libgeos and shapely need to install in advance. Other required packages can refer requirements.txt.
```
$ sudo apt-get install libgeos-dev
$ pip install shapely
$ pip install opencv-python
$ pip install pycontour
```

## Documentation
Hosted in [https://pycontour.readthedocs.io](https://pycontour.readthedocs.io), powered by [readthedocs](https://readthedocs.org) and
[Sphinx](http://www.sphinx-doc.org).

## Contributing
All questions, bug reports, and suggestions etc. are welcome to [Issue](https://github.com/PingjunChen/pycontour/issues). New features are welcome to [Pull Request](https://github.com/PingjunChen/pycontour/pulls).

## Contributors
See the [AUTHORS.md](AUTHORS.md) file for a complete list of contributors to the project.

## License
[pycontour](https://github.com/PingjunChen/pycontour) is free software made available under the Apache License 2.0. For details see the [LICENSE](LICENSE) file.
