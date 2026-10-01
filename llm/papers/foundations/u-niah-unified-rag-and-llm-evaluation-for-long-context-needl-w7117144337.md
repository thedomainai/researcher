---
title: "U-NIAH: Unified RAG and LLM Evaluation for Long Context Needle-in-a-Haystack"
authors: ["Yunfan Gao", "Yun Xiong", "Wenlong Wu", "Bohan Li", "Yijie Zhong", "Haofen Wang"]
year: 2025
cited_by_count: 5
doi: "https://doi.org/10.1145/3786609"
openalex_id: W7117144337
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# U-NIAH: Unified RAG and LLM Evaluation for Long Context Needle-in-a-Haystack

**Authors**: Yunfan Gao, Yun Xiong, Wenlong Wu, Bohan Li, Yijie Zhong, Haofen Wang | **Year**: 2025 | **Cited by**: 5 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Recent advancements in Large Language Models (LLMs) have significantly extended context windows, igniting discussions about the necessity of Retrieval-Augmented Generation (RAG). U-NIAH, a unified Needle-in-a-Haystack (NIAH) framework, systematically evaluates LLMs and RAG methods in controlled long-context settings. It extends beyond traditional NIAH by incorporating more practical and complex scenarios like multi-needle, long-needle, and needle-in-needle configurations and leveraging the synthetic dataset to mitigate LLM biases. The experiments aim to address three research questions in long-context scenarios: (1) performance tradeoffs between LLMs and RAG, (2) error patterns in RAG, and (3) RAG’s limitations in complex settings. Results show that smaller LLMs benefit more from RAG. In all settings, RAG achieves a win rate of 82.58% over direct answers. Additionally, it is found that retrieval noise and chunk ordering degrade RAG performance, and we further summarized typical error patterns, including omissions due to noise, hallucinations under high noise critical conditions, and self-doubt behaviors, as well as how these phenomena vary with context length. Finally, in some challenging scenarios, experiments show that deep reasoning models are more easily affected by distractors. These findings highlight the complementary roles of RAG and LLMs and offer actionable insights for optimizing deployment strategies ( https://github.com/Tongji-KGLLM/U-NIAH ).
