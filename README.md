**pycontour - Python contour toolkit**
============
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7a79d543daca49f49d2c8e90bc9b14ce)](https://app.codacy.com/app/PingjunChen/pycontour?utm_source=github.com&utm_medium=referral&utm_content=PingjunChen/pycontour&utm_campaign=Badge_Grade_Dashboard)
[![CircleCI](https://circleci.com/gh/PingjunChen/pycontour.svg?style=svg)](https://circleci.com/gh/PingjunChen/pycontour)
[![Documentation Status](https://readthedocs.org/projects/pycontour/badge/?version=latest)](https://pycontour.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pycontour.svg)](https://badge.fury.io/py/pycontour)
![](https://img.shields.io/github/stars/PingjunChen/pycontour.svg)

<img src="./docs/media/wsi-mucosa-tissue.png" width="800" height="320" alt="Banner">

Motivation
------------
Contour is one of the most important concept in plenty of image-based applications, mainly for the representation of region of interest (ROI), especially in medical imaging area. [OpenCV](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) and [shapely](http://shapely.readthedocs.io/en/stable/manual.html) both provide a few contour functionalities.

This package tries to standardize the contour representation in python. Different from OpenCV, each contour is represented as a numpy 2d array with shape 2*N (0-h 1-w), in which height always comes first. Moreover, back and forth conversion between this representation with OpenCV or shapely are supported, enabling developers to take advantage of the functionalities of both OpenCV and shapely. If you find [pycontour](https://github.com/PingjunChen/pycontour) to be helpful for your work, please `star` this repo.

Installation
------------
To install pycontour, libgeos need to install in advance. Other required packages can refer to requirements.txt.
```
$ sudo apt-get install libgeos-dev
$ pip install shapely opencv-python skimage
$ pip install pycontour==1.3.2
```

Usage example
------------
Contour representation can be transformed back and forth between this representation with the way OpenCV or shapely represents. The user can use contour in their favor manner. We recommend numpy 2d array (2*N: 0-h, 1-w) as the standard representation, which is easiest to understand in our opinion.

```alpha
# load image
img_path = "./data/Imgs/20181218042607.jpg"
img = misc.imread(img_path)
# extract contours using OpenCV
cnts = extract_cnt_using_cv2(img_path)
test_cnt = cnts[1]
# convert cv2 contour to numpy 2d array
np_arr = cv_cnt_to_np_arr(test_cnt)
# convert numpy 2d arrary to cv2 contour
cv_cnt = np_arr_to_cv_cnt(np_arr)
# draw contour on image
draw_img = cv2.drawContours(img, [cv_cnt], 0, (0, 0, 255), 7)
```

Documentation
------------
Hosted in [https://pycontour.readthedocs.io](https://pycontour.readthedocs.io), powered by [readthedocs](https://readthedocs.org) and
[Sphinx](http://www.sphinx-doc.org).

Contributing
------------
``pycontour`` is an open source project and anyone is welcome to contribute. An easy way to get started is by suggesting a new enhancement on the [Issues](https://github.com/PingjunChen/pycontour/issues). If you have found a bug, then either report this through [Issues](https://github.com/PingjunChen/pycontour/issues), or even better, make a fork of the repository, fix the bug and then create a [Pull Request](https://github.com/PingjunChen/pycontour/pulls) to get the fix into the master branch.

Contributors
------------
See the [AUTHORS.md](AUTHORS.md) file for a complete list of contributors to the project.

License
------------
``pycontour`` is free software made available under the MIT License. For details see the [LICENSE](LICENSE) file.
