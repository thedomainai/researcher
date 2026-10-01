---
title: "Asking and Answering Questions to Evaluate the Factual Consistency of Summaries"
authors: ["Alex Wang", "Kyunghyun Cho", "Mike Lewis"]
year: 2020
cited_by_count: 337
doi: "https://doi.org/10.18653/v1/2020.acl-main.450"
openalex_id: W3034188538
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Asking and Answering Questions to Evaluate the Factual Consistency of Summaries

**Authors**: Alex Wang, Kyunghyun Cho, Mike Lewis | **Year**: 2020 | **Cited by**: 337 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Practical applications of abstractive summarization models are limited by frequent factual inconsistencies with respect to their input.Existing automatic evaluation metrics for summarization are largely insensitive to such errors.We propose QAGS, 1 an automatic evaluation protocol that is designed to identify factual inconsistencies in a generated summary.QAGS is based on the intuition that if we ask questions about a summary and its source, we will receive similar answers if the summary is factually consistent with the source.To evaluate QAGS, we collect human judgments of factual consistency on model-generated summaries for the CNN/DailyMail (Hermann et al., 2015) and XSUM (Narayan et al., 2018) summarization datasets.QAGS has substantially higher correlations with these judgments than other automatic evaluation metrics.Also, QAGS offers a natural form of interpretability: The answers and questions generated while computing QAGS indicate which tokens of a summary are inconsistent and why.We believe QAGS is a promising tool in automatically generating usable and factually consistent text.Code for QAGS will be available at https://github. com/W4ngatang/qags.Article: On Friday, 28-year-old Usman Khan stabbed reportedly several people at Fishmongers' Hall in London with a large knife, then fled up London Bridge.Members of the public confronted him; one man sprayed Khan with a fire extinguisher, others struck him with their fists and took his knife, and another, a Polish chef named ukasz, harried him with a five-foot narwhal tusk.[. . .] Summary : On Friday afternoon , a man named Faisal Khan entered a Cambridge University building and started attacking people with a knife and a fire extinguisher .Question 1: What did the attacker have ?Article answer: a large knife Summary answer: a knife and a fire extinguisher Question 2: When did the attack take place ?
