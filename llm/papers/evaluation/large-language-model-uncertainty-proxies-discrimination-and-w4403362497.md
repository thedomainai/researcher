---
title: "Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment"
authors: ["Thomas Savage", "John Wang", "Robert J. Gallo", "Abdessalem Boukil", "Vishwesh Patel", "Seyed Amir Ahmad Safavi‐Naini", "Ali Soroush", "Jonathan H. Chen"]
year: 2024
cited_by_count: 86
doi: "https://doi.org/10.1093/jamia/ocae254"
openalex_id: W4403362497
paper_type: article
evidence_kind: article
topics: ["evaluation"]
landmark: false
abstract_source: "openalex"
---

# Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment

**Authors**: Thomas Savage, John Wang, Robert J. Gallo, Abdessalem Boukil, Vishwesh Patel, Seyed Amir Ahmad Safavi‐Naini, Ali Soroush, Jonathan H. Chen | **Year**: 2024 | **Cited by**: 86 | **Kind**: article | **Relevance**: evaluation: supporting

## Abstract

INTRODUCTION: The inability of large language models (LLMs) to communicate uncertainty is a significant barrier to their use in medicine. Before LLMs can be integrated into patient care, the field must assess methods to estimate uncertainty in ways that are useful to physician-users. OBJECTIVE: Evaluate the ability for uncertainty proxies to quantify LLM confidence when performing diagnosis and treatment selection tasks by assessing the properties of discrimination and calibration. METHODS: We examined confidence elicitation (CE), token-level probability (TLP), and sample consistency (SC) proxies across GPT3.5, GPT4, Llama2, and Llama3. Uncertainty proxies were evaluated against 3 datasets of open-ended patient scenarios. RESULTS: SC discrimination outperformed TLP and CE methods. SC by sentence embedding achieved the highest discriminative performance (ROC AUC 0.68-0.79), yet with poor calibration. SC by GPT annotation achieved the second-best discrimination (ROC AUC 0.66-0.74) with accurate calibration. Verbalized confidence (CE) was found to consistently overestimate model confidence. DISCUSSION AND CONCLUSIONS: SC is the most effective method for estimating LLM uncertainty of the proxies evaluated. SC by sentence embedding can effectively estimate uncertainty if the user has a set of reference cases with which to re-calibrate their results, while SC by GPT annotation is the more effective method if the user does not have reference cases and requires accurate raw calibration. Our results confirm LLMs are consistently over-confident when verbalizing their confidence (CE).
