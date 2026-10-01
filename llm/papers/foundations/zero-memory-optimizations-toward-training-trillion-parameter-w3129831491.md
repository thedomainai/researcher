---
title: "ZeRO: Memory optimizations Toward Training Trillion Parameter Models"
authors: ["Samyam Rajbhandari", "Jeff Rasley", "Olatunji Ruwase", "Yuxiong He"]
year: 2020
cited_by_count: 850
doi: "https://doi.org/10.1109/sc41405.2020.00024"
openalex_id: W3129831491
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# ZeRO: Memory optimizations Toward Training Trillion Parameter Models

**Authors**: Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, Yuxiong He | **Year**: 2020 | **Cited by**: 850 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Large deep learning models offer significant accuracy gains, but training billions to trillions of parameters is challenging. Existing solutions such as data and model parallelisms exhibit fundamental limitations to fit these models into limited device memory, while obtaining computation, communication and development efficiency. We develop a novel solution, Zero Redundancy Optimizer (ZeRO), to optimize memory, vastly improving training speed while increasing the model size that can be efficiently trained. ZeRO eliminates memory redundancies in data- and model-parallel training while retaining low communication volume and high computational granularity, allowing us to scale the model size proportional to the number of devices with sustained high efficiency. Our analysis on memory requirements and communication volume demonstrates: ZeRO has the potential to scale beyond 1 Trillion parameters using today's hardware. We implement and evaluate ZeRO: it trains large models of over 100B parameter with super-linear speedup on 400 GPUs, achieving throughput of 15 Petaflops. This represents an 8x increase in model size and 10x increase in achievable performance over state-of-the-art. In terms of usability, ZeRO can train large models of up to 13B parameters (e.g., larger than Megatron GPT 8. 3B and T5 11B) without requiring model parallelism which is harder for scientists to apply. Last but not the least, researchers have used the system breakthroughs of ZeRO to create Turing-NLG, the world's largest language model at the time (17B parameters) with record breaking accuracy.
