---
title: "AI-Assisted Identity and Access Threat Detection Using the AITIR Framework for Public-Sector Cybersecurity Environments"
authors: "Md Sazzad Hossain, Sheikh Md Faysal, Md Abu Kawsar Prodhan Hemal, Subha Shamarukh"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-21T06:01:01.556928"
doi: "https://doi.org/10.32996/jcsts.2025.7.12.62"
openalex_id: "https://openalex.org/W7164888881"
source_api: "openalex"
---

# AI-Assisted Identity and Access Threat Detection Using the AITIR Framework for Public-Sector Cybersecurity Environments

**著者**: Md Sazzad Hossain, Sheikh Md Faysal, Md Abu Kawsar Prodhan Hemal, Subha Shamarukh
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

In public-sector cybersecurity, the password has become the prize. Agencies have moved their services into the cloud and now hand out access to employees, contractors, and members of the public alike, and that change has dragged the fight off the network perimeter and onto the credential itself. We describe AITIR, short for Adaptive Identity-and-access Threat Intelligence and Response, a layered machine-learning framework that watches for identity-based attacks as they happen and coordinates a response inside the governance rules agencies already have to follow. Three models share the detection work: a gradient-boosted classifier reads each access attempt, a bidirectional sequence model reads the order of an account's actions, and a graph-based behavior-analytics module flags the moment a session drifts away from an identity's usual company. Sitting on top of them, an explainable triage layer passes only the high-confidence, well-justified alerts to a person. To test the design, we assembled a corpus of about 14.8 million authentication and access events, part public benchmark data and part synthetic identity telemetry, and pushed credential stuffing, password spraying, privilege escalation, session hijacking, and insider misuse through it. AITIR scored an F1 of 0.967 and an area under the ROC curve of 0.985, ahead of all five baselines. Over a four-quarter deployment simulation it cut successful identity-based intrusions by 31.4 percent, brought mean time to detect down by 62 percent, and trimmed false positives by 41 percent against a conventional operations baseline. A cost-benefit model, scaled to a national public-sector portfolio, points to roughly US$10.2 billion in avoided cost a year and about 79,000 analyst hours given back. Those last two numbers are projections built on stated assumptions, not audited savings, and we say so plainly. The paper closes on the governance, staffing, and validity questions that decide whether any of them survives contact with a real agency.
