---
title: "RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models"
authors: ["Samuel Gehman", "Suchin Gururangan", "Maarten Sap", "Yejin Choi", "Noah A. Smith"]
year: 2020
cited_by_count: 660
doi: "https://doi.org/10.18653/v1/2020.findings-emnlp.301"
openalex_id: W3088599783
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models

**Authors**: Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, Noah A. Smith | **Year**: 2020 | **Cited by**: 660 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Pretrained neural language models (LMs) are prone to generating racist, sexist, or otherwise toxic language which hinders their safe deployment.We investigate the extent to which pretrained LMs can be prompted to generate toxic language, and the effectiveness of controllable text generation algorithms at preventing such toxic degeneration.We create and release RE-ALTOXICITYPROMPTS, a dataset of 100K naturally occurring, sentence-level prompts derived from a large corpus of English web text, paired with toxicity scores from a widelyused toxicity classifier.Using REALTOXICI-TYPROMPTS, we find that pretrained LMs can degenerate into toxic text even from seemingly innocuous prompts.We empirically assess several controllable generation methods, and find that while data-or compute-intensive methods (e.g., adaptive pretraining on non-toxic data) are more effective at steering away from toxicity than simpler solutions (e.g., banning "bad" words), no current method is failsafe against neural toxic degeneration.To pinpoint the potential cause of such persistent toxic degeneration, we analyze two web text corpora used to pretrain several LMs (including GPT-2; Radford et al., 2019), and find a significant amount of offensive, factually unreliable, and otherwise toxic content.Our work provides a test bed for evaluating toxic generations by LMs and stresses the need for better data selection processes for pretraining.
