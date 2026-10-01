---
title: "Constitutional AI: Harmlessness from AI Feedback"
authors: ["Yuntao Bai", "Saurav Kadavath", "Sandipan Kundu", "Amanda Askell", "John Kernion", "Andy Jones", "A. Chen", "Anna Goldie", "et al."]
year: 2022
cited_by_count: 3750
doi: null
openalex_id: arxiv-2212.08073
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "semantic_scholar"
---

# Constitutional AI: Harmlessness from AI Feedback

**Authors**: Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, John Kernion, Andy Jones, A. Chen, Anna Goldie, et al. | **Year**: 2022 | **Cited by**: 3750 | **Kind**: article | **Relevance**: post_training: core

## Abstract

As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.
