---
title: "Editing Factual Knowledge in Language Models"
authors: ["Nicola De Cao", "Wilker Ferreira Aziz", "Ivan S. Titov"]
year: 2021
cited_by_count: 172
doi: "https://doi.org/10.18653/v1/2021.emnlp-main.522"
openalex_id: W3154575616
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Editing Factual Knowledge in Language Models

**Authors**: Nicola De Cao, Wilker Ferreira Aziz, Ivan S. Titov | **Year**: 2021 | **Cited by**: 172 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

The factual knowledge acquired during pretraining and stored in the parameters of Language Models (LMs) can be useful in downstream tasks (e.g., question answering or textual inference).However, some facts can be incorrectly induced or become obsolete over time.We present KNOWLEDGEEDITOR, a method which can be used to edit this knowledge and, thus, fix 'bugs' or unexpected predictions without the need for expensive retraining or fine-tuning.Besides being computationally efficient, KNOWLEDGEEDITOR does not require any modifications in LM pretraining (e.g., the use of meta-learning).In our approach, we train a hyper-network with constrained optimization to modify a fact without affecting the rest of the knowledge; the trained hyper-network is then used to predict the weight update at test time.We show KNOWL-EDGEEDITOR's efficacy with two popular architectures and knowledge-intensive tasks: i) a BERT model fine-tuned for fact-checking, and ii) a sequence-to-sequence BART model for question answering.With our method, changing a prediction on the specific wording of a query tends to result in a consistent change in predictions also for its paraphrases.We show that this can be further encouraged by exploiting (e.g., automatically-generated) paraphrases during training.Interestingly, our hyper-network can be regarded as a 'probe' revealing which components need to be changed to manipulate factual knowledge; our analysis shows that the updates tend to be concentrated on a small subset of components. 1 How is Namibia's capital city called?Semantically equivalent Answers Scores Namibia Nigeria Nibia Namibia Tasman -0.43 -0.69 -0.89 -1.08 -1.19What is the capital of Namibia?Answers Scores Namibia Nigeria Nibia Tasman Namibia -0.32 -0.79 -0.87 -1.14 -1.16What is the capital of Russia?Answers Scores
