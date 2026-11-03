---
title: "Evidence-Consistent Generative Detection under Scenario-Level Distribution Shift"
authors: "San Kim, JinYeong Bak"
year: 2026
citations: 0
paper_type: "primary"
domain: "finance_corporate"
fetched: "2026-11-04T06:53:53.392191"
doi: "https://doi.org/10.1145/3799682.3840763"
openalex_id: "https://openalex.org/W7204078199"
source_api: "openalex"
---

# Evidence-Consistent Generative Detection under Scenario-Level Distribution Shift

**著者**: San Kim, JinYeong Bak
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートファイナンス

## Abstract

Conventional in-distribution evaluation can overestimate robustness when training and test data share recurring task-specific patterns or surface cues. This risk is especially relevant in social-engineering fraud detection, where attackers can preserve malicious intent while changing the scenario, impersonated entity, or wording. We study this problem as scenario-level out-of-distribution (SL-OOD) detection for SMS and voice phishing, where entire attack scenarios are held out from training while the label space remains fixed. This setting tests whether models can generalize to unseen attack scenarios using decision-relevant evidence rather than familiar scenario-specific cues. Using this SL-OOD evaluation, we find that high in-distribution performance does not reliably predict held-out robustness across feature-, encoder-, and decoder-based baselines. We interpret this gap as scenario memorization: reliance on recurring scenario-specific lexical or entity cues rather than decision-relevant evidence. We propose ECoG, an evidence-consistent generative framework that combines evidence-span supervision with a rationale-label consistency objective during training. On the 0.5B decoder, relative to the same backbone trained without consistency regularization, ECoG raises Macro-F1 on OOD challenging instances by 3.22 points, reduces the share of predictions whose generated rationale supports the opposite label by 4.22 points, and increases token-level overlap with reference evidence spans by 8.38 points; the reduction in prediction-rationale inconsistency is consistent across four decoder backbones. These results suggest that compact generative detectors can benefit from evidence supervision and rationale-label consistency under social-engineering shift.
