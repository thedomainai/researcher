---
title: "Photometric classification of supernovae detected by the Zwicky Transient Facility using noise augmentation"
authors: "A. Townsend, Jakob Nordin, M. Kowalski, Simeon Reusch, J. P. Anderson"
year: 2026
citations: 3
paper_type: "primary"
domain: "cosmology_astrophysics"
fetched: "2026-11-27T06:06:54.202312"
doi: "https://doi.org/10.1051/0004-6361/202557592"
openalex_id: "https://openalex.org/W7129092209"
source_api: "openalex"
---

# Photometric classification of supernovae detected by the Zwicky Transient Facility using noise augmentation

**著者**: A. Townsend, Jakob Nordin, M. Kowalski, Simeon Reusch, J. P. Anderson
**年**: 2026 | **被引用数**: 3
**タイプ**: primary | **分野**: 宇宙論・宇宙物理

## Abstract

Modern time-domain surveys, such as the Zwicky Transient Facility (ZTF), detect far more extragalactic transients than can be spectroscopically classified. Photometric classification offers a scalable alternative, enabling the identification of larger, fainter, and higher-redshift supernova (SN) samples suitable for applications such as Type Ia SN (SN Ia) cosmology. We present a feature-based photometric classifier for SNe detected by ZTF, with the primary goal of constructing a photometric SN Ia sample for cosmological analyses. Our approach utilises the autoencoder architecture from the model to capture the intrinsic diversity of SN light curves. We trained the model on a spectroscopically classified ZTF SN sample, incorporating a realistic redshift and augmentation procedure that simulates the flux uncertainties of fainter sources. This enables the model to generalise to noisier, higher-redshift populations. Light curve features were used to train a gradient-boosted decision tree classifier, implemented in both binary (SN Ia vs non-Ia) and multi-class configurations. We validated our classifier on independent, fainter ZTF data with and without augmentation. To evaluate real-time performance, we also applied our classifier to live ZTF alerts and conducted a spectroscopic classification survey within the ePESSTO+ collaboration. ParSNIP We found that redshift and noise augmentation significantly improves classification performance, particularly for fainter sources. Our binary classifier achieves an SN Ia recall of $(98.1 ± 0.4)%$, averaged across five train–test splits. SN Ia recall exceeds 98% for events with more than 10 detections and a peak apparent magnitude of up to 20, remaining above 96% up to a magnitude of 20.5. Overall, 95% of the sources were correctly classified in both binary and multi-class modes. In our live classification survey, we correctly identified the class for 78% of the targets, including rare events such as superluminous SNe, despite a median of only nine detections per object. Our classifier performs efficiently on real ZTF data, including faint and noisy light curves. Applied to the full ZTF transient sample, it will enable the construction of a large photometric SN Ia dataset for cosmology. It also provides a practical tool for real-time spectroscopic target prioritisation, which will be essential for large-scale surveys such as the Vera C. Rubin Observatory’s Legacy Survey of Space and Time.
