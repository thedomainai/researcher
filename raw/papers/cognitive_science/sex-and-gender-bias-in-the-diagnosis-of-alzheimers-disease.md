---
title: "Sex and gender bias in the diagnosis of Alzheimer’s disease"
authors: "Susanne Neufang, Atae Akhrif, Oya Beyan, Neuroimaging Initiative"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-11-08T06:10:31.357151"
doi: "https://doi.org/10.1038/s41598-026-77773-2"
openalex_id: "https://openalex.org/W7212274081"
source_api: "openalex"
---

# Sex and gender bias in the diagnosis of Alzheimer’s disease

**著者**: Susanne Neufang, Atae Akhrif, Oya Beyan, Neuroimaging Initiative
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

Abstract Fairness in clinical machine-learning (ML) remains a critical challenge, particularly in neurodegenerative disease where demographic factors may confound disease-related patterns. We developed and evaluated bias-aware ML models for Alzheimer’s disease (AD) classification using data from the Alzheimer’s Disease Neuroimaging Initiative (ADNI), comprising 757 individuals with mild cognitive impairment (MCI) and AD. Four supervised learning algorithms (logistic regression, support vector machine, random forest, and XGBoost) were trained using demographic, genetic, neuropsychological, and MRI-derived features. Sex was treated as a protected attribute, and bias mitigation was implemented using pre-processing, in-processing, and post-processing methods within the IBM AI Fairness 360 framework. Bias mitigation reduced disparities in predictions, with disparate impact decreasing from 1.167 to 0.823. The logistic regression model with Disparate Impact Remover (LR/DIR) improved performance while maintaining fairness, whereas adversarial debiasing achieved the highest balanced accuracy (88.91%). Explainability analyses in the LR/DIR model using LIME showed altered feature attribution patterns with increased convergence between sexes and stronger contribution of clinical and gender-related variables after debiasing. SHAP analysis in the adversarial debiasing model confirmed that Mini-Mental State Examination score, functional status, age, and medial temporal lobe atrophy were the strongest predictors of AD. These findings demonstrate that fairness-aware ML can reduce sex-related bias in AD classification without loss of performance and improve interpretability through more balanced representation of disease determinants.
