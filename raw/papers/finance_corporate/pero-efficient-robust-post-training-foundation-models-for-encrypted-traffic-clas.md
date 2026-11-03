---
title: "PERO: Efficient Robust Post-Training Foundation Models for Encrypted Traffic Classification"
authors: "Wumei Du, Jiarong Wen, Kaiyu Zhang, Zi Yang, Yiqin Lv"
year: 2026
citations: 0
paper_type: "primary"
domain: "finance_corporate"
fetched: "2026-11-04T06:53:57.011884"
doi: "https://doi.org/10.1145/3799682.3840944"
openalex_id: "https://openalex.org/W7203695447"
source_api: "openalex"
---

# PERO: Efficient Robust Post-Training Foundation Models for Encrypted Traffic Classification

**著者**: Wumei Du, Jiarong Wen, Kaiyu Zhang, Zi Yang, Yiqin Lv
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートファイナンス

## Abstract

Encrypted traffic classification is vital for network security, yet real-world deployments are inherently sensitive to rare but high-loss errors such as misclassification of malicious traffic. The encrypted traffic foundation model, as a promising general-purpose technique, can achieve impressive overall performance. However, employing standard objectives such as empirical risk minimization often overlooks high-risk tail events, and commonly used performance metrics hardly reflect robustness limitations in risk-sensitive scenarios. Directly applying robust optimization objectives, such as conditional value-at-risk, to post-training is computationally prohibitive for large models, as identifying high-loss samples exhausts substantial computation. To this end, we propose Pre-Evaluation Robust Optimization (PERO), an efficient robust post-training framework for encrypted traffic foundation models. PERO employs a lightweight proxy to estimate sample-wise risk and selects a subset of high-risk samples to update the foundation model, decoupling risk estimation from expensive large-model optimization. Extensive experiments on typical encrypted traffic datasets show that PERO achieves competitive or superior robustness and average performance compared to outstanding robust post-training methods, while significantly reducing computational and memory costs.
