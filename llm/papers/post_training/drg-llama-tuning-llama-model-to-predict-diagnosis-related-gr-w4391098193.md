---
title: "DRG-LLaMA : tuning LLaMA model to predict diagnosis-related group for hospitalized patients"
authors: ["Hanyin Wang", "Chufan Gao", "Christopher Dantona", "Bryan Hull", "Jimeng Sun"]
year: 2024
cited_by_count: 101
doi: "https://doi.org/10.1038/s41746-023-00989-3"
openalex_id: W4391098193
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# DRG-LLaMA : tuning LLaMA model to predict diagnosis-related group for hospitalized patients

**Authors**: Hanyin Wang, Chufan Gao, Christopher Dantona, Bryan Hull, Jimeng Sun | **Year**: 2024 | **Cited by**: 101 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

In the U.S. inpatient payment system, the Diagnosis-Related Group (DRG) is pivotal, but its assignment process is inefficient. The study introduces DRG-LLaMA, an advanced large language model (LLM) fine-tuned on clinical notes to enhance DRGs assignment. Utilizing LLaMA as the foundational model and optimizing it through Low-Rank Adaptation (LoRA) on 236,192 MIMIC-IV discharge summaries, our DRG-LLaMA -7B model exhibited a noteworthy macro-averaged F1 score of 0.327, a top-1 prediction accuracy of 52.0%, and a macro-averaged Area Under the Curve (AUC) of 0.986, with a maximum input token length of 512. This model surpassed the performance of prior leading models in DRG prediction, showing a relative improvement of 40.3% and 35.7% in macro-averaged F1 score compared to ClinicalBERT and CAML, respectively. Applied to base DRG and complication or comorbidity (CC)/major complication or comorbidity (MCC) prediction, DRG-LLaMA achieved a top-1 prediction accuracy of 67.8% and 67.5%, respectively. Additionally, our findings indicate that DRG-LLaMA 's performance correlates with increased model parameters and input context lengths.
