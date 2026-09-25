---
title: "Replication Package of "Integrating Human Knowledge Through Action Masking in Reinforcement Learning for Operations Research""
authors: "Bernhard Lutz"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-04T09:25:22.949615"
doi: "https://doi.org/10.6084/m9.figshare.33098051"
openalex_id: "https://openalex.org/W7206212598"
source_api: "openalex"
---

# Replication Package of "Integrating Human Knowledge Through Action Masking in Reinforcement Learning for Operations Research"

**著者**: Bernhard Lutz
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

This repository contains the code and problem instances of our paper "Integrating Human Knowledge Through Action Masking in Reinforcement Learning for Operations Research".The code and instances of each problem are provided in a separate folder. The code of the stochastic problems uses random seeds to deterministically reproduce the results provided in the paper.paint_shop_problem/ contains the code and instances of the deterministic paint shop problem. Please unzip the zip-file paint_shop_data.zip to a folder "Data/"load_management_problem/ contains the code the stochastic load management problem.inventory_problem contains the code of the stochastic inventory management problem.Each folder contains a Run.bat file, which starts several processes to distribute the effort for policy learning. Trained reinforcement learning policies and logfiles of mean reward over time will be stored in the folders "Models/" and "Logs/". These folders are created automatically by the scripts. The main scripts are "Run_Experiments.py", which also accept several command line parameters. The Run_Experiments.py scripts (when called by Run.bat) generate multiple output csv-files, which you then have to merge before aggregating the final results.In addition, each folder contains a script AnalyzeResults.py, which reproduces all aggregated results and the statistical test results. In the paint shop problem, aggregated results are directly provided as csv files.The package was tested under Python 3.14.6 and the following packages:gymnasium 1.3.0stable-baselines3 2.9.0torch 2.13.0numpy 2.5.0pandas 3.0.3The hyperparameters are generally set to the default values of stable-baselines3 (except timesteps, entropy coefficient, and target KL divergence). Please see the supplementary materials for the full list of PPO hyperparameters.
