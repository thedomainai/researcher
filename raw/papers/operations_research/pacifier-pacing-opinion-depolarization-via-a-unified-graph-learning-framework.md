---
title: "PACIFIER: Pacing Opinion Depolarization via a Unified Graph Learning Framework"
authors: "Mingkai Liao, Zijun Zhang, Mingyang Zhou"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-04T06:55:07.143859"
doi: "https://doi.org/10.1145/3799682.3840684"
openalex_id: "https://openalex.org/W7133241553"
source_api: "openalex"
---

# PACIFIER: Pacing Opinion Depolarization via a Unified Graph Learning Framework

**著者**: Mingkai Liao, Zijun Zhang, Mingyang Zhou
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Online social networks often form opposing echo chambers that reinforce opinion polarization. Under the Friedkin-Johnsen (FJ) model, ModerateInternal (MI) and ModerateExpressed (ME) reduce polarization by neutralizing selected users' internal or expressed opinions, but existing solutions are largely model-specific and learning-based depolarization remains underexplored. We study FJ-based moderation as feedback-free autoregressive sequential planning and propose PACIFIER, a unified graph-learning framework that constructs ordered intervention sequences from the initial graph-opinion instance without using recomputed post-intervention expressed opinions as intermediate feedback. PACIFIER combines history-aware node representations with Greedy and RL variants for immediate and long-horizon action scoring, and supports MI, ME, continuous opinions, cost-aware moderation, and node removal. We evaluate intervention trajectories by Accumulated Normalized Polarization (ANP). Trained only on synthetic graphs with fewer than 50 nodes, PACIFIER transfers to 15 real-world Twitter networks with up to 155,599 nodes. It improves over the strongest non-PACIFIER baseline by up to 35.3%, while PACIFIER-RL improves over PACIFIER-Greedy by up to 37.69%. Compared with oracle-style Greedy, PACIFIER retains 98.94% and 97.39% near-oracle quality on MI and ME, respectively, and is about 600x faster at the 450-node range. The source code is available at https://github.com/RickyYY-SZU/PACIFIER
