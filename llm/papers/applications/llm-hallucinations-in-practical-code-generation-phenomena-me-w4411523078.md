---
title: "LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation"
authors: ["Ziyao Zhang", "Chong Wang", "Yanlin Wang", "Ensheng Shi", "Yuchi Ma", "Wanjun Zhong", "Jiachi Chen", "Mingzhi Mao", "et al."]
year: 2025
cited_by_count: 94
doi: "https://doi.org/10.1145/3728894"
openalex_id: W4411523078
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation

**Authors**: Ziyao Zhang, Chong Wang, Yanlin Wang, Ensheng Shi, Yuchi Ma, Wanjun Zhong, Jiachi Chen, Mingzhi Mao, et al. | **Year**: 2025 | **Cited by**: 94 | **Kind**: article | **Relevance**: applications: core

## Abstract

Code generation aims to automatically generate code from input requirements, significantly enhancing development efficiency. Recent large language models (LLMs) based approaches have shown promising results and revolutionized code generation task. Despite the promising performance, LLMs often generate contents with hallucinations, especially for the code generation scenario requiring the handling of complex contextual dependencies in practical development process. Although previous study has analyzed hallucinations in LLM-powered code generation, the study is limited to standalone function generation. In this paper, we conduct an empirical study to study the phenomena, mechanism, and mitigation of LLM hallucinations within more practical and complex development contexts in repository-level generation scenario. First, we manually examine the code generation results from six mainstream LLMs to establish a hallucination taxonomy of LLMgenerated code. Next, we elaborate on the phenomenon of hallucinations, analyze their distribution across different models. We then analyze causes of hallucinations and identify four potential factors contributing to hallucinations. Finally, we propose an RAG-based mitigation method, which demonstrates consistent effectiveness in all studied LLMs.
