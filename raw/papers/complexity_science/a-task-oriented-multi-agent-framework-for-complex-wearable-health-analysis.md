---
title: "A Task-Oriented Multi-Agent Framework for Complex Wearable Health Analysis"
authors: "Kunpeng Yang"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-23T06:01:59.945884"
arxiv_id: "http://arxiv.org/abs/2609.24107v1"
source_api: "arxiv"
categories: "cs.MA"
---

# A Task-Oriented Multi-Agent Framework for Complex Wearable Health Analysis

**著者**: Kunpeng Yang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Wearable health questions often combine data retrieval, longitudinal analysis, and health advice over structured records. Prompting a single large language model with a complete record and a composite query obscures whether every request is executed and which evidence supports the answer. We propose a task-oriented multi-agent framework that represents a composite query as distinct intents and typed tasks with explicit intra-intent dependencies. Specialized agents execute retrieval, analysis, and advice tasks; isolated intent states preserve request boundaries and evidence relationships before aggregation. We evaluate the framework on a synthetic dataset of $10{,}000$ virtual users with one month of longitudinal wearable records, covering structured data retrieval, multi-intent recognition, and overall response quality. Across $1{,}500$ retrieval questions, the Query Agent achieves $98.3\%$ accuracy, compared with $97.9\%$ for the Direct LLM baseline, while reducing average query-stage token consumption from $6{,}869$ to $3{,}136$. On $180$ multi-intent questions, the Manager Agent achieves $100.0\%$ Multi-Intent Coverage and $94.4\%$ Multiset Jaccard Similarity. Under the current synthetic evaluation setting, our method receives higher mean Trustworthiness and Transparency scores on both question categories, whereas Actionability does not improve consistently. These results provide preliminary evidence that explicit task organization can support task-relevant data access and data-grounded longitudinal analysis, while leaving health advice generation and validation on real wearable data as open challenges.
