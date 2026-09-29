# 並列独立層による権限の有界化

## 概要

並列独立層による権限の有界化(Authority Bounding by Parallel Independent Layers)とは、AIシステムの**能力そのもの**ではなく、それが**行使できる権限**を、技術・組織・人的といった複数の独立した層で並列に制限する構造原理である。責任を事後の監視や倫理審査に委ねず、設計段階に埋め込む点に特徴がある。

AI Nativeな社会では、エージェント型AIが実行主体として業務や意思決定に深く組み込まれる。能力は継続的に向上し、事前に上限を見積もることが難しい。そのため、「モデルが十分安全かどうか」を単一の判断軸にするのは脆い。この原理は、安全性の中心変数を「能力」から「結果を生みうる権限」へ移し、権限の設計を複数の独立した防壁に分散させる。

## メカニズム

この構造は、制御対象がAIでも人間でも組織でも技術システムでも成立する。次の三つの要素で整理できる。

### 1. 権限と能力の分離

主体が「何ができるか(能力)」と「何をしてよい、あるいは実際にできる状態にあるか(権限)」を区別する。能力が高くても、権限が有界であれば結果への影響も有界になる。逆に能力が低くても、過大な権限が与えられればリスクは大きくなる。制御の焦点は、能力の評価ではなく権限の付与・獲得・委譲の経路に置かれる。

### 2. 多層並列統制による単一障害点の排除

制限を一つの層(たとえば技術的なガードレールだけ)に頼らず、技術・組織・人的の各層で独立に、並列して課す。層同士が互いの失敗に依存しないため、一つの層が破られても他の層が権限を有界に保つ。これは複数の独立した判断者による牽制([[plural-independent-checks-against-singular-power]])や、制度的耐久性([[multi-layer-independent-control-and-institutional-durability]])と同型の発想である。

### 3. 予防的設計への責任の埋め込み

責任を、問題が起きた後の監視や説明として付加するのではなく、権限が不可逆な結果を生む前の設計段階に組み込む。これは不可逆化前の権限判断と制約の内部設計化([[pre-irreversibility-authority-and-constraint-embedding]])、および実行時の権限委譲設計([[execution-time-governance]])と連続する考え方である。

## 理論的背景

### AI Authority Control Framework(AACF)

Saipによる AACF は、この概念の中核となるソースである。ソースの抜粋から確認できる要点は次のとおりである。

- モデルの能力だけを安全性の中心変数とせず、結果を左右する権限(consequential authority)を有界化する社会技術的枠組みである。
- 権限を Granted(付与済み)、Obtainable(獲得可能)、Deferred(委譲・繰延)、Systemic(体系的)に区別する。
- 技術的な実行権限(AAL)と体系的な影響力(SIL)を分離する。
- 外部のコントロールプレーン、認証情報の仲介、権限予算、安全な遷移、人的監督、ガバナンス、ポートフォリオの各統制を規定する。
- 自己昇格、自己統治、封じ込められない永続化や複製、一方的な破滅的権限など、意味のある人的統制を損ないうる構成に対しては、厳格なデプロイゲートを導入する。

ソースの核心的知見は、技術・組織・人的の複数層で権限を並列に制限する社会技術的アーキテクチャが、自律型スケーリングに対する本質的な防壁になるという点である。

### Responsible Autonomy Framework(RAF)

Siddiqui と Kamal は、e-business におけるエージェント型AIのための階層型ガバナンス構造を提案している。運用的自律、戦略的自律、責任ある自律の三層からなり、責任を「後付け」ではなく統治層として位置づける。既存のガバナンス枠組みは透明性・説明責任・公平性を個別に扱いがちで、運用自動化から組み込み型ガバナンスまでを通貫するものはない、と指摘する。核心的知見は、責任ガバナンスを自動化層構造に埋め込むことで、事後的な倫理監視から予防的設計へ転換できるという点である。ただし本ソースは概念的研究であり、実証データに基づく検証は抜粋からは確認できない。

### 人・AI共存のガバナンス枠組み

Kajino らの論文は、プロトコル駆動のガバナンスモデルを提案し、AIを人間の知的能力の拡張、ロボティクスを身体機能の拡張として区別している。抜粋の範囲では、AIに法的なエージェントとしての地位を認めれば対称的なガバナンス構造が可能になるが、その実装メカニズムは未整備であるとされる。権限有界化の観点では、権限主体の位置づけを問う補助的な視座を与えるが、並列独立層の具体的な設計は示されていない。

## AI Nativeな設計への示唆

1. **能力評価から権限設計へ重心を移す。** モデルの性能評価だけで展開可否を判断せず、付与・獲得可能・委譲される権限を棚卸しし、その上限を設計する。
2. **層の独立性を確認する。** 技術的制限、組織的手続き、人的監督が同じ前提や同じ故障モードに依存していないかを点検する。独立していなければ、並列化の意味が薄れる。
3. **自己昇格・自己統治などの構成にはデプロイゲートを置く。** 人的統制を損ないうる構成は、運用で調整するのではなく展開そのものを止める境界として設計する。
4. **責任を統治層として組み込む。** 責任ある運用を自動化層の一部とし、事後の監査だけに依存しない。行為の根拠を独立に再構成できる仕組み([[authorization-artifact-and-independent-reconstructability]])も併用できる。
5. **権限と影響力を分けて扱う。** 個別の実行権限だけでなく、システム全体への影響力も別の指標として管理する。
6. **人的層の役割変化に備える。** 自動化が進むと人間側に残る問題の複雑度が上がりうる([[automation-layer-elevating-residual-human-complexity]])。また、意思決定サイクルの圧縮下でも残余権限を確保する必要がある([[decision-cycle-compression-and-residual-authority]])。

## 関連コンセプト

- [[multi-layer-independent-control-and-institutional-durability]] — 独立した複数の制御層による耐久性
- [[plural-independent-checks-against-singular-power]] — 独立した複数判断者による牽制
- [[pre-irreversibility-authority-and-constraint-embedding]] — 不可逆化前の権限判断と制約の内部設計化
- [[execution-time-governance]] — 実行時ガバナンスと権限委譲設計
- [[authorization-artifact-and-independent-reconstructability]] — 認可アーティファクトと独立的再構成可能性
- [[ai-decision-authority-restructuring]] — AI組み込みによる意思決定権限の再構成
- [[decision-cycle-compression-and-residual-authority]] — 意思決定サイクルの圧縮と残余権限
- [[automation-layer-elevating-residual-human-complexity]] — 自動化層と人間層の複雑度
- [[self-improvement-loop-and-deployment-harness-design]] — 自己改善ループとハーネス設計

## 参考ソース

1. Responsible Automation in E-business: A Framework for Agentic AI Integration and Governance — Mohammad Talha Siddiqui, usuf Kamal (2026)
   File: raw/papers/systems_engineering/responsible-automation-in-e-business-a-framework-for-agentic-ai-integration-and-.md
2. An Ontological and Protocol-Driven Governance Framework for Autonomous AI Safety, Sustainability, and Human-AI Coexiste — Hideo Kajino, AI (2026)
   File: raw/papers/systems_engineering/an-ontological-and-protocol-driven-governance-framework-for-autonomous-ai-safety.md
3. AI Authority Control Framework: A Sociotechnical Architecture for Bounding Consequential AI Authority — Alexander Saip (2026)
   File: raw/papers/systems_engineering/ai-authority-control-framework-a-sociotechnical-architecture-for-bounding-conseq.md
