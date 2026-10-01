---
title: "Do Large Language Models Pay Similar Attention Like Human Programmers When Generating Code?"
authors: ["Bonan Kou", "S. Chen", "Zhijie Wang", "Lei Ma", "Tianyi Zhang"]
year: 2024
cited_by_count: 14
doi: "https://doi.org/10.1145/3660807"
openalex_id: W4400582376
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Do Large Language Models Pay Similar Attention Like Human Programmers When Generating Code?

**Authors**: Bonan Kou, S. Chen, Zhijie Wang, Lei Ma, Tianyi Zhang | **Year**: 2024 | **Cited by**: 14 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Large Language Models (LLMs) have recently been widely used for code generation. Due to the complexity and opacity of LLMs, little is known about how these models generate code. We made the first attempt to bridge this knowledge gap by investigating whether LLMs attend to the same parts of a task description as human programmers during code generation. An analysis of six LLMs, including GPT-4, on two popular code generation benchmarks revealed a consistent misalignment between LLMs’ and programmers’ attention. We manually analyzed 211 incorrect code snippets and found five attention patterns that can be used to explain many code generation errors. Finally, a user study showed that model attention computed by a perturbation-based method is often favored by human programmers. Our findings highlight the need for human-aligned LLMs for better interpretability and programmer trust.
