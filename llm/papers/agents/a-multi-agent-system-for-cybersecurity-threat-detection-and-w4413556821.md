---
title: "A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models"
authors: ["Yasser Hmimou", "Mohamed Tabaa", "Azeddine Khiat", "Zineb Hidila"]
year: 2025
cited_by_count: 21
doi: "https://doi.org/10.1109/access.2025.3602681"
openalex_id: W4413556821
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# A Multi-Agent System for Cybersecurity Threat Detection and Correlation Using Large Language Models

**Authors**: Yasser Hmimou, Mohamed Tabaa, Azeddine Khiat, Zineb Hidila | **Year**: 2025 | **Cited by**: 21 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

As cyber-attacks rapidly evolve across communication, infrastructure and data layers, traditional security solutions such as rule-based intrusion detection systems (IDS) or signature-based antivirus programs are effective at detecting known threats, but they often lack the contextual understanding and semantic interpretation necessary to detect complex or evolving attacks. For example, spear-phishing campaigns, advanced persistent threats (APTs), and multi-stage attacks often escape detection due to their subtle and context-dependent nature. This limitation creates a critical gap in detecting coordinated or subtle attack patterns that span multiple systems and domains. The need for semantic understanding, cross-domain visibility, and adaptive detection is increasingly urgent, particularly as threat actors employ polymorphic and AI-driven strategies that traditional systems cannot interpret or correlate effectively. This paper presents a modular multi-agent architecture that integrates established cybersecurity analysis tools with large language models (LLMs) to achieve intelligent, explicable and highly accurate detection of threats across diverse data types. Three specialized agents: (1) email verification, (2) log analysis, and (3) IP address scanning each operate independently with tailored detection pipelines that combine domain-specific tools and LLM-powered semantic analysis components to identify, characterize, and report threats specific to their domain. At the core of the system lies a contextual recommendation system that processes and cross-analyzes the outputs of all specialized agents to detect complex threat patterns such as multi-vector, time-based, or stealth attacks that would otherwise evade isolated detection mechanisms. The evaluation on benchmark datasets, including CIC-IDS 2017, SpamAssassin, and custom simulated network environments, demonstrates threat detection accuracy of 93.6%, multi-agent correlation accuracy of 87%, and false positive reduction of 41.3% compared to traditional approaches. The use of LLMs for both structured explanations and chain-of-thought reporting further enhances analyst confidence and reduces triage time.
