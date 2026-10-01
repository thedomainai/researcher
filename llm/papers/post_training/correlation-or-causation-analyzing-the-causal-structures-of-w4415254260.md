---
title: "Correlation or Causation: Analyzing the Causal Structures of LLM and LRM Reasoning Process"
authors: ["Zhizhang Fu", "Guangsheng Bao", "Hongbo Zhang", "Chenkai Hu", "Yue Zhang"]
year: 2026
cited_by_count: 1
doi: "https://doi.org/10.1109/taslpro.2026.3688949"
openalex_id: W4415254260
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Correlation or Causation: Analyzing the Causal Structures of LLM and LRM Reasoning Process

**Authors**: Zhizhang Fu, Guangsheng Bao, Hongbo Zhang, Chenkai Hu, Yue Zhang | **Year**: 2026 | **Cited by**: 1 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

LLMs suffer from critical reasoning issues such as unfaithfulness, bias, and inconsistency, since they lack robust causal underpinnings and may rely on superficial correlations rather than genuine understanding. Successive LRMs have emerged as a promising alternative, leveraging advanced training techniques such as reinforcement learning (RL) and distillation to improve task accuracy. However, the impact of these training methods on causality remains largely unexplored. In this study, we conduct a systematic causal analysis on LLMs and LRMs, examining structural causal models (SCMs) of four key variables: problem instruction (Z), thinking process (T), reasoning steps (X), and answer (Y). Our findings reveal that RLVR-trained LRMs exhibit enhanced causal reasoning capabilities, aligning more closely with ideal causal structures, while LLMs and distilled LRMs fail to address causality-related deficiencies. Our further investigation indicates that RLVR reduces spurious correlations and strengthens genuine causal patterns, thereby mitigating unfaithfulness and bias. In addition, our inspection on the dynamics of the RLVR training process observes a high correlation between reduced spurious features and improved causal structures, where the causal relationships consistently improve in the training process. This study contributes to the understanding of causality in reasoning models, highlights the critical role of RLVR in enhancing causal reasoning, and provides insights for designing future AI systems with stronger causal foundations. We release our code and data at https://github.com/Harryking1999/CoT_Causal_Analysis.
