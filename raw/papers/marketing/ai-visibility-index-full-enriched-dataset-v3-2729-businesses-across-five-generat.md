---
title: "AI Visibility Index — Full Enriched Dataset (v3): 2,729 Businesses Across Five Generative AI Search Systems"
authors: "Joel House"
year: 2026
citations: 0
paper_type: "primary"
domain: "marketing"
fetched: "2026-05-09T06:05:40.165704"
doi: "https://doi.org/10.5281/zenodo.20076406"
openalex_id: "https://openalex.org/W7160543359"
source_api: "openalex"
---

# AI Visibility Index — Full Enriched Dataset (v3): 2,729 Businesses Across Five Generative AI Search Systems

**著者**: Joel House
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: マーケティング

## Abstract

This dataset accompanies the v3 release of the AI Visibility Index paper. It is the full enriched per-business panel for n = 2,729 businesses sampled across 14 verticals (personal injury law; real estate; dental; accounting; med spa; home services; financial advisors; SaaS-CRM; SaaS project management; digital marketing; e-commerce DTC baby; boutique hospitality; insurance brokers; personal-finance apps) and four metropolitan markets (Los Angeles, New York, Chicago, Sydney). Each business was probed against five generative AI systems — ChatGPT GPT-4o, Anthropic Claude Sonnet, Perplexity sonar-pro, Google Gemini 2.5-flash, and Google AI Overview via SerpApi — with approximately 95 intent-based prompts per system, producing 266,844 paired (business, model, prompt) observations. The CSV (`phase2-anonymized-dataset.csv`) has 2,729 rows × 74 columns. Each row is one business, identified by an opaque `BIZ_P2_xxxxx` ID; brand names, URLs, place IDs, and any directly identifying field have been removed. Columns cover: AI-visibility outcomes per model and a composite visibility score; ranking and reputation (Google rank position, Google review count and rating, Moz Domain Authority); robots / crawler configuration; on-page signals (schema, citability, FAQ, sitemap, indexed pages, blog count, llms.txt); SpyFu organic-search performance; twelve off-page presence indicators (Reddit and Quora mention counts, Wikipedia, LinkedIn, Crunchbase, BBB, Yelp, Trustpilot, G2, Capterra, Google Business, YouTube), aggregate directory and review-platform counts, and an off-page composite score; Moz total external links; press coverage rollup over the trailing 12 months; and a tier-3 backlinks/trends/press composite. Coverage caveat: the dataset includes 426 businesses for which no first-party URL could be resolved (no detectable web presence at sampling time). For those rows, all URL-dependent enrichment columns (Domain Authority, SpyFu, on-page) are null by design. After the URL-backfill pass, coverage on the remaining ~2,300 URL-resolved rows is ~80% non-null on Domain Authority, ~84% on SpyFu organic metrics, and ~84% on on-page signals; off-page presence indicators (Reddit, Quora, Wikipedia, LinkedIn, etc.) are populated for ≥99% of all 2,729 rows. README.md gives full per-column missingness, codebook, and data-quality flags. Twelve analysis-output JSONs accompany the CSV and reproduce the headline tables and figures of the v3 paper, including descriptive statistics (`analysis.json`), raw and partial correlations with FDR correction (`layer2-correlations.json`, `correlations-fdr-corrected.json`, `log-correlations.json`), the per-model strict-isolation table that is the v3 paper's headline analysis (`per-model-strict-isolation.json`), composite-outcome strict isolation (`layer2-strict-isolation.json`), the multicollinearity-cleaned logistic regression with bootstrap CIs (`layer2-logreg-v2.json`), Perplexity / Google-AIO citation lifts (`layer2-citation-correlation.json`), the source-URL category breakdown (`source-url-analysis.json`), Domain Authority quartile cross-reference (`layer2-cross-reference.json`), per-industry breakdown (`layer2-by-industry.json`), and bootstrap CIs on every headline number (`bootstrap-cis.json`).
