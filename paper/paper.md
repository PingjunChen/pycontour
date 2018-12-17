---
title: 'pycontour: A Python package for contour representation and functionality'
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
 - name: Department of Biomedical Engineering, University of Florida
   index: 1
date: 17 December 2018
bibliography: paper.bib
---

# Summary
Contour, which also was called as polygon, boundary, and closed curve et al., is a very important element in biomedical image analysis. Both segmentation and detection results can be saved as a list of region of interests (ROI) [@yushkevich2006user] or bounding boxes [@zitnick2014edge], respectively. Contour is a well suited to represent both ROI and bounding box. However, there is no standards on how to save the contour. Now contours could be saved as a list of point set, numpy array (e.g. OpenCV [@bradski2000opencv]), or Polygon class (e.g. Shapely [@gillies2013shapely]) et al.
The order of coordinates (What Comes First? Width or Height?) can also be set at will by the user.

``pycontour`` package is written with two goals in mind for developers and researchers dealing with contour using Python: 1) Implementing contour format transformation of three commonly used contour representation methods; 2) Collecting contour functionalities from these packages, such as contour relationship checking functions in Shapely, contour property calculation functions in OpenCV.

``pycontour`` is designed to be used by computer vision developers and researchers, especially for those focusing on biomedical image analysis. With pycontour, users can choose the contour representation format of their like, easily convert other formats to their chosen one, and use collected functionalities of all contour related packages. ``pycontour`` can help users relieve the format inconsistency trouble when using Python dealing with contours .

# Acknowledgement
Development was supported by National Institutes of Health R01 AR065479-02.

# References
