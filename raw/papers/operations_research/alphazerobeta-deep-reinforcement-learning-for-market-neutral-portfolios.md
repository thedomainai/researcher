---
title: "AlphaZeroBeta: deep reinforcement learning for market-neutral portfolios"
authors: "Boris Belyakov"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-22T09:24:06.197599"
doi: "https://doi.org/10.1186/s40854-026-00955-4"
openalex_id: "https://openalex.org/W7170084705"
source_api: "openalex"
---

# AlphaZeroBeta: deep reinforcement learning for market-neutral portfolios

**著者**: Boris Belyakov
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Abstract Market-neutral portfolios aim to generate consistent returns while offsetting systematic market risk. Traditional approaches based on factor models or convex optimization often underperform during market regime shifts or when structural assumptions break down. We propose AlphaZeroBeta, a deep reinforcement learning framework designed to deliver benchmark-relative alpha (excess returns) with near-zero beta (market neutrality). AlphaZeroBeta combines a composite reward function that balances risk-adjusted excess return, benchmark correlation, and transaction costs, with a CNN-GRU policy trained end-to-end via Recurrent PPO and evaluated through a rolling walk-forward protocol. Backtests covering 2014–2024 across seven equity indices show that the model achieves higher Sharpe ratios than the baselines while maintaining near-zero benchmark correlations and competitive drawdowns.
