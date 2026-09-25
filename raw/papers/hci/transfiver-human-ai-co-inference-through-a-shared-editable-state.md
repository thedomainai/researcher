---
title: "Transfiver: Human-AI Co-Inference through a Shared Editable State"
authors: "Minji Park, Seunghyun Yoon, Hyuk Lim"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-05T06:03:15.149321"
arxiv_id: "http://arxiv.org/abs/2609.03797v1"
source_api: "arxiv"
categories: "cs.AI, cs.CL, cs.HC"
---

# Transfiver: Human-AI Co-Inference through a Shared Editable State

**著者**: Minji Park, Seunghyun Yoon, Hyuk Lim
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Long-term human-AI interaction is difficult because the information that guides inference is updated implicitly by the model and is not directly inspectable or controllable by the user. We introduce the TRANSparent Framework for Interactive, Verifiable, Editable Representation (Transfiver), an architecture for human-AI co-inference through a shared editable state. Its central idea is that interaction-specific information is maintained in a single persistent state $(S_t)$ that both the model and the human update.
  Transfiver distinguishes two modes of state evolution. In an implicit stream update, the model interprets ongoing interaction and decides whether new information revises an existing state item or creates a new one. In an explicit directed edit, a human inspects and modifies an addressed item. Both act on the same underlying state, so a human correction changes the state that subsequent computation reads, rather than adding another instruction or separate record.
  The architecture separates shared parameters $(θ)$, learned before ordinary use, from the persistent state $(S_t)$, which evolves during deployment without parameter retraining. Extending Transfiver to rich natural-language, relational, and large-scale shared states remains open.
