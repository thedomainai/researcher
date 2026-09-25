---
title: "Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs"
authors: "Kostia Kudriavtsev, Parvez Rafi, Sha Sundaram"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-11T06:00:59.928574"
arxiv_id: "http://arxiv.org/abs/2609.10430v1"
source_api: "arxiv"
categories: "cs.MA, cs.IR"
---

# Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs

**著者**: Kostia Kudriavtsev, Parvez Rafi, Sha Sundaram
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Enterprise data lakes accumulate tables faster than human stewards can document or classify them, leaving columns with missing descriptions and unassigned governance labels. This documentation debt undermines data discovery, access control, and regulatory compliance. We present Glyph, a production system that frames two coupled problems, column description generation and column type annotation for data classification, as cooperating LLM agents orchestrated as stateful graphs. The Descriptor grounds generation in the pipeline source code that produces each column, retrieved on demand from an enterprise GitHub via a reasoning--acting tool loop (active Retrieval-Augmented Generation). The Tagger assigns labels from a governed 275-leaf Data Classification Ontology by running three complementary strategies in parallel (a description tagger, a line-of-business regex tagger, and a metadata tagger backed by a fine-tuned contrastive encoder over a vector database), then fuses their ranked outputs with Reciprocal Rank Fusion (RRF). We fine-tune a 6-layer MiniLM metadata encoder with an in-batch contrastive objective, lifting same-tag retrieval on an in-distribution held-out split from NDCG@10 0.55 to 0.92 (MAP@100 $0.19 \rightarrow 0.90$) relative to the stock base encoder. We report end-to-end multi-label tagging quality under a recall-weighted F2 objective across three evaluation groups, an ablation isolating each strategy and the RRF fusion, and the engineering decisions that distinguish Glyph from prior column-type-annotation work and from commercial value/regex sensitivity scanners: value-free and code-grounded design, per-tag provenance, and graceful degradation. Together these make multi-agent LLM cataloging auditable and operable as a production service.
