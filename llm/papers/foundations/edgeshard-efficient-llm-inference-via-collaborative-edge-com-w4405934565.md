---
title: "EdgeShard: Efficient LLM Inference via Collaborative Edge Computing"
authors: ["Mingjin Zhang", "Xiaoming Shen", "Jiannong Cao", "Zeyang Cui", "Shan Jiang"]
year: 2024
cited_by_count: 215
doi: "https://doi.org/10.1109/jiot.2024.3524255"
openalex_id: W4405934565
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# EdgeShard: Efficient LLM Inference via Collaborative Edge Computing

**Authors**: Mingjin Zhang, Xiaoming Shen, Jiannong Cao, Zeyang Cui, Shan Jiang | **Year**: 2024 | **Cited by**: 215 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Large language models (LLMs) have shown great success in content generation and intelligent intelligent decision making for IoT systems. Traditionally, LLMs are deployed on the cloud, incurring prolonged latency, high bandwidth costs, and privacy concerns. More recently, edge computing has been considered promising in addressing such concerns because the edge devices are closer to data sources. However, edge devices are cursed by their limited resources and can hardly afford LLMs. Existing studies address such a limitation by offloading heavy workloads from edge to cloud or compressing LLMs via model quantization. These methods either still rely heavily on the remote cloud or suffer substantial accuracy loss. This work is the first to deploy LLMs on a collaborative edge computing environment, in which edge devices and cloud servers share resources and collaborate to infer LLMs with high efficiency and no accuracy loss. We design EdgeShard, a novel approach to partition a computation-intensive LLM into affordable shards and deploy them on distributed devices. The partition and distribution are nontrivial, considering device heterogeneity, bandwidth limitations, and model complexity. To this end, we formulate an adaptive joint device selection and model partition problem and design an efficient dynamic programming algorithm to optimize the inference latency and throughput. Extensive experiments of the popular Llama2 serial models on a real-world testbed reveal that EdgeShard achieves up to 50% latency reduction and$2 \times $throughput improvement over the state-of-the-art.
