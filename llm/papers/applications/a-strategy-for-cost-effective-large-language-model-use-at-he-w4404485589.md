---
title: "A strategy for cost-effective large language model use at health system-scale"
authors: ["Eyal Klang", "Donald U. Apakama", "Ethan E. Abbott", "Akhil Vaid", "Joshua Lampert", "Ankit Sakhuja", "Robert Freeman", "Alexander W. Charney", "et al."]
year: 2024
cited_by_count: 43
doi: "https://doi.org/10.1038/s41746-024-01315-1"
openalex_id: W4404485589
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# A strategy for cost-effective large language model use at health system-scale

**Authors**: Eyal Klang, Donald U. Apakama, Ethan E. Abbott, Akhil Vaid, Joshua Lampert, Ankit Sakhuja, Robert Freeman, Alexander W. Charney, et al. | **Year**: 2024 | **Cited by**: 43 | **Kind**: article | **Relevance**: applications: core

## Abstract

Large language models (LLMs) can optimize clinical workflows; however, the economic and computational challenges of their utilization at the health system scale are underexplored. We evaluated how concatenating queries with multiple clinical notes and tasks simultaneously affects model performance under increasing computational loads. We assessed ten LLMs of different capacities and sizes utilizing real-world patient data. We conducted >300,000 experiments of various task sizes and configurations, measuring accuracy in question-answering and the ability to properly format outputs. Performance deteriorated as the number of questions and notes increased. High-capacity models, like Llama-3-70b, had low failure rates and high accuracies. GPT-4-turbo-128k was similarly resilient across task burdens, but performance deteriorated after 50 tasks at large prompt sizes. After addressing mitigable failures, these two models can concatenate up to 50 simultaneous tasks effectively, with validation on a public medical question-answering dataset. An economic analysis demonstrated up to a 17-fold cost reduction at 50 tasks using concatenation. These results identify the limits of LLMs for effective utilization and highlight avenues for cost-efficiency at the enterprise scale.
