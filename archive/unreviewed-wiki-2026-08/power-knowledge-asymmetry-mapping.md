# 権力知識非対称性マッピング

## 概要

**権力知識非対称性マッピング（Power-Knowledge Asymmetry Mapping）** は、AIシステムが設計・展開される過程で、誰の知識が優先されるのか、そして誰の利益が最大化されるのかという権力構造の非対称性を可視化・分析する批判的枠組みです。

AI Native時代の社会設計において、この概念は極めて重要です。なぜなら、AIシステムは本質的に特定の知識体系と利益構造を内包するアーティファクトであり、その「普遍的」に見える判断基準が実は特定の立場を優遇しているからです。医療用アルゴリズムの人種差別的バイアス、教育AIが特定の学習スタイルのみを最適化するケース、あるいはプラットフォームAIが支配的な言語や文化的規範を強化する現象——これらすべてが権力知識非対称性の具体例です。

AI Nativeな設計では、技術的パフォーマンスだけでなく、**このような非対称性をシステムレベルで可視化し、複数の知識体系と利益構造を統合する設計戦略**が求められます。

## 理論的背景

### 知識と権力の不可分性

Donna Harawayの「状況的知識（Situated Knowledges）」の概念は、すべての知識が特定の社会的位置から生成される点を指摘しました。完全に「客観的」な知識というものは存在せず、観察者の身体性、社会的位置、政治的関心が知識生成に組み込まれています。

AIシステムにおいて、これは学習データの選別基準、特徴量エンジニアリング、評価指標の設定に顕著に表れます。どのデータを「代表的」と見なすのか、どの予測誤差を「許容可能」と考えるのか——こうした選択は、設計者や利害関係者の権力的立場を反映しています。

### アルゴリズムバイアスと知識の普遍化

2019年のObermeyer et alの研究「Dissecting racial bias in an algorithm used to manage the health of populations」は、医療管理システムで広く採用されたアルゴリズムが人種差別的バイアスを内包していたことを実証しました。このバイアスは、特定の人口統計グループのコストデータが学習データに過度に反映され、医療ニーズを正確に予測していなかったことに由来していました。重要な点は、このアルゴリズムが「客観的」で「中立的」であるとみなされていたことです——権力知識非対称性はまさにここで作用しており、特定の知識体系（経済効率性）が医学的知識（個別患者のニーズ）よりも優先されていました。

### システム的な説明責任の欠如

Guidotti et alの「A survey of methods for explaining black box models」が示すように、AIシステムの内部ロジックが隠蔽されることで、どのような知識が優先されているのかを検証する能力そのものが失われます。この「説明不可能性」は技術的問題というより、権力関係の問題です。説明責任を果たせないシステムは、その判断基準となる知識体系とそれを推し進める利益構造を隠蔽しているのです。

### 多層的な制度化と経路依存性

Paul Piersonの「Increasing Returns, Path Dependence, and the Study of Politics」が指摘する経路依存性は、AIの導入においても機能します。一度あるアルゴリズムが組織に組み込まれると、その設計上の選択（したがって権力的選択）が組織文化に埋め込まれ、修正が困難になります。権力知識非対称性はこうした制度化プロセスを通じて強化されていきます。

## AI Nativeな設計への示唆

### 1. 複数知識体系の明示的統合

設計段階で異なる知識体系——専門的知識、利用者の経験知、周縁化された知識体系——を等価なものとして扱う仕組みが必要です。これは単なる「多様なステークホルダーの参加」ではなく、各知識体系が設計判断にどのような影響を与えるかを可視化することを意味します。

AI Nativeシステムでは、複数の特徴量セットや複数の評価指標を平行して運用し、異なる知識体系に基づく複数の「モデル」を保持することが有効です。これにより、どの知識体系が優先されているかが明白になります。

### 2. 権力図の動的マッピング

静的な権力分析ではなく、AIシステム導入プロセス全体を通じて権力関係がどう変化するかを追跡することが重要です。特に、データ収集段階、モデル学習段階、導入段階、運用段階ごとに異なるアクターが権力を行使します。

[[algorithmic-accountability-stack]] の考え方と組み合わせることで、各段階における知識優先性を記録し、多層的な説明責任を実現できます。

### 3. 利益構造の明示化と再協議

AIシステムが「最適化」する対象（コスト削減か、ユーザー満足度か、平等性か）は政治的選択です。AI Nativeな設計では、この選択が明示的に行われ、定期的に再協議されることが必要です。

単一の目的関数ではなく、複数の目的関数を並行実行し、それらが衝突する場面を可視化することで、どの利益が優先されているかを透明化できます。

### 4. 周縁化された知識の復権メカニズム

既存のAIシステムは多くの場合、計量可能な知識（ビッグデータ）を優先し、定性的・文脈的知識を周縁化します。AI Nativeな設計では、こうした周縁化された知識を意図的に統合するメカニズムが必要です。

例えば、[[mixed-initiative-orchestration]] モデルでは、AIの判断を人間の経験知や倫理的直観と交差させることで、複数知識体系の対話を組み込むことができます。

### 5. 権力知識非対称性の監視指標

[[algorithmic-accountability-stack]] と連携して、権力知識非対称性を定量化する指標を開発することが有効です。例えば：

- 学習データにおける異なる人口統計グループの表現度
- モデルの予測誤差がどのグループで最大か
- 特徴量の重要度が異なる知識体系をどう反映しているか
- システム導入による異なる利害関係者への影響分布

これらの指標を継続的に監視することで、非対称性の発生と拡大を検知できます。

## 関連コンセプト

- **[[algorithmic-accountability-stack]]** — 権力知識非対称性を可視化するための多層的な説明責任アーキテクチャ
- **[[human-centered-value-alignment]]** — 異なる価値体系をどう調整するかという根本的問題
- **[[mixed-initiative-orchestration]]** — 複数知識体系を対話させるための実装パターン
- **[[techno-institutional-transition-analysis]]** — 権力関係の制度化プロセスを分析するための枠組み
- **[[federated-governance-model]]** — 権力を分散させる組織設計アプローチ

## 参考ソース

- Haraway, Donna. "Situated Knowledges: The Science Question in Feminism and the Privilege of Partial Perspective" (1988). *raw/papers/philosophy/situated-knowledges-the-science-question-in-feminism-and-the-privilege-of-partia.md*

- Obermeyer, Ziad et al. "Dissecting racial bias in an algorithm used to manage the health of populations." *Nature Medicine* 25.10 (2019): 1357-1359. *raw/papers/law/dissecting-racial-bias-in-an-algorithm-used-to-manage-the-health-of-populations.md*

- Guidotti, Riccardo et al. "A survey of methods for explaining black box models" (2019). *raw/papers/law/a-survey-of-methods-for-explaining-black-box-models.md*

- Pierson, Paul. "Increasing Returns, Path Dependence, and the Study of Politics" (2000). *raw/papers/sociology/increasing-returns-path-dependence-and-the-study-of-politics.md*

- Latour, Bruno. *Reassembling the Social* (2005). *raw/papers/sociology/reassembling-the-social.md*

- Floridi, Luciano et al. "AI4People—An Ethical Framework for a Good AI Society" (2018). *raw/papers/law/ai4peoplean-ethical-framework-for-a-good-ai-society-opportunities-risks-principl.md*