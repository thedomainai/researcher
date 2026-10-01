---
title: "Aligning large language models with human preferences using historical text edits"
authors: ["Jan Majkutewicz", "Julian Szymański"]
year: 2025
cited_by_count: 6
doi: "https://doi.org/10.1016/j.knosys.2025.113566"
openalex_id: W4410461195
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Aligning large language models with human preferences using historical text edits

**Authors**: Jan Majkutewicz, Julian Szymański | **Year**: 2025 | **Cited by**: 6 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Aligning large language models with human values (to be helpful, harmless, honest) requires high-quality, comprehensive human preference datasets. However, the substantial cost of creating such datasets often limits their size and scope, hindering preference learning research and limiting open-source model development. In our research, we propose EditPrefs, a cost-effective method that uses historical text edits to create preference datasets without manual data labeling or distilling preferences from strong language models. Our method automatically builds the dataset while capturing genuine human preferences expressed through text revisions. The method constructs the dataset by treating the revised text as a response preferred over the original text and generates matching instructions using a language model. To validate EditPrefs, we applied it to Wikipedia article revisions and extensively evaluated the resulting dataset’s performance. The Zephyr-7b- β -SFT model aligned with our dataset performed on par with models trained on manually curated datasets. Additionally, a reward model trained on our dataset captured more nuanced human preferences and outperformed models trained on widely used datasets built through crowd-sourcing, manual annotation, or distillation from large language models. These findings validate the effectiveness of our approach, highlighting its potential for creating larger, more diverse, and potentially multilingual or domain-specific preference datasets.
