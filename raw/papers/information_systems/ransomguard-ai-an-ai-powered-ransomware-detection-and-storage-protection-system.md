---
title: "RansomGuard AI: An AI-Powered Ransomware Detection and Storage Protection System"
authors: "Rithvik Rajmohan, Roheith R, Bharath R, P. Durgadevi"
year: 2026
citations: 0
paper_type: "primary"
domain: "information_systems"
fetched: "2026-10-29T20:40:17.830878"
doi: "https://doi.org/10.17148/ijarcce.2026.1510120"
openalex_id: "https://openalex.org/W7224081452"
source_api: "openalex"
---

# RansomGuard AI: An AI-Powered Ransomware Detection and Storage Protection System

**著者**: Rithvik Rajmohan, Roheith R, Bharath R, P. Durgadevi
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 情報システム

## Abstract

Ransomware continues to pose a severe threat to data availability by executing unauthorized encryption, rapid file alterations, and malicious extension changes across local file storage.This paper introduces RansomGuard AI, an integrated defense-in-depth storage surveillance and recovery system designed to monitor filesystem events, analyze behavioral risk indicators, and maintain cryptographically verified snapshot recovery points.Operating on a Python FastAPI backend paired with a reactive web dashboard, the framework continuously evaluates filesystem activity against key telemetry signals: modification rates, burst write frequencies, Shannon entropy shifts, and file extension mutations.To guarantee disaster recovery without relying on compromised storage, recovery copies are secured using immutable SHA-256 manifest checkpoints.The system includes a sandboxed synthetic attack simulator that reproduces ransomwarelike behaviors inside an isolated environment, demonstrating complete monitoring, detection, audit logging, and pointin-time recovery workflows without exposing the host OS to live malware.
