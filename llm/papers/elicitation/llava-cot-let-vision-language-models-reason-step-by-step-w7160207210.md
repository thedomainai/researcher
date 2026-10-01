---
title: "LlaVA-CoT: Let Vision Language Models Reason Step-By-Step"
authors: ["Guowei Xu", "Peng Jin", "Ziang Wu", "Hao Li", "Yibing Song", "Lichao Sun", "Li Yuan"]
year: 2025
cited_by_count: 34
doi: "https://doi.org/10.1109/iccv51701.2025.00202"
openalex_id: W7160207210
paper_type: conference-paper
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "semantic_scholar"
---

# LlaVA-CoT: Let Vision Language Models Reason Step-By-Step

**Authors**: Guowei Xu, Peng Jin, Ziang Wu, Hao Li, Yibing Song, Lichao Sun, Li Yuan | **Year**: 2025 | **Cited by**: 34 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Large language models have demonstrated substantial advancements in reasoning capabilities. However, current Vision-Language Models (VLMs) often struggle to perform systematic and structured reasoning, especially when handling complex visual question-answering tasks. In this work, we introduce LLaVA-COT11Our LLaVA-CoT is built upon Llama-3.2-Vision model [43]., a large VLM designed to conduct autonomous multistage reasoning. Unlike chain-of-thought prompting, LLaVA-COT independently engages in sequential stages of summarization, visual interpretation, logical reasoning, and conclusion generation. This structured approach enables LLaVA-CoT to achieve marked improvements on reasoning-intensive tasks. To accomplish this, we construct the LLaVA-COT-100k dataset, integrating samples from various visual question answering sources and providing structured reasoning annotations. Besides, we propose a test-time stage-wise retracing search method (SWIRES), which enables effective and efficient testtime scaling. Remarkably, with only 100 k training samples and test-time scaling, LLaVA-COT not only outperforms its base model by $\mathbf{9. 4 \%}$ on a wide range of multimodal reasoning benchmarks, but also surpasses the performance of larger and even closed-source models, such as Gemini-1.5pro, GPT-4o-mini, and Llama-3.2-90B-Vision-Instruct. The code, dataset, and pre-trained weights are publicly available at https://github.com/PKU-YuanGroup/LLaVA-CoT.
