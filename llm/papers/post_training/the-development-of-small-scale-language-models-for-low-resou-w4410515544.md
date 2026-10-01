---
title: "The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization"
authors: ["Nurgali Kadyrbek", "Жансеит Кансеитович Туймебаев", "Мадина Мансурова", "Vitor Manuel Rodrigues Viegas"]
year: 2025
cited_by_count: 12
doi: "https://doi.org/10.3390/bdcc9050137"
openalex_id: W4410515544
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization

**Authors**: Nurgali Kadyrbek, Жансеит Кансеитович Туймебаев, Мадина Мансурова, Vitor Manuel Rodrigues Viegas | **Year**: 2025 | **Cited by**: 12 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Low-resource languages remain underserved by contemporary large language models (LLMs) because they lack sizable corpora, bespoke preprocessing tools, and the computing budgets assumed by mainstream alignment pipelines. Focusing on Kazakh, we present a 1.94B parameter LLaMA-based model that demonstrates how strong, culturally aligned performance can be achieved without massive infrastructure. The contribution is threefold. (i) Data and tokenization—we compile a rigorously cleaned, mixed-domain Kazakh corpus and design a tokenizer that respects the language’s agglutinative morphology, mixed-script usage, and diacritics. (ii) Training recipe—the model is built in two stages: causal language modeling from scratch followed by instruction tuning. Alignment is further refined with Direct Preference Optimization (DPO), extended by contrastive and entropy-based regularization to stabilize training under sparse, noisy preference signals. Two complementary resources support this step: ChatTune-DPO, a crowd-sourced set of human preference pairs, and Pseudo-DPO, an automatically generated alternative that repurposes instruction data to reduce annotation cost. (iii) Evaluation and impact—qualitative and task-specific assessments show that targeted monolingual training and the proposed DPO variant markedly improve factuality, coherence, and cultural fidelity over baseline instruction-only and multilingual counterparts. The model and datasets are released under open licenses, offering a reproducible blueprint for extending state-of-the-art language modeling to other under-represented languages and domains.
