---
title: "Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing"
authors: ["裕二 池谷", "Robert Tinn", "Hao Cheng", "MICHAEL A. LUCAS", "Naoto Usuyama", "Xiaodong Liu", "Tristan Naumann", "Jianfeng Gao", "et al."]
year: 2021
cited_by_count: 2196
doi: "https://doi.org/10.1145/3458754"
openalex_id: W3046375318
paper_type: article
evidence_kind: article
topics: ["foundations", "applications"]
landmark: false
abstract_source: "openalex"
---

# Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing

**Authors**: 裕二 池谷, Robert Tinn, Hao Cheng, MICHAEL A. LUCAS, Naoto Usuyama, Xiaodong Liu, Tristan Naumann, Jianfeng Gao, et al. | **Year**: 2021 | **Cited by**: 2196 | **Kind**: article | **Relevance**: foundations: supporting; applications: supporting

## Abstract

Pretraining large neural language models, such as BERT, has led to impressive gains on many natural language processing (NLP) tasks. However, most pretraining efforts focus on general domain corpora, such as newswire and Web. A prevailing assumption is that even domain-specific pretraining can benefit by starting from general-domain language models. In this article, we challenge this assumption by showing that for domains with abundant unlabeled text, such as biomedicine, pretraining language models from scratch results in substantial gains over continual pretraining of general-domain language models. To facilitate this investigation, we compile a comprehensive biomedical NLP benchmark from publicly available datasets. Our experiments show that domain-specific pretraining serves as a solid foundation for a wide range of biomedical NLP tasks, leading to new state-of-the-art results across the board. Further, in conducting a thorough evaluation of modeling choices, both for pretraining and task-specific fine-tuning, we discover that some common practices are unnecessary with BERT models, such as using complex tagging schemes in named entity recognition. To help accelerate research in biomedical NLP, we have released our state-of-the-art pretrained and task-specific models for the community, and created a leaderboard featuring our BLURB benchmark (short for Biomedical Language Understanding & Reasoning Benchmark) at https://aka.ms/BLURB .
