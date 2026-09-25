---
title: "Deceptive bias measurement in deep learning: Assessing shortcut reliance in TCGA cancer models"
authors: "Farnaz Kheiri, Shahryar Rahnamayan, Masoud Makrehchi"
year: 2026
citations: 1
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-05T06:04:14.236115"
doi: "https://doi.org/10.1371/journal.pdig.0001165"
openalex_id: "https://openalex.org/W4417346112"
source_api: "openalex"
---

# Deceptive bias measurement in deep learning: Assessing shortcut reliance in TCGA cancer models

**著者**: Farnaz Kheiri, Shahryar Rahnamayan, Masoud Makrehchi
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Abstract Bias in machine learning is a persistent challenge because it can create unfair outcomes, limit generalization, and reduce trust in real-world applications. A key source of this problem is shortcut learning, where models exploit signals linked to sensitive attributes, such as data source or collection site, instead of relying on task, relevant features. To tackle this, we propose the Deceptive Signal metric, a novel quantitative measure designed to assess the extent of a model’s reliance on hidden shortcuts during the learning process. This metric is derived via the Deceptive Bias Detection pipeline, which isolates shortcut dependence by contrasting model behavior under two controlled conditions: (1) Full Exclusion, where a sensitive subgroup is completely removed from training; and (2) Partial Exclusion, where the model has limited access to specific classes within the subgroup. By calculating the behavioral shift between these settings, the Deceptive Signal metric provides a concrete value representing the model’s proneness to learning task-irrelevant patterns. In experiments with the TCGA histopathology dataset, our metric successfully quantified strong dependencies on center-specific artifacts in models trained for cancer classification. Author summary Deep learning models are becoming powerful tools in healthcare, but they often suffer from a critical vulnerability: they can get the right answer for the wrong reason. In medical imaging, an AI might correctly identify a tumor not by analyzing the tissue, but by recognizing irrelevant digital markers unique to the specific hospital or scanner that produced the image. This phenomenon, known as shortcut learning, makes AI systems appear accurate at first glance while remaining unreliable for real-world patient care. To solve this, our research moves beyond simple accuracy checks and introduces a specific quantitative metric for shortcut learning. We developed a testing framework that forces the model into controlled training scenarios, deliberately withholding specific “shortcut” information to see how the model reacts. By mathematically comparing the model’s behavior across these scenarios, we calculate a precise score that indicates the magnitude of the model’s dependence on irrelevant patterns. This metric allows to put a concrete number on a model’s trustworthiness and ensuring that medical decisions are driven by biology, not background noise.
