---
title: "Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning"
authors: "Ye-Chan Kim, Seunghee Choi, SeungJu Cha, Si-Woo Kim, Hwiseon Kim"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-05T06:04:45.716104"
arxiv_id: "http://arxiv.org/abs/2609.04183v1"
source_api: "arxiv"
categories: "cs.CV, cs.AI"
---

# Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning

**著者**: Ye-Chan Kim, Seunghee Choi, SeungJu Cha, Si-Woo Kim, Hwiseon Kim
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions lack visual grounding and are rigidly assigned to every inter-event gap at a fixed location and duration. To address these, we propose Seeing Before Synthesizing (SBS), a framework that adaptively provides visually grounded linguistic guidance only where warranted. Leveraging a VLM, we generate frame-level narratives for the inter-event gaps and detect transitions from the semantic variation across them. For identified transitions, we then refine inter-event temporal masks by blending the temporal midpoint with the semantic change point and selecting the width that maximizes vision-language alignment. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance in both captioning and localization.
