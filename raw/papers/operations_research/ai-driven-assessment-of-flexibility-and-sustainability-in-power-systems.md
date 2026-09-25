---
title: "AI-Driven Assessment of Flexibility and Sustainability in Power Systems"
authors: "Shuai Zhang, Cangbao Du"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-02T09:12:38.888838"
doi: "https://doi.org/10.3390/sym18091463"
openalex_id: "https://openalex.org/W7204799082"
source_api: "openalex"
---

# AI-Driven Assessment of Flexibility and Sustainability in Power Systems

**著者**: Shuai Zhang, Cangbao Du
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

New energy power systems with high penetration rates feature complex spatiotemporal coupling relationships among generation, transmission, load, and storage. The random fluctuations in wind and solar power output, combined with load uncertainty, exacerbate system operational risks. Traditional static modeling, single-metric evaluation, and centralized analysis methods struggle to adapt to the dynamic, highly uncertain, and multi-constrained operational scenarios of new power systems. To address this, this paper proposes an Artificial Intelligence-based Comprehensive Evaluation Method for Power System Flexibility and Sustainability (AI-FSEA) under privacy and security constraints. This method first establishes an intelligent fusion module for multi-source, heterogeneous power data, which accurately extracts the system’s multidimensional dynamic features through adaptive wavelet denoising and a temporal self-attention mechanism. Second, it establishes a five-objective coupled evaluation model that balances technical, economic, low-carbon, and reliability considerations, with regulation margin loss, response delay, operating costs, carbon emissions, and power supply instability rate as the core optimization objectives, thereby achieving multi-objective trade-off optimization within the system’s feasible domain; furthermore, a Hierarchical Deep Q-Network-Assisted Multi-Objective Evolutionary Algorithm (HDQN-MOEA) is designed, which leverages the value iteration, composite reward mechanism, and feedback clustering screening mechanism of the deep Q-network to enhance the model’s solution accuracy and convergence efficiency. Results from multiple sets of comparative experiments, ablation studies, and uncertainty generalization experiments conducted using the IEEE standard node system and real-world power grid data from East China indicate that, compared with mainstream optimization algorithms such as NSGA-III and TS-NSGA-II, the proposed HDQN-MOEA algorithm achieves an average improvement of 10.2% in the hypervolume metric and an average reduction of 35.6% in the span metric; the results of the ablation experiments confirm that the absence of the multi-source data fusion module, the hierarchical strategy module, or the feedback clustering screening module would result in a 15.3% and 12.1% decrease in the model’s hypervolume metric, respectively, as well as a slight deterioration in population diversity; under three types of highly uncertain operating conditions—random fluctuations in renewable energy, sudden load spikes, and extreme weather—the algorithm proposed in this paper consistently maintains stable optimization performance, meeting convergence accuracy requirements in as few as 5000 iterations. Without increasing the complexity of existing algorithms, it achieves the synergistic optimization of data privacy and security, evaluation accuracy, and operational efficiency. The proposed method can accurately quantify the dynamic flexibility and long-term sustainability of the new power system, providing reliable intelligent technical support for the planning and dispatch of the new power system, the optimal allocation of resources, and low-carbon, sustainable operation.
