# 汎用能力に対する進化的選択圧と適応度のパラドックス

## 概要

「汎用的な知能は高いほど有利である」という直観は、しばしば暗黙の前提として置かれる。しかし、この前提は自明ではない。汎用能力が適応上有利になるかどうかは、環境、維持コスト、競争構造によって決まる。能力が高いことと、存続できることは別の問題である。これが本記事で扱う「適応度のパラドックス」である。

本コンセプトの主張は次のとおりである。**能力の高度化と存続可能性は分離して設計すべきである。** 能力を伸ばせば存続性も自動的に上がる、という設計上の前提を置いてはならない。

AI Nativeな社会設計にとって、この原理は重要である。AIの能力向上は、それ自体が目的として扱われやすい。しかし、能力が社会・組織・個人の存続や健全性に結びつくかどうかは、コストと便益の分配、環境条件、周囲の競争構造に依存する。能力の高さだけを指標にした設計は、この依存関係を見落とす。

## メカニズム

この原理は、対象を人間、AI、組織、技術のいずれに入れ替えても成立する構造として整理できる。中核は次の3つである。

### 1. 選択圧と適応度の環境依存性

適応度は、能力そのものの属性ではなく、能力と環境の組み合わせによって決まる。ある環境で有利な汎用性が、別の環境では過剰な負担になりうる。「汎用的であること」は、特化した対応が有利な環境では優位を保証しない。

### 2. 能力と存続の乖離

能力の水準と存続確率は、必ずしも単調な関係にない。能力が高くても存続できない場合がある。このため、能力を評価する軸と存続性を評価する軸は、設計上別々に置く必要がある。

### 3. コスト対便益の非対称性

汎用能力は、獲得・維持・運用にコストがかかる。一方で、その便益は環境や競争構造次第で実現しない場合がある。コストが確実に発生し、便益が不確実であるという非対称性が、能力の選択を左右する。

### 構造としての一般化

| 対象 | 能力 | 環境・競争構造 | 乖離の例 |
|---|---|---|---|
| 生物種 | 汎用的な知能 | 生態的条件 | 高い知能でも存続に寄与しない |
| AI | 汎用的な推論能力 | 制度・市場・統治 | 能力は伸びるが運用体制が追いつかない |
| 組織 | 幅広い技術ストック | 統合能力・競争 | 保有しても価値化できない |
| 個人 | 外部化された能力 | 環境の変化 | 便利さが自前の能力を弱める |

## 理論的背景

### 進化的観点からの問題提起

主要な根拠は、David Klotz による2026年の論文 "Smart Enough to Go Extinct? An Evolutionary Challenge to the Value of General Intelligence and Its Ethical Implications for AGI" である。ソースの核心的知見は、一般知能が進化的に不利になる可能性があり、それがAGI倫理に根本的な示唆を与える、というものである。タイトルが示すとおり、この論文は一般知能の価値を進化の観点から問い直している。

なお、今回参照できたのは書誌情報と要旨の冒頭のみであり、論証の詳細や具体的なモデル、実証データについては確認できていない。本記事の記述は、上記の核心的知見とコンセプト定義の範囲にとどめている。

### 能力の「同等性」をめぐる議論

民慶権(민경권)による2026年の論文 "Can AI Be an Individual, a Mental Entity, and a Subject?" は、直接の主題は異なる。AIが人間と同等の standing(地位)を持つための条件を論じており、その核心的知見は、そのためには人間と同じ心的メカニズムの全領域を実装する必要がある、というものである。人間は地球上で最も広い範囲の心的実体である、という位置づけも示されている。

この議論は、汎用性が何を指すのかを精密に定義する必要があることを示す。「汎用能力」を語る際には、比較の基準と対象範囲を明確にしなければならない。

### 補足的なソースについて

Hao らによる2026年の研究(衣装旅行写真の動機づけの進化心理学的分析)は、進化的な観点を用いる研究として収集されたが、Tier 2 であり、汎用能力の選択圧という本主題への直接の寄与は確認できていない。

## AI Nativeな設計への示唆

以上から、次の設計指針を導ける。これらは上記の原理に基づく設計上の含意であり、ソースが個別に提示した処方ではない。

1. **能力指標と存続指標を分けて管理する。** 性能の向上を、そのまま持続可能性や健全性の向上とみなさない。両者を別々の評価軸として設計に組み込む。
2. **環境を前提に能力を評価する。** 能力は、運用される環境、制度、競争構造との組み合わせで評価する。環境が変われば有利さも変わりうる。
3. **コストを便益と対で見積もる。** 汎用性の獲得・維持コストと、実現が不確実な便益とを対比する。便益が実現する条件を明示する。
4. **能力拡大に制御と統治を同期させる。** 能力が制御や責任の設計を上回らないよう、拡大の速度と統治の整備を対応づける。
5. **汎用性を目的化せず、必要な範囲を定義する。** どの範囲の能力が必要かを目的に即して定め、過剰な汎用化を避ける。

## 関連コンセプト

- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大と責任・統治設計の乖離
- [[capability-realization-organizational-bottleneck]] — 技術ストックではなく組織的統合能力が価値を決めるボトルネック
- [[capability-externalization-dual-effects]] — 能力外部化の二面性と非定常環境での再適応
- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による所有感・責任・能力の侵食
- [[capability-profile-based-task-allocation]] — 能力プロファイルに基づく役割分担と協働設計
- [[evolutionary-economics-and-organizational-routines]] — 進化経済学と組織ルーティン
- [[capability-overconfidence-and-cognitive-distortion]] — 能力過信による評価の系統的歪み

## 参考ソース

1. David Klotz (2026). *Smart Enough to Go Extinct? An Evolutionary Challenge to the Value of General Intelligence and Its Ethical Implications for AGI*.
   File: raw/papers/neuroscience/smart-enough-to-go-extinct-an-evolutionary-challenge-to-the-value-of-general-int.md
2. Yameng Hao, Hong Xu, Xiaoyi Li (2026). *Motivations in Chinese costume travel photography: An evolutionary psychology perspective*.
   File: raw/papers/neuroscience/motivations-in-chinese-costume-travel-photography-an-evolutionary-psychology-per.md
3. 민경권 (2026). *Can AI Be an Individual, a Mental Entity, and a Subject?*
   File: raw/papers/neuroscience/can-ai-be-an-individual-a-mental-entity-and-a-subject.md
