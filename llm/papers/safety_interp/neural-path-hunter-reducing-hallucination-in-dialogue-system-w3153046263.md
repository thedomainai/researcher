---
title: "Neural Path Hunter: Reducing Hallucination in Dialogue Systems via Path Grounding"
authors: ["Nouha Dziri", "Andrea Madotto", "Osmar R. Zai͏̈ane", "Avishek Joey Bose"]
year: 2021
cited_by_count: 77
doi: "https://doi.org/10.18653/v1/2021.emnlp-main.168"
openalex_id: W3153046263
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Neural Path Hunter: Reducing Hallucination in Dialogue Systems via Path Grounding

**Authors**: Nouha Dziri, Andrea Madotto, Osmar R. Zai͏̈ane, Avishek Joey Bose | **Year**: 2021 | **Cited by**: 77 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Dialogue systems powered by large pretrained language models exhibit an innate ability to deliver fluent and natural-sounding responses.Despite their impressive performance, these models are fitful and can often generate factually incorrect statements impeding their widespread adoption.In this paper, we focus on the task of improving faithfulness and reducing hallucination of neural dialogue systems to known facts supplied by a Knowledge Graph (KG).We propose NEU-RAL PATH HUNTER which follows a generatethen-refine strategy whereby a generated response is amended using the KG.NEURAL PATH HUNTER leverages a separate tokenlevel fact critic to identify plausible sources of hallucination followed by a refinement stage that retrieves correct entities by crafting a query signal that is propagated over a k-hop subgraph.We empirically validate our proposed approach on the OpenDialKG dataset (Moon et al., 2019) against a suite of metrics and report a relative improvement of faithfulness over dialogue responses by 20.35% based on FeQA (Durmus et al., 2020).The code is available at https://github.com/ nouhadziri/Neural-Path-Hunter.
