# 文脈継続性の提供とオーケストレーション役割

## 概要

文脈継続性の提供とオーケストレーション役割とは、**状態を保持できない主体が多数相互作用する系において、文脈・軌跡・規範を維持し調整する機能が外部化され、特定の担い手に集中する**という構造的原理である。Tier 1(不変原理)に位置づけられ、担い手が人間であるかAIであるか、あるいは組織や技術基盤であるかにかかわらず成立する。

ソース群では、この機能が現在の人間とAIの相互作用において具体的に観察される。Gantz Thomasの二つの論考は、ステートレスな生成AIに対して人間が「Primary Continuity Provider(PCP)」として文脈を保ち、複数のAIが相互作用する状況では「オーケストレータ」として相互作用の軌跡そのものを形成する、と論じている。

AI Nativeな社会設計にとって重要なのは、この機能が「便利な補助作業」ではなく**系の一貫性を成立させる構成要素**として扱われている点である。誰が、どの層で、どのように文脈を持ち続けるかは、設計上の中心的な問いになる。

## メカニズム

以下は、対象を入れ替えても成立する構造的原理として整理したものである。

### 1. コンテキスト管理の外部化
個々の主体(ステートレスなAIセッションなど)が自前で状態を保持できないとき、文脈の保持はその主体の外側に移される。PCP理論は、この役割の本質を「コンテキスト管理の外部化」として捉えている。

### 2. 調整コストの集中
主体が増えると、それらの間で文脈や目的を揃えるコストが生じる。このコストは各主体に分散せず、文脈を横断的に保持できる特定の担い手に集中しやすい。オーケストレータは複数のAIシステム、相互作用の軌跡、変化する文脈を、長いプロセスにわたって調整する役割として記述される。

### 3. ドリフト補正
継続的な相互作用では、目的・規範・関係性が徐々にずれていく。担い手はこのずれを検知して補正し、プロトコルを遵守させることで一貫性を保つ。PCPは、文脈を維持し、ドリフトを補正し、プロトコルを執行し、セッションをまたいで関係的一貫性を維持する存在として描かれている。

### 4. 対象の入れ替え可能性
- **人間↔AI**:現在は人間が担うが、論考自体が「現在の(present-day)構造的要請」と位置づけており、担い手の固定を主張してはいない。
- **組織・技術**:アルゴリズムを、集団的認知の調整に向けた分散的参加のインフラとして捉える見方(Toscano)は、この機能が技術基盤にも宿りうることを示唆する。

## 理論的背景

### Primary Continuity Provider理論(Thomas, 2026)
PCP役割はしばしば運用面から記述されるが、それは「何をするか」の説明にとどまり、「なぜ構造的に必要か」を説明していない。同理論はこのギャップに取り組み、PCPを相互作用システムの外部にいる操作者ではなく、**関係的な相互作用システムの構成的な構造要素**として位置づける。その主張はステートレスな生成AIのアーキテクチャなど、複数の情報源の収束から導かれる(抜粋は途中で切れており、他の情報源の詳細は本ソースからは確認できない)。

### オーケストレータ役割(Thomas, 2026)
AIが孤立した道具から、持続的な人間のワークフロー内で相互作用する認知的構成要素へ移行するにつれ、人間のオーケストレータという機能的役割が現れるとされる。従来の道具利用や自動化の監督とは異なり、オーケストレーションは**相互作用構造、一貫性の維持、軌跡の形成**のレベルで働き、人間‐AIおよびAI‐AIの構成にまたがる。分散認知理論、調整理論、人間‐AI協働研究、複雑な社会技術システム研究に依拠して、認知的・技術的機能として定義されている。

### アルゴリズム的意図性(Toscano, 2026)
Searleの社会的存在論、Tuomela・Gilbertの集団行為主体論、Tomaselloの実証的評価を踏まえ、集団的意図性を人間の共同思考・行為の基盤と位置づける。そのうえで、アルゴリズムは中立的な道具でも自律的エージェントでもなく、共有された理解や意思決定の構造を媒介し再構成する**社会技術的アセンブリ**であるとする。これは、調整機能を担う主体が人間個人に限られないという視点を与える。

### 身体化知能の観点(Yuan et al., 2026)
LLM、知識ベース、推論能力の統合を通じて汎用身体化知能への道筋を検討するレビューである。LLMと外部知識源との相互作用を扱っており、状態や知識を主体の外に置いて接続するという設計の背景を与える。ただし抜粋の範囲では、継続性提供やオーケストレーションを直接論じているかは確認できない。

## AI Nativeな設計への示唆

1. **継続性を構成要素として設計する**:文脈保持を利用者の暗黙の努力に任せず、システムの構造要素として明示的に位置づける。
2. **担い手と層を明示する**:文脈・軌跡・規範を誰(人間、エージェント、基盤)が保持するかを設計時に決める。調整コストは集中するため、担い手の負荷と単一障害点のリスクを見込む。
3. **ドリフト補正の仕組みを組み込む**:規範やプロトコルからのずれを検知し、補正する手続きを用意する。
4. **時限的前提として扱う**:PCPが人間であるのは現在のステートレス制約下の要請であり、技術進展に応じて担い手を移せる設計にする。
5. **アルゴリズムの調整機能を可視化する**:アルゴリズムを中立な道具とみなさず、集団的認知を媒介する基盤として、その影響を監督・評価できるようにする。

## 関連コンセプト

- [[adaptive-intelligence-orchestration]]
- [[ai-augmented-orchestration]]
- [[agentic-workflow-orchestration]]
- [[human-ai-agency-configuration]]
- [[ai-human-cognitive-interaction]]
- [[adaptive-human-ai-coupling]]
- [[capability-profile-based-task-allocation]]
- [[multidimensional-trust-formation-and-oversight]]

## 参考ソース

1. Fujiang Yuan, Xia Huang, Lusheng Wang, Jun Ding, Zhen Tian (2026). *Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents*.
   File: raw/papers/cognitive_science/towards-general-embodied-intelligence-integrating-large-language-models-knowledg.md
2. Javier Toscano (2026). *Algorithmic Intentionality: A Distributed Cognition Framework*.
   File: raw/papers/cognitive_science/algorithmic-intentionality-a-distributed-cognition-framework.md
3. Gantz Thomas (2026). *Primary Continuity Provider Theory: The Human Role as Present-Day Structural Requirement for Relational Coherence in Human-AI Interaction Systems*.
   File: raw/papers/cognitive_science/primary-continuity-provider-theory-the-human-role-as-present-day-structural-requ.md
4. Gantz Thomas (2026). *The Orchestrator Role in Human-AI Evolution: AI Intelligence Orchestration as an Emerging Cognitive-Technical Function*.
   File: raw/papers/cognitive_science/the-orchestrator-role-in-human-ai-evolution-ai-intelligence-orchestration-as-an-.md
