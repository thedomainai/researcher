---
title: "DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION"
authors: ["Pengcheng He", "Xiaodong Liu", "Jianfeng Gao", "Weizhu Chen"]
year: 2021
cited_by_count: 913
doi: null
openalex_id: W3122890974
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION

**Authors**: Pengcheng He, Xiaodong Liu, Jianfeng Gao, Weizhu Chen | **Year**: 2021 | **Cited by**: 913 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Recent progress in pre-trained neural language models has significantly improved the performance of many natural language processing (NLP) tasks. In this paper we propose a new model architecture \textbf{DeBERTa} (\textbf{D}ecoding-\textbf{e}nhanced \textbf{BERT} with disentangled \textbf{a}ttention) that improves the BERT and RoBERTa models using two novel techniques. The first is the disentangled attention mechanism, where each word is represented using two vectors that encode its content and position, respectively, and the attention weights among words are computed using disentangled matrices on their contents and relative positions. Second, an enhanced mask decoder is used to incorporate absolute positions in the decoding layer to predict the masked tokens in model pre-training. We show that these two techniques significantly improve the efficiency of model pre-training and performance of downstream tasks. Compared to RoBERTa-Large, a DeBERTa model trained on half of the training data performs consistently better on a wide range of NLP tasks, achieving improvements on MNLI by +0.9% (90.2% vs. 91.1%), on SQuAD v2.0 by +2.3% (88.4% vs. 90.7%) and RACE by +3.6% (83.2% vs. 86.8%). The DeBERTa code and pre-trained models will be made publicly available.
