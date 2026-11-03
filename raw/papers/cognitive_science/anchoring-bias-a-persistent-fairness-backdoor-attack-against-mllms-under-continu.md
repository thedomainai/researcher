---
title: "Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning"
authors: "Yuyang Luo, Kai Shu"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-11-04T06:16:45.960957"
doi: "https://doi.org/10.1145/3799682.3841079"
openalex_id: "https://openalex.org/W7204156395"
source_api: "openalex"
---

# Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning

**著者**: Yuyang Luo, Kai Shu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

Multimodal Large Language Models (MLLMs) are increasingly deployed in high-stakes domains where fairness is a critical safety requirement. In practice, these models are continually updated through continual learning (CL) to adapt to evolving tasks and data distributions. Prior work has shown that backdoor attacks can manipulate MLLM responses through hidden triggers, but naively implanted backdoors degrade as models undergo subsequent updates of CL. Although fairness has emerged as a central concern for MLLM deployment, whether backdoor-induced fairness violations can survive CL remains unexplored, leaving two critical questions unanswered: (1) whether a backdoor can reliably induce fairness violations in MLLMs, and (2) whether such fairness-targeted backdoors can persist through continual learning. We bridge this gap by proposing Persistent Fairness Backdoor Attack (PFBA) to inject persistent and group-specific discrimination into MLLMs. Specifically, PFBA achieves this through two novel mechanisms. The Latent Space Fairness Reinforcement reshapes the model's deep feature geometry by anchoring privileged-group representations to preserve utility while repelling and clustering targeted-group representations to sustain discrimination, and the Continual Learning Simulation iteratively optimizes the trigger against simulated parameter drift to ensure backdoor persistence across future updates. Extensive experiments demonstrate that PFBA induces severe fairness disparities that persist across continual learning rounds, evading standard backdoor defenses. The data and code are publicly available at https://github.com/lyygua/PFBA.
