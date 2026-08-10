---
title: "Open-Set Fake News Detection Framework: Addressing Algorithm Aversion through AI Geometric Bounding"
authors: "Ali Safari, Dan J Kim"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-06-13T06:18:32.945219"
doi: ""
openalex_id: "https://openalex.org/W7164468246"
source_api: "openalex"
---

# Open-Set Fake News Detection Framework: Addressing Algorithm Aversion through AI Geometric Bounding

**著者**: Ali Safari, Dan J Kim
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Most fake news detection models assume a "closed-set" environment where test data resembles training data. In reality, misinformation evolves rapidly, and models inevitably encounter novel content unseen during training. When standard classifiers (e.g., Softmax) face this novel data, they force high-confidence but wrong predictions. These "False Alarms" constitute a technical precondition that prior research has shown to induce Algorithm Aversion, where users lose trust and stop delegating to the AI. We reframe fake news detection as an Open-Set Recognition problem using the ISOT Fake News Dataset (33,320 political articles) with a strict chronological split. We apply an Extreme Value Machine (EVM) over RoBERTa embeddings, enabling the system to output "Unknown" when encountering unfamiliar content. Our results show that compared to a closed-set baseline, the EVM significantly reduced False Alarms on novel data while simultaneously improving overall classification accuracy. Rigorous statistical validation, including bootstrap confidence intervals and McNemar tests, confirms these performance differences are highly significant. An ablation study confirms both deep embeddings and geometric bounding are strictly necessary for mitigating these trust-breaking technical failures under temporal shift.
