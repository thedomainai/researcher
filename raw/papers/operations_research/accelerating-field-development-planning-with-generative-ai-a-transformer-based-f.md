---
title: "Accelerating Field Development Planning with Generative AI: A Transformer-Based Framework"
authors: "M. A. Al-Ismael, A. A. Awotunde"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-10-15T08:05:58.448677"
doi: "https://doi.org/10.2118/234057-ms"
openalex_id: "https://openalex.org/W7221601816"
source_api: "openalex"
---

# Accelerating Field Development Planning with Generative AI: A Transformer-Based Framework

**著者**: M. A. Al-Ismael, A. A. Awotunde
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Abstract Field development planning for oil and gas reservoirs is becoming increasingly complex, making traditional simulation-based optimization prohibitively costly in time and compute. This research explores a generative AI transformer that directly predicts optimal well locations, aiming to maximize net present value (NPV) while reducing planning time by orders of magnitude. A custom transformer was built to ingest reservoir fields (pressure, porosity, permeability, fluid saturations) together with wellbore production and injection rates. Raw voxel data are first projected into dense embeddings, then passed through stacked multi-head self-attention blocks that encode both spatial and temporal dependencies via sinusoidal positional encodings. To keep memory footprints tractable for full-field models, we partition the volume into overlapping chunks before feeding them to the network. The model was developed using 200 Brugge simulation scenarios using a mean squared error loss on well locations and well production/injection rates, with model parameters optimized using the Adam optimizer. The transformer architecture successfully accommodated scenarios with varying numbers of wells and achieved stable training convergence after 100 epochs. We used the trained transformer to optimize well placement in different scenarios from the test dataset, achieving instantaneous inference times and acceptable accuracy. The NPV obtained from the transformer-inferred wells achieved 87% of that obtained from traditional simulation-based stochastic optimization, which is a significant improvement considering the substantial reduction in computational time and cost. Additionally, comparison with several AI-based surrogate-assisted optimization workflows demonstrated that the generative framework achieved higher economic performance while eliminating the iterative optimization process. These results demonstrate that a transformer-based generative model can deliver near-optimal well placement with negligible computational cost, opening the door to rapid and iterative field development studies. This work applies a full-field transformer to generative well placement, learning high-dimensional spatial and temporal reservoir relationships directly from data. The model delivers instantaneous, optimization-free predictions, enabling rapid scenario screening and substantially accelerating field development decision cycles.
