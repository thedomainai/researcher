---
title: "Hardening LLM Fine-Tuning: From Differentially Private Data Selection to Trustworthy Model Quantization"
authors: ["Zehang Deng", "Ruoxi Sun", "Minhui Xue", "Wanlun Ma", "Sheng Wen", "‪Surya Nepal‬", "Yang Xiang"]
year: 2025
cited_by_count: 31
doi: "https://doi.org/10.1109/tifs.2025.3581103"
openalex_id: W4411408927
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Hardening LLM Fine-Tuning: From Differentially Private Data Selection to Trustworthy Model Quantization

**Authors**: Zehang Deng, Ruoxi Sun, Minhui Xue, Wanlun Ma, Sheng Wen, ‪Surya Nepal‬, Yang Xiang | **Year**: 2025 | **Cited by**: 31 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Critical infrastructures are increasingly integrating artificial intelligence (AI) technologies, including large language models (LLMs), into essential systems and services that are vital to societal functioning. Fine-tuning LLMs for specific domain tasks are crucial for their effective deployment in these contexts, but this process must carefully address both privacy and security concerns. Without proper safeguards, such integration can introduce additional risks, such as data leakage during training and diminished model trustworthiness due to the need for model compression to operate within limited bandwidth and computational capacity constraints. In this paper, we proposeHardening LLM Fine-tuning framework(HARDLLM), which addresses these challenges through two key components: (i) we develop a differentially private data selection method that ensures privacy protection by training the model exclusively on sampled and synthesized public data, thereby preventing any direct use of private data and enhancing leakage resilience throughout the training process, and (ii) we introduce a trustworthiness-aware model quantization approach to improve LLMs performance, such as reducing toxicity, enhancing adversarial robustness, and mitigating stereotypes, while maintaining negligible impact on model utility. Experimental results show that, the proposed algorithm ensures differential privacy when privacy budget is set at ϵ = 0.5, with only a 1% drop in accuracy, while other state-of-the-art methods experience an accuracy drop of at least 20% under the same privacy budget. Additionally, our quantization approach improves the trustworthiness of fine-tuned LLMs by an average of 3-4%, with only a negligible utility loss (approximately 1%) at a 50% compression rate.
