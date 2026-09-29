# 制度による情報非対称性の橋渡しと二重経路の信頼形成

## 概要

リスクや便益を利用者自身が評価しにくい対象(新しい技術、長期的な影響を持つ政策、AIシステムなど)に対して、人はどのように信頼を形成し、使い続ける、あるいは拒むという判断に至るのか。この概念は次の原理を述べている。

- 評価が困難な対象への信頼は、制度やガバナンスが情報の非対称性を橋渡しすることで成立する。
- その信頼は認知的信頼と感情的信頼という二つの経路を通じて形成される。
- 二つの経路は、継続利用と抵抗という別々の結果へ分岐しうる。

AI Nativeな社会では、AIが医療・感情支援・行政・エネルギーなど評価の難しい領域に入り込む。利用者はモデルの内部を検証できず、提供者との間に構造的な情報格差がある。このとき、信頼を個々のAIの性能や見た目だけに委ねる設計は不安定になる。制度的な保証の層を設計し、認知と感情の両面から信頼を扱う必要がある。

## メカニズム

この構造は対象を入れ替えても成立する。

1. **情報の非対称性**: 評価する側(市民、利用者、専門家)は、評価される側(技術、企業、AI)のリスクを直接確認できない。不確実性が高く、影響が長期にわたるほどこの格差は大きくなる。
2. **制度ベース信頼による媒介**: 直接評価できない代わりに、評価者は政府・企業・規制といった制度的主体への信頼を代理指標として使う。制度がリスク評価の肩代わりをすることで、受容が成立する。
3. **二重経路**: 制度への信頼は二つの経路に展開する。
   - 認知的信頼: 「役に立つか」「有能か」という評価につながる。
   - 感情的信頼: 「思いやりがあるか」「配慮されているか」という評価につながる。
4. **行動の分岐**: 二つの評価は、継続利用と抵抗という別々の採用後の結果を予測する。抵抗は継続利用の単なる裏返しではなく、独立した結果として扱われる。
5. **ガバナンス強度による調整**: 知覚されたガバナンスの強さが、信頼が行動上の依存へ変換される度合いを調整する。
6. **段階的相互作用による共進化**: 信頼は一度に確定せず、反復的な相互作用の中で、異質な主体間の信頼状態が共に変化していく。

この連鎖は、対象が人間の専門家でもAIでも組織でも技術でも、「検証困難性 → 制度による代理 → 認知・感情の二経路 → 行動の分岐」という形で再現される。

## 理論的背景

**AIガバナンスと感情支援AI(Yang, Zhao, Konopka, 2026)**
社会認知理論、制度ベース信頼、採用後研究を統合し、二重経路モデルを提案している。認知的信頼は知覚された有用性へ、感情的信頼は知覚された思いやりへとつながる。この二つの価値評価が、継続利用と抵抗という別々の採用後の結果を予測する。知覚されたAIガバナンスの強さは、信頼が行動上の依存に変換される過程を調整する。モデルはEU・米国・中国の比較事例研究で、二次データをパターンマッチングで分析して検討されている。

**再生可能エネルギー受容と制度信頼(Stuhm, Baumann, Weil, 2026)**
エネルギー転換政策は不確実性が高く、影響が長期的で、情報の非対称性がある。そのため市民はリスクと便益の評価を制度的主体に頼らざるを得ない。この研究は、従来の研究が政府と企業への信頼を区別してこなかった点を課題とし、制度信頼の形態ごとの違いを検討している。制度信頼が技術リスク評価における情報の非対称性を橋渡しし、受容を媒介するという点が本概念の核である。

**人間とAIのチームにおける信頼の共進化(Mahmud, 2026)**
Hanelt et al. (2026) の質的研究では、人間の専門家、AI、クライアントの三者関係で、信頼構築が「恐れによる排除」「統制された開放」「機会的チーミング」という三段階で進むとされる。Mahmudはこれを受け、AIをチームの一員と捉え直し、異質なエージェント間で共有された信頼状態が反復的な相互作用を通じて共進化する過程を、エージェントベースモデリングで探ることを提案している。これは提案段階の研究である。

**周辺的な知見**
- 若年層の感情支援チャットボット利用の研究(Osetrow et al., 2026)は、機能的有用性を超えて、どの条件で利用者がシステムを信頼するかを問い、混合研究法で検討している。
- 「Attachment by Design」(Scurtu, 2026)は、AIへの愛着を既存理論で説明できるとし、愛着形成、システムのアフォーダンスによる強化、依存、提供者のガバナンスの四層を区別する暫定的枠組みを示している。新たな基礎的心理メカニズムは確立されていないとする。
- 市民のコンプライアンス支援を扱うHARMONY(Hasmawaty et al., 2026)は、社会規範理論と説得的技術に基づき、強制的な自動執行への心理的リアクタンスに対処する枠組みである。

## AI Nativeな設計への示唆

- **制度層を設計の一部として扱う**: 利用者が検証できない部分は、ガバナンスの強さとその知覚可能性によって補う。ガバナンスは実質だけでなく、利用者にどう認識されるかも信頼形成に影響する。
- **認知と感情を分けて設計・計測する**: 有用性の担保(認知的信頼)と、配慮や誠実さの伝達(感情的信頼)は別の経路であり、それぞれ評価指標を持たせる。
- **継続利用と抵抗を別指標として観測する**: 利用率が高いことは抵抗の不在を意味しない。二つを独立した結果として追跡する。
- **制度主体ごとの信頼を区別する**: 政府、企業、提供者への信頼を一括りにせず、どの主体が情報の橋渡しを担っているかを分けて把握する。
- **信頼を段階的に育てる**: 信頼は反復的な相互作用の中で共進化する。AIの権限や開放度を、段階に応じて統制しながら広げる設計が考えられる。
- **提供者支配の構造に注意する**: 愛着や依存はシステムのアフォーダンスによって強まりうるため、提供者側のガバナンスも設計と監督の対象に含める。
- **文脈差を前提にする**: 国ごとにガバナンスの強度や知覚が異なるため、同一のAIでも制度環境により信頼の帰結が変わりうる。

## 関連コンセプト

- [[multidimensional-trust-formation-and-oversight]] — 多次元的な信頼形成と監督による媒介
- [[scoped-trust-and-automatic-deference-asymmetry]] — 機能限定的な信頼と権威への追従の非対称性
- [[prior-attitude-filtered-trust-formation]] — 事前態度に濾過される信頼形成
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失
- [[verification-cost-and-trust-testing-of-automated-advisors]] — 検証コストと信頼判定
- [[complementary-information-and-epistemic-asymmetry]] — 補完的情報構造と認識論的非対称性
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入速度と統治能力の非対称ギャップ
- [[trust-continuity]] — 信頼の継続性
- [[ai-anthropomorphism-journey]] — AI擬人化の形成過程

## 参考ソース

1. Trusting to Continue or Resist: How AI Governance Shapes AI-Based Emotional Support Usages Across Countries — Ning Yang, Weijie Zhao, Björn Konopka (2026)
   File: raw/papers/sociology/trusting-to-continue-or-resist-how-ai-governance-shapes-ai-based-emotional-suppo.md
2. Renewable energy acceptance and responsible actors: unravelling the influence of trust in governments and corporations — Patrick Stuhm, Manuel Baumann, Marcel Weil (2026)
   File: raw/papers/sociology/renewable-energy-acceptance-and-responsible-actors-unravelling-the-influence-of-.md
3. When AI Becomes a Teammate: Agent-Based Modeling of Triadic Human-AI Relationships — Jishan Mahmud (2026)
   File: raw/papers/sociology/when-ai-becomes-a-teammate-agent-based-modeling-of-triadic-human-ai-relationship.md
4. The Influence of Trust and Need Satisfaction on Young Adults' Interactions with AI Chatbots for Emotional Support — Stefanie Osetrow, Holger Klapperich, Alina Huldtgren (2026)
   File: raw/papers/sociology/the-influence-of-trust-and-need-satisfaction-on-young-adults-interactions-with-a.md
5. Trustworthy AI for Sustainable Cities: A Multimodal Orchestration Agent-Based Framework for Civic Compliance — Hasmawaty A.R., Zaid Amin, Nazlena Mohamad Ali, Rahma Santhi Zinaida (2026)
   File: raw/papers/sociology/trustworthy-ai-for-sustainable-cities-a-multimodal-orchestration-agent-based-fra.md
6. Attachment by Design: AI attachment under provider-controlled relational architecture — Luiza Scurtu (2026)
   File: raw/papers/sociology/attachment-by-design-ai-attachment-under-provider-controlled-relational-architec.md
