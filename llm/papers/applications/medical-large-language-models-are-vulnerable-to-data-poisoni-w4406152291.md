---
title: "Medical large language models are vulnerable to data-poisoning attacks"
authors: ["Daniel Alexander Alber", "Zihao Yang", "Anton Alyakin", "Eunice Yang", "Sumedha Rai", "Aly Al-Amyn Valliani", "Jeff Zhang", "Gabriel R. Rosenbaum", "et al."]
year: 2025
cited_by_count: 192
doi: "https://doi.org/10.1038/s41591-024-03445-1"
openalex_id: W4406152291
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# Medical large language models are vulnerable to data-poisoning attacks

**Authors**: Daniel Alexander Alber, Zihao Yang, Anton Alyakin, Eunice Yang, Sumedha Rai, Aly Al-Amyn Valliani, Jeff Zhang, Gabriel R. Rosenbaum, et al. | **Year**: 2025 | **Cited by**: 192 | **Kind**: article | **Relevance**: applications: supporting

## Abstract

The adoption of large language models (LLMs) in healthcare demands a careful analysis of their potential to spread false medical knowledge. Because LLMs ingest massive volumes of data from the open Internet during training, they are potentially exposed to unverified medical knowledge that may include deliberately planted misinformation. Here, we perform a threat assessment that simulates a data-poisoning attack against The Pile, a popular dataset used for LLM development. We find that replacement of just 0.001% of training tokens with medical misinformation results in harmful models more likely to propagate medical errors. Furthermore, we discover that corrupted models match the performance of their corruption-free counterparts on open-source benchmarks routinely used to evaluate medical LLMs. Using biomedical knowledge graphs to screen medical LLM outputs, we propose a harm mitigation strategy that captures 91.9% of harmful content (F1 = 85.7%). Our algorithm provides a unique method to validate stochastically generated LLM outputs against hard-coded relationships in knowledge graphs. In view of current calls for improved data provenance and transparent LLM development, we hope to raise awareness of emergent risks from LLMs trained indiscriminately on web-scraped data, particularly in healthcare where misinformation can potentially compromise patient safety.
