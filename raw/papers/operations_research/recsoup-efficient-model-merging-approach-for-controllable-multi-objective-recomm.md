---
title: "RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective Recommendation"
authors: "Zidong Jia, Guofu Xie, Xiao Zhang"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-04T06:55:05.364644"
doi: "https://doi.org/10.1145/3799682.3840938"
openalex_id: "https://openalex.org/W7222411049"
source_api: "openalex"
---

# RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective Recommendation

**著者**: Zidong Jia, Guofu Xie, Xiao Zhang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Recommender systems often need to balance multiple conflicting objectives. Controllable Multi-Objective Recommendation (CMOR) enables dynamic adjustment of objective trade-offs at inference time without retraining, adapting to shifting user or system requirements. Existing CMOR approaches typically rely on output-level reranking or parameter-generating modules, which either limit the scope of feasible trade-offs or incur substantial training and inference cost. Model merging provides a promising alternative by reusing multiple objective-specific models via parameter combination. However, its direct application to recommender systems is challenging due to the lack of a shared linear regime and cross-objective interference. To address these issues, we propose RecSoup, a lightweight two-stage approach for effective CMOR via specialized model merging. RecSoup first mitigates parameter interference across objectives through a pruning strategy that jointly considers objective-specific importance and cross-objective relevance. It then performs adaptive parameter merging via a learnable preference-to-coefficient mapping, allowing dynamic trade-off control at inference time without joint retraining or additional generative modules. Theoretically, we prove that RecSoup outperforms the parameter generation paradigm in effectiveness and efficiency, as it can fully navigate the Pareto front without smoothness constraints. Extensive experiments on multiple benchmarks demonstrate that RecSoup achieves improved Pareto front quality and effective controllability while delivers 165--228x faster inference-time latency than parameter generation approaches. Code is available at https://github.com/35798642/RECSOUP.git.
