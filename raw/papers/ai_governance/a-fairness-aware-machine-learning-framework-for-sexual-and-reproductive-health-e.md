---
title: "A Fairness-Aware Machine Learning Framework for Sexual and Reproductive Health: Evaluating Algorithmic Bias Across Models"
authors: "Efosa Osagie, Shemi Ayo-Ogbor, Dr.Rebecca Balasundaram"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-05-09T06:04:29.234572"
doi: "https://doi.org/10.47852/bonviewjdsis62027678"
openalex_id: "https://openalex.org/W7160549935"
source_api: "openalex"
---

# A Fairness-Aware Machine Learning Framework for Sexual and Reproductive Health: Evaluating Algorithmic Bias Across Models

**著者**: Efosa Osagie, Shemi Ayo-Ogbor, Dr.Rebecca Balasundaram
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Advances in computational infrastructure and the widespread adoption of electronic health record (EHR) systems have accelerated the integration of artificial intelligence (AI) and machine learning (ML) into sexual and reproductive health (SRH) services. These technologies enhance diagnostic accuracy, support clinical decision-making, and enable predictive analytics using diverse healthcare data. However, biases within training datasets can produce unfair outcomes, particularly for underrepresented groups. This study proposes a fairness-aware ML framework designed to detect and mitigate algorithmic bias in SRH services. The framework is evaluated using two open-source datasets: a large SRH dataset from England (2014–2015) containing 2,126,413 records and the PCOS dataset covering the top 75 countries, enabling assessment of generalizability and intersectional fairness. It integrates pre-processing, in-processing, and post-processing techniques, including model-specific and group-specific thresholding. Results show that on the SRH England dataset, logistic regression (LR) achieved near-optimal parity fairness with minimal performance loss, improving disparate impact from 0.99 to 1.00 while maintaining 0.66 accuracy. Random Forest (RF) and Gradient Boosting (GB) exhibited larger fairness shifts, with disparate impact decreasing from 0.94 to 0.66 (RF) and 0.93 to 0.77 (GB), though accuracy remained stable. On the PCOS dataset, LR reduced bias with only a 1.96% accuracy drop, while GB improved performance but saw fairness decline, with disparate impact falling from 1.08 to 0.57. RF improved fairness but experienced a 28% accuracy reduction. Overall, the findings show that fairness-aware ML can substantially reduce bias, though equity–performance trade-offs vary across models and datasets. Received: 16 September 2025 | Revised: 21 January 2026 | Accepted: 31 March 2026 Conflicts of Interest The authors declare that they have no conflicts of interest to this work. Data Availability Statement The PCOS dataset that support the findings of this study is openly available on Kaggle at https://www.kaggle.com/datasets/ankushpanday1/pcos-prediction-datasettop-75-countries. The NHS Sexual and Reproductive Health (SRH) Services England 2014–15 dataset that support the findings of this study is openly available through NHS Digital at https://digital.nhs. uk/data-and-information/publications/statistical/sexual-and-reproductive-health-services/sexual-and-reproductive-health-servicesengland-2014-15. Author Contribution Statement Efosa Osagie: Conceptualization, Methodology, Validation, Formal analysis, Investigation, Writing – original draft, Writing – review &amp; editing, Visualization, Supervision, Project administration. Shemi Ayo-Ogbor: Investigation, Writing – original draft. Rebecca Balasundaram: Investigation, Writing – original draft.
