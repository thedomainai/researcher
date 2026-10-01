---
title: "How Much Knowledge Can You Pack Into the Parameters of a Language Model?"
authors: ["Adam Paul Roberts", "Colin Raffel", "Noam Shazeer"]
year: 2020
cited_by_count: 630
doi: "https://doi.org/10.18653/v1/2020.emnlp-main.437"
openalex_id: W3008686018
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# How Much Knowledge Can You Pack Into the Parameters of a Language Model?

**Authors**: Adam Paul Roberts, Colin Raffel, Noam Shazeer | **Year**: 2020 | **Cited by**: 630 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

It has recently been observed that neural language models trained on unstructured text can implicitly store and retrieve knowledge using natural language queries.In this short paper, we measure the practical utility of this approach by fine-tuning pre-trained models to answer questions without access to any external context or knowledge.We show that this approach scales with model size and performs competitively with open-domain systems that explicitly retrieve answers from an external knowledge source when answering questions.To facilitate reproducibility and future work, we release our code and trained models. 1 * Equal contribution.Noam suggested trying T5 on open-domain QA and coded and ran initial experiments on TriviaQA showing improved performance with model size.Adam wrote the code and ran most experiments.Colin set the research scope, wrote the paper, and ran a few experiments.1 https://goo.gle/t5-cbqa
