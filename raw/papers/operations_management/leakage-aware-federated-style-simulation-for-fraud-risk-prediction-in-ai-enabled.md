---
title: "Leakage-aware federated-style simulation for fraud risk prediction in AI-enabled FinTech platforms"
authors: "Jyoti Agarwal, Moin Uddin"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-11-09T06:51:51.703210"
doi: "https://doi.org/10.55670/fpll.futech.5.4.9"
openalex_id: "https://openalex.org/W7225457753"
source_api: "openalex"
---

# Leakage-aware federated-style simulation for fraud risk prediction in AI-enabled FinTech platforms

**著者**: Jyoti Agarwal, Moin Uddin
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

AI-enabled FinTech platforms increasingly rely on automated fraud-risk prediction to secure high-volume digital payments, mobile-money transactions, and real-time financial services. However, fraud detection remains difficult because fraudulent transactions are rare, financial data are sensitive, and centralized machine-learning models may create privacy and data-governance risks. This study evaluates a leakage-aware and imbalance-aware federated-style simulation for fraud-risk prediction in AI-enabled FinTech platforms. The study does not implement FedAvg, cryptographic secure aggregation, differential privacy, or model-parameter exchange. Instead, the PaySim Synthetic Financial Dataset was partitioned into five simulated FinTech clients, local models were trained separately, and prediction-level aggregation was used to compare centralized and simulated decentralized learning settings. The experimental workflow included data-quality assessment, leakage-aware feature selection, feature engineering, class-imbalance analysis, centralized model development, threshold optimization, and federated-style model comparison. The results show that fraud cases represented only 0.0466% of all transactions and occurred only in CASH_OUT and TRANSFER operations. The best-balanced centralized model was the Improved Random Forest at a threshold of 0.33, achieving an F1-score of 0.3019. Federated Ensemble Aggregation achieved the highest PR-AUC of 0.2699 and a precision of 1.0000, but its recall remained low at 0.1429. The centralized Improved Random Forest retained the highest F1-score of 0.3019, indicating a stronger overall precision-recall balance. Global feature-importance analysis showed that transaction amount, log-transformed amount, temporal features, transaction type, and destination-account activity were the main fraud-risk indicators. These findings should be interpreted as evidence from simulated decentralized fraud-risk learning rather than a full secure federated learning implementation.
