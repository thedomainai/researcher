# 信頼を前提としない実行境界による自律主体の制御

## 概要

信頼を前提としない実行境界による制御とは、主体(AIエージェント、人間、組織、国家)の内部状態や意図を信頼できない多主体環境において、**行為が実効を持つ地点(実行点)**に、検証可能な「許可・拒否・保留」の境界を置くことで統制の基盤とする考え方である。統制の根拠を「主体が善良であること」や「モデルの整合性」ではなく、「境界を通過しない行為は実効化しない」という構造に置く。

この原理には限界もある。事前に定めたルールは離散的なカテゴリで連続的な行為空間を近似するため、ルールの一般化限界が**残余リスク**として残る。AI Nativeな社会では、自律エージェントが複数の組織・国家をまたいで行為するため、相互のモデル内部を検証できない状況が常態になる。そのため、この構造的原理は設計上の前提となる。

## メカニズム

対象を入れ替えても成立する構造として、次の3要素に整理できる。

1. **実行時点での認可ゲート**:行為が外部に効果を及ぼす直前に、ALLOW(許可)、DENY(拒否)、ABSTAIN(保留)のいずれかを返す検査点を置く。ソース[2]は、宣言されたワークフロー内のこの種のゲートを、自動化された重大な行為に必要なものと位置づける。
2. **信頼非依存の相互検証**:境界の判定が、相手のモデルや意図への信頼なしに、検証可能な証拠として第三者に示せること。ソース[1]は、相互信頼をモデルに求めずに未承認のAI実効化を防ぐ構想を扱い、ソース[4]は「特定の行為が許可されたこと」の再生可能で独立検証可能な証拠を求める。
3. **離散規則による連続行為空間の近似限界**:許可・拒否といった有限の規則は、連続的に変化する行為を粗く分類する。境界の外側に近似誤差が残り、これが残余リスクとなる。これは人間の判断、組織の内規、AIのポリシーのいずれにも共通して現れる。

この構造は、人間の承認者、組織の内部統制、国家間の枠組み、AIエージェントの権限管理のいずれにも適用できる。

## 理論的背景

**実行境界と主権保全(ソース[1])**:米中間のAI安全対話を背景に、事故時の連絡回線だけでなく、事故が起きる前に何ができるかを問う。提案は、相互にモデルを信頼しなくても成立する「実行の確定性(execution-finality)」アーキテクチャである。競争関係にある主体間でも、技術的な収束点を持てる可能性を示している。

**決定論的統治の多次元性(ソース[2])**:有界な実行ゲートは必要だが、それだけでは十分でない。ゲートは入力の意味、適用されるポリシーが現行のものか、証拠の出所が確立しているか、判定を独立に再構築できるかを、単独では保証しない。閉じた世界の外へ認可の主張を拡張するには、これらの制御と合成可能性が必要になる。ただし、各条件が害の防止にどう寄与するかのメカニズムは十分に解明されていない。

**事前ルールの一般化限界(ソース[3])**:一般ユーザー113名を対象に、行為ごとの人間承認(HITL)、モデルによる自動レビュー(AUTO)、ユーザー作成の帰結ポリシー(POLICY)を比較した。POLICYはHITLより越権行為の阻止率が低かった(約20.1ポイント低下と報告)。決定を事前にルール化することの利得と損失を問う研究であり、離散カテゴリが連続的な行為空間で一般化しきれないという課題を示す。

**可視性・整合性・認可の区別(ソース[4])**:AI統治の問題を、可視性(ログ・監視)、整合性(RLHFやガードレール等)、認可(実行前に許可を証拠付きで示す統治)に区別する。ただし提案フレームワークの充分性は未検証である。

**多エージェント協調と監査可能性(ソース[5])**:病院OSのAI-HOSは、異種のAIエージェントが共有文脈のもとでポリシー制約下の認可行為を実行し、端から端まで監査可能であることを要件とする。複雑性が増す社会での不変的な構造問題を示す事例である。

**責任の分散(ソース[6])**:開発者・デプロイ者・ユーザー・仲介者の制御度が異なるため、法的責任の帰属が難しくなる。制御度に応じた義務を設計するライフサイクル型の枠組みが提案されている。

**エージェントの行動特性(ソース[7])**:コーディングエージェントの文書利用では、指示ファイルや作業メモなどエージェント向け成果物が全文書関連操作の60.5%を占める(古典的技術文書は10.6%)。機械可読な指示が行動を左右することから、境界の設計も機械が解釈できる形式が要る。

## AI Nativeな設計への示唆

- **統制点を実行点に置く**:モデルの内部や意図の検証に頼らず、行為が効果を持つ直前に認可ゲートを置く。
- **判定を三値にする**:許可・拒否だけでなく「保留」を設け、曖昧な場合は人間や上位の検証に回す。
- **証拠を残す**:判定を再生可能・独立検証可能にし、ポリシーの版、入力の意味、証拠の出所を判定に束縛する。
- **ゲートの適用範囲を明示する**:宣言された閉じた世界の内側でのみ認可を主張し、範囲を拡張するときは追加の制御と合成の実証を求める。
- **残余リスクを前提に設計する**:事前ルールは連続的な行為を近似するにすぎないため、境界近傍の行為には行為ごとの承認、監視、事後監査を併用する。
- **責任の帰属を制御度に対応させる**:多主体環境では、各主体が持つ制御の度合いに応じて義務と証拠の責任を割り当てる。
- **機械可読な形式で境界を提供する**:エージェントが読む指示・ポリシーを標準的な形式で整備する。

## 関連コンセプト

- [[execution-time-governance]] — 実行時ガバナンスと権限委譲設計
- [[constraint-anchored-validity-and-verifiable-boundaries]] — 制約による妥当性の担保と検証可能な境界
- [[evidence-obligation-and-ambiguity-retention-in-autonomous-systems]] — 自律システムにおける証拠義務と曖昧性の保持
- [[meaning-bound-decision-record-and-audit-stability]] — 意味バージョン束縛による意思決定の監査安定性
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失と証拠境界の喪失
- [[autonomous-procurement-architecture]] — 自律型調達アーキテクチャ
- [[autonomous-multi-is-systems]] — 自律型マルチ情報システム
- [[human-like-vs-system-like-trust]] — 人間的信頼とシステム的信頼の対比
- [[ai-ethics-trust-transparency]] — AIの倫理・信頼・透明性

## 参考ソース

1. From AI Hotlines to Execution Boundaries: A Sovereignty-Preserving Middle Ground for U.S.–China AI Safety — Sangam Das, 2026
   File: raw/papers/finance_corporate/from-ai-hotlines-to-execution-boundaries-a-sovereignty-preserving-middle-ground-.md
2. Deterministic Governance Is Multi‐Dimensional: Beyond Bounded Execution Gating in AI Systems — Edward Meyman, 2026
   File: raw/papers/hci/deterministic-governance-is-multidimensional-beyond-bounded-execution-gating-in-.md
3. Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach? — Ting Yan, 2026
   File: raw/papers/hci/do-user-authored-permission-policies-improve-protection-against-ai-agent-overrea.md
4. The Enterprise AI Governance Buyer's Guide — FERZ Inc., Edward Meyman, 2026
   File: raw/papers/hci/the-enterprise-ai-governance-buyers-guide.md
5. AI-HOS: An AI-Native Hospital Operating System with a Healthcare Agent Interaction Protocol for Context-Centric, Policy-Governed Clinical Workflow Orchestration — Mohamed Salah Ramadan, 2026
   File: raw/papers/hci/ai-hos-an-ai-native-hospital-operating-system-with-a-healthcare-agent-interactio.md
6. Artificial Intelligence and Cyber Law in India: Recalibrating Legal Responsibility in The Age of Generative AI — Sagar Vilas Shelke, 2026
   File: raw/papers/hci/artificial-intelligence-and-cyber-law-in-india-recalibrating-legal-responsibilit.md
7. From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of How Coding Agents Discover, Read, and Write Technical Documentation — Zhijun Gao, Jing Chen, 2026
   File: raw/papers/hci/from-agent-behaviour-to-agent-friendly-documentation-an-empirical-study-of-how-c.md
