---
title: "Flamingo: a Visual Language Model for Few-Shot Learning"
authors: ["Alayrac, Jean-Baptiste", "Jeff Donahue", "Pauline Luc", "Antoine Miech", "Barr, Iain", "Yana Hasson", "Karel Lenc", "Arthur Mensch", "et al."]
year: 2022
cited_by_count: 1238
doi: "https://doi.org/10.48550/arxiv.2204.14198"
openalex_id: W4225323055
paper_type: preprint
evidence_kind: article
topics: ["elicitation"]
landmark: true
abstract_source: "openalex"
---

# Flamingo: a Visual Language Model for Few-Shot Learning

**Authors**: Alayrac, Jean-Baptiste, Jeff Donahue, Pauline Luc, Antoine Miech, Barr, Iain, Yana Hasson, Karel Lenc, Arthur Mensch, et al. | **Year**: 2022 | **Cited by**: 1238 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research. We introduce Flamingo, a family of Visual Language Models (VLM) with this ability. We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs. Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities. We perform a thorough evaluation of our models, exploring and measuring their ability to rapidly adapt to a variety of image and video tasks. These include open-ended tasks such as visual question-answering, where the model is prompted with a question which it has to answer; captioning tasks, which evaluate the ability to describe a scene or an event; and close-ended tasks such as multiple-choice visual question-answering. For tasks lying anywhere on this spectrum, a single Flamingo model can achieve a new state of the art with few-shot learning, simply by prompting the model with task-specific examples. On numerous benchmarks, Flamingo outperforms models fine-tuned on thousands of times more task-specific data.
