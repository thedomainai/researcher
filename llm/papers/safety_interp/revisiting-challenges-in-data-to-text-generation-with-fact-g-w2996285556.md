---
title: "Revisiting Challenges in Data-to-Text Generation with Fact Grounding"
authors: ["Hongmin Wang"]
year: 2019
cited_by_count: 35
doi: "https://doi.org/10.18653/v1/w19-8639"
openalex_id: W2996285556
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Revisiting Challenges in Data-to-Text Generation with Fact Grounding

**Authors**: Hongmin Wang | **Year**: 2019 | **Cited by**: 35 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Data-to-text generation models face challenges in ensuring data fidelity by referring to the correct input source.To inspire studies in this area, Wiseman et al. (2017) introduced the RotoWire corpus on generating NBA game summaries from the box-and line-score tables.However, limited attempts have been made in this direction and the challenges remain.We observe a prominent bottleneck in the corpus where only about 60% of the summary contents can be grounded to the boxscore records.Such information deficiency tends to misguide a conditioned language model to produce unconditioned random facts and thus leads to factual hallucinations.In this work, we restore the information balance and revamp this task to focus on fact-grounded data-to-text generation.We introduce a purified and larger-scale dataset, RotoWire-FG (Fact-Grounding), with 50% more data from the year 2017-19 and enriched input tables, hoping to attract more research focuses in this direction.Moreover, we achieve improved data fidelity over the stateof-the-art models by integrating a new form of table reconstruction as an auxiliary task to boost the generation quality.
