---
title: "AI-Driven Prediction of Cuttings Concentration and Arrival Mass in Underbalanced Coiled-Tubing Drilling of Tight Gas Reservoirs Using Nitrogen Injection and Drilling Parameters"
authors: "Klemens Katterbauer, S. Abu Alsaud, Saleh Komies, Ahmed Alsmaeil"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-05-19T06:03:20.347775"
doi: "https://doi.org/10.2118/232640-ms"
openalex_id: "https://openalex.org/W7161500474"
source_api: "openalex"
---

# AI-Driven Prediction of Cuttings Concentration and Arrival Mass in Underbalanced Coiled-Tubing Drilling of Tight Gas Reservoirs Using Nitrogen Injection and Drilling Parameters

**著者**: Klemens Katterbauer, S. Abu Alsaud, Saleh Komies, Ahmed Alsmaeil
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Abstract Accurate prediction of cuttings concentration and mass arrival at the surface is critical for optimizing underbalanced coiled-tubing drilling (UBCTD) operations in tight gas reservoirs. The complex interplay between nitrogen injection rate, annular velocity, rock properties, and well geometry creates dynamic multiphase flow conditions that traditional empirical correlations often fail to capture. These limitations can lead to poor hole cleaning, excessive surface gas handling loads, and inefficient drilling practices. This study presents the development and validation of an artificial intelligence (AI) algorithm trained on a comprehensive synthetic dataset designed to model the coupled hydraulic and mechanical interactions governing cuttings transport under underbalanced conditions. A large-scale, physically consistent dataset comprising 100,000 operational scenarios was generated to capture the wide variability in UBCTD parameters. Input features included nitrogen injection rate, annular velocity, rate of penetration (ROP), bit and coil dimensions, rock density, gas fraction, inclination, choke size, temperature, and formation permeability. Derived quantities such as hole and annulus geometry, transport efficiency, and retention factor were modeled using empirical and physics-informed relationships. The AI framework employed a supervised learning approach using ensemble regression techniques (e.g., Random Forest and Gradient Boosting) to predict two target variables: (i) cuttings concentration at surface (kg/m³), and (ii) arrival mass rate (kg/hr). The dataset was partitioned into training (80%) and testing (20%) subsets, and hyperparameter optimization was performed via cross-validation. Model explainability was assessed through feature importance ranking and SHAP value interpretation. The trained AI model achieved high predictive accuracy for both target variables on the test set. The most influential predictors were annular velocity, nitrogen injection rate, gas fraction, and ROP, confirming their dominant role in determining cuttings transport dynamics. The model successfully captured nonlinear dependencies such as reduced transport efficiency at excessive gas fractions and the stabilizing effect of higher bit rotation speed on suspension. Sensitivity analyses revealed that moderate nitrogen injection combined with annular velocities produced optimal cuttings removal in most tight gas scenarios. The AI predictions showed consistent alignment with physical expectations derived from multiphase flow theory, demonstrating the robustness of the synthetic dataset and the underlying feature engineering strategy. This study introduces a hybrid data-driven and physics-informed AI approach for real-time estimation of cuttings concentration and surface arrival mass in underbalanced drilling. Unlike conventional empirical models, the proposed algorithm captures nonlinear multivariate interactions between gas–liquid–solid phases, providing a scalable and field-adaptable predictive tool. The generated dataset represents one of the most comprehensive synthetic frameworks for UBCTD hydraulics to date, enabling algorithm training without dependence on proprietary field data. The developed AI model can be integrated into digital drilling platforms for real-time hole cleaning monitoring, optimization of nitrogen injection, and predictive control of surface handling systems, thereby enhancing safety, operational efficiency, and cost-effectiveness in tight gas developments.
