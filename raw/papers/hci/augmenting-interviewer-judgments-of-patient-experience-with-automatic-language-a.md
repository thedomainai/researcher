---
title: "Augmenting Interviewer Judgments of Patient Experience with Automatic Language Analysis"
authors: "Aowen Shi, Michal Balazia, Danilo Postin, René Hurlemann, Jan Alexandersson"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-02T08:56:05.863401"
arxiv_id: "http://arxiv.org/abs/2608.31007v1"
source_api: "arxiv"
categories: "cs.HC, cs.CL"
---

# Augmenting Interviewer Judgments of Patient Experience with Automatic Language Analysis

**著者**: Aowen Shi, Michal Balazia, Danilo Postin, René Hurlemann, Jan Alexandersson
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Understanding how psychiatric patients subjectively experienced a clinical conversation is important for feedback and alliance-related process monitoring. While interviewers form post-session judgments about patient experience, these judgments do not always match patients' self-reports. Automatic approaches for predicting perceived interaction quality from conversation have been proposed, but it remains unclear whether such approaches can complement human judgment rather than simply replicate it. To address this gap, we evaluate a clinician-support framework in which post-session interviewer ratings are combined with automatic language-based predictions to estimate patient-reported interaction quality in free clinical interviews. We assess this integration across multiple standard model types, including Ridge, SVR, MLP, GRU, and BiLSTM, all trained on sentence embeddings extracted from dyadic transcripts of 107 free conversations between psychiatric patients and interviewers. Our results show that combining interviewer judgments with model predictions through simple averaging yields the strongest overall performance. The interviewer-only baseline reached a Pearson correlation of 0.365. Among fully automatic models, Ridge achieved the strongest Pearson correlation (r = 0.286), while BiLSTM achieved r = 0.270. The strongest result was obtained by BiLSTM interviewer integration (r = 0.403). Our findings suggest that automatic language analysis and interviewer judgment capture complementary aspects of patient experience and that their combination provides a more accurate approximation of the patient's own report than either source alone.
