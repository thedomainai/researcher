---
title: "MoE-LLaVA: Mixture of Experts for Large Vision-Language Models"
authors: ["Bin Lin", "Zhenyu Tang", "Yang Ye", "Jinfa Huang", "Junwu Zhang", "Yatian Pang", "Peng Jin", "Munan Ning", "et al."]
year: 2026
cited_by_count: 32
doi: "https://doi.org/10.1109/tmm.2026.3654458"
openalex_id: W7124471359
paper_type: article
evidence_kind: guideline
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# MoE-LLaVA: Mixture of Experts for Large Vision-Language Models

**Authors**: Bin Lin, Zhenyu Tang, Yang Ye, Jinfa Huang, Junwu Zhang, Yatian Pang, Peng Jin, Munan Ning, et al. | **Year**: 2026 | **Cited by**: 32 | **Kind**: guideline | **Relevance**: elicitation: supporting

## Abstract

Recently, remarkable progress has been made in scaling up Large Language Models (LLMs) through the use of the sparse Mixture-of-Expert (MoE) layers without significantly increasing computational cost. However, the transition from a pre-trained LLM to a sparse Large Vision-Language Model (LVLM) with MoE remains an open challenge. Directly fine-tuning an LLM to a sparse LVLM often leads to training collapse, characterized by (1) a large modality feature distribution gap and (2) expert load imbalance. This paper proposes a three-stage decoupled weight training process. In the first two stages, the model learns to adapt the LLM to an LVLM. In the third stage, the FFN weights from the second stage are used as lossless initialization for expert weights, effectively constructing a sparse model with a vast number of parameters while maintaining constant computational cost. Through extensive ablation experiments, we derive three empirical guidelines and propose a sparse LVLM termedMoE-LLaVA. MoE-LLaVA is a MoE-based sparse LVLM architecture, which uniquely activates only the top-$k$experts through routers during deployment, keeping the remaining experts inactive. Extensive experiments demonstrate that MoE-LLaVA outperforms LLaVA-1.5-7B with an average improvement of 4.6 across nine visual understanding benchmarks. Notably, with only 2.2B active parameters, our MoE-LLaVA shows comparable result with LLaVA-1.5-13B (87.0 vs. 85.9) on POPE benchmark. Our work establishes a baseline for sparse LVLMs and provides empirical guidelines for exploring the sparse LVLMs. Our code is available at:https://github.com/PKU-YuanGroup/MoE-LLaVA.
