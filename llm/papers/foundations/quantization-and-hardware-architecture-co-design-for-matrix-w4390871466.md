---
title: "Quantization and Hardware Architecture Co-Design for Matrix-Vector Multiplications of Large Language Models"
authors: ["Wenjie Li", "Aokun Hu", "Ningyi Xu", "Guanghui He"]
year: 2024
cited_by_count: 22
doi: "https://doi.org/10.1109/tcsi.2024.3350661"
openalex_id: W4390871466
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Quantization and Hardware Architecture Co-Design for Matrix-Vector Multiplications of Large Language Models

**Authors**: Wenjie Li, Aokun Hu, Ningyi Xu, Guanghui He | **Year**: 2024 | **Cited by**: 22 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Large language models (LLMs) have sparked a new revolution in the field of natural language processing (NLP), and have garnered tremendous attention in both academic research and everyday life, thanks to their unprecedented performance in a wide range of applications. However, their deployment remains a significant challenge, primarily due to their intensive computational and memory requirements. Hardware acceleration and efficient quantization are promising solutions to address the two issues. In this paper, a quantization and hardware architecture co-design is presented for matrix-vector multiplications (MVMs) of LLMs. During quantization, we uniformly group weights and activations to ensure workload balance for hardware. To enhance the performance of quantization, we further propose two approaches called channel sorting and channel selection, which can be applied simultaneously. To support the proposed quantization scheme, we develop two precision-scalable MVM hardware architectures. They are specifically designed for high speed and high energy efficiency, respectively. Experimental results show that our proposed quantization scheme achieves state-of-the-art performance among all the reported post-training schemes that quantize both weights and activations into integers. Compared to MVM architecture of the state-of-the-art LLM accelerator OliVe, our design exhibits significant advantages in terms of area efficiency and energy efficiency.
