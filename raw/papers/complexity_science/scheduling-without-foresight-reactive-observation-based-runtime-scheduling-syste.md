---
title: "Scheduling Without Foresight: Reactive, Observation-Based Runtime Scheduling Systems for Unpredictable Workloads"
authors: "Jianru Ding"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-07-04T06:01:54.180975"
doi: "https://doi.org/10.6082/m6bv1-gyb16"
openalex_id: "https://openalex.org/W7166721503"
source_api: "openalex"
---

# Scheduling Without Foresight: Reactive, Observation-Based Runtime Scheduling Systems for Unpredictable Workloads

**著者**: Jianru Ding
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Modern computing systems increasingly face workloads whose resource demands cannot be known in advance. Workloads themselves are becoming more heterogeneous and irregular, the pipelines that compose them mix fundamentally different execution models, and growing power constraints force schedulers to operate within tight resource envelopes rather than simply provisioning for peak demand. The emergence of generative AI services such as LLM inference compounds this further, as the compute cost is inherently unpredictable. Existing systems either assume that future demands can be predicted from past behavior—an assumption that ranges from brittle to fundamentally impossible depending on the workload—or discard readily observable information and forgo adaptation entirely. This thesis argues for an alternative to prediction-based scheduling: rather than modeling future demand from historical data, each system reacts to a carefully chosen signal observed at runtime, which provides sufficient structure to schedule effectively even when full prediction is difficult or impractical. We demonstrate this across three systems. Robin-Hood addresses load balancing for hybrid workloads that combine in-memory and streaming tasks. By encapsulating both task types into a shared abstraction, Robin-Hood decouples scheduling from data source, enabling a single two-level hierarchical scheduler that combines local atomic claiming with locality-aware work stealing across both modalities. In overprovisioned distributed systems, a cluster-wide power budget must be divided among nodes whose demands fluctuate unpredictably. DPS manages this without application profiling or learned models. Instead, it tracks power dynamics—the first derivative and frequency of recent power changes—to anticipate near-future demand and distribute the budget fairly, while guaranteeing no worse performance than a static equal allocation. For multi-turn LLM agentic workloads, total compute is unknowable at arrival, yet most of it is decode that should remain on a single replica to reuse the KV cache. ConServe turns this apparent obstacle into a scheduling advantage by disaggregating only the first-turn prefill, the one expensive and predictable piece, from everything else. This decomposition renders the scheduling problem fully observable: prefiller utilization determines queueing time and decoder utilization determines end-to-end latency, both known when a request arrives. Where prior serving systems formulate scheduling as a constrained optimization that requires predicting conversation length and output size, ConServe chooses a decomposition that eliminates the need for such prediction. The resulting architecture maps naturally onto heterogeneous GPU clusters, assigning first-turn prefill to high-power GPUs and the rest to lower-power GPUs with comparable memory bandwidth, achieving improved performance with better power scaling. Robin-Hood achieves up to 3.22× speedup over static scheduling, DPS outperforms SLURM's power manager by a mean 8\%, and ConServe reduces job completion latency by up to 25\% at saturation. Together, these results demonstrate that across scheduling, power management, and inference serving, the right abstraction often matters more than the right prediction. In each domain, a single well-chosen runtime signal recovers much of the performance gap between naive baselines and oracle systems, suggesting that this lightweight, signal-driven approach offers a broadly applicable design principle for systems facing unpredictable demands.
