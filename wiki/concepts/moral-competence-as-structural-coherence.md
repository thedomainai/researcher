# 構造的一貫性としての道徳的能力と価値多元性下の統治

## 概要

価値の「正解」そのものが争われる状況では、AIや組織の判断を「内容が正しいか」で評価することが原理的に難しい。この概念は、評価の軸を**内容の正しさ**から**判断の構造的一貫性・論証の構造的品質**へ移し、さらに、ステークホルダー間の利害対立を技術の最適化ではなく**制度設計**で扱うべきだと整理する不変原理である。

AI Nativeな社会では、AIが判断や行政的裁量、規制執行にまで組み込まれていく。そのとき「どの価値が正しいか」という合意を待たずに、実際に運用できる評価基準と統治の型が必要になる。構造的一貫性は、正解の不在を前提にしても機能する評価の「床(structural floor)」を提供する。

## メカニズム

この原理は、評価対象が人間・AI・組織・技術のいずれであっても成り立つ構造として、次の三つに整理できる。

1. **形式的一貫性による評価**: 判断主体を「状況から判定への写像(政策)」とみなす。道徳的に関連する特徴が保たれる限り判定は不変で、それが変われば判定も変わる。この性質は、道徳基準や専門家の基準を参照せず、振る舞いだけから評価できる。
2. **価値多元性下の手続的正当性**: 正解が一つに定まらない場合、正当性は結論の内容ではなく、批判的な問いに対して防御を構築できるか、判断過程が透明で説明責任へ制度的にアクセスできるか、といった手続の質に宿る。
3. **利害対立の制度的処理**: ステークホルダーごとに公平性・透明性・説明責任・精度・不確実性への関心が異なる場合、それは技術パラメータの調整では解消しない構造的問題であり、制度による調停が必要になる。

## 理論的背景

### 道徳的能力の4つの構造条件

Libertらの論文「Moral Competence Before Moral Content」は、価値多元性のもとでは正しい目標が存在しないため、システムの振る舞いが**一貫した政策**を表現していることが共通の前提条件になると論じる。そのための構造条件として、次の4つを導入している。

- 判定の安定性(verdict stability)
- 単調性(monotonicity)
- 決定性(decisiveness)
- パレート実行可能性(Pareto viability)

これらは道徳基準にも専門家の基準にも依拠せず、行動のみから評価できる「道徳的能力」の一形態を測る。規範的な目標ではなく、アラインメントの構造的な床として位置づけられている。論文はLLMエージェントが道徳的ジレンマに直面する3つのシミュレーション配備でこの方法論を示し、9つのフロンティアモデルを評価している(具体的な結果は、提供された抜粋の範囲では確認できない)。

### 論証分析による説明責任の測定

Henselmansらの論文は、AI監督手法が検証のために正解(ground truth)を必要とする一方で、適切なAIの振る舞いが何かは争われている、という問題を出発点とする。代替基準として、批判的な問いに応じてモデルが自らの判定を防御できる**構造的な質**を提案する。測定にはWaltonの論証スキーム理論とGovierの論証の妥当性(cogency)基準に基づく4フェーズの弁証法的プロトコルを用いる。このプロトコルは推論の枠組みに適応的で、多肢選択形式を超えて適用でき、判定に先立つ推論と事後的な正当化の両方を扱う。9つのフロンティアモデルと、曖昧性の高い200個のMoralChoice項目(6,778個の判定者採点セル)で検証されている。

### 利害対立と制度

リスクアセスメントと予測的警察活動に関する論文は、システム思考とデザイン思考を用い、アルゴリズムのバイアス、投資、データ品質、公共の信頼、制度的対応の間の強化・均衡フィードバックループを特定する。また、市民・司法・科学・アドボカシーの4群からなるステークホルダー枠組みを示し、各群が公平性・透明性・説明責任・精度・不確実性・監督について異なる関心を持つことを整理している。ここから、価値観の対立は技術設計の最適化だけでは解決できない構造的問題を生む、という含意が得られる。

### 統治の正当性

ガバナンス原則に関する論文は、権力システムの正当性が意思決定プロセスの透明性と説明責任への制度的アクセスに依存すると論じる。ブラックボックス問題、責任の拡散、アルゴリズムによる裁量といった課題に対し、法的保護・監督・透明性規範を組み合わせる規範モデルを提案している。

補助的な知見として、倫理的AIのフレームワーク(政府・企業・学術・アルゴリズムという起源別に整理)には合意の余地があるが、その運用は制度的背景によって定義されるとされる。インドの事例研究も、アルゴリズム的正義が特定の制度的文脈に依存する一方、統制原理そのものは普遍的課題だと示唆する。

## AI Nativeな設計への示唆

- **正解ではなく一貫性を検査する**: 評価では、道徳的に無関係な変化に対する判定の不変性と、関連する特徴の変化に対する感度を、振る舞いから直接測定する。判定の安定性・単調性・決定性・パレート実行可能性を最低限の受け入れ条件とできる。
- **論証の耐久性を説明責任の指標にする**: 判定だけでなく、批判的質問に対する防御の構造的品質(論証スキームの整合性)を検査する。推論過程と事後的正当化の双方を対象にする。
- **構造的な床と規範的目標を分離する**: 一貫性は必要条件であって、価値内容の正しさを保証しない。価値内容の決定は、多様なステークホルダーが関与する制度的プロセスに委ねる。
- **利害対立を制度に委ねる**: 精度向上やバイアス低減といった技術最適化は、ステークホルダー間の対立を解消しない。調停・監督・異議申立ての仕組みを制度として設計する。
- **説明責任への制度的アクセスを保証する**: 意思決定の透明性と、影響を受ける者が説明責任に到達できる経路を、正当性の条件として組み込む。

## 関連コンセプト

- [[ai-alignment-and-moral-agency]] — 価値多元性下でのアラインメントと道徳的エージェンシー
- [[ai-ethics-and-moral-agency]] — AIの倫理的エージェント性
- [[ethical-value-alignment-systems]] — 倫理的価値整合システム
- [[multi-stakeholder-value-dynamics]] — ステークホルダー間の価値動態
- [[corporate-value-maximization]] — 価値最大化とステークホルダー論の対立
- [[ai-coherence-collapse]] — 判断の一貫性が崩れる現象
- [[evidence-bearing-decision-traceability]] — 意思決定の追跡可能性と説明責任
- [[structural-separation-of-verification-from-governed-system]] — 検証機構の構造的分離
- [[prosocial-moral-decision-making]] — 向社会的道徳意思決定

## 参考ソース

1. Henselmans, D. R., Prinzhorn, D. W. E., Libert, A. (2026). *Measuring AI Accountability Through Argumentation Analysis: Can Model Reasoning Withstand Scrutiny?* — `raw/papers/ai_governance/measuring-ai-accountability-through-argumentation-analysis-can-model-reasoning-w.md`
2. Libert, A., Prinzhorn, D. W. E., Henselmans, D. R. (2026). *Moral Competence Before Moral Content: Why LLM Agents Lack the Prerequisites for Coherent Alignment* — `raw/papers/ai_governance/moral-competence-before-moral-content-why-llm-agents-lack-the-prerequisites-for-.md`
3. Vasikhanov, A., Sultanbekova, A., Manap, A. (2026). *Critical Issues with the Application of Algorithms in Risk Assessment and Predictive Policing* — `raw/papers/ai_governance/critical-issues-with-the-application-of-algorithms-in-risk-assessment-and-predic.md`
4. Kumar, S., Roopa, U. (2026). *Principles of Good Governance in the Age of AI* — `raw/papers/ai_governance/principles-of-good-governance-in-the-age-of-ai.md`
5. Divya, V., Krishnan, S. B. (2026). *Towards Ethical AI: A Structured Review of Responsible Development and Deployment Practices* — `raw/papers/ai_governance/towards-ethical-ai-a-structured-review-of-responsible-development-and-deployment.md`
6. el-Rakhawi, M. K. A. (2026). *Algorithmic Justice in the Platform Republic: Constitutional Rights, Accountability, and the Emerging AI Governance Framework in India* — `raw/papers/ai_governance/algorithmic-justice-in-the-platform-republic-constitutional-rights-accountabilit.md`
