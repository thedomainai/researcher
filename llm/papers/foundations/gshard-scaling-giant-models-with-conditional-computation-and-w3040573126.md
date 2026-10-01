---
title: "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding"
authors: ["Dmitry Lepikhin", "HyoukJoong Lee", "Yuanzhong Xu", "Dehao Chen", "Orhan Fırat", "Yanping Huang", "Maxim Krikun", "Noam Shazeer", "et al."]
year: 2020
cited_by_count: 351
doi: "https://doi.org/10.48550/arxiv.2006.16668"
openalex_id: W3040573126
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

**Authors**: Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Fırat, Yanping Huang, Maxim Krikun, Noam Shazeer, et al. | **Year**: 2020 | **Cited by**: 351 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Neural network scaling has been critical for improving the model quality in many real-world machine learning applications with vast amounts of training data and compute. Although this trend of scaling is affirmed to be a sure-fire approach for better model quality, there are challenges on the path such as the computation cost, ease of programming, and efficient implementation on parallel devices. GShard is a module composed of a set of lightweight annotation APIs and an extension to the XLA compiler. It provides an elegant way to express a wide range of parallel computation patterns with minimal changes to the existing model code. GShard enabled us to scale up multilingual neural machine translation Transformer model with Sparsely-Gated Mixture-of-Experts beyond 600 billion parameters using automatic sharding. We demonstrate that such a giant model can efficiently be trained on 2048 TPU v3 accelerators in 4 days to achieve far superior quality for translation from 100 languages to English compared to the prior art.
