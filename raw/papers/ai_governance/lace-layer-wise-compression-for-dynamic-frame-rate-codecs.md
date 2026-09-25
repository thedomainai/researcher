---
title: "LACE: Layer-Wise Compression for Dynamic Frame Rate Codecs"
authors: "Thanapat Trachu, Samuele Cornell, William Chen, Shinji Watanabe"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-17T06:03:51.258453"
arxiv_id: "http://arxiv.org/abs/2609.17509v1"
source_api: "arxiv"
categories: "cs.SD, cs.AI, cs.CL"
---

# LACE: Layer-Wise Compression for Dynamic Frame Rate Codecs

**著者**: Thanapat Trachu, Samuele Cornell, William Chen, Shinji Watanabe
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Neural audio codecs are a key component in speech language modeling. However, their high frame rates lead to long sequence lengths, increasing computational costs. Dynamic frame rate codecs mitigate this by reducing the effective frame rate using a compression step to merge multiple frames together. However, most prior methods either operate on single-codebook codecs or apply a single compression step before multi-layer quantization. This forces all quantization layers to share the same segmentation boundaries, despite the residual embeddings at different quantization layers exhibiting different rates of change over time. We propose LACE (Layer-Adaptive Codec Encoding), a dynamic frame rate codec that applies an independent compression step at each quantization layer, enabling layer-specific segmentation boundaries. To use LACE tokens in downstream text-to-speech (TTS), we further introduce union alignment and boundary anchor mechanisms to make durations consistent across layers while preserving compression benefits. Experiments on LibriTTS show that LACE offers a better rate-quality tradeoff than prior dynamic frame rate methods on the reconstruction task and improves TTS inference efficiency while maintaining competitive synthesis quality. Our code is released as part of the ESPnet3 codec recipe.
