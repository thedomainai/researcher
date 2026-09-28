---
title: "Extending SDN control for programmable data planes in advanced 6G network scenarios"
authors: "Manuel Álvarez-Campana Fernández-Corredor, Diego Rivera Pinto, Marta Blanco Caamaño, Jose Ignacio Moreno Novella, Silvia Mauleón Hortelano"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-09-26T06:05:10.217469"
doi: ""
openalex_id: "https://openalex.org/W7204678146"
source_api: "openalex"
---

# Extending SDN control for programmable data planes in advanced 6G network scenarios

**著者**: Manuel Álvarez-Campana Fernández-Corredor, Diego Rivera Pinto, Marta Blanco Caamaño, Jose Ignacio Moreno Novella, Silvia Mauleón Hortelano
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

Future 6G networks are expected to support highly heterogeneous and demanding services, requiring advanced levels of programmability, automation, and fine-grained control across both control and data planes. Software-Defined Networking (SDN), combined with programmable data planes based on the P4 language, enables flexible and adaptive network behavior that is difficult to achieve with fixed-function forwarding devices. This work presents developments carried out in the context of the DESIRE6G project, where P4-based forwarding infrastructures were extensively used to support advanced network scenarios characterized by stringent requirements in terms of latency, isolation, and reliability. The project considered the use of the ETSI TeraFlowSDN controller, an open-source platform backed by ETSI and under active development with progressively expanding functionalities, including the control of P4 devices through the standardized P4Runtime interface. However, the commercial switches used in the demonstrator infrastructure did not allow control through this interface, nor could such functionality be enabled through software upgrades. Instead, they exposed the BFRT interface of the Tofino architecture as the only available control mechanism, which enables access to hardware-specific functionalities not covered by P4Runtime. These constraints led to the development of a TeraFlowSDN extension integrating BFRT support. The developed extension maintains compatibility with standardized P4Runtime-based workflows and has been seamlessly integrated into the existing ETSI TeraFlowSDN architecture. It enables per-device selection between P4Runtime- and BFRT-based control backends under a unified operational framework. The solution was validated both in a virtualized Tofino-based environment and in a real DetNet transport network scenario, and is released as open-source software, enabling reuse in operational, experimental, and educational contexts.
