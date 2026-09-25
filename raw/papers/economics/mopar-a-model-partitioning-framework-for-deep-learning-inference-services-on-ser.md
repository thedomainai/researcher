---
title: "MOPAR: A Model Partitioning Framework for Deep Learning Inference Services on Serverless Platforms"
authors: "Jiaang Duan, Shiyou Qian, Hanwen Hu, Jian Cao, Guangtao Xue"
year: 2026
citations: 2
paper_type: "primary"
domain: "economics"
fetched: "2026-09-14T06:02:50.742364"
doi: "https://doi.org/10.1145/3832810.3832925"
openalex_id: "https://openalex.org/W4393968378"
source_api: "openalex"
---

# MOPAR: A Model Partitioning Framework for Deep Learning Inference Services on Serverless Platforms

**著者**: Jiaang Duan, Shiyou Qian, Hanwen Hu, Jian Cao, Guangtao Xue
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: 経済学

## Abstract

With its elastic power and a pay-as-you-go cost model, the deployment of deep learning inference services (DLISs) on serverless platforms is emerging as a prevalent trend. However, the varying resource requirements of different layers in DL models hinder resource utilization and increase costs, when DLISs are deployed as a single function on serverless platforms. To tackle this problem, we propose a model partitioning framework called MOPAR. This work is based on the two resource usage patterns of DLISs: global differences and local similarity, due to the presence of resource dominant (RD) operators and layer stacking. Considering these patterns, MOPAR adopts a hybrid approach that initially divides the DL model vertically into multiple slices composed of similar layers to improve resource efficiency. Slices containing RD operators are further partitioned into multiple sub-slices, enabling parallel optimization to reduce inference latency. Moreover, MOPAR comprehensively employs data compression and share-memory techniques to offset the additional time introduced by communication between slices. We implement a prototype of MOPAR and evaluate its efficacy using four categories of 12 DL models on OpenFaaS and AWS Lambda. The experiment results show that MOPAR can improve the resource efficiency of DLISs by 27.62\% on average, while reducing latency by about 5.52\%. Furthermore, based on Lambda's pricing, the cost of running DLISs is reduced by about 2.58 $\times$ using MOPAR.
