---
title: "Agentic Discovery of Cryomicroneedle Formulations"
authors: "Hui Li, Lifu Du, Nurul Hameed, Shemonti Saha Authai, Zlata Stefanovic"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-05-21T06:13:02.842188"
doi: "https://doi.org/10.65215/ltspreprints.2026.05.19.000248"
openalex_id: "https://openalex.org/W7161682167"
source_api: "openalex"
---

# Agentic Discovery of Cryomicroneedle Formulations

**著者**: Hui Li, Lifu Du, Nurul Hameed, Shemonti Saha Authai, Zlata Stefanovic
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Cryomicroneedles offer a route to minimally invasive intradermal delivery of living cells, but their cryogenic formulations must reconcile cell protection with constraints on toxicity and device fabrication. Here we report an AI-assisted, closed-loop workflow for cryomicroneedle cryoprotectant discovery that combines literature curation, Gaussian-process surrogate modelling, Bayesian optimization, and sequential wet-lab validation. A curated dataset of 198 mesenchymal stem-cell cryopreservation formulations from 42 studies was converted into 21 ingredient features and used to train an uncertainty-aware literature prior. This model captured moderate structure in the literature data but failed prospectively, motivating iterative wet-lab correction. Across ten validation iterations and 106 wet-lab observations, the model progressively adapted to cryomicroneedle-specific outcomes: batch RMSE decreased from 41.21 to 6.86 percentage points, later-stage rank correlations became consistently positive, and the cumulative wet-lab predicted-versus-measured summary reached R2 = 0.942. The best validated formulation achieved 95.15% post-thaw viability with low DMSO, ectoin, ethylene glycol, and fetal bovine serum. However, high viability alone did not ensure intact cryomicroneedle formation, highlighting the need for future multi-objective optimization. These results demonstrate that agent-assisted computational infrastructure can make data-efficient formulation discovery more accessible to labs with minimal data expertise in-house. Project code is available at https://github.com/baitmeister/ML-for-CryoMN.
