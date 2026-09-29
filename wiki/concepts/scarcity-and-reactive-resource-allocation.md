# 希少性と観測に基づく反応的資源配分

## 概要

希少性(scarcity)は経済学の「メタ前提」であり、古典的には「有限な資源と無限の欲求」と定義される。本コンセプトは、この相克が人間経済に固有のものではなく、AIシステムや計算システムにも構造的に成立することを出発点とする。有限な資源に対して需要や内部状態が事実上無限であり、しかもその需要が事前に予測できない場合、事前最適化(予測に基づく計画)よりも、実行時に観測した状態へ反応して配分する方式が根本的なメカニズムになる。

AI Nativeな社会設計にとってこの原理が重要なのは、次の理由による。

- 人間・AIエージェント・計算基盤が混在する系では、需要の不規則性と異質性が常態になる。
- LLM推論のように、コストが本質的に予測困難な処理が増えている。
- 対象を入れ替えても成立する不変原理として、設計判断の土台にできる。

## メカニズム

構造は次の三要素で整理できる。対象が人間・AI・組織・技術のいずれでも同じ形で成り立つ。

1. **有限資源と無限需要の相克**
   資源(計算能力、電力、注意、時間など)は有限である一方、需要側の状態や欲求は際限なく広がる。ソース[1]は、この構図を人間系では「有限な資源と無限の欲求」、AI系では「有限な資源と無限の内部状態」として対応づけている。
2. **観測に基づく反応的制御**
   将来の需要を過去データから予測して配分するのではなく、実行時に観測できる情報に応じて配分を調整する。予測が「脆い」あるいは原理的に不可能なワークロードでは、この方式が現実的な選択肢となる(ソース[2])。
3. **異質主体への最適割当**
   資源を受け取る主体は均一ではない。異質なエージェント間でタスクをどう割り当てるかは、対象を問わず繰り返し現れる問題である(ソース[3])。

この三要素は、「制約の存在」「需要の予測不能性」「主体の異質性」という前提の下で、「観測して反応し、主体の違いに合わせて割り当てる」という一つの設計様式にまとまる。

## 理論的背景

### AI-AI Scarcity(AASc)

ソース[1]は、サイバネティクスと情報理論の観点から希少性の構成要素を分析している。

- 第1章で、5人の古典的経済学者の定義から希少性を構成する7つの中核要素を抽出し、いずれも伝統的経済学では厳密な構造的定義を受けていないと論じる。
- 第2章で、Human-Human Fundamental Axiom(HHFA)を出発点に、Gan's Black-Box Structure Model(GBS)とPointing Alignment Model(PAM)を導入し、7要素を再定義して人間間希少性(HHSc)の枠組みを再構築する。
- 第3章で、7要素を人間系から人工知能系へ移し、AAScの中核定式「限られた資源と無限の内部状態」を提示する。

ここから、経済の根底的制約が人間固有のものでなくAIシステムにも成立するという見方が得られる。なお、抜粋はAbstractの途中までであるため、その先の主張の詳細は本記事では扱わない。

### 予見なきスケジューリング

ソース[2]は、資源需要を事前に知り得ないワークロードを扱う。背景として次が挙げられている。

- ワークロードが異質で不規則になっている。
- 根本的に異なる実行モデルがパイプライン内で混在している。
- 電力制約により、ピーク需要に合わせた単純な確保ができず、厳しい資源枠内で動かす必要がある。
- LLM推論のような生成AIサービスでは、計算コストが本質的に予測不能である。

既存システムは、過去の挙動から将来需要を予測できると仮定するか、観測可能な情報を捨てて適応を放棄するかのどちらかだと指摘される。そのうえで、過去データから将来需要をモデル化する代わりに、実行時に観測できる情報に依拠する代替案が主張されている。抜粋はここで途切れており、具体的な手法の詳細は確認できない。

### 異質エージェントへの割当

ソース[3]は、異質なマルチロボットシステムにおけるタスク割当を、LLMとローカルサーチのハイブリッド手法で扱う論文である。異質エージェントへの最適割当は不変の問題だが、LLMハイブリッドという手法自体は技術特定的である、と位置づけられる。抜粋にAbstractの本文は含まれていないため、手法の詳細や実験結果は本記事では述べない。

### 人間側の含意

ソース[4]は、AIがルーティンで狭いタスクを自動化するにつれ、経済的・戦略的プレミアムが、複雑なシステムを統括し、多分野の知識を統合し、批判的判断を下せるジェネラリスト(「アーキテクト」)へ移ると論じる。配分を設計・監督する統合的判断の価値が相対的に上昇する、という読み方ができる。

## AI Nativeな設計への示唆

- **予測を前提にしない設計**: 需要が予測不能な領域では、精緻な予測モデルより、観測可能な信号を取得し配分へ反映する仕組みを優先する。
- **観測情報を捨てない**: 観測可能な情報を無視して適応を放棄する設計は避ける(ソース[2]の指摘)。
- **ピーク前提の確保に頼らない**: 電力などの制約下では、ピーク需要を見込んだ過剰確保ではなく、資源枠内での動的な配分を基本とする。
- **異質性を明示的に扱う**: 主体ごとの能力差を前提に、タスクを割り当てる仕組みを設ける。人間とAIの役割分担にも通じる。
- **統合的判断を担う役割の確保**: 自動化が進むほど、系全体を見渡して配分方針を判断する役割が重要になる(ソース[4])。
- **原理としての位置づけ**: 特定の手法(例: LLMとローカルサーチの併用)は技術に依存するため、変わりうる実装と、変わらない原理を区別して設計する。

## 関連コンセプト

- [[capability-profile-based-task-allocation]] — 異質な主体への能力に応じた割当という観点で直接関係する。
- [[metacognitive-allocation-under-finite-resources]] — 有限な認知資源の配分という、人間側の希少性の表れ。
- [[costly-verification-allocation-tradeoff]] — 検証コストという制約下での配分判断。
- [[contextual-intelligence-allocation]] — 文脈に応じた知能の配分。
- [[decentralized-coordination-and-power-concentration]] — 分散した配分・協調の力学。
- [[resource-based-view]] — 資源を軸にした組織分析の視点。

## 参考ソース

1. AI-AI Scarcity (AASc) — guoguang gan, 2026 — `raw/papers/complexity_science/ai-ai-scarcity-aasc.md`
2. Scheduling Without Foresight: Reactive, Observation-Based Runtime Scheduling Systems for Unpredictable Workloads — Jianru Ding, 2026 — `raw/papers/complexity_science/scheduling-without-foresight-reactive-observation-based-runtime-scheduling-syste.md`
3. Agentic Task Allocation for Heterogeneous Multi-Robot Systems: A Hybrid LLM and Local Search Approach — H M Zhang, Shengkang Chen, Ziyi Xia, Huan Yin, Fumin Zhang, 2026 — `raw/papers/complexity_science/agentic-task-allocation-for-heterogeneous-multi-robot-systems-a-hybrid-llm-and-l.md`
4. Management Talks – Part 3: Artificial Intelligence, Human Adaptability, and the Future of Decision-Making — Partha Majumdar, 2026 — `raw/papers/complexity_science/management-talks-part-3-artificial-intelligence-human-adaptability-and-the-futur.md`
