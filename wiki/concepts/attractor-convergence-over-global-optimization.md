# 大域最適化ではなく構造アトラクタへの局所自己組織化による収束

## 概要

この概念は、学習や適応を「大域的な損失関数の最小化」としてではなく、「局所情報と構造制約のもとで、安定な構造(構造アトラクタ)へ有限回の操作で収束する過程」として捉える原理である。Tier 1(不変原理)に位置づけられる。

中核となるメカニズムは次の3つである。

- アトラクタへの自己組織化
- 局所情報による信用割り当て
- 臨界近傍での動的安定性

AI Nativeな社会設計で重要になる理由は、システムの規模が大きくなるほど、全体を見渡して単一の目的関数を最適化する設計が現実的でなくなるためである。全体を集中的に最適化する代わりに、局所ルールと構造制約を整え、望ましい安定構造へ収束する条件を設計する、という発想に転換できる。

## メカニズム

この原理は、対象が脳、AIモデル、組織、技術基盤のいずれであっても、次のような構造として整理できる。

1. **構造制約の設定**: 状態が取りうる構造の空間(ソース[2]ではハイパーグラフ空間)と、その中で許される変換操作を定める。
2. **局所情報による更新**: 各要素は、自分が観測できる局所的な情報(ソース[3]では局所シナプスのスパイクタイミング)だけで更新を行う。全体の勾配を必要としない。
3. **アトラクタへの収束**: 更新が繰り返されると、構造は安定な状態(アトラクタ)に落ち着く。収束は有限回で保証されうる。
4. **臨界近傍での動作**: 安定性と柔軟性の両立のため、系は秩序と無秩序の境界である臨界領域の近くで動くことが想定される。臨界への近さは計測可能である(ソース[1])。

大域最適化との違いは、「何を最小化するか」ではなく「どの構造に収束するか」を問う点にある。評価は損失値ではなく、到達した構造の存在・一意性・安定性で行われる。

## 理論的背景

### 構造アトラクタとしての学習(ソース[2])

Invariant Structural Learning(ISL)理論は、概念形成に対する非最適化アプローチを提案している。学習はハイパーグラフ空間における構造アトラクタへの収束と解釈され、大域損失関数の最小化としては扱われない。論文の数学的部分では、次の3点が示されたとされる。

- 構造的縮約過程の有限収束
- クラスごとの構造アトラクタの存在と一意性
- アトラクタマップの自己組織化

計算面では、古典的な画像認識タスクで、バックプロパゲーションを用いず、きわめて小さな訓練データで実行可能であることが示されている。神経生物学的解釈も仮説として提示されている。

### 局所スパイクタイミングによる信用割り当て(ソース[3])

主流のスパイキングニューラルネットワークは、代理勾配によるバックプロパゲーションの近似を用いるため、学習が生物学的なスパイクタイミングから切り離される。この研究は時間的信用割り当てを「状態分離問題」、つまり過去の摂動によって生じたタスク必要成分を現在の神経状態から取り出す問題として再定式化した。勾配トンネリング(GT)アルゴリズムとリード・ラグ展開により、局所的なシナプスのスパイクタイミングから信用割り当てを導く。ANN-SNNハイブリッド構成とも両立するとされる。局所情報だけで信用割り当てが成立しうることを示す知見である。

### 臨界性のモデル非依存な計測(ソース[1])

臨界現象の特徴はべき乗則に従うアバランシェの出現だが、臨界指数の推定は難しく、解釈もモデル依存になりやすい。この研究は、一般化感受率の尺度であるフィッシャー情報計量(FIM)が、神経系の臨界領域をモデル非依存に特徴づけることを示した。分枝過程からスパイキングモデル、全脳モデルまで、生物学的複雑さの異なるモデルで検証され、各モデルの制御パラメータに対するFIMが臨界度を確実に追跡するとされている。

### 周辺的な知見(ソース[4][5])

- ソース[4]は、ニューロン-アストロサイトの二層力学ネットワークが、報酬誘発の分岐などの力学機構を通じて文脈変化の証拠蓄積を実現することを示す。ただしこれは生物実装に依存した記述にとどまり、本原理への寄与は間接的である(Tier 2)。
- ソース[5]は、適度な神経ノイズが、限られた経験から学んだ内部モデルによる希少事象の再生精度を支えることを扱う。抜粋の範囲では、ノイズが局所的な学習過程の推定制約を補うという示唆にとどまり、詳細な結果は確認できない。

## AI Nativeな設計への示唆

- **収束条件を設計対象にする**: 単一の大域目的関数を定義するより、許容される局所操作と構造制約を定め、有限回で安定構造に到達する条件を設計する。
- **局所信用割り当てを前提にする**: 各エージェントや部門が自分の観測できる情報だけで更新できるようにし、全体の勾配や中央集権的な評価に依存しない。
- **臨界近傍の計測を運用に組み込む**: モデル非依存な指標(FIMのような感受率的尺度)で、システムが硬直(秩序過多)と混乱(無秩序過多)のどちらに寄っているかを監視する。ただしソース[1]は神経系モデルでの検証であり、社会システムへの直接適用は今後の検証課題である。
- **少データ・非バックプロパゲーションの選択肢を持つ**: ソース[2]は、極小データでの学習が構造的アプローチで可能であることを示唆する。
- **局所適合の限界に注意する**: 局所的な整合が全体の整合を保証するとは限らない。構造制約の設計には全体との接続点が必要になる。
- **ノイズを排除対象にしない**: ソース[5]の示唆では、適度なゆらぎが内部モデルの精度に寄与しうる。

## 関連コンセプト

- [[self-organization-emergence]] — 自己組織化と創発。本原理の基盤となる考え方。
- [[energy-landscape-attractor-memory]] — アトラクタによる記憶・推論の安定化。アトラクタ収束の別の実現形態。
- [[local-compliance-global-failure-composability-gap]] — 局所適合の総和が全体適合を保証しない問題。局所自己組織化の限界を示す。
- [[stigmergic-self-organization-of-organizational-structure]] — 組織構造の自己組織化。組織における局所ルールからの構造形成の例。
- [[global-standard-local-context-reconciliation]] — 普遍基準と局所文脈の調和。
- [[combinatorial-optimization-graphs]] — 大域最適化との対比で参照できる組合せ最適化。
- [[causality-based-iot-self-adaptation]] — 技術システムにおける局所的な自律適応。

## 参考ソース

1. Fisher Information Metric as a model-free measure of proximity to criticality in neural systems — Yuewei Du, Alberto Liardi, Hardik Rajpal, Henrik Jeldtoft Jensen (2026)
   File: raw/papers/neuroscience/fisher-information-metric-as-a-model-free-measure-of-proximity-to-criticality-in.md
2. Formation of structural attractors in neuromorphic systems — Yurii Parzhyn, Alexander Schwarzmann, Mykyta Lapin, Kostiantyn Bokhan (2026)
   File: raw/papers/neuroscience/formation-of-structural-attractors-in-neuromorphic-systems.md
3. A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits — Xiangnan Zhang, Jingxin Liu, Ranqi Lu, Jingyu Liu, Qunxi Dong (2026)
   File: raw/papers/neuroscience/a-gradient-based-yet-spike-timing-dependent-solution-to-the-feedback-learning-pr.md
4. A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation — Giacomo Vedovati, Ilya E. Monosov, Thomas J. Papouin, ShiNung Ching (2026)
   File: raw/papers/neuroscience/a-neural-astrocyte-architecture-implements-a-hybrid-automaton-for-evidence-accum.md
5. Neural noise enables accurate internal simulation of rare events — Heng Zhang, Pawel Herman, Zenas C. Chao (2026)
   File: raw/papers/neuroscience/neural-noise-enables-accurate-internal-simulation-of-rare-events.md
