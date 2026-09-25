---
title: "Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems"
authors: "Sara Vera Marjanović, Jiacheng Xu, Aleksandr Laptev, Grigor Nalbandyan, Erik Arakelyan"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-17T06:01:03.538353"
arxiv_id: "http://arxiv.org/abs/2609.17306v1"
source_api: "arxiv"
categories: "cs.MA, cs.AI"
---

# Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems

**著者**: Sara Vera Marjanović, Jiacheng Xu, Aleksandr Laptev, Grigor Nalbandyan, Erik Arakelyan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.
