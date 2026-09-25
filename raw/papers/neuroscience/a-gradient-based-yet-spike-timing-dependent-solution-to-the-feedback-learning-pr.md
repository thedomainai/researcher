---
title: "A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits"
authors: "Xiangnan Zhang, Jingxin Liu, Ranqi Lu, Jingyu Liu, Qunxi Dong"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-10T06:00:26.717082"
arxiv_id: "http://arxiv.org/abs/2609.08070v1"
source_api: "arxiv"
categories: "cs.NE, cs.LG, q-bio.NC"
---

# A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits

**著者**: Xiangnan Zhang, Jingxin Liu, Ranqi Lu, Jingyu Liu, Qunxi Dong
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

The brain uses discrete spikes for dynamic computation, yet, how neural microcircuits (NMCs) solve temporal credit assignment using local spike timing remains a fundamental open question. Dominant spiking neural network (SNN) approaches circumvent this by approximating backpropagation through surrogate gradients, decoupling learning from biological spike timing. Here, we reformulate temporal credit assignment as a state separation problem: extracting task-required components induced by historical perturbations directly from the current neural state. This enables an online feedback learning framework for NMCs through a gradient tunneling (GT) algorithm and the lead-lag expansion technique that derives credit assignment from local synaptic spike timing, while remaining compatible with ANN-SNN hybrid architectures. Experimentally, GT-trained NMCs excel at long-timescale evidence integration and noise-robust memory retention, and perform comparably to leading SNN online learning methods on real-world benchmarks with far fewer parameters. The proposed framework addresses the two-decade-old NMC feedback learning problem and suggests a computationally plausible explanation for the brain's learning mechanisms.
