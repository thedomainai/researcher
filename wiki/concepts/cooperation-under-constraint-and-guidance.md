# 資源制約・ガイダンス下での協力の進化と安全性保証

## 概要

この概念は、マルチエージェント系において、(1) 計算・物理コストの制約、(2) 確率的ガイダンス、(3) 社会的ルール、(4) ノイズ付き最適応答という要素が組み合わさることで、自由乗車(フリーライド)を抑えながら協力を創発させ、同時に性能の下限と安全性を保証できる、という不変原理を指す。

AI Nativeな社会では、人間・AIエージェント・組織が混在し、多数の主体が共有資源や共通目的のもとで相互作用する。各主体が自己利益だけで動けば、協力の崩壊や相互干渉、最悪均衡への固定化が起こりうる。したがって、「協力を期待する」のではなく、「協力が成立しやすく、失敗しても下限が保証される構造」を設計することが重要になる。

## メカニズム

対象が人間・AI・組織・技術のいずれであっても成立する構造として、次の三つに整理できる。

1. **インセンティブ設計による自由乗車の抑制**
   - 資源獲得と共有資源の維持のジレンマを、行動のコスト構造そのものに埋め込む。
   - ルール違反者(自由乗車者)に働きかけて行動を調整させる「ガイダンス」を、確率的なものとして設計する。ガイダンスには、仲間が費用を負担して行うもの(ピアガイダンス)と、制度が担うもの(プールガイダンス)がある。
2. **不安定均衡のノイズによる回避**
   - 最悪ケースに近い均衡は不安定であることが多い。主体が最適応答の近傍から確率的に行動を選ぶ(ノイズを許容する)ことで、そのような均衡に留まり続けることを避け、高価値の状態へ到達しやすくする。
3. **共通ルールによる相互干渉の制限**
   - 全主体が従う社会的ルールにより、各主体が単独で最適な方策を追求しても、他者との干渉で得られる効用があらかじめ定めた水準を下回らないようにする。

## 理論的背景

### 計算と協力の共進化(Autopoietic Game Theory)
Jhaらは、社会的相互作用、複製メカニズム、およびそれに伴う計算コストが内生的かつ同時に共進化する計算モデル「Autopoietic Game Theory」を提案している。従来の進化ゲーム理論は社会的相互作用を行動の物理的コストから切り離して扱い、人工生命モデルは資源獲得と複製に必要な共有エネルギーの維持というジレンマを形式化してこなかった、という問題意識に立つ。実証にはZ80機械語のランダム初期化プログラムという計算基盤が用いられ、社会的ジレンマを系の「物理」に直接組み込むことの効果が、実験的に、また簡略化した理論モデルで示されている(抜粋は途中で切れており、詳細な結果は本記事では扱わない)。

### 確率的ガイダンスと集団協力
Liuらは、繰り返し公共財ゲームの枠組みに確率的ガイダンスを導入した。1回のゲームでは、ガイダンスを受け付けない頑固な主体が存在するため、全ての自由乗車者を協力者に転換することは非現実的だという前提がある。ピアガイダンスでは案内者がコストを負担し、プールガイダンスでは制度が自由乗車者を導く。無限集団のレプリケータ動力学と確率的動力学の両面で協力の進化への影響が調べられている。

### 切り詰めノイズ付き最適応答(TNBR)
Singh and Brownは、劣モジュラ最大化目的のマルチエージェント調整問題を扱う。対応するゲームのナッシュ均衡は常に最適の50%以内にあるが、その最悪境界を達成する均衡は不安定であることが知られている。この不安定性を利用するために、主体が非同期かつ確率的に、最適応答の報酬近傍から行動を選ぶTNBRアルゴリズム群が提案された。関連するマルコフ連鎖の再帰類に対して二種類の境界が導かれている。
- **性能境界**:高価値の再帰状態が必ず存在することを保証する。
- **安全境界**:任意に悪い再帰状態が存在しないことを保証する。

### 確率環境における社会的ルール
Fernandezらは、決定論的・ゴール志向の設定で研究されてきた社会的ルールを、確率的・報酬ベースの環境へ拡張した。全主体がルールに従う場合に、各主体が単独最適方策を追求しつつ保持できる効用の保証を測る指標として「α-ロバスト性」を導入し、その検証を一連のマルコフ決定過程を解く問題への還元によって行う手法を示している。評価は簡単なトイ環境で行われている。

### ノイズと情報処理能力
Kotokuらは、駆動される力学系の情報処理容量(IPC)においてノイズの影響を整理した。ノイズ実現にわたって平均した応答のIPCは、一般に無擾乱系のIPCと一致しない。ノイズは計算容量を再配分し、特定タスクでは性能を高めることさえあり、単なる劣化要因ではないと示された。これは、ノイズを設計上の資源として扱う見方と整合する。

## AI Nativeな設計への示唆

- **協力の前提をコスト構造に組み込む**:計算資源やエネルギーのコストと協力のジレンマを切り離さず、同じ枠組みで設計・評価する。
- **ガイダンスは確率的・多層的に設計する**:全員の転換を前提とせず、頑固な主体が残ることを織り込み、ピア型と制度型を組み合わせる。制度型の費用負担の所在も設計対象となる。
- **ノイズを意図的に許容する**:最適応答への厳密な固執を避け、近傍からの確率的選択を認めることで、不安定な悪均衡から脱出する余地を残す。
- **性能下限と安全上限を分けて保証する**:「高価値状態が存在する」ことと「極端に悪い状態が存在しない」ことを別個の性質として検証可能にする。
- **共通ルールをα-ロバスト性などで検証する**:ルール導入後も各主体の最低効用が保たれるかを、形式的に検証してから展開する。
- **注意点**:ソースはいずれも2026年の新しい研究で、社会的ルールの評価はトイ環境にとどまるなど、実社会規模での実証は今後の課題である。

## 関連コンセプト

- [[indirect-reciprocity-evolution]] — 間接互恵性による協力の進化
- [[constraint-anchored-validity-and-verifiable-boundaries]] — 制約による妥当性の担保と検証可能な境界
- [[constitutional-constraint-and-power-balance]] — 共通ルールと権力制衡による統治
- [[ai-safety-and-governance]] — AIの安全性とガバナンス
- [[long-horizon-emergent-failure-and-feedback-coupling]] — 長期相互作用における創発的失敗
- [[coevolving-threat-defense-and-ecosystem-coordination]] — 共進化と生態系的協調
- [[responsibility-dilution-and-moral-status-symmetry]] — 多主体チームでの責任の希薄化
- [[cultural-evolution]] — 文化的進化論

## 参考ソース

1. Truncated Noisy Best-Response Algorithms: Toward Game Theoretic Learning with Safety Guarantees — Vartika Singh, Philip N. Brown (2026)
   File: raw/papers/complexity_science/truncated-noisy-best-response-algorithms-toward-game-theoretic-learning-with-saf.md
2. Tapes Together Strong: The Co-evolution of Computation and Cooperation — Kunal Jha, Francesco Cicala, Blaise Agüera y Arcas, Blake Aaron Richards, Natasha Jaques (2026)
   File: raw/papers/complexity_science/tapes-together-strong-the-co-evolution-of-computation-and-cooperation.md
3. Emergence of group cooperation through probabilistic guidance in repeated interactions — Siyu Liu, Lichen Wang, Shijia Hua, Linjie Liu (2026)
   File: raw/papers/complexity_science/emergence-of-group-cooperation-through-probabilistic-guidance-in-repeated-intera.md
4. Social Laws for Multi-agent Coordination in Stochastic Environments — Rolando Fernandez, Caleb Probine, Tyler Lee, Jeffrey Chen, Erez Karpas (2026)
   File: raw/papers/complexity_science/social-laws-for-multi-agent-coordination-in-stochastic-environments.md
5. Reconstructing the information processing capacity of physical systems from noisy observations — Shun Kotoku, Rodrigo Martínez-Peña, Takatomo Mihana, Felix Köster, Johannes Nokkala (2026)
   File: raw/papers/complexity_science/reconstructing-the-information-processing-capacity-of-physical-systems-from-nois.md
