---
title: "The AIVA Platform: A Retrieval Augmented Generation Large Language Model Postoperative Assistant"
authors: "Syed Ali Haider, Srinivasagam Prabha, Cesar A. Gomez-Cabello, Ariana Genovese, Bernardo Collaco"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-05-11T06:04:46.531958"
doi: "https://doi.org/10.5281/zenodo.20086612"
openalex_id: "https://openalex.org/W7160626352"
source_api: "openalex"
---

# The AIVA Platform: A Retrieval Augmented Generation Large Language Model Postoperative Assistant

**著者**: Syed Ali Haider, Srinivasagam Prabha, Cesar A. Gomez-Cabello, Ariana Genovese, Bernardo Collaco
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

PURPOSE: During postoperative recovery, patients and their caregivers often lack crucial information, leading to numerous repetitive inquiries that burden healthcare providers. Traditional discharge materials, including paper handouts and patient portals, are often static, overwhelming, or underutilized, leading to patient overwhelm and contributing to unnecessary ER visits and overall healthcare overutilization. Conversational chatbots offer a solution, but Natural Language Processing (NLP) systems are often inflexible and limited in understanding, while powerful Large Language Models (LLMs) are prone to generating "hallucinations". Our purpose is to combine the deterministic framework of traditional NLP with the probabilistic capabilities of LLMs, we developed the AI Virtual Assistant (AIVA) Platform. This system utilizes a retrieval-augmented generation (RAG) architecture, integrating Gemini 2.0 Flash with a medically verified knowledge base via Google Vertex AI, to safely deliver dynamic, patient-facing postoperative guidance grounded in validated clinical content. METHODS: The AIVA Platform was evaluated through 750 simulated patient interactions derived from 250 unique postoperative queries across 20 high-frequency recovery domains. Three blinded physician reviewers assessed formal system performance, evaluating classification metrics (accuracy, precision, recall, F1-score), relevance (SSI Index), completeness, and consistency (5-point Likert scale). Safety guardrails were tested with 120 out-of-scope queries and 40 emergency escalation scenarios. Additionally, groundedness, fluency, and readability were assessed using automated LLM metrics. RESULTS: The system achieved 98.4% classification accuracy (precision 1.0, recall 0.98, F1-score 0.9899). Physician reviews showed high completeness (4.83/5), consistency (4.49/5), and relevance (SSI Index 2.68/3). Safety guardrails successfully identified 100% of out-of-scope and escalation scenarios. Groundedness evaluations demonstrated strong context precision (0.951), recall (0.910), and faithfulness (0.956), with 95.6% verification agreement. While fluency and semantic alignment were high (BERTScore F1 0.9013, ROUGE-1 0.8377), readability was 11th-grade level (Flesch-Kincaid 46.34). CONCLUSION: The simulated testing demonstrated strong technical accuracy, safety, and clinical relevance in simulated postoperative care. Its architecture effectively balances flexibility and safety, addressing key limitations of standalone NLP and LLM models. While readability remains a challenge, these findings establish a solid foundation, demonstrating readiness for clinical trials and real-world testing within surgical care pathways. *Source: https://ps-rc.org/meeting/Program/2026/61.cgi*
