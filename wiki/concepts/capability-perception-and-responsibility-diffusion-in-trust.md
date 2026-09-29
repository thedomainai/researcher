# 能力知覚・代理性知覚と信頼・責任転嫁

## 概要

信頼は、対象の**能力(competence)の評価**と**善意(benevolence、共感)の知覚**という複数の次元から形成される。一方、利用者がシステムを「受動的な道具」ではなく「自律的な代理実行者」と見なすと、行為の道徳的責任が自分から離れていく(責任転嫁)。さらに、技術の導入は仕事に対して新たな**要求**と新たな**資源**を同時にもたらすため、受容や遵守の程度は知覚と文脈に左右される。

AI Nativeな社会設計では、AIが助言・診断・実行を担う場面が増える。そこでは「どれだけ信頼されるか」だけでなく、「何に基づいて信頼されるか」「責任の所在がどこへ移るか」が設計課題になる。本記事は、この三つの論点(信頼形成の多次元性、代理性知覚と責任転嫁、要求と資源の両義性)を、ソースに基づいて整理する。

## メカニズム

以下は、対象を人間・AI・組織・技術のいずれに入れ替えても成り立つ構造的な原理として整理したものである。

### 1. 信頼形成の多次元性
信頼の対象(人、AI、組織)が何であれ、信頼は少なくとも「できるか(能力)」と「配慮してくれるか(善意)」の二つの知覚から形成される。能力の効き方は課題の複雑さによって調整されうる。機能的な性能だけでは信頼は完結せず、関係的な要素が別に必要になる。

### 2. 代理性の知覚と責任の移動
行為者が、対象を「自律的に目標を持って動く代理実行者」と知覚するほど、自分の行為の責任を対象へ移す(責任転嫁)。これは道徳的離脱の一形態であり、実際の行為に先立って(予期的に)働き、非倫理的な行動意図を高めうる。責任の所在が知覚によって動く点は、対象が人間の代理人でも組織でも技術でも同型である。

### 3. 要求と資源の両義性
新しい仕組みは、負荷(要求)と支援(資源)を同時にもたらす。最終的な影響は、受け手の知覚と文脈条件(個人の資源、組織的支援など)に依存する。同じ導入でも、不安に転じることも優位性に転じることもある。

### 4. 信頼の不一致
信頼の形成と、実際の遵守・行動は必ずしも一致しない。専門家であっても、導入されたシステムに懸念を抱くことがある。投資や導入の規模は、有効な利用を保証しない。

## 理論的背景

**信頼の二つの先行要因(ソース1)**
AIによるセルフ診断を扱う研究は、AIの善意(共感)と能力を信頼の二つの先行要因として位置づけ、能力の効果が課題の複雑さによって調整されるモデルを提案している。準実験による検証が計画されている段階で、実証結果はまだ示されていない。この研究が強調するのは、正確性だけでなく信頼が導入の成否を左右するという点である。ただし、「共感」という要素がどのような心理的メカニズムで働くかは、なお不明確である。

**遵守における人間-AI信頼の不一致(ソース2)**
AIが生成する情報セキュリティ推奨への遵守を扱う研究は、AI対応のセキュリティへの巨額の投資が、有効な展開と利用を必ずしも保証しないと指摘する。InfoSec専門家のような主要な利用者ですら、AIに懸念を抱いている。この研究は信頼の不一致のメカニズムを扱う。ただし対象が特定の職業に限られるため、一般化には限界がある。

**要求-資源の枠組み(ソース3)**
Job Demands–Resources(JD–R)モデルに基づく研究は、AIを、新たな要求を導入すると同時に新たな資源を可能にする職務特性として概念化する。適応的気質や自己効力感といった個人資源、職務の複雑さという挑戦的要求、知覚された組織的支援という職務資源が、革新的な業務行動をともに形づくると想定している。最終的な影響は、従業員の知覚と文脈条件に依存する。

**代理性知覚と道徳的離脱(ソース4)**
ECサイトのアフターサービスで、生成AIを使って商品損傷の証拠を偽造し、不正に返金を請求する行動を扱う研究である。ここでの知覚されたAI代理性とは、AIが受動的な道具ではなく自律的な代理実行者として働くという、消費者の主観的な帰属を指す。道徳的離脱理論に基づき、この知覚が責任の転嫁を活性化し、予期的な道徳的離脱を引き起こして、非倫理的な行動意図を高めるという命題が立てられている。被害者の特定可能性と警告メッセージの種類が境界条件として導入され、4つのシナリオ実験が設計されている。3次元の概念化にも触れているが、抜粋の範囲では詳細は確認できない。

**信頼を関係的成果とみなす枠組み(ソース5)**
BEETSフレームワークは、バイアス、公正性、倫理、信頼、セキュリティを、機能的には区別されるが相互に結びつく責任あるAIの次元として統合的に整理する。倫理は説明責任を運用するガバナンス層、信頼は関係的な成果として位置づけられる。感情は情動的な下位層として扱われる。これは実証研究ではなく概念的貢献である。

**利用方法に依存する影響(ソース6)**
AIと批判的思考の関係を論じた研究は、AIが利用のされ方によって批判的思考の促進要因にも制約要因にもなりうると論じる。これは、能力への信頼が依存や思考の外部化に転じうることを考える手がかりになる。

## AI Nativeな設計への示唆

1. **能力と善意を分けて設計・評価する。** 精度の提示と、利用者への配慮の表現は別の信頼経路である。課題の複雑さに応じて、能力の見せ方を調整する。
2. **代理性の演出に慎重になる。** AIを自律的な実行者として見せる設計は、利用者による責任の転嫁を助長する恐れがある。責任の所在(誰が最終的に決めるか)をインターフェース上で明示し、警告メッセージは種類ごとの効果を検証して設計する。
3. **行為の影響を受ける側を可視化する。** 被害者の特定可能性が境界条件として扱われているため、行為の帰結や影響を受ける人を見えるようにする工夫は、責任転嫁への対策候補になる。
4. **導入を要求と資源の両面から設計する。** 新たな負荷だけでなく、組織的支援や自己効力感を高める資源を同時に用意する。
5. **信頼と遵守の乖離を前提にする。** 利用者の主観的信頼だけでなく、実際の遵守や行動を測定し、導入の有効性を評価する。
6. **批判的思考を保つ利用様式を促す。** AIを判断の代替ではなく、思考を支える手段として使う設計にする。

## 関連コンセプト

- [[ai-ethics-trust-transparency]] — AIの倫理・信頼・透明性
- [[ai-ethics-and-moral-agency]] — AIの倫理的エージェント性
- [[ai-alignment-and-moral-agency]] — AIアラインメントと道徳的エージェンシー
- [[digital-human-error-trust-dynamics]] — デジタルヒューマンの信頼喪失ダイナミクス
- [[fluency-induced-trust-miscalibration]] — 流暢性による信頼キャリブレーションの歪みと迎合の罠
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失
- [[ai-disclosure-and-organizational-trust]] — AI関与開示が組織の信頼性に与える影響
- [[digital-responsibility-paradoxes]] — 医療デジタル化におけるパラドキシカルな対立
- [[distributed-agency-and-assemblage-reconfiguration]] — 分散的行為者性と組織アセンブリッジの再構成

## 参考ソース

1. Patient Trust In Ai Self-Diagnosis — Vishal Uppala, Supavich Pengnate (2026)
   `raw/papers/complexity_science/patient-trust-in-ai-self-diagnosis.md`
2. Compliance with AI-Generated InfoSec Recommendations — Arman Falahati, Laura Amo, Joana Gaia (2026)
   `raw/papers/complexity_science/compliance-with-ai-generated-infosec-recommendations.md`
3. From Anxiety to Advantage: A Multi-Level Framework for AI-Driven Performance — Jairo de Jesus, Jayabhushan Praneeth Pallepogu, Reza Vaezi (2026)
   `raw/papers/complexity_science/from-anxiety-to-advantage-a-multi-level-framework-for-ai-driven-performance.md`
4. From Tools to Proxy Executors: The Role of Perceived AI Agency in Unethical Consumer Behavior — chen wang, Jiacheng Zhang, Xincan Liu, Xi Wang (2026)
   `raw/papers/complexity_science/from-tools-to-proxy-executors-the-role-of-perceived-ai-agency-in-unethical-consu.md`
5. The BEETS framework for responsible artificial intelligence — Sharon Tettegah (2026)
   `raw/papers/complexity_science/the-beets-framework-for-responsible-artificial-intelligence.md`
6. PSYCHOLOGICAL CHARACTERISTICS OF THE RELATIONSHIP BETWEEN ARTIFICIAL INTELLIGENCE AND CRITICAL THINKING — Mehrigul Abdurasulova (2026)
   `raw/papers/complexity_science/psychological-characteristics-of-the-relationship-between-artificial-intelligenc.md`
