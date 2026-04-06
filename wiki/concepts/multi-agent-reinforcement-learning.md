# マルチエージェント強化学習

## 概要

マルチエージェント強化学習（Multi-Agent Reinforcement Learning、MARL）は、複数の自律的なエージェントが共有環境の中で相互に作用しながら、各自の方策（ポリシー）を学習する強化学習の拡張フレームワークである。単一エージェントの強化学習とは異なり、MARLでは複数のエージェントが同時に環境と相互作用するため、環境自体が他のエージェントの行動によって変化するという非定常性の問題が生じる。

MARLが重要視される理由は、現実世界の多くの問題が本質的に複数の意思決定主体を含むためである。スマートグリッドの電力管理、自律走行車の協調制御、金融市場のシミュレーション、ロボット群の協調行動など、単一エージェントでは解決困難な複雑系問題に対して強力なアプローチを提供する。また、協調・競合・混合といった様々なエージェント間関係を扱える柔軟性も、その重要性を高めている。

---

## 詳細

### 基本的な問題設定

MARLにおける環境は、一般に**マルコフゲーム**（Markov Game）または**確率ゲーム**（Stochastic Game）として定式化される。各エージェントは自身の観測に基づいて行動を選択し、環境から報酬を受け取り、価値関数（Value Function）や方策を更新する。エージェントが環境全体を観測できない場合は、**分散部分観測マルコフ決定過程**（Decentralized Partially Observable Markov Decision Process、DEC-POMDP）として定式化されることが多い。

例えば、再生可能エネルギーを活用するマイクログリッドコミュニティにおけるP2P（Peer-to-Peer）電力取引の研究では、各マイクログリッドの意思決定プロセスがDEC-POMDPとして定式化され、MARLによって解かれている。各マイクログリッドは自己の経済的利益を追求しつつ、市場運営者は低炭素排出というコミュニティ全体の社会的厚生を最大化するという、協調と自己利益が共存する構造が扱われている。

### 協調型MARL

協調型MARLでは、エージェントが共通の目標に向けて協力して学習を行う。分散学習においては、各エージェントが近傍エージェントとの通信を通じて価値関数や方策の更新情報を共有することが一般的である。

分散Q学習（Distributed Q-Learning）はその代表的な手法であり、エージェントが通信ネットワークを介して最適価値関数を協調的に学習する。ただし、実際の分散環境では通信ネットワークの信頼性が保証されない場合があり、これが重要な研究課題となっている。

### ビザンチン耐性MARL

現実の分散システムでは、一部のエージェントやエッジ（通信リンク）が悪意のある攻撃や故障によって誤った情報を送信する可能性がある。このような攻撃主体を**ビザンチン故障**（Byzantine Fault）と呼ぶ。

Lee と Panagou (2026) による研究では、ビザンチン攻撃に対して完全に耐性を持つ分散マルチエージェントQ学習アルゴリズムが提案されている。従来の耐性MARLアプローチは以下のいずれかの限界を抱えていた：

- 最適に近い（near-optimal）価値関数への概収束しか保証できない
- 最適解への収束を保証するために過度に制限的な仮定が必要

この研究の核心的なアイデアは、**冗長性に基づくフィルタリング機構**（Redundancy-based Filtering Mechanism）である。具体的には、2ホップ先の近傍エージェントの情報を活用して受信メッセージを検証し、双方向の情報フローを維持しながらビザンチン攻撃を排除する。また、アルゴリズムの収束に必要な新たなトポロジー条件とそのネットワーク構築の体系的手法も提示されている。

### 公平性と多目的MARL

現実のMARLシステムでは、単一の目標ではなく複数の目的を同時に最適化する必要がある場面が多い。**協調型多目的MARL**（Cooperative Multi-objective MARL）では、エージェント間の公平性（Fairness）が重要な設計指標となる。

Chouaki らの研究は、期待効用（Expected Utility）の枠組みを用いて、協調的多目的MARLにおける公平性の実現を探求している。エージェント間でどのように報酬や資源を公平に分配するかは、社会的選択理論や倫理的AI設計とも密接に関連する課題である。

### 個体選択・集団選択とMARLの接点

より生態学的・進化論的な観点からMARLを捉えた研究も存在する。Chaturvedi ら (2026) は、非協調的なエージェント群が同一の資源チャネルを奪い合う「コモンズの悲劇」（Tragedy of the Commons）を回避するための計算モデルを提案している。

自然界では、集団内の個体が異なる役割に分化することで資源の枯渇を防ぐことが知られているが、この役割分化がいかにして個体レベルの継続的な選択圧のみから創発しうるかは未解明であった。同研究は、**多段階選択**（Multi-Level Selection）の計算モデルを導入し、集団レベルの選択が共通の基盤（substrate）と突然変異演算子を形成し、個体レベルの選択と相互作用することを示している。これはMARLにおける役割分化と創発的協調の理解に重要な示唆を与えるものである。

### 主要な課題と研究動向

| 課題 | 説明 |
|------|------|
| スケーラビリティ | エージェント数の増大に伴う計算・通信コストの爆発 |
| 非定常性 | 他エージェントの学習によって環境が変化し続ける問題 |
| 部分観測性 | エージェントが環境全体を観測できない場合の対処 |
| 耐故障性 | ビザンチン故障や通信障害への対応 |
| 公平性 | 複数目標・複数エージェント間での公平な資源配分 |
| 創発的協調 | 明示的な設計なしに協調行動を自律的に生み出す仕組み |

---

## 関連概念

- [[強化学習 (Reinforcement Learning)]]
- [[Q学習 (Q-Learning)]]
- [[マルコフ決定過程 (Markov Decision Process)]]
- [[分散部分観測マルコフ決定過程 (DEC-POMDP)]]
- [[ビザンチン故障耐性 (Byzantine Fault Tolerance)]]
- [[分散学習 (Distributed Learning)]]
- [[協調型AIエージェント (Cooperative AI Agents)]]
- [[コモンズの悲劇 (Tragedy of the Commons)]]
- [[多段階選択 (Multi-Level Selection)]]
- [[スマートグリッド (Smart Grid)]]
- [[P2P電力取引 (Peer-to-Peer Energy Trading)]]
- [[複雑系科学 (Complexity Science)]]

---

## 参考ソース

1. **Fully Byzantine-Resilient Distributed Multi-Agent Q-Learning**
   Haejoon Lee, Dimitra Panagou (2026)
   `raw/Fully_Byzantine-Resilient_Distributed_Multi-Agent_Q-Learning.md`

2. **Multi-agent Reinforcement Learning-based Joint Design of Low-Carbon P2P Market and Bidding Strategy in Microgrids**
   Junhao Ren, Honglin Gao, Sijie Wang, Lan Zhao, Qiyu Kang (2026)
   `raw/Multi-agent_Reinforcement_Learning-based_Joint_Design_Low-Carbon_P2P.md`

3. **Role Differentiation in a Coupled Resource Ecology under Multi-Level Selection**
   Siddharth Chaturvedi, Ahmed El-Gazzar, Marcel van Gerven (2026)
   `raw/Role_Differentiation_Coupled_Resource_Ecology_Multi-Level_Selection.md`

4. **Fairness in Cooperative Multi-objective Multi-agent Reinforcement Learning using Expected Utility**
   Farès Chouaki, Aurélie Beynier, Nicolas Maudet, Paolo Viappiani (2026)
   `raw/Fairness_Cooperative_Multi-objective_MARL_Expected_Utility.md`