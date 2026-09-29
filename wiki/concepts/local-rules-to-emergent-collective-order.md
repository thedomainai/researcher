# 局所ルールと選別から創発する集団秩序とその操舵

## 概要

単純な局所相互作用、非線形性、選別圧が組み合わさると、個々の要素の設計には書かれていない集団的な秩序が立ち上がる。この秩序は、個々の要素を直接制御しなくても、環境への間接的な介入や上位レベルの制御によって方向づけられる。ただし、そのシミュレーション、検証、制御に必要な計算負荷は非線形に増大する。

AI Nativeな社会設計では、多数のAIエージェントと人間が相互作用する。全体の振る舞いを個別の指示だけで規定するのは現実的でなく、また規定できたとしても検証が追いつかない。そのため「何を局所ルールとし、何を環境や上位層で操舵し、どこまでを検証可能とするか」が設計上の中心課題になる。本記事は2026年の複雑系科学分野の論文群に基づき、この構造的原理を整理する。

## メカニズム

対象が人間、AI、組織、技術のいずれでも成立する構造として、次の4要素に整理できる。

1. **局所相互作用の非線形性**:各主体は近傍の情報や自らのルールだけで行動する。非線形な相互作用が重なることで、個々の単純なルールからは予測しにくい集団的パターンが生じる。
2. **スティグマジー(環境媒介の調整)**:主体同士が直接通信せず、共有環境(痕跡や場)を書き換え、それを読むことで間接的に調整する。この経路は外部から操舵する入口にもなる。
3. **自己組織化と選別**:ルールやシステムの候補を評価し、残すものと捨てるものを選別することで、より適応的で複雑なパターンが形成される。
4. **多時間スケール相互作用**:緩速な変数と高速な変数が交互に作用し、単一の時間スケールでは説明できない複雑な振動や構造が生まれる。

操舵の原理は「微視的な状態を指定せず、秩序パラメータ(集団レベルの指標)や環境場を通じて相転移の位置や秩序の出現を動かす」ことである。一方で、主体が複雑化(学習や推論能力の付与)するほど、検証と計算のコストは非線形に膨らむ。

## 理論的背景

**環境介入による操舵(蟻群モデル)**:Pitteriらは、蟻群モデルの機能的制御可能性の枠組みを提案している。強化学習で訓練したスティグマジー・エージェントの集団が、共有フェロモン場のみを通じて蟻に作用し、秩序ある行動の創発を促す。訓練は中央集権的訓練・分散実行の設定で行われ、報酬はトレイル状のフェロモン構造と、蟻の位置が高フェロモン経路に沿うことを促すよう設計され、特定の微視的配置の制御は要求しない。学習された方策は、系の大域的振る舞いを特徴づける相転移線を実効的に移動させる。

**場媒介の集団対称性破れの操舵(量子系)**:Westrickは、IBM Heron R2上の156量子ビットで、各量子ビットを個別のQITE制御器で調整しつつ、大域的な場結合を加える実験を報告している。秩序パラメータM = mean(p1) − 0.5は、ESP32-C3マイクロコントローラ上で各サイクルにオンチップ計算され、全エージェントの調整目標を集合的にシフトする。古典制御が量子多体系の集団的対称性破れを支配しうることを示す事例である。

**局所ルールと非線形性のMARLへの応用**:Zhangは、集団的創発理論(局所ルールと非線形相互作用)をマルチエージェント強化学習に適用する枠組みを提案する。個別エージェントの最適化に偏る従来手法に対し、環境と報酬関数を集団行動の創発を促すよう設計することを主張している。

**選別による自己組織化**:同じくZhangは、遺伝的アルゴリズムのような反復的な選別・改良の仕組みにより、単純なルールとフィードバックループから複雑で適応的なパターンを持つシステムを進化させる枠組みを論じている。ただし提示されている内容は方法論と予備的なアーキテクチャの提案の段階である。

**多時間スケールの力学**:Phan and Wangは、皮質ニューロンの3時間スケール生物物理モデルで、混合モード・バースト振動(MMBO)を、幾何学的特異摂動理論(GSPT)の3時間スケール版で分析した。従来の2時間スケール分析で個別に特定されていた機構を統一的に説明できるとしている。

**相互作用からの意味の創発**:Marghoubの計算プロセッサ存在論(CPO)は、意味をプロセッサ間のデータ交換から生じる相関構造として定式化する。20プロセッサのマルチエージェントシミュレーションでは、自由な情報交換により知覚誤差が4.6913から1.0533へ低下した(約4.45倍の精度向上)と報告されている。

**エージェント化に伴う検証負荷**:Blandoらは、Mesa製のエージェントベースモデル(Schelling分離モデルの拡張)にLLM駆動の判断を持つエージェントを混在させ、統計的モデル検査ツールMultiVeStAで分析している。中核的な知見は、学習エージェントを組み込むと計算負荷と検証難度が非線形に増加するという点である。

なお、線虫と揮発性有機化合物による害虫防除の研究(Chacon Hurtado)は、宿主選択が嗅覚・味覚の手がかりに駆動されるという行動操作の構造を示すが、農業という固有の制約に依拠するため、本原理の補助的な参照にとどまる。

## AI Nativeな設計への示唆

- **直接指示より環境設計**:個々のエージェントの内部を規定せず、共有環境(痕跡、場、報酬構造)を設計して秩序を誘導する。蟻群の事例は、微視的状態の制御なしに相転移線を動かせることを示す。
- **集団レベルの秩序パラメータを制御対象にする**:全体の状態を要約する指標を継続的に計測し、それを基準に調整目標を動かす。量子系の事例はこの構造を示す。
- **報酬・環境を創発が起きるよう設計する**:MARLでは個別性能の最大化だけでなく、集団的協調が生じる相互作用の形を設計に含める。
- **選別圧を明示的な設計要素とする**:何を残し何を淘汰するかが、生じる秩序の性質を決める。
- **時間スケールを分けて設計・分析する**:緩速な制度・方針の層と、高速なエージェント動作の層を区別し、それらの相互作用を前提に検証する。
- **検証コストを最初から見積もる**:エージェントの能力を高めるほど検証が非線形に難しくなるため、統計的モデル検査のような手法を設計工程に組み込み、どこにLLM等の複雑な判断を入れるかを選択する。

## 関連コンセプト

- [[emergent-order-and-narrative-attribution]] — 分散的相互作用からの秩序創発と事後的物語化
- [[interaction-emergent-coordination]] — 相互作用から創発する協調と逸脱の伝染
- [[strategy-as-simple-rules]] — シンプルなルールによる経営戦略
- [[decision-loops-and-layered-decentralized-control]] — 意思決定ループと分散アクティブ制御の多層構造
- [[unobservable-control-and-emergent-collusion-limits]] — 可観測性・制御の原理的限界と創発的暗黙協調のリスク
- [[bounded-diversity-adaptive-feedback-collectives]] — 限定的多様性と適応的フィードバックによる集合知
- [[emergent-governance-networks]] — 創発的ガバナンスネットワーク
- [[institutional-steering-of-ai-competition]] — AI競争の制度的ステアリング
- [[organizational-change-approaches]] — 計画的変革と創発的変革の統合
- [[evidence-grounded-role-separated-agent-coordination]] — 根拠中心・役割分離型のエージェント協調と検証の構造的分離

## 参考ソース

1. Towards Agentic Agent-based Models: Feasibility, Performance, and Statistical Model Checking — Stefano Blando, Emanuele Guerrazzi, Riccardo Porcedda, Giuseppe Squillace, Max Tschaikowski (2026)
   - File: raw/papers/complexity_science/towards-agentic-agent-based-models-feasibility-performance-and-statistical-model.md
2. Ant swarm functional control via stigmergic Reinforcement Learning agents — Alessio Pitteri, Andrea Guizzo, Laura Ferrarotti, Bruno Lepri, Riccardo Gallotti (2026)
   - File: raw/papers/complexity_science/ant-swarm-functional-control-via-stigmergic-reinforcement-learning-agents.md
3. Experimental Demonstration of Steerable Emergence on 156 Qubits: A Microcontroller Governs Collective Symmetry Breaking on IBM Heron R2 — Bernd Westrick (2026)
   - File: raw/papers/complexity_science/experimental-demonstration-of-steerable-emergence-on-156-qubits-a-microcontrolle.md
4. Mixed-mode bursting oscillations in a three-timescale biophysical neuronal oscillator model — Ngoc Anh Phan, Yangyang Wang (2026)
   - File: raw/papers/complexity_science/mixed-mode-bursting-oscillations-in-a-three-timescale-biophysical-neuronal-oscil.md
5. Algorithmic Self-Organization of Complex Systems — Jincheng Zhang (2026)
   - File: raw/papers/complexity_science/algorithmic-self-organization-of-complex-systems.md
6. Collective Emergence in Multi-Agent Reinforcement Learning — Jincheng Zhang (2026)
   - File: raw/papers/complexity_science/collective-emergence-in-multi-agent-reinforcement-learning.md
7. Entomopathogenic Nematodes and Volatile Organic Compounds to Control Wireworms — Jeimy Andrea Chacon Hurtado (2026)
   - File: raw/papers/complexity_science/entomopathogenic-nematodes-and-volatile-organic-compounds-to-control-wireworms.md
8. Computational Processor Ontology (CPO): Mathematical Formulation of Operational Time, Emergence of Meaning, and Error Dynamics in Multi-Agent Systems — Vahid Marghoub (2026)
   - File: raw/papers/complexity_science/computational-processor-ontology-cpo-mathematical-formulation-of-operational-tim.md
