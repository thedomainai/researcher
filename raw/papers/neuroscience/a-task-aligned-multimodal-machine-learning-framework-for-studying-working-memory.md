---
title: "A task-aligned multimodal machine learning framework for studying working memory dysfunction in Parkinson’s disease"
authors: "Mercedes Terry, Samuel Birkholz, Jeffrey Johnson, Jau-Shin Lou, Asenath Huether"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-08-14T06:05:41.101618"
doi: "https://doi.org/10.1007/s11571-026-10526-z"
openalex_id: "https://openalex.org/W7162000679"
source_api: "openalex"
---

# A task-aligned multimodal machine learning framework for studying working memory dysfunction in Parkinson’s disease

**著者**: Mercedes Terry, Samuel Birkholz, Jeffrey Johnson, Jau-Shin Lou, Asenath Huether
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

<title>Abstract</title> Cognitive impairment is one of the most functionally debilitating non-motor symptoms in Parkinson's disease (PD). Yet, current diagnostic and clinical practices rely heavily on subjective assessments and burdensome behavioral testing, which lack the temporal resolution to detect subtle deficits. While EEG and pupillometry offer promising non-invasive insights into cognitive processing, more scalable and objective methods are needed to detect subtle and often elusive dysfunction in early PD. Machine learning (ML) leverages patterns in neurophysiological signals recorded during cognitive tasks to identify subtle impairments that may not be evident in standard evaluations. We recorded EEG and pupillometry data from 68 participants (35 PD, 33 healthy controls (HC)) during a visual Change Detection working memory task. Using our custom, standardized feature-extraction toolbox, we extracted 108 features and incorporated the resulting feature matrices into an ML pipeline. We applied SMOTE to balance the classes, then used principal component analysis (PCA) to reduce dimensionality. An automated elbow method identified optimal cutoffs for principal components (PCs) and original features, which guided subsequent recursive elimination (RE) for computational efficiency. We trained a support vector machine with a radial basis function kernel (RBF-SVM) to classify PD and evaluated the final model's performance on a hold-out dataset. The automated elbow method identified optimal cutoffs at 20 PCs and 22 original features. The RE revealed that a model using 14 PCs and the top 7 PCA-weighted features achieved the highest performance, with 71% accuracy and an F1 score of 0.701. The classifier's performance declined slightly when tested on held-out data, with an accuracy of 63% and an F1 score of 0.626. This study demonstrates the potential of a task-aligned ML pipeline for uncovering early cognitive markers of PD. The framework supports traceable tools that link classification back to specific physiological features and task stages, supporting mechanistic investigation of cognitive dysfunction in PD.
