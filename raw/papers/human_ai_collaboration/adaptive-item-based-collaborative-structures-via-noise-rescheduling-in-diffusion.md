---
title: "Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion for Generative Recommendation"
authors: "Jiaqi Wang, Tianying Liu, Heng Chang, Jihong Guan, Wengen Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-08-25T18:32:03.977255"
arxiv_id: "http://arxiv.org/abs/2608.23400v1"
source_api: "arxiv"
categories: "cs.IR, cs.AI"
---

# Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion for Generative Recommendation

**著者**: Jiaqi Wang, Tianying Liu, Heng Chang, Jihong Guan, Wengen Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Discrete Diffusion Models (DDMs) have recently been introduced to recommendation systems, modeling user history as a token generation process via iterative denoising. However, while effective at capturing user-level sequential patterns, these methods often fail to explicitly integrate item-based collaborative filtering information, a critical component for accurate recommendation. This deficiency manifests in two key aspects: (1) the item representation is often semantic-focused, lacking collaborative priors for diffusion training; and (2) the denoising process employs a uniform noise schedule, treating all tokens indiscriminately and ignoring item-level adaptive structural dependencies. To bridge this gap, we propose ANR-DiffRec, a unified framework designed to encode item-based collaborative structures into discrete diffusion for generative recommendation. First, we explicitly incorporate an item co-occurrence matrix to guide semantic ID generation, providing a structured collaborative prior for discrete diffusion training. Second, we introduce an item-based adaptive noise rescheduling mechanism that dynamically adjusts denoising weights according to both local contextual recoverability and behavior-aware item dependencies. Specifically, the proposed strategy jointly models intra-item structural context and inter-item collaborative signals, enabling structure-aware denoising during diffusion training. Extensive experiments on multiple benchmarks demonstrate that our method consistently outperforms state-of-the-art generative recommendation models. Code: https://github.com/CalmaQi/ANR-DiffRec.
