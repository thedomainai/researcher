---
title: "Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery"
authors: "Kevin Zhou, Sparsh Roy"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-23T06:00:24.995208"
arxiv_id: "http://arxiv.org/abs/2609.23924v1"
source_api: "arxiv"
categories: "cs.LG, q-bio.NC"
---

# Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery

**著者**: Kevin Zhou, Sparsh Roy
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supervised comparator evaluated here outperforms every foundation-model configuration, including validation-selected fine-tuning. We then examine a key confound: foundation models and task-specific decoders are normally evaluated using different input pipelines. Retraining three supervised architectures on the broadband arrays consumed by the foundation models produces matched-input accuracy differences of opposite sign across architectures: broadband input improves ATCNet by 0.078 accuracy while reducing EEG Conformer accuracy by 0.088. None of the three individual matched-input terms is significant after multiple-comparison correction at n = 9, so we treat the sign variation descriptively rather than as a formal architecture-by-pipeline interaction. These observed sign differences suggest that a single comparator may not provide an architecture-invariant decomposition of a pretrained-versus-supervised performance gap. The four-class deficit also does not reproduce uniformly across motor-imagery datasets: on two-class BNCI2014-004 we cannot detect the same separation between fine-tuned CBraMod and the supervised comparators. Finally, validation-fitted temperature scaling returns foundation-model calibration error to the supervised range despite substantially lower four-class accuracy.
