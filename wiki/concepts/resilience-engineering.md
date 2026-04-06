# レジリエンスエンジニアリング（Resilience Engineering）

## 概要

レジリエンスエンジニアリングは、複雑な社会技術システムにおける安全性を「失敗の排除」ではなく「変動する条件下での適応能力」として捉え直すアプローチである。Hollnagel、Woods、Levesonらが中心的な貢献者。

従来の安全工学が「何が間違ったか」（Safety-I）に焦点を当てるのに対し、レジリエンスエンジニアリングは「何がうまくいっているか」（Safety-II）に注目する。

## 4つの能力

レジリエントなシステムには以下の4つの能力が必要とされる：

- **応答（Responding）**: 現在の脅威や変動に対処する能力
- **監視（Monitoring）**: 環境の変化や潜在的脅威を検知する能力
- **学習（Learning）**: 過去の経験から教訓を抽出する能力
- **予見（Anticipating）**: 将来の脅威や機会を予測する能力

## AI Nativeな設計への示唆

### Tier 1（不変原理）としての位置づけ

レジリエンスの4能力は、対象がAIシステムであっても成立する不変原理である。

**AIエージェントの障害モード**: 複数のAIエージェントが連携するシステムでは、単一のエージェントの誤動作がカスケード的に波及する。航空業界やプロセス産業の知見が直接転用可能。

**適応的キャパシティ**: AIシステムは高い処理能力を持つが、「設計時に想定されていなかった状況への適応」は依然として困難。レジリエンスエンジニアリングの知見は、AIシステムの適応能力をどう設計するかの指針を提供する。

**Safety-II的アプローチ**: AI nativeなシステムの安全性は、「AIがエラーを起こさない」ことを目指すのではなく、「AIがエラーを起こしても全体として機能し続ける」設計を目指すべき。

### 化学プロセス産業からの知見

Natech（自然災害に起因する技術的事故）に関するレジリエンスエンジニアリングのシステマティックレビューは、以下を示している：
- 複合的な障害シナリオの設計時想定が不十分
- 組織間連携の脆弱性が主要なリスク因子
- レジリエンスの指標化と安全管理への統合が進行中

これらの知見は、AIエージェント間の連携障害設計に直接応用可能。

## Ashbyの必要多様性の法則との接続

制御系（安全管理システム）は、被制御系（複雑な運用環境）と同等以上の多様性を持たなければならない。AIが運用環境の複雑性を増大させるならば、安全管理システムもそれに応じた多様性の増大が必要。

## 関連概念

- [[coding-agents]] — エージェントのエラー処理とリカバリ設計
- [[reward-hacking]] — 安全性指標のGoodhart's Law的な劣化
- [[human-ai-collaboration]] — 人間-AIシステムにおける安全性の分担

## 参考ソース

- "A systematic review of Resilience Engineering applications to Natech accidents" — `raw/papers/systems_engineering/`
- "Resilience Engineering Indicators and Safety Management: A Systematic Review" — `raw/papers/systems_engineering/`
- "Systematic Review of Resilience Engineering and Operational Risk Management in Telecom Networks" — `raw/papers/systems_engineering/`
