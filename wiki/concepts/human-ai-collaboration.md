# 人間-AI協働（Human-AI Collaboration）

## 概要

人間-AI協働は、AIを単なるツールとしてではなく、協働する知的パートナーとして位置づけるアプローチである。BCG/Harvardの研究ではCentaurモデル（人間とAIが明確に分業）とCyborgモデル（人間とAIが融合的に協働）が区別されている。

## 実証的知見

### 生産性への影響

複数のRCTおよび準実験的研究が蓄積されている：

- **開発者生産性**: 2025年初頭のAIツール導入に関する測定では、経験豊富なオープンソース開発者における生産性への影響が報告されている（被引用84）
- **企業環境でのRCT**: AI導入が開発スピードに与える影響のランダム化比較試験（被引用14）
- **系統的レビュー**: 人間-AI協働のトレンドに関する体系的レビューが複数存在

### 一貫した知見

レビュー論文群から浮かび上がるパターン：
- AIの効果は**タスクの性質に強く依存**する（ルーチン的タスクで大きな効果、複雑な判断で限定的効果）
- 専門家と非専門家で効果の方向が異なる場合がある（AIは能力の低い人により大きな恩恵を与える傾向）
- 信頼のキャリブレーション（AIをいつ信頼し、いつ疑うか）が協働の質を決定する

## AI Nativeな設計への示唆

### 「AI-enabled」vs.「AI-native」の分水嶺

現在の実証研究の多くは、既存のワークフローにAIを「追加」した場合の効果を測定している（AI-enabled）。AI nativeな設計とは、AIの存在を前提にワークフロー自体を再設計すること。

既存研究からの示唆：
- **スキルの非対称性**: AIが非専門家のスキルを底上げするなら、AI nativeな組織では「専門性の定義」自体が変わる
- **タスク分解の粒度**: AIとの協働が効果的なタスクの粒度がある。粒度設計が協働の質を規定する
- **フィードバックループ**: AIの提案→人間の判断→結果の観察→AIの改善、というループの設計

### IT支援サービスにおける知見

IT支援における人間-AI協働のシステマティックレビューは、ユーザーエクスペリエンスとワークフロー自動化の統合が鍵であることを示している。これはより広い文脈（組織の意思決定、顧客対応、ナレッジワーク全般）にも一般化可能。

## 関連概念

- [[self-determination-theory]] — 協働設計における人間の主体性確保
- cognitive-load — 協働のインターフェース設計における認知的負荷管理
- mixed-initiative — 主導権の動的交代のデザインパターン
- [[coding-agents]] — ソフトウェア開発における人間-AI協働の最前線

## 参考ソース

- "A Systematic Review of Trends in Human–AI Collaboration Research" (cited: 4) — `raw/papers/human_ai_collaboration/`
- "A Systematic Review of Human-AI Collaboration in IT Support Services" (cited: 1) — `raw/papers/human_ai_collaboration/`
- "How Much Does AI Impact Development Speed? An Enterprise-Based RCT" (cited: 14) — `raw/papers/human_ai_collaboration/`
- "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (cited: 84) — `raw/papers/human_ai_collaboration/`
