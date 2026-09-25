---
title: "Why shared attention vectors fail: a case for outcome-indexed tuning"
authors: "Lenard Dome"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-10T06:00:26.716440"
arxiv_id: "http://arxiv.org/abs/2609.08615v1"
source_api: "arxiv"
categories: "cs.LG, cs.NE, q-bio.NC"
---

# Why shared attention vectors fail: a case for outcome-indexed tuning

**著者**: Lenard Dome
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for learning and generalization. We address this by introducing an outcome-indexed attentional matrix that converts globally shared attentional tuning into an outcome-indexed representation. We present an analysis of the unstable shared vectors and derive the conditions under which it holds. Empirically, three synthetic experiments benchmark the proposed attention matrices and show that they converge to meaningful representations, something shared attention vectors fail to do. These results suggest that outcome-indexed attentional matrices are a general fix for gradient-based attentional processes, which improves models of learning under multi-outcome conditions.
