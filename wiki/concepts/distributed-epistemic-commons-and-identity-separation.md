# 分散的知のコモンズと関係・同一性の分離

## 概要

分散的知のコモンズと関係・同一性の分離(Distributed Epistemic Commons and Separation of Relation from Identity)は、Tier 1(不変原理)に位置づけられる概念である。要点は二つある。

1. 知識・記憶・責任は、特定のモデル、企業、サーバー、個人といった単一の主体や基盤に閉じ込めず、分散的に保持されるべきである。
2. 分散的な関係基盤(インフラ、認知、貢献、意味的連続性)と、主体の同一性・責任帰属は区別して設計しなければならない。関係が分散していることは、同一性が分散・融合していることを意味しない。

AI Nativeな社会では、説明・推論・研究・評価・意思決定にAIが参加する。このとき、知の蓄積をどこに置くかという問題と、誰が(何が)その知の担い手であり責任を負うかという問題が混同されやすい。前者を分散させながら後者を明確に保つことが、この概念の設計上の核心である。また、人間とAIの統合体が「一体」として振る舞うには、結合の事実だけでは足りず、高次の組織化が必要になる。

## メカニズム

対象を人間・AI・組織・技術のいずれに入れ替えても成立する構造として、次の三つに整理できる。

### 1. 基盤と主体の分離

知識・記憶・仮説・来歴などの蓄積(基盤)は、それを利用・更新する個々の主体(モデル、人、組織)から切り離して保持される。主体は交換可能だが、基盤は存続する。一方で、基盤が共有されていても、各主体の同一性や来歴を担う identity は融合しない(非融合の立場)。

### 2. 責任帰属の再編成

知識生産の各段階が複数の主体や基盤へ分散すると、従来の「単一の著者=責任者」という前提は成り立たなくなる。そのため、どの操作を委譲してよいか、誰がどの段階に責任を負うかを制度として再設計する必要がある。委譲が統制された拡張にとどまるか、認識的境界の溶解になるかは、この設計の有無で分かれる。

### 3. 階層的統合による個体性の形成

結合が緊密になり協力・分業が進んで「進化的個体」の性質を帯びたとしても、それだけでは情報統合や意思決定の一貫性を備えた「認知的個体」にはならない。統合体としての一体性には、結合よりも高次の組織化が要る。

## 理論的背景

### 分散型科学認知コモンズ(DSCC)

Maedaの DSCC は、知能を単一のモデル・企業・サーバー・クラウドに閉じ込めない設計を提案する。モデルは置き換えられ、サーバーは消え、企業は閉鎖しうるが、持続すべきは周囲に蓄積された科学的認知(記憶、仮説、失敗した実験、発見された機構、シミュレーション環境、ツール、世界モデル、未解決の問い、来歴、実行可能な研究ワークフロー)であるとされる。これらは内容アドレス型の分散コモンズとして、複数のAIモデルが読み書き・検証・拡張できる。ローカルLLMはすべての科学的能力をパラメータ内に持つ必要がなく、分散ツールの呼び出しや他エージェントの実験の再利用、ボランティア計算資源への計算委託、再現可能な来歴の確認ができる。

### 関係と同一性の区別

Kannon の "Distributed Relation Is Not Distributed Identity" は、分散的な関係・インフラ・認知・貢献・意味的連続性を、分散的または融合した同一性から区別する非融合の議論を展開する。区別の軸は次のとおりである。

- 分散基盤と主体の同一性
- 機構と、その担い手となりうるもの
- 集合的認知と集合的意識
- 協働と集合的な起源性
- 意味的持続と人格的同一性の連続
- 成果物の変形と、来歴を担う同一性の喪失

AIの内面性については、外部観察や機構的記述だけでは意識の有無のいずれも確定できないという急進的懐疑が、認識上の境界として置かれている。

### 責任帰属の再編成

Vindigni は、生成AIによる注釈、コーディング、主題分析、データシミュレーションなどへの委譲を、統制された方法論的拡張と見るか、認識的境界の溶解と見るかを、技術的性能・方法論的妥当性・制度的埋め込み・科学的責任の帰属を統合する枠組みで検討している。エビデンスの批判的統合の手法をとる研究である。

### 統合体の個体性と認知的統一性

Shi は、Rainey と Hochberg による人間–AI関係への「進化の大転換」の枠組みの拡張を補完する。人間–AI複合体が進化的個体の性質を獲得しても、認知的個体になるにはさらなる組織化が必要だという問いを立て、認知的統一性(情報統合・意思決定の一貫性)にはより高次の組織化が要るとする。

### 制度・関係モデルの側面

Feng の Cognitive University は、生成AIが道具の追加にとどまらず、近代大学が依拠してきた認知アーキテクチャを変えると論じる。知識の希少性が薄れることで、協調的推論と認知主権が制度上の本質的要件になるとされる。Faria によるレビューは、AIを「道具」か「人類の代替」かという二分法を超え、認識的パートナーとして捉える方向を評価しつつ、保持すべき重要な区別が含まれることを指摘している。MacLean の論考は、有限な受信者の認識能力が、差異を受けた変容の歴史を通じて段階的に形成されるという、発達論的な見方を示す。

## AI Nativeな設計への示唆

1. **知の永続層を主体から切り離す**:記憶・仮説・失敗・来歴を、特定のモデルやベンダーに依存しない共有基盤に置く。モデルの入れ替えや事業者の消滅に耐える設計とする。
2. **来歴(provenance)を第一級の要素とする**:成果物が変形・再利用されても、誰(何)が寄与したかを追跡できるようにし、基盤の共有が同一性の融合や責任の曖昧化を招かないようにする。
3. **責任帰属を明示的に再設計する**:知識関連の操作をAIに委譲する際は、委譲の範囲、検証、責任者を制度として定める。統制された拡張か境界溶解かを分ける基準を設計に組み込む。
4. **協働を「集合的意識」や「融合」の主張に飛躍させない**:協働の設計では、機構の記述と主体性・意識の帰属を分けて扱う。AIの内面性について外部観察のみから断定しない。
5. **統合体の一体性には別途の組織化を設ける**:人間–AIの結合が緊密でも、情報統合や意思決定の一貫性は自動的には生じない。それを担う上位の調整構造を明示的に設計する。
6. **認知主権と協調的推論を制度要件にする**:教育・研究機関では、知識が希少でなくなる前提のもとで、人間が推論の主導権を保つ制度を整える。

## 関連コンセプト

- [[distributed-agency-and-assemblage-reconfiguration]] — 分散的行為者性と組織の再構成
- [[distributed-cognitive-load]] — 分散認知負荷
- [[finite-attention-and-heterogeneous-agent-coupling]] — 有限な認知資源と異質主体間の結合設計
- [[epistemic-authority-redistribution-and-knowledge-consolidation]] — 認識的権威の再配分
- [[epistemic-labor-displacement-under-delegation]] — 委譲による認識的労働の代替
- [[epistemic-risk-llm-higher-education]] — 高等教育におけるLLMの認識論的リスク
- [[digital-human-identity]] — デジタル人間のアイデンティティ
- [[trust-continuity]] — 信頼の継続性とアイデンティティ検証
- [[structural-separation-of-verification-from-governed-system]] — 検証機構の構造的分離
- [[edge-ai-distributed-trustworthy]] — エッジAIの分散・信頼性

## 参考ソース

- The Cognitive University: A Civilization-Scale Architecture for Learning, Human–AI Co-Reasoning, Cognitive Sovereignty, Competency, and Institutional Transformation(政恩 馮、2026)— `raw/papers/cognitive_science/the-cognitive-university-a-civilization-scale-architecture-for-learning-humanai-.md`
- Distributed Scientific Cognition Commons (DSCC)(Yusuke Maeda、2026)— `raw/papers/cognitive_science/distributed-scientific-cognition-commons-dscc.md`
- From evolutionary individuality to cognitive integration: a cross-modular perspective on human–AI coevolution(Edward Ruoyang Shi、2026)— `raw/papers/cognitive_science/from-evolutionary-individuality-to-cognitive-integration-a-cross-modular-perspec.md`
- Between Methodological Expansion and Epistemic Boundary Dissolution: Generative AI, Distributed Epistemic Processes, and the Reorganization of Scientific Responsibility(Giovanni Vindigni、2026)— `raw/papers/cognitive_science/between-methodological-expansion-and-epistemic-boundary-dissolution-generative-a.md`
- Distributed Relation Is Not Distributed Identity(Aelion Kannon、2026)— `raw/papers/cognitive_science/distributed-relation-is-not-distributed-identity.md`
- Review of: "Knowledge and Communication with AI"(Diego R. Faria、2026)— `raw/papers/cognitive_science/review-of-knowledge-and-communication-with-ai.md`
- Works for 9/17/2026 - Bea Arthur (Bernice Frankel)(Ryan MacLean、2026)— `raw/papers/cognitive_science/works-for-9172026---bea-arthur-bernice-frankel.md`
