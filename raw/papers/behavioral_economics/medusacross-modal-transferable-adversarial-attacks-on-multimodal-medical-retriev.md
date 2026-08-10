---
title: "Medusa:Cross-Modal Transferable Adversarial Attacks on Multimodal Medical Retrieval-Augmented Generation"
authors: "Yingjia Shang, Yi; id_orcid 0000-0002-0811-6150 Liu, H Wang, Feng Li, Wenfang Sun"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-07-07T06:01:10.933668"
doi: "https://doi.org/10.1145/3770854.3780277"
openalex_id: "https://openalex.org/W7165142990"
source_api: "openalex"
---

# Medusa:Cross-Modal Transferable Adversarial Attacks on Multimodal Medical Retrieval-Augmented Generation

**著者**: Yingjia Shang, Yi; id_orcid 0000-0002-0811-6150 Liu, H Wang, Feng Li, Wenfang Sun
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

With the rapid advancement of retrieval-augmented vision-language models, multimodal medical retrieval-augmented generation (MMed-RAG) systems are increasingly adopted in clinical decision support. These systems enhance medical applications by performing cross-modal retrieval to integrate relevant visual and textual evidence for tasks, e.g., report generation and disease diagnosis. However, their complex architecture also introduces underexplored adversarial vulnerabilities, particularly via visual input perturbations. In this paper, we propose Medusa, a novel framework for crafting cross-modal transferable adversarial attacks on MMed-RAG systems under a black-box setting. Specifically, Medusa formulates the attack as a perturbation optimization problem, leveraging a multi-positive InfoNCE loss (MPIL) to align adversarial visual embeddings with medically plausible but malicious textual targets, thereby hijacking the retrieval process. To enhance transferability, we adopt a surrogate model ensemble and design a dual-loop optimization strategy augmented with invariant risk minimization (IRM). Extensive experiments on two real-world medical tasks, including medical report generation and disease diagnosis, demonstrate that Medusa achieves over 90% average attack success rate across various generation models and retrievers under appropriate parameter configuration, while remaining robust against four mainstream defenses, outperforming state-of-the-art baselines. Our results reveal critical vulnerabilities in the MMed-RAG systems and highlight the necessity of robustness benchmarking in safety-critical medical applications. The code and data are available at https://github.com/yiliucs/MMed-RAG-Attack. © 2026 Owner/Author.
