---
title: 'pycontour: A Python package for contour representation and functionalities'
tags:
    - contour
    - boundary
    - polygon
    - representation
    - feature
authors:
    - name: Pingjun Chen
        orcid: 0000-0003-0528-1713
        affiliation: "1"
    - name: Lin Yang
        affiliation: "1"
affiliations:
    - name: Department of Biomedical Engineering, University of Florida
        index: 1
date: 17 December 2018
bibliography: paper.bib
---

Summary
------------
Contour, which also was called as polygon, boundary, or closed curve etc., is a very important concept in image analysis and computer vision. Both segmentation and detection results can be saved as a list of region of interests (ROI) [@yushkevich2006user, @xing2016automatic] or bounding boxes [@zitnick2014edge, @cai2018iterative], respectively, and contour is well suited to represent both ROI and bounding box. However, there is no standard on how to represent the contour in Python. Right now, contours could be represented as a list of points, numpy array (e.g. OpenCV [@bradski2000opencv]), or Polygon class (e.g. Shapely [@gillies2013shapely]) et al. In addition, the order of coordinates (What Comes First? Width or Height?) also can be set at will by the user.

``pycontour`` package is written with two goals in mind for developers and researchers dealing with contours using Python: 1) Implementing contour format transformation of three commonly used contour representations; 2) Collecting and improving contour functionalities from these packages, such as contour relationship checking functions in Shapely, contour property calculation functions in OpenCV.

``pycontour`` is designed to be used by computer vision developers and researchers, especially for those focusing on biomedical image analysis. With pycontour, users can choose the contour representation format of their like, easily convert other representation formats to their chosen one, and use collected functionalities of all contour related packages. ``pycontour`` can help users relieve the troubles of representation inconsistency when using Python dealing with contours.

Acknowledgement
------------
Development was supported by National Institutes of Health R01 AR065479-02.

References
------------
