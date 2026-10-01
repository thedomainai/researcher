---
title: "LinkBERT: Pretraining Language Models with Document Links"
authors: ["Michihiro Yasunaga", "Jure Leskovec", "Percy Liang"]
year: 2022
cited_by_count: 317
doi: "https://doi.org/10.18653/v1/2022.acl-long.551"
openalex_id: W4221153690
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# LinkBERT: Pretraining Language Models with Document Links

**Authors**: Michihiro Yasunaga, Jure Leskovec, Percy Liang | **Year**: 2022 | **Cited by**: 317 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Language model (LM) pretraining captures various knowledge from text corpora, helping downstream NLP tasks.However, existing methods such as BERT model a single document, failing to capture document dependencies and knowledge that spans across documents.In this work, we propose LinkBERT, an effective LM pretraining method that incorporates document links, such as hyperlinks.Given a pretraining corpus, we view it as a graph of documents, and create LM inputs by placing linked documents in the same context.We then train the LM with two joint self-supervised tasks: masked language modeling and our newly proposed task, document relation prediction.We study LinkBERT in two domains: general domain (pretrained on Wikipedia with hyperlinks) and biomedical domain (pretrained on PubMed with citation links).LinkBERT outperforms BERT on various downstream tasks in both domains.It is especially effective for multi-hop reasoning and few-shot QA (+5% absolute improvement on HotpotQA and TriviaQA), and our biomedical LinkBERT attains new state-of-the-art on various BioNLP tasks (+7% on BioASQ and USMLE).We release the pretrained models, LinkBERT and BioLinkBERT, as well as code and data. 1
