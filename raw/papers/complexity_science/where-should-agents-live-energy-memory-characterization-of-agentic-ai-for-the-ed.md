---
title: "Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum"
authors: "Carolina Fortuna, Vid Hanžel, Tim Strnad, Blaž Bertalanič"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-18T06:01:00.822607"
arxiv_id: "http://arxiv.org/abs/2609.18283v1"
source_api: "arxiv"
categories: "cs.AI, cs.LG, cs.MA"
---

# Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum

**著者**: Carolina Fortuna, Vid Hanžel, Tim Strnad, Blaž Bertalanič
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

As telecommunication networks evolve toward autonomous 5G-Advanced and 6G operations, agentic artificial intelligence (AI) workflows, where large language models (LLMs) execute multi-step reasoning, invoke diagnostic tools, retrieve domain knowledge, and coordinate across agent teams, are increasingly embedded across the edge-cloud continuum. While the biological brain accomplishes complex cognition on an exceptionally modest metabolic power budget of approximately 20W contemporary LLMs are profoundly energy- and memory-intensive, making sustainable lifecycle orchestration a critical operational priority. However, existing AI lifecycle metrics evaluate only isolated, single-model inferences or overlook multi-agent execution graphs entirely. Consequently, network operators lack foundational models to determine whether distributed agent communication incurs meaningful energy costs and where across edge-cloud tiers agent teams should physically reside. To address this gap, we introduce agentic-eCAL, generalizing the Energy Cost of AI Lifecycle (eCAL) metric to directed multi-agent workflows by coupling a closed-form two-rate single-call energy model (compute-bound prefill and memory-bound decode) with 7-layer OSI data transport. Grounded in hundreds of GPU benchmark configurations on NVIDIA A100 and H100, 16 open-weight models and 8 orchestration topologies, we validate components of the metric and study workflow placement implications. Our findings demonstrate that inter-agent text transport incurs 0.25% of workflow energy across 5G RAN, metro, and optical links. Therefore in edge-cloud agent placement the dominant energy cost of distribution is often not the transmission of inter-agent text itself, but the additional inference and context processing induced by that communication.
