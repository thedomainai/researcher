---
title: "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"
authors: ["Naman Jain", "King Han", "Gu, Alex", "Wen-Ding Li", "Fanjia Yan", "Tianjun Zhang", "Sida Wang", "Armando Solar-Lezama", "et al."]
year: 2024
cited_by_count: 29
doi: "https://doi.org/10.48550/arxiv.2403.07974"
openalex_id: W4392822190
paper_type: preprint
evidence_kind: article
topics: ["evaluation"]
landmark: true
abstract_source: "openalex"
---

# LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

**Authors**: Naman Jain, King Han, Gu, Alex, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, et al. | **Year**: 2024 | **Cited by**: 29 | **Kind**: article | **Relevance**: evaluation: core

## Abstract

Large Language Models (LLMs) applied to code-related applications have emerged as a prominent field, attracting significant interest from both academia and industry. However, as new and improved LLMs are developed, existing evaluation benchmarks (e.g., HumanEval, MBPP) are no longer sufficient for assessing their capabilities. In this work, we propose LiveCodeBench, a comprehensive and contamination-free evaluation of LLMs for code, which continuously collects new problems over time from contests across three competition platforms, namely LeetCode, AtCoder, and CodeForces. Notably, our benchmark also focuses on a broader range of code related capabilities, such as self-repair, code execution, and test output prediction, beyond just code generation. Currently, LiveCodeBench hosts four hundred high-quality coding problems that were published between May 2023 and May 2024. We have evaluated 18 base LLMs and 34 instruction-tuned LLMs on LiveCodeBench. We present empirical findings on contamination, holistic performance comparisons, potential overfitting in existing benchmarks as well as individual model comparisons. We will release all prompts and model completions for further community analysis, along with a general toolkit for adding new scenarios and model
