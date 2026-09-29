# 合意超過分への信用割当と統合位置の設計

## 概要

合意超過分への信用割当と統合位置の設計とは、協調学習において「どの信号を集団で統合し、どの調整を個別に保つか」を設計し、さらに「集団の平均(合意)を超える貢献」を明示的に最適化する原理である。

協調学習の設計には二つの問いがある。第一に、信用(advantage)をどの範囲で集約するか。第二に、方策更新の安定化に使う確率比(ratio)をどの単位で構成するか。第三に、各メンバーの報酬を「正解を再現できたか」で測るのか、「集団の合意より良くなったか」で測るのか。ここで不適切な設計をすると、全員が同じ答えを再生産する冗長な集団になるか、逆に協調に必要なグローバル情報が失われる。

AI Nativeな社会では、複数のAIエージェントや人間が役割を分担して働く。その際、「全体の成果をどう各主体に帰属させるか」「更新や調整をどこで束ねるか」は、組織設計そのものである。本概念は、エージェント学習の具体的な知見を、この設計問題に適用できる不変原理として整理する。

## メカニズム

対象がAIエージェント、人間、組織、技術のいずれでも成り立つ構造として、次の三つに整理できる。

### 1. 全体信号は統合し、個別調整は分離する(集約位置の非対称性)

協調にはグローバルな情報が必要だが、その情報は「評価信号(信用)」の側に入れるのが適切であり、「実際の更新や調整の単位(比率)」の側では各主体に保つ。評価は全体を見て、動きは各自の持ち場で行うという分業である。両方を同じ粒度で統合したり、両方を分離したりするのは、それぞれ極端な配置の一つにすぎない。

### 2. 平均からの超過を報酬にする

主体の評価を「正解を出したか」ではなく、「集団の合意水準に対してどれだけ上積みしたか」で定義する。集団の平均をベースラインとして差し引くことで、平均をなぞるだけの行動には報酬が生じなくなる。結果として、集団は冗長化せず、平均を超える貢献が選択される。

### 3. ベースラインの動的・役割条件付き設計

ベースラインは固定値ではなく、事例ごと・役割ごとに変わる。難しい問いでは合意水準が低く、易しい問いでは高い。動的に基準を置くことで、貢献の大きさが状況に応じて公平に測られる。

## 理論的背景

### 集約の二軸分析

Zhao & Li(2026)は、協力的マルチエージェント方策最適化(PPO系)における集約の設計を、二つの軸で整理している。一つは advantage(どのエージェントの報酬が信用信号に寄与するか)、もう一つは ratio(どのエージェントの尤度比がクリップ付き重要度重みを構成するか)である。既存手法はこの二軸上の散在した点を占めるとされる。

- IPPO: 両方を個別に扱う
- MAPPO: チーム単位の advantage と、エージェントごとの ratio を組み合わせる
- HAPPO: 逐次的な ratio と、エージェントごとの advantage を用いる
- 因子化された同時方策に対する単一エージェント縮約: 両方を集約する系統

この分析は、信用割当(advantage)は全体で統合し、確率比(ratio)は個別に配置するのが情報理論的に最適であると結論づける。これが本概念の中核となる「集約位置の非対称性」である。

### 合意超過分の最適化

Pulici ら(2026)のMADA-RLは、4B以下のコンパクトモデルを生成役(generator)と批評役(critic)に専門化し、LoRAアダプタで少数のパラメータのみを微調整する事後学習枠組みである。中核は「反事実的な批評者 advantage」で、批評者の advantage を「その報酬から、生成者アンサンブルの事例ごとの正解率を引いたもの」と再定義する。これは動的かつ役割条件付きのベースラインであり、批評者に「正解を再現すること」ではなく「生成者の合意を上回って改善すること」を最適化させる。計算制約下のマルチエージェント学習では、見解の平均からの超過改善を明示的に最適化すべきだという知見につながる。

### 複数の専門化の動的統合

Zeng ら(2026)のMixture of Roles(MoRe)は、複数の専門化を単一のステアリングベクトルへ適応的に合成し、単一ターン推論で多視点の問題解決を得ようとする。ステアリングベクトルのコードブックが潜在的な役割を符号化し、クエリ対応ルーターが動的に組み合わせる。マルチエージェントシステムで多ターンのやり取りにより統合すると文脈長と推論コストが膨らむ、という問題への対処である。ここでは「どこで統合するか」の位置が、対話の中から単一モデル内部へ移されている。

### 集団的創発

Zhang(2026)は、局所的ルールと非線形相互作用という集団的創発の原理をMARLの環境・報酬設計に反映させ、集団行動の創発を促す枠組みを提案する。従来のMARLが個々のエージェントの性能最適化に偏り、システム全体の知性を制限しうるという問題意識である。報酬設計で集団レベルの振る舞いを誘導するという点で、合意超過分への信用割当と問題意識を共有する。

## AI Nativeな設計への示唆

1. **評価は全体視点、更新は現場単位で設計する。** チーム全体の成果を評価信号に反映しつつ、各エージェントや担当者の調整権限と更新単位は局所に残す。評価と権限の粒度を意図的に非対称にする。
2. **個人ではなく「平均に対する上積み」を評価する。** 複数のAIが同じ問題に取り組む場合、合意と同じ答えを返すだけの主体には高い評価を与えない。合意を超えて改善した部分を貢献として認識する。
3. **ベースラインを事例・役割ごとに動的に置く。** 一律の基準ではなく、その課題での集団の水準を基準にする。批評役や検証役には、生成役の合意水準を基準にした評価を与える。
4. **計算制約下では専門化と統合位置を併せて設計する。** 小型モデルの役割分化(生成・批評)や、単一モデル内での役割合成のように、統合をどの層で行うかがコストと性能を左右する。
5. **冗長化と過度な統合を警戒する。** 統合を強めるほど個別の不一致が見えなくなる。集約を導入する際は、失われる情報を意識して設計する(→ 関連コンセプト参照)。

なお、上記のうち3〜5は、ソースの知見を組織・運用設計に敷衍した指針であり、ソース自体が組織設計を実証したわけではない。

## 関連コンセプト

- [[aggregation-induced-information-loss]] — 集約が不一致を不可視化する問題。統合位置の設計で何を統合し何を残すかと直結する
- [[multi-agent-collaboration-and-group-dynamics]] — 協調における合意形成のダイナミクス。本概念の「合意」を超える貢献という視点の背景となる
- [[evidence-grounded-role-separated-agent-coordination]] — 生成と検証の役割分離。生成役と批評役の専門化と対応する
- [[local-rules-to-emergent-collective-order]] — 局所ルールから創発する集団秩序。報酬設計による集団行動の操舵と関連する
- [[decision-loops-and-layered-decentralized-control]] — 意思決定ループと多層の分散制御。全体信号と個別調整の階層配置と関連する
- [[self-monitoring-feedback-and-adaptive-plasticity]] — 内部状態の自己監視。動的ベースラインによるフィードバックと通じる
- [[unobservable-control-and-emergent-collusion-limits]] — 創発的な暗黙協調のリスク。合意への収束や協調設計の限界を考える際の対概念

## 参考ソース

1. Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov, Zifeng Ding, Volker Tresp (2026). "MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient Reasoning in Compact Models"
   File: raw/papers/complexity_science/mada-rl-multi-agent-debate-aware-reinforcement-learning-for-parameter-efficient-.md
2. Zijian Zhao, Sen Li (2026). "Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization"
   File: raw/papers/complexity_science/aggregate-in-the-advantage-not-the-ratio-a-canonical-form-analysis-of-cooperativ.md
3. Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu (2026). "One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles"
   File: raw/papers/complexity_science/one-model-many-minds-unlocking-multi-agent-synergy-in-a-single-agent-via-mixture.md
4. Jincheng Zhang (2026). "Collective Emergence in Multi-Agent Reinforcement Learning"
   File: raw/papers/complexity_science/collective-emergence-in-multi-agent-reinforcement-learning.md
