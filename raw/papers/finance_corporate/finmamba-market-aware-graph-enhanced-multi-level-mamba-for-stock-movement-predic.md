---
title: "FinMamba: Market-Aware Graph Enhanced Multi-Level Mamba for Stock Movement Prediction"
authors: "Yifan Hu, Peiyuan Liu, Yijie Li, Dawei Cheng, Naiqi Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "finance_corporate"
fetched: "2026-11-04T06:53:51.621411"
doi: "https://doi.org/10.1145/3799682.3840638"
openalex_id: "https://openalex.org/W4407359489"
source_api: "openalex"
---

# FinMamba: Market-Aware Graph Enhanced Multi-Level Mamba for Stock Movement Prediction

**著者**: Yifan Hu, Peiyuan Liu, Yijie Li, Dawei Cheng, Naiqi Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートファイナンス

## Abstract

Recently, combining stock features with inter-stock correlations has become a common and effective approach for stock movement prediction. However, financial data presents significant challenges due to its low signal-to-noise ratio and the dynamic complexity of the market, which give rise to two key limitations in existing methods. First, the relationships between stocks are highly influenced by multifaceted factors including macroeconomic market dynamics, and current models fail to adaptively capture these evolving interactions under specific market conditions. Second, for the accuracy and timeliness required by real-world trading, existing financial data mining methods struggle to extract beneficial pattern-oriented dependencies from long historical data while maintaining high efficiency and low memory consumption. To address the limitations, we propose FinMamba, a Mamba-GNN-based framework for market-aware and multi-level hybrid stock movement prediction. Specifically, we devise a dynamic graph to learn the changing representations of inter-stock relationships by integrating a pruning module that adapts to market trends. Afterward, with a selective mechanism, the multi-level Mamba discards irrelevant information and resets states to skillfully recall historical patterns across multiple time scales with linear time costs, which are then jointly optimized for reliable prediction. Extensive experiments on U.S. and Chinese stock markets demonstrate the effectiveness of our proposed FinMamba, achieving state-of-the-art prediction accuracy and trading profitability, while maintaining low computational complexity. The code is available at https://github.com/TROUBADOUR000/FinMamba.
