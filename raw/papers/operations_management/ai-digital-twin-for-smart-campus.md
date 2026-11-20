---
title: "AI Digital Twin for Smart Campus"
authors: "Priti P. Tijare, Aparna Khairkar, Arjun R. More, Om R. Pimpre, Arpit S. Gawande"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-11-21T06:05:24.873472"
doi: "https://doi.org/10.22214/ijraset.2026.85481"
openalex_id: "https://openalex.org/W7225226219"
source_api: "openalex"
---

# AI Digital Twin for Smart Campus

**著者**: Priti P. Tijare, Aparna Khairkar, Arjun R. More, Om R. Pimpre, Arpit S. Gawande
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

Smart campuses generate massive heterogeneous data from IoT sensors, cameras, and administrative systems, yet existing infrastructures operate in silos, leading to fragmented visibility, reactive maintenance, and suboptimal resource utilization. This paper presents a unified AI Digital Twin framework that integrates real-time IoT telemetry, centralized data ingestion, predictive machine-learning analytics, and an interactive 3D digital twin interface to enable data-driven campus operations. The architecture comprises four layers: (1) edge sensor networks (DHT22, PIR, RFID, PZEM-004T, HC-SR04) collecting environmental, occupancy, electrical, and water-level data via MQTT/HTTP; (2) a FastAPI-backed central platform persisting telemetry in SQLite and synchronizing a room-level digital twin state; (3) AI/ML models (RandomForest regressor for occupancy forecasting, IsolationForest for anomaly detection, LogisticRegression for asset-failure probability) trained on historical observations; and (4) a web-based dashboard with Three.js 3D visualization, Chart.js KPIs, and an AI-assisted conversational interface. The system enforces data-quality guarantees: no synthetic feeds at staleness, explicit unavailability markers, and predictions always labeled as such. Deployed on a live testbed at PRMCEAM, the platform demonstrates real-time monitoring of 12 campus rooms, predictive maintenance alerts for electrical anomalies, 24-hour occupancy forecasts with mean absolute error below 3 persons, and resource optimization recommendations reducing estimated idle power consumption by 18%. Results confirm that a unified digital twin foundation enables scalable, intelligent campus management while maintaining transparency regarding data limits and prediction confidence.
