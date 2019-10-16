---
title: 'pycontour: A Python-Based Toolkit for Contour Representation and Functionalities'
tags:
  - contour
  - boundary
  - polygon
  - representation
authors:
 - name: Pingjun Chen
   orcid: 0000-0003-0528-1713
   affiliation: "1"
 - name: Lin Yang
   affiliation: "1"
affiliations:
 - name: J. Crayton Pruitt Family Department of Biomedical Engineering, University of Florida
   index: 1
date: 26 March 2019
bibliography: paper.bib
---

Summary
------------
Contour, also called as polygon, boundary, or closed curve, is one of the most important concept in image analysis and computer vision. The results of segmentation, localization, and detection all can be saved in contour format, in the form of region of interest (ROI) [@yushkevich2006user, @xing2016automatic, @chen2019tissueloc] or bounding box [@zitnick2014edge, @cai2018iterative], etc. However, there are no standards on how to represent contour format in Python. Right now, there are mainly three available contour representations: 1) list of points; 2) numpy array (e.g. OpenCV [@bradski2008learning]); 3) Polygon class (e.g. Shapely [@gillies2013shapely]). They all have their limitations. List of points is not easy to use. OpenCV-based numpy array representation is too complex. Polygon class is not intuitive. Moreover, the order of contour coordinates (What Comes First? Width or Height?) can also confuse the user.

``pycontour`` package is written mainly with two goals in mind for developers and researchers dealing with contours using Python: 1) Proposing a simple and intuitive contour format representation, with fully back-and-forth conversion to other three contour representations; 2) Implementing commonly used contour functionalities, including contour transforming, masking image, and feature extracting etc, to enable researchers to handle contour more easily.

``pycontour`` is designed to be used by computer vision developers and researchers, especially those focusing on biomedical image analysis. With pycontour, users can use contour with a easily understood representation, and take advantage of ready-made comprehensive contour functionalities.

Acknowledgement
------------
Development was supported by National Institutes of Health R01 AR065479-02.

References
------------
