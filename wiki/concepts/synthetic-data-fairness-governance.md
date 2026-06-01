# 合成データの公平性とガバナンス

**合成データの公平性とガバナンス（Synthetic Data Fairness and Governance）**は、プライバシーを保護しつつデータを共有・活用する有力な手段である「合成データ（Synthetic Data）」において、そのデータが内包する偏り（バイアス）を評価・是正し、EU AI法（EU AI Act）などの法規制に準拠した運用を行うための学術的・実務的な枠組みです。

近年、AIモデルのトレーニングに合成データを利用する動きが活発化していますが、生成元の実データ（リアルデータ）に含まれる差別や偏見が合成データへと継承・増幅されるリスクが指摘されています。そのため、法的な要求事項を満たしつつ、技術的に公平性を評価・ガバナンス（管理・統制）する手法の確立が強く求められています。

---

## 詳細セクション

Nicki Lena Kämpf氏らによる研究（2026年）は、欧州連合（EU）のAI法を背景に、合成データの公平性評価における「法規制」と「技術的評価」のギャップを分析し、情報システム（IS）の視点から以下の知見を提示しています。

### 1. 公平性評価における2つの技術的潮流
学術文献の系統的レビュー（Systematic Literature Review）により、合成データの公平性を評価する最先端の指標（メトリクス）は、大きく以下の2つのアプローチに分類されることが明らかになりました。

*   **バイアス指向の評価（Bias-oriented Evaluation）:**
    データセット内に存在する、特定の保護対象属性（性別、人種、年齢など）に対する差別的な歪みや偏りを検出し、是正することを目指すアプローチ。
*   **多様性指向の評価（Diversity-oriented Evaluation）:**
    データセット全体が、対象となる母集団の多様性を十分に、かつ過不足なく反映しているかを評価するアプローチ。

### 2. 現在のガバナンスにおける3つの課題
法的な適合性と技術的な評価手法を統合する過程において、以下の3つの相互に関連する問題領域（Problem Fields）が浮き彫りになっています。

1.  **運用化と自動化の欠如（Lack of Operationalization and Automation）:**
    公平性の指標を実際のシステム開発プロセスやデータパイプラインへ具体的に落とし込み、自動的に評価する仕組みが十分に確立されていません。
2.  **ガバナンスメカニズムの欠如（Lack of Governance Mechanisms）:**
    組織内で合成データの生成、評価、監査を体系的に管理・統制するためのプロセスや責任の所在（ガバナンス構造）が不足しています。
3.  **公平性の義務に関する法的な不確実性（Legal Unclarity Concerning Fairness Obligations）:**
    EU AI法のもとで、合成データプロバイダーや利用者が具体的にどのような公平性の担保義務を負うのかについて、法的な解釈や基準が未だ不透明な状態にあります。

---

## 関連概念

*   [[合成データ]] (Synthetic Data)
*   [[AIガバナンス]] (AI Governance)
*   [[EU AI法]] (EU Artificial Intelligence Act)
*   [[信頼できるAI]] (Trustworthy AI)
*   [[プライバシー保護技術]] (Privacy-Preserving Technologies)

---

## 参考ソース

*   **タイトル**: Between Regulation And Evaluation: An Information Systems Perspective On Fairness For Synthetic Data In The Eu (2026)
*   **ファイルパス**: `raw/Between_Regulation_And_Evaluation_An_Information_Systems_Perspective_On_Fairness_For_Synthetic_Data_In_The_Eu.md`