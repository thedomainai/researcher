---
title: "Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification"
authors: "Zihan Wang, Daixin Li, Guilin Wang, Mushal Zia, Xiaoqi Wei"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-23T06:00:24.996205"
arxiv_id: "http://arxiv.org/abs/2609.23317v1"
source_api: "arxiv"
categories: "q-bio.NC"
---

# Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification

**著者**: Zihan Wang, Daixin Li, Guilin Wang, Mushal Zia, Xiaoqi Wei
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Epileptic seizures arise from complex, nonlinear interactions within brain networks, yet reliable electroencephalographic (EEG) prediction remains challenging due to the nonstationary and heterogeneous nature of neural dynamics. Existing methods typically analyze EEG data as static or weakly time-dependent snapshots, overlooking the intrinsic dynamics and lacking the geometric sensitivity to capture the hierarchical, localized evolution of the epileptogenic zone. To address these limitations, we propose an offline, patient-specific evaluation of chaotic dynamics-regulated topological learning (CDRTL) for distinguishing preictal from interictal EEG states. This framework unifies chaotic dynamics, multiscale algebraic topology, and local network differentiation. Specifically, we partition EEG signals into discrete functional subnets based on correlation strengths, capturing the multi-scale connectivity of the brain. By modeling each node as a Lorenz oscillator, we embed the underlying chaotic dynamics into the network architecture. We then apply the persistent Laplacian to simultaneously extract topological invariants and geometric shape evolution through harmonic and non-harmonic spectral analysis. Additionally, a node-removal topological differentiation strategy isolates localized neural contributions. Our framework was evaluated on the CHB-MIT database using balanced preictal and interictal labels and stratified channel-level cross-validation within each patient. The results support offline discrimination of preictal and interictal channel-level nodes within fixed patient-specific networks. Because representations are constructed from the complete network, including held-out unlabeled nodes, before cross-validation, the reported performance is specific to this transductive setting and does not establish generalization to unseen EEG windows, seizures, or patients.
