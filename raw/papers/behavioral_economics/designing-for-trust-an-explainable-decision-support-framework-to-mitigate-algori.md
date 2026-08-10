---
title: "Designing for Trust: An Explainable Decision Support Framework to Mitigate Algorithmic Aversion in Oncology"
authors: "Abdullah Al Helal"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-06-28T06:01:13.585925"
doi: ""
openalex_id: "https://openalex.org/W7166269969"
source_api: "openalex"
---

# Designing for Trust: An Explainable Decision Support Framework to Mitigate Algorithmic Aversion in Oncology

**著者**: Abdullah Al Helal
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Diagnostic AI models for breast imaging increasingly achieve strong predictive performance, yet clinical adoption remains limited when systems are perceived as opaque. This challenge, known as algorithmic aversion, is especially critical in oncology workflows where clinicians must justify decisions and manage the asymmetric consequences of false negatives and false positives (Dietvorst et al., 2015). I argue that the bottleneck in AI-driven healthcare is not only predictive accuracy, but decision-interface design: a highly accurate model without calibrated, transparent, and threshold-aware output may have limited clinical utility. Therefore, the central Information Systems (IS) challenge is designing AI-enabled clinical decision support that is interpretable, trustworthy, and usable. This TREO proposes an explainable decision-support framework that translates breast imaging predictions into clinician-facing diagnostic evidence. Building on prior engineering work in sparse-representation classification of breast ultrasound and rotation-invariant Local Binary Pattern analysis for mammography, this project examines how different forms of model transparency may influence human trust. Using contemporary public breast ultrasound data, such as BUSI (Al-Dhabyani et al., 2020), the study will develop a prototype diagnostic pipeline. Feature-engineered and mathematically transparent models, including LBP-based and sparse-representation approaches, will be compared against contemporary tree-based models such as XGBoost and black-box deep learning models such as ResNet50. SHAP values and Grad-CAM visualizations will be used to identify the radiomic or visual evidence driving classification. The resulting IT artifact is an explainable diagnostic “decision card” that combines a calibrated risk score, uncertainty information, visual evidence, and a suggested triage category. To evaluate the artifact, a simulated diagnostic decision task will compare user trust, perceived usefulness, and intention to adopt across interpretable versus opaque model outputs. The study examines whether a model with slightly lower predictive accuracy but greater transparency may generate higher decision value and adoption intent. The expected contribution is a human-centered Design Science Research framework for clinical AI. By bridging computational modeling with behavioral IS constructs, this research reframes medical AI design as a problem of trustworthy decision support and argues that clinical AI systems should be designed for human collaboration rather than human replacement.
