---
title: "Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms"
authors: ["Said Saidakhrarovich Gulyamov", "Said Saidakhrarovich Gulyamov", "Said Saidakhrarovich Gulyamov", "Said Saidakhrarovich Gulyamov", "Andrey Aleksandrovich Rodionov", "Rustam Khursanov", "Мехмонов Камбариддин Мирадхамович", "D.B. Babaev", "et al."]
year: 2026
cited_by_count: 38
doi: "https://doi.org/10.3390/info17010054"
openalex_id: W7118532765
paper_type: article
evidence_kind: article
topics: ["safety_interp", "agents"]
landmark: false
abstract_source: "openalex"
---

# Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms

**Authors**: Said Saidakhrarovich Gulyamov, Said Saidakhrarovich Gulyamov, Said Saidakhrarovich Gulyamov, Said Saidakhrarovich Gulyamov, Andrey Aleksandrovich Rodionov, Rustam Khursanov, Мехмонов Камбариддин Мирадхамович, D.B. Babaev, et al. | **Year**: 2026 | **Cited by**: 38 | **Kind**: article | **Relevance**: safety_interp: core; agents: core

## Abstract

Large language models (LLMs) have rapidly transformed artificial intelligence applications across industries, yet their integration into production systems has unveiled critical security vulnerabilities, chief among them prompt injection attacks. This comprehensive review synthesizes research from 2023 to 2025, analyzing 45 key sources, industry security reports, and documented real-world exploits. We examine the taxonomy of prompt injection techniques, including direct jailbreaking and indirect injection through external content. The rise of AI agent systems and the Model Context Protocol (MCP) has dramatically expanded attack surfaces, introducing vulnerabilities such as tool poisoning and credential theft. We document critical incidents including GitHub Copilot’s CVE-2025-53773 remote code execution vulnerability (CVSS 9.6) and ChatGPT’s Windows license key exposure. Research demonstrates that just five carefully crafted documents can manipulate AI responses 90% of the time through Retrieval-Augmented Generation (RAG) poisoning. We propose PALADIN, a defense-in-depth framework implementing five protective layers. This review provides actionable mitigation strategies based on OWASP Top 10 for LLM Applications 2025, identifies fundamental limitations including the stochastic nature problem and alignment paradox, and proposes research directions for architecturally secure AI systems. Our analysis reveals that prompt injection represents a fundamental architectural vulnerability requiring defense-in-depth approaches rather than singular solutions.
