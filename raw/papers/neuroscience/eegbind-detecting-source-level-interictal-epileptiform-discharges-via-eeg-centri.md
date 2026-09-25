---
title: "EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding"
authors: "Muchen Li, Anglin Liu, Xuetian Gao, Ruijian Xu, Jintai Chen"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-11T06:00:26.870286"
arxiv_id: "http://arxiv.org/abs/2609.09728v1"
source_api: "arxiv"
categories: "cs.LG, cs.MM, q-bio.NC"
---

# EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding

**著者**: Muchen Li, Anglin Liu, Xuetian Gao, Ruijian Xu, Jintai Chen
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Source-level analysis of interictal epileptiform discharges (IEDs) is relevant to presurgical evaluation and treatment planning because it helps characterize where epileptiform activity is likely to arise. Beyond detecting whether an IED is present, this setting requires assigning IED-positive activity to clinically meaningful brain-region categories. This setting is challenging because source-region evidence in short electroencephalography (EEG) windows can be subtle, partial, and affected by subject variability, class imbalance, and imperfect multimodal context. We present EEGBind, an EEG-centric multimodal binding framework for five-class source-level IED classification. EEGBind treats EEG as the primary modality and binds synchronized video-context features around an EEG-centric representation. Instead of relying on early or overly strong multimodal fusion, which may perturb the source-sensitive EEG representation, EEGBind uses video context as auxiliary evidence for robust classification. A view-consistent repair stage is further used to improve hidden-set robustness while preserving the learned source-class boundary. On the NeuroMM 2026 Grand Challenge Track 3 NMM-Source-IED benchmark, EEGBind achieves 0.8395 on weighted-F1 and outperforms strong competitors. These results support EEG-centric multimodal binding as a practical strategy for source-level IED classification. The open-source code is available at https://github.com/HKUSTGZ-ML4Health-Lab/NeuroMM2026_IED_Detection.
