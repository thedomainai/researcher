---
title: "RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics"
authors: "W. Chen, Song Liao"
year: 2026
citations: 0
paper_type: "primary"
domain: "leadership_ob"
fetched: "2026-11-04T06:55:14.107653"
doi: "https://doi.org/10.1145/3799682.3839887"
openalex_id: "https://openalex.org/W7221530276"
source_api: "openalex"
---

# RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics

**著者**: W. Chen, Song Liao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: リーダーシップ・組織行動

## Abstract

As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline retrieval and dynamic reliability evaluation. Experimental results demonstrate that RATED achieves a 52.2% relative MRR improvement over the ToolLLM API retriever on real-world queries, and reduces fault selection rate from 86.2% to 2.9% under severe API outage scenarios with a 30% failure rate, while incurring negligible latency overhead of less than 1 ms over encode-only inference. The code and dataset are available at https://github.com/Elliotes/EcoAgent.
