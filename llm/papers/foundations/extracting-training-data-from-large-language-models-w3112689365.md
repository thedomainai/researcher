---
title: "Extracting Training Data from Large Language Models"
authors: ["Nicholas Carlini", "Florian Tramèr", "Eric W. Wallace", "Matthew Jagielski", "Ariel Herbert-Voss", "Katherine Lee", "Roberts, Adam", "Brown, Tom", "et al."]
year: 2020
cited_by_count: 272
doi: "https://doi.org/10.48550/arxiv.2012.07805"
openalex_id: W3112689365
paper_type: preprint
evidence_kind: article
topics: ["foundations", "safety_interp"]
landmark: true
abstract_source: "openalex"
---

# Extracting Training Data from Large Language Models

**Authors**: Nicholas Carlini, Florian Tramèr, Eric W. Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Roberts, Adam, Brown, Tom, et al. | **Year**: 2020 | **Cited by**: 272 | **Kind**: article | **Relevance**: foundations: supporting; safety_interp: core

## Abstract

It has become common to publish large (billion parameter) language models that have been trained on private datasets. This paper demonstrates that in such settings, an adversary can perform a training data extraction attack to recover individual training examples by querying the language model. We demonstrate our attack on GPT-2, a language model trained on scrapes of the public Internet, and are able to extract hundreds of verbatim text sequences from the model's training data. These extracted examples include (public) personally identifiable information (names, phone numbers, and email addresses), IRC conversations, code, and 128-bit UUIDs. Our attack is possible even though each of the above sequences are included in just one document in the training data. We comprehensively evaluate our extraction attack to understand the factors that contribute to its success. Worryingly, we find that larger models are more vulnerable than smaller models. We conclude by drawing lessons and discussing possible safeguards for training large language models.
