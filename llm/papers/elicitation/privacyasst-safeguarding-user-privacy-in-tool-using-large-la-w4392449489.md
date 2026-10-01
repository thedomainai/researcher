---
title: "PrivacyAsst: Safeguarding User Privacy in Tool-Using Large Language Model Agents"
authors: ["Xinyu Zhang", "Huiyu Xu", "Zhongjie Ba", "Zhibo Wang", "Yuan Hong", "Jian Liu", "Zhan Qin", "Kui Ren"]
year: 2024
cited_by_count: 62
doi: "https://doi.org/10.1109/tdsc.2024.3372777"
openalex_id: W4392449489
paper_type: article
evidence_kind: article
topics: ["elicitation", "agents"]
landmark: false
abstract_source: "openalex"
---

# PrivacyAsst: Safeguarding User Privacy in Tool-Using Large Language Model Agents

**Authors**: Xinyu Zhang, Huiyu Xu, Zhongjie Ba, Zhibo Wang, Yuan Hong, Jian Liu, Zhan Qin, Kui Ren | **Year**: 2024 | **Cited by**: 62 | **Kind**: article | **Relevance**: elicitation: supporting; agents: core

## Abstract

Swift advancements in large language model (LLM) technologies lead to widespread research and applications, particularly in integrating LLMs with auxiliary tools, known as tool-using LLM agents. However, amid user interactions, the transmission of private information to both LLMs and tools poses considerable privacy risks to users. In this paper, we delve into current privacy-preserving solutions for LLMs and outline three pivotal challenges for tool-using LLM agents: generalization to both open-source and closed-source LLMs and tools, compliance with privacy requirements, and applicability to unrestricted tasks. To tackle these challenges, we present PrivacyAsst, the first privacy-preserving framework tailored for tool-using LLM agents, encompassing two solutions for different application scenarios. First, we incorporate a homomorphic encryption scheme to ensure computational security guarantees for users as a safeguard against both open-source and closed-source LLMs and tools. Moreover, we propose a shuffling-based solution to broaden the framework's applicability to unrestricted tasks. This solution employs an attribute-based forgery generative model and an attribute shuffling mechanism to craft privacy-preserving requests, effectively concealing individual inputs. Additionally, we introduce an innovative privacy concept,$t$-closeness in image data, for privacy compliance within this solution. Finally, we implement PrivacyAsst, accompanied by two case studies, demonstrating its effectiveness in advancing privacy-preserving artificial intelligence.
