---
title: "AI-Based Fault Diagnosis for Subsurface Rod Pumps in India's Largest Onshore Field: An Alternative to Manual Card Interpretation"
authors: "K. Chanchlani, M. Shah"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-09-30T06:01:36.723701"
doi: "https://doi.org/10.2118/232303-ms"
openalex_id: "https://openalex.org/W7214643965"
source_api: "openalex"
---

# AI-Based Fault Diagnosis for Subsurface Rod Pumps in India's Largest Onshore Field: An Alternative to Manual Card Interpretation

**著者**: K. Chanchlani, M. Shah
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Abstract Subsurface rod pumps are vital to artificial lift operations in mature oilfields, yet they frequently encounter mechanical and operational faults such as incomplete fillage, gas interference, fluid pounding, rod parting, and hitting down. Traditional diagnostic practices rely on manual interpretation of dynamometer cards, which is subjective and time-consuming. The workflow begins with acquisition of polished rod load-displacement signals, which are transformed into surface dynamometer cards. From these raw signals, tabular features are engineered to capture geometric and statistical descriptors, including card area, maximum and minimum load, stroke length, slope variations, and Fourier transform coefficients. These features provide a compact yet informative representation of pump behavior. Supervised learning models such as Random Forests, Support Vector Machines, and Gradient Boosting were trained on the feature set. Feature importance analysis revealed that geometric descriptors such as card asymmetry, reversal point slopes, and stroke length variations were most influential in detecting incomplete fillage, while frequency-domain features proved critical for diagnosing gas interference. This interpretability bridges automated analytics with actionable decision-making for field engineers. To address class imbalance, particularly for rare events such as rod parting and hitting down, SMOTE was applied to augment minority samples. Despite their sparse representation, the model successfully identified these classes, ensuring that critical anomalies were not overlooked. Cross-validation confirmed robustness, while hyperparameter tuning optimized predictive accuracy. The multiclass classification model achieved an overall accuracy of 97%, with precision and recall values of 0.97 and an average F1-score of 0.97. Field deployment validated scalability, demonstrating the framework's potential to guide remedial actions. The results highlight the system's ability not only to automate diagnostics but also to enhance transparency and support proactive maintenance strategies. This study introduces a reproducible ML pipeline for subsurface rod pump fault identification that combines tabular feature engineering with multiclass pattern classification. Unlike traditional approaches, the framework not only automates diagnosis but also highlights diagnostic markers that enhance interpretability and demonstrating the feasibility of integrating AI into artificial lift diagnostics. The novelty lies in bridging conventional dynamometer card interpretation with modern data-driven methods, offering efficiency, transparency, and scalability.
