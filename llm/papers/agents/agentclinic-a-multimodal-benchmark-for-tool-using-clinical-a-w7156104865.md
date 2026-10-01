---
title: "AgentClinic: a multimodal benchmark for tool-using clinical AI agents"
authors: ["Samuel Schmidgall", "Rojin Ziaei", "Carl Harris", "Ji Woong Kim", "Eduardo Pontes Reis", "Jeffrey Jopling", "Michael Moor"]
year: 2026
cited_by_count: 10
doi: "https://doi.org/10.1038/s41746-026-02674-7"
openalex_id: W7156104865
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# AgentClinic: a multimodal benchmark for tool-using clinical AI agents

**Authors**: Samuel Schmidgall, Rojin Ziaei, Carl Harris, Ji Woong Kim, Eduardo Pontes Reis, Jeffrey Jopling, Michael Moor | **Year**: 2026 | **Cited by**: 10 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Evaluating large language models (LLM) in clinical scenarios is crucial to assessing their potential clinical utility. Existing benchmarks rely heavily on static question-answering, which does not accurately depict the complex, sequential nature of clinical decision-making. Here, we introduce AgentClinic, a multimodal agent benchmark for evaluating LLMs in simulated clinical environments that include patient interactions, multimodal data collection under incomplete information, and the usage of various tools, resulting in an in-depth evaluation across nine medical specialties and seven languages. We find that solving MedQA problems in the sequential decision-making format of AgentClinic is considerably more challenging, resulting in diagnostic accuracies that can drop to below a tenth of the original accuracy. Overall, we observe that agents sourced from Claude-3.5 outperform other LLM backbones in most settings. Nevertheless, we see stark differences in the LLMs' ability to make use of tools, such as experiential learning, adaptive retrieval, and reflection cycles. Strikingly, Llama-3 shows up to 92% relative improvements with the notebook tool that allows for writing and editing notes that persist across cases. To further scrutinize our clinical simulations, we leverage real-world electronic health records, perform a clinical reader study, perturb agents with biases, and explore patient-centric metrics that this interactive environment enables.
