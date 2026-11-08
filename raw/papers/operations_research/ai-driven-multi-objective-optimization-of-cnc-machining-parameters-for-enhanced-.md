---
title: "AI-driven multi-objective optimization of CNC machining parameters for enhanced surface finish and tool life"
authors: "Arvinder Singh Channi, Altaf Hanifbhai Nalbandh, Amol Raoji Madane, Vikas Gulati, Gadde Raghu Babu"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-09T06:52:24.512857"
doi: "https://doi.org/10.55670/fpll.futech.5.4.19"
openalex_id: "https://openalex.org/W7225467766"
source_api: "openalex"
---

# AI-driven multi-objective optimization of CNC machining parameters for enhanced surface finish and tool life

**著者**: Arvinder Singh Channi, Altaf Hanifbhai Nalbandh, Amol Raoji Madane, Vikas Gulati, Gadde Raghu Babu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

AI-driven CNC machining optimization requires balancing surface quality and productivity while avoiding unsupported integration of independently collected machining data. This study proposes a leakage-controlled, surrogate-assisted framework using two open datasets: a 27-condition turning surface-quality dataset and a 968-observation milling tool-life dataset comprising 14 tools. The datasets were analyzed independently, with no row-wise fusion or DOC–ADOC mapping. Cutting speed, feed rate, and depth of cut were used as controllable turning variables, while milling sensor and metadata features were used separately for remaining useful life (RUL) prediction. The selected Ridge surface model achieved LOOCV MAE = 0.1077, RMSE = 0.1383, and , while nested validation yielded , indicating limited out-of-sample generalization. The no-cycle RUL model achieved MAE = 23.44 cycles, RMSE = 31.39 cycles, and under leave-one-tool-out validation. NSGA-II significantly outperformed equal-budget random search in normalized hypervolume (0.7711 vs. 0.7421). Because the surrogate surface was statistically limited, continuous optimization was treated as exploratory. Final selection was therefore anchored to measured Pareto-efficient turning conditions. Equal-weight TOPSIS selected , , and , with measured and , as the balanced practical recommendation.
