---
title: "Detecting Hallucinated Content in Conditional Neural Sequence Generation"
authors: ["Chunting Zhou", "Graham Neubig", "Jiatao Gu", "Mona Diab", "Francisco Guzmán", "Luke Zettlemoyer", "Marjan Ghazvininejad"]
year: 2021
cited_by_count: 112
doi: "https://doi.org/10.18653/v1/2021.findings-acl.120"
openalex_id: W3173343821
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Detecting Hallucinated Content in Conditional Neural Sequence Generation

**Authors**: Chunting Zhou, Graham Neubig, Jiatao Gu, Mona Diab, Francisco Guzmán, Luke Zettlemoyer, Marjan Ghazvininejad | **Year**: 2021 | **Cited by**: 112 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Neural sequence models can generate highly fluent sentences, but recent studies have also shown that they are also prone to hallucinate additional content not supported by the input.These variety of fluent but wrong outputs are particularly problematic, as it will not be possible for users to tell they are being presented incorrect content.To detect these errors, we propose a task to predict whether each token in the output sequence is hallucinated (not contained in the input) and collect new manually annotated evaluation sets for this task.We also introduce a method for learning to detect hallucinations using pretrained language models fine tuned on synthetic data that includes automatically inserted hallucinations.Experiments on machine translation (MT) and abstractive summarization demonstrate that our proposed approach consistently outperforms strong baselines on all benchmark datasets.We further demonstrate how to use the token-level hallucination labels to define a fine-grained loss over the target sequence in low-resource MT and achieve significant improvements over strong baseline methods.We also apply our method to word-level quality estimation for MT and show its effectiveness in both supervised and unsupervised settings 1 .
