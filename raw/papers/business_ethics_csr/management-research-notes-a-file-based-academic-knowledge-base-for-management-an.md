---
title: "Management Research Notes: A File-Based Academic Knowledge Base for Management and Business Sustainability Research"
authors: "Binqi Tang"
year: 2026
citations: 0
paper_type: "primary"
domain: "business_ethics_csr"
fetched: "2026-05-13T06:02:58.021661"
doi: "https://doi.org/10.5281/zenodo.20129499"
openalex_id: "https://openalex.org/W7160826765"
source_api: "openalex"
---

# Management Research Notes: A File-Based Academic Knowledge Base for Management and Business Sustainability Research

**著者**: Binqi Tang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経営倫理・CSR

## Abstract

Management Research Notes is a portable, file-based academic knowledge base for management and business sustainability research. Each peer-reviewed article becomes one Markdown note with YAML frontmatter (trusted bibliographic metadata, a controlled-vocabulary topic taxonomy, three custom analytic fields — unit_of_analysis, level_of_theory, dependent_variable_family — and verbatim evidence anchors on every factual claim) and a human-readable distillation (research question, mechanism, theoretical contribution, practical implication, limitations, future research, APA citation). A small Python pipeline derives a SQLite index with FTS5, a CSV export, and a BibTeX file from the notes, and a two-layer faithfulness audit (mechanical substring check on evidence anchors plus a cold-context Claude subagent scoring prose fields against a published rubric) gates every note into the library. Version 0.13.0 (2026-05-12) contains 197 curated notes — adds AMJ vol-67-no-1 (11 notes: Barkema, Bettinazzi, Cao, Dorobantu, Gruber editorial, Han, Jia, two Park papers, Soublière, To). The vol-67-no-1 batch is the second consecutive batch ingested under the Tier 3 prevention infrastructure (tools/populate_manifest.py, introduced in v0.12.0) and the post-extraction column-merge heuristic in docs/extraction-prompt.md (commit 59a9ace) — all 11 papers passed Layer 1 (anchor validity) on first extraction and Layer 2 audit with only 1 PARTIAL across the batch: 77 from the Network for Business Sustainability (NBS) February 2026 monthly digest (62 in v0.2.0 plus 15 previously-missing papers recovered in v0.3.0) and a 120-note Academy of Management Journal pilot across vol. 67 no. 1, vol. 67 no. 2, vol. 67 no. 3, vol. 67 no. 4, vol. 67 no. 5, vol. 67 no. 6, vol. 68 no. 1 through vol. 68 no. 6, and vol. 69 no. 1 (vol. 67 no. 1 added in v0.13.0). The full library passes the v0.13.0 audit sweep with 197/197 PASS and zero CONTRADICTED verdicts across thirteen release cycles. An AGENTS.md file provides a tool-agnostic entry point so that AI agents (Claude Code, Cursor, Windsurf, custom SDK apps) can discover and consume the data with known faithfulness guarantees.
