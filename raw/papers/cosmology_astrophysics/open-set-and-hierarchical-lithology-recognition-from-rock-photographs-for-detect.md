---
title: "Open-set and Hierarchical Lithology Recognition from Rock Photographs for Detecting Unseen Rock Types across Two Public Image Collections"
authors: "Nidhal Becheikh, Boutheyna Belhaj Bettaieb, Taoufik S. Saidani, Refka Ghodhbani, Yahia Said"
year: 2026
citations: 0
paper_type: "primary"
domain: "cosmology_astrophysics"
fetched: "2026-11-28T08:09:11.739365"
doi: "https://doi.org/10.22266/ijies2026.1231.69"
openalex_id: "https://openalex.org/W7235080283"
source_api: "openalex"
---

# Open-set and Hierarchical Lithology Recognition from Rock Photographs for Detecting Unseen Rock Types across Two Public Image Collections

**著者**: Nidhal Becheikh, Boutheyna Belhaj Bettaieb, Taoufik S. Saidani, Refka Ghodhbani, Yahia Said
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 宇宙論・宇宙物理

## Abstract

Rock-type classifiers are usually tested on random splits of one image collection, yet deployed models meet unseen lithologies and new imaging conditions.This evaluation audit merged two public rock-photograph collections into a 15-type, three-family taxonomy and grouped duplicates and augmented copies into 3,521 deduplicated units for group-aware cross-validation of handcrafted features and frozen and fine-tuned ImageNet backbones in closed-set, hierarchical and open-set recognition.A support vector machine reached a macro-F1 of 0.758 under random imagelevel splits and 0.483 when the same images were split by source photograph, so leakage explained almost all of the drop to 0.468 on deduplicated units.In five-fold fine-tuning, ConvNeXt-T and ViT-S/16 reached 0.706 and 0.712 and could not be ranked, and about 45 percent of their errors crossed a family boundary.With score and threshold chosen on validation data only, the AUROC for unseen rock types was 0.625 to 0.748 when training on one collection and 0.734 to 0.815 on the other, while 60 to 97 percent of unknown images were still accepted.Basalt, the only shared type, was scored almost as novel as the unknown types when it came from the other collection, and a probe trained on Basalt alone identified the source collection with an AUROC of 0.94 to 0.95.
