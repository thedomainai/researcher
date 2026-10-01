---
title: "Sources of Hallucination by Large Language Models on Inference Tasks"
authors: ["Nick McKenna", "Tianyi Li", "Liang Cheng", "Mohammad Javad Hosseini", "Mark S. Johnson", "Mark J. Steedman"]
year: 2023
cited_by_count: 122
doi: "https://doi.org/10.18653/v1/2023.findings-emnlp.182"
openalex_id: W4389519585
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Sources of Hallucination by Large Language Models on Inference Tasks

**Authors**: Nick McKenna, Tianyi Li, Liang Cheng, Mohammad Javad Hosseini, Mark S. Johnson, Mark J. Steedman | **Year**: 2023 | **Cited by**: 122 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Large Language Models (LLMs) are claimed to be capable of Natural Language Inference (NLI), necessary for applied tasks like question answering and summarization.We present a series of behavioral studies on several LLM families (LLaMA, GPT-3.5, and PaLM) which probe their behavior using controlled experiments.We establish two biases originating from pretraining which predict much of their behavior, and show that these are major sources of hallucination in generative LLMs.First, memorization at the level of sentences: we show that, regardless of the premise, models falsely label NLI test samples as entailing when the hypothesis is attested in training data, and that entities are used as "indices" to access the memorized data.Second, statistical patterns of usage learned at the level of corpora: we further show a similar effect when the premise predicate is less frequent than that of the hypothesis in the training data, a bias following from previous studies.We demonstrate that LLMs perform significantly worse on NLI test samples which do not conform to these biases than those which do, and we offer these as valuable controls for future LLM evaluation. 1 * Equal contribution.
