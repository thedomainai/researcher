---
title: "Reward modeling for mitigating toxicity in transformer-based language models"
authors: ["Farshid Faal", "Ketra Schmitt", "Jie Yu"]
year: 2022
cited_by_count: 28
doi: "https://doi.org/10.1007/s10489-022-03944-z"
openalex_id: W4225817241
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "semantic_scholar"
---

# Reward modeling for mitigating toxicity in transformer-based language models

**Authors**: Farshid Faal, Ketra Schmitt, Jie Yu | **Year**: 2022 | **Cited by**: 28 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Transformer-based language models can generate fluent text and be efficiently adapted across various natural language generation tasks. However, language models that are pretrained on large unlabeled web text corpora have been shown to suffer from degenerating toxic content and social bias behaviors, consequently hindering their safe deployment. Various detoxification methods have been proposed to mitigate language model toxicity; however, these methods struggle to detoxify language models when conditioned on prompts that contain specific social identities related to gender, race, or religion. In this study, we propose Reinforce-Detoxify, a reinforcement learning-based method for mitigating toxicity in language models. We address the challenge of safety in language models and propose a new reward model that can detect toxic content and mitigate unintended bias towards social identities in toxicity prediction. The experiments demonstrate that the Reinforce-Detoxify method for language model detoxification outperforms existing detoxification approaches in automatic evaluation metrics, indicating that our approach in language model detoxification is less prone to unintended bias toward social identities in generated content.
