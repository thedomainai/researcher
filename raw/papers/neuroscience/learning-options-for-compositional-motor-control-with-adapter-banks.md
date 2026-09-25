---
title: "Learning Options for Compositional Motor Control with Adapter Banks"
authors: "Sreejan Kumar, Marcelo Mattar, Lea Duncker"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-17T06:00:27.354641"
arxiv_id: "http://arxiv.org/abs/2609.17042v1"
source_api: "arxiv"
categories: "cs.LG, cs.RO, q-bio.NC"
---

# Learning Options for Compositional Motor Control with Adapter Banks

**著者**: Sreejan Kumar, Marcelo Mattar, Lea Duncker
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Learning flexible motor primitives is a hallmark of skilled motor control. Recent neuroscience theory proposes that motor primitives may be implemented as low-rank perturbations of a shared recurrent network, but leaves open how such a system is learned. We translate this principle into a novel architecture for learning motor skills end-to-end: a shared recurrent core modulated by a bank of residual adapters, each selected by a discrete latent code. Trained on closed-loop biomechanical control, the adapters develop emergent low-rank perturbations of the recurrent dynamics despite no architectural rank constraint, placing task representations in disparate subspaces of the shared core network. A simple high-level policy over the learned options, optimized while the whole network is frozen, sequences the low-rank adapters to produce novel out-of-distribution movements. We demonstrate the ability to generalize to novel motor sequences within the closed-loop control setting, improving on the generalization error of a task-input-conditioned multitask baseline by upto order of magnitude.
