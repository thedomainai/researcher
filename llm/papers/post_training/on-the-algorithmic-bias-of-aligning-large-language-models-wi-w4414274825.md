---
title: "On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization"
authors: ["Jiancong Xiao", "Ziniu Li", "Xingyu Xie", "Emily Getzen", "Cong Fang", "Qi Long", "Weijie Su"]
year: 2025
cited_by_count: 11
doi: "https://doi.org/10.1080/01621459.2025.2555067"
openalex_id: W4414274825
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization

**Authors**: Jiancong Xiao, Ziniu Li, Xingyu Xie, Emily Getzen, Cong Fang, Qi Long, Weijie Su | **Year**: 2025 | **Cited by**: 11 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Accurately aligning large language models (LLMs) with human preferences is crucial for informing fair, economically sound, and statistically efficient decision-making processes. However, we argue that the predominant approach for aligning LLMs with human preferences through a reward model—reinforcement learning from human feedback (RLHF)—suffers from an inherent algorithmic bias due to its Kullback–Leibler-based regularization in optimization. In extreme cases, this bias could lead to a phenomenon we term preference collapse, where minority preferences are virtually disregarded. To mitigate this algorithmic bias, we introduce preference matching (PM) RLHF, a novel approach that provably aligns LLMs with the preference distribution of the reward model under the Bradley–Terry–Luce/Plackett–Luce model. Central to our approach is a PM regularizer that takes the form of the negative logarithm of the LLM’s policy probability distribution over responses, which helps the LLM balance response diversification and reward maximization. Notably, we obtain this regularizer by solving an ordinary differential equation that is necessary for the PM property. For practical implementation, we introduce a conditional variant of PM RLHF that is tailored to natural language generation. Finally, we empirically validate the effectiveness of conditional PM RLHF through experiments on the OPT and Llama-family models, demonstrating a 29% to 41% improvement in alignment with human preferences, as measured by a certain metric, compared to standard RLHF.
