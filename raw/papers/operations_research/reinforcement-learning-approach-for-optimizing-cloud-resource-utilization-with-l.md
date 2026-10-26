---
title: "Reinforcement Learning Approach for Optimizing Cloud Resource Utilization with Load Balancing"
authors: "Miss. P. V. Kapse Miss. Sonawane Rutuja Sitaram, Prof. J. R. Mahajan"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-10-27T06:06:05.884392"
doi: "https://doi.org/10.48175/ijarsct-40157"
openalex_id: "https://openalex.org/W7223573183"
source_api: "openalex"
---

# Reinforcement Learning Approach for Optimizing Cloud Resource Utilization with Load Balancing

**著者**: Miss. P. V. Kapse Miss. Sonawane Rutuja Sitaram, Prof. J. R. Mahajan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Cloud computing provides flexible access to processing, storage, and networking resources, but efficient use of these resources remains a difficult management problem. Workloads vary in size, arrival rate, execution time, and resource demand, while virtual machines and containers may differ in capacity and current utilization. A static scheduler can perform well under one workload and poorly when the workload changes. This paper presents a reinforcement learning (RL)-based framework for cloud task scheduling and load balancing. The proposed controller observes system conditions, selects a suitable placement or scheduling action, and receives feedback based on execution delay, resource utilization, queue length, migration cost, and service-level constraints. The design uses a Markov decision process to describe the scheduling problem and considers Q-learning or a deep Q-network as possible policy-learning methods. A practical evaluation plan is defined using repeatable workload traces and baseline schedulers such as First Come First Served, Round Robin, Min-Min, Max-Min, and Minimum Completion Time. The paper specifies metrics, experimental controls, and implementation considerations so that the framework can be evaluated without claiming results that have not yet been measured. The main contribution is a structured, reproducible design for learning-based load balancing that accounts for both performance and operational overhead.
