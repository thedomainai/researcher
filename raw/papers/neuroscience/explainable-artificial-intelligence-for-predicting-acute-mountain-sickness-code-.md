---
title: "Explainable Artificial Intelligence for Predicting Acute Mountain Sickness — Code and Analysis"
authors: "César A. Astudillo, Leonardo Fuentes Escobar, A Gonzalez Villalobos, Carlos Chavez Sanchez"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-26T06:00:09.796012"
doi: "https://doi.org/10.5281/zenodo.20788978"
openalex_id: "https://openalex.org/W7165486818"
source_api: "openalex"
---

# Explainable Artificial Intelligence for Predicting Acute Mountain Sickness — Code and Analysis

**著者**: César A. Astudillo, Leonardo Fuentes Escobar, A Gonzalez Villalobos, Carlos Chavez Sanchez
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

This repository contains the full code and computational analysis for the paper "Explainable Artificial Intelligence for Predicting Acute Mountain Sickness", submitted to the 29th Iberoamerican Congress on Pattern Recognition (CIARP 2026). The work presents a reproducible benchmark of five machine learning classifiers (Random Forest, SVM, AdaBoost, XGBoost, and a Multilayer Perceptron) for binary prediction of Acute Mountain Sickness (AMS), using the publicly available physiological and psychological dataset of Boos et al. (2018). Models are evaluated under subject-level nested cross-validation to prevent data leakage, compared with non-parametric statistical tests, and interpreted with SHAP (SHapley Additive exPlanations) to identify the most influential predictors of AMS susceptibility. The repository is organized as a Jupyter Notebook that documents the complete workflow: data loading and preprocessing, the binary label construction, the cross-validation and hyperparameter-tuning procedure, the benchmark results, the statistical comparison of classifiers, and the SHAP-based explainability analysis. Each step includes the executable code together with explanatory commentary, so the experiments can be inspected, reproduced, and extended. Source code: https://github.com/ML-Project-2026/AMS_2026
