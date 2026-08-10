---
title: "Noise-Resilient Quantum Extreme Learning Machines for Astrophysical Spectral Analysis"
authors: "Marco Vetrano"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-28T06:00:10.024182"
doi: ""
openalex_id: "https://openalex.org/W7165501542"
source_api: "openalex"
---

# Noise-Resilient Quantum Extreme Learning Machines for Astrophysical Spectral Analysis

**著者**: Marco Vetrano
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

In this thesis we investigate the information processing capabilities of Quantum Extreme Learning Machines and discuss their real world applications in the field of astrophysics, particularly for atmospheric retrieval of exoplanets and supernovae spectral analysis, designing noise resilient models for Noise Intermediate Scale Quantum (NISQ) implementations. Extreme Learning Machines (ELMs) offer rapid training and structural efficiency by utilizing a randomized hidden layer—the reservoir—to map input data into a high-dimensional feature space, effectively linearizing complex learning problems. While traditionally implemented via randomized classical neural networks, the mathematical properties of these reservoirs naturally extend to complex physical systems. This universality has driven the development of Quantum Extreme Learning Machines (QELMs), which utilize quantum systems as the computational reservoir. In the field of physical extreme learning machines, information is processed through the internal dynamics of the system and recollected by measuring the system. In the context of QELMs, this consists in selecting a set of observables or a POVM to be measured on the reservoir, whose outcomes is then used to train the post-processing layer.In this work, we will first review the foundations of Neural Networs, ELMs and Reservoir Computers, highlighting specifically on similarities and fundamental differences between these models and develop the theory behind the quantum counterparts. Then, we demonstrate that QELMs can efficiently process and estimate quantum states well beyond the reservoir's scrambling time, beyond which the information should be irretrievable through local measurements. Furthermore, we show that within this regime, specific classes of Hamiltonians achieve reconstruction accuracies matching those of global random unitary dynamics. Following these theoretical aspects, we design noise-resilient QELM architectures tailored for the spectral analysis of complex astrophysical phenomena. We apply these models to exoplanetary atmospheric retrieval and supernova remnant datasets, particularly deploying the algorithm for the exoplanetary context on real quantum hardware (IBM Fez). By evaluating various pre-processing and encoding strategies—including Dense Angle Encoding, IQP embedding, and Data Re-uploading—we demonstrate that these noise-resilient QELMs are highly adaptable to different classes of astrophysical objects and capable of extracting critical spectral parameters also on NISQ devices, paving the way for real world applications of Quantum Computing in the astrophysical field.
