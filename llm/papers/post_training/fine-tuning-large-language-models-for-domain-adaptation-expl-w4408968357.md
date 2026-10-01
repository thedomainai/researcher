---
title: "Fine-tuning large language models for domain adaptation: exploration of training strategies, scaling, model merging and synergistic capabilities"
authors: ["Wei Lu", "Rachel K. Luu", "Markus J. Buehler"]
year: 2025
cited_by_count: 102
doi: "https://doi.org/10.1038/s41524-025-01564-y"
openalex_id: W4408968357
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Fine-tuning large language models for domain adaptation: exploration of training strategies, scaling, model merging and synergistic capabilities

**Authors**: Wei Lu, Rachel K. Luu, Markus J. Buehler | **Year**: 2025 | **Cited by**: 102 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

The advancement of Large Language Models (LLMs) for domain applications in fields such as materials science and engineering depends on the development of fine-tuning strategies that adapt models for specialized, technical capabilities. In this work, we explore the effects of Continued Pretraining (CPT), Supervised Fine-Tuning (SFT), and various preference-based optimization approaches, including Direct Preference Optimization (DPO) and Odds Ratio Preference Optimization (ORPO), on fine-tuned LLM performance. Our analysis shows how these strategies influence model outcomes and reveals that the merging of multiple fine-tuned models can lead to the emergence of capabilities that surpass the individual contributions of the parent models. We find that model merging is not merely a process of aggregation, but a transformative method that can drive substantial advancements in model capabilities characterized by highly nonlinear interactions between model parameters, resulting in new functionalities that neither parent model could achieve alone, leading to improved performance in domain-specific assessments. We study critical factors that influence the success of model merging, such as the diversity between parent models and the fine-tuning techniques employed. The insights underscore the potential of strategic model merging to unlock novel capabilities in LLMs, offering an effective tool for advancing AI systems to meet complex challenges. Experiments with different model architectures are presented, including the Llama 3.1 8B and Mistral 7B family of models, where similar behaviors are observed. Exploring whether the results hold also for much smaller models, we use a tiny LLM with 1.7 billion parameters and show that very small LLMs do not necessarily feature emergent capabilities under model merging, suggesting that model scaling may be a key component. In open-ended yet consistent chat conversations between a human and AI models, our assessment reveals detailed insights into how different model variants perform, and shows that the smallest model achieves a high intelligence score across key criteria including reasoning depth, creativity, clarity, and quantitative precision. Other experiments include the development of image generation prompts that seek to reason over disparate biological material design concepts, to create new microstructures, architectural concepts, and urban design based on biological materials-inspired construction principles. We conclude with a series of questions about scaling and emergence that could be addressed in future research.
