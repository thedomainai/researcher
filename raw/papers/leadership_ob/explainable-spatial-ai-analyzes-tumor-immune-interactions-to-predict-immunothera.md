---
title: "Explainable spatial AI analyzes tumor-immune interactions to predict immunotherapy outcomes and identify new targets"
authors: "Gang Liu, Jia Wang, Jia Zhu"
year: 2026
citations: 1
paper_type: "primary"
domain: "leadership_ob"
fetched: "2026-09-14T09:13:48.505046"
doi: "https://doi.org/10.63808/ihf.v2i3.510"
openalex_id: "https://openalex.org/W7204896046"
source_api: "openalex"
---

# Explainable spatial AI analyzes tumor-immune interactions to predict immunotherapy outcomes and identify new targets

**著者**: Gang Liu, Jia Wang, Jia Zhu
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: リーダーシップ・組織行動

## Abstract

The effectiveness of immune checkpoint inhibitors (ICIs) heavily depends on the complex spatial interactions of cells within the tumor microenvironment (TME). However, existing predictive biomarkers generally lack spatial resolution and interpretability, making it difficult to guide clinical decisions or reveal actionable targets. This study aims to develop an interpretable spatial AI framework to systematically decode the tumor-immune spatial architecture, achieve high-accuracy predictions of immunotherapy responses, and identify new immunotherapy targets. We collected pre-treatment tumor samples from melanoma and non-small cell lung cancer patients across multiple centers, simultaneously obtaining spatial transcriptomics and multiplex immunofluorescence data. We developed a deep learning framework called “SpaImmune,” which integrates graph attention networks and visual transformer architectures, modeling hundreds of thousands of cells based on their real spatial coordinates as a heterogeneous graph network to automatically learn multi-scale features of the immune microenvironment. The model’s explainability module uses attention weight mechanisms and SHAP values to quantify each spatial component’s contribution to predictions and extract higher-order interaction rules. In three independent validation cohorts, SpaImmune predicted the objective response to ICIs with area under the curve (AUC) values all over 0.91, significantly outperforming methods based on immune cell density, PD-L1 expression, and traditional machine learning. Explainability analysis revealed that the tight spatial coupling of B cells and CD4⁺ follicular helper T cells in tertiary lymphoid structures (TLS) is the strongest feature for predicting treatment response. More importantly, by scanning the cell-gene spatial colocalization network built by the model, we discovered a molecule called SLAMF7, previously unreported as an immune target, which is highly expressed specifically in immune-active regions and associated with good prognosis. Subsequent in vitro functional tests confirmed that activating SLAMF7 can enhance CD8⁺ T cell tumor-killing function, while blocking it weakens immunotherapy effects. Explainable spatial AI can faithfully reveal the intrinsic logic of tumor-immune interactions, not only greatly improving predictive accuracy for immunotherapy but also directly guiding rational discovery of new targets, offering a whole new paradigm for spatial intelligence-driven precision immuno-oncology.
