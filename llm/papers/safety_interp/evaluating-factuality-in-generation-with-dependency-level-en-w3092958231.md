---
title: "Evaluating Factuality in Generation with Dependency-level Entailment"
authors: ["Tanya M. Goyal", "Greg Durrett"]
year: 2020
cited_by_count: 92
doi: "https://doi.org/10.18653/v1/2020.findings-emnlp.322"
openalex_id: W3092958231
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Evaluating Factuality in Generation with Dependency-level Entailment

**Authors**: Tanya M. Goyal, Greg Durrett | **Year**: 2020 | **Cited by**: 92 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Despite significant progress in text generation models, a serious limitation is their tendency to produce text that is factually inconsistent with information in the input.Recent work has studied whether textual entailment systems can be used to identify factual errors; however, these sentence-level entailment models are trained to solve a different problem than generation filtering and they do not localize which part of a generation is non-factual.In this paper, we propose a new formulation of entailment that decomposes it at the level of dependency arcs.Rather than focusing on aggregate decisions, we instead ask whether the semantic relationship manifested by individual dependency arcs in the generated output is supported by the input.Human judgments on this task are difficult to obtain; we therefore propose a method to automatically create data based on existing entailment or paraphrase corpora.Experiments show that our dependency arc entailment model trained on this data can identify factual inconsistencies in paraphrasing and summarization better than sentencelevel methods or those based on question generation, while additionally localizing the erroneous parts of the generation. 1
