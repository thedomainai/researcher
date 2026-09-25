---
title: "Recommendations for visual predictive checks in Bayesian workflow"
authors: "Teemu Säilynoja, Andrew R. Johnson, Osvaldo A. Martin, Aki Vehtari"
year: 2026
citations: 1
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-17T06:00:07.988238"
doi: "https://doi.org/10.54337/jovi.v1i1.11478"
openalex_id: "https://openalex.org/W4415084883"
source_api: "openalex"
---

# Recommendations for visual predictive checks in Bayesian workflow

**著者**: Teemu Säilynoja, Andrew R. Johnson, Osvaldo A. Martin, Aki Vehtari
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: 脳科学

## Abstract

Introduction A key step in the Bayesian workflow for model building is the graphical assessment of model predictions, whether these are drawn from the prior or posterior predictive distribution. The goal of these assessments is to identify whether the model is a reasonable (and ideally accurate) representation of the domain knowledge and/or observed data. There are many commonly used visual predictive checks which can be misleading if their implicit assumptions do not match the reality. Thus, there is a need for more guidance for selecting, interpreting, and diagnosing appropriate visualizations. As a visual predictive check itself can be viewed as a model fit to data, assessing when this model fails to represent the data is important for drawing well-informed conclusions. Demonstration We present recommendations for appropriate visual predictive checks for observations that are: continuous, discrete, or a mixture of the two. We also discuss diagnostics to aid in the selection of visual methods. Specifically, in the detection of an incorrect assumption of continuously-distributed data: identifying when data is likely to be discrete or contain discrete components, detecting and estimating possible bounds in data, and a diagnostic of the goodness-of-fit to data for density plots made through kernel density estimates. Conclusion We offer recommendations and diagnostic tools to mitigate ad-hoc decision-making in visual predictive checks. These contributions aim to improve the robustness and interpretability of Bayesian model criticism practices. Materials The source code implementing the visualization functions and probabilistic models, as well as extended case-studies and the data for the examples are provided online. The version of these materials used in this article is available in Zenodo, and the latest version at https://github.com/TeemuSailynoja/visual-predictive-checks/tree/main/code.
