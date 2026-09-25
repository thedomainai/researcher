---
title: "The Unfairness of Multifactorial Bias in Recommendation"
authors: "Masoud Mansoury, Jin Huang, Mykola Pechenizkiy, Herke van Hoof, Maarten de Rijke"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-08-22T15:47:42.148428"
doi: "https://doi.org/10.1145/3841477"
openalex_id: "https://openalex.org/W7125104682"
source_api: "openalex"
---

# The Unfairness of Multifactorial Bias in Recommendation

**著者**: Masoud Mansoury, Jin Huang, Mykola Pechenizkiy, Herke van Hoof, Maarten de Rijke
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Popularity bias and positivity bias are two prominent sources of bias in recommender systems. Both arise from input data, propagate through recommendation models, and lead to unfair or suboptimal outcomes. Popularity bias occurs when a small subset of items receives most interactions, while positivity bias stems from the over-representation of high rating values. Although each bias has been studied independently, their combined effect , to which we refer to as multifactorial bias , remains underexplored. In this work, we examine how multifactorial bias influences item-side fairness, focusing on exposure bias, which reflects the unequal visibility of items in recommendation outputs. Through simulation studies, we find that positivity bias is disproportionately concentrated on popular items, further amplifying their over-exposure. Motivated by this insight, we adapt a percentile-based rating transformation as a pre-processing strategy to mitigate multifactorial bias. Experiments using six recommendation algorithms across four public datasets show that this approach improves exposure fairness with negligible accuracy loss. We also demonstrate that integrating this pre-processing step into post-processing fairness pipelines enhances their effectiveness and efficiency, enabling comparable or better fairness with reduced computational cost. These findings highlight the importance of addressing multifactorial bias and demonstrate the practical value of simple, data-driven pre-processing methods for improving fairness in recommender systems.
