---
title: "Implementation of a secure digital data exchange framework based on post-quantum cryptography"
authors: "Nhu-Quynh Luc, Duc-Huy Quach, Thanh-Long Le-Nguyen, Duy-Phuong Nguyen"
year: 2026
citations: 0
paper_type: "primary"
domain: "quantum_mechanics"
fetched: "2026-11-27T06:06:05.293524"
doi: "https://doi.org/10.11591/eei.v15i6.13736"
openalex_id: "https://openalex.org/W7236646845"
source_api: "openalex"
---

# Implementation of a secure digital data exchange framework based on post-quantum cryptography

**著者**: Nhu-Quynh Luc, Duc-Huy Quach, Thanh-Long Le-Nguyen, Duy-Phuong Nguyen
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 量子力学・量子情報

## Abstract

Quantum computing threatens Rivest-Shamir-Adleman (RSA)- and elliptic-curve-based data exchange, motivating practical post-quantum cryptography (PQC). This study implements a cross-platform file-exchange framework using Kyber-1024 for key encapsulation mechanism (KEM)-based session-key establishment, Falcon-1024 detached signatures, and advanced encryption standard (AES)-256-cipher block chaining mode (CBC) for bulk encryption. Evaluation covered an IEEE 802.11ac Linux/Windows testbed (1,000–40,365 KiB) and controlled single-host transmission control protocol (TCP)-loopback runs up to 102,400 KiB. The three reported Linux-to-Linux wireless session-key-establishment times averaged 25.26 ms (approximately 25.3 ms); encrypting 4,352 KiB in 29.8 ms yielded 142.6 MiB/s. Inspection of captured packets revealed no plaintext file content or session-key material in the application payloads, and a forged file/signature pair was rejected. These results support implementation feasibility on commodity hardware within the tested workflow, but they do not establish authenticated key exchange, active man-in-the-middle (MITM) resistance, metadata confidentiality, or traffic-analysis resistance.
