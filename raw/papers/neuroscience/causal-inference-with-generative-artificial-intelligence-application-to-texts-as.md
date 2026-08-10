---
title: "Causal Inference with Generative Artificial Intelligence: Application to Texts as Treatments*"
authors: "Kosuke Imai, Kentaro Nakamura"
year: 2026
citations: 1
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-26T06:00:09.797737"
doi: "https://doi.org/10.1080/01621459.2026.2689629"
openalex_id: "https://openalex.org/W4403826407"
source_api: "openalex"
---

# Causal Inference with Generative Artificial Intelligence: Application to Texts as Treatments*

**著者**: Kosuke Imai, Kentaro Nakamura
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: 脳科学

## Abstract

In this paper, we demonstrate how to enhance the validity of causal inference with unstructured high-dimensional treatments like texts, by leveraging the power of generative Artificial Intelligence (GenAI). Specifically, we propose to use a deep generative model such as large language models (LLMs) to efficiently generate treatments and use their internal representation for subsequent causal effect estimation. We show that the knowledge of this true internal representation helps disentangle the treatment features of interest, such as specific sentiments and certain topics, from other possibly unknown confounding features. Unlike existing methods, the proposed GenAI-Powered Inference (GPI) methodology eliminates the need to learn representation directly from the data, and hence produces more accurate and efficient estimates. We formally establish the conditions required for the nonparametric identification of the average treatment effect, propose an estimation strategy that avoids the violation of the overlap assumption, and derive the asymptotic properties of the proposed estimator through the application of double machine learning. Finally, using an instrumental variables approach, we extend the proposed GPI methodology to the settings in which the treatment feature is based on human perception. The GPI is also applicable to text reuse where an LLM is used to regenerate existing texts. We conduct simulation and empirical studies, using the generated text data from an open-source LLM, Llama 3, to illustrate the advantages of our estimator over state-of-the-art representation learning algorithms. An open-source software package is available for implementing the proposed GPI methodology.
