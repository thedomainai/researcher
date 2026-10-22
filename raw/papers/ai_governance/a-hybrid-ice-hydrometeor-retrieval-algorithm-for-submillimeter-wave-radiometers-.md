---
title: "A hybrid ice hydrometeor retrieval algorithm for submillimeter-wave radiometers in support of the PolSIR and PMM missions"
authors: "Yuli Liu, Jie Gong, Ian Stuart Adams, Rachael A. Kroodsma, Ruiyao Chen"
year: 2026
citations: 1
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-10-23T08:08:50.133539"
doi: "https://doi.org/10.5194/amt-19-6661-2026"
openalex_id: "https://openalex.org/W7151974708"
source_api: "openalex"
---

# A hybrid ice hydrometeor retrieval algorithm for submillimeter-wave radiometers in support of the PolSIR and PMM missions

**著者**: Yuli Liu, Jie Gong, Ian Stuart Adams, Rachael A. Kroodsma, Ruiyao Chen
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Abstract. This paper presents an ice hydrometeor retrieval algorithm for submillimeter-wave radiometers in support of the upcoming PolSIR (Polarized Submillimeter Ice Cloud Radiometer) and PMM (Precipitation Measuring Mission) satellite missions. The algorithm employs a hybrid Bayesian Monte Carlo Integration (BMCI) and Optimal Estimation Method (OEM) approach, which leverages the strengths of the BMCI method but extends the retrieval capability beyond the limitations of the a priori database when BMCI alone fails to identify enough database cases matching the observations. To address the highly non-Gaussian nature of the a priori statistics, a method using cumulative distribution functions (CDFs) and empirical orthogonal functions (EOFs) is applied to enable effective implementation of the OEM algorithm. With the CDFs/EOFs method, the OEM can maximize the posterior probability density function using the a priori constraint that is largely consistent with that used in the BMCI step, ensuring that the entire retrieval operates under a nearly uniform prior constraint. The algorithm is first applied to evaluate the PMM-C2OMODO (Convective Core Observations through MicrOwave Derivatives in the trOpics) radiometer using simulated observations. Retrieval accuracies for key microphysical parameters are presented. Also, the retrieval diagnostics, including the vertical resolution, Degrees of Freedom (DoF), and Shannon information content, are analyzed. The algorithm is further applied to real CoSSIR (Configurable Scanning Submillimeter-wave Instrument/Radiometer) observations during the IMPACTS (Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms) campaign, and the results are evaluated against the collocated triple-frequency radar retrievals from CRS (Cloud Radar System) and HIWARP (High-altitude Imaging Wind & Rain Airborne Profiler) observations. Multiple ice particle habits are examined, and both layer-resolved and column-integrated mass and size parameters are evaluated. Both simulated experiments and real-observation retrievals demonstrate that the hybrid BMCI-OEM method is highly effective in reducing simulated and observed brightness temperature (TB) discrepancies. With an appropriate selection of ice cloud particle habits, the TB simulations closely reproduce the observations. Using the logarithmic difference as the quantitative metric, the CoSSIR-retrieved ice water content, layer-resolved particle diameter, ice water path, and column-averaged mean mass diameter with the hybrid BMCI–OEM algorithm differ from triple-frequency radar retrievals by 3.75, 0.82, 2.53, and 0.55 dB, respectively, representing reductions of 0.21, 0.02, 0.85, and 0.13 dB relative to BMCI-only retrievals. The hybrid Bayesian framework also demonstrates high extensibility to other remote-sensing observations. As more information becomes available through multi-sensor integration or the use of hyperspectral measurements, the hybrid Bayesian algorithm shows increasing potential to better constrain cloud microphysical properties.
