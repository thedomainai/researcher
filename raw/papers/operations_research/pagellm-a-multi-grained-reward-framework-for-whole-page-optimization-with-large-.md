---
title: "PageLLM: A Multi-Grained Reward Framework for Whole-Page Optimization with Large Language Models"
authors: "Xinyuan Wang, Liang Wu, Dongjie Wang, Yanjie Fu"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-04T06:55:05.365759"
doi: "https://doi.org/10.1145/3799682.3840685"
openalex_id: "https://openalex.org/W4417307855"
source_api: "openalex"
---

# PageLLM: A Multi-Grained Reward Framework for Whole-Page Optimization with Large Language Models

**著者**: Xinyuan Wang, Liang Wu, Dongjie Wang, Yanjie Fu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Whole-page optimization (WPO) decides how search and recommendation results are surfaced to users, and large language models (LLMs) open a new route to it by treating page generation as sequence generation. Adapting LLMs to web-scale WPO, however, remains bottlenecked by the need for costly human annotations and by the mismatched granularity between page-level coherence and item-level placement. In this work we show that these two challenges are coupled: implicit user feedback alone suffices for alignment, provided the reward signal is decoupled into two complementary granularities. We propose PageLLM, a reward-based fine-tuning framework that (i) turns implicit feedback into four contrastive preference-pair families covering relevance, ranking, diversity, and redundancy, (ii) learns a coarse page-level reward and a fine item-level reward that captures engagement-sensitive position swaps, and (iii) combines both rewards in PPO-based RLHF over a pre-trained LLM. Extensive experiments on seven Amazon categories against eleven baselines show that neither reward alone is sufficient -- dropping the page-level or item-level signal reduces NDCG@100 by 17.8% and 15.2% respectively, whereas the joint reward improves NDCG@100 by up to 46.8%. Deployed in a 10M-user online A/B test, PageLLM raises GMV by 0.44% and click-through rate by 0.14%, confirming that multi-grained rewards from implicit feedback scale to production WPO. Code and data are available at an anonymized repository.
