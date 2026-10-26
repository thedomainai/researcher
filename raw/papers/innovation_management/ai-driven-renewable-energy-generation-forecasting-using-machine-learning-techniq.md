---
title: "AI-driven Renewable Energy Generation Forecasting Using Machine Learning Techniques"
authors: "Arathi H L, Sinchana C S, Partha C M, Shobha N, Shreya K S"
year: 2026
citations: 0
paper_type: "primary"
domain: "innovation_management"
fetched: "2026-10-27T06:04:51.363649"
doi: "https://doi.org/10.17148/ijarcce.2026.151087"
openalex_id: "https://openalex.org/W7223473378"
source_api: "openalex"
---

# AI-driven Renewable Energy Generation Forecasting Using Machine Learning Techniques

**著者**: Arathi H L, Sinchana C S, Partha C M, Shobha N, Shreya K S
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: イノベーション管理

## Abstract

Short-term forecasting of solar and wind generation is a prerequisite for economical plant operation, yet most reported machine-learning studies conclude at a table of error values computed on stored datasets.In earlier work the present authors reviewed five recent studies, identified six practical deficiencies, and proposed a five-layer forecasting framework; no implementation or measured result was reported at that stage.This paper reports the construction and quantitative evaluation of that framework as a working system.A web application was developed in which the browser Geolocation API and a public meteorological service supply the four environmental parameters used by the models, removing manual data entry.Four regression algorithms-linear regression, a decision tree, a random forest, and support vector regression-were trained separately for solar and wind output on a 5,922-record physics-based reference dataset and compared under identical conditions.On a 1,185-record held-out partition the selected solar model (support vector regression) attained MAE 1.340 kWh, RMSE 1.795 kWh and R² 0.9940, and the selected wind model (random forest) attained MAE 1.484 kWh, RMSE 1.932 kWh and R² 0.9939, for a reference plant rated at 100 kW per source.Linear regression proved adequate for solar output (R² 0.9930) but failed for wind (R² 0.8375); the discrepancy is traced to the piecewise-cubic turbine power curve.Residual analysis shows that the non-linear models operate at the injected noise floor of the reference data, so differences among them are not statistically meaningful, and permutation importance recovers the dominant physical driver of each source.Of the six deficiencies previously identified, three are closed, one is partially addressed, and two remain open.Because the reference dataset is synthetic, the reported accuracy characterises model capacity and pipeline correctness rather than field performance.
