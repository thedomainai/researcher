---
title: "OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure"
authors: ["Jikai Wang", "Yi Su", "Juntao Li", "Qingrong Xia", "Zi Ye", "Xinyu Duan", "Zhefeng Wang", "Min Zhang"]
year: 2025
cited_by_count: 11
doi: "https://doi.org/10.1162/tacl_a_00735"
openalex_id: W4408105642
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure

**Authors**: Jikai Wang, Yi Su, Juntao Li, Qingrong Xia, Zi Ye, Xinyu Duan, Zhefeng Wang, Min Zhang | **Year**: 2025 | **Cited by**: 11 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Abstract Autoregressive language models demonstrate excellent performance in various scenarios. However, the inference efficiency is limited by its one-step-one-word generation mode, which has become a pressing problem recently as the models become increasingly larger. Speculative decoding employs a “draft and then verify” mechanism to allow multiple tokens to be generated in one step, realizing lossless acceleration. Existing methods mainly adopt fixed heuristic draft structures, which do not adapt to different situations to maximize the acceptance length during verification. To alleviate this dilemma, we propose OPT-Tree, an algorithm to construct adaptive and scalable draft trees, which can be applied to any autoregressive draft model. It searches the optimal tree structure that maximizes the mathematical expectation of the acceptance length in each decoding step. Experimental results reveal that OPT-Tree outperforms the existing draft structures and achieves a speed-up ratio of up to 3.2 compared with autoregressive decoding. If the draft model is powerful enough and the node budget is sufficient, it can generate more than ten tokens in a single step. Our code is available at https://github.com/Jikai0Wang/OPT-Tree.
