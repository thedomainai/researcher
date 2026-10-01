---
title: "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-Tuning"
authors: ["Yun Luo", "Zhen Chao Yang", "Fandong Meng", "Yafu Li", "Jie Zhou", "Yue Zhang"]
year: 2025
cited_by_count: 62
doi: "https://doi.org/10.1109/taslpro.2025.3606231"
openalex_id: W4414037010
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-Tuning

**Authors**: Yun Luo, Zhen Chao Yang, Fandong Meng, Yafu Li, Jie Zhou, Yue Zhang | **Year**: 2025 | **Cited by**: 62 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Catastrophic forgetting (CF) is a phenomenon that occurs in machine learning when a model forgets previously learned information while acquiring new knowledge for achieving satisfactory performance in downstream tasks. As large language models (LLMs) have demonstrated remarkable performance, it is intriguing to investigate whether CF exists during the continual instruction tuning of LLMs. This study empirically evaluates the forgetting phenomenon in LLMs' knowledge during continual instruction tuning from the perspectives of domain knowledge, reasoning, and reading comprehension. The experiments reveal that catastrophic forgetting is generally observed in LLMs ranging from 1b to 7b parameters. Surprisingly, as the model scale increases, the severity of forgetting intensifies in such a model scale range, which may result from the much more significant initial performance in the larger LLM. The finding is also observed by the experiment of Qwen-2.5-Inst from 3B to 14B. Comparing the decoder-only model BLOOMZ with the encoder-decoder model mT0, BLOOMZ exhibits less forgetting and retains more knowledge. Interestingly, we also observe that LLMs can mitigate language biases, such as gender bias, during continual fine-tuning. Furthermore, our findings indicate that general instruction tuning can help alleviate the forgetting phenomenon in LLMs during subsequent fine-tuning.
