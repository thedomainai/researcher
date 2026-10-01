---
title: "Analog in-memory computing attention mechanism for fast and energy-efficient large language models"
authors: ["Nathan Leroux", "Paul-Philipp Manea", "Chirag Sudarshan", "Jan Finkbeiner", "Sebastian Siegel", "John Paul Strachan", "Emre Neftci"]
year: 2025
cited_by_count: 24
doi: "https://doi.org/10.1038/s43588-025-00854-1"
openalex_id: W4414064893
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Analog in-memory computing attention mechanism for fast and energy-efficient large language models

**Authors**: Nathan Leroux, Paul-Philipp Manea, Chirag Sudarshan, Jan Finkbeiner, Sebastian Siegel, John Paul Strachan, Emre Neftci | **Year**: 2025 | **Cited by**: 24 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Transformer networks, driven by self-attention, are central to large language models. In generative transformers, self-attention uses cache memory to store token projections, avoiding recomputation at each time step. However, graphics processing unit (GPU)-stored projections must be loaded into static random-access memory for each new generation step, causing latency and energy bottlenecks. Here we present a custom self-attention in-memory computing architecture based on emerging charge-based memories called gain cells, which can be efficiently written to store new tokens during sequence generation and enable parallel analog dot-product computation required for self-attention. However, the analog gain-cell circuits introduce non-idealities and constraints preventing the direct mapping of pre-trained models. To circumvent this problem, we design an initialization algorithm achieving text-processing performance comparable to GPT-2 without training from scratch. Our architecture reduces attention latency and energy consumption by up to two and four orders of magnitude, respectively, compared with GPUs, marking a substantial step toward ultrafast, low-power generative transformers.
