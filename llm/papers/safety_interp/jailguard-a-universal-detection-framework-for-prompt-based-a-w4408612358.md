---
title: "JailGuard : A Universal Detection Framework for Prompt-based Attacks on LLM Systems"
authors: ["Xiaoyu Zhang", "Cen Zhang", "Tianlin Li", "Yihao Huang", "Xiaojun Jia", "Ming Hu", "Jie Zhang", "Yang Liu", "et al."]
year: 2025
cited_by_count: 22
doi: "https://doi.org/10.1145/3724393"
openalex_id: W4408612358
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# JailGuard : A Universal Detection Framework for Prompt-based Attacks on LLM Systems

**Authors**: Xiaoyu Zhang, Cen Zhang, Tianlin Li, Yihao Huang, Xiaojun Jia, Ming Hu, Jie Zhang, Yang Liu, et al. | **Year**: 2025 | **Cited by**: 22 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

The systems and software powered by Large Language Models (LLMs) and Multi-Modal Large Language Models (MLLMs) have played a critical role in numerous scenarios. However, current LLM systems are vulnerable to prompt-based attacks, with jailbreaking attacks enabling the LLM system to generate harmful content, while hijacking attacks manipulate the LLM system to perform attacker-desired tasks, underscoring the necessity for detection tools. Unfortunately, existing detecting approaches are usually tailored to specific attacks, resulting in poor generalization in detecting various attacks across different modalities. To address it, we propose JailGuard , a universal detection framework deployed on top of LLM systems for prompt-based attacks across text and image modalities. JailGuard operates on the principle that attacks are inherently less robust than benign ones. Specifically, JailGuard mutates untrusted inputs to generate variants and leverages the discrepancy of the variants’ responses on the target model to distinguish attack samples from benign samples. We implement 18 mutators for text and image inputs and design a mutator combination policy to further improve detection generalization. The evaluation on the dataset containing 15 known attack types suggests that JailGuard achieves the best detection accuracy of 86.14%/82.90% on text and image inputs, outperforming state-of-the-art methods by 11.81–25.73% and 12.20–21.40%.
