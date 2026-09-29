# 意思決定時点での証拠結合と事後復元の限界

## 概要

証拠は、意思決定が行われた瞬間の属性である。その時点で意思決定に結合して記録しなかった場合、事後に得られるのは当時の「行動」ではなく、残存する断片から組み立てた「信念」にとどまる。これが本記事で扱う「事後復元の限界」である。

ソース[6]は、AI障害の説明を求められた組織は「その瞬間になって初めて、自分たちが何を書き残していたかを知る」と述べる。この発見は取り返しがつかない。ここから、証拠の確保は事後対応の手順ではなく、プラットフォーム側の設計制約として扱うべきだという含意が導かれる。

AI Nativeな設計にとって重要なのは、AIが意思決定の参加者、あるいは実行主体になるほど、判断の速度と量が人間の記憶や事後調査の能力を超えるためである。検証可能性、権限、統制はいずれも、事前に設計された記録と介入点に依存する。

## メカニズム

この原理は、対象が人間、AI、組織、技術のいずれでも次の構造として成り立つ。

1. **決定時点での固定**: 判断が下される瞬間に、その根拠となった証拠と、その時点で有効だった規則(ポリシーのバージョン)を結合して記録する。
2. **事後の非対称性**: 記録がなければ、事後の調査は残存物からの推測になる。時間が経つほど、復元できるのは「何を信じていたか」の物語であり、「実際に何が起きたか」ではなくなる。
3. **検証可能性による信頼の担保**: 信頼は主張ではなく、第三者が確かめられる仕組みに支えられる。ソース[1]は、暗号技術とPKIが、行為への主体の結合、データの真正性、監査可能性を支える基盤になると論じる。
4. **事前設計された介入点**: 制限、停止、上書きといった統制は、権限の所在と安全な状態への遷移経路があらかじめ定義されていて初めて実効性を持つ。
5. **役割分担の先行設計**: 自動化と人間判断の境界、意思決定の境界、人間による審査責任は、AI導入より前に定義されているほど堅牢になる。

要するに、証拠・権限・統制はいずれも「後から足せる機能」ではなく、意思決定が起きる前に組み込まれるべき構造である。

## 理論的背景

### AIインシデント対応プロトコル(AIRP)
ソース[6]は、AIインシデントへの対応と復元のためのプロトコルとして、signal、classify、contain、escalate、reconstruct、closeの6段階を定義する。中心要件は「インシデントは、その説明に必要な証拠が意思決定の瞬間に存在し、当時有効だったポリシーバージョンに結合されている場合にのみ説明可能になる」というものである。これは対応チームの手順ではなく、プラットフォームへの設計制約として位置づけられている。

### 暗号基盤と検証可能性
ソース[1]は、AI駆動の知識管理で信頼の問題が単純なデータ保管から、検索・要約・エージェント的ワークフロー全体における完全性、由来、統制された利用へ移ると整理する。NISTのAIリスクマネジメントフレームワークが信頼性を設計・開発の段階から組み込む枠組みとして位置づけられていることも紹介されている。

### 事前設計されたガバナンスと人間の判断
ソース[2]は、品質監視とインシデント対応の枠組み(ガバナンスモデル、運用定義、決定境界、人間の審査責任)がAI導入に先行していた事例を扱う。エージェントAIは証拠の検索、分類、報告、意思決定の準備を支援する拡張として導入され、重大な判断に対する人間の説明責任は維持された。

### ガバナンス決定から運用状態へ
ソース[3]は、AIガバナンスの枠組みが組織の担い手に、AI機能を制限・停止・上書き・変更する権限を与えつつある点に注目する。安全工学の安全状態遷移、サイバーセキュリティの封じ込めと失効の伝播、内部監査による統制設計と運用有効性の評価、実行時保証を手がかりに、承認された組織的ガバナンス介入が上位の保証主張として有用かを検討している。

### 領域別の応用
- ソース[4](航空安全)は、AIが安全上重要な判断を推奨・実行するようになる中で、SMSが明示的な権限境界や、説明可能で復元可能な判断を必要とすると論じる。自動化バイアスや人間の上書き権限も論点である。
- ソース[5](公共調達)は、供給者への義務付けが、購入者に情報取得の権利を与えるとは限らないという「供給者責任」と「購入者統制」の区別を示す。検証の仕組みを契約に埋め込む必要が示唆される。
- ソース[7]は、判断の根拠を版管理された決定記録(Decision Record)に残し、条件変化時に再検討できるようにする、ワークフロー単位の方法を提示する。
- ソース[9]は、透明性・説明可能性、プライバシー、説明責任が、生成AI導入とイノベーション成果の関係を強めるという実証結果を示す。公正性・バイアス統制は異なる振る舞いを示す(抜粋では詳細不明)。

## AI Nativeな設計への示唆

- **証拠を決定の一部として設計する**: ログは事後の付属物ではなく、決定イベントと同時に生成され、ポリシーバージョンと結合されるべきである。
- **記録の完全性を暗号的に担保する**: 主体と行為の結合、真正性、監査可能性を、暗号技術やPKIといった検証可能な仕組みで支える。
- **権限と介入点を事前に定義する**: 誰がどの条件でAI機能を制限・停止できるか、その決定がどう運用状態に反映され伝播するかを、運用前に設計する。
- **人間の判断領域を明示する**: 重大な決定の境界と審査責任をAI導入前に固定し、AIは証拠検索や準備の拡張として位置づける。
- **購入者側の検証権を確保する**: 外部調達では、供給者の義務だけでなく、情報を得る購入者の権利も契約に組み込む。
- **決定を再検討可能にする**: 根拠を版管理して記録し、条件変化に応じて見直せるようにする。
- **説明できることを設計目標にする**: 「後で調べる」ではなく「後で説明できる状態を最初から作る」ことを基準とする。

なお、ソース[6]の抜粋は途中で終わっているため、要件の充足条件の詳細は本記事では扱っていない。

## 関連コンセプト

- [[evidence-bearing-decision-traceability]] — 証拠を伴う意思決定の追跡可能性
- [[decision-event-governance]] — 意思決定イベントを構成単位とするAIガバナンス
- [[assurance-evidence-parity-and-governance-facade]] — 保証と証拠の均衡とガバナンスの見せかけ
- [[ai-decision-authority-restructuring]] — AI組み込みによる意思決定権限の再構成
- [[decision-cycle-compression-and-residual-authority]] — 意思決定サイクルの圧縮と残余権限の設計
- [[ai-explainability-decision-making]] — AI説明可能性と意思決定支援
- [[decision-process-visibility-and-reliance-calibration]] — 意思決定過程の可視性と依存度の較正

## 参考ソース

1. Vincent Lozupone (2026)「Securing Knowledge Ecosystems: The Role of Encryption and PKI in AI-Driven Knowledge Management Systems」
   File: raw/papers/organization_science/securing-knowledge-ecosystems-the-role-of-encryption-and-pki-in-ai-driven-knowle.md
2. Saheli Basu (2026)「Evidence-Grounded AI Operations Workflow: Extending a Human-Designed Quality Monitoring Framework with Agentic AI」
   File: raw/papers/organization_science/evidence-grounded-ai-operations-workflow-extending-a-human-designed-quality-moni.md
3. Jess J. Montgomery (2026)「From Governance Decision to Operational State: An Assurance-Case Perspective on AI Governance Interventions」
   File: raw/papers/organization_science/from-governance-decision-to-operational-state-an-assurance-case-perspective-on-a.md
4. A. F. Clark (2026)「AI as an Aviation Safety Decision Maker」
   File: raw/papers/organization_science/ai-as-an-aviation-safety-decision-maker.md
5. Hasan Alaali (2026)「From AI Governance to Purchaser Control: A Comparative Analysis of Public-Sector AI Contractual Regimes」
   File: raw/papers/organization_science/from-ai-governance-to-purchaser-control-a-comparative-analysis-of-public-sector-.md
6. Nabeel A. Khan (2026)「The AI Incident Response Protocol: Six Stages, and the Evidence a Reconstruction Requires」
   File: raw/papers/organization_science/the-ai-incident-response-protocol-six-stages-and-the-evidence-a-reconstruction-r.md
7. Zafer Demirkol (2026)「From AI Maturity to Reopenable Decisions: The AI Native Transition Method v0.2 as an Open, Workflow-Level Decision Artifact」
   File: raw/papers/organization_science/from-ai-maturity-to-reopenable-decisions-the-ai-native-transition-method-v02-as-.md
9. Tahereh Hasani (2026)「When Does Generative AI Adoption Pay Off? Ethical Governance as a Dynamic Capability in SMEs」
   File: raw/papers/organization_science/when-does-generative-ai-adoption-pay-off-ethical-governance-as-a-dynamic-capabil.md
