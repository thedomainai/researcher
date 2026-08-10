---
title: "Amagi-MEM v1.1: Self-Protecting, Context-Aware Memory Architecture for High-Assurance AI Systems"
authors: "Alexey Mikhailovich Burlai"
year: 2026
citations: 8
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-06-26T06:02:45.244042"
doi: "https://doi.org/10.5281/zenodo.20753402"
openalex_id: "https://openalex.org/W7165365448"
source_api: "openalex"
---

# Amagi-MEM v1.1: Self-Protecting, Context-Aware Memory Architecture for High-Assurance AI Systems

**著者**: Alexey Mikhailovich Burlai
**年**: 2026 | **被引用数**: 8
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

License: This work is dual-licensed.(1) CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/legalcode(2) S-APL v2.0 — full text in the attached PDF and at https://zenodo.org/records/20753406 The Zenodo `license` field shows CC BY-NC 4.0 (the SPDX ID accepted by Zenodo); S-APL v2.0 governs any commercial or safety-critical use of derivative works. ─────────────────────────────────────────────── High-assurance memory substrate specification for the AMAGI Architectural Class — defines the three-tier memory hierarchy that enforces INV-004 (Memory Partitioning) and INV-006 (Provable Shutdown) for safety-critical autonomous Cyber-Physical Systems where data integrity, contextual authenticity, and deterministic shutdown outweigh raw performance. SCOPEEstablishes the normative contract for all addressable and non-addressable storage in an AMAGI-compliant system: immutable roots of trust in eFuse/OTP, executable code in SHMF regions, and append-only audit logging through a hardware audit diode. The MEM specification is consumed by Framework v2.0 (architectural contract), NIPU v1.1 (memory access FSM), and MPS v2.0 (memory map parameters). MEMORY TIERS• MAG (Master Authority Guard) — eFuse / One-Time-Programmable region holding CRTM hash, root public key, silicon serial number, and calibration constants. Read-only after manufacturing; write attempts trigger INV-006 shutdown.• SHMF (Safety-critical Hardened Memory Framework) — executable code and static data regions with SEC-DED ECC, write-protected during safety transitions, and protected by cryptographic hash chains recomputed every watchdog tick.• Audit Log — append-only, hash-chained record of all safety state transitions, written through a hardware audit diode that physically prevents read-back from the application tier. DUAL-TIER TRUST MODELThe MEM hierarchy enforces the INV-003 Dual-Tier Trust Model: Tier-1 (Safety Kernel) has read access to MAG and write access to SHMF and Audit Log; Tier-2 (Application Sandbox) has no direct access to MAG and can only append to the Audit Log through the diode. This separation aligns with the FDA Pre-market Certifiable Change Package (PCCP) model — Tier-1 changes require full recertification, Tier-2 changes may be deployed under PCCP without recertification. KEY MECHANISMS• ECC (Error-Correcting Code) — SEC-DED on all SHMF regions; double-bit errors trigger INV-006 shutdown• Cryptographic hash chains — SHA-3-256 over SHMF blocks, recomputed every watchdog tick• Audit diode — unidirectional write path from Tier-1/Tier-2 to Audit Log, physically enforced in FPGA fabric• INV-006 compliance — any invariant violation forces CRTM-safe state within one watchdog tick, with full audit trail VERSION 1.1Version 1.1 supersedes MEM v1.0 (Zenodo record 10.5281/zenodo.17679327). Principal changes: (a) consolidation of the audit diode as a hardware-enforced INV-006 mechanism; (b) explicit alignment with the Dual-Tier Trust Model and FDA PCCP; (c) harmonization with Master Parameter Sheet v2.0 memory map parameters; (d) removal of deprecated ICG and TDF mechanisms, consolidated into the SCC FSM defined in NIPU v1.1. ALIGNMENTThis document is normatively aligned with: Framework v2.0, NIPU v1.1, MPS v2.0, HARA v1.0, FMEDA v1.0, Open Spec v1.1, NIST Profile v1.1, Traceability Matrix v1.0, S-APL v2.0, and AGIAM Charter v1.2.
