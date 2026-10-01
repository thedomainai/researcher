---
title: "Type-Constrained Code Generation with Language Models"
authors: ["Niels Mündler", "Jingxuan He", "Hao Wang", "Koushik Sen", "Dawn Xiaodong Song", "Martin Vechev"]
year: 2025
cited_by_count: 10
doi: "https://doi.org/10.1145/3729274"
openalex_id: W4411267925
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Type-Constrained Code Generation with Language Models

**Authors**: Niels Mündler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Xiaodong Song, Martin Vechev | **Year**: 2025 | **Cited by**: 10 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Large language models (LLMs) have achieved notable success in code generation. However, they still frequently produce uncompilable output because their next-token inference procedure does not model formal aspects of code. Although constrained decoding is a promising approach to alleviate this issue, it has only been applied to handle either domain-specific languages or syntactic features of general-purpose programming languages. However, LLMs frequently generate code with typing errors, which are beyond the domain of syntax and generally hard to adequately constrain. To address this challenge, we introduce a type-constrained decoding approach that leverages type systems to guide code generation. For this purpose, we develop novel prefix automata and a search over inhabitable types, forming a sound approach to enforce well-typedness on LLM-generated code. We formalize our approach on a foundational simply-typed language and extend it to TypeScript to demonstrate practicality. Our evaluation on the HumanEval and MBPP datasets shows that our approach reduces compilation errors by more than half and significantly increases functional correctness in code synthesis, translation, and repair tasks across LLMs of various sizes and model families, including state-of-the-art open-weight models with more than 30B parameters. The results demonstrate the generality and effectiveness of our approach in constraining LLM code generation with formal rules of type systems.
