---
title: "Learning Adaptive Safety Margins for Visual Navigation"
authors: "Junyi Hu, Shuaihang Yuan, Geeta Chandra Raju Bethala, Anthony Tzes, Yi Fang"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-07-22T06:02:43.416032"
arxiv_id: "http://arxiv.org/abs/2607.18200v1"
source_api: "arxiv"
categories: "cs.RO, cs.AI"
---

# Learning Adaptive Safety Margins for Visual Navigation

**著者**: Junyi Hu, Shuaihang Yuan, Geeta Chandra Raju Bethala, Anthony Tzes, Yi Fang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Robots in cluttered indoor spaces often fail not because they cannot generate collision-free paths, but because a fixed safety margin is mis-calibrated: conservative margins cause detours and timeouts, while permissive margins lead to near-boundary shortcuts under perception bias. Diffusion-based planners propose diverse trajectory candidates from egocentric RGB-D, yet reliable selection remains the bottleneck. We propose a context-conditioned safety critic that learns an adaptive clearance preference for ranking diffusion proposals, decomposed into three complementary terms: (i) a safety term with a clearance-budget penalty and a control-barrier-function residual for waypoint- and transition-wise safety, (ii) an efficiency term combining a smoothness penalty with a safety-gated detour-ratio penalty that avoids detours without incentivizing risky shortcuts, and (iii) a distance-constraint matching term that anchors the learned budget to realized ESDF clearances to prevent margin collapse. We train the critic with privileged ESDF geometry in simulation and distill it into a perception-only selector via a two-stage teacher-student procedure. On PointGoal navigation in HM3D and MP3D, including cross-dataset transfer, our method achieves the highest success rate (SR) and success weighted by path length (SPL) among strong diffusion, optimization, and RL baselines. Trained purely in simulation, it transfers to a Unitree G1 humanoid and navigates cluttered indoor scenes without task-specific tuning.
