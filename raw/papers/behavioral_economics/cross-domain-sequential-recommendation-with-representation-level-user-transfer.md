---
title: "Cross-Domain Sequential Recommendation with Representation-Level User Transfer"
authors: "Abdulaziz Samra, Nikita Sukhorukov, Alexey Grishanov, Alexey Vasilev, Evgeny Frolov"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "behavioral_economics"
fetched: "2026-11-04T06:27:29.191519"
doi: "https://doi.org/10.1145/3799682.3841135"
openalex_id: "https://openalex.org/W7224017649"
source_api: "openalex"
---

# Cross-Domain Sequential Recommendation with Representation-Level User Transfer

**著者**: Abdulaziz Samra, Nikita Sukhorukov, Alexey Grishanov, Alexey Vasilev, Evgeny Frolov
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: 行動経済学

## Abstract

Cross-domain sequential recommendation aims to improve next-item prediction in a target domain by leveraging user behavior from auxiliary source domains. However, real-world deployment faces two critical challenges: business constraints that isolate interaction data across domains, and user heterogeneity, where many users lack cross-domain activity. This makes existing cross-domain methods difficult to apply. In this paper, we propose a simple and practical framework for cross-domain sequential recommendations that transfers information exclusively through learned user representations, without sharing raw interaction data or item embeddings across domains. We introduce a lightweight adapter that projects the source-domain user representation into the target-domain embedding space and integrates it with the target interaction sequence. Importantly, when source data is unavailable (i.e., the user observed only in the target domain), the model seamlessly defaults to a robust target-only sequential recommender, retaining benefits from joint training across all users. Extensive experiments were conducted under two setups; one targets benchmarking against previous baselines, while the other focuses on realistic and scalable conditions. Both sets of experiments demonstrate consistent performance gains for shared and unshared users.
