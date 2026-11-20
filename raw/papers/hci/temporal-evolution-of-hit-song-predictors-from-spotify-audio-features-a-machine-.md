---
title: "Temporal Evolution of Hit Song Predictors from Spotify Audio Features: A Machine Learning and Explainable AI Study"
authors: "Christopher Andreas"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-11-21T06:02:56.146444"
doi: "https://doi.org/10.47738/jads.v7i4.1506"
openalex_id: "https://openalex.org/W7224078540"
source_api: "openalex"
---

# Temporal Evolution of Hit Song Predictors from Spotify Audio Features: A Machine Learning and Explainable AI Study

**著者**: Christopher Andreas
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Understanding the factors that distinguish commercially successful songs remains an important problem in music analytics, with implications for applied data science. While previous studies have demonstrated that machine learning models can predict hit songs from audio features, they generally treat the prediction task as static and pay limited attention to how the determinants of success evolve over time. This study investigates the temporal evolution of hit-song predictors using Spotify audio features extracted from 41,103 Billboard-labelled tracks released between 1960 and 2019. The dataset is divided into three industry eras (Analog, CD/Digital, and Streaming) to examine changes in predictive performance and feature importance across distinct periods of music production and distribution. Logistic Regression, Random Forest, and K-Nearest Neighbours are optimized using grid-search cross-validation and evaluated with accuracy, F1-score, and ROC-AUC. Model interpretability is achieved through SHAP analysis. Cross-era differences in feature importance are statistically evaluated using bootstrap confidence intervals, while robustness is further assessed through repeated random seeds, permutation importance, alternative era definitions, and data de-duplication. Among the evaluated models, Random Forest consistently achieves the highest predictive performance, with ROC-AUC ranging from 0.848 to 0.917 across the three eras, indicating that chart success has become increasingly predictable from audio characteristics over time. Explainable AI analysis reveals a systematic evolution in the importance of musical attributes: instrumentalness remains the strongest predictor throughout, loudness becomes substantially more influential in the Streaming era, whereas speechiness and acousticness progressively decline in importance. These patterns are supported by bootstrap statistical testing and remain stable across multiple robustness analyses, suggesting that the observed temporal changes are not artifacts of sampling variability, model specification, or data partitioning. Overall, this study demonstrates that explainable machine learning can characterize the temporal evolution of feature importance, providing a robust analytical framework for investigating long-term changes in cultural data.
