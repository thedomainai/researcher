---
title: "RecRanker: Instruction Tuning Large Language Model as Ranker for Top-k Recommendation"
authors: ["Sichun Luo", "Bowei He", "Haohan Zhao", "Wei Shao", "Yanlin Qi", "Yinya Huang", "Aojun Zhou", "Yuxuan Yao", "et al."]
year: 2024
cited_by_count: 23
doi: "https://doi.org/10.1145/3705728"
openalex_id: W4404856308
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# RecRanker: Instruction Tuning Large Language Model as Ranker for Top-k Recommendation

**Authors**: Sichun Luo, Bowei He, Haohan Zhao, Wei Shao, Yanlin Qi, Yinya Huang, Aojun Zhou, Yuxuan Yao, et al. | **Year**: 2024 | **Cited by**: 23 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Large language models (LLMs) have demonstrated remarkable capabilities and have been extensively deployed across various domains, including recommender systems. Prior research has employed specialized prompts to leverage the in-context learning capabilities of LLMs for recommendation purposes. More recent studies have utilized instruction tuning techniques to align LLMs with human preferences, promising more effective recommendations. However, existing methods suffer from several limitations. The full potential of LLMs is not fully elicited due to low-quality tuning data and the overlooked integration of conventional recommender signals. Furthermore, LLMs may generate inconsistent responses for different ranking tasks in the recommendation, potentially leading to unreliable results. In this article, we introduce Ranker for top- k Recommendations (RecRanker), tailored for instruction tuning LLMs to serve as the Ranker for top- k Recommendations. Specifically, we introduce importance-aware sampling, clustering-based sampling, and penalty for repetitive sampling for sampling high-quality, representative, and diverse training data. To enhance the prompt, we introduce a position shifting strategy to mitigate position bias and augment the prompt with auxiliary information from conventional recommendation models, thereby enriching the contextual understanding of the LLM. Subsequently, we utilize the sampled data to assemble an instruction-tuning dataset with the augmented prompts comprising three distinct ranking tasks: pointwise, pairwise, and listwise rankings. We further propose a hybrid ranking method to enhance the model performance by ensembling these ranking tasks. Our empirical evaluations demonstrate the effectiveness of our proposed RecRanker in both direct and sequential recommendation scenarios. 1
