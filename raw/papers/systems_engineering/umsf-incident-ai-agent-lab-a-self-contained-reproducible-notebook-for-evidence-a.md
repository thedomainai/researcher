---
title: "UMSF Incident AI Agent Lab: A Self-Contained Reproducible Notebook for Evidence-Aware Decision Support in Critical Infrastructure Incidents (v1.2.0)"
authors: "Dmytro Prokopovych-Tkachenko"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-10-16T06:03:11.773215"
doi: "https://doi.org/10.5281/zenodo.23380522"
openalex_id: "https://openalex.org/W7221770738"
source_api: "openalex"
---

# UMSF Incident AI Agent Lab: A Self-Contained Reproducible Notebook for Evidence-Aware Decision Support in Critical Infrastructure Incidents (v1.2.0)

**著者**: Dmytro Prokopovych-Tkachenko
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

Description / Abstract UMSF Incident AI Agent Lab is a self-contained research notebook for Google Colab and Jupyter. It accompanies version 1.0.0 of the UMSF incident AI agent, a deterministic decision-support component for evidence-aware multisensor monitoring in critical infrastructure incidents. The notebook embeds the original agent source, two synthetic incident scenarios and the companion P1 incident-dataset fixture in a SHA-256-verified payload. It needs no external dataset, language-model API, credentials or cloud storage. After three setup cells, each analysis cell can run on its own, in any order, or after a kernel restart. The experiments cover robust personal reference baselines, handling of missing channels, persistent flags, group decisions that take monitoring coverage into account, and an incident state that records the source of each item of evidence. They also cover exact lexicographic assignment of rescue teams, exact multi-resource allocation for service continuity, heuristic scheduling of recovery work, the authority model for proposals, and the integrity of the hash-chain audit trail. Both scenarios are replayed at 41 chronological cutoffs to show how the agent's assessments and proposals change as evidence arrives. All 116 original tests pass with none skipped. This includes six P1 integration tests that the standalone source archive would skip, and all 44 supplied analytical checks also pass. The release contains clean and executed notebooks, a rendered HTML report, an offline interactive replay explorer, 30 figures in PNG and SVG, CSV/JSON outputs, replay audit records and validation evidence. Local runs verified all 31 code cells in sequence in a fresh kernel, then each of the 28 analysis cells alone in its own fresh kernel. The hosted Google Colab interface has not been independently tested. Deterministic algorithms compute every decision. The optional LLM adapter is kept for provenance but is never invoked, and its compatibility with a live API is unverified. Every plan is a proposal that requires review by an authorized human. The software performs no dispatch, equipment control or real approval, and the authority demonstration is explicitly simulated. The recovery scheduler is heuristic, not optimal. Scores are not diagnoses, and silence is not treated as evidence of casualties. The audit chain supports integrity checks but is not authentication or tamper-proof storage. All records are synthetic, and neither operational safety nor rescue effectiveness has been validated. Notebook release 1.2.0 preserves agent version 1.0.0 byte for byte. Keywords critical infrastructure; incident support; AI agent; decision support; human-in-the-loop; evidence provenance; monitoring coverage; rescue logistics; constrained resource allocation; service continuity; recovery scheduling; audit trail; synthetic scenarios; reproducibility; Jupyter notebook; Google Colab
