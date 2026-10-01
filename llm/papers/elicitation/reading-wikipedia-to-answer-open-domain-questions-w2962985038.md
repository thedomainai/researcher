---
title: "Reading Wikipedia to Answer Open-Domain Questions"
authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "Antoine Bordes"]
year: 2017
cited_by_count: 1461
doi: "https://doi.org/10.18653/v1/p17-1171"
openalex_id: W2962985038
paper_type: conference-paper
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Reading Wikipedia to Answer Open-Domain Questions

**Authors**: Danqi Chen, Adam Fisch, Jason Weston, Antoine Bordes | **Year**: 2017 | **Cited by**: 1461 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

This paper proposes to tackle open-domain question answering using Wikipedia as the unique knowledge source: the answer to any factoid question is a text span in a Wikipedia article. This task of machine reading at scale combines the challenges of document retrieval (finding the relevant articles) with that of machine comprehension of text (identifying the answer spans from those articles). Our approach combines a search component based on bigram hashing and TF-IDF matching with a multi-layer recurrent neural network model trained to detect answers in Wikipedia paragraphs. Our experiments on multiple existing QA datasets indicate that (1) both modules are highly competitive with respect to existing counterparts and (2) multitask learning using distant supervision on their combination is an effective complete system on this challenging task.
