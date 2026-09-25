# レジリエント社会技術設計

## 概要

**レジリエント社会技術設計（Resilient Sociotechnical Design）** は、AI システムを含む複雑な社会技術システムが外乱や予測不可能な環境変化に対して、単に吸収するだけでなく、適応し、さらには創造的に変革できる多層的な回復力を内在させた設計論である。

従来の安全設計や品質管理は「Safety I」と呼ばれるアプローチ（問題が起きた後に原因を特定し排除する）に依拠していた。しかし AIが統合された社会技術システムでは、複雑性と不確実性の程度が質的に変わる。予測不可能な相互作用、エマージェント現象、多主体間の価値衝突が常態化する環境では、事前に完全な仕様を定義し「正常/異常」を二項対立的に分類することは不可能である。

そこで求められるのが、システムが**継続的に学習・調整しながら機能する能力**、つまり「Safety II」的アプローチ――変化する環境に「常に適応する」ことで安全と効率を両立させる設計思想である。レジリエント社会技術設計は、このアプローチを、組織・技術・人間・制度層の全体を視野に入れて体系化したものだ。

## 理論的背景

### システムの適応的回復力

C. S. Hollingの古典的研究は、エコロジカルシステムが複数の安定状態を持つことを示した。システムが外乱に対して「同じ状態に戻る」吸収性レジリエンス（resistance resilience）だけでなく、「新しい状態に移行しながら機能を維持する」適応的レジリエンス（adaptive resilience）を備えることの重要性を指摘している。

### 動的能力とシステム進化

Eisenhardtら（raw/papers/complexity_science/dynamic-capabilities-what-are-they.md）の研究によれば、急速に変化する環境下で組織が競争優位を維持するには、「プロセス開発」「統合」「再構成」という**動的能力**が不可欠である。これは単なる適応ではなく、既存のリソース基盤そのものを継続的に再組織化する能力を意味する。AI Native社会ではこうした動的能力がシステムレベルで求められる。

### 医療システムに学ぶ実装モデル

Braithwaitre、Wears、Hollnagelら（raw/papers/systems_engineering/resilient-health-care-turning-patient-safety-on-its-head.md）は医療システムの実践的レジリエンスを分析した。医療の複雑性と高リスク環境において、システムは「標準化された手順」と「現場の柔軟な判断」を動的に組み合わせることで機能している。この二層的な適応メカニズムが、社会技術システム全般の設計原理として転用できる。

### 複雑系における適応メカニズム

Hollandの遺伝的アルゴリズムと適応系理論（（パス未確認））も、人間の直感的判断では捉えきれない遅延や非線形フィードバックがシステム挙動を支配することを明らかにしている。

### AIアカウンタビリティと多主体ガバナンス

Rajiら（raw/papers/systems_engineering/closing-the-ai-accountability-gap.md）の研究は、AI システムの社会的影響が検査後に判明する現状を指摘し、**継続的な監査・検証・是正メカニズム**を組み込んだ設計の必要性を訴えている。これは、導入後の学習ループを構造化することの重要性を示唆している。

## AI Nativeな設計への示唆

### 1. 多層的フィードバック構造の実装

レジリエント設計では、AIシステムに対する信号が単一レイヤーに集約されてはならない。技術層（システムメトリクス）、組織層（プロセス指標）、社会層（利用者/被影響者の評価）、制度層（規制環境・法的変化）から並行して信号を入力し、システムがこれら複数の目的関数を**同時適応的に調整**する仕組みが必要である。

### 2. 予測不可能性への設計対応

外乱（adversarial attack、コンセプトドリフト、規制変更、利用者行動の急激な変化）を個別に予測し対策するのではなく、システム自体が**サーボメカニズム的に自動調整できる構造**を備えること。これは、堅牢性（robustness）と柔軟性（flexibility）を両立させる二層構造（安定コア+変動フロンティア）の実装を意味する。

### 3. 組織学習ループの統合設計

Chambersら（raw/papers/complexity_science/the-dynamic-sustainability-framework-addressing-the-paradox-of-sustainment-amid-.md）の動的持続性フレームワークは、変化の中で機能を維持するには、継続的な仮説検証と改善サイクルが必須であることを示している。AIシステムの設計段階から、継続的な性能評価・知識獲得・再構成を**組織制度に埋め込む**ことが重要である。

### 4. 透明性と調整可能性の両立

Amagi Open Specificationなどのハードウェア・ソフトウェア協調設計（raw/papers/systems_engineering/amagi-open-specification-v11-the-standard-for-hardware-enforced-ai-safety.md）は、AIシステムに対する直接的な制御ポイントをシステムに内蔵することの重要性を示唆している。「ブラックボックス性」とレジリエンスは両立しない。

### 5. 技術採択と組織文化の同期

Venkateshら（raw/papers/complexity_science/technology-acceptance-model-3-and-a-research-agenda-on-interventions.md）のTAM3は、新技術の実装が、単なる機能性ではなく、組織文化・権力構造・個人のセルフ・エフィカシーと調和する必要があることを示している。AIシステムは技術的に完璧でも、実装組織がそれを適応的に運用できなければレジリエンスは失われる。

## 関連コンセプト

レジリエント社会技術設計は以下の概念と密接に関連している：

- **[[sociotechnical-coevolution]]** ― 社会と技術が相互に形成される過程の理解
- **[[dynamic-capability-regeneration]]** ― 組織的適応能力の継続的再生成
- **[[algorithmic-accountability-stack]]** ― 多層的な説明責任メカニズムの構築
- **[[federated-governance-model]]** ― 分散的な意思決定と調整の制度設計
- **[[mixed-initiative-orchestration]]** ― 人間とAIの役割分担の動的最適化
- **[[bounded-rationality-augmentation]]** ― 人間の判断限界を補完する設計

## 参考ソース

- Braithwaite, J., Wears, R. L., & Hollnagel, E. (2015). "Resilient health care: turning patient safety on its head." *Maturitas*, 82(1), 3-6. [raw/papers/systems_engineering/resilient-health-care-turning-patient-safety-on-its-head.md]

- Woods, D. D. (2017). "Resilience Engineering." [raw/papers/systems_engineering/resilience-engineering.md]

- Holling, C. S. (1973). "Resilience and Stability of Ecological Systems." *Annual Review of Ecology and Systematics*, 4, 1-23. [raw/papers/operations_research/resilience-and-stability-of-ecological-systems.md]

- Holland, J. H. (1992). *Adaptation in Natural and Artificial Systems*. MIT Press. [raw/papers/complexity_science/adaptation-in-natural-and-artificial-systems.md]

- Eisenhardt, K. M., & Martin, J. A. (2000). "Dynamic capabilities: what are they?" *Strategic Management Journal*, 21(10-11), 1105-1121. [raw/papers/complexity_science/dynamic-capabilities-what-are-they.md]

- Sterman, J. D. (2002). *System Dynamics: Systems Thinking and Modeling for a Complex World*. McGraw-Hill. [raw/papers/complexity_science/system-dynamics-systems-thinking-and-modeling-for-a-complex-world.md]

- Chambers, D., Glasgow, R. E., & Stange, K. C. (2013). "The dynamic sustainability framework: addressing the paradox of sustainment amid ongoing change." *Implementation Science*, 8(1), 117. [raw/papers/complexity_science/the-dynamic-sustainability-framework-addressing-the-paradox-of-sustainment-amid-.md]

- Raji, I. D., Smart, A., White, R. N., Mitchell, M., & Gebru, T. (2020). "Closing the AI accountability gap." *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency*, 33-44. [raw/papers/systems_engineering/closing-the-ai-accountability-gap.md]

- Venkatesh, V., & Bala, H. (2008). "Technology Acceptance Model 3 and a Research Agenda on Interventions." *Decision Sciences*, 39(2), 273-315. [raw/papers/complexity_science/technology-acceptance-model-3-and-a-research-agenda-on-interventions.md]