---
title: "ALPaCA: Adapting Llama for Pathology Context Analysis to enable slide-level question answering"
authors: "Zeyu Gao, Kai He, Weiheng Su, Xiaobo Pang, Inês Machado"
year: 2026
citations: 3
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-08-29T06:00:52.220837"
doi: "https://doi.org/10.1038/s41467-026-76372-z"
openalex_id: "https://openalex.org/W4409710058"
source_api: "openalex"
---

# ALPaCA: Adapting Llama for Pathology Context Analysis to enable slide-level question answering

**著者**: Zeyu Gao, Kai He, Weiheng Su, Xiaobo Pang, Inês Machado
**年**: 2026 | **被引用数**: 3
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Abstract Large Vision Language Models (LVLMs) are increasingly used in computational pathology for image classification, description generation, question answering and interactive diagnostics. However, most pathology LVLMs analyse small regions of interest rather than pyramidal, gigapixel-scale whole-slide images (WSIs), limiting their use for tasks requiring whole-slide assessment across sub-regions and magnification levels. Here, we present ALPaCA (Adapting Llama for Pathology Context Analysis), a slide-level LVLM framework for WSI question answering across diverse cancer types and tissue sites. ALPaCA is trained using 35,913 WSIs with curated descriptions and 341,051 question-answer pairs from TCGA and GTEx. It combines a LongFormer vision-text adaptor with a Gaussian mixture model-based prototyping adaptor and Llama3.1. ALPaCA exceeds 90% accuracy on internal close-ended benchmarks and maintains 77–82% accuracy on independent external cohorts. Expert pathologist evaluation of open-ended responses supports its slide-level reasoning capability. Additionally, ALPaCA can be fine-tuned on organ- or disease-specific datasets, supporting specialised pathology question answering.
