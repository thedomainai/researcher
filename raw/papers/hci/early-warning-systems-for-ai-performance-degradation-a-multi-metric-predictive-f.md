---
title: "Early Warning Systems for AI Performance Degradation: A Multi Metric Predictive Framework"
authors: "Shaymaa Kaseb Layus"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-11-01T06:26:05.612889"
doi: "https://doi.org/10.25195/ijci.v52i2.756"
openalex_id: "https://openalex.org/W7224773743"
source_api: "openalex"
---

# Early Warning Systems for AI Performance Degradation: A Multi Metric Predictive Framework

**著者**: Shaymaa Kaseb Layus
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

The extensive use of artificial intelligence systems in manufacturing settings has posed significant pressure on ensuring the sustainability of performance in the long term. Although the development of models has improved, AI systems are still vulnerable to slow performance decline due to data drift, changes in concepts, and resource variability, which can silently build up until major failures happen. Nevertheless, the current monitoring methods are restricted by the use of a single metric assessment, use of reactive threshold-based warning systems and also being reliant on labeled data, which are inadequate in early and reliable detection of degradation. To overcome these shortcomings, the following paper will suggest a multi-metric predictive early warning framework to detect and predict AI performance degradation at an early stage. The suggested system will combine ten metrics of heterogeneous performances such as predictive accuracy, operational efficiency, resource usage, and statistical drift signals in a single monitoring architecture. More complex feature engineering algorithms are used to detect acute anomalies and long-term degradation trends, including rolling statistics and rate-of-change analysis, spectral decomposition. The framework is a combination of various complementary detection techniques, such as statistical process control, cumulative sum (CUSUM), exponentially weighted moving averages (EWMA), changepoint detection, and multivariate anomaly detection, to produce a composite warning index with graduated alert levels. Moreover, a predictive component predicts system health, and assists in planning interventions proactively. The framework is confirmed by large-scale simulation experiments with realistic degradation curves, periodically varying, and stochastic noise behavior in production AI systems. Findings indicate that the suggested method identifies degradation on average 14.3 days before approaching critical levels. It has a good discriminative performance with AUC = 0.89, whereas at the warning threshold (0.6) it has a true positive rate of 84.7% and a false positive rate of 8.9% and at the critical threshold (0.8), its true positive rate is 91.2% and false positive rate is 12.3% respectively. Moreover, the system has shown good anomaly detection performance with up to 94 percent of the abnormal events detected and can make accurate short-term prediction with a mean absolute error of 0.021 when forecasting one-day-ahead health index. Visual analytics dashboards and action-oriented decision-support outputs support the framework, increasing the interpretability and usefulness of the outputs in operations. On the whole, the suggested framework will provide a solid base of proactive and trustworthy AI performance tracking, allowing shifting towards the proactive and data-driven management of the system in a real-life deployment setting.
