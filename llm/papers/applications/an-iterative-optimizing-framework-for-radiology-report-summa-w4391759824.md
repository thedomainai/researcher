---
title: "An Iterative Optimizing Framework for Radiology Report Summarization With ChatGPT"
authors: ["Chong Ma", "Zihao Wu", "Jiaqi Wang", "Shaochen Xu", "Yaonai Wei", "Zhengliang Liu", "Fang Zeng", "Xi Jiang", "et al."]
year: 2024
cited_by_count: 106
doi: "https://doi.org/10.1109/tai.2024.3364586"
openalex_id: W4391759824
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# An Iterative Optimizing Framework for Radiology Report Summarization With ChatGPT

**Authors**: Chong Ma, Zihao Wu, Jiaqi Wang, Shaochen Xu, Yaonai Wei, Zhengliang Liu, Fang Zeng, Xi Jiang, et al. | **Year**: 2024 | **Cited by**: 106 | **Kind**: article | **Relevance**: applications: supporting

## Abstract

The “Impression” section of a radiology report is a critical basis for communication between radiologists and other physicians. Typically written by radiologists, this part is derived from the “Findings” section, which can be laborious and error-prone. Although deep-learning based models, such as BERT, have achieved promising results in Automatic Impression Generation (AIG), such models often require substantial amounts of medical data and have poor generalization performance. Recently, Large Language Models (LLMs) like ChatGPT have shown strong generalization capabilities and performance, but their performance in specific domains, such as radiology, remains under-investigated and potentially limited. To address this limitation, we propose ImpressionGPT, leveraging the contextual learning capabilities of LLMs through our dynamic prompt and iterative optimization algorithm to accomplish the AIG task. ImpressionGPT initially employs a small amount of domain-specific data to create a dynamic prompt, extracting contextual semantic information closely related to the test data. Subsequently, the iterative optimization algorithm automatically evaluates the output of LLMs and provides optimization suggestions, continuously refining the output results. The proposed ImpressionGPT model achieves superior performance of AIG task on both MIMIC-CXR and OpenI datasets without requiring additional training data or fine-tuning the LLMs. This work presents a paradigm for localizing LLMs that can be applied in a wide range of similar application scenarios, bridging the gap between general-purpose LLMs and the specific language processing needs of various domains.
