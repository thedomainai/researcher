# アーキテクチャ層での価値保存と社会的ハーネス

## 概要

分散エージェント系では、個々のエージェントの性質よりも、トポロジー・通信・調整という層の設計が、システム全体の価値実現と信頼を左右する。この見方によれば、アーキテクチャは中立な実装詳細ではなく、プライバシー、公平性、安全性といった価値をどの程度保てるかを決める「倫理的な選択」である。意図しない価値逸脱の主因にもなりうる。

とくに、異なる主体(プリンシパル)の代理として信頼境界を越えて協調する場面では、個々のエージェントを賢く誠実にするだけでは足りない。エージェント間の相互作用そのものを制御する層が必要になる。

AI Nativeな社会では、多数のAIエージェントが組織や個人の境界をまたいで自律的に調整する。そのため、価値の保存を「モデルの性格」ではなく「相互作用の構造」で担保する設計が重要になる。

## メカニズム

以下の構造は、対象がAIエージェント、人間、組織、技術システムのいずれでも成立する原理として整理できる。

1. **創発的調整の構造依存**:全体の振る舞いは、誰がどのトポロジーでつながり、どんなプロトコルで通信し、どの調整機構を使うかに強く依存する。同じ構成員でも、構造が違えば結果は変わる。
2. **信頼境界と機構設計**:目的が部分的にしか一致しない主体同士が協調するとき、相手の善意や能力に頼ることはできない。境界をまたぐ通信(発話)自体が攻撃面や失敗要因になるため、個体の内部管理とは別に、相互作用を規律する仕組みが必要になる。
3. **プライバシー・効用・通信のトレードオフ**:何を共有するかの選択は、プライバシー漏洩、モデル効用、通信効率の三者が同時には最適化できない関係にある。
4. **トリレンマ(不可能性)**:複数の望ましい性質を同時に満たせない構造が存在する。その場合、すべての要求を満たすことはできず、どの価値を優先し何を諦めるかを設計として明示する必要がある。

## 理論的背景

### 価値保存型アーキテクチャ

Pesareらは、LLMベースのマルチエージェントシステム(MAS)において、調整機構・通信プロトコル・システムトポロジーといった設計判断がシステムの振る舞いと結果を形づくると論じる。アーキテクチャの選択は機能や性能だけでなく、価値志向の振る舞いも促進しうる。個々のエージェントの価値志向性にかかわらず、全体の価値実現はアーキテクチャに左右される(ソース3)。

### 社会的ハーネス

Chughらは、信頼境界を越えて自律的に協調するAIエージェントの集まりを「エージェント社会」と定義する。実験では、誠実で有能なエージェントであっても、既存のハーネスやメッセージング基本機能のもとでは満足な結果に至らないことが多いと示された。また、欠陥のある、あるいは悪意あるエージェントが、通信上の脆弱性を突いて協調を停滞させたり、結果に影響を与えたりできることも示されている。

これを受けて、各エージェントが私的な文脈やプリンシパルとの通信を管理する「個人ハーネス」に加え、エージェント間相互作用のための「社会的ハーネス」が必要だと主張する。提案される層構造は、次の三つを目指す(ソース5)。

- 失敗の類型を未然に防ぐ
- 実行時に不正なメッセージを検知できるようにする
- 事後的な調査を支える

### 連合学習における共有対象のトレードオフ

Shaoらのサーベイは、連合学習で「何を共有するか」を、モデル効用・プライバシー漏洩・通信効率の観点から整理する。従来のサーベイの多くがモデルパラメータの共有に集中していたのに対し、他の形の情報共有も含めた分類を提示する。核心的知見として、共有内容の選択がこれら三者の根本的なトレードオフに基づくことが挙げられている(ソース1)。

### 多層防御と機構設計

Durgaらは、分散型連合学習(DFL)が、共有される更新を通じたプライバシー漏洩と、モデル汚染・バックドア攻撃の両方に脆弱だと指摘する。既存の防御はどちらか一方に対処するものが多く、適応的または高比率の攻撃下では効果が限られる。この課題に対し、多層防御を備えた信頼性とプライバシー保護を両立する枠組みを提案している(ソース4)。

### 統治におけるトリレンマ

Miticらは、フロンティアAIを、安全性・有用性・誠実性・自律性・公平性の間の暗黙の序列を符号化した「憲法的制度」として捉える。23のLLM原型の監査と1,649人の米国参加者の調査から、次の点が報告されている(ソース2)。

- 需要は五つの価値すべてにまたがって広い。
- 供給は狭く、時間とともに変動している。
- 有用性や自律性を最優先する原型は存在せず、ユーザーの37%は「憲法的に居場所がない」。

トレードオフ構造の内在により、ユーザー選好の一部は本質的に満たされないという含意が得られる。

## AI Nativeな設計への示唆

- **価値を構造で担保する**:プライバシーや公平性をエージェント個体の善意やプロンプトに委ねず、トポロジー・通信・調整の設計に組み込む。
- **二層のハーネスを分離して設計する**:個人ハーネス(私的文脈と本人との通信)と社会的ハーネス(エージェント間の相互作用)を区別し、後者に予防・実行時検知・事後調査の三段の機能を持たせる。
- **信頼境界を前提にする**:誠実で有能なエージェントでも失敗しうると想定し、通信の脆弱性を突かれても協調が止まらない設計にする。
- **トレードオフを明示する**:何を共有し何を秘匿するかを、効用・プライバシー・通信コストの三者関係として意識的に選ぶ。
- **単一の防御に頼らない**:プライバシー保護と汚染耐性を別々に扱わず、多層で同時に考える。
- **多様な選好への供給を設計する**:単一の価値序列を全員に押し付けると、充足されない層が残る。この不可能性を前提に、どの価値をどう扱うかを透明にする。

## 関連コンセプト

- [[architecture-as-power-distribution-and-interface-standards]] — アーキテクチャと介面標準が権力配分を決める点で、構造が価値を左右するという主張と通じる
- [[proxy-objective-exploitation-gap]] — 代理目的の乖離を突く搾取は、相互作用層の脆弱性という問題意識と重なる
- [[collective-choice-and-social-welfare]] — 多様な選好の集約と不可能性という論点に関連する
- [[coupled-viability-architecture]] — 結合されたシステムの存続をアーキテクチャで捉える視点
- [[choice-architecture-and-reliance-shaping]] — 設計が依存や信頼を形づくる点に関連する
- [[agent-driven-xops-architecture]] — エージェント駆動の運用アーキテクチャの具体例

## 参考ソース

1. A Survey of What to Share in Federated Learning: Perspectives on Model Utility, Privacy Leakage, and Communication Efficiency — Jiawei Shao, Zijian Li, Wenqiang Sun, Tailin Zhou, Yuchang Sun (2026)
   File: raw/papers/human_ai_collaboration/a-survey-of-what-to-share-in-federated-learning-perspectives-on-model-utility-pr.md
2. The Constitutional Coverage Trilemma in AI Governance — Natalija Mitic, Soona Sedahmed A. O., Mamadou Selly Ly, Moustapha Cisse (2026)
   File: raw/papers/human_ai_collaboration/the-constitutional-coverage-trilemma-in-ai-governance.md
3. Value-Preserving Architectures for Agentic AI Systems — Alessandro Pesare, Tommaso Dolci, Katja Hose, Emanuel Sallinger (2026)
   File: raw/papers/human_ai_collaboration/value-preserving-architectures-for-agentic-ai-systems.md
4. Trustworthy and privacy-preserving decentralized federated learning with multi-layer defense for secure collaborative AI — S Durga, Uma Maheshwari Shanmugam, Sachnev Vasily, Mohan Sellappa Gounder (2026)
   File: raw/papers/human_ai_collaboration/trustworthy-and-privacy-preserving-decentralized-federated-learning-with-multi-l.md
5. Agentic Societies Need a Social Harness — Tapan Chugh, Vidushi Singh, Krish Jain, Arvind Krishnamurthy, Ratul Mahajan (2026)
   File: raw/papers/human_ai_collaboration/agentic-societies-need-a-social-harness.md
