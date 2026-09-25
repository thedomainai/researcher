---
title: "Algorithmic fairness in AI-based fitness advice: evaluating socioeconomic bias in county-contextualized physical activity prescriptions"
authors: "Hegui Bao, Tianle Yu, J. Wang, Han Yin, Yuan Gao"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-08-28T09:14:32.222449"
doi: "https://doi.org/10.3389/fpubh.2026.1844470"
openalex_id: "https://openalex.org/W7204267605"
source_api: "openalex"
---

# Algorithmic fairness in AI-based fitness advice: evaluating socioeconomic bias in county-contextualized physical activity prescriptions

**著者**: Hegui Bao, Tianle Yu, J. Wang, Han Yin, Yuan Gao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Background Large language models (LLMs) can significantly broaden access to physical-activity guidance. However, advice that implicitly assumes available financial resources, reliable transportation, specialized equipment, or local facilities can be difficult for individuals in resource-constrained environments to act upon. We evaluated whether such resource assumptions systematically vary across socioeconomic settings when underlying health needs remain fixed. Methods We developed a county-aware, matched-counterfactual auditing framework integrating U.S. public health and socioeconomic data, synthetic patient profiles, and structured LLM outputs. To evaluate resource burden, we constructed a transparent access-cost proxy that renders each coded component directly inspectable. We evaluated accessibility-aware prompting, output reranking, alternative weighting schemes, and a bounded three-model comparative panel (including DeepSeek) to audit and mitigate socioeconomically driven bias. Results In the full DeepSeek model panel, accessibility-aware prompting reduced the access-cost proxy gap between high- and low-socioeconomic status (SES) counties from 0.306 to 0.139. Subsequent output reranking maintained this narrowed gap while simultaneously improving coarse alignment with physical-activity volume and intensity guidelines. Sensitivity analyses using alternative weighting schemes preserved the overall comparative ordering, while the three-model comparison demonstrated model-specific variations in resource-assumption responses. Discussion This study establishes a reproducible framework that connects equity-oriented health-recommender principles to traceable output auditing and targeted bias mitigation. By offering a transparent approach to evaluating implicit resource assumptions, this work provides researchers and practitioners with an actionable foundation for downstream expert, user, and implementation validation.
