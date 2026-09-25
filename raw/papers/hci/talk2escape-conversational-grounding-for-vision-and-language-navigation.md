---
title: "Talk2Escape: Conversational Grounding for Vision-and-Language Navigation"
authors: "Zerui Li, Sihao Lin, Yanyan Shao, Jiwen Zhang, Xiangyu Shi"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-25T06:03:06.347367"
arxiv_id: "http://arxiv.org/abs/2609.28296v1"
source_api: "arxiv"
categories: "cs.RO, cs.HC"
---

# Talk2Escape: Conversational Grounding for Vision-and-Language Navigation

**著者**: Zerui Li, Sihao Lin, Yanyan Shao, Jiwen Zhang, Xiangyu Shi
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

While Vision-and-Language Navigation (VLN) has demonstrated remarkable success, the prevailing single-turn paradigm exposes a fundamental vulnerability: agents operate in a strictly open-loop manner. In practice, factors such as perceptual aliasing, sensor noise, and odometry drift can cause minor deviations to accumulate over time, often leading to catastrophic mission failures with no built-in mechanism for error recovery. To address this, we introduce \textit{Talk2Escape}, a proactive and model-agnostic dialogue intervention framework that reframes navigation as a closed-loop interactive process. At its core, a lightweight vision-language module continuously monitors agent kinematics. Upon detecting localized looping or severe trajectory divergence, it translates raw egocentric observations into concise, grounded queries to solicit targeted corrective feedback from either an algorithmic oracle or a human-in-the-loop. Extensive evaluations in high-fidelity simulators, including R2R-CE, RxR-CE, and VLNVerse,
  demonstrate that \textit{Talk2Escape} exhibits consistent improvements across diverse base agents. Empirically, \textit{Talk2Escape} achieves a 66.0\% Success Rate on R2R-CE, outperforming the current supervised and zero-shot state-of-the-art methods. We further validate its sim-to-real transfer on a Unitree Go2 quadruped, proving that proactive dialogue drastically improves navigation robustness in physical environments.
