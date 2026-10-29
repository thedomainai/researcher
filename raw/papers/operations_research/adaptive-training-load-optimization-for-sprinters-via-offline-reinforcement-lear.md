---
title: "Adaptive training load optimization for sprinters via offline reinforcement learning and multi-modal physiological feedback"
authors: "Xinhe Hu, Linjun Liu, Yuting Pei"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-10-29T20:40:28.422359"
doi: "https://doi.org/10.3389/fpsyg.2026.1902098"
openalex_id: "https://openalex.org/W7224103005"
source_api: "openalex"
---

# Adaptive training load optimization for sprinters via offline reinforcement learning and multi-modal physiological feedback

**著者**: Xinhe Hu, Linjun Liu, Yuting Pei
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Elite sprint training requires daily adjustment of training load to balance performance adaptation and fatigue, yet physiological monitoring does not necessarily translate into a specific next-session prescription. This study formalizes daily sprint training prescription as a finite-horizon Markov Decision Process and develops an adaptive load-optimization framework that couples multi-modal physiological feedback with offline reinforcement learning (RL). A 19-dimensional state fusing autonomic, neuromuscular, endocrine, subjective, and load-aggregate signals is encoded by a dual-tower network [a one-dimensional convolutional neural network–Transformer temporal branch and a multi-layer perceptron (MLP) static branch] over an action space of 62 admissible training-type/intensity/volume combinations. A composite reward penalizes overreaching while rewarding short-term gain, longitudinal adaptation, and acute-to-chronic workload ratio conformity. The policy is learned by conservative off-policy training on retrospective data, evaluated through the Fitted Q-Evaluation (FQE) and Doubly Robust (DR) estimators, and presented to coaches as the three leading candidate actions, with SHapley Additive exPlanations (SHAP) values used to explain the model's preferences among the candidate actions. In a 12-week single-center retrospective comparison of 70 national-level sprinters (35 men and 35 women; 100 m personal best (PB) ≤ 11.20 s for men or ≤ 12.50 s for women), grouped by whether their squad had adopted the tool ( n = 35 RL-guided) or continued classical block periodisation ( n = 35 control), the RL-guided cohort demonstrated between-cohort differences of +0.240 s in 100 m [95% confidence interval (CI) +0.128 to +0.352; p < 0.001, d = 1.00], +0.104 s in 30 m ( p < 0.001, d = 1.00) and +2.17 cm in countermovement jump ( p < 0.001, d = 1.01). Zero algorithmically defined sustained multi-indicator fatigue/load events were observed in the RL-guided cohort vs. seven in the control cohort (1.43 per 1,000 athlete-days); these events should not be interpreted as clinically diagnosed overtraining syndrome. Off-policy evaluation yielded exploratory point estimates whose precision remains unknown because uncertainty intervals were not calculated. These observational findings describe associations with an RL-guided, coach-in-the-loop workflow and do not establish a causal effect of the RL policy.
