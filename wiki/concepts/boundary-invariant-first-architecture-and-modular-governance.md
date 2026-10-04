# 境界制約を第一義とするアーキテクチャと用途別モジュール型統治

## 概要

境界制約を第一義とするアーキテクチャ(Boundary-First Architecture)とは、管轄やデータ越境などの**境界制約を「最適化の対象」ではなく「許容される構造を決める先行事実」として扱う**設計原理である。あわせて、用途(ユースケース)ごとのリスクプロファイルに応じて、法的・組織的な統治構造を**展開(デプロイ)前に**モジュールとして設計する必要があるという主張を含む(用途別モジュール型統治)。

AI Nativeな社会設計で重要になるのは、AIの導入が「まず技術を選び、あとから規制や契約に適合させる」順序で進みやすいためである。この順序では、コストで選んだ構成を「条項が許すはずだ」と後付けで正当化することになりやすい。本概念はこの順序を反転させ、制約→許容構造→最適化という順で設計することを求める。さらに、モデル単位の統制や全社一律の方針では、用途固有の組織的関係を捉えきれないという統治の空白にも対処する。

## メカニズム

この原理は、対象が人間・AI・組織・技術のいずれであっても成立する構造として、次の3つの段階に整理できる。

1. **制約による設計空間の限定**
   境界(管轄、データ所在、権限範囲など)は、選択肢を比較する前に許容される構造の集合を決める。制約は最適化の目的関数に入る項目ではなく、最適化が動ける範囲を定める。「データは管轄外に出してはならない」という文言は障害ではなく、その展開の構造に関する最初の事実である。

2. **リスク階層別のモジュール化**
   用途ごとにリスクプロファイルが異なるため、統治構造も一様にはできない。用途を中間的な境界単位として捉え、その周囲に責任と機能を束ねたモジュールを設け、段階的に実装する。これは展開に先行して行う。

3. **文言・定義による義務の固定**
   義務は定義された役割や用語に付着し、文書・契約・調達ファイルを通じて、元の会話が終わった後も伝播する。したがって、日常的に同義に使われる語であっても、法的・契約的・証拠上の重みが異なりうる。用語の選択は、そのまま義務の範囲の選択になる。

この3段階は、「先に境界を確定する」「境界の内側を用途別に区切る」「境界と区切りを言葉で固定する」という共通の骨格を持つ。主体が人間の組織であっても、AIシステムであっても、技術インフラであっても、同じ順序で適用できる。

## 理論的背景

### 用語と義務の結合(ソース1)

Patronの研究ノートは、欧州のAIガバナンスが大部分「言葉」を通じて運用されていると論じる。義務は定義された役割に付着し、証拠は文書として蓄積され、主張は契約や調達ファイルを通じて流通する。研究は、user と deployer、provider と vendor、training と AI literacy、certificate と certification、compliance と conformity といった、実務上は同義に見える語が異なる法的・契約的・証拠上の重みを持つことを扱う。方法は文書分析で、各定義や条項を一次資料に遡り、主張を法、公式ガイダンス、標準、認定実務、著者分析、著者提案モデルに分類している。同一の実質的概念が立法過程で言い換えられうるという知見は、言語的曖昧性と立法過程の結合から生じる現象として位置づけられる。

### データ越境と境界不変則(ソース2)

Khanの仕様書は、データ越境に関する制約を「Boundary Invariant」をデータ居住境界クラスに適用した実例として示す。条項が境界であり、トポロジーは最適化であり、パターンは越えてはならない条項の下での最適化である、という位置づけである。単一のワークロードクラスの水準で、次の3パターンが列挙される。

- **Sovereign Silo**:データが一切外へ出ない。
- **Federated**:名指しされた派生成果物は移動できるが、元データは移動できない。
- **Regional Hub**:関与する全管轄が受け入れる送付先への移転が許される。

Hybridは第4のパターンではなく、副題のとおり「第4は選択肢ではない」とされる。境界制約が許容されるアーキテクチャの型を決定論的に規定するという主張である。

### 用途別モジュール型の法的・組織的構造(ソース3)

OkunoとOkunoは、企業システム工学、社会技術的ガバナンス、モジュール性理論、アカウンタビリティ研究、組織法を統合した設計理論的研究として、AIのユースケースを企業システムの中間的な境界とみなす。そのうえで、人間と企業の責任をこの境界の周りに構造化する一つの法的・組織的アーキテクチャとして「モジュール型法人格(modular legal personhood)」を展開する。この概念はAIに法人格や自律的責任を帰属させるものではない。枠組みは、接続されたガバナンス機能、段階的実装、評価メカニズムを規定する。異なるユースケースのリスクプロファイルには異なる構造が必要であり、その実装は展開に先行する、というのが核心的知見である。

### 補助的知見(ソース4)

ラテンアメリカにおけるAIのプライバシーリスクを扱う報告は、分散型識別子、検証可能な資格情報、ゼロ知識証明といった暗号技術基盤が、AI起因のプライバシーリスクに対する実用的インフラとなりうるかを、スコーピングレビューと22件の半構造化インタビュー、5件の事例研究で検討している。この文脈では、データ主権の非対称性を緩和する技術基盤が具体技術に依存しつつも、情報コントロール権という不変の原理を扱う点が本概念と接続する(Tier 2の補助的位置づけ)。

## AI Nativeな設計への示唆

- **制約を先に棚卸しする**:導入検討では、性能やコストの比較より前に、管轄・データ居住などの境界条項を列挙し、許容される構造の集合を確定する。
- **最適化は許容集合の内側で行う**:コスト最適なトポロジーを先に選び、条項適合を後付けで論じる順序を避ける。
- **パターン化して選ぶ**:越境制約に対しては、Sovereign Silo、Federated、Regional Hubのように、制約の型に対応する構成から選ぶ。曖昧な混成(Hybrid)を自明な選択肢として扱わない。
- **用途単位で統治をモジュール化する**:全社一律の方針とモデル単位の統制のあいだに、ユースケースという中間境界を置き、リスクプロファイルごとに責任構造・統治機能・評価手段を設計する。
- **展開前に段階実装を設計する**:統治構造は導入後の追従ではなく、展開に先行して整える。
- **用語を義務として管理する**:契約・調達・証跡で使う語(役割名や認証・適合に関する語)の定義を確認し、同義と思い込まない。文言は義務の範囲を固定する設計要素である。
- **責任は人間と組織に帰属させる**:モジュール型の構造は、AIへの法人格付与ではなく、人間と企業の責任を用途の周囲に整理する枠組みとして扱う。

## 関連コンセプト

- [[multi-scale-governance-architecture]] — 用途単位のモジュールを含む多層的な統治構造の全体像
- [[ai-use-case-selection-taxonomy]] — 用途のリスクプロファイルに基づく分類・選択
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入が統治に先行する非対称性への背景
- [[functional-attribution-of-intent-to-accountable-principals]] — 責任主体への遡及という構造
- [[multi-actor-value-chain-liability-reallocation]] — 多主体の連鎖における責任配分
- [[socio-technical-fit-as-implementation-condition]] — 社会技術的適合が導入成否を左右する点
- [[ai-governance-and-regulation]] — AIガバナンスと規制の一般的文脈
- [[ai-governance]] — AIガバナンス全般

## 参考ソース

1. Rafael Alberto Patron (2026). *When Words Become Obligations: Terminology, Contracts and Compliance in Artificial Intelligence*. `raw/papers/law/when-words-become-obligations-terminology-contracts-and-compliance-in-artificial.md`
2. Nabeel A. Khan (2026). *Cross-Border AI Architecture Patterns: Three Patterns, and Why the Fourth Is Not a Choice*. `raw/papers/law/cross-border-ai-architecture-patterns-three-patterns-and-why-the-fourth-is-not-a.md`
3. Mayumi J. Okuno, Hiroshi G. Okuno (2026). *Modular Legal Personhood for AI Use Cases: An Enterprise Systems Engineering Framework for Digital Transformation*. `raw/papers/law/modular-legal-personhood-for-ai-use-cases-an-enterprise-systems-engineering-fram.md`
4. Claudio Cifuentes Lobo, Marcus Alburez (2026). *Mitigating AI Privacy Risks in Latin America: Identity Infrastructure, Institutional Capacity and the Path to Adoption*. `raw/papers/law/mitigating-ai-privacy-risks-in-latin-america-identity-infrastructure-institution.md`

## 追加ソース（2026-10-04）

* **タイトル**: A LAYERED REFERENCE FRAMEWORK FOR SCALABLE DATA ENGINEERING AND AI APPLICATIONS (2026)
  **ファイルパス**: `raw/papers/organization_science/a-layered-reference-framework-for-scalable-data-engineering-and-ai-applications.md`
