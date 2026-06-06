---
title: "Survival Analysis-Powered AI in Risk-Aware Data-Driven Multi-Objective Optimization for Geological CO2 Storage"
authors: "A. Gurwicz, A. C. A. Abreu, D. H. Gutman, E. Gildin, M. A. C. Pacheco"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-06-03T06:09:45.241449"
doi: "https://doi.org/10.2118/231654-ms"
openalex_id: "https://openalex.org/W7163040741"
source_api: "openalex"
---

# Survival Analysis-Powered AI in Risk-Aware Data-Driven Multi-Objective Optimization for Geological CO2 Storage

**著者**: A. Gurwicz, A. C. A. Abreu, D. H. Gutman, E. Gildin, M. A. C. Pacheco
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Summary We construct the first AI-driven, survival analysis-backed optimization models for CCS that simultaneously determine optimal injection strategies while minimizing long-term environmental and safety risk. These procedures necessitate expensive, full-physics reservoir simulations due to the need to accurately model CO2 migration over centuries-long monitoring spans. To ensure tractability in the stochastic optimizations proposed, we employ a recently developed class of simulator surrogates powered by survival analysis-driven AI, enjoying benefits such as computational efficiency and feature sparsity. We explore the state-of-the-art in AI-based, multi-objective, gradient-free optimization by leveraging the NSGA-II genetic algorithm to maximize CO2 injection volume over an initial sequestration period while minimizing long-term leakage risk. Training a survival analysis-based surrogate in the offline stage, we enable rapid objective evaluation and ensure effective exploration of the optimization solution domain. Survival analysis uniquely leverages the phenomenon of data censorship, reducing the simulation horizon required for training. We draw from the literature to evaluate the proposed methodology with a case study of permanent storage in a saline aquifer, optimizing volume allocation while minimizing leakage risk. The synthetic, compositional simulation model has four CO2 injectors and five pressure-maintenance producers, and accounts for uncertainty through permeability realizations generated via the Dykstra-Parsons coefficient. The survival analysis-based surrogate for time-to-leakage displays low errors, with training times of just seconds on personal computers. We verify the performance of NSGA-II, empirically observed to achieve good results in reservoir optimization, using both the simulator and the surrogate model. The framework effectively explored the feasible region and yielded solutions that increase operational efficiency while successfully avoiding failure. This is the first work to integrate survival analysis-driven AI into optimization methodologies, pushing their boundaries in real-world challenges. We leverage these unique machine learning models to propose a novel framework that yields risk-optimized solutions for safe and efficient injection and reservoir control. This addresses the need for optimal, long-term risk-guided decision-making in CO2 storage projects without compromising on accuracy or efficiency, further establishing AI as a cornerstone for advancing CCS viability in the energy industry.
