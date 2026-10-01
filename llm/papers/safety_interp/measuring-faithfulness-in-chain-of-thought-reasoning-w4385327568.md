---
title: "Measuring Faithfulness in Chain-of-Thought Reasoning"
authors: ["Tamera Lanham", "Anna Chen", "Ansh Radhakrishnan", "Benoit Steiner", "Carson Denison", "Danny Hernandez", "Dustin Li", "Esin Durmus", "et al."]
year: 2023
cited_by_count: 32
doi: "https://doi.org/10.48550/arxiv.2307.13702"
openalex_id: W4385327568
paper_type: preprint
evidence_kind: article
topics: ["safety_interp"]
landmark: true
abstract_source: "openalex"
---

# Measuring Faithfulness in Chain-of-Thought Reasoning

**Authors**: Tamera Lanham, Anna Chen, Ansh Radhakrishnan, Benoit Steiner, Carson Denison, Danny Hernandez, Dustin Li, Esin Durmus, et al. | **Year**: 2023 | **Cited by**: 32 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Large language models (LLMs) perform better when they produce step-by-step, "Chain-of-Thought" (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model's actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT's performance boost does not seem to come from CoT's added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.
