---
title: "Bias-aware error-compensation framework for approximate multipliers in DNN hardware accelerators"
authors: "Ahsan Rafiq, Salvatore Pappalardo, Alberto Bosio, Maksim Jenihhin"
year: 2026
citations: 0
paper_type: "primary"
domain: "corporate_governance"
fetched: "2026-09-05T06:05:04.184049"
doi: "https://doi.org/10.1016/j.micpro.2026.105326"
openalex_id: "https://openalex.org/W7206156137"
source_api: "openalex"
---

# Bias-aware error-compensation framework for approximate multipliers in DNN hardware accelerators

**著者**: Ahsan Rafiq, Salvatore Pappalardo, Alberto Bosio, Maksim Jenihhin
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートガバナンス

## Abstract

Multiplication dominates the computational cost and energy consumption of deep neural network (DNN) inference. This paper presents a novel bias-aware two-stage error compensation that generates structured families of approximate multipliers (AMs) with analytically controllable error bias and magnitude while maintaining uniform energy consumption within each family of AMs. Using a truncation-based signed multiplier as a base, the first compensation stage of the framework introduces deterministic binary compensation at the least significant bits to mitigate systematic underestimation without adding arithmetic logic or increasing switching activity. The second stage inserts a two-gate compensation circuit at the first column after truncation, supplying a fixed positive mean error that works in conjunction with the constant to drive the net mean bias error towards zero. The combination provides a unified closed-form design equation, from which any member of the family is fully characterised without simulation. The proposed AM designs are synthesized in a 45 nm technology and compared with state-of-the-art AMs using a comprehensive set of error metrics. All the multipliers are evaluated on LeNet-5, ResNet-14, VGG-16, and VGG-19 under INT8 post-training quantization (PTQ). Proposed 8 × 8 AMs achieved up to 31.41% reduction in power-delay product (PDP) when compared with the state-of-the-art design, with accuracy drops below 1% across all four benchmarks.
