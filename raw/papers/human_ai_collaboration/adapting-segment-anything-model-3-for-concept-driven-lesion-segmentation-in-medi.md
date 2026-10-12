---
title: "Adapting Segment Anything Model 3 for concept-driven lesion segmentation in medical images: an experimental study"
authors: "Guoping Xu, Jayaram K. Udupa, Yubing Tong, Xin Long, Ying Zhang"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-10-13T06:03:27.745706"
doi: "https://doi.org/10.1186/s42492-026-00234-0"
openalex_id: "https://openalex.org/W7143352533"
source_api: "openalex"
---

# Adapting Segment Anything Model 3 for concept-driven lesion segmentation in medical images: an experimental study

**著者**: Guoping Xu, Jayaram K. Udupa, Yubing Tong, Xin Long, Ying Zhang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Abstract Accurate segmentation of lesions is fundamental for medical image analysis. However, most existing approaches are designed for specific anatomical sites and imaging modalities, limiting their applicability in heterogeneous clinical environments. Recent vision-language foundation models have enabled concept-driven segmentation of natural images, offering a promising path toward more flexible and generalizable medical image segmentation. However, to the best of the authors’ knowledge, concept-prompt-based lesion segmentation in medical images, particularly using the latest Segment Anything Model 3 (SAM3), has not been thoroughly examined. In this paper, the authors present a systematic investigation of the SAM3 framework for lesion segmentation. An extensive evaluation of SAM3 was first conducted using geometric bounding boxes and concept-based text and image exemplars as prompts for lesion segmentation across multiple cancer types and imaging modalities, including magnetic resonance imaging, computed tomography, ultrasound, dermoscopy, and endoscopic imaging, with particular emphasis on volumetric medical imaging datasets. To improve robustness and segmentation accuracy, additional knowledge into the input representation was further integrated, including predictions from adjacent slices, multiparametric imaging information, and prior annotations. In addition, the study compared different SAM3 fine-tuning strategies on the BraTS2023-MET dataset, including partial module fine-tuning, adapter-based optimization, and full-model fine-tuning, under different training objectives. Extensive experiments conducted on 13 datasets covering 11 lesion types demonstrate that SAM3 achieves strong cross-modality generalization and accurate instance-specific lesion delineation. These results highlight the potential of concept-driven foundation models for scalable and practical medical-image segmentation in real-world clinical settings. The source code and dataset splits are publicly available at https://github.com/apple1986/lesion-sam3 .
