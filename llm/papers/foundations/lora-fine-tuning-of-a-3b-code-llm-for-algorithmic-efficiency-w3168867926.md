---
title: "LoRA Fine-Tuning of a 3B Code LLM for Algorithmic Efficiency"
authors: ["J. Edward Hu", "Yelong Shen", "Phillip Wallis", "Zeyuan Allen-Zhu", "Yuanzhi Li", "Shean Wang", "Wang, Lu", "Chen, Weizhu"]
year: 2021
cited_by_count: 2522
doi: "https://doi.org/10.48550/arxiv.2106.09685"
openalex_id: W3168867926
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# LoRA Fine-Tuning of a 3B Code LLM for Algorithmic Efficiency

**Authors**: J. Edward Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Wang, Lu, Chen, Weizhu | **Year**: 2021 | **Cited by**: 2522 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times. LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency. We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA. We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints for RoBERTa, DeBERTa, and GPT-2 at https://github.com/microsoft/LoRA.
