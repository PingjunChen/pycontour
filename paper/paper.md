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
Contour, also called as polygon, boundary, or closed curve etc., is one of the most important concept in image analysis and computer vision. Both segmentation and detection results can be saved with contour format, in the form of region of interests (ROI) [@yushkevich2006user, @xing2016automatic] or bounding boxes [@zitnick2014edge, @cai2018iterative], respectively. However, there are no standards on how to represent contour format in Python. Right now, there are mainly three contour representations: 1) list of points; 2) numpy array (e.g. OpenCV [@bradski2000opencv]); 3) Polygon class (e.g. Shapely [@gillies2013shapely]). Moreover, the order of contour coordinates (What Comes First? Width or Height?) also confuse the user.

``pycontour`` package is written mainly with two goals in mind for developers and researchers dealing with contours using Python: 1) Proposing a new intuitive contour format representation in Python, with fully back forth conversion to other three commonly used contour representation format; 2) Implementing commonly used contour functionalities to enable researchers to handle contour easily, including contour transforming, contour masking image, and contour feature extracting et al.

``pycontour`` is designed to be used by computer vision developers and researchers, especially those focusing on biomedical image analysis. With pycontour, users can use contour with a easily understood representation, and take advange of ready-made comprensive contour functionalities. 

Acknowledgement
------------
Development was supported by National Institutes of Health R01 AR065479-02.

References
------------
