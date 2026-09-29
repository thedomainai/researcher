# 分解による情報保持の数理的限界と収穫逓減

## 概要

大きなタスクを木構造の階層やエージェントのアンサンブルに分割すると、文脈が小さくなる、責務が分離される、並列化できるといった利点が得られる。しかしソース [1] は、この分割が「葉が発見した内容のうち、どれだけが根に届くか」を必ず変えると指摘する。分解は整合性(integrity)をもたらすが、収量(yield)は増やさない。

ソース [2] は別の角度から同じ構造を示している。アンサンブルに加えるモデルを増やすほど、追加1つあたりの利得(Benefit Yield Function)は逓減し、やがてゼロを切って全体性能が劣化に転じる。

この2つを合わせると、「深さに応じた情報損失」と「規模に対する収穫逓減」は設計上の工夫では消せない不変原理だと言える。AI Nativeな組織設計では、エージェントを増やす・階層を深くするという直感的な拡張が、どこで損失に転じるかを定量的に見積もる必要がある。

## メカニズム

この構造は、対象がLLMエージェントでも人間の組織でも成立する形で整理できる。

1. **分割と選別**:上位の主体が b 個の項目を受け取ると、そのうち一部しか次の層へ渡さない。ソース [1] では、b 項目を受けた主体が任意の1項目を保持する確率を r(b) とモデル化している。
2. **層ごとの乗算的な損失**:保持は各階層で繰り返されるため、深さが増すほど残存量は掛け算で減る。
3. **タスク規模とアーキテクチャの分離**:r(b)=C·b^(-δ) の場合、深さ k の木が N 個の知見から生む収量は C^k · N^(1-δ) になる。規模 N に依存する項(指数 δ)と、構造に依存する項(層ごとの C ≤ 1)が分かれる。
4. **構造が寄与できる範囲**:構造が寄与するのは層あたり C ≤ 1 だけであり、収量だけを見れば平坦(flat)な構造が最適になる。どんなエージェント配置でも指数 δ は回避できない。
5. **規模の上限**:アンサンブルでも、追加要素の限界利得が正から負へ交差する点(implosion threshold θ*)が存在し、最適規模はそこで頭打ちになる。

したがって整合性と収量はトレードオフの関係にある。整合性を得る仕組みを重ねるほど、通過する情報は絞られる。

## 理論的背景

### 情報保持率のモデル(ソース [1])

- r(b)=1/b のとき、あらゆるタスク規模・あらゆる木の形状で、ちょうど1つの知見だけが届く。著者らはこれを20,000本のランダムな不規則木で 2.4×10^-15 の精度まで検証したと報告している。
- r(b)=C·b^(-δ) のときは前述の C^k N^(1-δ) となる。
- 実証として、本番の deep-research トレース600件から δ = 0.34 [0.30, 0.38] が、互いに失敗モードを共有しない3通りの同定で得られている。
- 項目境界がテキストのヒューリスティクスではなくツールから与えられ、b=1 が550回現れるホップでは、C = 0.571 [0.527, 0.615] が外挿ではなく観測値として得られている(16,082ホップ)。

なお、ソース抜粋はここで途切れており、これ以降の結果や結論は本記事では扱わない。

### ベネフィット収量関数と崩壊閾値(ソース [2])

ソース [2] は、多数のLLMを構造化された検索コーパスとみなす Universe of Universes (UoU) フレームワークを提案している。中心的な貢献は、アンサンブルにモデルを1つ追加したときの限界的な性能向上である Benefit Yield Function (BYF) の形式的な特徴づけと、BYF がゼロを横切る点である implosion threshold θ* の同定である。従来のLLMアンサンブルや mixture-of-agents は出力を集約するが、モデル全体の宇宙にわたって性能をアンサンブル規模 N の関数として調べてはいなかった、と位置づけている。

なお、θ* の具体的な数値や、δ と C の組み合わせによる最適規模の導出式は、提示された抜粋には含まれていない。

### 周辺的な知見

- ソース [3] は、多様なエージェントの推論が共有された誤りを増幅しうる点を扱い、異なる因子分解(順方向と逆方向のベイズ推論)による相関誤差の軽減を論じている。
- ソース [4] は、役割分担と論証・反論によって曖昧な推論を構造化できることを示している。構造化は精度に寄与するが、それは整合性側の利得である。
- ソース [5] は、階層的な Manager-Worker や Router 型の通信では自律性が制限され、誤ルーティングが誤りを伝播させうると指摘し、共有チャネル(Bus)による代替を提案している。

## AI Nativeな設計への示唆

- **収量が目的なら平坦にする**:分解の理由が「文脈を小さくする」「見通しを良くする」といった経験則だけなら、その根拠は弱い。深さは層ごとに C ≤ 1 の損失を課すため、深くする理由は整合性の確保に限定して明示する。
- **δ と C を計測する**:自組織のパイプラインで、各ホップに渡る項目数と保持数を記録し、δ と C を推定する。ソース [1] のようにツール由来の項目境界を使うと、推定が安定する。
- **アンサンブルには上限を置く**:エージェントやモデルの追加は、BYF が正である範囲に留める。追加コストを払う前に限界利得を測り、θ* を超えないようにする。
- **整合性と収量を分けて評価する**:分解の効果を「品質が上がった」の一語で評価せず、整合性(誤りの抑制・責務の分離)と収量(根まで届いた知見の量)を別指標にする。
- **損失を可視化する**:階層を通過して落ちた情報を記録し、人が後から参照できるようにする。集約が不一致や曖昧さを隠す問題は関連概念でも扱われている。
- **通信構造の見直しは補助策と考える**:ソース [5] のようなバス型通信は自律性と調整の両立に役立つ可能性があるが、ソース [1] の論理では、配置の工夫で指数 δ は変えられず、改善できるのは C の側に限られる。

## 関連コンセプト

- [[aggregation-induced-information-loss]] — 集約で情報が失われ不一致が見えなくなる問題。階層伝播の損失と直接つながる。
- [[homogeneous-multi-agent-debate-limits]] — 同質なエージェントを増やしても得られる利得に限界とコストがあること。
- [[decision-node-decomposition-and-bounded-relocation]] — 意思決定ノードの分解と限定合理性の再配置。
- [[evidence-obligation-and-ambiguity-retention-in-autonomous-systems]] — 曖昧性や証拠を保持する設計。
- [[local-information-limits-and-decentralized-guarantees]] — 局所情報下での分散協調に伴う不可避な性能限界。
- [[computational-limits-forcing-decentralized-autonomy]] — 中央集約の限界が分散化を強いる点。
- [[stigmergic-self-organization-of-organizational-structure]] — 課題に応じた組織構造の設計。
- [[responsibility-dilution-and-moral-status-symmetry]] — 多主体チームでの責任の希薄化。
- [[llm-capabilities-and-limits]] — LLM単体の能力と限界。
- [[long-horizon-emergent-failure-and-feedback-coupling]] — 長期の相互作用で生じる創発的失敗。

## 参考ソース

1. Decomposition Buys Integrity, Not Yield — Rong He (2026)
   File: raw/papers/complexity_science/decomposition-buys-integrity-not-yield.md
2. The Universe of Universes: Benefit Yield Functions, Implosion Thresholds, and Infrastructure-Aware Optimization in Multi-LLM Systems — Danielle Franklin, Vasu Raj Jain (2026)
   File: raw/papers/complexity_science/the-universe-of-universes-benefit-yield-functions-implosion-thresholds-and-infra.md
3. When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making — Ken Chen, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge (2026)
   File: raw/papers/complexity_science/when-agents-disagree-bayesian-backward-reasoning-as-a-label-free-anchor-for-mult.md
4. Who Are They to Each Other? Multi-Agent Reasoning for Speaker Relationship Inference — Yaohan Guan, Yen-Ju Lu, Yuzhe Wang, Junhyeok Lee, Jesus Villalba (2026)
   File: raw/papers/complexity_science/who-are-they-to-each-other-multi-agent-reasoning-for-speaker-relationship-infere.md
5. BusMA: A Bus Communication Substrate for Multi-Agent Systems — Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras (2026)
   File: raw/papers/complexity_science/busma-a-bus-communication-substrate-for-multi-agent-systems.md
