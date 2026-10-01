---
title: "The relationship between reasoning and performance in large language models—o3 (mini) thinks harder, not longer"
authors: ["Marthe Ballon", "Andres Algaba", "Vincent Ginis"]
year: 2026
cited_by_count: 6
doi: "https://doi.org/10.1038/s41598-026-50923-2"
openalex_id: W7160398065
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# The relationship between reasoning and performance in large language models—o3 (mini) thinks harder, not longer

**Authors**: Marthe Ballon, Andres Algaba, Vincent Ginis | **Year**: 2026 | **Cited by**: 6 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Large language models have demonstrated remarkable progress in mathematical reasoning, leveraging chain-of-thought and reinforcement learning. However, many open questions remain regarding the interplay between reasoning token usage and accuracy gains. In particular, when comparing models across generations, it is unclear whether improved performance results from longer reasoning chains or more effective reasoning. We systematically analyze reasoning chain length across o1-mini and o3-mini variants on the Omni-MATH benchmark, finding that o3-mini (m) achieves superior accuracy without requiring longer reasoning chains than o1-mini. Moreover, we show that accuracy generally declines as reasoning chains grow across all models and compute settings, even when controlling for difficulty of the questions. This accuracy drop is significantly smaller in more proficient models, suggesting that new generations of reasoning models use test-time compute more effectively. Finally, we highlight that while o3-mini (h) achieves a marginal accuracy gain over o3-mini (m), it does so by allocating substantially more reasoning tokens across all problems, even the ones that o3-mini (m) can already solve. These findings provide new insights into the relationship between model capability and reasoning length, with implications for efficiency, scaling, and evaluation methodologies.
