# 保証と証拠の均衡:ガバナンスの見せかけ(ラウンダリング)の構造

## 概要

**保証と証拠の均衡(Assurance–Evidence Parity)**とは、ガバナンスが主張する保証水準が、それを支える検証可能な証拠と強制力を上回ってはならない、という不変原理である。両者が乖離した状態では、ガバナンスは形式上は存在しても実質を失う。Meyman(2026)はこの状態を**ガバナンス・ラウンダリング(governance laundering)**と名付けた。定義は「保証の主張が、それを支える証拠または強制の性質を上回っている状態」である。

AI Nativeな社会では、意思決定の多くをAIや自律システムが担う。そこではログ、ダッシュボード、証明書、宣誓書といった「ガバナンスの成果物」が大量に生成される。しかし、それらが個別のAI判断を独立に検証できるとは限らない。成果物の量が信頼の根拠になってしまうと、統治の正統性は空洞化する。したがって、AI Nativeな設計では「何を保証すると主張し、その根拠となる証拠が何か」を対応づけることが基本条件になる。

## メカニズム

この原理は、対象が人間、AI、組織、技術のいずれであっても次の構造で成り立つ。

1. **保証の主張**:主体が「この判断・行為は統制されている」と表明する。
2. **証拠と強制力**:主張を裏づける記録、検証手段、実際に効く制約が存在する。
3. **均衡の判定**:主張の水準が証拠・強制力の水準以下であれば健全である。上回れば、その差分が「見せかけ」となる。
4. **独立検証**:当事者以外が証拠を再検証できることが、正統性の担保になる。

もう一つの軸は時間である。単発のチェックでは、チェック後の変化に対して保証が失効する。Lifecycle Governance Doctrine(LGD)は、生成から廃止までの全期間を連鎖として統治することを求める。その骨格は次の三原則である。

- **誕生時の登録(Registry)**:識別情報、作成者、統治上の責任主体を記録する。
- **重要行為ごとの証拠(Evidence)**:ログ、リスク台帳、変更記録を残す。
- **進化前のゲート(Gates)**:トリガー → 評価 → 認可 → レビューの順に進め、承認権限は人間が持つ。

この二つを合わせると、証拠に基づく段階的ゲートが、各段階で保証の上限を証拠の水準に固定する仕組みになる。

## 理論的背景

### ガバナンス・ラウンダリングの分類学

Meyman(2026)は、AIガバナンス・ツールがしばしば認可層の保証を提供するものとして購入される一方、実際には個別のAI判断の独立検証を支えられない成果物を生むだけだと指摘する。論文は次の枠組みを示す。

- 構造的な形態として、「ポリシー・シアター(policy theater)」と、関連する6つの失敗モード・ファミリーを定義する。
- 証拠グレードのガバナンス要件R1〜R7の7項目を定め、各失敗モードを、違反する要件によって分類する。
- 拡張アンチ・ラウンダリング・プロトコル(EALP)として、手順、合格基準、段階的な結果を備えた7つの診断テストを定式化する。これは同著者の先行研究「可視性・整合・認可を区別するAIガバナンス手法の分類学」のアンチ・ラウンダリング・テストを拡張したものである。

核心的知見は、ガバナンスの正当性が、証拠グレード要件の形式化と独立検証手段によって担保される、という点にある。

### ライフサイクル・ガバナンス

LGD(2026)は、自律的なもの(AI、ロボット、自動運転車、低空システム、データ資産など)の統治は、単点の検査ではなく誕生から退役までの全期間の連鎖でなければならないと主張する。参照モデルは医療機器のライフサイクル規制で、12の領域に一般化されている。GB/Z 185—2026、ISO/IEC 42001、NIST AI RMF、EU AI Act、IETF/CSAの方向性と整合する位置づけであり、LGDは実装層(How)、医療機器分野での具体化、分野横断のマスターテンプレートを提供するとされる。ライフサイクルの追跡と段階的認可は、技術の形態に依らず、責任と説明責任という社会的要件から導かれる根本構造だと整理されている。

### 周辺的な知見

- Albarelliら(2026)は、AIによる監視技術が、個人データの処理能力を組織に集中させ、プライバシー、透明性、説明責任、ガバナンスの懸念を生むと論じる。既存の法規制は、その拡大速度に追いつくのに苦慮しているという。能力の集中と説明責任の断絶は、保証が証拠に先行する典型的な土壌である。
- Lakkita & Tsironis(2026)は、地方政府の行政手続の多くが、複数部門・階層的承認・断片化した情報の流れに依存し、実行を体系的に監視する仕組みを欠くと述べる。行政のデジタルツインは、複雑な手続のデジタル表現によって意思決定の透視可能性を回復する機構として位置づけられる。これは証拠を生成する基盤の一例として読める。

## AI Nativeな設計への示唆

1. **主張と証拠を対で設計する**:ガバナンス上の各主張(「監査済み」「承認済み」など)に、それを検証できる証拠と、逸脱時に働く強制手段を明示的に対応づける。対応のない主張は保証としては扱わない。
2. **成果物と検証可能性を区別する**:ログやダッシュボードが存在することと、個別判断を独立に検証できることは別問題である。導入時に、成果物が独立検証を支えるかを診断する。
3. **全期間でゲートを設ける**:登録から廃止まで、変更・進化のたびに、評価と認可を経るゲートを置く。承認の最終責任は人間に残す。
4. **独立検証を前提にする**:証拠は当事者以外が再検証できる形式で保持する。自己申告の証明だけでは正統性の根拠にならない。
5. **診断を定期的に実施する**:EALPのような診断テストを手続化し、結果を段階的に評価して、保証水準を証拠の水準まで引き下げる、または証拠を強化する。
6. **証拠を生む基盤を整える**:業務手続のデジタル表現など、意思決定の透視可能性を回復する基盤が、証拠の供給源になる。

## 関連コンセプト

- [[ai-governance]] — AIガバナンスの全体像
- [[ai-governance-and-auditing]] — 証拠と独立検証を担う監査の視点
- [[ai-governance-risk-compliance]] — GRCにおける形式的遵守と実効性
- [[ai-governance-and-risk-management]] — リスク管理とライフサイクル
- [[ai-governance-and-regulation]] — 規制との関係
- [[agentic-ai-and-governance]] — 自律的なエージェントの統治
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入速度と統治能力の非対称
- [[surface-openness-masking-structural-power]] — 表層の開放性が構造を覆い隠す点で構造的に類似
- [[institutional-readiness-gates-technology-diffusion]] — 制度的成熟度によるゲートの発想
- [[academic-grey-lit-ai-governance]] — 学術と実務の差異

## 参考ソース

- Lifecycle Governance Doctrine (LGD): Evidence-Gated AI Lifecycle Governance — zhaoxinghua09-cell(2026)
  File: raw/papers/information_systems/lifecycle-governance-doctrine-lgd-evidence-gated-ai-lifecycle-governance.md
- Governance Laundering: A Taxonomy of Failure Modes in AI Compliance Architectures — Edward Meyman(2026)
  File: raw/papers/information_systems/governance-laundering-a-taxonomy-of-failure-modes-in-ai-compliance-architectures.md
- Public Policy Imperatives for Emerging AI Surveillance Technologies — Martina Albarelli, David Eisenberg, Jorge Fresneda, Simone Marras(2026)
  File: raw/papers/innovation_management/public-policy-imperatives-for-emerging-ai-surveillance-technologies.md
- Administrative digital twins for AI-supported performance management in regional government — Athanasia Lakkita, Loukas K. Tsironis(2026)
  File: raw/papers/innovation_management/administrative-digital-twins-for-ai-supported-performance-management-in-regional.md
