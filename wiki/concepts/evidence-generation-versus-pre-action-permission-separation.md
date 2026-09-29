# 証拠生成と行為許可の分離(観測は執行ではない)

## 概要

**証拠生成と行為許可の分離**とは、行為の記録・監視・説明をいくら積み上げても、その行為が起きるかどうかは制御されない、という不変原理である。ログ、ダッシュボード、説明可能性の成果物、ドリフト検知、改ざん防止された監査バンドルは、いずれも「何が起きたか」を示す証拠を生成する。しかし、実行の直前に許可・拒否・保留を返す関門がなければ、それらは行為の成立条件にならない。

ソース[1]はこの区別を、次の二つの類型で整理している。

- **証拠ルーティング型のコンプライアンス**:成果物を収集・変換し、レビューへ回す。
- **実行時認可境界**:統治対象の効果の発生を、行為に紐づいたALLOW判定を伴う認可アーティファクトの存在に条件づける。

AI Nativeな設計で重要になるのは、AIが文章生成から自律的な実行(データベースへの書き込み、取引の開始、インフラの変更)へ移るからである。ソース[3]は、この移行によって統治の問題が「行動の観察」から「行為の認可」へ移ると論じている。事後に説明できることと、事前に止められることは別の機能であり、規範遵守には後者を担う構造が別途必要になる。

## メカニズム

この原理は、行為主体が人間、AI、組織、技術システムのいずれであっても成立する。構造は三つの要素に分解できる。

### 1. 観測と執行の機能的非等価性

観測は行為の後(または最中)に情報を生む。執行は行為の前に、その行為を通すか止めるかを決める。証拠が増えても、行為の可否を条件づける経路が存在しなければ、行為の発生には影響しない。監査に備えた状態(audit readiness)や規制上のトレーサビリティは、実行の統制とは別の性質である。

### 2. 実行前ゲートによる許可判定

ソース[2]は、宣言されたワークフロー内でALLOW、DENY、ABSTAINのいずれかを返す実行前チェックを「境界づけられた実行ゲート」と呼ぶ。ソース[3]は、認可境界の性質として、迂回不能な実行時ゲーティングや決定論的な検証などを挙げている。要点は、ゲートが行為の効果が現実になる決定境界に置かれ、迂回できないことである。「保留」を含む三値の応答は、判断できない状況を黙って通過させないための設計でもある。

### 3. 観察と判定の役割分離

観察する機能と判定する機能は分けられる。ソース[5]は、監視機能を「観察し報告するが、裁定はしない」ものとして設計し、この分離を注意容量の限界から必然となる構造とみなしている。継続的な監視の範囲は、個々の人間の注意容量を超えるからである。観察側が判定まで担うと、監視の劣化や飽和がそのまま判定の劣化になる。

## 理論的背景

**観測は執行ではないという教義的枠組み(ソース[1])**:コンプライアンス計装は大量の証拠を生み出せるが、統治対象の行為が起きるかどうかは制御しない。多くの現行システムは、行為の時点で認可を実行の条件にしていない。この論文は、証拠ルーティングと実行時認可境界という区別を軸に、コンプライアンス計測だけでは実行時の規範遵守を保証できないと主張する。

**監視から認可への構造転換(ソース[3])**:監視ベースのアーキテクチャは何が起きたかを記録するが、特定の行為が実行前に許可されていたかは判定しない。この論文は、EU、米国、アジア太平洋の規制枠組みに共通する曖昧さを指摘する。それは、AIの意図が現実の効果になる決定境界で、執行の基本要素(enforcement primitive)が十分に規定されていないという点である。そして、影響の大きいエージェント型の展開では、監視だけでは執行水準の要件を満たせないと論じる。

**単一ゲートの限界(ソース[2])**:実行前ゲートは、自動化された重大な行為に必要であり、閉じた世界の内側では本物の事前認可を支えうる。しかしゲートだけでは、入力の意味、適用される政策が現に有効な政策であるか、証拠の出自が確立されているか、判定を独立に再構成できるか、を保証しない。決定論的ガバナンスには、これらを含む多次元の統制が必要になる。

**実行ギャップ(ソース[4])**:方針、コンプライアンスのチェックリスト、人間による承認(human-in-the-loop)といった従来の統治機構は、人と文書を統治するものであり、AI判断の実行時そのものを統治しない。問うべきは、AI支援による行為のすべてが実行前に正当に認可されていたことを組織が証明できるか、である。統治を事後的なコンプライアンス活動として扱うと、組織は大きなリスクにさらされる。

**観察と判定の分離の必然性(ソース[5])**:委任型の一貫性監視のアーキテクチャは、ガーディアン(観察機能)のドリフト、処理量の飽和、偽りの安心といった失敗モードを分類し、監視機能が基準に対して較正され続けるための二次検証サイクルを規定する。

**計測基盤の重要性(ソース[6])**:AIの信頼性は、モデル自体と同程度かそれ以上に、周辺のデータパイプライン、データ契約、計測システムで決まる。この論文は、安全でないデプロイをゲートで止める仕組みも含め、本番環境の観測・評価・ゲートが断片的で場当たり的になっている点を課題として挙げる。観測基盤は必要条件だが、それだけでは許可判定にならない点で、他のソースと補完的である。

## AI Nativeな設計への示唆

- **記録の充実を統制の達成とみなさない。** ログや説明可能性の整備は、監査対応力を高めても、行為の発生を制御しない。統制の有無は「実行が認可に条件づけられているか」で判断する。
- **ゲートを効果の発生点に置く。** 書き込み、送金、インフラ変更など、意図が現実の効果になる境界に、迂回できない認可を配置する。
- **応答を三値にする。** 許可・拒否・保留を明示的に返し、判断不能な場合の既定動作を設計に含める。
- **認可を行為に束縛する。** 認可アーティファクトは、特定の行為に紐づけて発行し、一般的な承認と混同しない。
- **観察と判定の役割を分ける。** 監視機能は報告に徹し、裁定は別の機能が担う。監視側の劣化(ドリフト、飽和、偽りの安心)を検出する二次検証も組み込む。
- **ゲートの適用範囲を明示する。** 単一ゲートの主張が及ぶのは宣言された閉じた世界までである。入力の意味、政策の有効性、証拠の出自、再現可能性は、別途統制する必要がある。

## 関連コンセプト

- [[pre-irreversibility-authority-and-constraint-embedding]] — 不可逆化の前に権限判断を置くという、実行前ゲートの考え方と直結する。
- [[structural-separation-of-verification-from-governed-system]] — 検証機構を被統治系から分離する構造。観察と判定の分離と対応する。
- [[structural-separation-and-hierarchical-verification]] — 機能分離と階層的検証によるエラー伝播の抑制。
- [[evidence-bearing-decision-traceability]] — 証拠を伴う意思決定の追跡可能性。証拠生成の側の要件を扱う。
- [[generation-governance-impedance-mismatch]] — 生成の速度とガバナンスの不整合。
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入速度が統治能力を上回るギャップ。
- [[evidence-grounded-role-separated-agent-coordination]] — 役割分離型のエージェント協調と検証の分離。
- [[human-finite-capacity-and-stable-adaptation-patterns]] — 人間の有限な処理資源。監視の注意容量の限界に関わる。

## 参考ソース

1. Edward Meyman (2026). *Observability Is Not Enforcement: A Doctrinal Framework for Distinguishing Compliance Instrumentation from Runtime Authorization in AI Governance Architectures (Working Paper v2.0)*. File: `raw/papers/information_systems/observability-is-not-enforcement-a-doctrinal-framework-for-distinguishing-compli.md`
2. Edward Meyman (2026). *Deterministic Governance Is Multi-Dimensional: Beyond Authorization in AI Systems*. File: `raw/papers/information_systems/deterministic-governance-is-multi-dimensional-beyond-authorization-in-ai-systems.md`
3. Edward Meyman (2026). *From Monitoring to Authorization: The Structural Shift in Agentic AI Governance*. File: `raw/papers/information_systems/from-monitoring-to-authorization-the-structural-shift-in-agentic-ai-governance.md`
4. Michal Harcej (2026). *How AI is Impacting Corporate Governance*. File: `raw/papers/information_systems/how-ai-is-impacting-corporate-governance.md`
5. Thomas Gantz (2026). *Delegated Coherence Monitoring: AI-Assisted Verification and Drift Detection Under Human Governance*. File: `raw/papers/information_systems/delegated-coherence-monitoring-ai-assisted-verification-and-drift-detection-unde.md`
6. Sheena Sathri (2026). *Evaluation and Observability Frameworks for Reliable AI Deployment at Enterprise Scale: Patterns from Production Environments*. File: `raw/papers/information_systems/evaluation-and-observability-frameworks-for-reliable-ai-deployment-at-enterprise.md`
