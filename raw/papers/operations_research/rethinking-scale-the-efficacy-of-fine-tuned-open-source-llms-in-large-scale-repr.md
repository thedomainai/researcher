---
title: "Rethinking Scale: The Efficacy of Fine-Tuned Open-Source LLMs in Large-Scale Reproducible Social Science Research"
authors: "Marcello Carammia, Stefano M. Iacus, Giuseppe Porro"
year: 2026
citations: 2
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-17T09:23:10.150863"
doi: "https://doi.org/10.1177/08944393261485320"
openalex_id: "https://openalex.org/W4404350789"
source_api: "openalex"
---

# Rethinking Scale: The Efficacy of Fine-Tuned Open-Source LLMs in Large-Scale Reproducible Social Science Research

**著者**: Marcello Carammia, Stefano M. Iacus, Giuseppe Porro
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Large language models (LLMs) are distinguished by their architecture, parameter size, and performance capabilities. Social scientists have increasingly adopted LLMs to automate high-dimensional text classification tasks which are difficult to scale with human coders. Very large, closed-source models often deliver superior performance. However, reliance on large proprietary models raises concerns about transparency, reproducibility, and costs that make them impractical for large-scale research projects. In contrast, open-source models offer distinct advantages: they can be run locally (ensuring data privacy), fine-tuned for specific tasks, shared within the research community, and integrated into reproducible workflows. On the other hand, open-source models often underperform compared to commercial alternatives. In this study, we assess whether small, open-source LLMs – when fine-tuned appropriately – can match or exceed the performance of commercial alternatives such as GPT-4, while remaining feasible for large-scale academic research. To produce the labeled data that fine-tuning requires, we develop a hybrid annotation workflow in which several LLMs propose labels that human reviewers verify; this infrastructure is what makes fine-tuning feasible at scale. We apply this pipeline to three substantive social science classification tasks: coding tweets for human flourishing indicators, classifying European Parliament questions by policy area, and tagging datasets from the Harvard Dataverse. Our results show that fine-tuned models as small as Llama2-7B achieve performance on par with much larger closed models, offering a reproducible, low-cost alternative for computational social science research. We also explore the limits of fine-tuning effectiveness across model sizes and training set volumes. This work demonstrates a scalable and replicable approach to integrating open-source LLMs into empirical social science workflows.
