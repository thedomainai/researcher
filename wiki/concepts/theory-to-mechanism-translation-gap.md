# 理論から設計機構への変換ギャップと内発的動機の充足

## 概要

理論や規範は、引用されるだけでは行動を変えない。原則・理論・基準が、利用者や実務者の目に見える具体的な仕組み(機構)に翻訳されなければ、初期の採用は起きても持続的な関与は失われ、形式的遵守に終わる。これが「理論から設計機構への変換ギャップ」である。

この概念にはもう一つの側面がある。持続的で実質的な関与は、自律性・有能感(コンピテンス)・関係性という基本的心理欲求が充足されるときに生じる。これらが満たされない設計は、外形的な採用と内実のある関与を分離させる。

AI Nativeな社会設計では、AIツールの導入・倫理原則の運用・規制基準の適用が同時に進む。どの場面でも「採用したこと」と「実際に機能していること」は別物であり、設計者は前者を成果指標にしてはならない。本概念はその判断の土台になる。

## メカニズム

この構造は、対象が個人・組織・AIシステム・制度のいずれでも成立する。

1. **理論と実装の乖離**:理論や規範は「参照される」段階にとどまり、利用者向けの具体的機構に落とし込まれない。要件から設計、機能へのトレーサビリティ(追跡可能性)がないため、理念は実装のどこにも現れない。
2. **初期採用と持続的関与の分離**:導入時の関心や義務によって採用は起こる。しかし関与を支える機構がなければ、使い続ける理由が生まれない。
3. **基本的心理欲求の未充足**:自律性(自分で選んでいる感覚)、有能感(できるという感覚)、関係性(つながりや配慮)が満たされないと、規範は外から課されたものにとどまり、内面化されない。
4. **形式的遵守への帰結**:内面化されない規範は、象徴的な遵守(体裁を整える対応)として処理される。形式は満たされていても、実質的な関与はない。

対象を入れ替えても構造は同じである。ウェルネスアプリの利用者、サステナビリティ報告を担う会計専門職、生成AIを使う学生のいずれも、欲求が満たされなければ形式的な関与に落ち着く。

## 理論的背景

### 理論から設計機構への翻訳(ソース1)

Thanthrige と Wickramasinghe(2026)は、デジタルウェルネスツールが初期の利用者獲得には成功しても持続的エンゲージメントに苦戦する背景として、「理論から設計への持続的ギャップ」を挙げる。行動理論や関係性理論はしばしば引用されるが、利用者向けの具体的なシステム機構に翻訳されることは稀だという指摘である。

この論文は、自己決定理論(SDT)と CARE(Compassion, Assistance, Respect, Empathy)フレームワークを、AI拡張型のプログレッシブWebアプリのための一貫した設計ロジックへと操作化する、理論駆動型のユーザー中心設計(UCD)フレームワークを提示する。方法にはデザインサイエンス研究方法論(DSRM)と、若年成人および領域専門家とのコデザインを用いる。設計要件から設計機構へ至る、透明で追跡可能な変換の形式化を目指している。核心的知見は、心理学理論を設計ロジックへ体系的に変換することで、技術形態を超えた持続的エンゲージメントの実装が可能になるという点である。なお、入手できた抜粋は途中までであり、それ以降の詳細は本記事では扱わない。

### 内発的動機の欠如と形式的遵守(ソース2)

Benhayoun(2026)は、モロッコなど新興経済圏の会計専門職が、ISSB基準などのサステナビリティ報告基準を、実質的な関与ではなく象徴的な遵守として採用している現象を扱う。SDTに基づくミクロ基盤の説明として、自律性・有能感・関係性の充足が内発的動機と、サステナビリティ原則の真正な内面化を育むと論じる。意味ある関与は単なる遵守ではなく原則の内面化に依存する、という主張である。手法は GSCA-SEM と必要条件分析(抜粋は途中で切れている)を組み合わせた多手法の定量アプローチである。形式的遵守の根因は、基本的心理欲求の充足の欠如にあると位置づけられる。

### 有能感と自制(ソース7)

Herianto ら(2026)は、177名の大学生への調査から、AI自己効力感(AIを倫理的かつ効率的に使える自信)が、AI利用頻度と学術的誠実性との負の関連を有意に弱めることを示した。クラスター分析では3つのAI利用者プロファイルも識別されている(抜粋に現れるのは Confident and Cautious Users などの一部)。制限的な方法ではなく、有能感を通じて倫理的な使用を促す方向性を示す実証知見である。

### 周辺的な知見(ソース4〜6ほか)

- ソース4(メタバース/VRと体育)は、SDTなどに導かれ、没入型環境が動機づけや参加を高めると報告する。ただし効果は現在のVRのセンサ精度やリアルタイムフィードバック速度に依存するとされる。
- ソース3(包摂教育とAI)、ソース5(デジタルツインによる生産計画)、ソース6(エージェント型自動化)は、いずれも技術実装や分類に主眼があり、本概念に対しては間接的な位置づけにとどまる。ソース6には、直感的なUX設計、AIの透明な説明、信頼構築への配慮が有効な実装の要件だという記述がある。

## AI Nativeな設計への示唆

- **採用ではなく関与を測る**:導入率やチェックリスト充足を成功指標にせず、持続利用や実質的な行動変化を評価対象にする。
- **要件から機構への追跡可能性を確保する**:各理論・原則が、どの設計要件を通じて、どの利用者向け機能に実装されたかを説明できるようにする(ソース1の DSRM 的発想)。
- **三つの欲求を設計要件に組み込む**:自律性(選択と管理の余地)、有能感(できるという実感を支える支援)、関係性(配慮や共感を伴うやり取り)を、機能レベルの要件として明示する。
- **禁止より能力形成を優先する**:規制や制限だけでなく、利用者の自己効力感を高める設計が、過度な依存の抑制や倫理的使用につながりうる(ソース7)。
- **規範の内面化を促す**:基準を外部から課すだけでなく、実務者が意味を理解し自分のものとして受け止められる過程を設計する(ソース2)。
- **共設計を取り入れる**:対象利用者と専門家を設計過程に参加させ、翻訳の妥当性を検証する。
- **技術依存性に注意する**:動機づけの効果が特定技術の性能に依存する場合(ソース4)、その前提が変わると効果も変わる。欲求充足の原理と技術実装を切り分けて設計する。

## 関連コンセプト

- [[principles-to-practice-legitimacy-gap]] — 原則が実践に翻訳されないときの正当性の問題
- [[principle-to-practice-gap-and-layered-responsibility-allocation]] — 原則と実装の乖離を多層的な責任配置で扱う視点
- [[organizational-ethical-translation]] — 倫理原則を組織の実践へ変換する過程
- [[technical-success-value-realization-gap]] — 技術的な成功が価値実現に結びつかない断絶
- [[formal-rule-shadow-labor-accountability-gap]] — 形式的規則と不可視の実務のあいだのギャップ
- [[assistance-mediated-capability-erosion-and-homogenization]] — 支援が有能感や多様性を損なう側面

## 参考ソース

1. A Theory-Driven UCD Framework for Young Adult Wellness: Translating SDT and CARE into the Design Logic — Ayesha Thanthrige, Nilmini Wickramasinghe (2026)
   File: raw/papers/psychology/a-theory-driven-ucd-framework-for-young-adult-wellness-translating-sdt-and-care-.md
2. The Micro‐Foundations of Sustainability Reporting: A Self‐Determination Theory on ISSB Implementation — Issam Benhayoun (2026)
   File: raw/papers/psychology/the-microfoundations-of-sustainability-reporting-a-selfdetermination-theory-on-i.md
3. Bridging Inclusive Education and AI: A Technology-Centric Taxonomy and Systematic Literature Review — Yunfeng Wan, Yuchao Jiang, Hui Guo (2026)
   File: raw/papers/psychology/bridging-inclusive-education-and-ai-a-technology-centric-taxonomy-and-systematic.md
4. The Impact of Metaverse and Virtual Reality (VR) on Gamified Physical Education Learners' Outcomes — Sohom Saha, Patcharavadee Sriboonruang, Pawan Deep, Himanshi Verma, SJ Singh (2026)
   File: raw/papers/psychology/the-impact-of-metaverse-and-virtual-reality-vr-on-gamified-physical-education-le.md
5. A Conceptual Framework for AI-Enabled Digital Twin-Based Production Planning — Dmitrii Voistrochenko (2026)
   File: raw/papers/psychology/a-conceptual-framework-for-ai-enabled-digital-twin-based-production-planning.md
6. AI, Agentic Automation, and the Future of Design and Engineering — Theodoros Galanos (2026)
   File: raw/papers/psychology/ai-agentic-automation-and-the-future-of-design-and-engineering.md
7. From threat to tool: AI self-efficacy and user profiles in higher education — Herianto Herianto, Eko Wahyudi, Andi Jusmiana, Habib Ratu Perwira Negara, Ansyari Ansyari (2026)
   File: raw/papers/psychology/from-threat-to-tool-ai-self-efficacy-and-user-profiles-in-higher-education.md
