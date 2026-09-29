# 反復的依存による判断・主体性能力の段階的侵食

## 概要

反復的依存による判断・主体性能力の段階的侵食とは、AIなどの技術に受動的に頼る行為が繰り返されることで、意図を形成し、判断を下し、責任を引き受けるという能力そのものが再形成され、弱まっていく現象である。Tier 1(不変原理)に位置づけられ、特定の技術や製品に依存しない構造的な原理として扱う。

焦点は個々の出力や単発の意思決定の良否ではなく、相互作用の反復がもたらす通時的(diachronic)な効果にある。一度ごとの依存は合理的で無害に見えても、積み重なると主体の能力構成が変わる。その帰結として道徳的責任の転位(責任が技術側へ移ること)と、価値判断の麻痺が生じうる。

AI Nativeな社会設計にとって重要なのは、AIが日常の意思決定に組み込まれるほど、この侵食が個人の問題にとどまらず組織・制度の判断能力の問題になるためである。防御条件は、責任の主体を明示的に保持し続けること(明示的アンカリング)にある。

## メカニズム

対象を人間、組織、AIエージェント、技術システムのいずれに置き換えても成立する構造として整理する。

1. **受動的依存の反復**: 主体が判断の一部を外部の仕組みに預け、既定値をそのまま受け入れる。
2. **習慣化による能力の再形成**: 反復により、預けた機能を使わない状態が常態になる。能力は使われなければ維持されず、形成のされ方自体が変わる。
3. **責任の転位**: 判断が外部に預けられると、結果への責任感覚も外部に移る。「システムがそう出した」という理由づけが標準化する。
4. **麻痺と自己強化**: 責任感覚と価値判断が鈍ると、依存を見直す契機(違和感や疑問)そのものが生じにくくなり、依存が強まる循環に入る。
5. **防御条件**: 判断・検証・責任の所在を明示的に主体に固定すると、1〜3の連鎖が断たれる。

この構造の要点は、侵食が「能力の低下」だけでなく、能力を行使するための前提(意図の形成、責任の自覚、自らの依存を second-order で問い直す力)にまで及ぶことである。

## 理論的背景

### 習慣化と倫理的主体性(ソース1)

Herrera (2026) は、AIへの反復的依存が倫理的主体性を行使するための能力を段階的に再形成しうると論じる。アリストテレス的徳倫理学、自律支援的デザイン、技術による道徳形成(techno-moral formation)の議論を基盤とし、分析対象を孤立した出力や個別の決定から、反復的相互作用の通時的効果へ移す。

倫理的主体性は、相互に区別できるが因果的に連関する六つの次元で整理される。

- 人間の主体性(human agency)
- 道徳的判断(moral judgment)
- 倫理的認識(ethical awareness)
- 自律性(autonomy)
- 人間の意図(human intention)
- 二次的主体性(second-order agency)

侵食をもたらす相互作用上・制度上のメカニズムとして、既定値の習慣的受容、迎合的な強化(sycophantic reinforcement)、欺瞞的デザインなどが挙げられている(抜粋は途中で切れているため、これ以外の列挙は確認できない)。

### 道徳的転位と倫理的麻痺(ソース2)

Kim & Lee (2026) は、AI採用によって人間が道徳的責任を技術に転位させ、固有の価値判断能力が構造的に麻痺するという知見を示している。対象は職場での環境配慮行動の抑制であり、責任転位と倫理的麻痺が行動を抑える経路として扱われる。取得できた抜粋はアブストラクト冒頭までのため、詳細な実証設計や効果量は本記事では扱わない。

### 認識論的責任の保持(ソース3)

Beau ら (2026) は、中等教育におけるAI支援型研究を扱い、生成AIが「学習者が探究本来の知的作業を行ったか」を見えにくくする問題を指摘する。提案されるAI-assisted research competency (AARC) は、「著者性・判断・検証・知的責任を手放さずにAIとともに探究する統合的能力」と定義され、徳認識論を基盤に七つの教えられる次元を持つ。指導付きの基礎から領域横断的な転用、自律的探究へと段階的に発達し、「検証する・引用する・省察する」という三つの反復的コミットメントに落とし込まれる。責任の明示的保持を、教育設計として具体化した例といえる。

### 道徳的責任の帰属(ソース4)

Iyer (2026) は、AIが道徳的行為者になりうるかを論じ、自律的決定と道徳的責任の関係を検討する。医療、金融リスク評価、採用、教育など重大な帰結を伴う領域でAIが判断に影響している状況が前提となる。ソース群の要約では、自律的決定と責任の因果関係は技術に依らず不変である一方、定義や法的枠組みは制度に依存するとされる。責任の空白を作らないという要請の背景として位置づけられる。

### 周辺的なソース

ソース5 (Daryanto ら, 2026) は場所ラベルによるナッジとリサイクル選択を扱い、ソース6 (Keleş, 2026) はAIエージェントへの規範的ガバナンス機能の組み込みを扱う。いずれも抜粋が限られ、本概念との関係は間接的である。ナッジによる行動誘導が条件依存的であること、規範的機能を汎用的な構造メカニズムとして抽象化する必要があることが示唆される程度にとどめる。

## AI Nativeな設計への示唆

以下はソースの知見を踏まえた設計上の指針であり、個別の効果検証を主張するものではない。

- **責任主体の明示的アンカリング**: 意思決定フローの各段階で、最終判断と責任を負う主体(人・役割)を明示する。「AIが出した」を責任の終点にしない。
- **既定値の設計に注意する**: 既定値の習慣的受容が侵食経路の一つである以上、既定値を無自覚に受け入れさせない設計にする。選択アーキテクチャが依存を形成する点は [[choice-architecture-and-reliance-shaping]] が扱う。
- **迎合的挙動の抑制**: 承認を強化し続ける応答は判断の外部化を促す。摩擦を意図的に残す考え方は [[epistemic-friction-and-sycophancy-erosion]] と接続する。
- **検証・引用・省察のルーチン化**: AARCの「検証する・引用する・省察する」のように、人間側が知的作業を行った証跡を残す手順を組み込む。
- **段階的な自律の設計**: 指導付きの段階から自律的運用へと移行する発達的設計により、能力の形成と維持を支える。
- **二次的主体性の維持**: 自らの依存のあり方を点検し、見直す機会(定期的なレビューや、AIなしで判断する場面)を設ける。
- **制度面の対応**: 責任の定義や法的枠組みは制度依存であるため、組織・制度ごとに責任の所在の規則を明文化する。

## 関連コンセプト

- [[cognitive-capacity-delegation-and-bifurcation]] — 認知の委譲による能力の侵食と二極化
- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による所有感・責任・能力の侵食と回復的足場設計
- [[epistemic-friction-and-sycophancy-erosion]] — 認識的摩擦の喪失と迎合による自律性の侵食
- [[adaptive-assistance-objective-drift-and-agency-erosion]] — 適応的支援システムにおける目的乖離と主体性の侵食
- [[compensatory-adaptation-hidden-erosion]] — 補償的適応の枯渇と安定性の錯覚
- [[choice-architecture-and-reliance-shaping]] — 選択アーキテクチャによる依存・信頼の形成
- [[decision-process-visibility-and-reliance-calibration]] — 意思決定過程の可視性と依存度の較正
- [[administrative-substitution-and-judgment-residual]] — 管理機能の代替と判断・価値選択への役割移行
- [[external-scaffolding-of-finite-cognitive-capacity]] — 有限認知容量の外部足場による補完

## 参考ソース

1. Francisco Herrera (2026). *Habituation and the Human Will: How Passive Reliance on Human-AI Collaboration Erodes Ethical Agency to Prevent It*.
   File: raw/papers/philosophy/habituation-and-the-human-will-how-passive-reliance-on-human-ai-collaboration-er.md
2. Byung-Jik Kim, Julak Lee (2026). *The unintended consequences of AI adoption: How moral displacement and ethical numbing suppress pro-environmental behavior at work*.
   File: raw/papers/philosophy/the-unintended-consequences-of-ai-adoption-how-moral-displacement-and-ethical-nu.md
3. Mathieu Beau, Mehdi Lazar, Brice Flaquiere (2026). *AI-Assisted Research Competency in Secondary Education: A Framework for Epistemic Agency, Authorship and Responsible Knowledge Production*.
   File: raw/papers/philosophy/ai-assisted-research-competency-in-secondary-education-a-framework-for-epistemic.md
4. Ananya Iyer (2026). *Can Artificial Intelligence Become a Moral Agent? Philosophical Perspectives on Responsibility, Ethics and Machine Autonomy*.
   File: raw/papers/philosophy/can-artificial-intelligence-become-a-moral-agent-philosophical-perspectives-on-r.md
5. Ahmad Daryanto, Zening Song, Jingxi Huang (2026). *Place label nudges: How place attachment shapes recycling choice*.
   File: raw/papers/philosophy/place-label-nudges-how-place-attachment-shapes-recycling-choice.md
6. Serap Keleş (2026). *Toward an internal moral purpose like normative governance function in artificial agency*.
   File: raw/papers/philosophy/toward-an-internal-moral-purpose-like-normative-governance-function-in-artificia.md
