---
title: "ViperGPT: Visual Inference via Python Execution for Reasoning"
authors: ["Dídac Surís", "Sachit Menon", "Carl Vondrick"]
year: 2023
cited_by_count: 212
doi: "https://doi.org/10.1109/iccv51070.2023.01092"
openalex_id: W4390872747
paper_type: conference-paper
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# ViperGPT: Visual Inference via Python Execution for Reasoning

**Authors**: Dídac Surís, Sachit Menon, Carl Vondrick | **Year**: 2023 | **Cited by**: 212 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Answering visual queries is a complex task that requires both visual processing and reasoning. End-to-end models, the dominant approach for this task, do not explicitly differentiate between the two, limiting interpretability and generalization. Learning modular programs presents a promising alternative, but has proven challenging due to the difficulty of learning both the programs and modules simultaneously. We introduce ${\color{green}{\text{ViperGPT}}}$, a framework that leverages code-generation models to compose vision-and-language models into subroutines to produce a result for any query. ${\color{green}{\text{ViperGPT}}}$ utilizes a provided API to access the available modules, and composes them by generating Python code that is later executed. This simple approach requires no further training, and achieves state-of-the-art results across various complex visual tasks.
