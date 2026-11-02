---
title: "Knowledge Organization Matters: How Graph Design and Temporal Structure Shape Agentic AI Performance on Drilling Activity Reports"
authors: "Anurag Bihani, Sunil Manikani, Hakim Arabi, Minyue Liu"
year: 2026
citations: 0
paper_type: "primary"
domain: "organization_science"
fetched: "2026-11-03T06:34:29.919507"
doi: "https://doi.org/10.2118/235330-ms"
openalex_id: "https://openalex.org/W7225036264"
source_api: "openalex"
---

# Knowledge Organization Matters: How Graph Design and Temporal Structure Shape Agentic AI Performance on Drilling Activity Reports

**著者**: Anurag Bihani, Sunil Manikani, Hakim Arabi, Minyue Liu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 組織科学

## Abstract

Abstract Agentic AI over drilling reports can automate analytics that today take hours per question, from non-productive-time trending to offset-well lookup. Published systems typically commit to a single graph design without testing it: most studies in literature perform multi-method comparisons and evaluate whole pipelines and do not evaluate individual design decisions. We compare five ways of organizing a corpus for an agent (a vectorless reasoning tree, an open-vocabulary graph, that graph with community post-processing, a domain-schema graph, and a fine-grained quantitative graph) against a shared flat-vector baseline, on two public corpora: 1,681 Daily Drilling Reports from Equinor's Volve field (North Sea, 1992–2016) and 1,888 Weekly Activity Reports from Shell Offshore operations in the Gulf of Mexico (BSEE eWell archive, 2022–2024). We benchmark a ReAct agent that runs the full matrix at four capability tiers: two successive frontier versions, a fast-tier cloud model, and an open-weights 26B model on a 16 GB consumer GPU. Under frontier agents the vectorless tree leads relevance on both corpora, while hybrid retrieval leads completeness against machine-verified answer keys, with the domain-schema hybrid the strongest graph configuration. A blinded pair-preserved scoring of all 1,080 frontier cells confirms the BSEE architecture effects: hybrid retrieval beats vector-only (+0.040, Holm-corrected p=0.0004), the schema step over the open-vocabulary control is the largest effect measured (+0.068), and community post-processing alone does not contribute anything. The architecture ranking reproduces at every capability tier, and the spread widens as the agent weakens. A bi-temporal fact table with a point-in-time query tool raises as-of accuracy to 1.00 on both corpora, correcting all nine static errors with no regressions (96 paired queries, exact McNemar p=0.004). A schema audit shows the cost of a hand-designed ontology: named storms present in 30 reports were invisible to schema-graph retrieval, producing confident false negatives that open-vocabulary and vector retrieval avoided.
