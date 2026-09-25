---
title: "pyAvalanches: A Python Package for Analyzing Spatiotemporal Propagation in Neuronal Avalanches"
authors: "M. Marzulli, A. Angiolelli, C. Mannino, M. Demuru, P. Sorrentino"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-12T06:01:40.595423"
arxiv_id: "http://arxiv.org/abs/2609.11530v1"
source_api: "arxiv"
categories: "q-bio.NC"
---

# pyAvalanches: A Python Package for Analyzing Spatiotemporal Propagation in Neuronal Avalanches

**著者**: M. Marzulli, A. Angiolelli, C. Mannino, M. Demuru, P. Sorrentino
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

The analysis of neuronal avalanches offers insights into brain dynamics utilizing the framework of criticality, but the reproducibility and comparability of studies are limited by the use of fragmented, lab-specific scripts. To address this issue, we introduce pyAvalanches, an open-source Python package providing a standardized, end-to-end pipeline for avalanche analysis from electrophysiological recordings (e.g., electroencephalography-EEG). Starting from the detection of neuronal avalanches the package provides their core statistical characterization, including size and duration distributions. Beyond this, the main aim of pyAvalanches is to characterize the spatiotemporal organization of activity propagation during avalanches. To this end, the core innovation of pyAvalanches is the compuation of Avalanche Transition Matrices (ATMs) to map spatiotemporal propagation patterns. Building on this, the package derives network-based metrics from the ATMs, bridging the study of the topology and organization of the underlying dynamical interactions with network neuroscience adopting the framework of neuronal avalanches. The entire workflow is encapsulated in a modular and scikit-learn compatible architecture. We demonstrate the utility of pyAvalanches through an illustrative group-level analysis on a public resting-state EEG dataset, comparing propagation patterns across different clinical populations. By providing a user-friendly, tested, and extensible tool, pyAvalanches facilitates reproducible research, enables the development of novel avalanche-based biomarkers, and makes complex avalanche analysis accessible to a broader scientific community. The package is fully documented and distributed via the Python Package Index (PyPI).
