---
title: "InterPLM: discovering interpretable features in protein language models via sparse autoencoders"
authors: ["Elana P. Simon", "James Zou"]
year: 2025
cited_by_count: 45
doi: "https://doi.org/10.1038/s41592-025-02836-7"
openalex_id: W4414589084
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "semantic_scholar"
---

# InterPLM: discovering interpretable features in protein language models via sparse autoencoders

**Authors**: Elana P. Simon, James Zou | **Year**: 2025 | **Cited by**: 45 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Protein language models (PLMs) have demonstrated remarkable success in protein modeling and design, yet their internal mechanisms for predicting structure and function remain poorly understood. Here we present a systematic approach to extract and analyze interpretable features from PLMs using sparse autoencoders (SAEs). By training SAEs on embeddings from the PLM ESM-2, we identify thousands of human-interpretable latent features per layer that highlight hundreds of known biological concepts such as binding sites, structural motifs, and functional domains. In contrast, examining individual neurons in ESM-2 reveals significantly less conceptual alignment, suggesting that PLMs represent most concepts in superposition. We further demonstrate that a larger PLM (ESM-2 with 650M parameters) captures substantially more interpretable concepts than a smaller PLM (ESM-2 with 8M parameters). Beyond capturing known annotations, we show that ESM-2 learns coherent concepts that do not map onto existing annotations and propose a pipeline using language models to automatically interpret novel latent features learned by the SAEs. As practical applications, we demonstrate how these latent features can fill in missing annotations in protein databases and enable targeted steering of protein sequence generation. Our results demonstrate that PLMs encode rich, interpretable representations of protein biology and we propose a systematic framework to uncover and understand these latent features. In the process, we recover both known biology and potentially new protein motifs. As community resources, we introduce InterPLM (interPLM.ai), an interactive visualization platform for investigating learned PLM features, and release code for training and analysis at github.com/ElanaPearl/interPLM.
