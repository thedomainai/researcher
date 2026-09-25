---
title: "Road-oriented attention and class-balanced learning for post-disaster road damage segmentation"
authors: "Tsujimoto Eda, Eom Sunyong, Suzuki Tsutomu"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-08-11T06:02:30.245281"
doi: ""
openalex_id: "https://openalex.org/W7202015154"
source_api: "openalex"
---

# Road-oriented attention and class-balanced learning for post-disaster road damage segmentation

**著者**: Tsujimoto Eda, Eom Sunyong, Suzuki Tsutomu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Accurate pixel-level segmentation of post-disaster road damage is important for decision-support applications that require reliable and spatially explicit road-scene understanding. This study proposes a deep-learning framework for localizing visible road-damage regions in post-disaster imagery. The framework integrates a Road-Oriented Multi-Level Attention (RO-MLA) module into a DeepLabV3+ backbone, where channel-, spatial-, and pixel-level attention are guided by an average road-mask prior to concentrate feature learning on road-relevant regions. To address severe class imbalance and weak feature contrast in disaster-related road imagery, we further introduce a Road-Oriented Class-Weighted Balanced Dice (RO-Dice CWB) loss to improve the segmentation of sparse, low-contrast, and underrepresented damage regions. To evaluate the framework, we construct a merged dataset from the Post-Disaster Road Damage Dataset-Japan (PDRDD-J) and the Social Media Disaster Road Damage (SoDR) dataset, yielding 2684 pixel-level annotated images across real-world road-damage scenarios. Validation-based ablation studies support the selection of the DeepLabV3+ base architecture, ResNet152 backbone, and RO-Dice CWB loss. On the held-out test set, the proposed framework achieves an mIoU of 0.7248 and a damage-class IoU of 0.6029, outperforming representative segmentation baselines including U-Net, FCN, ResUNet, standard DeepLabV3+, and MLA DeepLabV3+. Qualitative, resolution-sensitivity, and error-map analyses further show that the proposed attention and loss design produces more coherent damage masks while maintaining stable road-region interpretation. These results demonstrate that the proposed framework supports post-disaster road damage segmentation and offers a task-specific approach for learning sparse, imbalanced, and visually ambiguous targets in complex road scenes.
