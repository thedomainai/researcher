---
title: "SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings"
authors: "Julia Ive, Felix Jozsa, Evridiki Georgaki, Nabeel Sheikh, Emma Cattell"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-11-14T06:13:38.653008"
doi: "https://doi.org/10.21203/rs.3.rs-11288339/v1"
openalex_id: "https://openalex.org/W7164487170"
source_api: "openalex"
---

# SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings

**著者**: Julia Ive, Felix Jozsa, Evridiki Georgaki, Nabeel Sheikh, Emma Cattell
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

Abstract Background: Large language models (LLMs) are increasingly used to access organisational documentation, including standard operating procedures (SOPs), HR policies and institutional guidelines. However, retrieval-augmented generation (RAG) approaches that rely on free-form rewriting can introduce hallucinations and unstable trade-offs between completeness and conciseness, particularly in safety-and compliance-critical settings. Objectives: To evaluate extraction as a hallucination-resistant alternative to rewriting-based RAG, and to compare strategies that balance precision, recall and safety across document types and model scales. Methods: We compare multiple prompting strategies, including line-number-based source selection, extraction of relevant guideline sentences with explicit annotation of safety-related content, and a multi-stage pipeline that refines draft answers using supporting evidence from the source guideline. Constrained extraction strategies enable more reliable selection of clinically relevant source content, while direct verbatim copying provides a strong precision-oriented baseline. Experiments are conducted on documents of varying length (local NHS guidelines in acute care and oncology, as well as UK-wide NICE guidelines) and structures, using both frontier-scale and smaller locally deployable models. Performance is assessed using automatic metrics and via human expert evaluation of relevance and completeness. Results: Line-number selection provides the most consistent recall improvements for shorter, protocol-like guidelines across both large and small models, achieving medical-term recall of up to 95%. For substantially longer guidelines, draft-first extraction achieves the highest recall with selected frontier models, reaching up to 97%. Safety-oriented approaches improve precision but introduce systematic omissions, and multi-stage filtering further amplifies this trade-off. Conclusions: Line-number selection provides a robust alternative to rewriting-based RAG for accessing organisational documentation. Drafting-based approaches may offer additional benefits in very long-document settings. These findings highlight the importance of adapting retrieval strategies to document structure, model scale and the risks of omission.
