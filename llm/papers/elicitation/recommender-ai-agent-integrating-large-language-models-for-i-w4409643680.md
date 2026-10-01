---
title: "Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations"
authors: ["Xu Huang", "Jianxun Lian", "Yuxuan Lei", "Jing Yao", "Defu Lian", "Xing Xie"]
year: 2025
cited_by_count: 71
doi: "https://doi.org/10.1145/3731446"
openalex_id: W4409643680
paper_type: article
evidence_kind: article
topics: ["elicitation", "agents"]
landmark: false
abstract_source: "openalex"
---

# Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations

**Authors**: Xu Huang, Jianxun Lian, Yuxuan Lei, Jing Yao, Defu Lian, Xing Xie | **Year**: 2025 | **Cited by**: 71 | **Kind**: article | **Relevance**: elicitation: supporting; agents: supporting

## Abstract

Recommender models capture ever-changing user preferences by training with in-domain user behavior data. These models are typically lightweight, facilitating real-time and large-scale online services. However, these models often falter when tasked with providing more sophisticated functionalities, such as offering explanations or engaging in conversations. Recently, large language models (LLMs) have emerged as a significant advancement towards artificial general intelligence, demonstrating impressive capabilities in instruction comprehension, reasoning, and human interaction. Unfortunately, LLMs lack the understanding of domain-specific item catalogs and behavioral patterns, especially in areas that deviate from general world knowledge, such as online e-commerce. This limitation makes them unsuitable to function as recommender models directly. In this article, we bridge the gap between recommender models and LLMs, combining their respective strengths to create an interactive recommender system. We present an efficient framework, termed as InteRecAgent , which utilizes LLMs as the brain and recommender models as instrumental tools. We first outline a minimal set of essential tools required to transform LLMs into InteRecAgent. To overcome specific challenges associated with LLM-based agents for recommender systems, we enhance three core components, covering memory mechanism, task planning, and tool learning abilities. The InteRecAgent empowers traditional recommender systems, like ID-based matrix factorization models, to evolve into versatile and interactive systems with a natural language interface through the integration of LLMs. Experimental results derived from three public datasets demonstrate that the InteRecAgent delivers strong performance as a conversational recommender system, surpassing general LLMs such as GPT-4.
