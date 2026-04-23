---
title: "Cogninet: an explainable deep learning model for multi-class MRI-based Alzheimer’s disease staging"
authors: "Treeve White, Sareh Rowlands"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-04-18T06:00:10.336523"
doi: "https://doi.org/10.1007/s11548-026-03617-z"
openalex_id: "https://openalex.org/W7154576533"
source_api: "openalex"
---

# Cogninet: an explainable deep learning model for multi-class MRI-based Alzheimer’s disease staging

**著者**: Treeve White, Sareh Rowlands
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Abstract Purpose Alzheimer’s Disease (AD) is a neurodegenerative condition which presents significant challenges in early diagnosis and clinical decision-making. This paper seeks to address key limitations in existing research—namely, a reliance on binary classification, a lack of model interpretability, and minimal consideration for clinical usability. Methods This paper presents CogniNet , a novel convolutional neural network (CNN) architecture specifically designed for the classification of Alzheimer’s progression using magnetic resonance imaging (MRI) data. CogniNet combines the architectural depth of VGGNet19 with the feature reuse and gradient efficiency of DenseNet201, mitigating vanishing gradients while promoting richer internal representations. Trained on axial slices from preprocessed T1-weighted MRI scans, the model performs four-way classification and uses gradient-weighted class activation mapping (Grad-CAM) to generate class-specific attention maps to visually highlight regions most influential to improve interpretability. Results CogniNet was tested on 3,200 unseen axial MRI slices using standard performance metrics achieving 98% accuracy and 98% sensitivity. This paper compared CogniNet’s performance against several established CNN architectures and prior research and demonstrates improved performance. Conclusion These results highlight CogniNet as a high-performing and explainable deep learning model suitable for AI-assisted neuroimaging diagnostics. Beyond quantitative performance, the model provided interpretable outputs through Grad-CAM attention maps, allowing end users to visually audit which regions of the brain influenced predictions—an essential step toward clinical trust and adoption.
