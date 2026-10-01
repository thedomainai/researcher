---
title: "Adversarial GLUE: A Multi-Task Benchmark for Robustness Evaluation of Language Models"
authors: ["Boxin Wang", "Chejian Xu", "Shuohang Wang", "Zhe Gan", "Yu Cheng", "Jianfeng Gao", "Ahmed Hassan Awadallah", "Bo Li"]
year: 2021
cited_by_count: 72
doi: "https://doi.org/10.48550/arxiv.2111.02840"
openalex_id: W3208206463
paper_type: preprint
evidence_kind: article
topics: ["evaluation"]
landmark: false
abstract_source: "openalex"
---

# Adversarial GLUE: A Multi-Task Benchmark for Robustness Evaluation of Language Models

**Authors**: Boxin Wang, Chejian Xu, Shuohang Wang, Zhe Gan, Yu Cheng, Jianfeng Gao, Ahmed Hassan Awadallah, Bo Li | **Year**: 2021 | **Cited by**: 72 | **Kind**: article | **Relevance**: evaluation: supporting

## Abstract

Large-scale pre-trained language models have achieved tremendous success across a wide range of natural language understanding (NLU) tasks, even surpassing human performance. However, recent studies reveal that the robustness of these models can be challenged by carefully crafted textual adversarial examples. While several individual datasets have been proposed to evaluate model robustness, a principled and comprehensive benchmark is still missing. In this paper, we present Adversarial GLUE (AdvGLUE), a new multi-task benchmark to quantitatively and thoroughly explore and evaluate the vulnerabilities of modern large-scale language models under various types of adversarial attacks. In particular, we systematically apply 14 textual adversarial attack methods to GLUE tasks to construct AdvGLUE, which is further validated by humans for reliable annotations. Our findings are summarized as follows. (i) Most existing adversarial attack algorithms are prone to generating invalid or ambiguous adversarial examples, with around 90% of them either changing the original semantic meanings or misleading human annotators as well. Therefore, we perform a careful filtering process to curate a high-quality benchmark. (ii) All the language models and robust training methods we tested perform poorly on AdvGLUE, with scores lagging far behind the benign accuracy. We hope our work will motivate the development of new adversarial attacks that are more stealthy and semantic-preserving, as well as new robust language models against sophisticated adversarial attacks. AdvGLUE is available at https://adversarialglue.github.io.
