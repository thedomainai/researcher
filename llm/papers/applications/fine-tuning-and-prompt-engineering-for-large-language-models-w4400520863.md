---
title: "Fine-tuning and prompt engineering for large language models-based code review automation"
authors: ["Chanathip Pornprasit", "Chakkrit Kla Tantithamthavorn"]
year: 2024
cited_by_count: 107
doi: "https://doi.org/10.1016/j.infsof.2024.107523"
openalex_id: W4400520863
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# Fine-tuning and prompt engineering for large language models-based code review automation

**Authors**: Chanathip Pornprasit, Chakkrit Kla Tantithamthavorn | **Year**: 2024 | **Cited by**: 107 | **Kind**: article | **Relevance**: applications: core

## Abstract

The rapid evolution of Large Language Models (LLMs) has sparked significant interest in leveraging their capabilities for automating code review processes. Prior studies often focus on developing LLMs for code review automation, yet require expensive resources, which is infeasible for organizations with limited budgets and resources. Thus, fine-tuning and prompt engineering are the two common approaches to leveraging LLMs for code review automation. We aim to investigate the performance of LLMs-based code review automation based on two contexts, i.e., when LLMs are leveraged by fine-tuning and prompting. Fine-tuning involves training the model on a specific code review dataset, while prompting involves providing explicit instructions to guide the model’s generation process without requiring a specific code review dataset. We leverage model fine-tuning and inference techniques (i.e., zero-shot learning, few-shot learning and persona) on LLMs-based code review automation. In total, we investigate 12 variations of two LLMs-based code review automation (i.e., GPT-3.5 and Magicoder), and compare them with the Guo et al.’s approach and three existing code review automation approaches (i.e., CodeReviewer, TufanoT5 and D-ACT). The fine-tuning of GPT 3.5 with zero-shot learning helps GPT-3.5 to achieve 73.17%–74.23% higher EM than the Guo et al.’s approach. In addition, when GPT-3.5 is not fine-tuned, GPT-3.5 with few-shot learning achieves 46.38%–659.09% higher EM than GPT-3.5 with zero-shot learning. Based on our results, we recommend that (1) LLMs for code review automation should be fine-tuned to achieve the highest performance.; and (2) when data is not sufficient for model fine-tuning (e.g., a cold-start problem), few-shot learning without a persona should be used for LLMs for code review automation. Our findings contribute valuable insights into the practical recommendations and trade-offs associated with deploying LLMs for code review automation.
