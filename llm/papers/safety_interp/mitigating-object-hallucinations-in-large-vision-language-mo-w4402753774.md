---
title: "Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding"
authors: ["Sicong Leng", "Hang Zhang", "Guanzheng Chen", "Xin Shane Li", "Shijian Lu", "Chunyan Miao", "Lidong Bing"]
year: 2024
cited_by_count: 172
doi: "https://doi.org/10.1109/cvpr52733.2024.01316"
openalex_id: W4402753774
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding

**Authors**: Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Shane Li, Shijian Lu, Chunyan Miao, Lidong Bing | **Year**: 2024 | **Cited by**: 172 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Large Vision-Language Models (LVLMs) have advanced considerably, intertwining visual recognition and language understanding to generate content that is not only coherent but also contextually attuned. Despite their success, LVLMs still suffer from the issue of object hallucinations, where models generate plausible yet incorrect outputs that include objects that do not exist in the images. To mitigate this issue, we introduce Visual Contrastive Decoding (VCD), a simple and training-free method that contrasts output distributions derived from original and distorted visual inputs. The proposed VCD effectively reduces the over-reliance on statistical bias and unimodal priors, two essential causes of object hallucinations. This adjustment ensures the generated content is closely grounded to visual inputs, resulting in contextually accurate outputs. Our experiments show that VCD, without either additional training or the usage of external tools, significantly mitigates the object hallucination issue across different LVLM families. Beyond mitigating object hallucinations, VCD also excels in general LVLM benchmarks, highlighting its wide-ranging applicability.
