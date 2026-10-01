---
title: "Structured Chain-of-Thought Prompting for Code Generation"
authors: ["Jia Li", "Ge Li", "Yongmin Li", "Zhi Gang Jin"]
year: 2024
cited_by_count: 132
doi: "https://doi.org/10.1145/3690635"
openalex_id: W4401996408
paper_type: article
evidence_kind: article
topics: ["elicitation", "applications"]
landmark: false
abstract_source: "openalex"
---

# Structured Chain-of-Thought Prompting for Code Generation

**Authors**: Jia Li, Ge Li, Yongmin Li, Zhi Gang Jin | **Year**: 2024 | **Cited by**: 132 | **Kind**: article | **Relevance**: elicitation: core; applications: core

## Abstract

Large Language Models (LLMs) have shown impressive abilities in code generation. Chain-of-Thought (CoT) prompting is the state-of-the-art approach to utilizing LLMs. CoT prompting asks LLMs first to generate CoTs (i.e., intermediate natural language reasoning steps) and then output the code. However, the accuracy of CoT prompting still cannot satisfy practical applications. For example, gpt-3.5-turbo with CoT prompting only achieves 53.29% Pass@1 in HumanEval. In this article, we propose Structured CoTs (SCoTs) and present a novel prompting technique for code generation named SCoT prompting. Our motivation is that human developers follow structured programming. Developers use three programming structures (i.e., sequential, branch, and loop) to design and implement structured programs. Thus, we ask LLMs to use three programming structures to generate SCoTs (structured reasoning steps) before outputting the final code. Compared to CoT prompting, SCoT prompting explicitly introduces programming structures and unlocks the structured programming thinking of LLMs. We apply SCoT prompting to two LLMs (i.e., gpt-4-turbo, gpt-3.5-turbo, and DeepSeek Coder-Instruct- \(\{\) 1.3B, 6.7B, 33B \(\}\) ) and evaluate it on three benchmarks (i.e., HumanEval, MBPP, and MBCPP). SCoT prompting outperforms CoT prompting by up to 13.79% in Pass@1. SCoT prompting is robust to examples and achieves substantial improvements. The human evaluation also shows human developers prefer programs from SCoT prompting.
