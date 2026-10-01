---
title: "How Can We Know What Language Models Know?"
authors: ["Zhengbao Jiang", "Frank F. Xu", "Jun Araki", "Graham Neubig"]
year: 2020
cited_by_count: 991
doi: "https://doi.org/10.1162/tacl_a_00324"
openalex_id: W2991382858
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# How Can We Know What Language Models Know?

**Authors**: Zhengbao Jiang, Frank F. Xu, Jun Araki, Graham Neubig | **Year**: 2020 | **Cited by**: 991 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Recent work has presented intriguing results examining the knowledge contained in language models (LMs) by having the LM fill in the blanks of prompts such as “ Obama is a __ by profession”. These prompts are usually manually created, and quite possibly sub-optimal; another prompt such as “ Obama worked as a __ ” may result in more accurately predicting the correct profession. Because of this, given an inappropriate prompt, we might fail to retrieve facts that the LM does know, and thus any given prompt only provides a lower bound estimate of the knowledge contained in an LM. In this paper, we attempt to more accurately estimate the knowledge contained in LMs by automatically discovering better prompts to use in this querying process. Specifically, we propose mining-based and paraphrasing-based methods to automatically generate high-quality and diverse prompts, as well as ensemble methods to combine answers from different prompts. Extensive experiments on the LAMA benchmark for extracting relational knowledge from LMs demonstrate that our methods can improve accuracy from 31.1% to 39.6%, providing a tighter lower bound on what LMs know. We have released the code and the resulting LM Prompt And Query Archive (LPAQA) at https://github.com/jzbjyb/LPAQA .
