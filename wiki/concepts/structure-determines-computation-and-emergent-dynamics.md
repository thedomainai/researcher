# 構造が計算能力と創発動態を規定する原理

## 概要

「構造が計算能力と創発動態を規定する原理」とは、系の**ネットワーク構造**、**局所規則**、**時間・決定の表現**が、その系にできる計算と大域的な振る舞いを決めるという不変原理である。実装基盤が脳、AI、組織のどれであっても、構造と現象の対応が保たれているかどうかが系の有効性を左右する。

AI Nativeな社会設計でこの原理が重要なのは、人間・AIエージェント・組織が混在する系では、個々の構成要素の性能よりも、それらをどう結線し、どんな局所規則と時間表現を与えるかが全体の能力と失敗様式を決めるからである。基盤が入れ替わっても設計上の問いは変わらない。「どの構造が、どの計算と創発を許すのか」を問う視点が、設計の出発点になる。

## メカニズム

この原理は、次の3つの構造的要素に整理できる。いずれも対象(人間/AI/組織/技術)を入れ替えても成立する。

1. **構造-機能対応**:結合の仕方(アーキテクチャ)が、系に実行可能な計算の範囲を決める。多くの構造は表現力が限られ、能力の高い構造は少数である。
2. **局所規則からの大域的創発**:各要素が局所的な情報だけで動作しても、規則と構造の組み合わせによって、系全体に安定したパターンが自発的に現れる。大域的な現象は、個々の要素の中に書き込まれてはいない。
3. **時間・決定の状態表現**:時間の経過や決定は、系の内部状態として表現されなければならない。この表現は情報処理系に必須の計算構造として扱われる。

これらを組織に当てはめると、構造は権限や情報の流れの結線、局所規則は各主体の行動ルール、時間・決定の表現は意思決定の記録や手順の状態管理に対応する。この対応づけは本記事による類推であり、ソースが直接組織を論じているわけではない。

## 理論的背景

### 構造と計算能力の系統的関係

Talpir と Schneidman(2026)は、リカレントニューラルネットワークの計算能力を結合構造の関数として特徴づけた。多数のネットワークを大量のブール関数を計算するよう訓練し、小規模ネットワークでは構造と関数の性能を網羅した「カタログ」を作成している。その結果、計算能力はアーキテクチャによって大きく異なり、ほとんどのネットワークは性能が低く、ほとんどの関数は計算が難しいことが示された。核心的知見は、ネットワーク構造と計算能力の間に系統的な関係が存在し、ほとんどのアーキテクチャの表現力は限定的だという点である。

### 局所規則からの大域的創発

Meessen(2026)は、離散時間のスパイキングニューロンモデルを構築した。このモデルは、乗算型スパイクタイミング依存可塑性(WSTDP)、除算正規化、恒常的な閾値適応、1ステップの不応期を組み合わせたものである。興奮性・抑制性ニューロン対を2次元の再帰ネットワークに組み、周期的な局所刺激を与えると、散逸ソリトンの性質を持つ自己伝播波束が自発的に現れる。波束は空間プロファイルを保ち、一定速度で伝播し、正面衝突で消滅する。この出現には興奮性と抑制性の間の幾何学的非対称性が必要とされる。局所的な相互作用規則と構造の非対称性が、大域的な波動現象を決めていることが分かる。

### 時間と決定の表現

Jarne ら(2026)は、リカレントニューラルネットワークにおける時間と決定の表現を扱う。ソースの整理では、時間と決定の表現はどの情報処理システム(脳、AI、組織)にも必須の計算構造であり、不変の設計制約とされる。

### 構造と現象の対応が有効性を決める

Wang ら(2026)は、教育における認知モデルとしてのAIの妥当性を論じている。言語的な理論が機構レベルで不十分であることを背景に、AIを、実行可能な学習者の認知モデルとして扱う新しいパラダイムを整理している。核心的知見は、計算モデルの説明的有効性は実現基盤(AIか従来型シミュレーションか)に依存せず、構造と現象の対応性に依存するという点である。

### 世界表現の正規化と構造

Slaoui(2026)のS-AI-WorldModelは、世界を、実体・関係・述語・事象・因果依存・目標・時間的組織・作業記憶からなる正準的な認知構造として表現する。この表現を、曖昧さや不整合、不要な複雑さを減らす規制された再帰過程で精緻化し、安定した正準表現を確定させる。ソースの整理では、計算資源制約下での世界表現の正規化は、あらゆる知的主体に避けられない構造問題とされる。

### 決定の不可逆性という構造的マーカー

Nagae(2026)は、意識・主観性の有無を「収束点」の有無として構造的に評価する枠組みを示す。収束点とは、身体性と生存可能性の制約のもとで、複数の可能な軌跡が単一の実行可能な履歴へ不可逆的に縮約される構造上の場所である。ここでも、現象(主観性)は構造的条件から定義されている。

## AI Nativeな設計への示唆

- **構造を先に設計する**:能力の高い構造は少数であるため、モデルの性能を単に増やすよりも、結線・役割分担・情報経路といった構造の選定に設計資源を割く。
- **局所規則と大域挙動を分けて検証する**:個々のエージェントの規則が妥当でも、大域的には予期しないパターンが現れうる。局所規則の変更が全体に与える影響をシミュレーションで確認する。
- **非対称性を意図的に設計する**:創発には構造の非対称性が要件となる例がある。役割や情報の対称性は、創発を左右する設計変数として扱う。
- **時間と決定を明示的な状態として持たせる**:意思決定の履歴、待機、期限などを内部状態として表現し、追跡可能にする。
- **基盤非依存の妥当性基準を置く**:人間、AI、従来のルールベースのいずれが担う部分でも、構造と観測される現象が対応しているかで評価する。
- **表現の正規化に予算を置く**:資源制約下では、世界表現の整理と単純化を継続的な処理として組み込む。

## 関連コンセプト

- [[complex-network-dynamics]] — ネットワーク構造が大域的ダイナミクスを規定する点で直接関連する
- [[local-rules-to-emergent-collective-order]] — 局所規則からの集団秩序の創発
- [[emergent-order-and-narrative-attribution]] — 分散的相互作用からの秩序創発
- [[interaction-emergent-coordination]] — 相互作用から生じる協調
- [[feedback-loops-system-dynamics]] — 構造に埋め込まれたフィードバックの動態
- [[metastable-basin-dynamics]] — 系の状態空間における安定状態の構造
- [[constraint-driven-computation-and-precision-weighted-inference]] — 制約下での計算と推論
- [[coupling-amplified-failure-and-legitimacy-gaps]] — 結合構造による障害の増幅
- [[external-scaffolding-of-finite-cognitive-capacity]] — 有限な計算資源の補完

## 参考ソース

1. Talpir, T., Schneidman, E. (2026). *Identifying structural design principles shaping the computational abilities of recurrent neural networks*.
   File: raw/papers/neuroscience/identifying-structural-design-principles-shaping-the-computational-abilities-of-.md
2. Meessen, Ch. (2026). *Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity*.
   File: raw/papers/neuroscience/soliton-like-waves-in-a-two-dimensional-recurrent-spiking-neural-network-with-we.md
3. Jarne, C., Yoon, R., Eissa, T. L., Kilpatrick, Z. P., Josić, K. (2026). *Task-Parametrized dynamics: Representation of time and decisions in recurrent neural networks*.
   File: raw/papers/neuroscience/task-parametrized-dynamics-representation-of-time-and-decisions-in-recurrent-neu.md
4. Wang, P., Viberg, O., Law, E. L.-C., Greiff, S. (2026). *When Can AI Models Explain Learning? Validity Criteria for AI as Cognitive Models in Education*.
   File: raw/papers/neuroscience/when-can-ai-models-explain-learning-validity-criteria-for-ai-as-cognitive-models.md
5. Slaoui, S. (2026). *S-AI-WorldModel: Regulated Canonicalization of the World Model*.
   File: raw/papers/neuroscience/s-ai-worldmodel-regulated-canonicalization-of-the-world-model.md
6. Nagae, M. (2026). *An AI Prompt for Strongly Inferring the Presence or Absence of Subjectivity III — A Provisional Consciousness-Assessment Tool Based on Convergence-Point Analysis Using Fifty Sample Entities —*.
   File: raw/papers/neuroscience/an-ai-prompt-for-strongly-inferring-the-presence-or-absence-of-subjectivity-iii-.md
