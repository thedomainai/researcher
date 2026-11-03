---
title: "DefaultGNN: A Dual-Perspective GNN Framework for Predicting Corporate Default from Buyer-Seller Transaction Networks"
authors: "Junghoon Kim, Hyunsung Kim, Seungyoon Choi, KyoungYong Park, Jihun Lee"
year: 2026
citations: 0
paper_type: "primary"
domain: "finance_corporate"
fetched: "2026-11-04T06:53:57.009913"
doi: "https://doi.org/10.1145/3799682.3840153"
openalex_id: "https://openalex.org/W7214116986"
source_api: "openalex"
---

# DefaultGNN: A Dual-Perspective GNN Framework for Predicting Corporate Default from Buyer-Seller Transaction Networks

**著者**: Junghoon Kim, Hyunsung Kim, Seungyoon Choi, KyoungYong Park, Jihun Lee
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートファイナンス

## Abstract

Corporate default prediction is a core problem in financial risk management, yet traditional credit models rely heavily on financial statements that are often sparse or unavailable for many firms. Corporate transaction networks offer a complementary view of real economic activity, but how risk propagates through buyer-seller relationships remains underexplored. We conduct a large-scale empirical study using real-world electronic tax-invoice data spanning six years that links transaction histories with default events, revealing that transaction-driven risk is both role-dependent (buyer or seller) and scale-dependent. Based on these findings, we construct multiplex buyer-view and seller-view transaction networks and propose DefaultGNN, a dual-perspective graph neural network-based framework for corporate default prediction. DefaultGNN integrates both views to model how risk flows through transactional relationships, achieving strong improvements over both attribute-based and graph-based baselines, especially for firms with limited intrinsic risk signals. We further provide interpretable network-based explanations by visualizing how distressed trading partners contribute to default risk. In collaboration with a licensed credit rating agency, we validate that DefaultGNN's predictions complement existing credit scoring models, improving approval rates by 7-11%p without increasing default risk among approved firms. The source code can be found at https://github.com/jhkim611/DefaultGNN
