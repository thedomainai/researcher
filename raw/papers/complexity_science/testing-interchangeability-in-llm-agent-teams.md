---
title: "Testing Interchangeability in LLM Agent Teams"
authors: "Jianxin Gao, Tianyi Yu, Linna Deng, Runze Li, Zining Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-08T06:01:00.758235"
arxiv_id: "http://arxiv.org/abs/2609.05279v1"
source_api: "arxiv"
categories: "cs.AI, cs.MA"
---

# Testing Interchangeability in LLM Agent Teams

**著者**: Jianxin Gao, Tianyi Yu, Linna Deng, Runze Li, Zining Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Production multi-agent systems replace agents constantly, on the assumption that an agent filling a role is interchangeable with any other agent that can do the job. We test that assumption. Eight teams per setting are formed independently from one base model on the same tasks, each agent keeping a private notebook across ten formation episodes; we then trade role-matched agents between teams and measure what changes on held-out tasks. Against a placebo that reproduces the disruption of a roster change without changing who occupies the seat, a swap costs little in task score but raises the communication a team spends per unit of progress by 16 to 63 percent, and in Hanabi a swapped agent is more expensive than an inexperienced one, consistent with interference from conventions learned with its former partner. In Collab-Overcooked, when the agent that sets the agenda is replaced, most of the extra communication comes from the agent that stayed. Three ablations, over base models, decoding temperature and formation length, move the swap penalty alongside one other quantity: how far independently formed teams drift apart. Greedy decoding lowers both; doubling a team's history raises both. In these settings, agents are more fungible in task outcome than in coordination efficiency, with larger swap effects after longer formation histories.
