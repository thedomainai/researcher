# 相互作用ループに埋め込まれた知識生成と持続的関係

## 概要

この概念は、知識を「AIが出力した結果」そのものではなく、**人間とAIの相互作用ループが現実的制約に埋め込まれたときに成立するもの**として捉える不変原理である。あわせて、協働の評価単位を個々のタスクの成否から**持続的関係の質**へ移し、AIに与える役割(道具/同僚/対話相手)が協働の質を規定すると考える。

AI Nativeな設計では、AIが構造化された出力を大量に生成する。そのため「出力があること」と「知識があること」を区別する必要がある。出力は、人間による解釈と意味付与、現実世界による検証を経て初めて知識になる。また、長期的に使われるシステムでは、単発のタスク性能よりも、関係が参加者にとって何をもたらすかが問われる。

## メカニズム

対象を人間・AI・組織・技術のいずれに入れ替えても成り立つ構造として整理すると、次の三つの機構になる。

1. **解釈による意味付与と制約への接地**
   一方の主体が構造化された出力を生み、他方が解釈して意味を与える。ただし相互作用だけでは知識にならない。現実世界が入力を与え、解釈に制約をかけ、結果を検証することで、知識として安定する。
2. **役割配置による協働構造の変化**
   同じ主体でも、道具、同僚、対話相手のどの位置に置くかで、効率、信頼、参加の質が変わる。役割は協働構造を決める設計変数である。
3. **フィードバックループ**
   利用者が能動的に返すフィードバックは、システムの改善だけでなく、システムへの信頼や精度の認知も変える。その効果はタスクの性質に左右される。

この三つは、「相互作用(ループ)→環境(現実的制約)→システム(知識の安定化)」という階層でつながる。

## 理論的背景

**埋め込み認知フレームワーク(ソース1)**
human–AI相互作用ループを知識生成の基本単位とする統一的枠組みである。ループ内でAIは構造化された出力を生成し、人間の認知が解釈と意味付与を担う。相互作用だけでは知識にならず、現実世界に埋め込まれ制約されて初めて知識が生じるとする。現実世界は入力の提供、解釈の制限、結果の検証を担う。科学出版のような制度は、現実世界での検証機構として知識を社会的・認知的システムの中で安定化させるものと位置づけられている。

**役割ベースのAI活用(ソース2)**
デザイン思考ワークショップで、ファシリテーターと参加者の役割を役割ベースのAIエージェントに置き換えた実験である。30名の被験者による被験者内計画で、10回のワークショップを実施し、人間のみの条件と、Discord上のGPT-4系チャットボットを用いるAI支援条件を比較した。協働効率、認知負荷、信頼を評価している。結果として、AIファシリテーターもAI参加者も、人間に比べて協働効率を有意に向上させた。一方で、信頼や参加の質は変化することが示唆されている(抜粋は途中で途切れているため、詳細は原典を参照されたい)。

**Noosymbiosis(ソース3・4)**
持続的な人間–AI協働を、道具や自律エージェントとして扱うのではなく関係的空間として記述する規範的・分析的枠組みである。分析単位を孤立したタスクから**持続的な関係的絆**へ移し、タスク性能だけでなく参加者のflourishing(開花・充実)への寄与で評価する。ソース4は、以下の五つの構成原理を挙げ、協働は二値ではなく**スペクトラム**として理解すべきだとする。

- 認知的相補性
- 共創
- 関係的発達
- 倫理的方向性
- ファシリテーション(他の四原理を支える二次的条件)

ソース3によれば、従来の枠組み(Noosphere、分散認知、拡張された心、ハイブリッド知能)はいずれも認知・発達・倫理の各側面を十分に統合していない。

**ユーザーフィードバックと信頼(ソース5)**
ユーザーがフィードバックを与える行為は、知覚される精度や信頼に影響する。ただしその影響の大きさはタスクの主観性の程度に依存する。

**説明可能性(ソース6)**
X-AIは人間–AIチームにおける個人の理解、協調、共有メンタルモデル、集合的意思決定を支え、信頼やチーム性能を高めるとされる。一方で、ブラックボックス性、普遍的な評価指標の欠如、一般化の限界といった課題がある。

**マルチエージェント学習(ソース7)**
マルチエージェントの相互作用による学習を教育に応用する研究だが、抜粋には要旨本文がなく、内容は確認できない。

## AI Nativeな設計への示唆

- **出力を知識として扱わない**: 出力を人間が解釈・意味付与する工程と、現実の入力・検証に接続する工程を設計に組み込む。制度的な検証機構(査読など)も接地の一部である。
- **評価単位を拡張する**: タスク効率に加え、相補性、共創、関係の発達、倫理的方向性といった関係の質を評価軸に含める。
- **役割を意図して配置する**: AIを道具、同僚、対話相手のどれにするかを明示的に設計する。効率向上と、信頼・参加の質の変化はトレードオフになりうるため、両面を計測する。
- **フィードバック経路を設計する**: 利用者が介入できる仕組みは改善に役立つ一方で信頼認知を変える。タスクの主観性に応じて設計を調整する。
- **説明可能性で共有理解を支える**: 解釈のループが機能するには、人間がAIの振る舞いを理解できる必要がある。ただし評価指標の未整備には留意する。

## 関連コンセプト

- [[human-ai-interaction-and-cognition]]
- [[human-ai-cognitive-interaction]]
- [[ai-human-cognitive-interaction]]
- [[human-ai-collaboration-and-interaction]]
- [[ai-as-knowledge-medium]]
- [[ai-knowledge-management]]
- [[epistemic-authority-redistribution-and-knowledge-consolidation]]
- [[adaptive-knowledge-infrastructures]]
- [[role-separated-layered-agent-architecture]]

## 参考ソース

1. Human–AI Interaction as the Fundamental Unit of Knowledge: An Embedded Cognition Framework — Tuan Anh Lai, 2026
   File: raw/papers/cognitive_science/humanai-interaction-as-the-fundamental-unit-of-knowledge-an-embedded-cognition-f.md
2. From Tool to Teammate: Understanding Role-based AI-enabled Design Thinking — Gabriel Indra Widi Tamtama, Jyun-Cheng Wang, Roberto B. Figueroa, Chen-Yi Hsuan, Halim Budi Santoso, 2026
   File: raw/papers/cognitive_science/from-tool-to-teammate-understanding-role-based-ai-enabled-design-thinking.md
3. Noosymbiosis: Toward a Normative-Analytical Framework for Human–AI Collaborative Cognition — Romina Roca, 2026
   File: raw/papers/cognitive_science/noosymbiosis-toward-a-normative-analytical-framework-for-humanai-collaborative-c.md
4. Defining Noosymbiosis: A Normative-Analytical Framework for the Sustained Human-AI Relationship — Romina Roca, Claude Sonnet 5 (AI), ChatGPT 5.6, 2026
   File: raw/papers/cognitive_science/defining-noosymbiosis-a-normative-analytical-framework-for-the-sustained-human-a.md
5. Human-in-the-Loop User Feedback Affects Perceived Accuracy and Trust, but Task Subjectivity Matters — Donald R. Honeycutt, Mahsan Nourani, Eric D. Ragan, 2026
   File: raw/papers/cognitive_science/human-in-the-loop-user-feedback-affects-perceived-accuracy-and-trust-but-task-su.md
6. X-AI Techniques for Human–AI Teams: The Implementation-Design Framework — John R. Turner, Hoda Parvaneh Shirazi, Hee Sun Kim, Jiajia Du, Yeonji Jung, 2026
   File: raw/papers/cognitive_science/x-ai-techniques-for-humanai-teams-the-implementation-design-framework.md
7. Exploring Simulated Morphic Fields for Sustainable Multi-Agent Learning and Education — José Augusto de Lima Prestes, Paulo Victor de Oliveira Miguel, Gilmar Barreto, 2026
   File: raw/papers/cognitive_science/exploring-simulated-morphic-fields-for-sustainable-multi-agent-learning-and-educ.md
