---
title: "An interoperable and reusable research environment for digital medicine"
authors: "Severin Kohler, Falk Meyer-Eschenbach, Leon Schüßler, Maximilian Meixner, Florian Kärcher"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-10-29T20:39:54.723648"
doi: "https://doi.org/10.3389/fdgth.2026.1943167"
openalex_id: "https://openalex.org/W7224097825"
source_api: "openalex"
---

# An interoperable and reusable research environment for digital medicine

**著者**: Severin Kohler, Falk Meyer-Eschenbach, Leon Schüßler, Maximilian Meixner, Florian Kärcher
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

Clinical research infrastructures remain fragmented and project-specific, with semantic inconsistency accumulating across studies and constantly increasing “interoperability debt”. Repeated transformations between heterogeneous standards cause semantic drift and information loss. Prospective studies require duplicate data entry across clinical and research systems, increasing workload and introducing inconsistencies. Project-driven data models accumulate technical debt that undermines the sustainability and maintainability of research infrastructure across studies and funding cycles. Here, we explore how a reusable research environment can be built, and whether governing data semantics at the persistence layer provides a foundation that outlasts individual projects. We present an environment addressing these deficiencies at the architectural level. An openEHR-based clinical data repository with governed archetypes serves as the canonical persistence layer, integrating retrospective EHR data, prospective study data, patient-reported outcomes, and wearable sensor streams under a shared semantic model. Prospective data is captured directly through openEHR-based forms, which removes the separate capture system for study variables, while duplicate documentation with a hospital information system that does not run on openEHR remains. Reusable transformation pipelines support bidirectional FHIR interoperability and OMOP-based analytics. Federation nodes at three institutions were tested with cohort count queries across sites and are not yet in routine use. Deployed at Charité university medical center across five studies covering approximately 16,000 patients and 7.9 million data points, the environment shows that one governed repository can be reused across successive studies from different clinical domains within an existing healthcare IT landscape. Of its 125 archetypes, 57 are shared between at least two studies. Sustainability beyond these five studies and scaling beyond one institution remain to be shown. All tooling is publicly available and provided as a deployable configuration for institutional adoption.
