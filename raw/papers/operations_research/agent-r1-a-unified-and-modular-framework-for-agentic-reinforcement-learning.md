---
title: "Agent-R1: A Unified and Modular Framework for Agentic Reinforcement Learning"
authors: "Mingyue Cheng, Shuo Yu, Daoyu Wang, Qingchuan Li, Xiaoyu Tao"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-04T06:55:00.139940"
doi: "https://doi.org/10.1145/3799682.3840255"
openalex_id: "https://openalex.org/W7106156359"
source_api: "openalex"
---

# Agent-R1: A Unified and Modular Framework for Agentic Reinforcement Learning

**著者**: Mingyue Cheng, Shuo Yu, Daoyu Wang, Qingchuan Li, Xiaoyu Tao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Large language models (LLMs) have rapidly evolved from single-turn text generators into the foundation of increasingly capable agents. As these agents take on more complex reasoning, decision making, tool use, and long-horizon tasks, reinforcement learning (RL) is becoming increasingly important for shaping their behavior. This shift is especially visible in agentic RL, where models must interact with tools and environments across multiple rounds rather than produce a single standalone response. In this regime, the usual view of a trajectory as one ever-growing token sequence becomes increasingly inadequate: it makes context evolution rigid and creates representation mismatches between rollout and training. This paper presents Agent-R1, a unified and modular framework for agentic RL built around step-level trajectory representation, flexible context management, and layered interfaces for workflows, environments and optimization. The key idea is to treat each interaction step as the basic reinforcement-learning transition, while keeping the optimization layer flexible: once the interaction is modeled at the step level, the framework can support token-level credit assignment, step-level credit assignment, or other compatible designs. These design choices make the framework compatible with a range of optimization strategies rather than tying it to a single algorithm. Together, these components provide a principled, extensible, and reusable substrate for agentic RL.
