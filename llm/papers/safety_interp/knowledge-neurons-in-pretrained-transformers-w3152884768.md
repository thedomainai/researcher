---
title: "Knowledge Neurons in Pretrained Transformers"
authors: ["Damai Dai", "Li Dong", "Yaru Hao", "Zhifang Sui", "Baobao Chang", "Furu Wei"]
year: 2022
cited_by_count: 164
doi: "https://doi.org/10.18653/v1/2022.acl-long.581"
openalex_id: W3152884768
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Knowledge Neurons in Pretrained Transformers

**Authors**: Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, Furu Wei | **Year**: 2022 | **Cited by**: 164 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Large-scale pretrained language models are surprisingly good at recalling factual knowledge presented in the training corpus (Petroni et al., 2019; Jiang et al., 2020b).In this paper, we present preliminary studies on how factual knowledge is stored in pretrained Transformers by introducing the concept of knowledge neurons.Specifically, we examine the fill-in-the-blank cloze task for BERT.Given a relational fact, we propose a knowledge attribution method to identify the neurons that express the fact.We find that the activation of such knowledge neurons is positively correlated to the expression of their corresponding facts.In our case studies, we attempt to leverage knowledge neurons to edit (such as update, and erase) specific factual knowledge without fine-tuning.Our results shed light on understanding the storage of knowledge within pretrained Transformers.The code is available at https://github.com/ Hunter-DDM/knowledge-neurons.
