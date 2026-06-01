---
title: "TorchIO: A Python library for efficient loading, preprocessing, augmentation and patch-based sampling of medical images in deep learning"
authors: "Fernando Pérez‐García, Rachel Sparks, Sébastien Ourselin"
year: 2021
citations: 574
paper_type: "primary"
domain: "leadership_ob"
domain_label: "リーダーシップ・組織行動"
source_api: "openalex"
fetched: "2026-05-04T16:46:44.451428"
doi: "10.1016/j.cmpb.2021.106236"
openalex_id: "W3012412627"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://doi.org/10.1016/j.cmpb.2021.106236"
tier: 2
explore_depth: 1
---

# TorchIO: A Python library for efficient loading, preprocessing, augmentation and patch-based sampling of medical images in deep learning

**著者**: Fernando Pérez‐García, Rachel Sparks, Sébastien Ourselin
**年**: 2021 | **被引用数**: 574
**タイプ**: primary | **分野**: リーダーシップ・組織行動

## Abstract

BACKGROUND AND OBJECTIVE: Processing of medical images such as MRI or CT presents different challenges compared to RGB images typically used in computer vision. These include a lack of labels for large datasets, high computational costs, and the need of metadata to describe the physical properties of voxels. Data augmentation is used to artificially increase the size of the training datasets. Training with image subvolumes or patches decreases the need for computational power. Spatial metadata needs to be carefully taken into account in order to ensure a correct alignment and orientation of volumes. METHODS: We present TorchIO, an open-source Python library to enable efficient loading, preprocessing, augmentation and patch-based sampling of medical images for deep learning. TorchIO follows the style of PyTorch and integrates standard medical image processing libraries to efficiently process images during training of neural networks. TorchIO transforms can be easily composed, reproduced, traced and extended. Most transforms can be inverted, making the library suitable for test-time augmentation and estimation of aleatoric uncertainty in the context of segmentation. We provide multiple generic preprocessing and augmentation operations as well as simulation of MRI-specific artifacts. RESULTS: Source code, comprehensive tutorials and extensive documentation for TorchIO can be found at http://torchio.rtfd.io/. The package can be installed from the Python Package Index (PyPI) running pip install torchio. It includes a command-line interface which allows users to apply transforms to image files without using Python. Additionally, we provide a graphical user interface within a TorchIO extension in 3D Slicer to visualize the effects of transforms. CONCLUSION: TorchIO was developed to help researchers standardize medical image processing pipelines and allow them to focus on the deep learning experiments. It encourages good open-science practices, as it supports experiment reproducibility and is version-controlled so that the software can be cited precisely. Due to its modularity, the library is compatible with other frameworks for deep learning with medical images.
