---
title: "On the Effectiveness of Large Language Models in Domain-Specific Code Generation"
authors: ["Xiaodong Gu", "Meng Chen", "Yalan Lin", "Yuhan Hu", "Hongyu Zhang", "Chengcheng Wan", "Zhao Wei", "Yong Xu", "et al."]
year: 2024
cited_by_count: 53
doi: "https://doi.org/10.1145/3697012"
openalex_id: W4403007658
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# On the Effectiveness of Large Language Models in Domain-Specific Code Generation

**Authors**: Xiaodong Gu, Meng Chen, Yalan Lin, Yuhan Hu, Hongyu Zhang, Chengcheng Wan, Zhao Wei, Yong Xu, et al. | **Year**: 2024 | **Cited by**: 53 | **Kind**: article | **Relevance**: applications: core

## Abstract

Large language models (LLMs) such as ChatGPT have shown remarkable capabilities in code generation. Despite significant achievements, they rely on enormous training data to acquire a broad spectrum of open-domain knowledge. Besides, their evaluation revolves around open-domain benchmarks like HumanEval, which primarily consist of programming contests. Therefore, it is hard to fully characterize the intricacies and challenges associated with particular domains (e.g., Web, game, and math). In this article, we conduct an in-depth study of the LLMs in domain-specific code generation. Our results demonstrate that LLMs exhibit sub-optimal performance in generating domain-specific code, due to their limited proficiency in utilizing domain-specific libraries. We further observe that incorporating API knowledge as prompts can empower LLMs to generate more professional code. Based on these findings, we further investigate how to effectively incorporate API knowledge into the code generation process. We experiment with three strategies for incorporating domain knowledge, namely, external knowledge inquirer, chain-of-thought prompting, and chain-of-thought fine-tuning. We refer to these strategies as a new code generation approach called DomCoder . Experimental results show that all strategies of DomCoder improve the effectiveness of domain-specific code generation under certain settings.
