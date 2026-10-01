---
title: "Sparse autoencoders uncover biologically interpretable features in protein language model representations"
authors: ["Onkar Singh Gujral", "Mihir Bafna", "Eric J. Alm", "Bonnie Berger"]
year: 2025
cited_by_count: 30
doi: "https://doi.org/10.1073/pnas.2506316122"
openalex_id: W4413312092
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Sparse autoencoders uncover biologically interpretable features in protein language model representations

**Authors**: Onkar Singh Gujral, Mihir Bafna, Eric J. Alm, Bonnie Berger | **Year**: 2025 | **Cited by**: 30 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Foundation models in biology-particularly protein language models (PLMs)-have enabled ground-breaking predictions in protein structure, function, and beyond. However, the "black-box" nature of these representations limits transparency and explainability, posing challenges for human-AI collaboration and leaving open questions about their human-interpretable features. Here, we leverage sparse autoencoders (SAEs) and a variant, transcoders, from natural language processing to extract, in a completely unsupervised fashion, interpretable sparse features present in both protein-level and amino acid (AA)-level representations from ESM2, a popular PLM. Unlike other approaches such as training probes for features, the extraction of features by the SAE is performed without any supervision. We find that many sparse features extracted from SAEs trained on protein-level representations are tightly associated with Gene Ontology (GO) terms across all levels of the GO hierarchy. We also use Anthropic's Claude to automate the interpretation of sparse features for both protein-level and AA-level representations and find that many of these features correspond to specific protein families and functions such as the NAD Kinase, IUNH, and the PTH family, as well as proteins involved in methyltransferase activity and in olfactory and gustatory sensory perception. We show that sparse features are more interpretable than ESM2 neurons across all our trained SAEs and transcoders. These findings demonstrate that SAEs offer a promising unsupervised approach for disentangling biologically relevant information present in PLM representations, thus aiding interpretability. This work opens the door to safety, trust, and explainability of PLMs and their applications, and paves the way to extracting meaningful biological insights across increasingly powerful models in the life sciences.
