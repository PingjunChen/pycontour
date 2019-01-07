# **pycontour - Contour toolkit in Python**
[![Build Status](https://travis-ci.org/PingjunChen/pycontour.svg?branch=master)](https://travis-ci.org/PingjunChen/pycontour)
[![Documentation Status](https://readthedocs.org/projects/pycontour/badge/?version=latest)](https://pycontour.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pycontour.svg)](https://badge.fury.io/py/pycontour)
![](https://img.shields.io/github/license/PingjunChen/pycontour.svg)

<img src="./docs/media/wsi-mucosa-tissue.png" width="800" height="320" alt="Banner">


## Origin
Contour is one of the most important concept in lots of image-based applications, especially in medical imaging domain, mainly for region of interest (ROI) representation. [OpenCV](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) and [shapely](http://shapely.readthedocs.io/en/stable/manual.html) both provide a few contour functionality support.

This package tries to simplify the usage of contour operation, using numpy 2d array ([0]-h, [1]-w) as the standards for contour representation.  If you find [pycontour](https://github.com/PingjunChen/pycontour) to be helpful for your work, please `star` this repo.


## Installation
To install pycontour, libgeos and shapely need to install in advance. Other required packages can refer to requirements.txt.
```
$ sudo apt-get install libgeos-dev
$ pip install shapely
$ pip install opencv-python
$ pip install pycontour
```

## Usage example
Contour representation can be transformed back and forth. The user can operate the contours in their favor manner.
```
# load image
img_path = "./data/Imgs/20181218042607.jpg"
img = misc.imread(img_path)
# extract contours using OpenCV
cnts = extract_cnt_using_cv2(img_path)
test_cnt = cnts[1]
# convert cv2 contour to numpy array
np_arr = cv_cnt_to_np_arr(test_cnt)
# convert numpy arrary to cv2 contour
cv_cnt = np_arr_to_cv_cnt(np_arr)
# draw contour on image
draw_img = cv2.drawContours(img, [cv_cnt], 0, (0, 0, 255), 7)
```

## Documentation
Hosted in [https://pycontour.readthedocs.io](https://pycontour.readthedocs.io), powered by [readthedocs](https://readthedocs.org) and
[Sphinx](http://www.sphinx-doc.org).

## Contributing
``pycontour`` is an open source project and anyone is welcome to contribute. An easy way to get started is by suggesting a new enhancement on the [Issues](https://github.com/PingjunChen/pycontour/issues). If you have found a bug, then either report this through [Issues](https://github.com/PingjunChen/pycontour/issues), or even better, make a fork of the repository, fix the bug and then create a [Pull Request](https://github.com/PingjunChen/pycontour/pulls) to get the fix into the master branch.

## Contributors
See the [AUTHORS.md](AUTHORS.md) file for a complete list of contributors to the project.

## License
``pycontour`` is free software made available under the MIT License. For details see the [LICENSE](LICENSE) file.
