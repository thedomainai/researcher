---
title: "Sparse autoencoders reveal interpretable cell-type programs in single-cell foundation model representations"
authors: ["Ihor Kendiukhov"]
year: 2026
cited_by_count: 3
doi: "https://doi.org/10.1016/j.jbi.2026.105056"
openalex_id: W7161630786
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Sparse autoencoders reveal interpretable cell-type programs in single-cell foundation model representations

**Authors**: Ihor Kendiukhov | **Year**: 2026 | **Cited by**: 3 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

OBJECTIVE: Single-cell foundation models such as scGPT learn rich representations of cellular identity, yet the biological programs encoded in their internal activations remain opaque. We investigate whether sparse autoencoders (SAEs), a mechanistic interpretability technique from AI safety research, can decompose these representations into sparse, biologically interpretable features. METHODS: We extract residual-stream activations from all 12 transformer layers of a pre-trained scGPT model processing 1000 human immune cells from the Tabula Sapiens atlas. We train SAEs with dictionary size M=2,048 at multiple sparsity levels (λ∈{1,3,10}) and evaluate recovered features using cell-type classification (AUROC), gene set enrichment (Fisher's exact test, FDR <0.05), and comparison with PCA baselines. RESULTS: >0.76. Later-layer SAE features recover biologically coherent programs aligned with annotated cell types, with 64% of alive features receiving significant gene set annotations at layer 11 (λ=3). We observe a sparsity-dead-feature trade-off: at λ=10, up to 66% of dictionary elements become inactive. CONCLUSION: Mechanistic interpretability methods developed for large language models transfer productively to biological foundation models, but require domain-specific calibration. SAEs provide a principled approach to understanding what single-cell foundation models learn about cellular identity, with potential applications in model auditing and biological discovery.
