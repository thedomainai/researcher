---
title: "Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models"
authors: ["Shahriar Golchin", "Mihai Surdeanu"]
year: 2025
cited_by_count: 9
doi: "https://doi.org/10.1162/tacl.a.20"
openalex_id: W4412930207
paper_type: article
evidence_kind: article
topics: ["evaluation"]
landmark: false
abstract_source: "openalex"
---

# Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models

**Authors**: Shahriar Golchin, Mihai Surdeanu | **Year**: 2025 | **Cited by**: 9 | **Kind**: article | **Relevance**: evaluation: core

## Abstract

Abstract We propose the Data Contamination Quiz (DCQ), a simple and effective approach to detect data contamination in large language models (LLMs) and estimate the amount of it. Specifically, we frame data contamination detection as a series of multiple-choice questions, devising a quiz format wherein three perturbed versions of each instance, subsampled from a specific dataset partition, are created. These changes only include word-level perturbations. The generated perturbations, along with the original dataset instance, form the options in the DCQ, with an extra option accommodating the selection of none of the provided options. Given that the only distinguishing signal among the options is the exact wording with respect to the original dataset instance, an LLM, when tasked with identifying the original dataset instance, gravitates towards selecting the original one if it has been exposed to it. While accounting for positional biases in LLMs, the quiz performance reveals the contamination level for the tested model with the dataset partition to which the quiz pertains. Applied to various datasets and LLMs, under controlled and uncontrolled contamination, our findings—while fully lacking access to training data and model parameters—suggest that DCQ achieves state-of-the-art results and uncovers greater contamination levels through memorization compared to existing methods. Also, it proficiently bypasses more safety filters, especially those set to avoid generating copyrighted content.1
