---
title: "BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks"
authors: "Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs, Julian Moncarz, Kaustubh Kislay"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-02T08:56:45.471354"
arxiv_id: "http://arxiv.org/abs/2608.30724v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI"
---

# BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks

**著者**: Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs, Julian Moncarz, Kaustubh Kislay
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

LLM agents are increasingly used to run autonomous ML experiments, iterating on target metrics with little human oversight. Prior work has documented reward hacking in these environments, bringing into question the validity of produced research and the broader safety case for AI R&D. Existing benchmarks do not measure exploits that live in the data or the modeling task itself. We introduce BAITBENCH, a suite of three synthetic tabular ML tasks that each contain a shortcut that allows agents to inflate the public test score but fail on a hidden test set. Since the shortcut is optional and using it breaks no stated rule, BAITBENCH measures how often models exploit the shortcut to achieve inflated scores. Across seven frontier agents scored by our two-stage judge pipeline, 57.1% of runs exhibit reward hacking, with five of seven above 50%. Agents cheat even under a second condition where they are prompted not to -the mean cheating rate remains above 50%. We release BAITBENCH, along with the judge implementation, and an annotated dataset of transcripts containing reward hacks as a testbed for evaluating reward-hacking mitigations head-to-head.
