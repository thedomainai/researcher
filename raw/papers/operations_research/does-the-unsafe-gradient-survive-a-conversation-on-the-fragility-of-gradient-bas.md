---
title: "Does the Unsafe Gradient Survive a Conversation? On the Fragility of Gradient-Based Jailbreak Detection in Multi-Turn Dialogue"
authors: "Omar Sheta, Rinku Deuja, Hadi Masoudi, Minghong Fang"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-06T08:14:00.546511"
doi: "https://doi.org/10.1145/3846374.3846392"
openalex_id: "https://openalex.org/W7214944946"
source_api: "openalex"
---

# Does the Unsafe Gradient Survive a Conversation? On the Fragility of Gradient-Based Jailbreak Detection in Multi-Turn Dialogue

**著者**: Omar Sheta, Rinku Deuja, Hadi Masoudi, Minghong Fang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Safety-aligned language models are commonly deployed as multi-turn assistants, which lets adversaries spread unsafe intent across several user turns instead of a single prompt. Gradient-based jailbreak detectors such as GradSafe were developed for single prompts: they score an input by the alignment between its induced gradient and a fixed unsafe reference direction, and their effectiveness in multi-turn dialogue remains unclear. We conduct a controlled evaluation of gradient-based jailbreak detection in multi-turn settings. We extend GradSafe with a Context Window Scanner that applies the detector to fixed-size windows of user turns and uses the maximum window score as the conversation-level score. We evaluate different window sizes, attack families, benign conversation distributions, and target models. The results differ sharply between synthetic and realistic benign settings. Against synthetic benign conversations, the detector achieves an ROC-AUC of 0.98 on human-authored multi-turn jailbreaks. On WildChat benign conversations, ROC-AUC drops to 0.76, and a threshold calibrated on synthetic data flags more than 90% of benign conversations as unsafe. Under realistic benign distributions, single-turn windows give the highest separability, whereas longer windows and accumulated contexts reduce performance. The detector is also sensitive to the attack-generation method and target model: successful Crescendo attacks receive scores comparable to or lower than benign conversations, and Qwen2.5-7B-Instruct yields near-random separability with a different optimal window size. These findings show that gradient-based signals can support multi-turn jailbreak detection, but reliable deployment requires calibration on realistic benign conversations, short-window scoring, length-aware thresholds, and evaluation across attack types and model architectures.
