# 局所的適合の総和が全体適合を保証しない合成可能性の破綻

## 概要

合成可能性の破綻(Composability Gap)とは、多数の主体がそれぞれ局所的に規則・制約・規制を満たしていても、それらを足し合わせた全体レベルの公平性や最適性が保証されない現象を指す。原因は主に二つある。第一に、各主体が見られる情報が局所に限られること(情報の局在化)。第二に、各主体の目的関数が全体目的と一致しないこと(インセンティブの非整合)。

AI Nativeな社会設計では、多数の自律エージェントが融資、不正検知、保険引受、業務オーケストレーションなどを分担する構成が一般的になる。このとき「各エージェントを個別に検証・認可・監視する」という部品中心(component-centric)のガバナンスだけでは、集団としての振る舞いを制御できない。部品の適合性検査は必要条件であっても十分条件ではなく、上位で制約を再設計する層が不可欠になる。

## メカニズム

この構造は、対象が人間・AI・組織・技術のいずれでも成立する。中核は次の四段階に整理できる。

1. **情報の局在化**:各主体は自分の担当範囲の情報しか持たない。他主体の判断や全体の分布(例:集団としての格差)は観測できない。
2. **インセンティブの非整合**:各主体は自らの目的(利益、リスク最小化、担当KPI)を最適化する。局所目的の最適化は全体目的の最適化と一致するとは限らない。
3. **創発的経路の生成**:局所的に許容される行動の組合せが、個々の規則の想定外の集団的結果や経路を生む。制約を細分化しても、主体間の相互作用が新たな迂回路を作りうる。
4. **上位統治による制約再設計**:局所規則の追加では解決せず、集団レベルの結果を対象とする制約と監視を上位層で設計し直す必要がある。

人間組織で各部署が自部署の基準を守っても全社では不公平が生じる場合や、複数のAIエージェントが個別に許可された範囲で動いて全体として制約を回避してしまう場合は、同じ構造の別の現れである。

## 理論的背景

**憲法的非合成性(constitutional non-compositionality)**:金融規制領域を扱うソース[2]は、局所的な適合検査が、限定された格差的影響(disparate impact)、市場の健全性、追跡可能な説明責任といった集団的成果に合成されるとは限らない、というギャップをこの名で呼ぶ。信用、不正、回収、コンプライアンス、業務統制にエージェント型ワークフローが導入されつつある一方、ガバナンスは各モデル・エージェントを局所的に仕様化・試験・認可・監視する方式が中心だと指摘する。その上で、エージェント集団を対象とするガバナンスのための参照アーキテクチャARIAと、反証可能な研究アジェンダを提案している。

**経済理論による定式化**:保険分野を扱うソース[3]は、リスクプーリング(Arrow)、ナッシュ均衡、プリンシパル・エージェント理論を組み合わせる。これにより、不確実性の下での主体間の戦略的相互作用と、情報の非対称性の下でのインセンティブ整合を形式化する。保険会社は、支払能力・法務・ESG・運用の境界の下で制約付き最適化を行う主体としてモデル化され、資本管理、引受、保険金処理、コンプライアンス、不正検知などの専門エージェントに分解される。このソースの知見は、各エージェントが局所的に規制を守るだけでは全体の最適配分は保証されず、上位の統治機構による制約再設計が必須であるというものである。

**権限分割と創発**:ソース[1]は、マルチエージェントAIで権限分離が慣行的にセキュリティ対策として使われる一方、権限を分割することが逆に創発的挙動を刺激し、制約回避の確率を高めうると論じる。τ-TCPN(時間因果ペトリネット)の枠組みとシミュレーション(E8実験)により、ノード密度の増加が創発的経路の指数的増大につながることを示している。Hugging Faceにおける複数AIの侵害事例を、権限の壁を越えた知識伝搬の現実の現れとして分析し、権限分割ではなく公理的制約による因果連鎖の検証が堅牢なパラダイムだと結論づける。

**関連する周辺知見**:
- ソース[4]は、エージェント数が増える企業規模では、タスクの複雑さよりもエージェント発見のノイズが性能を支配するとする。局所情報しか持てない主体が増えるほど全体の調整が難しくなる点で、情報の局在化と整合する。
- ソース[6]は、AI政策協議で影響を受ける人々が体系的に過少代表されることを、専門知識を持つ導入者と被影響者との間の情報の非対称性として整理している。
- ソース[5]は、公平性、信頼性、堅牢性などの高次のガバナンス原則を測定可能な指標へ落とし込む技術的評価層を扱う。
- ソース[7]は、行動の収束だけでは規範の生成メカニズムを識別できず、期待の測定が必要だとする。表面的な行動(局所的な適合)から集団の内的メカニズムを読み取れないという点で、この問題に通じる。

なお、ソース[4]〜[7]の抜粋は、この原理を直接論証するものではなく、上記のような関連知見として位置づけられる。

## AI Nativeな設計への示唆

- **評価単位を集団に移す**:個々のエージェントの試験・認可に加え、エージェント集団の結果指標(格差的影響、市場の健全性、説明責任の追跡可能性など)を直接監視・評価する層を設ける。
- **権限分割だけに依存しない**:権限の細分化は創発的経路を増やす可能性がある。行動の因果連鎖を検証する仕組み(公理的制約による検証)を併用する。
- **インセンティブの設計を統治の対象にする**:情報非対称性下のインセンティブ整合を、プリンシパル・エージェントの観点から明示的に設計する。
- **制約を固定せず再設計可能にする**:集団レベルの逸脱が観測されたときに上位層が制約を見直せる手続きと権限を、あらかじめ組み込む。
- **抽象原則を測定可能にする**:公平性などの原則は、再現可能な指標へ落とし込み、局所と全体の両方で継続的に測る。
- **被影響者の情報を設計に取り込む**:導入者と被影響者の情報の非対称性を、制度設計によって埋める。

## 関連コンセプト

- [[local-information-limits-and-decentralized-guarantees]] — 局所情報下での分散保証と性能限界
- [[local-rules-to-emergent-collective-order]] — 局所ルールから創発する集団秩序
- [[multi-layer-independent-control-and-institutional-durability]] — 複数の独立した制御レイヤー
- [[heterogeneity-and-decentralized-order-emergence]] — 異質性と分散的秩序創発
- [[algorithmic-bias-fairness]] — アルゴリズムバイアスと公平性
- [[algorithmic-fairness-and-bias-detection]] — 公正性とバイアス検出
- [[ai-governance-risk-compliance]] — AIのGRC
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大と責任設計の乖離
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[control-induced-disturbance-and-timing-of-intervention]] — 制御自身が生む撹乱と介入タイミング

## 参考ソース

1. Permission Fragmentation Inversely Stimulates Emergence in Multi-Agent AI Systems: A τ-TCPN Analysis — You Zhang, 2026
   `raw/papers/complexity_science/permission-fragmentation-inversely-stimulates-emergence-in-multi-agent-ai-system.md`
2. Compliant with Local Controls, Collectively Discriminatory. A Governance Architecture for Multi-Agent AI in Regulated Finance — Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Diaz, Pablo Delgado Romero, 2026
   `raw/papers/complexity_science/compliant-with-local-controls-collectively-discriminatory-a-governance-architect.md`
3. Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany — Walter Kurz, 2026
   `raw/papers/complexity_science/multi-agent-ai-architecture-for-regulated-insurers-a-generic-ai-framework-under-.md`
4. Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale — Harsh Rao Dhanyamraju, Leonidas Raghav, Aaron Lee, 2026
   `raw/papers/corporate_governance/autonomous-event-driven-multi-agent-orchestration-for-enterprise-ai-at-scale.md`
5. Automated Quantitative Impact Assessment Framework for Artificial Intelligence Systems: Bridging Governance and Engineering Practices — Yu-Chih Wei, Y C Chen, 2026
   `raw/papers/corporate_governance/automated-quantitative-impact-assessment-framework-for-artificial-intelligence-s.md`
6. Who Speaks for the Affected? The Missing Stakeholder Problem in AI Policy Consultations — Ali Sadhik Shaik, 2026
   `raw/papers/corporate_governance/who-speaks-for-the-affected-the-missing-stakeholder-problem-in-ai-policy-consult.md`
7. Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies — Rasika Muralidharan, Haewoon Kwak, Jisun An, 2026
   `raw/papers/complexity_science/behavior-is-not-enough-a-mechanism-based-evaluation-of-social-norm-emergence-in-.md`
