---
title: "OmniGuard AI: A Dual-Engine Platform for Code Leakage and Phishing Defense"
authors: "Santhosh V, Yuvan Sundar R, Vishwa Kumar R, Sathya B"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-11-22T06:00:34.147494"
doi: "https://doi.org/10.22214/ijraset.2026.85569"
openalex_id: "https://openalex.org/W7237227901"
source_api: "openalex"
---

# OmniGuard AI: A Dual-Engine Platform for Code Leakage and Phishing Defense

**著者**: Santhosh V, Yuvan Sundar R, Vishwa Kumar R, Sathya B
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

In modern software development environments, sensitive credential exposure and phishing attacks remain two of the most critical security vulnerabilities threatening enterprise infrastructure. Traditional security solutions often operate in isolation and identify vulnerabilities long after code has been committed or applications deployed. This paper presents OmniGuard AI, an integrated dual-engine security platform that unifies static secret detection, automated remediation and phishing threat analysis. Engine 1 (Code Secret Scanner) combines regular-expression signatures with Shannon entropy scoring to detect hardcoded API keys, database connection strings and tokens, while Engine 2 (Phishing Threat Analyzer) evaluates URLs with structural and lexical feature heuristics to assign risk scores. To enforce a “shift-left” security model, the platform provides a local Git pre-commit hook that intercepts credential leaks before they are committed, and Credential Shield JS, a lightweight browser-side runtime monitoring module. An automated refactoring engine then remediates detected vulnerabilities by replacing hardcoded credentials with secure environment-variable calls (os.getenv()). The prototype is implemented in Python Flask with a browser dashboard and is validated functionally on backend and frontend routes: the scanner reports simulated credentials with file, line, signature, entropy and severity, no false positives were observed on the clean templates tested, and the pre-commit hook is implemented to abort commits that contain credential patterns. By bridging pre-commit prevention with application-level threat analysis, OmniGuard AI provides a scalable, developer-centric framework for enterprise security assurance.
