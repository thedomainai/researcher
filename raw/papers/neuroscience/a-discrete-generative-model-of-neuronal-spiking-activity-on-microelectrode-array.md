---
title: "A discrete generative model of neuronal spiking activity on microelectrode arrays"
authors: "Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-23T06:00:24.996026"
arxiv_id: "http://arxiv.org/abs/2609.23907v1"
source_api: "arxiv"
categories: "cs.LG, eess.SP, q-bio.NC"
---

# A discrete generative model of neuronal spiking activity on microelectrode arrays

**著者**: Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a discrete generative model that represents this activity using a shared vocabulary of spatiotemporal motifs. A residual vector-quantized autoencoder learns the motif vocabulary, while a factorized masked transformer predicts where activity occurs and which motif appears at each active location. We evaluate the model on 31 assays spanning human brain organoids and acute \emph{ex vivo} human hippocampal tissue. The learned motifs are broadly reused: assay identity explains only $9%$ of the entropy in motif use, and motif overlap across tissue types is comparable to overlap within them. When representation quality is evaluated independently of the generative prior, our approach achieves $5.2\times$ the voxel-level reconstruction average precision of a matched flat tokenizer. For masked completion and free generation, the full model achieves $1.4$--$2.6\times$ the site-level average precision of the matched generative baseline and outperforms it across all four families of generation metrics. These results establish a compact, reusable representation for array-wide spiking activity without learned assay-specific parameters, providing a scalable foundation for generative modeling across diverse neural preparations.
