---
title: "Trustworthy direct interval propagation via conformal prediction in neural network surrogates"
authors: "Ghifari Adam Faza, Hans Hallez, David Moens"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-01T06:00:06.258105"
doi: "https://doi.org/10.17877/tudobooks-11.195"
openalex_id: "https://openalex.org/W7201906978"
source_api: "openalex"
---

# Trustworthy direct interval propagation via conformal prediction in neural network surrogates

**著者**: Ghifari Adam Faza, Hans Hallez, David Moens
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Uncertainty propagation is essential for reliable engineering design, but when input distributions are unknown, or data are scarce, probabilistic models risk misspecification, making interval representations a more robust alternative. However, interval propagation requires solving optimisation problems for each bound, leading to high computational cost, especially in downstream tasks such as design optimisation or reliability analysis. To mitigate this, surrogate models can be designed to provide interval predictions directly via interval-valued regression, supported by recent neural-network-based methods and data augmentation strategies for constructing interval datasets. Yet these approaches typically ignore surrogate approximation error and data noise. We address this by extending interval regression with a conformal prediction framework, which is model-agnostic and provides user-controlled confidence levels to capture both input and model uncertainty in a distribution-free manner. Experimental results on analytical and PDE benchmark problems demonstrate that the proposed conformalised interval propagation significantly improves coverage reliability compared to uncalibrated predictors, while maintaining practical prediction efficiency. Furthermore, we show that calibration using approximate interval data remains effective when the approximation error is limited, highlighting the practical applicability of the proposed framework in data-scarce settings.
