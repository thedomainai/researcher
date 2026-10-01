---
title: "Enhancing Auditory Reasoning in Large Audio–Language Models Via Supervised Fine-Tuning and Reinforcement Learning With Verifiable Rewards"
authors: ["Jian Wang", "Shengyan Hao"]
year: 2026
cited_by_count: 0
doi: "https://doi.org/10.1109/access.2026.3728498"
openalex_id: W7204964929
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Enhancing Auditory Reasoning in Large Audio–Language Models Via Supervised Fine-Tuning and Reinforcement Learning With Verifiable Rewards

**Authors**: Jian Wang, Shengyan Hao | **Year**: 2026 | **Cited by**: 0 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

The objective of this paper is to improve and analyze auditory reasoning in large audio–language models for audio question answering (AQA), where a model must infer the correct answer from acoustic evidence and textual answer options. Although reinforcement learning (RL) with verifiable rewards has recently improved reasoning alignment in text and vision tasks, its role in audio remains underexplored because auditory inputs involve temporal structure, perceptual ambiguity, and signal-grounded decision making. To address this gap, we propose a two-stage training framework built on Qwen2.5-Omni-7B. The first stage performs supervised fine-tuning (SFT) on AQA data to establish task alignment and factual grounding from acoustic cues, and the second stage applies Group Relative Policy Optimization (GRPO) with verifiable rewards to directly refine answer correctness and output behavior. On the MMAU Test-mini benchmark, the proposed SFT+GRPO framework achieves the highest average accuracy among the compared methods, reaching 78.87% and outperforming the SFT-only and GRPO-only variants. Further analyses of training stages, RL objectives, reward design, data efficiency, and prompt formats suggest that verifier-guided implicit reasoning is more effective than enforcing long explicit reasoning traces in this AQA setting. These findings suggest that auditory reasoning can benefit from training strategies tailored to audio signals and objective answer verification, and they provide empirical evidence for applying RLVR to large audio–language models.
