---
title: "One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation"
authors: "Ryuki Unno, Keigo Sakurai, Koshi Watanabe, Keisuke Maeda, Takahiro Ogawa"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-11-15T06:21:06.606717"
doi: "https://doi.org/10.1145/3858063.3858783"
openalex_id: "https://openalex.org/W7225321415"
source_api: "openalex"
---

# One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation

**著者**: Ryuki Unno, Keigo Sakurai, Koshi Watanabe, Keisuke Maeda, Takahiro Ogawa
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Financial asset recommendation for retail investors is typically optimized for relevance, that is, how well a recommendation matches what each user will buy. From the service provider's point of view, the value of a recommendation also depends on portfolio performance: the risk-adjusted return the recommended assets (the basket) deliver, which drives user engagement and fee revenue. The two goals are rarely achieved jointly, because the recommendations that best match user behavior concentrate on a few popular assets whose returns are highly correlated, which caps the risk-adjusted return a provider can offer. We propose Decorrelated-Satellite Expert Re-ranking (\textbf{DSER}), which retains the most relevant recommendations from an expert-following list and replaces the rest with return-decorrelated alternatives. The number of replaced slots is a single integer~$m$ (a knob) that the provider sets, so the relevance--performance trade-off becomes an explicit, auditable choice rather than a property hidden inside a learned model. In experiments on the public FAR-Trans retail-brokerage dataset, under the primary protocol, replacing a few slots improves risk-adjusted return at a small relevance cost, and the gain survives realistic trading costs at typical retail portfolio sizes. Minimizing correlation would lower basket volatility, but in our data the least-correlated assets are more volatile and higher-return, so their volatility offsets that reduction while their return drives the gain, not lower volatility. The resulting trade-off is asymmetric, with the relevance cost consistent across market phases while the gain is phase-dependent. The provider sets $m$ to read off exactly how much relevance each operating point costs.
