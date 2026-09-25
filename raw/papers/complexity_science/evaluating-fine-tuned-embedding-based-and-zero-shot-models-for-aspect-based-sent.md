---
title: "Evaluating fine-tuned, embedding-based, and zero-shot models for aspect-based sentiment analysis in South Slavic news"
authors: "Nishan Chatterjee, Boshko Koloski, Antoine Doucet, Senja Pollak, Matthew Purver"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-19T10:29:41.157640"
doi: "https://doi.org/10.3389/frai.2026.1844418"
openalex_id: "https://openalex.org/W7153693637"
source_api: "openalex"
---

# Evaluating fine-tuned, embedding-based, and zero-shot models for aspect-based sentiment analysis in South Slavic news

**著者**: Nishan Chatterjee, Boshko Koloski, Antoine Doucet, Senja Pollak, Matthew Purver
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

In the contemporary digital media landscape, the ability to automatically distill public opinion from a vast and continuous stream of information is highly important. Aspect-Based Sentiment Analysis (ABSA) offers this granular capability. In this work, we address a specific, industrially relevant formulation of this task, more formally known as document-level entity-targeted sentiment analysis (TSA) or entity-level sentiment analysis (ELSA), where the “aspects” are named entities such as companies and brands. However, its application to morphologically complex, less-resourced languages like those in the South Slavic family, particularly within the long-form news domain, remains a significant challenge. In this work, we introduce AspectBench, a new benchmark dataset for document-level ABSA, comprising real-world online news articles in Slovenian and Serbo-Croatian, designed to test generalization to unseen aspects, with the Serbo-Croatian portion being made publicly available. Using this benchmark, we conduct a comprehensive empirical study evaluating five distinct modeling paradigms, including lightweight document-embedding-based classifiers, fine-tuned multilingual and language-specific pretrained language models (PLMs), hierarchical attention networks (HANs), local large language models (LLMs) in zero and few-shot settings, and learning-to-defer (L2D) policies with multi-expert PLMs, complete LLM deferral, and confidence-gated selective LLM deferral using DSPy-calibrated prompts. Our experiments show that supervised expert models remain the most reliable foundation for this task, with Longformer, mDeBERTa-v3, mT5, language-specific encoders, and hierarchical models providing strong performance depending on language and class balance. Aspect masking is generally useful for supervised expert models, especially the PLM and HAN variants, but is not uniformly beneficial across all model families and evaluation views. Standalone local LLMs are not competitive, and complete LLM deferral is unstable when applied to every instance. However, selective LLM deferral is more promising because routing low-confidence expert predictions to the LLM can improve or stabilize performance while limiting unnecessary LLM calls. We additionally use minimum viable set analysis to show how performance, calibration, and uncertainty scale with annotation volume, providing practical guidance for future media-monitoring annotation campaigns on real-world datasets. Our work therefore fills a crucial gap for less-resourced ABSA and offers practical insights into the trade-offs between model complexity, data characteristics, and the development of robust, learning-to-defer systems for real-world media monitoring.
