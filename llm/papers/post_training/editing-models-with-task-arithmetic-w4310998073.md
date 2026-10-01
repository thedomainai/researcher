---
title: "Editing Models with Task Arithmetic"
authors: ["Gabriel Ilharco", "Marco Túlio Ribeiro", "Mitchell Wortsman", "Suchin Gururangan", "Ludwig Schmidt", "Hannaneh Hajishirzi", "Ali Farhadi"]
year: 2022
cited_by_count: 31
doi: "https://doi.org/10.48550/arxiv.2212.04089"
openalex_id: W4310998073
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# Editing Models with Task Arithmetic

**Authors**: Gabriel Ilharco, Marco Túlio Ribeiro, Mitchell Wortsman, Suchin Gururangan, Ludwig Schmidt, Hannaneh Hajishirzi, Ali Farhadi | **Year**: 2022 | **Cited by**: 31 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Changing how pre-trained models behave -- e.g., improving their performance on a downstream task or mitigating biases learned during pre-training -- is a common practice when developing machine learning systems. In this work, we propose a new paradigm for steering the behavior of neural networks, centered around \textit{task vectors}. A task vector specifies a direction in the weight space of a pre-trained model, such that movement in that direction improves performance on the task. We build task vectors by subtracting the weights of a pre-trained model from the weights of the same model after fine-tuning on a task. We show that these task vectors can be modified and combined together through arithmetic operations such as negation and addition, and the behavior of the resulting model is steered accordingly. Negating a task vector decreases performance on the target task, with little change in model behavior on control tasks. Moreover, adding task vectors together can improve performance on multiple tasks at once. Finally, when tasks are linked by an analogy relationship of the form ``A is to B as C is to D", combining task vectors from three of the tasks can improve performance on the fourth, even when no data from the fourth task is used for training. Overall, our experiments with several models, modalities and tasks show that task arithmetic is a simple, efficient and effective way of editing models.
