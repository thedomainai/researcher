---
title: "FEQA: A Question Answering Evaluation Framework for Faithfulness Assessment in Abstractive Summarization"
authors: ["Esin Durmus", "He He", "Mona Diab"]
year: 2020
cited_by_count: 105
doi: "https://doi.org/10.18653/v1/2020.acl-main.454"
openalex_id: W3022685184
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# FEQA: A Question Answering Evaluation Framework for Faithfulness Assessment in Abstractive Summarization

**Authors**: Esin Durmus, He He, Mona Diab | **Year**: 2020 | **Cited by**: 105 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Neural abstractive summarization models are prone to generate content inconsistent with the source document, i.e. unfaithful.Existing automatic metrics do not capture such mistakes effectively.We tackle the problem of evaluating faithfulness of a generated summary given its source document.We first collected human annotations of faithfulness for outputs from numerous models on two datasets.We find that current models exhibit a trade-off between abstractiveness and faithfulness: outputs with less word overlap with the source document are more likely to be unfaithful.Next, we propose an automatic question answering (QA) based metric for faithfulness, FEQA, 1 which leverages recent advances in reading comprehension.Given questionanswer pairs generated from the summary, a QA model extracts answers from the document; non-matched answers indicate unfaithful information in the summary.Among metrics based on word overlap, embedding similarity, and learned language understanding models, our QA-based metric has significantly higher correlation with human faithfulness scores, especially on highly abstractive summaries.* Most of the work is done while the authors were at Amazon Web Services AI.1 Faithfulness Evaluation with Question Answering.
