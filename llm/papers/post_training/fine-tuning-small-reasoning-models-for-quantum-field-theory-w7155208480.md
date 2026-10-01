---
title: "Fine-tuning small reasoning models for quantum field theory"
authors: ["Nathaniel Sherlock Woodward", "Zhiqi Gao", "Yurii Kvasiuk", "Kendrick M. Smith", "Frederic Sala", "Moritz Münchmeyer"]
year: 2026
cited_by_count: 0
doi: "https://doi.org/10.1088/2632-2153/aea39e"
openalex_id: W7155208480
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Fine-tuning small reasoning models for quantum field theory

**Authors**: Nathaniel Sherlock Woodward, Zhiqi Gao, Yurii Kvasiuk, Kendrick M. Smith, Frederic Sala, Moritz Münchmeyer | **Year**: 2026 | **Cited by**: 0 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Abstract Despite the growing application of large language models (LLMs) to theoretical physics, there has been little academic exploration of how domain-specific physics reasoning ability develops during training. To investigate this, we perform the first academic comparison of reinforcement learning and supervised fine-tuning for LLMs on verifiable problem-solving tasks in theoretical physics. Because the open-source verifiable training data required to develop such capabilities is scarce, we built a robust data generation pipeline that can both create synthetic problems and make existing human-authored problems suitable for model training. Selecting quantum field theory (QFT) as our primary domain, we generated over 2,500 synthetic problems alongside a curated collection of human-adapted problems sourced from arXiv and standard pedagogical resources. We conduct both reinforcement learning (RL) and supervised fine-tuning (SFT) experiments, benchmarking performance gains as well as generalization to other physics domains. Although both methods improve over the base model on every dataset, SFT gains are concentrated on in-distribution synthetic tasks, while RL generalizes better, outperforming SFT on the human-adapted datasets and TPBench. We perform an extensive analysis of model chain-of-thought (CoT) reasoning before and after fine-tuning to understand how reasoning errors evolve during RL and SFT. Finally, we publicly release our data pipeline, verifiable QFT training data, and ~200M tokens of QFT reasoning traces.
