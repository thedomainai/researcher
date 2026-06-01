# マルチエージェント強化学習

## 概要

**マルチエージェント強化学習（Multi-Agent Reinforcement Learning、MARL）**とは、複数の自律的なエージェントが環境と相互作用しながら、それぞれの方策（ポリシー）を学習する強化学習の拡張フレームワークである。単一エージェントの強化学習とは異なり、MARLでは各エージェントが他のエージェントの行動や意思決定の影響を受けながら学習を進める点が特徴的である。

MARLが重要視される理由は、現実世界の多くの問題が本質的に複数の意思決定主体を含むためである。エネルギー管理、自律ロボティクス、経済市場設計、通信ネットワーク最適化など、単一エージェントでは対処できない複雑な分散型問題に対して有効なアプローチを提供する。また、エージェント間の協調・競合・役割分担といった創発的な集団行動の研究においても中心的なツールとなっている。

---

## 詳細

### 基本的な定式化

MARLにおける各エージェントの意思決定問題は、しばしば**マルコフ決定過程（MDP）**の多エージェント版として定式化される。エージェントが環境の全情報を観測できない場合は、**分散型部分観測マルコフ決定過程（Decentralized Partially Observable Markov Decision Process、DEC-POMDP）**が用いられる。DEC-POMDPでは、各エージェントが自身の局所的な観測情報のみに基づいて行動を決定するため、不完全情報下での分散型意思決定という現実的な設定を捉えることができる。

### 協調型MARLとQ学習

協調型MARLでは、エージェント群が共通の目標を達成するために連携して学習を行う。その代表的なアルゴリズムの一つが**分散型Q学習（Distributed Q-Learning）**であり、各エージェントが通信ネットワークを介して近傍エージェントと情報を交換しながら最適価値関数を学習する。

ただし、分散型通信環境では**ビザンチン攻撃（Byzantine Attack）**と呼ばれる悪意ある通信妨害の問題が存在する。ビザンチン攻撃とは、一部のエージェントやエッジが誤った情報を送信し、学習プロセスを意図的に妨害する攻撃形態である。Lee & Panagou（2026）は、通信ネットワークが侵害された状況においても、全エージェントの価値関数をほぼ確実（almost surely）に最適値へ収束させる新しい分散型Q学習アルゴリズムを提案している。この手法の核心は、**冗長性に基づくフィルタリング機構**であり、2ホップ先の近傍情報を活用してメッセージを検証しつつ、双方向の情報フローを維持する点にある。

### 応用：低炭素マイクログリッドの市場設計

MARLは実用的なエネルギーシステムにも応用されている。Ren et al.（2026）は、マイクログリッドコミュニティにおける**ピア・ツー・ピア（P2P）電力取引市場**の設計にMARLを活用した研究を提案している。この研究では、再生可能エネルギーの不確実性や実時間市場の不安定性という課題に対し、各マイクログリッドが自己利益を追求しつつ、市場運営者がコミュニティ全体の社会的厚生（低炭素排出目標）を最大化する枠組みを構築している。意思決定プロセスはDEC-POMDPとして定式化され、MARLによって解かれている。

### 多目的MARLと公平性

エージェントが単一の報酬ではなく、複数の目標を同時に最適化する必要がある場面では、**多目的MARL（Multi-objective MARL）**が用いられる。Chouaki et al.（2026）は、協調型多目的MARLにおける**公平性（Fairness）**の問題を期待効用の観点から研究している。複数エージェントが協調して多目的を追求する際、各エージェント間の利益配分における公平性の確保が重要な課題となる。

### 役割分化と多階層選択

自然界や社会システムにおいて、エージェント群は同一のリソースを競合して取り合う**コモンズの悲劇（Tragedy of the Commons）**を回避するために、異なる役割へ分化することが観察されている。Chaturvedi et al.（2026）は、**多階層選択（Multi-Level Selection）**の計算モデルを導入し、グループレベルの選択が共有基盤と突然変異演算子を形成することで、個体レベルの選択だけでは創発しにくい役割分化がいかに生じるかを探究している。この研究では、リソースチャネルを**正和のインテークチャネル**と**ゼロ和の再配分チャネル**に分類し、行動プリミティブを通じて結合された生態系における役割分化の創発メカニズムを分析している。

### 主要な研究課題

現在のMARL研究における主要な課題を以下に整理する。

| 課題 | 説明 |
|------|------|
| **収束保証** | 分散学習において最適解への収束を理論的に保証すること |
| **耐障害性・耐攻撃性** | ビザンチン攻撃などの悪意ある妨害に対する頑健性の確保 |
| **スケーラビリティ** | エージェント数が増大した際の計算・通信コストの管理 |
| **部分観測性** | 各エージェントが限られた情報しか持てない環境での意思決定 |
| **公平性** | 協調学習における複数エージェント間の利益配分の公平な設計 |
| **役割分化の創発** | 集団としての効率的な行動分担の自発的形成 |

---

## 関連概念

- 強化学習（Reinforcement Learning）
- マルコフ決定過程（Markov Decision Process）
- 分散型部分観測マルコフ決定過程（DEC-POMDP）
- Q学習（Q-Learning）
- ビザンチン耐性（Byzantine Fault Tolerance）
- コモンズの悲劇（Tragedy of the Commons）
- 多目的最適化（Multi-objective Optimization）
- ピア・ツー・ピアエネルギー取引（P2P Energy Trading）
- マイクログリッド（Microgrid）
- 進化ゲーム理論（Evolutionary Game Theory）
- 分散最適化（Distributed Optimization）
- [[complex-adaptive-systems|複雑適応系（Complex Adaptive Systems）]]

---

## 参考ソース

1. Lee, H., & Panagou, D. (2026). *Fully Byzantine-Resilient Distributed Multi-Agent Q-Learning*. arXiv:2604.02791v1. `raw/2604.02791v1`

2. Ren, J., Gao, H., Wang, S., Zhao, L., & Kang, Q. (2026). *Multi-agent Reinforcement Learning-based Joint Design of Low-Carbon P2P Market and Bidding Strategy in Microgrids*. arXiv:2604.02728v1. `raw/2604.02728v1`

3. Chaturvedi, S., El-Gazzar, A., & van Gerven, M. (2026). *Role Differentiation in a Coupled Resource Ecology under Multi-Level Selection*. arXiv:2604.00810v1. `raw/2604.00810v1`

4. Chouaki, F., Beynier, A., Maudet, N., & Viappiani, P. (2026). *Fairness in Cooperative Multi-objective Multi-agent Reinforcement Learning using Expected Utility*. OpenAlex:W7131948410. `raw/W7131948410`