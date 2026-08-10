---
title: "Amagi-NIPU v1.1: Neuro-Immune Processing Unit for Ethical, High-Assurance AI Systems"
authors: "Alexey Mikhailovich Burlai"
year: 2026
citations: 8
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-06-26T06:02:45.242730"
doi: "https://doi.org/10.5281/zenodo.20753401"
openalex_id: "https://openalex.org/W7165371574"
source_api: "openalex"
---

# Amagi-NIPU v1.1: Neuro-Immune Processing Unit for Ethical, High-Assurance AI Systems

**著者**: Alexey Mikhailovich Burlai
**年**: 2026 | **被引用数**: 8
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

License: This work is dual-licensed.(1) CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/legalcode(2) S-APL v2.0 — full text in the attached PDF and at https://zenodo.org/records/20753406 The Zenodo `license` field shows CC BY-NC 4.0 (the SPDX ID accepted by Zenodo); S-APL v2.0 governs any commercial or safety-critical use of derivative works. ─────────────────────────────────────────────── Neuro-Immune Processing Unit specification for the AMAGI Architectural Class — defines the deterministic, single-core safety controller that enforces the TTP Triad (Timely, Tamper-evident, Provable) through six hardware invariants and a hardware-resident Safety Control Core (SCC) finite state machine. SCOPEEstablishes the normative contract for the central safety computation element of an AMAGI-compliant system: a non-pipelined, non-speculative, fixed-latency processor with hardware-enforced safety transitions, cryptographic attestation on every state change, and a hard real-time CRTM (Critical Response Time Monitor) bounded at ≤ 15 µs. NIPU is the computational heart of the AMAGI class and is consumed by Framework v2.0 (architectural contract), MEM v1.1 (memory access patterns), and MPS v2.0 (timing and clock parameters). THE SIX INVARIANTS• INV-001 — Single-Core Determinism: no caches, no speculation, no pipelining, fixed-latency instruction stream• INV-002 — Hardware-Enforced TTP Triad: CRTM response ≤ 15 µs, EGW gate-close latency ≤ 50 ns, cryptographic attestation on every safety transition• INV-003 — Dual-Tier Trust Model: Tier-1 (Safety Kernel) and Tier-2 (Application Sandbox) with one-way isolation• INV-004 — Memory Partitioning: MAG, SHMF, Audit Log regions enforced in hardware• INV-005 — Cryptographic Determinism: ML-KEM-1024, ML-DSA-44, SLHDSA-128f from first boot• INV-006 — Provable Shutdown: any invariant violation forces CRTM-safe state within one watchdog tick KEY SUBSYSTEMS• SCC FSM (Safety Control Core Finite State Machine) — hardware-resident, non-bypassable state machine governing all safety transitions; consolidates the v1.0 ICG (Inter-Context Guard) and TDF (Temporal Determinism Filter) into a single authoritative controller• CRTM (Critical Response Time Monitor) — hardware timer enforcing the ≤ 15 µs safety response bound; any violation triggers INV-006 shutdown• EGW (Emergency Gate Wrangler) — hardware path closing safety gates in ≤ 50 ns, independent of software state• MAG Adapter — read-only interface to the Master Authority Guard (eFuse/OTP), exposing root keys and CRTM hash• Audit Diode Interface — unidirectional write path to the Audit Log for INV-006-compliant attestation VERSION 1.1Version 1.1 supersedes NIPU v1.0 (Zenodo record 10.5281/zenodo.17682668). Principal changes: (a) consolidation of ICG and TDF into the unified SCC FSM, eliminating two deprecated subsystems and reducing verification surface; (b) formalization of the CRTM ≤ 15 µs bound as a hardware-enforced invariant; (c) full PQC migration aligned with Amagi-Q; (d) harmonization with Master Parameter Sheet v2.0 timing parameters; (e) explicit alignment with the Dual-Tier Trust Model defined in Framework v2.0. ALIGNMENTThis document is normatively aligned with: Framework v2.0, MEM v1.1, MPS v2.0, HARA v1.0, FMEDA v1.0, Open Spec v1.1, NIST Profile v1.1, Traceability Matrix v1.0, S-APL v2.0, and AGIAM Charter v1.2.
