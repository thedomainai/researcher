---
title: "ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models"
authors: "Wencheng Ye, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen"
year: 2026
citations: 7
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-11-08T06:01:31.203985"
doi: "https://doi.org/10.1145/3767308.3835716"
openalex_id: "https://openalex.org/W7106700227"
source_api: "openalex"
---

# ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models

**著者**: Wencheng Ye, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen
**年**: 2026 | **被引用数**: 7
**タイプ**: primary | **分野**: 脳科学

## Abstract

Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.
