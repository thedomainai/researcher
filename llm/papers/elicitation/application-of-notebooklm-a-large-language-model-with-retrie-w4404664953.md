---
title: "Application of NotebookLM, a large language model with retrieval-augmented generation, for lung cancer staging"
authors: ["Ryota Tozuka", "Hisashi Johno", "Akitomo Amakawa", "Junichi Sato", "Mizuki Muto", "Shoichiro Seki", "Atsushi Komaba", "Hiroshi Onishi"]
year: 2024
cited_by_count: 48
doi: "https://doi.org/10.1007/s11604-024-01705-1"
openalex_id: W4404664953
paper_type: article
evidence_kind: guideline
topics: ["elicitation"]
landmark: false
abstract_source: "semantic_scholar"
---

# Application of NotebookLM, a large language model with retrieval-augmented generation, for lung cancer staging

**Authors**: Ryota Tozuka, Hisashi Johno, Akitomo Amakawa, Junichi Sato, Mizuki Muto, Shoichiro Seki, Atsushi Komaba, Hiroshi Onishi | **Year**: 2024 | **Cited by**: 48 | **Kind**: guideline | **Relevance**: elicitation: supporting

## Abstract

In radiology, large language models (LLMs), including ChatGPT, have recently gained attention, and their utility is being rapidly evaluated. However, concerns have emerged regarding their reliability in clinical applications due to limitations such as hallucinations and insufficient referencing. To address these issues, we focus on the latest technology, retrieval-augmented generation (RAG), which enables LLMs to reference reliable external knowledge (REK). Specifically, this study examines the utility and reliability of a recently released RAG-equipped LLM (RAG-LLM), NotebookLM, for staging lung cancer. We summarized the current lung cancer staging guideline in Japan and provided this as REK to NotebookLM. We then tasked NotebookLM with staging 100 fictional lung cancer cases based on CT findings and evaluated its accuracy. For comparison, we performed the same task using a gold-standard LLM, GPT-4 Omni (GPT-4o), both with and without the REK. For GPT-4o, the REK was provided directly within the prompt rather than through RAG. NotebookLM achieved 86% diagnostic accuracy in the lung cancer staging experiment, outperforming GPT-4o, which recorded 39% accuracy with the REK and 25% without it. Moreover, NotebookLM demonstrated 95% accuracy in searching reference locations within the REK. NotebookLM, a RAG-LLM, successfully performed lung cancer staging by utilizing the REK, demonstrating superior performance compared to GPT-4o (without RAG). Additionally, it provided highly accurate reference locations within the REK, allowing radiologists to efficiently evaluate the reliability of NotebookLM’s responses and detect possible hallucinations. Overall, this study highlights the potential of NotebookLM, a RAG-LLM, in image diagnosis.
