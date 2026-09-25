---
title: "AI-enabled state-robust EEG representations in children: implications for individualized ADHD monitoring - Model Source Code"
authors: "Lior Tobaly, Zeev Zalevsky"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-02T08:54:11.027505"
doi: "https://doi.org/10.5281/zenodo.22202393"
openalex_id: "https://openalex.org/W7204784826"
source_api: "openalex"
---

# AI-enabled state-robust EEG representations in children: implications for individualized ADHD monitoring - Model Source Code

**著者**: Lior Tobaly, Zeev Zalevsky
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

This repository contains the computational code and non-identifying source data associated with the study “AI-enabled state-robust EEG representations in children: implications for individualized ADHD monitoring.” The study investigates whether person-specific EEG structure remains stable across heterogeneous cognitive states in children and whether self-supervised representation learning can capture this stable individual signal. The analysis uses developmental EEG data from the Healthy Brain Network (HBN) and evaluates cross-paradigm participant retrieval across ten EEG paradigms. The repository includes code for EEG preprocessing, four-second segment generation, self-supervised Transformer-based representation learning, trait–state disentanglement, participant-level embedding extraction, spatial covariance and spectral baselines, cross-paradigm retrieval, permutation testing, bootstrap confidence intervals and participant-level paired statistical comparisons. The principal analysis compares a self-supervised EEG representation with spatial covariance, band power, combined handcrafted features, a trait-state representation and a randomly initialized encoder. The results show that stable inter-channel spatial organization carries a substantial proportion of the exact participant-specific EEG signature, while self-supervised learning improves broader retrieval quality. The archive also contains portable configuration files, environment specifications, pipeline scripts, citation metadata, checksums and aggregate source-data tables supporting the manuscript figures and statistical results. Raw Healthy Brain Network EEG data are not redistributed in this repository. They must be obtained separately from the HBN under the applicable data-access and data-use terms. Participant identifiers, participant-level embeddings and model checkpoints are also excluded from the public archive. The code reproduces the analysis reported in the manuscript. The reported self-supervised representation was pretrained using an earlier HBN participant split before construction of the final cross-paradigm retrieval folds; therefore, the learned-representation results should be interpreted as transductive within-cohort evidence rather than strict unseen-participant generalization.
