---
title: "An improved RT-DETR algorithm for small-object detection in UAV aerial images"
authors: "Qiyu Long, Zhixun Liang, Peng Chen, Peng Tang"
year: 2026
citations: 1
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-03T06:06:01.296085"
doi: "https://doi.org/10.1038/s41598-026-69495-2"
openalex_id: "https://openalex.org/W7118533186"
source_api: "openalex"
---

# An improved RT-DETR algorithm for small-object detection in UAV aerial images

**著者**: Qiyu Long, Zhixun Liang, Peng Chen, Peng Tang
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Abstract To address the challenges of UAV aerial imagery, including the prevalence of small objects, complex background interference, and difficulty in feature extraction that lead to high missed detection rates and compromise detection accuracy in existing RT-DETR algorithms, this paper proposes an improved small-object-oriented detector named MSFE-DETR (Multi-Scale Feature Enhancement DETR). A CMFE (CSP-MultiScale Feature Enhancement) module is integrated into the shallow backbone layers to enhance feature representation of small objects and alleviate feature loss caused by scale and background complexity. In deeper layers of backbone, the C2f module is employed to preserve fine-grained details and improve target–background discrimination, while multi-scale feature fusion further prevents small object information degradation. In addition, Deformable Attention (DAttention) is incorporated to adaptively focus on small target regions, retaining spatial positional information and suppressing background noise. The head integrates MPCA and FSA modules, where MPCA progressively fuses adjacent-scale features to complementarily enhance small object representations and suppress background interference, and FSA further improves detail enhancement and robustness. Moreover, an Inner-SIoU loss is proposed by combining Inner-IoU with SIoU, improving localization accuracy, convergence speed, and robustness in complex scenes. Experimental results on the VisDrone 2019 dataset show that MSFE-DETR outperforms RT-DETR-r18 by 1.9% in Precision, 2.1% in Recall and 2.4% in mAP@0.5, while real-time inference is maintained at 68.7 FPS. On the infrared HIT-UAV and satellite SIMD datasets, mAP@0.5 improves by 5.8% and 2.3% respectively over the baseline.
