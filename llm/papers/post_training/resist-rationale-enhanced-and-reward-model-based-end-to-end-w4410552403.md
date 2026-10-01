---
title: "RESIST: Rationale-Enhanced and Reward Model-Based End-to-End Social Influence Dialogue System"
authors: ["Tong Wu", "Jinhua Zhu", "Wengang Zhou", "Houqiang Li"]
year: 2025
cited_by_count: 4
doi: "https://doi.org/10.1145/3736580"
openalex_id: W4410552403
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# RESIST: Rationale-Enhanced and Reward Model-Based End-to-End Social Influence Dialogue System

**Authors**: Tong Wu, Jinhua Zhu, Wengang Zhou, Houqiang Li | **Year**: 2025 | **Cited by**: 4 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Developing proactive social influence dialogue systems presents a significant challenge, particularly in non-cooperative scenarios where the system’s goals may conflict with those of the user. Traditional methods often focus on training models to plan dialogue strategies, but since human strategies are often sub-optimal, relying solely on manually collected data can be problematic. While Large Language Models (LLMs) facilitate the generation of high-quality synthetic dialogues, their effectiveness in strategic dialogue under zero-shot or few-shot conditions is inconsistent. To address these issues, we propose a training framework applicable to multiple social influence dialogue tasks, named R ationale-Enhanced and R eward Model-Based E nd-to-End S ocial I nfluence Dialogue S ys t em (RESIST) . To streamline the dialogue system development, we first use existing datasets to prompt a teacher LLM for generating “chain-of-thought” rationales, which are then used to enrich the data and enable Supervised Fine-Tuning (SFT) of the model. Next, we train a reward model by ranking the fine-tuned model’s outputs, thereby deriving task-specific preferences without manually constructing scalar rewards. Finally, we apply reinforcement learning to further refine the system, optimizing dialogue strategies and responses according to specific tasks and conversational contexts. Experimental results on three social influence tasks demonstrate the effectiveness and adaptability of our training approach. In terms of task goal completion , RESIST outperforms baseline models and even exceeds the performance of ChatGPT-driven prompt-based policy planning methods in both efficiency and effectiveness. Additionally, we introduce strategic proactivity as a novel evaluation metric, enabling us to analyze how RESIST training influences the proactive traits of dialogue agents, with a particular focus on the personality tendencies of smaller-scale language models during task execution. Experimental findings indicate that RESIST enhances the strategic proactivity of language models, aligning them more closely with task requirements. The source code will be made publicly available upon publication.
