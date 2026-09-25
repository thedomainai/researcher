---
title: "ViMoWear: Visual Motion-Guided sEMG-IMU Representation Learning for Subject-Independent Thumb Gesture Recognition"
authors: "Wenjuan Zhong, Chenfei Ma, Kianoush Nazarpour"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-25T06:03:50.948309"
arxiv_id: "http://arxiv.org/abs/2609.27595v1"
source_api: "arxiv"
categories: "cs.HC"
---

# ViMoWear: Visual Motion-Guided sEMG-IMU Representation Learning for Subject-Independent Thumb Gesture Recognition

**著者**: Wenjuan Zhong, Chenfei Ma, Kianoush Nazarpour
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Wearable sensing enables intuitive hand gesture recognition for human--computer interaction, augmented reality, and prosthetic control, yet subject--independent recognition remains challenging because wearable signals provide only indirect and highly subject-specific observations of hand motion. Although visual information can improve wearable gesture recognition, requiring it during inference increases sensing complexity and limits practical deployment. We propose ViMoWear, a visual-motion-guided framework that leverages synchronized 3D hand motion as training-only supervision while requiring only wearable sensing for gesture classification at inference. Specifically, Motion-Guided Cross-Subject Contrastive Learning (MGCL) promotes subject-robust representations, and Thumb-Aware Masked Motion Reconstruction (TMMR) preserves fine-grained motion information. The leave-one-subject-out experiments on a synchronized sEMG--IMU--pose dataset demonstrate consistent improvements over supervised baselines across multiple sensing configurations, while the learned representations also support classifier-free retrieval. The proposed training-only visual motion supervision improves the generalization of wearable representations to unseen subjects.
