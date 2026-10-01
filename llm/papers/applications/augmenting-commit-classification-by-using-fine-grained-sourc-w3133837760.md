---
title: "Augmenting commit classification by using fine-grained source code changes and a pre-trained deep neural language model"
authors: ["Lobna Ghadhab", "Ilyes Jenhani", "Mohamed Wiem Mkaouer", "Montassar Ben Messaoud"]
year: 2021
cited_by_count: 46
doi: "https://doi.org/10.1016/j.infsof.2021.106566"
openalex_id: W3133837760
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "semantic_scholar"
---

# Augmenting commit classification by using fine-grained source code changes and a pre-trained deep neural language model

**Authors**: Lobna Ghadhab, Ilyes Jenhani, Mohamed Wiem Mkaouer, Montassar Ben Messaoud | **Year**: 2021 | **Cited by**: 46 | **Kind**: article | **Relevance**: applications: supporting

## Abstract

Abstract Context: Analyzing software maintenance activities is very helpful in ensuring cost-effective evolution and development activities. The categorization of commits into maintenance tasks supports practitioners in making decisions about resource allocation and managing technical debt. Objective: In this paper, we propose to use a pre-trained language neural model, namely BERT (Bidirectional Encoder Representations from Transformers) for the classification of commits into three categories of maintenance tasks — corrective, perfective and adaptive. The proposed commit classification approach will help the classifier better understand the context of each word in the commit message. Methods: We built a balanced dataset of 1793 labeled commits that we collected from publicly available datasets. We used several popular code change distillers to extract fine-grained code changes that we have incorporated into our dataset as additional features to BERT’s word representation features. In our study, a deep neural network (DNN) classifier has been used as an additional layer to fine-tune the BERT model on the task of commit classification. Several models have been evaluated to come up with a deep analysis of the impact of code changes on the classification performance of each commit category. Results and conclusions: Experimental results have shown that the DNN model trained on BERT’s word representations and Fixminer code changes (DNN@BERT+Fix_cc) provided the best performance and achieved 79.66% accuracy and a macro-average f1 score of 0.8. Comparison with the state-of-the-art model that combines keywords and code changes (RF@KW+CD_cc) has shown that our model achieved approximately 8% improvement in accuracy. Results have also shown that a DNN model using only BERT’s word representation features achieved an improvement of 5% in accuracy compared to the RF@KW+CD_cc model.
