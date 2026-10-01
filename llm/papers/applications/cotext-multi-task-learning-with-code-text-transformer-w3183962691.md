---
title: "CoTexT: Multi-task Learning with Code-Text Transformer"
authors: ["Long Phan", "Hieu Tran", "Daniel X. Le", "Hieu Nguyen", "James Annibal", "Alec Peltekian", "Yanfang Ye"]
year: 2021
cited_by_count: 101
doi: "https://doi.org/10.18653/v1/2021.nlp4prog-1.5"
openalex_id: W3183962691
paper_type: conference-paper
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# CoTexT: Multi-task Learning with Code-Text Transformer

**Authors**: Long Phan, Hieu Tran, Daniel X. Le, Hieu Nguyen, James Annibal, Alec Peltekian, Yanfang Ye | **Year**: 2021 | **Cited by**: 101 | **Kind**: article | **Relevance**: applications: core

## Abstract

We present CoTexT, a pre-trained, transformer-based encoder-decoder model that learns the representative context between natural language (NL) and programming language (PL). Using self-supervision, CoTexT is pre-trained on large programming language corpora to learn a general understanding of language and code. CoTexT supports downstream NL-PL tasks such as code summarizing/documentation, code generation, defect detection, and code debugging. We train CoTexT on different combinations of available PL corpus including both “bimodal” and “unimodal” data. Here, bimodal data is the combination of text and corresponding code snippets, whereas unimodal data is merely code snippets. We first evaluate CoTexT with multi-task learning: we perform Code Summarization on 6 different programming languages and Code Refinement on both small and medium size featured in the CodeXGLUE dataset. We further conduct extensive experiments to investigate CoTexT on other tasks within the CodeXGlue dataset, including Code Generation and Defect Detection. We consistently achieve SOTA results in these tasks, demonstrating the versatility of our models.
