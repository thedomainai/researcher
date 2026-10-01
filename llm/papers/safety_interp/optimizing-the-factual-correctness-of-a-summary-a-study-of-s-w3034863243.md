---
title: "Optimizing the Factual Correctness of a Summary: A Study of Summarizing Radiology Reports"
authors: ["Yuhao Zhang", "Derek L. Merck", "Emily B. Tsai", "Christopher D. Manning", "Curtis P. Langlotz"]
year: 2020
cited_by_count: 163
doi: "https://doi.org/10.18653/v1/2020.acl-main.458"
openalex_id: W3034863243
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Optimizing the Factual Correctness of a Summary: A Study of Summarizing Radiology Reports

**Authors**: Yuhao Zhang, Derek L. Merck, Emily B. Tsai, Christopher D. Manning, Curtis P. Langlotz | **Year**: 2020 | **Cited by**: 163 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Neural abstractive summarization models are able to generate summaries which have high overlap with human references.However, existing models are not optimized for factual correctness, a critical metric in real-world applications.In this work, we develop a general framework where we evaluate the factual correctness of a generated summary by factchecking it automatically against its reference using an information extraction module.We further propose a training strategy which optimizes a neural summarization model with a factual correctness reward via reinforcement learning.We apply the proposed method to the summarization of radiology reports, where factual correctness is a key requirement.On two separate datasets collected from hospitals, we show via both automatic and human evaluation that the proposed approach substantially improves the factual correctness and overall quality of outputs over a competitive neural summarization system, producing radiology summaries that approach the quality of humanauthored ones.Background: radiographic examination of the chest.clinical history: 80 years of age, male ... Findings: frontal radiograph of the chest demonstrates repositioning of the right atrial lead possibly into the ivc.... a right apical pneumothorax can be seen from the image.moderate right and small left pleural effusions continue.no pulmonary edema is observed.heart size is upper limits of normal. Human Summary: pneumothorax is seen. bilateral pleural effusions continue.Summary A (ROUGE-L = 0.77): no pneumothorax is observed.bilateral pleural effusions continue.Summary B (ROUGE-L = 0.44): pneumothorax is observed on radiograph.bilateral pleural effusions continue to be seen.
