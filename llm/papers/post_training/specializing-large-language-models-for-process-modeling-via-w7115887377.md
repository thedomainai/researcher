---
title: "Specializing large language models for process modeling via reinforcement learning with verifiable and universal rewards"
authors: ["Alessandro Berti", "Xiaoting Wang", "Humam Kourani", "Wil M. P. Van der Aalst"]
year: 2025
cited_by_count: 1
doi: "https://doi.org/10.1007/s44311-025-00034-4"
openalex_id: W7115887377
paper_type: article
evidence_kind: guideline
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Specializing large language models for process modeling via reinforcement learning with verifiable and universal rewards

**Authors**: Alessandro Berti, Xiaoting Wang, Humam Kourani, Wil M. P. Van der Aalst | **Year**: 2025 | **Cited by**: 1 | **Kind**: guideline | **Relevance**: post_training: supporting

## Abstract

Abstract Process models are central artefacts in business process management: they drive analysis, automation, simulation, and compliance checking. Yet creating and maintaining high-quality models is labor-intensive and requires expertise in both the domain and formal notations such as Petri nets or BPMN. At the same time, many organisations already document their processes informally through textual work instructions, guidelines, and tickets. Automatically generating formal process models from such natural-language descriptions would therefore accelerate modeling, keep model repositories aligned with documentation, and provide stronger support for downstream uses such as conformance checking and digital twins. In this work, we study process model generation in a narrow, technical sense: given a textual process description, the model must produce a complete, executable process model. This generative capability can then be used both to propose models from scratch and as a building block for process modeling assistance and model completion. Large Language Models (LLMs) pretrained on generic text often struggle with this task, producing syntactically invalid or behaviorally incorrect process models. To address this limitation, we apply Reinforcement Learning (RL) to specialize a pretrained LLM specifically for process model generation. Our RL approach combines automatically verifiable rewards, based on structural checks and behavioral footprints, with universal judgments provided by an LLM-as-a-Judge. We created a dataset of 1312 textual process descriptions with corresponding reference models to support Supervised Fine-Tuning and RL. Experiments demonstrate that RL significantly reduces invalid model generations, improves behavioral correctness, and allows control over model complexity. On the ProMoAI benchmark, the resulting checkpoint approaches the performance of state-of-the-art proprietary models while producing fewer invalid generations.
