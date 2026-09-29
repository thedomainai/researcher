# 多段階移転のボトルネックと評価可能性の連鎖

## 概要

知識・技術・情報の移転は、「発見した情報を渡せば終わり」という単発の出来事ではない。発見から実装(deployment)まで、複数の段階が連なる供給チェーン状の過程である。この過程では、情報がどこかに存在していること自体よりも、次の三点が採用を律速する。

1. **ボトルネックの所在**:連鎖のどの段階が全体のスループットを制約しているか
2. **追跡可能性**:提示された情報が根拠となる証拠まで辿れるか
3. **評価手続きへの接続性**:受け手が自分の評価・意思決定の手続きに情報を載せられるか

本概念は、供給元と受け手の間にある情報フロー障壁の構造が、移転の成否を決めるという不変原理として整理できる。

AI Nativeな社会設計では、生成・検索・要約によって情報の「利用可能性」がほぼ無限に拡大する。しかし、ソース[2]が指摘するように、情報が検索可能であることは、それが受け手にとって理解可能・評価可能であることを意味しない。AIが供給を増やすほど、律速点は「情報の量」から「証拠への追跡可能性と評価接続性」へ移る。この点が設計上の中心課題となる。

## メカニズム

以下の構造は、移転の主体が人間・AI・組織・技術のいずれであっても成立する。

### 1. 連鎖としての移転と制約理論的ボトルネック

移転を「発見 → 翻訳・整理 → 提示 → 評価 → 採用・実装」のような多段階の連鎖として捉えると、全体の成果は最も弱い段階に支配される(制約理論的な見方)。ある段階だけを強化しても、律速段階が別にあれば全体は改善しない。この論理は [[necessary-condition-bottleneck-logic]] や [[absorption-capacity-bottleneck-saturation]] と接続する。

### 2. 情報フロー障壁

供給側と受け手の間には、情報の流れを妨げる障壁がある。ソース[3]は、この障壁が国の差異のような単一の水準だけでなく、マクロ(国)、メゾ(企業)、ミクロ(個人)の多層要因の結合で決まると論じる。したがって障壁の所在を特定しないまま情報供給を増やしても、流量は増えない。

### 3. 追跡可能性と評価接続性

ソース[2]によれば、採用の障壁は情報の形式ではなく、証拠への追跡可能性と評価手続きとの接続性の欠如にある。受け手は事前採用の意思決定において、主張が何に基づくかを辿り、自らの判断手続きで検証できなければ、情報を使えない。評価を前に進められる主体や手続きに接続されていることも、情報が機能する条件である。

### 4. 対象を入れ替えても成り立つ構造

- **人間**:論文を読む実務家は、証拠に辿れない主張を採用の根拠にできない。
- **AI**:AIが生成した要約も、出典や検証経路に接続されなければ受け手の評価手続きに載らない。
- **組織**:部門間・拠点間の知識共有では、アクセス改善だけでは統合が進まない(ソース[4]の示唆)。
- **技術**:技術移転では、研究成果が存在しても、評価・実装に至る段階で滞留する。

## 理論的背景

### 技術移転の供給チェーン視点(ソース[1])

Agyei-Owusuらの2026年の論文は、技術移転を発見から実装までの供給チェーンプロセスとして扱い、多段階のボトルネックを伴うと位置づけている。移転を単一の取引ではなく連鎖として分析する枠組みの根拠となる。なお、ここで確認できたのは抜粋範囲(要旨の冒頭部分)の内容であり、個別のボトルネックの具体的な種類や実証結果までは本記事では扱わない。

### 採用可能な情報(adoption-ready information)(ソース[2])

Liang・Liuの論文は、大学の研究成果がリポジトリ、特許データベース、デジタルマッチングプラットフォームなどで検索可能になっていても、それだけでは潜在的な採用者にとって理解可能・評価可能にならない、と述べる。そこで、組織に埋め込まれた科学コミュニケーションが研究成果を採用前の意思決定で使える情報へ変換する過程を分析し、「採用可能な情報」という概念を提示している。その定義は次の四要素である。

- 証拠まで追跡可能であること
- 採用に関連する属性を軸に整理されていること
- 検証可能な文脈に位置づけられていること
- 評価を先へ進められる主体・手続きに接続されていること

イノベーション普及理論と知識境界研究に依拠し、対照的な複数事例を埋め込み型比較事例設計で検討している。

### 情報フロー障壁としての心理的距離(ソース[3])

Safari・Yildizは、心理的距離の研究の不整合が、概念が本来の定義(企業と市場の間の情報フローの障壁)から逸脱したことに由来すると論じる。国の文化・制度の差や、企業と市場の相互作用から切り離された個人の認知と同一視する操作化が原因だとする。そのうえで、国・企業・個人の各水準が企業と市場の情報フローに与える影響を追跡する多層的枠組みを構築している。

### 分散組織における知識共有とAI(ソース[4])

Li・Baruahは、多国籍企業の一事例(匿名化されたGlobalMFG)で、管理職と知識労働者6名への半構造化インタビューを行った。AIは情報へのアクセス改善、地理的に分散したチーム間のコミュニケーション支援、会議後のフォローアップ支援を通じて知識共有を支えるという。ソース側の整理では、言語・文化の違いは緩和されても、情報統合の原理は存続するとされる。

### 資源制約下の局所知識(ソース[5])

Danarのモダリカ沿岸コミュニティの事例研究は、地域の知恵、共同体内の協力、政府の防災プログラムへの参加を通じた適応戦略を報告している。同時に、経済的制約などが強靭性向上を妨げているという。本概念との関連では、外部から供給される情報や施策が局所知識や資源制約と接続されるかが、実効性の条件になるという読み方ができる(この点は本記事による解釈である)。

## AI Nativeな設計への示唆

1. **供給量ではなく評価可能性を設計目標にする**:AIによる情報生成・検索の拡張は利用可能性を高めるが、律速点は追跡可能性と評価接続性に移る。出力の量ではなく、受け手が評価を完了できる割合を指標にする。
2. **すべての主張に証拠への経路を付与する**:出典、根拠データ、検証条件へ辿れる構造を標準にする。これは [[shared-editable-state-and-evaluability-design]] の考え方と整合する。
3. **採用に関連する属性で情報を整理する**:研究や技術の説明を、受け手の意思決定属性に沿って再構成する(ソース[2]の四要素)。生成AIによる変換は [[generative-ai-affordance-in-knowledge-transfer]] の文脈で活用できる。
4. **連鎖全体でボトルネックを診断する**:改善投資の前に、どの段階が律速かを特定する。局所最適化は全体に効かない可能性がある。
5. **情報フロー障壁を多層で分解する**:制度・組織・個人のどの水準に障壁があるかを分けて把握する(ソース[3])。
6. **評価を担う主体と手続きを設計に含める**:情報の提示だけで終わらせず、評価を先へ進められる主体・手続きへ接続する。これには組織側の統合能力も関わる([[capability-realization-organizational-bottleneck]])。
7. **AIの支援範囲を過大評価しない**:ソース[4]の示唆のとおり、AIはアクセスや調整を改善するが、情報統合の原理そのものを消すわけではない。

## 関連コンセプト

- [[necessary-condition-bottleneck-logic]] — 必要条件ボトルネック論理と多層因果の可視化
- [[absorption-capacity-bottleneck-saturation]] — 吸収コスト・ボトルネックによる価値飽和
- [[capability-realization-organizational-bottleneck]] — 組織的統合能力が価値を決めるボトルネック
- [[capability-contingent-absorption-and-progressive-layering]] — 組織能力依存の吸収と段階的レイヤリング
- [[shared-editable-state-and-evaluability-design]] — 評価可能性を担保する情報設計
- [[generative-ai-affordance-in-knowledge-transfer]] — 生成AIアフォーダンスによる知識移転と統合
- [[technical-success-value-realization-gap]] — 技術的成功と価値実現の断絶
- [[validation-regime-shift-and-performance-inflation]] — 検証環境の乖離による性能インフレーション
- [[supply-chain-collaboration]] — サプライチェーンにおける協働と仮想統合

## 参考ソース

1. Agyei-Owusu, B., Siegel, D., Waldman, D., Gopalakrishnan, M., Mishra, S. (2026). "From discovery to deployment: technology transfer as a supply chain process."
   File: raw/papers/innovation_management/from-discovery-to-deployment-technology-transfer-as-a-supply-chain-process.md
2. Liang, S., Liu, L. (2026). "From Research Knowledge to Adoption-Ready Information: How Science Communication Supports the Diffusion of University Research Outputs."
   File: raw/papers/innovation_management/from-research-knowledge-to-adoption-ready-information-how-science-communication-.md
3. Safari, A., Yildiz, H. E. (2026). "The locus of psychic distance."
   File: raw/papers/international_business/the-locus-of-psychic-distance.md
4. Li, X., Baruah, B. (2026). "Working with AI: A Practice-Based Study of Knowledge Sharing in a Multinational Enterprise (MNE)."
   File: raw/papers/international_business/working-with-ai-a-practice-based-study-of-knowledge-sharing-in-a-multinational-e.md
5. Danar, O. R. (2026). "Understanding Rural Community Resilience to Natural Disasters: Challenges for Coastal Communities in Mandalika."
   File: raw/papers/international_business/understanding-rural-community-resilience-to-natural-disasters-challenges-for-coa.md
