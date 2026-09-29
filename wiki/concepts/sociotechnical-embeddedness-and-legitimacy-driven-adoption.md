# 社会技術的埋め込みと正当性による導入駆動

## 概要

社会技術的埋め込みと正当性による導入駆動とは、技術が「未踏の空間への領域拡張」として独立に広がるのではなく、既存の制度・地政・社会関係との相互作用の中で導入されるという原理である。また、組織はその技術が自らの正当性をどう脅かすかに応じて、採用の形態(何を、どの統制水準で使うか)を選ぶ。さらに、規則や規制の正当性そのものも、形式的なルールの存在ではなく、具体的な状況の中での解釈と適用に依拠する。

AI Nativeな社会を設計するうえで、この原理は次の理由で重要である。

- 技術能力だけを起点にした設計は、導入先の制度的・社会的文脈で摩擦や拒絶を招きやすい。
- 規制やガバナンスの設計は、AIが「中立で空白の空間」で動くという前提を捨て、埋め込みの認識から出発する必要がある。
- 組織の採用判断は、単なる技術・リスク管理の選択ではなく、正当性の維持という組織行動として理解できる。

## メカニズム

この原理は、対象を組織、技術、法制度、個人に入れ替えても成立する構造として整理できる。

1. **正当性脅威への反応**: 主体(組織など)は、外部の強力な資源を取り込む際、その利用が利害関係者からの評価を損なう可能性を感知する。脅威が認識されると、主体は関係の取り方を調整する。例えば外部依存から内部統制へ移行する。
2. **制度への埋め込み**: 導入される対象は真空ではなく、領土的インフラ、法的枠組み、社会関係の中に置かれる。対象は環境を形作り、同時に環境によって形作られる(相互構成)。
3. **解釈的適用による正当性**: 規則が存在するだけでは正当性は成立しない。規則が具体的な人間の状況の中でどう解釈され適用されるかが、正当性を左右する。

三つは連動する。埋め込みが正当性の評価基準を与え、脅威の認識が採用形態を決め、その形態が状況内で適用される過程で正当性が再び評価される。

## 理論的背景

### 正当性理論に基づく組織のGenAI採用(ソース1)

Xu、Tang、Xueによる論文は、生成AI(ChatGPTやGoogle Geminiなど)の公開・外部ホスト型モデルから、私的・内部統制型システムへ移行する「public-to-private」シフトを扱う。この移行は技術、金融、医療、高等教育など複数の業界で一般化しつつあるが、文献では純粋な技術・リスク管理上の選択として扱われがちで、組織行動論的な検討が不足していると著者らは指摘する。

著者らは正当性理論の観点から、公開GenAIの利用が組織を多次元の正当性脅威にさらすと論じる。抜粋に確認できる範囲では、実利的正当性のリスクは主要な利害関係者に関わるものとして提示されている。核心的知見として、実利的・規範的・認知的の各正当性脅威が意思決定を駆動するとされる。なお、抜粋はここで途切れており、規範的・認知的脅威の詳細な内容や検証手法は確認できない。

### AIは「最後のフロンティア」か(ソース2)

Frontoni、Epastoの論文は、AIを「final frontier」とみなす比喩が植民地的・拡張主義的起源を持ち、AIシステムの社会技術的な埋め込みを捉えるには不十分だと批判する。地理学的視点とコンピュータ工学の知見を組み合わせ、EUのAI規則(AI Act)を、征服の語りから規制・説明責任・共同生産に根ざした枠組みへの転換点と位置づける。医療、採用、刑事司法の事例(ヴィネット)を通じて、AIが中立で未踏の空間ではなく、空間的・制度的に位置づけられた環境で作動することを示す。アルゴリズムシステムは領土的インフラ、法的枠組み、社会関係を形作り、また形作られる。

### 法の正当性と解釈的適用(ソース3)

Qatraniの論文は、正義、慈悲、説明責任、人間の尊厳、法の精神の関係を通じて法の道徳的目的を検討する。イスラームの倫理的教え、古代の法伝統、憲法原理、人権基準、司法判断、修復的司法、恩赦、手続的保障などを比較的・省察的に扱う。分析は、法の正当性が形式規則の存在だけでなく、規則が特定の人間的状況の中でどう解釈・適用されるかに依存することを示す。慈悲は説明責任を消し去らない、という点も示されている。

### 補助的な知見(ソース4、5)

Tier 2のソースは、原理を補強する周辺的な文脈を与える。Kimの研究は、デジタル上の不正がレピュテーションリスクとなる過程を、企業データ(RepRisk、2011〜2020年)と投資家実験で検討している。プライバシー侵害が最も持続的なリスク上昇をもたらし、心理的不快感が投資意向や否定的な口コミを媒介し、AIか人間かという責任の枠組みがこれらの反応を条件づけるとされる。これは、利害関係者の反応が組織の正当性に直結することを示唆する。Elsakkaらの研究は、教育へのAI導入が不平等なアクセスやアルゴリズムバイアスなどによる新たな不平等を生みうることから、従来の「平等な教育を受ける権利」の概念が十分かを問う。これは、既存の制度概念が技術導入によって再解釈を迫られる例と読める。

## AI Nativeな設計への示唆

- **埋め込みを前提に設計する**: 導入計画では、技術仕様だけでなく、対象領域の制度、法的枠組み、地理的・社会的関係を設計対象に含める。AIを「空白地への拡張」として扱う語りを避ける。
- **正当性脅威を三層で点検する**: 実利(利害関係者への便益・損失)、規範(倫理・規制への適合)、認知(理解可能性・受容)の観点から、導入形態ごとの脅威を評価する。公開ツールの利用と内部統制型システムの構築は、この点検の結果として選択される。
- **採用形態を段階的な選択肢として扱う**: 全面採用か禁止かの二択ではなく、外部ホスト型から内部統制型への移行のように、統制水準を調整できるようにしておく。
- **規則を運用の文脈で評価する**: ルールの整備だけで正当性が確保されたとみなさず、具体的な状況での解釈・適用の実態、例外対応、説明責任の所在を継続的に確認する。
- **責任の枠組みを明示する**: AIか人間かという説明責任の帰属は、利害関係者の反応を左右しうる。責任の所在を利害関係者に見える形で示す。
- **既存概念の再検討を織り込む**: 教育の平等のような既存の権利概念が新しい階層化に対応できるか、導入と並行して検討する。

## 関連コンセプト

- [[adoption-velocity-versus-institutional-absorption-capacity]] — 導入速度と制度の吸収能力の不均衡は、埋め込みの摩擦として現れる。
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入が統治能力を上回る非対称性。
- [[ai-technology-adoption-firms]] — 企業における採用の要因と普及。
- [[ai-driven-organizational-transformation]] — 組織変革と正当性の関係。
- [[algorithmic-governance-ai-adoption]] — アルゴリズムによるガバナンスと採用。
- [[discretion-relocation-to-design-parameters]] — 解釈的適用が設計パラメータへ移る際の説明責任の問題。
- [[access-driven-cumulative-concentration]] — アクセス格差による新たな階層化。

## 参考ソース

1. From Public to Private: How Legitimacy Shape Organizational GenAI Adoption — Feng Xu, Zhenya Tang, Botong Xue (2026)
   File: raw/papers/law/from-public-to-private-how-legitimacy-shape-organizational-genai-adoption.md
2. AI as the "final frontier"? Narratives, geographies, and relationships in the human–algorithm coproduction — Emanuele Frontoni, Simona Epasto (2026)
   File: raw/papers/law/ai-as-the-final-frontier-narratives-geographies-and-relationships-in-the-humanal.md
3. Justice, Mercy, and the Spirit of Law: Reconsidering Punishment, Accountability, Protection, and Human Dignity — Osama S Qatrani (2026)
   File: raw/papers/law/justice-mercy-and-the-spirit-of-law-reconsidering-punishment-accountability-prot.md
4. When Digital Misconduct Becomes Reputational Risk: Evidence from Firms and Stakeholders — Jinwoo Kim (2026)
   File: raw/papers/law/when-digital-misconduct-becomes-reputational-risk-evidence-from-firms-and-stakeh.md
5. Artificial Intelligence and the Right to Equal Education: A Legal Framework for Algorithmic Educational Justice — Sally Awad Elsakka, Nasr Al-Sayed Rashid, Hassan H. Ghofair (2026)
   File: raw/papers/law/artificial-intelligence-and-the-right-to-equal-education-a-legal-framework-for-a.md
