---
title: "Reasoning with Language Model is Planning with World Model"
authors: ["Shibo Hao", "Yi Gu", "Haodi Ma", "Joshua Hong", "Zhen Wang", "Daisy Wang", "Zhiting Hu"]
year: 2023
cited_by_count: 145
doi: "https://doi.org/10.18653/v1/2023.emnlp-main.507"
openalex_id: W4389520747
paper_type: conference-paper
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Reasoning with Language Model is Planning with World Model

**Authors**: Shibo Hao, Yi Gu, Haodi Ma, Joshua Hong, Zhen Wang, Daisy Wang, Zhiting Hu | **Year**: 2023 | **Cited by**: 145 | **Kind**: article | **Relevance**: agents: core

## Abstract

Large language models (LLMs) have shown remarkable reasoning capabilities, particularly with chain-of-thought (CoT) prompting.However, LLMs sometimes still struggle with problems that are easy for humans, such as generating action plans to achieve given goals in an environment, or performing complex math or logical reasoning.The deficiency stems from the key fact that LLMs lack an internal world model to predict the world state (e.g., environment status, intermediate variable values) and simulate long-term outcomes of actions.This prevents LLMs from performing deliberate planning akin to human brains, which involves exploring alternative reasoning paths, anticipating future states and rewards, and iteratively refining existing reasoning steps.To overcome the limitations, we propose a new LLM reasoning framework, Reasoning via Planning (RAP).RAP repurposes the LLM as both a world model and a reasoning agent, and incorporates a principled planning algorithm based on Monte Carlo Tree Search for strategic exploration in the vast reasoning space.During reasoning, the LLM (as agent) incrementally builds a reasoning tree under the guidance of the LLM (as world model) and rewards, and efficiently obtains a high-reward reasoning path with a proper balance between exploration vs. exploitation.We apply RAP to various challenging reasoning problems including plan generation, math reasoning, and logical inference, and demonstrate its superiority over strong baselines.RAP with LLaMA-33B even surpasses CoT with GPT-4, achieving 33% relative improvement in a plan generation setting. 1
