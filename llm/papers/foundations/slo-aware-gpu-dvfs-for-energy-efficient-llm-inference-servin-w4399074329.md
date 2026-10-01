---
title: "SLO-Aware GPU DVFS for Energy-Efficient LLM Inference Serving"
authors: ["Andreas Kosmas Kakolyris", "Dimosthenis Masouros", "Sotirios Xydis", "Dimitrios Soudris"]
year: 2024
cited_by_count: 41
doi: "https://doi.org/10.1109/lca.2024.3406038"
openalex_id: W4399074329
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# SLO-Aware GPU DVFS for Energy-Efficient LLM Inference Serving

**Authors**: Andreas Kosmas Kakolyris, Dimosthenis Masouros, Sotirios Xydis, Dimitrios Soudris | **Year**: 2024 | **Cited by**: 41 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

The increasing popularity of LLM-based chatbots combined with their reliance on power-hungry GPU infrastructure forms a critical challenge for providers: minimizing energy consumption under Service-Level Objectives (SLOs) that ensure optimal user experience. Traditional energy optimization methods fall short for LLM inference due to their autoregressive architecture, which renders them incapable of meeting a predefined SLO withoutenergy overprovisioning. This autoregressive nature however, allows for iteration-level adjustments, enabling continuous fine-tuning of the system throughout the inference process. In this letter, we propose a solution based on iteration-level GPU Dynamic Voltage Frequency Scaling (DVFS), aiming to reduce the energy impact of LLM serving, an approach that has the potential for more than$22.8\%$and up to$45.5\%$energy gains when tested in real world situations under varying SLO constraints. Our approach works on top of existing LLM hosting services, requires minimal profiling and no intervention to the inference serving system.
