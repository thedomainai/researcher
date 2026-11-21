---
title: "Optimizing Resource Allocation in Cloud Computing Environments using Reinforcement Learning"
authors: "MSR Prasad"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-22T06:05:46.224193"
doi: "https://doi.org/10.21590/ijtmh.11.04.26"
openalex_id: "https://openalex.org/W7214222142"
source_api: "openalex"
---

# Optimizing Resource Allocation in Cloud Computing Environments using Reinforcement Learning

**著者**: MSR Prasad
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Cloud computing resource allocation remains a critical challenge, with organizations wasting an estimated $109 billion annually on idle or over-provisioned resources. Traditional allocation strategies—static provisioning, threshold-based autoscaling, and time-series forecasting—fail to capture the complex, non-stationary dynamics of modern cloud workloads characterized by bursty arrivals, heterogeneous resource demands, and multi-tenant interference effects. This paper presents CloudRL, a deep reinforcement learning framework for intelligent cloud resource allocation that jointly optimizes resource utilization, Service Level Agreement (SLA) compliance, infrastructure cost, and energy efficiency. CloudRL formulates resource allocation as a continuous-action Markov Decision Process (MDP) and employs a Soft Actor-Critic (SAC) agent with a multi-objective reward function that balances competing optimization goals through adaptive weighting. The system observes a high-dimensional state space comprising real-time CPU, memory, GPU, storage I/O, and network utilization metrics alongside workload arrival patterns and SLA parameters, and outputs fine-grained scaling, migration, and configuration actions. We evaluate CloudRL on a production-scale testbed comprising 500 virtual machines processing six diverse workload traces (web serving, batch analytics, machine learning training, video transcoding, database, and microservices) over 30 days. Results demonstrate that CloudRL achieves 88% average resource utilization (compared to 42% for static allocation and 65% for predictive methods), reduces SLA violations by 91.7% (from 12% to 0.98%), decreases infrastructure costs by 37.5%, and lowers energy consumption by 59% compared to static provisioning. CloudRL converges within 3,000 training episodes and adapts to workload distribution shifts within 200 episodes without manual retuning.
