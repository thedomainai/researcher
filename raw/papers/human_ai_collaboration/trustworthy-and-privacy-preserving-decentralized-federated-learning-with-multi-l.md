---
title: "Trustworthy and privacy-preserving decentralized federated learning with multi-layer defense for secure collaborative AI"
authors: "S Durga, Uma Maheshwari Shanmugam, Sachnev Vasily, Mohan Sellappa Gounder"
year: 2026
citations: 1
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-11T06:03:16.720522"
doi: "https://doi.org/10.1007/s44163-026-02045-x"
openalex_id: "https://openalex.org/W7208764802"
source_api: "openalex"
---

# Trustworthy and privacy-preserving decentralized federated learning with multi-layer defense for secure collaborative AI

**著者**: S Durga, Uma Maheshwari Shanmugam, Sachnev Vasily, Mohan Sellappa Gounder
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Decentralized Federated Learning (DFL) enables collaborative artificial intelligence model training without centralizing sensitive data, making it suitable for privacy-critical and distributed intelligent systems such as healthcare, Industrial IoT, and smart digital infrastructure. Despite its advantages, DFL remains vulnerable to privacy leakage through shared model updates and to model poisoning and backdoor attacks that compromise system reliability, robustness, and trustworthiness. Existing defense mechanisms primarily address either privacy preservation or poisoning robustness independently and often exhibit limited effectiveness under adaptive or high-ratio adversarial settings. This work proposes a trustworthy and privacy-preserving decentralized federated learning framework that jointly addresses these challenges through two integrated components: (i) a hybrid privacy mechanism based on public dataset pretraining followed by differentially private fine-tuning, and (ii) a multi-layer model defense architecture designed to mitigate poisoning and backdoor attacks across decentralized peer-to-peer environments. The framework integrates local data sanitization, peer-side model verification, robust trimmed-mean aggregation, and runtime inference protection to provide defense-in-depth across both training-time and inference-time attack surfaces. An adversary model and operational assumptions are formally defined, and the framework is evaluated under strong adversarial conditions, including a 20% poisoning ratio. Experimental results demonstrate consistent robustness improvements over a vanilla DFL baseline. While the baseline model achieves a clean accuracy of 83.10%, the proposed framework improves clean performance to 86.12%. Under adversarial conditions, accuracy improves from 37.71% to 53.88% for Fast Gradient Sign Method (FGSM) attacks, from 21.75% to 46.40% for Projected Gradient Descent (PGD) attacks, and from 40.62% to 67.35% for Carlini–Wagner (CW) attacks. For backdoor-based poisoning attacks such as BadNets and Blended attacks, the defense pipeline restores model accuracy to above 86% while maintaining stable benign performance. These findings demonstrate that the proposed framework provides an effective balance between privacy preservation, adversarial robustness, and trustworthy decentralized collaborative learning for secure AI-driven systems.
