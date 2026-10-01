---
title: "Efficient large-scale language model training on GPU clusters using megatron-LM"
authors: ["Deepak Narayanan", "Mohammad Shoeybi", "Jared Casper", "Patrick LeGresley", "Mostofa Ali Patwary", "Vijay Anand Korthikanti", "Dmitri Vainbrand", "Prethvi Kashinkunti", "et al."]
year: 2021
cited_by_count: 574
doi: "https://doi.org/10.1145/3458817.3476209"
openalex_id: W3187255235
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Efficient large-scale language model training on GPU clusters using megatron-LM

**Authors**: Deepak Narayanan, Mohammad Shoeybi, Jared Casper, Patrick LeGresley, Mostofa Ali Patwary, Vijay Anand Korthikanti, Dmitri Vainbrand, Prethvi Kashinkunti, et al. | **Year**: 2021 | **Cited by**: 574 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Large language models have led to state-of-the-art accuracies across several tasks. However, training these models efficiently is challenging because: a) GPU memory capacity is limited, making it impossible to fit large models on even a multi-GPU server, and b) the number of compute operations required can result in unrealistically long training times. Consequently, new methods of model parallelism such as tensor and pipeline parallelism have been proposed. Unfortunately, naive usage of these methods leads to scaling issues at thousands of GPUs. In this paper, we show how tensor, pipeline, and data parallelism can be composed to scale to thousands of GPUs. We propose a novel interleaved pipelining schedule that can improve throughput by 10+% with memory footprint comparable to existing approaches. Our approach allows us to perform training iterations on a model with 1 trillion parameters at 502 petaFLOP/s on 3072 GPUs (per-GPU throughput of 52% of theoretical peak).
