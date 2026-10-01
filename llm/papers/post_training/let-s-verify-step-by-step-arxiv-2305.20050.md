---
title: "Let's Verify Step by Step"
authors: ["H. Lightman", "V. Kosaraju", "Yura Burda", "Harrison Edwards", "Bowen Baker", "Teddy Lee", "Jan Leike", "John D. Schulman", "et al."]
year: 2023
cited_by_count: 4647
doi: null
openalex_id: arxiv-2305.20050
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "semantic_scholar"
---

# Let's Verify Step by Step

**Authors**: H. Lightman, V. Kosaraju, Yura Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John D. Schulman, et al. | **Year**: 2023 | **Cited by**: 4647 | **Kind**: article | **Relevance**: post_training: core

## Abstract

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.
