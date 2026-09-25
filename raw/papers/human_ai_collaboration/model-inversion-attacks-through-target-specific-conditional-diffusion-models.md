---
title: "Model Inversion Attacks Through Target-Specific Conditional Diffusion Models"
authors: "Ouxiang Li, Yanbin Hao, Zhicai Wang, Bin Zhu, Shuo Wang"
year: 2026
citations: 2
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-19T10:32:06.068636"
doi: "https://doi.org/10.1145/3842389"
openalex_id: "https://openalex.org/W4403754270"
source_api: "openalex"
---

# Model Inversion Attacks Through Target-Specific Conditional Diffusion Models

**著者**: Ouxiang Li, Yanbin Hao, Zhicai Wang, Bin Zhu, Shuo Wang
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Model inversion attacks (MIAs) aim to reconstruct private images from a target classifier's training set, thereby raising privacy concerns in AI applications. Previous GAN-based MIAs tend to suffer from inferior generative fidelity due to GANs’ inherent flaws and biased optimization within the latent space. To alleviate these issues, leveraging diffusion models’ remarkable synthesis capabilities, we propose Diffusion-based Model Inversion (Diff-MI) attacks. Specifically, we introduce a novel target-specific conditional diffusion model (CDM) to purposely approximate the target classifier's private data distribution and achieve a superior accuracy-fidelity balance. Our method involves a two-step learning paradigm. Step-1 incorporates the target classifier into the entire CDM learning under a pretrain-then-finetune fashion, by creating pseudo-labels as model conditions in pretraining and optimizing specified layers with image predictions in fine-tuning. Step-2 presents an iterative image reconstruction method, further enhancing the attack performance through a combination of diffusion priors and target knowledge. Additionally, we propose an improved max-margin loss that replaces the hard max with top-k maxes, fully leveraging feature information and soft labels from the target classifier. Extensive experiments demonstrate that Diff-MI significantly improves generative fidelity with an average decrease of 20% in FID while maintaining competitive attack accuracy compared to state-of-the-art methods across various datasets and models. Our code is available at: https://github.com/Ouxiang-Li/Diff-MI .
