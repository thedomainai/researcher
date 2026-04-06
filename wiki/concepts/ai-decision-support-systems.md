# AI意思決定支援システム

## 概要

AI意思決定支援システム（AI Decision Support Systems、AI-DSS）とは、人工知能技術を活用して、専門家や意思決定者が複雑な判断を行う際に補助・支援を行うシステムの総称である。特に医療分野においては、診断の精度向上・リスク早期検知・電子医療記録（EMR）の自動生成など、多岐にわたる用途で活用されている。

このようなシステムが重要視される背景には、医療資源の不均等な分配、専門人材の不足、そして医療従事者の意思決定における認知的負荷の増大といった課題がある。特に低・中所得国（LMIC）においては、AI-DSSが医療の格差を埋める手段として注目されており、予防可能なリスクを早期に検出することで患者の転帰改善に貢献することが期待されている。

---

## 詳細

### 1. 医療分野における応用

#### 母子保健への活用：Awaaz-e-Sehat

パキスタンの低資源環境における母子保健を対象として開発された **Awaaz-e-Sehat**（アワーズ・エ・セハト）は、音声入力によってEMRを自動生成し、臨床リスクアラートを発出するスマートフォンベースのAIシステムである。

本システムの主な技術的特徴は以下の通りである：

- **多言語音声認識（ASR）モデル**：ウルドゥー語に対応したファインチューニング済みモデルを採用し、識字率や技術的背景に関わらず医療従事者が自然な会話で入力できる。
- **大規模言語モデル（LLM）のプロンプトエンジニアリング**：構造化されたEMRの生成と重篤な母体健康リスクの自動フラグ立てを実現。
- **現場展開（In-situ Deployment）**：非営利病院において7か月間にわたる実地運用を実施し、システムの実用性・有効性を検証。

このシステムは、HCI（Human-Computer Interaction）の観点から設計されており、ユーザーの言語・文化的背景への適応が重視されている点が特徴的である。

#### 胎児リスク予測：AI-FRS

メキシコの臨床環境を対象とした **AI-FRS**（Artificial Intelligence–Fetal Risk Prediction System）は、胎児リスクを予測するためのアンサンブルベースのAI意思決定支援ツールである。

- 世界では毎年約200万件の死産が発生しており、その多くは医療アクセスの格差や医療資源の不足に起因する。
- AI-FRSは、リスクのある妊娠を動的に特定し、胎児転帰の改善を目的として設計されている。
- アンサンブル学習（複数のモデルを組み合わせた手法）を採用することで、単一モデルよりも高い予測精度と堅牢性を実現している。

### 2. 人間とAIの協働における課題

AI意思決定支援システムの有効性は、その技術的性能のみならず、人間がAIの提案をどのように受容・修正するかに大きく依存する。

**Anna‐Sophie Ulfertら（2026）** による研究では、「AIの提案に対して人間が調整を加える際に、その理由を言語化（説明）させることが意思決定パフォーマンスを向上させるか」という問いを実験的に検討している。この研究は、以下の問題意識を反映している：

- AIへの**過度な依存（オーバーリライアンス）**の防止
- 人間の批判的思考力の維持・促進
- 説明責任（Explainability）の観点からの人間とAIの適切な役割分担

この分野の知見は、AI-DSSの設計において「AIが答えを出すだけでなく、ユーザーの思考を支援する仕組み」を組み込む重要性を示唆している。

### 3. 低資源環境への対応

AI-DSSの設計において、展開対象となる環境の制約を考慮することは不可欠である。低資源環境特有の課題には以下が含まれる：

| 課題 | 対応アプローチ |
|------|--------------|
| 識字率・技術リテラシーの低さ | 音声インターフェースの採用 |
| 言語の多様性 | 多言語・現地語対応モデルの開発 |
| 専門医の不足 | AIによるリスク自動検知・アラート機能 |
| インフラの貧弱さ | スマートフォンベースの軽量実装 |

### 4. 技術的構成要素

現代のAI意思決定支援システムは、以下のような技術要素を組み合わせて構成されることが多い：

- **機械学習・アンサンブル学習**：複数のモデルを統合し予測精度を高める（例：AI-FRS）
- **大規模言語モデル（LLM）**：自然言語による入出力と構造化データ生成
- **自動音声認識（ASR）**：音声入力のテキスト変換
- **プロンプトエンジニアリング**：LLMの出力を特定タスク向けに最適化する技術

---

## 関連概念

- [[電子医療記録 (Electronic Medical Records)]]
- [[大規模言語モデル (Large Language Models)]]
- [[自動音声認識 (Automatic Speech Recognition)]]
- [[アンサンブル学習 (Ensemble Learning)]]
- [[説明可能なAI (Explainable AI)]]
- [[Human-Computer Interaction (HCI)]]
- [[母子保健 (Maternal Healthcare)]]
- [[医療AIの公平性 (Fairness in Medical AI)]]
- [[プロンプトエンジニアリング (Prompt Engineering)]]
- [[臨床リスク予測 (Clinical Risk Prediction)]]

---

## 参考ソース

1. **Awaaz-e-Sehat: A Mobile Voice-based AI System for EMR Generation and Clinical Decision Support in Low-resource Maternal Healthcare**
   Maryam Mustafa et al. (2026) — DOI: https://doi.org/10.1145/3790115

2. **AI-FRS: An Ensemble-Based AI Decision-Support System for Fetal Risk Prediction in a Mexican Clinical Setting**
   Abimael Guzmán-Pando et al. (2026) — DOI: https://doi.org/10.3390/ai7040129

3. **Does Prompting Human Explanations for Adjustments to AI Decision-Support System Advice Improve Performance?**
   Anna‐Sophie Ulfert et al. (2026) — OpenAlex: https://openalex.org/W7135002821