---
title: "LIMA: Less Is More for Alignment"
authors: ["Chunting Zhou", "Pengfei Liu", "Puxin Xu", "Srinivasan V. Iyer", "Jiao Sun", "Yuning Mao", "Xuezhe Ma", "Avia Efrat", "et al."]
year: 2023
cited_by_count: 128
doi: "https://doi.org/10.48550/arxiv.2305.11206"
openalex_id: W4377297670
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# LIMA: Less Is More for Alignment

**Authors**: Chunting Zhou, Pengfei Liu, Puxin Xu, Srinivasan V. Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, et al. | **Year**: 2023 | **Cited by**: 128 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Large language models are trained in two stages: (1) unsupervised pretraining from raw text, to learn general-purpose representations, and (2) large scale instruction tuning and reinforcement learning, to better align to end tasks and user preferences. We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling. LIMA demonstrates remarkably strong performance, learning to follow specific response formats from only a handful of examples in the training data, including complex queries that range from planning trip itineraries to speculating about alternate history. Moreover, the model tends to generalize well to unseen tasks that did not appear in the training data. In a controlled human study, responses from LIMA are either equivalent or strictly preferred to GPT-4 in 43% of cases; this statistic is as high as 58% when compared to Bard and 65% versus DaVinci003, which was trained with human feedback. Taken together, these results strongly suggest that almost all knowledge in large language models is learned during pretraining, and only limited instruction tuning data is necessary to teach models to produce high quality output.
