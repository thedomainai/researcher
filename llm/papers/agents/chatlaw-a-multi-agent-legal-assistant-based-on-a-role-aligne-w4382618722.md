---
title: "Chatlaw: A Multi-Agent Legal Assistant based on a Role-Aligned Mixture-of-Experts Architecture"
authors: ["Jiaxi Cui", "Munan Ning", "Zongjian Li", "Hao Li", "Yan Yang", "Bohua Chen", "Bin Ling", "Yonghong Tian", "et al."]
year: 2026
cited_by_count: 91
doi: "https://doi.org/10.1016/j.fmre.2026.03.026"
openalex_id: W4382618722
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Chatlaw: A Multi-Agent Legal Assistant based on a Role-Aligned Mixture-of-Experts Architecture

**Authors**: Jiaxi Cui, Munan Ning, Zongjian Li, Hao Li, Yan Yang, Bohua Chen, Bin Ling, Yonghong Tian, et al. | **Year**: 2026 | **Cited by**: 91 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Artificial Intelligence (AI) holds great potential in legal services, yet Large Language Models (LLMs) face two major challenges: limited knowledge of the Chinese legal system and vulnerability to hallucinations. To address these issues, we present Chatlaw, a multi-agent legal assistant. Chatlaw’s framework is designed to emulate the Standard Operating Procedures (SOP) of real law firms, where different roles (e.g., assistant, researcher, senior lawyer) collaborate on a case. To computationally mirror this collaborative structure, we developed a novel Role-Aligned Mixture-of-Experts (RA-MoE) architecture. In this system, the internal "experts" are specifically trained to align with the distinct tasks of each agent role (e.g., inquiry, analysis, drafting). These specialized agents (Legal Assistant, Researcher, etc.) then form the collaborative framework. When they interact with users, retrieve legal knowledge, analyze case details, or generate reliable consultations, the RA-MoE architecture intelligently routes their computations to the corresponding dedicated expert, ensuring each step is handled by the most qualified parameters. In evaluations, Chatlaw surpasses general-purpose AI models, including GPT-4, achieving a 7.73% improvement in accuracy on the LawBench benchmark and an 11-point higher score on the Unified Qualification Exam for Legal Professionals. Real-case studies and expert assessments further confirm its robustness. Chatlaw enhances the accessibility and reliability of legal services, advancing the provision of legal support to the public. Chatlaw is an advanced AI legal assistant that improves the accuracy and reliability of legal services. It integrates a high-quality legal dataset, a Role-Aligned Mixture-of-Experts (RA-MoE) architecture, and a multi-agent system to provide precise, case-specific legal advice. By emulating real law firm workflows, it reduces errors and outperforms general AI models like GPT-4, achieving better results in legal benchmarks and real-world evaluations. Chatlaw makes legal services more accessible, marking a significant step forward in AI for law.
