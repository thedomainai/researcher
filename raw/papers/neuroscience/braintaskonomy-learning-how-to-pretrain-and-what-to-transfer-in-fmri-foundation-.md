---
title: "BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models"
authors: "Junfeng Xia, Wenhao Ye, Junxiang Zhang, Jiayu Zuo, Mo Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-11T06:00:26.869994"
arxiv_id: "http://arxiv.org/abs/2609.10518v1"
source_api: "arxiv"
categories: "cs.CV, q-bio.NC"
---

# BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models

**著者**: Junfeng Xia, Wenhao Ye, Junxiang Zhang, Jiayu Zuo, Mo Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain curriculum combined with high-to-low-noise timestep scheduling and joint consolidation. During adaptation, controlled first- and higher-order transfer across fifteen tasks constructs a directed taskonomy, from which budgeted integer programming (BIP) selects directly supervised source tasks and target-specific routes. The joint priority-domain and high-to-low-timestep curriculum reduces v-NMSE, PSD-NMSE, and FC-MSE by 6.5%, 16.3%, and 10.5%, respectively, relative to uniform sampling over both dimensions, and shows strong downstream performance across six in- and out-of-domain tasks. The taskonomy reveals asymmetric, target-dependent transfer, while exploratory sealed-test evaluation shows larger descriptive gains for BIP policies when higher-order route spaces are available than for matched random controls. Together, these findings support organizing fMRI pretraining and adaptation by measured learning relations rather than treating domains and tasks as independent flat sets.
