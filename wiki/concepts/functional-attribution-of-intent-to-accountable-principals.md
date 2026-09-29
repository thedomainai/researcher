# 機能的意図帰属と責任主体への遡及構造

## 概要

**機能的意図帰属**とは、意図や責任を「行為者の内面で起きている心理状態の報告」としてではなく、「行為を誰に帰属させ、どこに法的効果や責任を割り当てるか」という制度上の機能として捉える考え方である。**責任主体への遡及構造**とは、自律的に動くエージェントが行為の途中に介在しても、責任の連鎖が背後の設置者・配備者(プリンシパル)まで辿れる状態を保つ構造を指す。

AI Nativeな社会設計では、AIが交渉・助言・環境適応・意思決定支援といった「意図的に見える」行為を大量に生成する。このとき「AIに心はあるか」「AIは人格を持つか」という形而上学的問いに設計を委ねると、責任の所在が曖昧になる。本概念は、問いを「この行為は誰に帰属し、誰が答責するか」という機能的な問いに置き換えることで、責任の空白を作らずにAIの自律性を活用するための不変原理として位置づけられる。

## メカニズム

この構造は、行為の担い手が人間・AI・組織・技術のいずれであっても成立する。要素は次の三つに整理できる。

1. **機能的帰属(法的虚構)**: 意図は、法的効果の発動を制御し、非難を配分し、リスクを管理するための規範的道具として使われる。実際の心的状態とは独立に、推定・擬制・帰属されうる。組織(法人)の意図や複数の行為者の行為を単一の主体に帰属させる仕組みは、その典型である。
2. **プリンシパル=エージェント構造**: 行為を実行するエージェントが非人格的であっても、その行為は代理、使用者責任、電子エージェントによる契約、法人への帰属といった既存の法理を通じて、特定可能な人間のプリンシパルに帰属させられる。
3. **遡及可能性の保存**: 自律性・不透明性・適応性が高まると、個々の行為の「帰属可能性」は複雑になる。しかし、配備者が与えた指針や統制に根ざす「答責性」は、標準的な遡及(トレーシング)構造を通じて残る。因果的・認識的に結果から遠ざかっても、答責性が減るわけではない。

逆に、責任の受け皿として新たな主体(人格)を作ると、意思決定権の所在が二重化・不明確化し、帰属に矛盾が生じる。したがって設計上の要点は、「誰が主体か」を増やすことではなく、既存の主体への遡及経路を切らさないことにある。

## 理論的背景

**機能的意図論(Gervais & Nay)**: AIシステムは法的人格を持たず、通常の意味での心も持たないが、契約法・不法行為法・会社法・刑事法を通じて、意図が内面の単純な報告であったことはないと論じられる。意図は推定され、帰属され、時に制度目的のために擬制される。この見方に立てば、AIは「法的主体の候補」ではなく、行為が特定の人間プリンシパルに帰属する「非人格的エージェント」として扱える。ただし、この帰属は現在の法的虚構に依存している点が指摘されている。

**委任の錯覚(Kong)**: エージェント型AIが「責任の空白」を生むという主張は、プリンシパルが個々の行為を意図・予見・統制していないことから、答責性が減るとみなす推論、すなわち「委任の錯覚」に基づくとされる。この論文は帰属可能性(attributability)、答責性(answerability)、説明責任(accountability)を区別し、自律性・不透明性・適応性が影響するのは帰属可能性であって、配備者の指針と統制に根ざした答責性は損なわれないと論じる。

**法の人間学的主権(Zito)**: 法的効果や基本権に匹敵する重大な効果をもたらす最終決定は、法の枠内で行動する有能かつ答責的な人間の決定者に帰属し続けなければならない。AIは補助できるが、自律的あるいは並行的な決定権限の源にはなれない。その根拠は、法的紛争の実存的な意味を理解し、解決の責任を引き受ける人間固有の能力に求められる。

**人格付与への批判(Kajino、Ayalew)**: Kajinoは、AIに法的人格を与えて独立した権利義務の主体とする提案を、システム論理・法と経済・安全保障の観点から根本的な設計上の失敗(アンチパターン)として退ける。意思決定権の所在を明確にできないまま権利を付与すれば、責任帰属に矛盾が生じるという趣旨である。Ayalewは、エチオピア正教の伝統から、知能は人格ではなく、能力は権威ではないといった区別を再構成し、「能力が高まれば人格や権威に近づく」という推論をカテゴリーエラーとして退ける。

**モジュール型の法的・組織的構造(Okuno & Okuno)**: 「モジュール型法人格」は、AIに法人格や自律的責任を与える概念ではない。AIのユースケースを企業システム上の中間的な境界として捉え、その周囲に人間と企業の責任を構造化する法的・組織的アーキテクチャとして提案されている。ユースケースごとにリスクプロファイルが異なるため、異なる構造が必要であり、段階的な実装がデプロイに先行すべきだとされる。

なお、デジタル時代の法制度が人間中心主義的で、AI生成物の所有や責任の帰属に対応できていないという指摘(Bhat & Raghavan)や、リーダーシップ研究におけるAI時代の再概念化の必要性(Liu ら)も、周辺的な文脈として参照できる。

## AI Nativeな設計への示唆

- **責任の遡及経路を設計要件にする**: あらゆるAIエージェントの行為について、配備者・設置者まで辿れる経路(誰が配備し、どの指針と統制を与えたか)を、記録可能な形で維持する。
- **人格ではなく帰属で設計する**: 責任の受け皿としてAI自体を主体化する案は避け、既存の代理・使用者責任・法人帰属の枠組みを拡張して対応する。
- **重大な最終決定の人間帰属**: 基本権や法的効果に関わる決定は、答責的な人間の決定者に帰属させ、AIは補助に位置づける。
- **自律性の増大を答責性の減免理由にしない**: 自律性、不透明性、適応性は帰属の難しさとして扱い、配備者の指針・統制に根ざした答責性の根拠は保持する。
- **ユースケース単位のモジュール型統治**: モデル単位の統制だけでなく、ユースケースごとの組織的関係とリスクに応じた責任構造を、導入前に段階的に整える。
- **能力と権威の分離**: 流暢さや性能の高さを、そのまま意思決定権限の根拠にしない。

## 関連コンセプト

- [[ai-accountability-attribution]] — AIシステムの責任帰属そのものを扱う関連概念
- [[evidence-bearing-decision-traceability]] — 遡及可能性を支える、証拠を伴う意思決定の追跡
- [[human-provenance-attribution-framework]] — 人間起源の帰属・来歴管理
- [[multi-actor-value-chain-liability-reallocation]] — 多主体の価値連鎖における責任配分
- [[boundary-invariant-first-architecture-and-modular-governance]] — 用途別モジュール型統治との接続
- [[formal-rule-shadow-labor-accountability-gap]] — 形式と実務の間の説明責任ギャップ
- [[incentive-compatible-control-of-hidden-agents]] — 隠れた選好を持つエージェントの制御
- [[surface-substrate-divergence]] — 宣言と実質の乖離、意図と原因の切り分け

## 参考ソース

- Intelligence Is Not Personhood: An Ethiopian Orthodox Contribution to Christian Theological Anthropology and AI Ethics — Yodit Ayalew, 2026 (`raw/papers/law/intelligence-is-not-personhood-an-ethiopian-orthodox-contribution-to-christian-t.md`)
- The Phantom Agent: Artificial Intentionality and Legal Responsibility — Daniel J. Gervais, John J. Nay, 2026 (`raw/papers/law/the-phantom-agent-artificial-intentionality-and-legal-responsibility.md`)
- The Anthropological Sovereignty of Law: Artificial Intelligence, Interpretation, and the Human Reserve of Judgment in the Algorithmic Age — Luigi Zito, 2026 (`raw/papers/law/the-anthropological-sovereignty-of-law-artificial-intelligence-interpretation-an.md`)
- The delegation illusion: why deploying autonomous AI agents does not diminish principal responsibility — Chun Yin Kong, 2026 (`raw/papers/law/the-delegation-illusion-why-deploying-autonomous-ai-agents-does-not-diminish-pri.md`)
- Reconfiguring Identity, Ownership, and Legal Framework in the Digital World — Anushree Bhat, Sreelatha Raghavan, 2026 (`raw/papers/law/reconfiguring-identity-ownership-and-legal-framework-in-the-digital-world.md`)
- Decisive Refutation of AI Personhood: The Logical Collapse of "Agency Risk" and "Attack Surface" — Hideo Kajino, 2026 (`raw/papers/law/decisive-refutation-of-ai-personhood-the-logical-collapse-of-agency-risk-and-att.md`)
- Modular Legal Personhood for AI Use Cases: An Enterprise Systems Engineering Framework for Digital Transformation — Mayumi J. Okuno, Hiroshi G. Okuno, 2026 (`raw/papers/law/modular-legal-personhood-for-ai-use-cases-an-enterprise-systems-engineering-fram.md`)
- Transformational Leadership in the Age of Artificial Intelligence: A Systematic Review and Research Agenda — Zhijiang Liu, Jacquline Tham, Ooi Boon Keat, 2026 (`raw/papers/leadership_ob/transformational-leadership-in-the-age-of-artificial-intelligence-a-systematic-r.md`)
