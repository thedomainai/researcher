---
title: "SummaC : Re-Visiting NLI-based Models for Inconsistency Detection in Summarization"
authors: ["Philippe Laban", "Tobias Schnabel", "Paul Nathan Bennett", "Marti A. Hearst"]
year: 2022
cited_by_count: 221
doi: "https://doi.org/10.1162/tacl_a_00453"
openalex_id: W3213990450
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# SummaC : Re-Visiting NLI-based Models for Inconsistency Detection in Summarization

**Authors**: Philippe Laban, Tobias Schnabel, Paul Nathan Bennett, Marti A. Hearst | **Year**: 2022 | **Cited by**: 221 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Abstract In the summarization domain, a key requirement for summaries is to be factually consistent with the input document. Previous work has found that natural language inference (NLI) models do not perform competitively when applied to inconsistency detection. In this work, we revisit the use of NLI for inconsistency detection, finding that past work suffered from a mismatch in input granularity between NLI datasets (sentence-level), and inconsistency detection (document level). We provide a highly effective and light-weight method called SummaCConv that enables NLI models to be successfully used for this task by segmenting documents into sentence units and aggregating scores between pairs of sentences. We furthermore introduce a new benchmark called SummaC (Summary Consistency) which consists of six large inconsistency detection datasets. On this dataset, SummaCConv obtains state-of-the-art results with a balanced accuracy of 74.4%, a 5% improvement compared with prior work.
