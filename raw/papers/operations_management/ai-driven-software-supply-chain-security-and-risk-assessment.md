---
title: "AI-Driven Software Supply Chain Security and Risk Assessment"
authors: "Samuel Okechukwu Nnaji, Christian Basil Omeh, Christabel Linda Uchenwa"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-09-18T09:12:38.736024"
doi: "https://doi.org/10.62154/ajastr.2026.023.01019"
openalex_id: "https://openalex.org/W7212531907"
source_api: "openalex"
---

# AI-Driven Software Supply Chain Security and Risk Assessment

**著者**: Samuel Okechukwu Nnaji, Christian Basil Omeh, Christabel Linda Uchenwa
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

The growing complexity of software ecosystems has made the Software Supply Chain (SSC) a primary target for cyberattacks, as evidenced by SolarWinds, Log4Shell, and the XZ Utils backdoor. Traditional Software Composition Analysis (SCA) and static scanning tools are reactive and poorly suited to detecting novel or provenance-based threats in dependencies, build pipelines, and package registries. This study proposes and evaluates an Artificial Intelligence (AI)-driven framework for software supply chain security and risk assessment that integrates a Graph Neural Network (GNN) for dependency-graph risk propagation, a Transformer encoder for source-code anomaly detection, and a Long Short-Term Memory (LSTM) network for modelling temporal drift in build and release pipelines. Outputs from the three learners are combined through an ensemble fusion layer to generate an interpretable risk score for each component. The study adopted a design-science and quantitative approach. The framework was trained and evaluated on a curated dataset comprising 6.4 million GitHub commits, 5,000 registry packages, 38,600 CVE-to-package mappings, 2,313 synthetic Software Bills of Materials (SBOMs), and 312 malicious artefacts. Results show that the hybrid ensemble achieved 96.3% accuracy, 95.6% precision, 94.8% recall, an F1-score of 95.2%, and an AUC-ROC of 0.98, outperforming GNN, LSTM, Random Forest, SVM, and Logistic Regression baselines by 6–18 percentage points across metrics. Combining structural, semantic, and temporal signals improves detection of malicious and high-risk components over single-model approaches, while producing risk scores aligned with NIST SSDF and the EU Cyber Resilience Act. The paper concludes with recommendations for AI-driven risk scoring in DevSecOps and SBOM governance.
