---
title: "Lightweight Swin Transformer with Prosodic Tokens and Huber‑based HuBERT Distillation for Cross‑lingual Speech Emotion Recognition"
authors: "Maather Alkhafaji, Amir Lakizadeh"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-08-31T06:03:47.480710"
doi: "https://doi.org/10.22266/ijies2026.0930.52"
openalex_id: "https://openalex.org/W7204653387"
source_api: "openalex"
---

# Lightweight Swin Transformer with Prosodic Tokens and Huber‑based HuBERT Distillation for Cross‑lingual Speech Emotion Recognition

**著者**: Maather Alkhafaji, Amir Lakizadeh
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Speech emotion recognition (SER) is essential for affect-aware human-computer interaction, yet real-world deployment demands models that are simultaneously accurate, compact, cross-lingually robust, and reproducible.In this paper, we present a lightweight SER framework based on a Swin Transformer that achieves all four goals through three synergistic innovations.First, a dual-branch input fuses high-resolution log-Mel spectrograms with a handful of lightweight prosodic tokens (derived from pitch, energy, and rate dynamics) at negligible overhead, enriching the representation with supra-segmental cues.Second, a stage-wise local-window attention schedule (3×3→5×5→7×7→7×7) progressively expands the receptive field in deeper layers, capturing fine time-frequency micro-structure in early stages and broader prosodic phrases in later ones.Third, we distill knowledge from a frozen HuBERT teacher using a feature-alignment loss; the Huber loss proves superior to MSE and L1, yielding consistent gains.Beyond within-language tests, we perform an initial cross-lingual generalization experiment -training on four English corpora (CREMA-D, RAVDESS, SAVEE, TESS) and testing zero-shot on unseen German EMO-DBachieving 63.44% weighted accuracy with our compact student.The full model attains state-of-the-art or competitive accuracy on five benchmarks (94.02% on CREMA-D, 96.32% on EMO-DB, 96.59% on RAVDESS, 98.08% on SAVEE, 99.89% on TESS) while requiring only 0.85 million parameters and 0.32 GFLOPs, making it approximately 33× lighter than a standard Swin-Tiny model.
