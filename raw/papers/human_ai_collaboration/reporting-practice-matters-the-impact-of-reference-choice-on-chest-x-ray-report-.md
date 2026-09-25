---
title: "Reporting Practice Matters: The Impact of Reference Choice on Chest X-ray Report Evaluation"
authors: "Daniel P. Jeong, Charles Q. Li, Hossein Hosseiny, Nitya M. Bhalla, Fatma Uyar Morency"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-18T06:03:21.549516"
arxiv_id: "http://arxiv.org/abs/2609.19093v1"
source_api: "arxiv"
categories: "cs.CL, cs.AI"
---

# Reporting Practice Matters: The Impact of Reference Choice on Chest X-ray Report Evaluation

**著者**: Daniel P. Jeong, Charles Q. Li, Hossein Hosseiny, Nitya M. Bhalla, Fatma Uyar Morency
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Radiologists follow heterogeneous reporting practices. Two radiologists examining the same image and identifying the same clinical findings might nevertheless compose superficially distinct reports, varying in terminology, shorthand, formatting, and level of detail. These variations in reporting norms represent an under-appreciated obstacle in efforts to evaluate AI-based radiology report generation (RRG) models, where machine-generated reports are typically assessed based on their concordance with human-generated references. In this paper, we quantify the sensitivity of established evaluation metrics to variations in reporting practices, revealing impacts large enough to alter the rankings of models. We introduce a radiologist-informed taxonomy of variations in radiology reporting practice and a method (ReRef) that rewrites reference reports along the axes of our taxonomy while preserving clinical interpretation. For instance, when comparing the performance of nine RRG models on MIMIC-CXR using RadCliQ-v1, condensing the discussion of normal findings in the reference reports causes Libra to drop from first to second place while CheXOne rises from third to first. Our results suggest that many current metrics fail to decouple clinical interpretation from conformity to reporting practices and that choosing the ``right'' references that accurately reflect the desired reporting practices can be important in practice. To support future research, we release MIMIC-CXR-Ext-ReRef, a radiologist-validated dataset of 120 (original, alternative) reference report pairs derived from MIMIC-CXR.
