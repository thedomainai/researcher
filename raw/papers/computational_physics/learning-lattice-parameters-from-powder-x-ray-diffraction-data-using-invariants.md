---
title: "Learning lattice parameters from powder X-ray diffraction data using invariants"
authors: "E. Hofgard, Kyucheol Min, Nofit Segal, David Moreau, Aria Mansouri Tehrani"
year: 2027
citations: 1
paper_type: "primary"
domain: "computational_physics"
fetched: "2026-11-27T06:08:42.864419"
doi: "https://doi.org/10.1107/s2053273326010284"
openalex_id: "https://openalex.org/W7171428924"
source_api: "openalex"
---

# Learning lattice parameters from powder X-ray diffraction data using invariants

**著者**: E. Hofgard, Kyucheol Min, Nofit Segal, David Moreau, Aria Mansouri Tehrani
**年**: 2027 | **被引用数**: 1
**タイプ**: primary | **分野**: 計算物理学

## Abstract

We present a machine learning (ML) method to determine unit-cell parameters from powder X-ray diffraction (XRD) data using a novel invariant lattice representation. In ML, the data representation used can have a substantial impact on the prediction quality. Previous approaches have directly predicted lattice parameters (a, b, c, α, β, γ) from XRD inputs. However, these parameters depend strongly on the unit-cell reduction or convention used. In this work, we construct an invariant representation of the reciprocal lattice that is independent of primitive-cell convention, based on the bispectrum - a descriptor built from spherical harmonic projections of lattice points. The calculation of the lattice bispectrum is differentiable, and we demonstrate how to invert it using gradient-based optimization initialized from a nearest-neighbor lookup. We show that, with a fixed ML model architecture, using the lattice bispectrum as the ML target rather than the unit-cell parameters leads to more accurate lattice parameter predictions. For example, using the MP-20 dataset, a subset of the Materials Project database, the bispectrum reduces length mean absolute percentage error (MAPE) from 11.08% to 2.43% and angle MAPE from 12.15% to 2.45% compared with direct prediction with the same model architecture. We additionally benchmark our approach against pre-existing XRD data to crystal structure models such as Crystalyze and assess its performance on experimental data. Beyond unit-cell representation, we anticipate this invariant lattice representation could serve more broadly as a geometry-aware target for other crystallographic ML tasks such as structure generation.
