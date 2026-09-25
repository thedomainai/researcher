---
title: "GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis"
authors: "Linh Le, Melanie Bui, My Chiffon Nguyen, Zachary Schlosser, David Williams-King"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-05T06:04:40.771345"
arxiv_id: "http://arxiv.org/abs/2609.03553v1"
source_api: "arxiv"
categories: "cs.AI, cs.CY"
---

# GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis

**著者**: Linh Le, Melanie Bui, My Chiffon Nguyen, Zachary Schlosser, David Williams-King
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Policy analysis requires more than predicting whether a proposal will pass: it requires identifying who will be affected, how those actors respond, and what follows. LLM-based policy simulations model these processes at scale, but their validity is hard to establish when plausible behaviour is never compared with observed outcomes. We introduce GPS-Bench, an evidence-grounded benchmark for governance policy simulation that links policies to relevant actors, actor actions and downstream impacts using legislative records, lobbying disclosures, regulatory documents, corporate filings, economic data and other public evidence. Actors are reconstructed from the dated record rather than prompted as archetypes, so a persona is an evidence object with provenance; a human-annotated pool forms the Gold evaluation set, while cases labelled by a separate LLM from retrieved evidence are treated as Silver supervision and never as test labels. Because every inference mode reads the same grounded state and emits the same schema, GPS-Bench turns "does multi-agent simulation help?" into a controlled comparison: we contrast joint reasoning, independent and communicating actor agents, graph-based methods and weight-level fine-tuning over one policy state. Fine-tuning on the grounded record gives the strongest actor-level impact prediction, and decomposition does not beat it; what decomposition adds is mechanism. Agents hold private, non-identical evidence, each seeing its own exposure clause, and address named partners with concrete joint proposals, what they offer, what they need in return, and why acting together beats acting alone, so the coalitions that form can be checked against the commitments the record holds. GPS-Bench therefore gives a common empirical setting for studying when evidence, actor modelling and multi-agent interaction improve the prediction and interpretation of policy outcomes.
