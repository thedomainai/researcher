# 検証の多様性と評価者の無限後退

## 概要

「検証の多様性と評価者の無限後退」は、検証者自身の信頼性を同種の検証で保証しようとすると原理的に閉じない、という構造的問題と、その対処原理を扱うTier 1(不変原理)の概念である。AIの出力を別のAIが評価する構成では、「その評価者は信頼できるのか」という問いが生じる。これを評価者でさらに評価する構成にしても、問いは一段上に移るだけである。これが評価者の無限後退である。

この後退は、次の二つの組み合わせで系全体の信頼を担保することで実務的に扱う。

1. **独立で異質な多層検証**: 検証手段を多様化し、共通原因による同時故障を抑える。
2. **決定論的な監視・拒否可能性**: 確率的に振る舞う要素を、決定論的な境界の内側に封じ込める。

AI Nativeな設計では、生成や判断の多くを確率的なモデルが担う。そのため「誰が・何が検証するのか」を設計の中心に置かないと、検証そのものが単一障害点になる。

## メカニズム

このメカニズムは、対象が人間、AI、組織、技術のいずれでも成立する構造として整理できる。

**1. 後退の構造**
検証者Vが対象Xを評価するとき、Vの信頼性は別の検証者V′を必要とする。V′がVと同種であれば、同じ盲点や失敗様式を共有しうる。このため同種の検証を積み重ねても信頼は閉じない。自動評価システム自身の信頼性判定は自動化できない、という本質的なパラドックスがここにある(ソース1)。

**2. 共通原因故障の抑制**
後退は、検証手段を異質にして独立性を確保することで実務上の許容範囲に収める。同じ種類の検証を重ねるのではなく、原理の異なる検証(統計的指標、決定論的ルール、人間による確認、冗長な実装など)を組み合わせる。単一の検証メカニズムでは複雑なAI支援システムに不十分だという指摘は、この点に対応する(ソース4)。

**3. 決定論的境界による封じ込め**
確率的な要素(LLMなど)には、決定論的で監査可能な層が最終的な権限を持たせる。モデルが直接データを変更できず、検証・認可・確認・冪等性制御などを通す構成がその例である(ソース2)。決定論的な層は、挙動が再現でき、監査できる。

**4. 拒否可能性**
系が「拒否」に対して回復できるか、すなわち想定条件が崩れたときに耐えられるかが、信頼の条件になる。秩序は既定の状態ではなく、維持されている平衡として扱われる(ソース3)。

## 理論的背景

**LLM-as-Judge(LaJ)の安全論証(ソース1)**
Cleggらは、安全クリティカルなタスクを大規模に処理する場合(例: 臨床トリアージ)には何らかの自動評価が必要になると述べる。LaJ評価は通常、単一の誤判定のリスクを分散させる「指標の籠(basket of metrics)」の形をとる。論文は、こうした比較指標が安全保証に十分かを検討し、LaJ評価を構造化し正当化するための安全論証パターンを提示している。周術期リスク評価という臨床例への適用も論じている。

**Backend-authoritative アーキテクチャ(ソース2)**
AWAは、LLMに自然言語の解釈、意図の識別、項目抽出、応答生成を担わせる。一方で、LLMがビジネスデータを直接変更することは許さない。すべての業務アクションは、決定論的なバックエンド検証、テナント固有設定、確認要件、顧客検証、認可チェック、冪等性制御を通過する。確率的推論と決定論的実行の分離という原則の具体例である。ただし、この実装はビジネスプロセスが中心である点に留意が必要である。

**Refusal HeuristicとSVAR(ソース3)**
Truongのワーキングペーパーは、「誰か、あるいは何かが従うことを拒んだらどうなるか」を問う敵対的視点を提案する。運用手法SVARは、Authority Dependency、Assumption Fragility、Internal Adversariality、Theater Gap、Adaptive Resilienceの5次元を検討する。証拠指向の尺度(Denialから「Changed and Re-tested」まで)を用い、最低の実質スコアを採用する規則によって、強力な文書化や計装が未検証の弱点を覆い隠すことを防ぐ。

**検証の多様性(T3-DEF)(ソース4)**
Leeの枠組みは、AI支援システムにおける再帰的な運用上の脆弱性と検証の多様性を扱う。ソースの提示情報では、単一の検証機構では足りず、多層的検証が必要であるという点が核心的知見とされている。

**分散環境での安全フォールバック(ソース5)**
Federated Uncertainty Consensusは、クラウドに判断を委ねられない切断環境のエッジAIを対象とする。各ノードがConformal Predictionによる局所的な不確実性定量化を行い、中央サーバーに依存せず合意形成で安全性を担保することを狙う。検証を単一の中心に集約しない構造の一例である。

**決定論的な安全モニタ(ソース6)**
HOLDは、ミッションクリティカルなAIシステムのための決定論的安全モニタである。提示された知見によれば、信頼性は監査可能性と決定の再現可能性に依存する。ただし、その実装形式は進化しうる。

**計算・タイミング・分離の枠組み(ソース7)**
ソフトウェア定義車両(SDV)では、ブレーキなどの機能が、物理AIワークロードも実行する集中型の異種エッジ計算基盤に統合される。これは固定ECUや単純なタイミング前提を崩し、ASIL-Dブレーキ機能の決定論性、分離、フェイルオペレーショナルな挙動の保証を難しくする。論文は、デュアルコントローラ、冗長な低電圧電源系、スマート電動機械式ブレーキコーナーアクチュエータを備えた分散型ブレーキ・バイ・ワイヤを土台に、compute、timing、isolationの3次元で枠組みを提案する。

## AI Nativeな設計への示唆

- **評価者を評価対象から外さない**: 自動評価器の信頼性判定は自動化できないため、評価器自体を検証対象として設計に組み込み、人間や別原理の検証を残す。
- **異質性を意図して確保する**: 同種の評価を重ねるのではなく、原理の異なる検証(統計指標、決定論的ルール、人間の確認、冗長構成)を組み合わせ、共通原因故障を抑える。
- **確率的な層に最終権限を与えない**: モデルの出力は提案とし、実行は決定論的な検証・認可・確認・冪等性制御の層が担う。
- **拒否できる設計にする**: 系が拒否や想定外に対して回復できるかを、実際に演習して確認する。書類や計装の充実で代替せず、最低スコア規則のように弱い次元を優先して評価する。
- **中央への依存を減らす**: 通信断などで中央の検証者が使えない場合に備え、局所的な不確実性定量化と合意による縮退動作を用意する。
- **監査可能性と再現性を保つ**: 決定論的モニタの判断は再現でき、後から監査できるようにする。
- **隔離と冗長性を設計する**: 安全クリティカルな機能は、異質なタイミング要求を持つ他の負荷から分離し、冗長構成でフェイルオペレーショナルを担保する。

## 関連コンセプト

- [[structural-separation-of-verification-from-governed-system]] — 検証機構を被統治系から分離する原理
- [[structural-separation-and-hierarchical-verification]] — 機能分離と階層的検証によるエラー伝播の抑制
- [[hierarchical-recursive-verification-and-accountability]] — 再帰的・階層的検証と説明責任
- [[verification-cost-and-trust-testing-of-automated-advisors]] — 自動化システムの検証コストと圧力試験
- [[evidence-grounded-role-separated-agent-coordination]] — 役割分離型エージェント協調と検証の分離
- [[opacity-verification-gap]] — 不透明性と検証可能性のギャップ
- [[costly-verification-allocation-tradeoff]] — 検査コストと精度の配分
- [[human-verification-loop-bias-amplification]] — 人間の検証ループにおけるバイアス増幅
- [[verification-to-authority-conversion-gap]] — 検証可能性から実効的権威への変換ギャップ

## 参考ソース

1. Arguing the Safety of Agentic AI using LLM-as-Judge Evaluations — Kester Clegg, Richard David Hawkins, Tom Lawton, Ibrahim Habli (2026)
   File: raw/papers/systems_engineering/arguing-the-safety-of-agentic-ai-using-llm-as-judge-evaluations.md
2. AWA: An LLM-First, Backend-Authoritative Architecture for Multi-Tenant Conversational Business Automation — Hari R Chandran (2026)
   File: raw/papers/systems_engineering/awa-an-llm-first-backend-authoritative-architecture-for-multi-tenant-conversatio.md
3. The Refusal Heuristic: A Proposed Stress Test for Adversarial Systems — Resilience Under Disobedience, Ambiguity, and Adversarial Pressure — Narnaiezzsshaa Truong (2026)
   File: raw/papers/systems_engineering/the-refusal-heuristic-a-proposed-stress-test-for-adversarial-systems-resilience-.md
4. T3-DEF: A Socio-Technical Framework for Recursive Operational Vulnerability and Verification Diversity in AI-Assisted Systems — Dae-Ryung Lee (2026)
   File: raw/papers/systems_engineering/t3-def-a-socio-technical-framework-for-recursive-operational-vulnerability-and-v.md
5. Federated Uncertainty Consensus: Swarm-Level Safety Fallbacks for Disconnected Edge AI — Chidiebere Christopher (2026)
   File: raw/papers/systems_engineering/federated-uncertainty-consensus-swarm-level-safety-fallbacks-for-disconnected-ed.md
6. HOLD a Deterministic Safety Monitor for Mission Critical AI Systems — Omar Lone, Hans Dermot Doran (2026)
   File: raw/papers/systems_engineering/hold-a-deterministic-safety-monitor-for-mission-critical-ai-systems.md
7. Architecting Safety-Critical Systems for AI-Enabled Software-Defined Vehicles: A Compute, Timing, and Isolation Framework with a Brake System Case Study — Soumyasudharsan Srinivasaraghavan (2026)
   File: raw/papers/systems_engineering/architecting-safety-critical-systems-for-ai-enabled-software-defined-vehicles-a-.md
