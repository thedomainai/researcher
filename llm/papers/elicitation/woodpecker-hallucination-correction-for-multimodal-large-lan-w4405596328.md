---
title: "Woodpecker: hallucination correction for multimodal large language models"
authors: ["Shukang Yin", "Chaoyou Fu", "Sirui Zhao", "Tong Bill Xu", "Hao Wang", "Dianbo Sui", "Yunhang Shen", "Ke Li", "et al."]
year: 2024
cited_by_count: 118
doi: "https://doi.org/10.1007/s11432-024-4251-x"
openalex_id: W4405596328
paper_type: article
evidence_kind: article
topics: ["elicitation", "safety_interp"]
landmark: false
abstract_source: "semantic_scholar"
---

# Woodpecker: hallucination correction for multimodal large language models

**Authors**: Shukang Yin, Chaoyou Fu, Sirui Zhao, Tong Bill Xu, Hao Wang, Dianbo Sui, Yunhang Shen, Ke Li, et al. | **Year**: 2024 | **Cited by**: 118 | **Kind**: article | **Relevance**: elicitation: supporting; safety_interp: supporting

## Abstract

Hallucinations is a big shadow hanging over the rapidly evolving multimodal large language models (MLLMs), referring to that the generated text is inconsistent with the image content. To mitigate hallucinations, existing studies mainly resort to an instruction-tuning manner that requires retraining the models with specific data. In this paper, we pave a different way, introducing a training-free method named Woodpecker. Like woodpeckers heal trees, it picks out and corrects hallucinations from the generated text. Concretely, Woodpecker consists of five stages: key concept extraction, question formulation, visual knowledge validation, visual claim generation, and hallucination correction. Implemented in a post-remedy manner, Woodpecker can easily serve different MLLMs, while being interpretable by accessing intermediate outputs of the five stages. We evaluate Woodpecker both quantitatively and qualitatively and show the huge potential of this new paradigm. On the POPE benchmark, our method obtains a 30.66%/24.33% improvement in accuracy over the baseline MiniGPT-4/mPLUG-Owl. The source code is released at https://github.com/BradyFU/Woodpecker.
