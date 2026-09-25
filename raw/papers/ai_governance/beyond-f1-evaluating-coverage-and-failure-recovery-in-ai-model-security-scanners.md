---
title: "Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners"
authors: "Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-08-29T06:03:48.448996"
arxiv_id: "http://arxiv.org/abs/2608.27424v1"
source_api: "arxiv"
categories: "cs.CR, cs.AI"
---

# Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners

**著者**: Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Static scanners are increasingly used to identify executable or otherwise unsafe content in machine- learning artifacts, yet conventional evaluation metrics characterize only cases where a scanner yields a usable security judgment. We evaluate ModelScan, ModelAudit, and Fickling using a controlled, artifact-backed benchmark on a synthetic corpus of 170 Pickle and PyTorch focused artifacts across 145 specimen families, 135 of which have binary security ground truth and 10 of which are intentionally malformed without labels. We explicitly distinguish non-N/A coverage, analysis completion, definitive security decisions, non-security findings, and unsupported outcomes. On labeled families, ModelAudit produced definitive security decisions for all 135 families (100%), Fickling for 110 (81.5%), and ModelScan for 67 (49.6%). Conditional on making a definitive judgment, ModelScan achieved 100% precision, recall, and F1. Fickling identified no unique true- positive families beyond those found by the combination of ModelAudit and ModelScan. Furthermore, for the 48 malicious families where ModelScan failed to complete its analysis, both ModelAudit and Fickling generated detections consistent with ground truth. These findings underscore the need to separate judgment accuracy from judgment availability, as well as incremental detection coverage from tool-level redundancy.
