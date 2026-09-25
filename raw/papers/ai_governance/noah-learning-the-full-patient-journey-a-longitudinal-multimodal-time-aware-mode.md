---
title: "NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting"
authors: "Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov, Özgün Turgut, Michelle Espranita Liman"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-10T06:03:52.898284"
arxiv_id: "http://arxiv.org/abs/2609.09140v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI"
---

# NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting

**著者**: Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov, Özgün Turgut, Michelle Espranita Liman
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

The digitization of healthcare has generated vast, longitudinal, and multimodal patient records over a lifetime, yet fully exploiting these data to represent and predict patient state trajectories remains a critical challenge. Current AI models often struggle to capture the complex, irregular temporal dynamics and inherent stochasticity of real-world multimodal patient data. Existing AI approaches for modeling longitudinal patient records are predominantly discriminative, limited to a few modalities, constrained by closed categorical vocabularies, treating time as a monotonic inductive bias, or they are limited in forecasting future patient states. We introduce NOAH, a time-aware, task-agnostic, generative transformer model representing and forecasting the full multimodal patient journey. NOAH features a novel bidirectional time integration and a variational latent space to capture the continuous evolution of patient states and the stochasticity of clinical trajectories. Built from over 559 million clinical events from 431,000 hospital visits of 299,000 patients across the MIMIC dataset family, NOAH natively processes medical images, time-series and numeric signals, categorical events, as well as structured and unstructured clinical records. NOAH is the first truly holistic generative model in its field, enabling autoregressive forecasting with optional time control, zero-shot classification, and counterfactual intervention simulation. It generates highly informative and predictive patient state representations that demonstrate strong performance in probing for clinical outcomes, 15 ICD chapters, and 29 comorbidities, as well as in time-to-event prediction. Seamlessly handling diverse modalities and complex temporal dynamics, NOAH provides a versatile, task-agnostic, scalable foundation for intelligent predictive systems in personalized clinical care and digital medicine.
