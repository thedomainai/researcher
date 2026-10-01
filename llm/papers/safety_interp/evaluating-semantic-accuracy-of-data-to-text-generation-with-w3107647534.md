---
title: "Evaluating Semantic Accuracy of Data-to-Text Generation with Natural Language Inference"
authors: ["Ondřej Dušek", "Zdeněk Kasner"]
year: 2020
cited_by_count: 44
doi: "https://doi.org/10.18653/v1/2020.inlg-1.19"
openalex_id: W3107647534
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Evaluating Semantic Accuracy of Data-to-Text Generation with Natural Language Inference

**Authors**: Ondřej Dušek, Zdeněk Kasner | **Year**: 2020 | **Cited by**: 44 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

A major challenge in evaluating data-to-text (D2T) generation is measuring the semantic accuracy of the generated text, i.e. checking if the output text contains all and only facts supported by the input data.We propose a new metric for evaluating the semantic accuracy of D2T generation based on a neural model pretrained for natural language inference (NLI).We use the NLI model to check textual entailment between the input data and the output text in both directions, allowing us to reveal omissions or hallucinations.Input data are converted to text for NLI using trivial templates.Our experiments on two recent D2T datasets show that our metric can achieve high accuracy in identifying erroneous system outputs.
