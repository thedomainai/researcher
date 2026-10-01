---
title: "Can large language models reason about medical questions?"
authors: ["Valentin Liévin", "Christoffer Hother", "Andreas Geert Motzfeldt", "Ole Winther"]
year: 2024
cited_by_count: 295
doi: "https://doi.org/10.1016/j.patter.2024.100943"
openalex_id: W4392359953
paper_type: article
evidence_kind: article
topics: ["elicitation", "applications"]
landmark: false
abstract_source: "openalex"
---

# Can large language models reason about medical questions?

**Authors**: Valentin Liévin, Christoffer Hother, Andreas Geert Motzfeldt, Ole Winther | **Year**: 2024 | **Cited by**: 295 | **Kind**: article | **Relevance**: elicitation: supporting; applications: core

## Abstract

Although large language models often produce impressive outputs, it remains unclear how they perform in real-world scenarios requiring strong reasoning skills and expert domain knowledge. We set out to investigate whether closed- and open-source models (GPT-3.5, Llama 2, etc.) can be applied to answer and reason about difficult real-world-based questions. We focus on three popular medical benchmarks (MedQA-US Medical Licensing Examination [USMLE], MedMCQA, and PubMedQA) and multiple prompting scenarios: chain of thought (CoT; think step by step), few shot, and retrieval augmentation. Based on an expert annotation of the generated CoTs, we found that InstructGPT can often read, reason, and recall expert knowledge. Last, by leveraging advances in prompt engineering (few-shot and ensemble methods), we demonstrated that GPT-3.5 not only yields calibrated predictive distributions but also reaches the passing score on three datasets: MedQA-USMLE (60.2%), MedMCQA (62.7%), and PubMedQA (78.2%). Open-source models are closing the gap: Llama 2 70B also passed the MedQA-USMLE with 62.5% accuracy.
