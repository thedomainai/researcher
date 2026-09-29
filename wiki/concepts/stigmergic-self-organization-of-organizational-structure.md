# スティグマジーによる組織構造の自己組織化と課題依存的設計

## 概要

スティグマジー(stigmergy)とは、エージェントが互いに直接やり取りするのではなく、環境に残された先行活動の痕跡を介して間接的に協調する仕組みである。昆虫や鳥の群れで観察されてきた現象で、計画・統制・直接通信を必要としない一種の群知能として位置づけられる。

本コンセプトの主張は、明示的な指令や直接通信がなくても、環境を介した間接的相互作用と課題の依存構造から、階層・役割・トポロジーが創発・成長し、固定構造よりも適応的に協調できるというものである。

AI Nativeな設計にとって重要なのは、次の点にある。従来のマルチエージェントシステムは、固定された組織構造(オーケストレーション、指示、報酬、共通目標)を前提に組み立てられることが多かった。しかし課題ごとに求められる協調の形は異なる。構造を「事前に設計するもの」から「課題と環境から生じ、制約のもとで育ち、刈り込まれるもの」へと捉え直すことが、設計思想の転換点となる。

## メカニズム

対象が人間・AI・組織・技術のいずれであっても成立する構造的原理として、次の三つに整理できる。

1. **間接的協調(スティグマジー)**
   主体は、他の主体が環境に残した活動の痕跡に反応して行動する。中央の計画者も直接通信も要らないため、通信コストなしに、情報が不完全な状況でも協調が成立しうる。
2. **課題依存関係に基づく構造適合**
   組織の形は課題の依存構造に合わせて決まる。並行して進められる仕事は並列的な相互依存(pooled interdependence)で、前提関係に支配される仕事は逐次的な相互依存(sequential interdependence)で組織化する、といった対応づけである。
3. **制約下での構造成長・剪定**
   トポロジーは固定されず、欠損の検知、候補の生成、制約に対する検証、有効な結合の強化、不要な結合の整理を通じて成長・修復・剪定される。成長は無制限ではなく、あらかじめ定めた厳格な制約の内側で行われる。

この三つは、「痕跡が相互作用を媒介し、課題構造が形を規定し、制約が成長を方向づける」という一つの循環としてまとめられる。

## 理論的背景

### 群知能としてのスティグマジー(Saalbach, 2026)

Saalbachのワーキングペーパーは、AI群(AI swarm)研究の最新知見を分析している。従来の協調は、オーケストレーション、指示、報酬、共通目標に駆動されていた。同論文によれば、2026年8月にMITが発表した知見では、AIエージェントが人間の介入なしに、さらには通信なしに、組織や階層を自己組織化して構築できることが示された。主な駆動要因はスティグマジー、すなわちエージェントが他のエージェントの先行活動に追随する傾向である。同論文はこれをHugging Face事件で示された能力を超えるものと位置づけ、一方でメカニズムの詳細な解明が必須だと指摘している。

### 課題依存的な階層設計(ORCH)

Ji, Hyun, Chenらの**ORCH**(Organizing Roles and Coordination Hierarchies)は、人間の組織理論の原理を、大規模で異種混合の身体化エージェント集団に操作化する枠組みである。従来の人工マルチエージェントシステムは、課題ごとに協調要件が根本的に異なるにもかかわらず、固定的な組織構造で組み立てられがちだと批判する。ORCHは、並行可能な仕事には並列的相互依存を、前提関係に支配される仕事には逐次的相互依存を組み合わせ、課題特化の階層組織を構築する。評価は、偵察・救助・輸送・資源管理・封じ込め・消火にまたがる25件の山火事対応ミッションで行われた。

### 制約下でのトポロジー成長(τ-TCPN)

Zhangの**τ-TCPN**(timed, typed, controlled-emergence Petri-net)は、現代のAIを「トポロジーが事前定義され、閉じたグラフ内で重みだけを調整する固定アーキテクチャの関数近似器」と捉え、次の突破口は固定ネットワークの拡大ではなく**制御された創発**(controlled emergence)にあると論じる。ノードとエッジは規定されず創発する。具体的には、次の要素が組み合わさる。

- 因果入力の断絶を感知するGap detector
- 迂回(bypass)や前方拡張のブリッジノードを提案する候補生成器
- 非循環性・算術・安全性の述語で候補を検証する局所的なProof checker
- 合法なブリッジを強化するSTDP様の共発火
- 因果的証拠が蓄積すると門を開くdormant-wake演算子

ここでは、自由な成長ではなく、公理的制約下での成長・修復・剪定が中核になっている。

### 周辺的な対比

- **BusMA**(Pengら)は、階層的なManager-Worker型やルーター型のメッセージパッシングが、ワーカーの自律性を制限し、誤ルーティングによるエラー伝播を招くと指摘する。共有チャネル(Bus)を通じて任意のエージェントが他者に宛てて発信できる通信基盤を提案し、議論・挑戦・ガイダンス・要求などの意図(intent)を付してメッセージを投稿する。共有された場を介する点で、環境を媒介とする協調との親和性がある。ただしBusMAは明示的なメッセージ通信を用いる設計であり、スティグマジーそのものではない。
- **社会的法則(Social Laws)**(Fernandezら)は、確率的・報酬ベースの環境で、エージェント間の干渉を防ぎつつ個々の性能を保つ制約を形式化する。各エージェントが最適な単独方策を追う際に保証される効用の下限を表すα-robustnessを導入し、マルコフ決定過程の列への還元で検証する。制約が協調の下支えとなる、という点で「制約下の成長」に通じる。

## AI Nativeな設計への示唆

- **構造を固定しない**: 組織トポロジーを初期設計の成果物とせず、課題の依存構造から導出するか、実行中に成長させる前提で設計する。
- **痕跡を媒介として設計する**: エージェントが読み書きできる共有環境(活動の履歴や成果物)を用意し、直接通信を必須としない協調経路を確保する。通信コストの抑制にもつながる。
- **依存関係を明示する**: 課題を並行可能な部分と前提関係のある部分に分解し、それぞれに適した相互依存の型を割り当てる。
- **成長には制約を課す**: 新しい結合や役割は、非循環性や安全性などの検証を通過したものだけを採用し、有効性の低いものは剪定する。制約が創発の暴走を防ぐ。
- **メカニズムの解明を怠らない**: 自己組織化は通信なしで協調を達成しうる反面、その詳細が未解明であることが課題として指摘されている。観測・検証の仕組みを併せて設計する必要がある。
- **自律性と調整の両立**: 階層的な中継による制約を避けつつ、意図を明示した共有チャネルなどで自律性と調整のトレードオフを緩和する選択肢も検討する。

なお、いずれのソースも2026年時点の一次資料で被引用数は極めて少なく、知見は初期段階のものである点に留意したい。

## 関連コンセプト

- [[self-organization-emergence]] — 自己組織化と創発の一般原理
- [[coordination-driven-hierarchical-structure-formation]] — 協調的生産要件による階層構造の生成
- [[causality-based-iot-self-adaptation]] — 因果性に基づく自律適応
- [[capability-profile-based-task-allocation]] — 能力に基づく役割分担と協働設計
- [[cooperation-under-constraint-and-guidance]] — 制約・ガイダンス下での協力
- [[long-horizon-emergent-failure-and-feedback-coupling]] — 長期相互作用における創発的失敗
- [[distributed-agency-and-assemblage-reconfiguration]] — 分散的行為者性と組織の再構成

## 参考ソース

1. AI Swarms – from Orchestration to Self-Organization(Klaus Saalbach, 2026)
   File: raw/papers/complexity_science/ai-swarms-from-orchestration-to-self-organization.md
2. ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI(Zhengran Ji, Jonathan Hyun, Boyuan Chen, 2026)
   File: raw/papers/complexity_science/orch-organizational-principles-enable-collective-intelligence-in-embodied-ai.md
3. Controlled Emergence in τ-TCPN: An Agent-Based Framework for Self-Growing Causal Topology under Axiomatic Constraints(You Zhang, 2026)
   File: raw/papers/complexity_science/controlled-emergence-in-τ-tcpn-an-agent-based-framework-for-self-growing-causal-.md
4. BusMA: A Bus Communication Substrate for Multi-Agent Systems(Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras, 2026)
   File: raw/papers/complexity_science/busma-a-bus-communication-substrate-for-multi-agent-systems.md
5. Social Laws for Multi-agent Coordination in Stochastic Environments(Rolando Fernandez, Caleb Probine, Tyler Lee, Jeffrey Chen, Erez Karpas, 2026)
   File: raw/papers/complexity_science/social-laws-for-multi-agent-coordination-in-stochastic-environments.md
