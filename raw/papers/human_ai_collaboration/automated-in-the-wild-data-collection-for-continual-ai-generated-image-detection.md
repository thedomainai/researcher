---
title: "Automated In-the-Wild Data Collection for Continual AI Generated Image Detection"
authors: "Thanasis Pantsios, Dimitrios Karageorgiou, Christos Koutlis, George Karantaidis, Olga Papadopoulou"
year: 2026
citations: 1
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-06-26T06:02:21.275227"
doi: "https://doi.org/10.1145/3810988.3812662"
openalex_id: "https://openalex.org/W7160429386"
source_api: "openalex"
---

# Automated In-the-Wild Data Collection for Continual AI Generated Image Detection

**著者**: Thanasis Pantsios, Dimitrios Karageorgiou, Christos Koutlis, George Karantaidis, Olga Papadopoulou
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

The rapid advancement of generative Artificial Intelligence (AI) has introduced significant challenges for reliable AI-generated image detection. Existing detectors often suffer from performance degradation under distribution shifts and when encountering newly emerging generative models. In this work, we propose a data-centric continual adaptation framework for updating detectors in evolving environments. We show that both in-the-wild data and generator-driven data are essential for adapting detectors. We introduce an automated, weakly supervised pipeline for constructing in-the-wild datasets through fact-check article retrieval. Additionally, we demonstrate that incorporating even a small amount of generator-driven data during training enables effective adaptation to newly emerging models, while combining it with in-the-wild data within a continual learning framework enables robust adaptation and mitigates catastrophic forgetting. Extensive experiments on two state-of-the-art detectors show significant improvements of +9.14% and +8% in average accuracy, respectively. The proposed dataset and model checkpoints are publicly available at https://mever-team.github.io/WildFC/.
