---
title: "FDA-Opt: Federated Fine-Tuning via Dynamic Update Schedules"
authors: "Michail Theologitis, Vasilis Samoladas, Antonios Deligiannakis"
year: 2026
citations: 0
paper_type: "primary"
domain: "strategic_management"
fetched: "2026-11-04T06:53:19.945261"
doi: "https://doi.org/10.1145/3799682.3840785"
openalex_id: "https://openalex.org/W4414681923"
source_api: "openalex"
---

# FDA-Opt: Federated Fine-Tuning via Dynamic Update Schedules

**著者**: Michail Theologitis, Vasilis Samoladas, Antonios Deligiannakis
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経営戦略

## Abstract

Federated Learning (FL) enables the utilization of vast, previously inaccessible data sources. At the same time, pre-trained Language Models (LMs) have taken the world by storm and for good reason. They exhibit remarkable emergent abilities and are readily adapted to downstream tasks. This opens one of the most exciting frontiers in FL: fine-tuning LMs. Yet, a persistent challenge in FL is the frequent, rigid communication of parameters -- a problem magnified by the sheer size of these contemporary models. The FedOpt family of algorithms has become the go-to approach for FL, relying on fixed but arbitrary intervals for model exchanges. Recently, the FDA algorithm prescribed a dynamic approach by monitoring the training progress. However, it introduced a hard-to-calibrate parameter and imposed a rigid synchronization scheme. In this work, we address these limitations by proposing the FDA-Opt family of algorithms -- a unified generalization of both FDA and FedOpt. Our experimental evaluation focuses on fine-tuning LMs on downstream NLP tasks and demonstrates that FDA-Opt outperforms FedOpt even when it is configured with hyper-parameters specifically optimized for the latter. In other words, we show that FDA-Opt is a practical, drop-in replacement for FedOpt in modern FL libraries and systems: it requires no additional configuration and delivers superior performance out of the box.
