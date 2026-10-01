---
title: "Enhancing Chat Language Models by Scaling High-quality Instructional Conversations"
authors: ["Ning Ding", "Yulin Chen", "Bokai Xu", "Yujia Qin", "Shengding Hu", "Zhiyuan Liu", "Maosong Sun", "Bowen Zhou"]
year: 2023
cited_by_count: 123
doi: "https://doi.org/10.18653/v1/2023.emnlp-main.183"
openalex_id: W4389519291
paper_type: conference-paper
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Enhancing Chat Language Models by Scaling High-quality Instructional Conversations

**Authors**: Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Shengding Hu, Zhiyuan Liu, Maosong Sun, Bowen Zhou | **Year**: 2023 | **Cited by**: 123 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Fine-tuning on instruction data has been widely validated as an effective practice for implementing chat language models like ChatGPT.Scaling the diversity and quality of such data, although straightforward, stands a great chance of leading to improved performance.This paper aims to push the upper bound of opensource models further.We first provide a systematically designed, diverse, informative, large-scale dataset of instructional conversations, UltraChat, which does not involve human queries.Our objective is to capture the breadth of interactions between a human user and an AI assistant and employs a comprehensive framework to generate multi-turn conversation iteratively.UltraChat contains 1.5 million high-quality multi-turn dialogues and covers a wide range of topics and instructions.Our statistical analysis of UltraChat reveals its superiority in various key metrics, including scale, average length, diversity, coherence, etc., solidifying its position as a leading opensource dataset.Building upon UltraChat, we fine-tune a LLaMA model to create a powerful conversational model, UltraLM.Our evaluations indicate that UltraLM consistently outperforms other open-source models, including WizardLM and Vicuna, the previously recognized state-of-the-art open-source models.
