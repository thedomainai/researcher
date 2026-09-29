# 自律的決定と現実効果の間の決定論的境界ゲート

## 概要

自律的決定と現実効果の間の決定論的境界ゲートとは、自律主体(AIエージェントなど)が下した「決定」と、それが世界に及ぼす「実効果」との間に、検証可能な強制境界と人間の上書き権を置く設計原理である。ゲートの厳しさは、不確実性と帰結の大きさに応じて調整される。主体の内部でどれほど高度な判断がなされても、実効果が生じる前に境界で権限が拘束される点が特徴である。

AI Nativeな社会では、意思決定や行動の多くがエージェントに委譲される。このとき、主体の善意や性能を信頼するだけの設計では、誤りが現実の被害に直結しうる。そこで「何を決めたか」ではなく「何が実行を許されるか」を、実行時に決定論的に統制する層が必要になる。ソース[1]は、この境界を組み込むことが自律システムに対して不可欠であると位置づけている。

## メカニズム

この原理は、対象が人間・AI・組織・技術のいずれであっても成立する構造として、次の三要素に整理できる。

1. **実行時の権限拘束**: 提案された行動は、実効果が生じる前に、宣言済みでバージョン管理されたポリシーに照らして評価される。評価結果は行動に紐づいた判定として出され、実行は該当する認可条件と結び付けられる。
2. **不確実性×帰結による権限ゲート**: 不確実性が高いだけ、あるいは帰結が大きいだけでなく、両者が同時に高い場合に、自律性を絞る安全ゲートが働く。
3. **人間による上書き権の保持**: 最終的な権限は、人間が介入・修正できる形で保持される。

構造として一般化すると、「提案する主体」と「効果を許可する境界」を分離し、境界側は提案主体の内部状態を信頼せずに、宣言された規則と状態だけで判定する。これにより、提案主体が人間でも機械でも組織でも、同じ統制が適用できる。

## 理論的背景

**実行時認可(ETA)の形式化[1]**: Meymanは、実行時認可(Execution-Time Authorization)を、実効果を持ちうる行動を扱うAIエージェントなどのための決定論的ガバナンス境界として定義する。ETAは、正規化(canonicalize)された提案行動を、宣言済みでバージョン管理されたポリシーと決定状態に照らして評価し、行動に紐づいた判定を出す。さらに、独立した再構成を支援することを意図した改ざん検知可能な認可アーティファクトを生成する。準拠した実装は、認可境界完全性モデル(ABIM)のもとで、出力の完全性、入力の完全性、再生(replay)の完全性を別々に評価する必要がある。なお同論文は、この定義を完全性テストではなく実装モデルとしている。

**神経哲学的(ニュートロソフィック)な認知制御[2]**: N-CogHCIは、認知的証拠を真・不確定・偽の成分で表し、その状態を用いて人間とAIの権限をリアルタイムに調整する枠組みである。信頼性で重み付けしたマルチモーダル証拠、不一致や欠測のモデル化、AIの認識的不確実性、タスクリスク、人間の専門性を組み合わせ、不確実性と帰結が同時に高いときに自律性を制約する安全ゲートを備える。権限は離散的な変数で、人間のみ、人間主導の共有、均衡した共有、AI主導の共有といった段階から選ばれる。

**人間による上書きと専門知の統合[3]**: Bhadoriyaは、人間の選好や制約を学習し、最適化解を提案しつつ人間の上書きを許すツールを検討している。機械最適化と人間の多様な判断の両立が協働設計の課題であるとされる。

**委譲における運用条件の重要性[4]**: OpenClawに関する73,093件のReddit投稿を価値感応設計で分析した研究では、価値は成果物そのものよりも、ユーザーが実行の周囲に設定する運用条件に集中していた。価値は、成果物を述べる場面では6群中5群で満たされていたが、監督を述べる場面では全6群で多くが満たされていなかった。21の価値には「限定された到達範囲(Bounded Reach)」や「レビュー可能性(Reviewability)」を含む群がある。これは、境界と監督の設計が価値実現の鍵であることを示す実証的知見である。

**制度設計の観点[5]**: Khanは、人間とAIの協働の持続性が、評価、統合、ガバナンス、人間の専門性の活用に関する制度条件に依存すると論じる。制度的評価メカニズムや行動の正規化ループが協働の有効性を左右するとされる。

## AI Nativeな設計への示唆

- **決定と実行の分離**: エージェントの提案と実効果の間に、必ず独立した強制点を置く。強制点は、提案主体の判断ではなく、宣言済みポリシーに基づいて決定論的に判定する。
- **行動の正規化と紐づけ**: 判定は正規化された特定の行動に束縛し、別の行動に流用できないようにする[1]。
- **監査可能な証跡**: 改ざん検知可能な認可記録を残し、第三者が独立に再構成できるようにする[1]。入力・出力・再生の完全性を個別に評価する。
- **リスク比例の権限段階**: 不確実性と帰結の組合せで、人間のみから AI主導までの権限段階を動的に切り替える[2]。低リスク領域は委譲し、両者が高い領域は人間に戻す。
- **上書き経路の常設**: 最適化提案には、人間が修正・拒否できる対話経路を組み込む[3]。
- **監督体験の設計**: 委譲では、実行前の条件設定と実行中の監督が価値実現を左右する[4]。到達範囲の制限やレビュー可能性を、利用者が扱えるインターフェースとして提供する。
- **制度との整合**: 技術的ゲートだけでなく、評価やガバナンスを含む制度条件を整える[5]。

## 関連コンセプト

- [[trust-free-boundary-enforcement-for-autonomous-actors]]: 信頼を前提とせずに実行境界で自律主体を制御する考え方で、本概念と最も近い。
- [[arithmetic-spectral-theory-ai-safety]]: 決定論的なAIガバナンスという観点で関連する。
- [[ai-decision-authority-restructuring]]: AI導入に伴う意思決定権限の再構成を扱う。
- [[layered-governance-and-agency-retention]]: 層別のガバナンスと主体性の保持という点で、上書き権の議論と接続する。
- [[ai-decision-support-systems]]: 人間の判断を支援するシステムとしての位置づけ。
- [[ai-augmented-decision-making]]: 人間とAIの協調的な意思決定。
- [[autonomous-multi-is-systems]]: 自律的な複数システム間での境界統制の対象領域。
- [[autonomous-procurement-architecture]]: 自律的な調達など、実効果を伴う応用領域。

## 参考ソース

1. Edward Meyman (2026) "Execution-Time Authorization for AI Agents: A Formal Framework for Deterministic Governance Boundaries" — `raw/papers/hci/execution-time-authorization-for-ai-agents-a-formal-framework-for-deterministic-.md`
2. Nada Mohamed, Alshaimaa A. Tantawy (2026) "N-CogHCI: A Reliability-Aware Neutrosophic Cognitive Control Framework for Cognitive AI-Enhanced Human–Computer Interaction" — `raw/papers/hci/n-coghci-a-reliability-aware-neutrosophic-cognitive-control-framework-for-cognit.md`
3. Smriti Bhadoriya (2026) "Investigating AI/ML Models that Learn the Preferences and Constraints of Human Decision-Makers to Develop Interactive or Tools that Suggest Optimized Solutions While Allowing for Human Override and Incorporating Expert Judgment" — `raw/papers/hci/investigating-aiml-models-that-learn-the-preferences-and-constraints-of-human-de.md`
4. Renkai Ma, Ruyuan Wan, Xuan Lu, Fan Yang, Chen Chen (2026) "Value-Sensitive Delegation in Everyday AI Agent Use: Evidence from OpenClaw" — `raw/papers/hci/value-sensitive-delegation-in-everyday-ai-agent-use-evidence-from-openclaw.md`
5. Taha Khan (2026) "Sustainable Human-AI Collaboration: A Human-Centered Institutional Design for AI-Mediated Institutions Version 3" — `raw/papers/hci/sustainable-human-ai-collaboration-a-human-centered-institutional-design-for-ai-.md`
