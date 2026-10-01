---
title: "Mitigating Political Bias in Language Models through Reinforced Calibration"
authors: ["Ruibo Liu", "Chenyan Jia", "Jason Wei", "Guangxuan Xu", "Lili Wang", "Soroush Vosoughi"]
year: 2021
cited_by_count: 62
doi: "https://doi.org/10.1609/aaai.v35i17.17744"
openalex_id: W3158733382
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Mitigating Political Bias in Language Models through Reinforced Calibration

**Authors**: Ruibo Liu, Chenyan Jia, Jason Wei, Guangxuan Xu, Lili Wang, Soroush Vosoughi | **Year**: 2021 | **Cited by**: 62 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Current large-scale language models can be politically biased as a result of the data they are trained on, potentially causing serious problems when they are deployed in real-world settings. In this paper, we describe metrics for measuring political bias in GPT-2 generation and propose a reinforcement learning (RL) framework for mitigating political biases in generated text. By using rewards from word embeddings or a classifier, our RL framework guides debiased generation without having access to the training data or requiring the model to be retrained. In empirical experiments on three attributes sensitive to political bias (gender, location, and topic), our methods reduced bias according to both our metrics and human evaluation, while maintaining readability and semantic coherence.
