# 実行時認可と定量的制御点の設計

## 概要

実行時認可と定量的制御点の設計とは、AIシステムのガバナンスを「設計時の規範・チェックリスト・倫理審査」だけで完結させず、システムが実際に動いている各時点に、制御点・限界値・自動応答・検証主体を埋め込む考え方である。中核には次の三つの区別がある。

- **可視性**: 何が起きたかを記録・観測する。
- **整列**: システムが全般的に安全であるよう調整する。
- **認可**: この具体的な行為が、実行時点でポリシー上許可されていたかを判定する。

これらは別々の問題であり、ログやダッシュボードが充実していても、個々の行為を実行前に止める仕組みがなければ認可は満たされない。

AI Nativeな社会では、エージェントが人間の逐次的な判断を介さず、認証情報を通じて権限を行使する。事後の説明や設計時の善意に頼る統治は、実行の速度と規模に追いつかない。そのため、権限を最小化し、限界値を超えたら即座に遮断し、その測定を誰が検証するかまで決めておく設計が不変の原理として重要になる。

## メカニズム

この構造は、対象が人間・AI・組織・技術のいずれでも成立する。

1. **設計時と実行時の分離**: 設計時ガバナンスは前提条件を整えるが、決定的な失敗は稼働中に起きる。予測の上書き、ロールバック、監査、エスカレーション、接続劣化時の安全維持は、実行時にしか行えない。
2. **制御点の特定**: 対象のライフサイクルのどこに制御点があるかを明示する。制御点のない管理体制は文書を生むが、安全は生まない。
3. **定量的な限界値**: 各制御点に測定可能な限界を設定し、曖昧な「適切さ」ではなく超過の有無で判定する。
4. **自動応答**: 限界を超えたときに人手の判断を待たず自動的に起動する応答(拒否、停止、縮退、エスカレーション)を定める。
5. **検証主体の明確化**: 測定が正しいことを誰が検証する能力を持つかを定める。判定は第三者が独立して再現・検証できることが望ましい。
6. **権限の最小化と即時遮断**: 権限は実行主体(人間でもエージェントでも)の資格情報に紐づくため、付与範囲を絞り、異常時に即座に取り消せる必要がある。

これは閉ループのフィードバック制御として捉えられる。測定、限界との比較、自動応答、検証という循環が、実行の各時点で回り続ける。

## 理論的背景

**認可の形式的分類**: Meymanの分類論は、「AIガバナンス」という語がログ、ガードレール、モデル整列、ダッシュボード、ポリシーワークフローなどに無差別に使われていると指摘する。そのうえで可視性・整列・認可の三問題を区別し、ベンダーの主張がどの問題を解いているかを対応づける。決定論的AIガバナンスは、実行前の認可層として定義される。同一のガバナンス状態からは同一の判定が得られ、第三者がオフラインで再現できる検証可能な判定成果物を出力する。判定はALLOW / DENY / ABSTAINの三値で構成される。

**HACCPによる制御点の導入**: PaciaroniのHACCP for AIは、AIガバナンスの多くの枠組みがリスクプロセスの実施を要求しても、制御点の位置、各点での測定可能な限界、超過時の自動対応、測定を検証できる主体までは示さないと論じる。これらを補う層として、長年にわたり分散した生産連鎖の見えないハザードを管理してきたHACCPを持ち込む。ISO/IEC 42001、EU AI Act第9条、NIST AI RMFの代替ではなく、それらが前提とするプロセス制御層という位置づけである。

**実行時依存としてのガバナンス**: Patelらは、災害管理AIが事前の倫理審査・データ共有協定・標準チェックリストで統治されがちだが、それは必要でも不完全だと論じる。ガバナンスを実行時依存として捉え直し、80件の文献群から10の実行時制御を、232件の非排他的な対応づけでコード化した。制御あたりの被覆は平均23.2件(中央値21.5、範囲6〜43)で、上位5制御が割り当ての80.2%を占める。被覆の偏りは、実行時制御の一部が十分に研究されていない可能性を示唆する。

**非人間アイデンティティ**: Hossainは、エージェンティックAIが人間の意図ではなく、サービスアカウントやAPI資格情報などの非人間アイデンティティ(NHI)を通じて行動すると論じる。既存のJML(入社・異動・退社)、PAM、ゼロトラストは人間向けに設計されており、そのままの適用は構造的な隔たりを生むとされる。

**AIによる特権アクセス管理**: Yilmaz & Canの章は、クラウドやハイブリッドなど分散環境で従来のルールベースPAMが高度な脅威の検知やアクセスパターンの変化への適応に苦戦していると述べる。振る舞いのベースライン化、リアルタイム異常検知、適応的リスクスコアリング、アクセス判断の自動化といったAI/MLの活用を検討している。

**層分離と実行の真実性**: PDE-OSの設計報告(v0.2、査読前の公開ドラフトで、統制された実証検証は主張していない)は、会話記憶・意味検索・エージェント実行がそれぞれ文脈を回復できても、現在有効な決定に基づき、正しい権限境界内で、実際に持つツールを使い、実行を正直に報告している保証にはならないと指摘する。そのため履歴的証拠と現在の決定を分離し、権限境界と実行の真実性を独立に検証する制御プレーンを提案している。

**決定論的な安全制御器**: Amagi-NIPU v1.1は、時間的即応性・改ざん耐性・証明可能性(TTP Triad)を、六つのハードウェア不変条件とハードウェア常駐の有限状態機械で強制する、決定論的な単一コア安全制御器の仕様を定める。

## AI Nativeな設計への示唆

- **三問題を混同しない**: ログ基盤の整備を認可の達成とみなさない。可視性・整列・認可のそれぞれに対応する機構があるかを点検する。
- **制御点の台帳化**: ライフサイクル上の制御点ごとに、測定指標、限界値、超過時の自動応答、検証主体を一覧化する。空欄がある制御点は未設計とみなす。
- **実行前認可を標準にする**: 高リスクの行為は、実行後の監査ではなく実行前に許可・拒否・保留(判断不能)で判定する。判定根拠は第三者が再現できる形で残す。
- **エージェントの資格情報を統治対象にする**: エージェントごとに識別可能な資格情報を発行し、最小権限とし、異常時に即時失効できるようにする。人間向けの入退社管理をそのまま流用しない。
- **静的規則に振る舞い検知を重ねる**: ルールで説明できない異常を、ベースラインからの逸脱として検出する層を設ける。
- **層ごとに検証を分ける**: 記憶、検索、実行の各層で権限境界と実行報告の真実性を独立に検証し、一つの層の誤りが他へ波及しないようにする。
- **縮退時の安全**: 接続が劣化しても安全側に倒れる挙動や、ロールバック、上書き、エスカレーション経路を事前に用意する。
- **実行時制御の偏りを測る**: 制御ごとの被覆を評価し、手薄な領域に投資する。

## 関連コンセプト

- [[agentic-ai-memory-control]] — 記憶・制御・検証を層として分離する設計と対応する
- [[agentic-workflow-orchestration]] — ワークフロー上の制御点と認可の配置
- [[ai-in-manufacturing-and-quality-assurance]] — HACCPなど品質保証の制御点の発想の源流
- [[opacity-verification-gap]] — 検証主体と検証可能性の問題
- [[human-verification-loop-bias-amplification]] — 人間による検証を制御点に置く際の留意点
- [[cognitive-limits-information-overload]] — 人間の検証能力の限界が自動応答を必要とする理由
- [[computational-limits-forcing-decentralized-autonomy]] — 中央集約制御の限界と分散的な制御の必要
- [[leverage-points]] — 制御点をシステム介入の梃子として捉える視点
- [[mnc-knowledge-flows-and-control]] — 分散組織における統制構造

## 参考ソース

1. Next-generation privileged access management — Erhan Yilmaz, Özgü Can (2026)
   `raw/papers/accounting/next-generation-privileged-access-management.md`
2. HACCP for AI: An Auditable Self-Control Standard for Artificial Intelligence — Simone Paciaroni (2026)
   `raw/papers/accounting/haccp-for-ai-an-auditable-self-control-standard-for-artificial-intelligence.md`
3. Personal Decision & Execution OS: A User-Owned Control Plane for AI-Mediated Decision Continuity and Verified Execution (v0.2) — 정유경 (2026)
   `raw/papers/accounting/personal-decision-execution-os-a-user-owned-control-plane-for-ai-mediated-decisi.md`
4. Governance Is a Runtime Dependency: An Evidence Map and Operational AI Readiness Matrix for Disaster Management — Sandip Patel, Deependra Singh Rawat, Bhavin Gandecha (2026)
   `raw/papers/accounting/governance-is-a-runtime-dependency-an-evidence-map-and-operational-ai-readiness-.md`
5. Non-Human Identity Governance: A Governance Framework for Agentic AI Credentials in Regulated Enterprises — M Maruf Hossain (2026)
   `raw/papers/ai_governance/non-human-identity-governance-a-governance-framework-for-agentic-ai-credentials-.md`
6. A Taxonomy of AI Governance Approaches: Distinguishing Visibility, Alignment, and Authorization — Edward Meyman (2026)
   `raw/papers/ai_governance/a-taxonomy-of-ai-governance-approaches-distinguishing-visibility-alignment-and-a.md`
7. Amagi-NIPU v1.1: Neuro-Immune Processing Unit for Ethical, High-Assurance AI Systems — Alexey Mikhailovich Burlai (2026)
   `raw/papers/ai_governance/amagi-nipu-v11-neuro-immune-processing-unit-for-ethical-high-assurance-ai-system.md`
