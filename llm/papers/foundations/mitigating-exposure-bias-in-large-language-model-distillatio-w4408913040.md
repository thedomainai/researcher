---
title: "Mitigating exposure bias in large language model distillation: an imitation learning approach"
authors: ["Andrea Pozzi", "Alessandro Incremona", "Daniele Tessera", "Daniele Toti"]
year: 2025
cited_by_count: 28
doi: "https://doi.org/10.1007/s00521-025-11162-0"
openalex_id: W4408913040
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Mitigating exposure bias in large language model distillation: an imitation learning approach

**Authors**: Andrea Pozzi, Alessandro Incremona, Daniele Tessera, Daniele Toti | **Year**: 2025 | **Cited by**: 28 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Abstract Knowledge distillation is recognized as a valuable model compression strategy that alleviates the computational burden of large language models while preserving performance. This strategy involves training a smaller model utilizing both real data and predictions from a more cumbersome model. Traditional distillation methods, however, are often compromised by exposure bias, which results from reliance on next-step prediction training loss. This bias emerges when models are tested in free-running mode, differing from their training regime and leading to a progressive drift in input distributions between testing and training phases. An analogous issue, known as ‘distributional shift’, has been effectively addressed in imitation learning through various methodologies. Therefore, this paper specifically tailors an imitation learning-based solution to a traditional knowledge distillation framework which inherently considers both real data and the teacher’s predictions as dual sources of expert demonstrations. The effectiveness of this approach is demonstrated over five different test datasets, where it outperforms traditional benchmarks across all evaluation metrics. Specifically, it achieves superior results in perplexity, multi-token generation, and G-Eval score, indicating improvements in both predictive accuracy and alignment with human judgment in text quality. These results underscore the potential of this approach to effectively address exposure bias in large language model distillation.
