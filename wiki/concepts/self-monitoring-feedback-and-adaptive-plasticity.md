# 内部状態の自己監視フィードバックと適応可塑性の維持

## 概要

非定常環境で自律的に適応し続けるには、外部環境の変化に反応するだけでは足りない。システム自身の内部状態、つまり学習能力の劣化、資源の枯渇、守るべき価値の維持状況などを監視し、状態遷移の連続性を保ちながら回復させるフィードバックループが必要になる。本記事ではこれを「内部状態の自己監視フィードバックと適応可塑性の維持」と呼ぶ。Tier 1(不変原理)に位置づけられる概念であり、実装基盤が生物・AI・組織のいずれであっても成立する構造として扱う。

AI Nativeな社会設計では、AIエージェントが長期にわたり変化する環境で稼働し続ける。このとき問題になるのは、外部へ適応しようとするほど内部が損なわれ、学べなくなる事態である。内部状態の可観測性と回復手段を設計に組み込むことが、持続的な適応の前提になる。

## メカニズム

対象を人間・AI・組織・技術のどれに入れ替えても、次の構造が繰り返し現れる。

1. **内部状態の監視(内受容)**: 外部環境のセンシングとは別に、自身の状態(休止、劣化、資源残量など)を観測する経路を持つ。
2. **価値(存続基準)の参照**: 何の劣化を防ぎ、何の維持を確保するのかという「賭け金(stakes)」を定義する。監視した状態はこの価値に照らして評価される。
3. **検証を伴う介入**: 異常の兆候が見えても、直ちに介入せず、複数の方向から確認してから回復操作を行う。誤った回復は、健全な機能を壊しかねない。
4. **遷移の連続性の維持**: 回復や適応の過程で、システムが連続した状態遷移をたどれるようにする。断絶的なリセットは、蓄積した機能まで失わせる。
5. **可塑性の保持**: 回復の結果、システムが以後も学習・再評価できる能力を持ち続ける。

この構造は、外部への反応だけを行う制御ループに、内部状態を対象とした二重目のループを重ねたものと捉えられる。一般的なフィードバックの枠組みは [[feedback-loops-system-dynamics]] や [[decision-loops-and-layered-decentralized-control]] と接続する。

## 理論的背景

### 内部状態の劣化と双方向確認(PRIME)

UAV支援の緊急通信ネットワークを対象とするPRIMEは、多くの強化学習コントローラが定常条件を仮定するか、変化に対応するものでも外部環境にのみ反応し、ネットワーク内部の状態を調べていない点を問題にする。持続的な非定常性は内部状態を直接損傷する。目的が変化するにつれてニューロンが徐々に休止し、共有ポリシーが学習能力を失っていくという。

自明な対処は休止ニューロンのリセットだが、共有パラメータのマルチエージェント学習では安全でない。休止に見えるニューロンの多くは、実際には強い訓練勾配を受けている。また、あるニューロンが休止して見えるかどうかは、どのエージェントの観測を処理しているかにも依存する。そのためPRIMEは、介入前に両方向を確認する(双方向のSilent Neuronの枠組みをマルチエージェント強化学習に拡張)。核心的知見は、共有パラメータ環境では休止判定に双方向確認が必須という点である。

### 内受容的AI

Lee、Oh、An、Yoon、Fristonによる、生命に着想を得た内受容的人工知能の研究は、自己監視フィードバックループが不確実性下での自律適応を支える根本原理であるという知見を示す。ソース抜粋にはAbstractの本文が含まれていないため、詳細なモデルや実験結果は本記事では扱わない。

### 価値システムの必然性

Terpstraは、LLMが感情を持つかという問いを、意識的感覚や感情様表現の有無ではなく機能面から分析する。感情を「模倣」ではなく「持つ」ための、3つの共同で必要な条件を提示している。

- **再編成(reorganization)**: 感情的に重要な刺激が、処理の持続的・多系統的な変化を生む。
- **可塑性(plasticity)**: そのエピソードが、以後の評価の仕方を持続的に変える。
- **賭け金(stakes)**: 再編成が、その劣化を防ぐ、または維持を確保するよう機能する、持続的な内部状態。

現在の言語モデルは、せいぜい最初の条件しか満たさないとされる。この枠組みでは知能は感じること・価値づけること・考えることの協調であり、適応的エージェントにおける価値システムは、生物的実装を超えた人工システムの根本要件として位置づけられる。

### 遷移の連続性(ENNORY)

ENNORYは「Transition Intelligence」を掲げ、複雑系が進化する状態間を遷移する際の連続性をモデル化・分析・保存する計算フレームワークである。共通の数学的・構造的基盤を保ちつつ、対象領域に応じた専門エンジンへ変形する。ソースではF1エンジニアリング、構造的心臓介入、人工知能への適用が示されている。状態遷移の連続性の維持が、ドメインを横断して適用できる構造として扱われている。

### 組織における内部資源状態の監視(参考的事例)

SMEを対象としたAIキャッシュフロー予測の研究は、売上や会計上の利益が黒字でも、資金移動のタイミングと不確実性によって債務を賄えず財務的困難が生じうると指摘する。従来の指標が悪化する前に流動性の転換点を特定するため、確率的予測により複数の将来キャッシュ軌道を生成し、流動性ランウェイや不足確率などを算出する。組織においても、外部指標(売上)とは別に内部の資源状態を監視する必要があることを示す一例である。

## AI Nativeな設計への示唆

- **内部ヘルス指標を設計に含める**: 性能指標だけでなく、学習能力の劣化(休止など)や資源余力といった内部状態を観測可能にする。
- **介入は検証してから行う**: 見かけの異常だけで回復操作をしない。共有資源やマルチエージェント環境では、複数の視点から確認する。
- **全面リセットを避ける**: 回復は既存機能の連続性を保つ形で行い、蓄積した能力を破壊しない。
- **価値・存続基準を明示する**: 何を劣化から守るのかを内部状態として持たせ、監視と回復の判断基準にする。
- **外部適応と内部維持を両立させる**: 環境変化への追従が内部の可塑性を犠牲にしていないかを、継続的に点検する。
- **組織・人間側の運用にも適用する**: 資源の時間的非同期性のように、外部指標に現れにくい内部状態の早期検知を、運用設計に組み込む。

## 関連コンセプト

- [[feedback-loops-system-dynamics]] — フィードバック構造の一般理論
- [[decision-loops-and-layered-decentralized-control]] — 多層的な制御ループの構造
- [[complex-adaptive-systems]] — 非定常環境で適応する系の基本枠組み
- [[causality-based-iot-self-adaptation]] — 自律適応の実装例
- [[consciousness-and-recursive-self-modeling]] — 自己の状態を対象とするモデリング
- [[adaptive-intelligence-emergence]] — 適応知能の創発

## 参考ソース

1. PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks — Wen Qiu, Zhiqiang He, Wei Zhao, Hiroshi Masui (2026)
   File: raw/papers/complexity_science/prime-plasticity-recovery-in-multi-agent-environments-for-uav-assisted-emergency.md
2. ENNORY: A Computational Framework for Transition Intelligence in Formula One Engineering, Structural Heart Intervention, and Artificial Intelligence — Anthea Tenayiah Leia Govender (2026)
   File: raw/papers/complexity_science/ennory-a-computational-framework-for-transition-intelligence-in-formula-one-engi.md
3. Life-inspired interoceptive artificial intelligence for autonomous and adaptive agents — Sung-Woo Lee, Younghyun Oh, Hyunhoe An, Hyebhin Yoon, Karl Friston (2026)
   File: raw/papers/complexity_science/life-inspired-interoceptive-artificial-intelligence-for-autonomous-and-adaptive-.md
4. Emotions and a Functional Test for Intelligence in Artificial Systems — Jeroen Terpstra (2026)
   File: raw/papers/complexity_science/emotions-and-a-functional-test-for-intelligence-in-artificial-systems.md
5. Artificial Intelligence-Based Cash Flow Forecasting for Early Financial Distress Detection and Adaptive Liquidity Management in SMEs — Mc-Niel Chinedu (2026)
   File: raw/papers/complexity_science/artificial-intelligence-based-cash-flow-forecasting-for-early-financial-distress.md
