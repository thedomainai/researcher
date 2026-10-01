---
title: "Large Language Model-Based Bidding Behavior Agent and Market Sentiment Agent-Assisted Electricity Price Prediction"
authors: ["Xin Lu", "Jing Qiu", "Yi Kun Yang", "Chenxi Zhang", "Jiafeng Lin", "Sihai An"]
year: 2024
cited_by_count: 48
doi: "https://doi.org/10.1109/tempr.2024.3518624"
openalex_id: W4405440125
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Large Language Model-Based Bidding Behavior Agent and Market Sentiment Agent-Assisted Electricity Price Prediction

**Authors**: Xin Lu, Jing Qiu, Yi Kun Yang, Chenxi Zhang, Jiafeng Lin, Sihai An | **Year**: 2024 | **Cited by**: 48 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Day-ahead electricity price prediction is crucial for market participants to make optimal trading decisions. The implementation of the five-minute settlement (5MS) process in the Australian National Electricity Market (NEM) on October 1, 2021, reduced the settlement interval from 30 minutes to 5 minutes. This change has led to more frequent adjustments in pricing, allowing for a more accurate reflection of real-time supply and demand conditions. However, this increased frequency has significantly heightened the complexity of price fluctuations in the wholesale market. Consequently, conventional machine learning and deep learning methods struggle to provide accurate predictions at this higher resolution. Since electricity prices are fundamentally determined by the supply-demand balance and the bidding behaviors of market participants, this work introduces individual participant's bidding behaviors into the prediction model. We fine-tune a pre-trained Large Language Model (LLM) to create bidding behavior agents, which forecasts day-ahead bidding behaviors. Moreover, market sentiment plays a significant role in electricity price volatility, yet it remains challenging to quantify and assess its impact. To address this, we employ a pre-trained LLM to analyze online resources, incorporating market sentiment into the price prediction model. Additionally, to enhance the accuracy of spike predictions, we improve the conditional time series generative adversarial network (CTSGAN) model by utilizing a spike confusion matrix and further strengthen the model by integrating bidding behavior and market sentiment as inputs. Case studies demonstrate that the proposed model significantly improves both electricity price and spike prediction accuracy, offering a robust tool for market participants to navigate the complexities of the modern electricity market.
