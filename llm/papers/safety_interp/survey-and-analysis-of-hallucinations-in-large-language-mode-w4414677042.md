---
title: "Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior"
authors: ["Dang Anh-Hoang", "Vu Tran", "Le-Minh Nguyen"]
year: 2025
cited_by_count: 125
doi: "https://doi.org/10.3389/frai.2025.1622292"
openalex_id: W4414677042
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior

**Authors**: Dang Anh-Hoang, Vu Tran, Le-Minh Nguyen | **Year**: 2025 | **Cited by**: 125 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Hallucination in Large Language Models (LLMs) refers to outputs that appear fluent and coherent but are factually incorrect, logically inconsistent, or entirely fabricated. As LLMs are increasingly deployed in education, healthcare, law, and scientific research, understanding and mitigating hallucinations has become critical. In this work, we present a comprehensive survey and empirical analysis of hallucination attribution in LLMs. Introducing a novel framework to determine whether a given hallucination stems from not optimize prompting or the model's intrinsic behavior. We evaluate state-of-the-art LLMs—including GPT-4, LLaMA 2, DeepSeek, and others—under various controlled prompting conditions, using established benchmarks (TruthfulQA, HallucinationEval) to judge factuality. Our attribution framework defines metrics for Prompt Sensitivity (PS) and Model Variability (MV) , which together quantify the contribution of prompts vs. model-internal factors to hallucinations. Through extensive experiments and comparative analyses, we identify distinct patterns in hallucination occurrence, severity, and mitigation across models. Notably, structured prompt strategies such as chain-of-thought (CoT) prompting significantly reduce hallucinations in prompt-sensitive scenarios, though intrinsic model limitations persist in some cases. These findings contribute to a deeper understanding of LLM reliability and provide insights for prompt engineers, model developers, and AI practitioners. We further propose best practices and future directions to reduce hallucinations in both prompt design and model development pipelines.
