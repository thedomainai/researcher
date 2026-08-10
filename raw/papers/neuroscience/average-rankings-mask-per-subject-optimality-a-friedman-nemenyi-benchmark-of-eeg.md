---
title: "Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders"
authors: "Xavier Vasques, Paul Barbaste, Olivier Oullier"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "neuroscience"
fetched: "2026-06-26T06:00:20.705299"
arxiv_id: "http://arxiv.org/abs/2606.24394v1"
source_api: "arxiv"
categories: "cs.HC, cs.AI, cs.RO, q-bio.NC"
---

# Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders

**著者**: Xavier Vasques, Paul Barbaste, Olivier Oullier
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: 脳科学

## Abstract

Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (feature extractor x scaler x classifier), >340,000 subject-level model fits, across three public left-versus-right motor-imagery datasets (PhysionetMI, 109 participants; Cho2017, 52; Zhou2016, 4) and two frequency bands (8-15 Hz, 8-30 Hz). Every model is fit and tested within a single session of a single participant, the easiest regime, giving every pipeline its best chance. We apply the statistics standard for multi-classifier comparison: Friedman omnibus tests, Nemenyi critical-difference analysis and Wilcoxon signed-rank tests with effect sizes. Covariance tangent-space projection (cov-tgsp) and Common Spatial Patterns (CSP) are the strongest families, but their ordering is dataset-dependent and, on the largest and most heterogeneous cohort (PhysionetMI), statistically indistinguishable (Nemenyi p = 0.27; Kendall's W = 0.11). At the individual level the single best pipeline is optimal for only 35% of PhysionetMI participants, and nonlinear descriptors are best for roughly one third; matching pipeline to participant adds about seven accuracy points over the best fixed choice. The ranking is not an artefact of dimensionality, and classifier and scaler choices are secondary to the feature representation. Even in the easiest regime, no single pipeline dominates: a lower bound on the personalization problem and a quantitative case for participant-aware model selection rather than a universal decoder.
