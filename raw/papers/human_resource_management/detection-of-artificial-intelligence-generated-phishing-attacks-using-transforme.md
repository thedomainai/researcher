---
title: "Detection of Artificial Intelligence-Generated Phishing Attacks Using Transformer Models"
authors: "Samuel Okechukwu Nnaji, Anyalebechi Felicia Nneamaka, Christabel Linda Uchenwa, Abigail Eberechi Nwoka"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_resource_management"
fetched: "2026-09-21T09:15:27.297425"
doi: "https://doi.org/10.5120/ijca209cd5833714"
openalex_id: "https://openalex.org/W7213657584"
source_api: "openalex"
---

# Detection of Artificial Intelligence-Generated Phishing Attacks Using Transformer Models

**著者**: Samuel Okechukwu Nnaji, Anyalebechi Felicia Nneamaka, Christabel Linda Uchenwa, Abigail Eberechi Nwoka
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人的資源管理

## Abstract

The proliferation of large language models (LLMs) such as GPT-4, Claude, and Llama has fundamentally altered the phishing threat landscape by enabling attackers to generate grammatically fluent, contextually convincing, and highly personalized phishing content at scale.Unlike traditional phishing emails, which often exhibit tell-tale linguistic errors and generic phrasing, artificial intelligence (AI)-generated phishing messages closely mimic legitimate human correspondence, substantially reducing the effectiveness of conventional rule-based and keyword-driven detection systems.This study proposes and evaluates a transformerbased framework for detecting AI-generated phishing attacks in enterprise email environments.A composite corpus of 15,000 labelled messages comprising legitimate correspondence, human-crafted phishing emails, and LLMgenerated phishing emails synthesized from multiple generator models was constructed and used to fine-tune four transformer variants (BERT-base, DistilBERT, RoBERTa, and a proposed attention-fusion hybrid) alongside classical machine learning and recurrent baselines.The proposed hybrid model, which combines domain-adaptively pre-trained RoBERTa and DistilBERT encoders through an attention-weighted fusion layer, achieved the strongest performance, recording 97.8% accuracy, an F1-score of 97.5%, and an area under the receiver operating characteristic curve (AUC) of 0.991, outperforming all baseline models and the best-performing single transformer (RoBERTa, 96.1% accuracy) by a statistically meaningful margin.Explainability analysis using attention visualization further showed that the model consistently attended to psychological-pressure cues, spoofed-domain indicators, and stylistic hallmarks characteristic of machine-generated text.These findings demonstrate that transformer architectures, when combined with a purpose-built AI-generated phishing corpus, can meaningfully close the detection gap created by generative AI misuse and offer a viable foundation for nextgeneration, explainable email security systems.
