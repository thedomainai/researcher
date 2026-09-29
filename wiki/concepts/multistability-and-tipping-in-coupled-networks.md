# 結合ネットワークの多安定性・転移点と低次元縮約

## 概要

相互作用する要素からなる系(ネットワーク)の挙動は、「結合構造の固有スペクトル」と「分岐点の相対的な配置」によって決まる。系がどの状態に落ち着くか、どこで急激に状態が切り替わるか、切り替えの前後で履歴(ヒステリシス)が残るかは、多数の要素の詳細ではなく、少数の有効変数で書ける低次元の記述で予測できる。これがこの概念(Tier 1: 不変原理)の主張である。

AI Nativeな社会設計では、人間・AIエージェント・組織・技術基盤が相互に結合した系を扱う。こうした系には複数の安定状態が共存し、小さな外乱で別の状態へ遷移し、元に戻りにくい履歴現象が生じうる。「何が起きるか」を個々の要素の振る舞いの積み上げで追うのではなく、構造と分岐の配置から予測し、設計に組み込む視点が重要になる。

## メカニズム

対象が人間、AI、組織、技術のいずれであっても、以下の三つの構造的原理は成立する。

1. **分岐と履歴現象**:結合の強さや遅れ(位相のずれ)、高次の相互作用などのパラメータを変えると、安定状態が生まれたり消えたりする。前進方向と後退方向で転移点が異なると、ヒステリシスループが現れ、系の状態は「現在のパラメータ」だけでなく「たどってきた経路」にも依存する。
2. **構造による引力域の決定**:多安定な系では、初期状態がどの安定状態に引き込まれるかは、結合構造と要素間の遅れなどから定まる引力域の大きさで決まる。構造は「どの状態が安定か」だけでなく「どの状態が選ばれやすいか」も規定する。
3. **次元削減による有効記述**:多数の要素の動力学を少数の変数の有効系に写像すると、転移点、双安定領域、転移の連続性といった大域的な性質を解析的に予測できる。

## 理論的背景

### Kuramotoネットワークの多安定性と引力域(ソース1)

Rossiらは、有限個の振動子ネットワークで、結合構造と不均一な位相遅れがどの集団状態を選ばせるかを扱っている。位相遅れは大域同期を不安定化し、一様な位相勾配をもつ状態やそれらの組み合わせといった位相ロック状態を促す。著者らは、結合構造と位相遅れを合成した「composite matrix」のスペクトルが、集団状態の線形安定性だけでなく引力域の大きさも支配することを示した。これにより、個々のネットワークについて、結合と位相遅れのみから位相ロック状態の引力域の大きさを解析的に見積もれる。

### 高階ネットワークの低次元相図(ソース2)

Qinらは、高階ネットワーク(ペア間を超える相互作用をもつ系)の動力学を有効な低次元系へ写像する解析的な次元削減の枠組みを構築した。この枠組みにより、転移点(tipping boundary)、双安定領域、相転移の性質を精度よく予測できる。さまざまな動力学過程に適用され、高階相互作用が転移の連続性やヒステリシスに与える異なる効果が示された。また、系のレジリエンスはペア結合と高階結合の整合(alignment)に強く依存し、同類的な混合(assortative mixing)が活性状態への転移を促進すると報告している。

### 二重の爆発的転移(ソース3)

DasとPalは、ペア相互作用と三体相互作用、非対称な位相遅れをもつ適応的二層マルチプレックスKuramotoネットワークを調べた。前進方向、後退方向、またはその組み合わせで「二重の爆発的転移」が現れ、単一または二重のヒステリシスループを伴う。Ott-Antonsen縮約で低次元系を導出して安定性解析を行った結果、縮約モデルは微視的な完全ダイナミクスを精度よく再現し、分岐点の解析式も得られた。複数のパラメータ平面の系統的なマッピングで8種類の同期レジームが見いだされた。サドルノード分岐とピッチフォーク分岐の点の相対的な順序が、位相遅れの非対称性、層間適応、高階相互作用の強さによって制御され、転移の段階的な様相を決める。

### 周辺的な知見

- **ソース4(休眠レポーター)**:不均一な結合をもつ複雑系で、疎な観測から外乱を分類する問題を扱う。初期条件の再現が不完全になると、感度の高い場所に観測点を置く方針は最適から大きく外れ、その差はノイズとともに拡大する。観測設計は感度最大化だけでは済まない。なお、抜粋は最良のパネルが「二つを混ぜる」と述べたところで途切れており、詳細は確認できない。
- **ソース5(時変データの層)**:時変データの表現形式を切り替えるときの情報損失を扱い、構造的な不変量に着目する。ネットワーク動力学の記録・比較のための表現選択にかかわる。
- **ソース7(再現可能なネットワーク)**:局所制約の設計集合から一意な構造が組み上がる条件(Unigraphical Design Theorem)を扱い、構造を設計で決めるという発想を与える。
- ソース6(確率的微分幾何)は、実務的優位性の実証が不十分と位置づけられており、本概念の根拠としては用いない。

## AI Nativeな設計への示唆

- **スペクトルと分岐点を設計変数として扱う**:エージェント間の結合(通信・依存・遅延)を、個々の性能ではなく結合行列のスペクトルと遅れの組み合わせで評価する。ソース1に基づけば、望ましい協調状態の引力域を構造から見積もれる。
- **ヒステリシスを前提に運用する**:転移点が前進と後退で異なる系では、いったん切り替わった状態をパラメータの巻き戻しだけでは戻せない。転移の手前に警戒指標を置き、復帰手順を事前に設計する。
- **低次元の有効モデルを併設する**:大規模なマルチエージェント系や組織に対し、少数変数の縮約モデルを用意して転移点や双安定領域を予測する。縮約モデルが微視的な挙動を再現できるかは、常に検証の対象とする。
- **ペア結合と高階結合の整合を意識する**:二者間の関係と多者間の協調構造の整合の度合いが、活性状態への転移のしやすさを左右する。
- **観測点は感度だけで選ばない**:ソース4の示唆に従い、不完全な情報下での状態判定では、堅牢性を考慮した観測配置を検討する。

## 関連コンセプト

- [[adaptive-reduction-theory-art]] — 適応的な次元削減という観点で対応する。
- [[recursive-feedback-criticality-threshold]] — 自己増幅が臨界閾値を超える転移と関係する。
- [[coupled-viability-architecture]] — 結合系の生存性を構造から捉える点で関連する。
- [[emergent-governance-networks]] — 結合構造から創発する秩序の議論とつながる。
- [[local-information-limits-and-decentralized-guarantees]] — 局所情報下での保証と限界という観点で関連する。
- [[structural-separation-and-hierarchical-verification]] — 構造による伝播の制御という設計面で関連する。

## 参考ソース

1. Phase-delays shape multistability and basin sizes in Kuramoto networks: analytical estimates from network structure — Kalel L. Rossi, Antonio Mihara, Lyle E. Muller, Rene O. Medrano-T, Roberto C. Budzinski (2026)
   File: raw/papers/complexity_science/phase-delays-shape-multistability-and-basin-sizes-in-kuramoto-networks-analytica.md
2. Low-Dimensional Phase Diagram of Higher-Order Networked Systems — Jia-Jie Qin, Jack Murdoch Moore, Xiaozhu Zhang, Gang Yan (2026)
   File: raw/papers/complexity_science/low-dimensional-phase-diagram-of-higher-order-networked-systems.md
3. Double explosive transitions in adaptive multilayer networks with higher-order interactions — Anath Bandhu Das, Pinaki Pal (2026)
   File: raw/papers/complexity_science/double-explosive-transitions-in-adaptive-multilayer-networks-with-higher-order-i.md
4. Efficiently classifying shocks in complex systems requires dormant reporters — David A. Brewster, Philippe Cluzel (2026)
   File: raw/papers/complexity_science/efficiently-classifying-shocks-in-complex-systems-requires-dormant-reporters.md
5. Time-Varying Data as Sheaves: an Invitation to Narratives — Wilmer Leal, Benjamin Merlin Bumpus, Jana K. Nickel, Johan García, James Fairbanks (2026)
   File: raw/papers/complexity_science/time-varying-data-as-sheaves-an-invitation-to-narratives.md
6. Probabilistic Differential Geometry in Artificial Intelligence — Jincheng Zhang (2026)
   File: raw/papers/complexity_science/probabilistic-differential-geometry-in-artificial-intelligence.md
7. Design Principles for Reproducible Networks — Jasper van der Kolk, Cory Glover, Albert-Lásló Barabási (2026)
   File: raw/papers/complexity_science/design-principles-for-reproducible-networks.md
