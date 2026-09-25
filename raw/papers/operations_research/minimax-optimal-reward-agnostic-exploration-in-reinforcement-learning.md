---
title: "Minimax-Optimal Reward-Agnostic Exploration in Reinforcement Learning"
authors: "Gen Li, Yuling Yan, Yuxin Chen, Jianqing Fan"
year: 2026
citations: 2
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-27T15:31:45.419220"
doi: "https://doi.org/10.1287/moor.2024.0538"
openalex_id: "https://openalex.org/W4366289288"
source_api: "openalex"
---

# Minimax-Optimal Reward-Agnostic Exploration in Reinforcement Learning

**著者**: Gen Li, Yuling Yan, Yuxin Chen, Jianqing Fan
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

This paper studies reward-agnostic exploration in reinforcement learning (RL)—a scenario where the learner is unaware of the reward functions during the exploration stage—and designs an algorithm that improves over the state of the art. More precisely, consider a finite-horizon inhomogeneous Markov decision process with S states, A actions, and horizon length H, and suppose that there are no more than a polynomial number of given reward functions of interest. By collecting an order of[Formula: see text]without the guidance of the reward information, our algorithm is able to find [Formula: see text]-optimal policies for all these reward functions, provided that [Formula: see text] is sufficiently small. This forms the first reward-agnostic exploration scheme in this context that is nearly minimax optimal. Furthermore, once the sample size exceeds [Formula: see text] episodes (up to log factor), our algorithm is able to yield [Formula: see text] accuracy for arbitrarily many reward functions (even when they are adversarially designed), a task commonly dubbed as “reward-free exploration.” The novelty of our algorithm design draws on insights from offline RL: The exploration scheme attempts to maximize a critical reward-agnostic quantity that dictates the performance of offline RL, whereas the policy learning paradigm leverages ideas from sample-optimal offline RL paradigms. Funding: This work was supported by Google, the Alfred P. Sloan Foundation, the Air Force Office of Scientific Research [Grant FA9550-22-1-0198], the National Science Foundation [Grants 1907661, 2210833, 2221009, and 2433450], and the Office of Naval Research [Grants N00014-22-1-2340 and N00014-22-1-2354].
