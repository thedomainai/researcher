# 予見的統治の運用前提と対象の性質の衝突

## 概要

予見的統治の運用前提と対象の性質の衝突(Operational Premise Collision in Anticipatory Governance)とは、規制が暗黙に依拠している運用上の前提条件を、規制対象である技術の性質そのものが侵食する構造的矛盾を指す。Kim (2026) は、予見的な規制ガバナンスが次の三つの運用前提に立つと論じる。

- **カテゴリの安定性**(categorical stability)
- **認識的到達可能性**(epistemic accessibility)
- **管理可能な速度**(manageable pace)

AIは、創発性(emergence)、不透明性(opacity)、速度(velocity)によって、この三つを同時に(compound に)侵害する。

この概念が重要なのは、失敗の原因が個々の制度設計の巧拙ではなく、前提と対象の不整合にあるからである。Kim は、主要な法域や国際機関で前提の大きく異なる改革が、互いによく似た失敗パターンに直面していると指摘する。異なる設計が同型に失敗するなら、条文の改良を重ねても問題は解消しない。AI Nativeな社会設計では、静的な原理を固定する発想から、前提の崩れ方を継続的に診断する発想へ移る必要がある。

## メカニズム

この構造は、規制対象を人間、AI、組織、技術のいずれに入れ替えても成立する。「統治の側が前提とする性質」と「対象が実際に持つ性質」がずれ、そのずれが統治の運用を空洞化させる、という形式で整理できる。

### 1. 規制ラグ(速度非対称)

規制の策定・改正には手続き上の時間がかかる。一方、対象技術は急速に変化・普及する。ソースでは次の指摘がある。

- 法律実務におけるAI/MLツールの普及は、既存の規制枠組みの統治能力を上回った(Das & Ganguly, 2026)。
- 建設分野でも、組織のAI導入は統治実務の整備より速い(Samsami, 2026)。

制度の具体的な形が入れ替わっても、この速度の非対称というラグの機構自体は変わらない。関連する論点は [[adoption-outpacing-governance-capacity-asymmetry]] にある。

### 2. カテゴリの不安定化

カテゴリ規制は、対象を事前に分類できることを前提にする。Samsami (2026) は、EU AI規則(Regulation (EU) 2024/1689)の Annex III point 2 が閉じたリストであり、構造物に及ばないため、公共インフラの状態を評価するソフトウェアが高リスク区分の外に置かれる点を指摘している。LLMは最も確からしい続きを返す確率的な仕組みで、流暢かつ自信ありげに失敗し、出力の表面から検出しにくい。複数エージェントとして配備された場合は、引き継ぎ地点で誰も誤りを観測しない。分類の境界と失敗の所在が、固定的なカテゴリでは捉えにくくなる。

### 3. 認識的到達可能性の喪失

Mitranescu (2026) は、法とAIをそれぞれ自らの区別を自己参照的に産出する二つのオートポイエーシス的システムとして捉える。規制意図とAI挙動のギャップは、起草上の欠陥や政治的妥協ではなく、構造的な認識論的条件だと論じる。したがって条文の改善だけでは修復できない。

### 4. 改革の罠

Kim (2026) は、既存の前提の内側で改革を行うと、その前提が生む侵害が再生産されるとし、これを「改革の罠」(reform trap)と呼ぶ。運用前提の水準での паラダイム的ロックインであり、経路依存や政策パラダイムの硬直とは区別される。同論文は、この収斂パターンを、実際に改革が進む五つの戦略にわたって見出している(抜粋で確認できる戦略はカテゴリ規制、プロセス管理、情報開示など)。

## 理論的背景

- **三前提モデル(Kim, 2026)**: 三つの運用前提は運用上の前提条件の層をなすものであり、統治の完全な理論ではないと明示されている。
- **静的原理から動的診断へ(一介叔声, 2026)**: 責任あるイノベーション、アジャイルガバナンス、リスクベース規制は、統治を固定ルールという目的地として扱う点で共通の欠陥があるとされる。同論文は、動的持続理論に由来する「ti-xiang」診断ツールキットを提案し、2023年のOpenAI危機の分析で妥当性を検証したと述べる。ただし抜粋で確認できる範囲に限られ、独自理論に基づく点には留意が必要である。
- **オートポイエーシス的ギャップ(Mitranescu, 2026)**: カント、コジブスキー、ベイトソン、マトゥラーナ、ヴァレラ、ルーマンの議論を用いて、法とAIの構造的遭遇を説明する。
- **法と経済学の視点(Zarra, 2026)**: 規制介入を市場の失敗、責任配分、規制手段の有効性から分析し、標準的な規制手段で足りるかを問う。
- **持続可能性の統合(Ariyanti et al., 2026)**: EU、米国、中国、日本、韓国、シンガポールの六法域を責任あるイノベーションの枠組み(予期、再帰性、包摂、応答性)で分析し、現行の枠組みには環境影響評価や適応的な持続可能性規制の明示的な仕組みが欠けていると指摘する。
- **社会技術的埋め込み(Frontoni & Epasto, 2026)**: AIは中立で未踏の空間ではなく、制度的・空間的環境に埋め込まれて動くとする。
- **自然言語とコードのギャップ(Chung et al., 2026)**: 規制は自然言語で表現される一方、コンプライアンスはスマートコントラクトに実装される。GRACE は、人間参加型のガバナンスを組み込んだ設計指向の対応例である。
- **データ主権と権力非対称(Mehta, 2026)**: 生成AIの下で従来の知的財産・プライバシー枠組みが構造的に崩れつつあるとし、「private-by-default」モデルを提案する。

## AI Nativeな設計への示唆

1. **前提の診断を制度に組み込む**: 規制設計の前に、カテゴリの安定性、認識的到達可能性、速度の三点が成立するかを点検し、崩れた前提を可視化する。
2. **固定ルールを目的地にしない**: 統治を継続的な適応の過程として設計し、段階的な介入を順序づける(一介叔声, 2026 の方向性)。
3. **カテゴリ依存を減らす**: 閉じたリストによる区分だけに頼らず、機能や利用文脈に基づく評価を併用する。
4. **引き継ぎ地点の責任を設計する**: 複数エージェント間の受け渡しで誰も誤りを観測しない状況に備え、観測と所有の主体を明確にする。
5. **実装層での監査可能性**: 規制の自然言語表現と実装コードの間に、人間参加型の検証層を置く(Chung et al., 2026)。
6. **制度の埋め込みを前提にする**: AIを外部の新領域と見なさず、既存の制度・社会構造との相互作用として規制枠組みを設計する。

## 関連コンセプト

- [[ai-governance]] — AIガバナンス全般
- [[ai-governance-and-regulation]] — AIガバナンスと規制
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入速度と統治能力の非対称ギャップ
- [[sociotechnical-embeddedness-and-legitimacy-driven-adoption]] — 社会技術的埋め込みと正当性による導入駆動
- [[agentic-ai-and-governance]] — エージェントAIとそのガバナンス
- [[ai-governance-and-risk-management]] — AIガバナンスとリスク管理
- [[authorization-artifact-and-independent-reconstructability]] — 認可アーティファクトと独立的再構成可能性
- [[discretion-relocation-to-design-parameters]] — 裁量の設計パラメータへの上流移転と説明責任の追跡不能化

## 参考ソース

- The shared blind spot: why diverse AI governance approaches fail for the same reason — Si Hyun Kim, 2026
  `raw/papers/law/the-shared-blind-spot-why-diverse-ai-governance-approaches-fail-for-the-same-rea.md`
- Chasing the algorithm: A law and economics perspective on experimental AI governance — Antonella Zarra, 2026
  `raw/papers/law/chasing-the-algorithma-law-and-economics-perspective-on-experimental-ai-governan.md`
- Governing Sustainable Artificial Intelligence: A Green AI Regulatory Framework Based on Responsible Innovation — Sri Ariyanti, Muhammad Suryanegara, Ajib Setyo Arifin, 2026
  `raw/papers/law/governing-sustainable-artificial-intelligence-a-green-ai-regulatory-framework-ba.md`
- From Static Principles to Dynamic Diagnosis: A Ti-Xiang Toolkit-Based Framework for AI Governance — 一介叔声, 2026
  `raw/papers/law/from-static-principles-to-dynamic-diagnosis-a-ti-xiang-toolkit-based-framework-f.md`
- A Study into the Evolving Challenges in Regulating Artificial Intelligence and Machine Learning in the Future Legal Profession — Sushanta Kumar Das, Shantanu Ganguly, 2026
  `raw/papers/law/a-study-into-the-evolving-challenges-in-regulating-artificial-intelligence-and-m.md`
- Artificial Intelligence (AI) on Construction Projects: Regulatory Position and Governance Gaps — Reihaneh Samsami, 2026
  `raw/papers/law/artificial-intelligence-ai-on-construction-projects-regulatory-position-and-gove.md`
- THE CARTESIAN MACHINE: Law at the Edge of Emergence — Tudor Mitranescu, 2026
  `raw/papers/law/the-cartesian-machine-law-at-the-edge-of-emergence.md`
- AI as the "final frontier"? Narratives, geographies, and relationships in the human–algorithm coproduction — Emanuele Frontoni, Simona Epasto, 2026
  `raw/papers/law/ai-as-the-final-frontier-narratives-geographies-and-relationships-in-the-humanal.md`
- GRACE: An AI-Augmented Compliance Information System for Real-World Asset Tokenization — Ming Hin Chung, Treza Bawm Win, Hao Zhong, 2026
  `raw/papers/law/grace-an-ai-augmented-compliance-information-system-for-real-world-asset-tokeniz.md`
- The Illusion of Digital Sovereignty: Reimagining Human Co-Authorship and Data Ownership in Indian and Global AI Governance — Prerna Mehta, 2026
  `raw/papers/law/the-illusion-of-digital-sovereignty-reimagining-human-co-authorship-and-data-own.md`
