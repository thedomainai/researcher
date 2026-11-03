---
title: "Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence"
authors: "Ante Lojić Kapetanović, Kemal Altwlkany, Andro Merćep, Tomislav Đuričić, Emanuel Lacić"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-11-04T06:27:27.372751"
doi: "https://doi.org/10.1145/3799682.3840879"
openalex_id: "https://openalex.org/W7204606853"
source_api: "openalex"
---

# Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence

**著者**: Ante Lojić Kapetanović, Kemal Altwlkany, Andro Merćep, Tomislav Đuričić, Emanuel Lacić
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Large language models (LLMs) increasingly assess generated content, giving rise to the LLM-as-a-Judge paradigm. These systems now score outputs, filter content, and gate iterative refinement in production pipelines, where each judgment is often assumed to be independent of earlier evaluations. We test this assumption using three prompt conditions: no metadata, revision framing, and anchored metadata containing revision, attempt, and prior-score fields. We show that prior scores, even when included only as context metadata, anchor judgments and systematically shift ratings toward their values. Across 192,000 attempted evaluations (185,271 successful), seven out of the eight evaluated models have 95% task-stratified bootstrap intervals below zero for the total anchored-metadata effect on 20 fixed texts. Cohen's $d$, a standardized measure of the difference between score distributions, reaches an absolute value of 0.71. Token-level analysis of selected model-task probes suggests a threshold-like response pattern: introducing anchored metadata produces a marked redistribution of output-score probabilities, while changing the anchor value within the tested below-threshold range produces comparatively little additional variation. On categorical industry data with human-labeled ground truth, anchored metadata blocks 48% of error corrections and flips 10.18% of correct judgments toward an assigned wrong label, demonstrating the bias extends beyond numerical scoring to categorical decisions. Neither Chain-of-Thought nor a metadata-disregard warning reduces the total effect, although the warning improves the paired accuracy effect relative to baseline in the industry experiment. Reliable LLM evaluation demands careful context engineering rather than an assumption of impartiality. Effective mitigation must be validated for the intended model and task or domain.
