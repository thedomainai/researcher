---
title: "Multi-Phase Guidance and Control for Small Satellite Docking via Deep Reinforcement Learning"
authors: "Tanner Gill, Greg Furlich, Nisar Ahmed"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-24T18:51:17.584224"
doi: ""
openalex_id: "https://openalex.org/W7204015174"
source_api: "openalex"
---

# Multi-Phase Guidance and Control for Small Satellite Docking via Deep Reinforcement Learning

**著者**: Tanner Gill, Greg Furlich, Nisar Ahmed
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

As interest in small satellite Rendezvous, Proximity Operations, and Docking (RPOD) grows, so does the need for high-level autonomy in space systems. Current systems relying on constrained hardware and ground-in-the-loop decision-making are ill-equipped for the evolving, contested space domain. Recent research on autonomous spacecraft guidance and control has moved beyond established optimal control and trajectory optimization methods to incorporate Reinforcement Learning (RL), though these efforts have predominantly focused on a single operational phase. This research advances small satellite docking autonomy by formulating the reference scenario as a Hierarchical Markov Decision Process (H-MDP), expanding the scope of the learned guidance and control algorithm to span the full mission profile rather than one phase. This structure rewards the agile deputy satellite for learning to transition between mission phases, modifying its behavior from long-range rendezvous through final approach, and for adapting to changing conditions such as a shift in the chief satellite's pointing mode. The framework uses the Basilisk astrodynamics simulator and BSK-RL library to train a Proximal Policy Optimization (PPO) agent under high-fidelity orbital dynamics, creating a lightweight, robust training pipeline. The analysis quantifies total delta-V, docking ingress characteristics, and mission success across randomized initial conditions, with the trained policy achieving a 99.2% docking success rate over a 500-run Monte Carlo analysis, demonstrating how H-MDP structures can bridge single-phase RL research and mission-ready autonomous G&C.
