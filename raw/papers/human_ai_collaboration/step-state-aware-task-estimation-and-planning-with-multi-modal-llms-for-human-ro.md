---
title: "STEP: State-Aware Task Estimation and Planning with Multi-Modal LLMs for Human-Robot Collaboration"
authors: "Maitrey Gramopadhye, Prakash Baskaran, Xiao Liu, Songpo Li, Soshi Iba"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-08-29T06:03:26.305049"
arxiv_id: "http://arxiv.org/abs/2608.27225v1"
source_api: "arxiv"
categories: "cs.RO, cs.AI"
---

# STEP: State-Aware Task Estimation and Planning with Multi-Modal LLMs for Human-Robot Collaboration

**著者**: Maitrey Gramopadhye, Prakash Baskaran, Xiao Liu, Songpo Li, Soshi Iba
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Effective human-robot collaboration in industrial settings requires robots to understand human intentions and assist with task planning, reducing workload. Recent works have explored the use of Multi-modal Large Language Models (MM-LLMs) for task planning in such data-scarce scenarios, leveraging in-context learning to interpret user actions and generate long-horizon action plans in natural language. However, MM-LLMs inherently lack an understanding of system states and do not track state transitions, often leading to hallucinated actions that deviate from the intended goal. Additionally, generating action plans in natural language tends to limit the generated plans to a high level, introducing ambiguity in action execution. To address these limitations, we propose the State-aware Task Estimator and Planner (STEP), which prompts a MM-LLM to explicitly estimate the state of the system and predict the state transitions resulting from executed actions. By forecasting future states alongside actions, STEP ensures task-convergent planning while also providing additional assistance parameters necessary for executing the predicted actions. We evaluate STEP in a simulated environment using a robot assembly task. Our approach outperforms the state-of-the-art by 32.8% in action executability and 14.8% in final-state error.
