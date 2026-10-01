---
title: "Parameter-Efficient Transfer Learning for NLP"
authors: ["Neil Houlsby", "Andrei Giurgiu", "Stanisław Jastrzȩbski", "Bruna Morrone", "Quentin de Laroussilhe", "Andréa Gesmundo", "Mona Attariyan", "Sylvain Gelly"]
year: 2019
cited_by_count: 141
doi: "https://doi.org/10.48550/arxiv.1902.00751"
openalex_id: W2913946806
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# Parameter-Efficient Transfer Learning for NLP

**Authors**: Neil Houlsby, Andrei Giurgiu, Stanisław Jastrzȩbski, Bruna Morrone, Quentin de Laroussilhe, Andréa Gesmundo, Mona Attariyan, Sylvain Gelly | **Year**: 2019 | **Cited by**: 141 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Fine-tuning large pre-trained models is an effective transfer mechanism in NLP. However, in the presence of many downstream tasks, fine-tuning is parameter inefficient: an entire new model is required for every task. As an alternative, we propose transfer with adapter modules. Adapter modules yield a compact and extensible model; they add only a few trainable parameters per task, and new tasks can be added without revisiting previous ones. The parameters of the original network remain fixed, yielding a high degree of parameter sharing. To demonstrate adapter's effectiveness, we transfer the recently proposed BERT Transformer model to 26 diverse text classification tasks, including the GLUE benchmark. Adapters attain near state-of-the-art performance, whilst adding only a few parameters per task. On GLUE, we attain within 0.4% of the performance of full fine-tuning, adding only 3.6% parameters per task. By contrast, fine-tuning trains 100% of the parameters per task.
