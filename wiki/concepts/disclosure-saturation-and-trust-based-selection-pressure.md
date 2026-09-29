# 開示の飽和と信頼を介した選別圧力

## 概要

開示の飽和と信頼を介した選別圧力とは、次の二つの構造を合わせた原理である。

1. **開示の飽和**: 受け手の認知負荷(処理できる情報量)が固定されている限り、情報開示を増やしても得られる価値は逓減する。
2. **信頼を介した選別圧力**: 外部からの監視や開示は、情報そのものを増やすというより、信頼の形成と利害構造を通じて主体の行動を選別・変化させる。

AI Nativeな社会では、AIが報告書・ログ・説明文を大量かつ低コストに生成できる。開示の供給量は容易に増え、受け手の処理能力との差は開きやすい。そのため「もっと開示する」「もっと監視する」だけでは透明性は改善せず、何をどの構造で開示し、誰の利害のもとで監視するかを設計することが重要になる。

## メカニズム

以下は対象(人間・AI・組織・技術)を入れ替えても成立する構造的原理として整理したものである。

### 1. 認知負荷の上限による限界効用逓減
受け手(投資家、利用者、規制者、あるいは監督するAIエージェント)の処理容量が一定なら、開示の量・範囲・複雑性が増すにつれ、追加情報の価値は初期に上昇した後で頭打ちになり、やがて低下しうる。情報の空白が埋まる段階では価値が増すが、飽和閾値を超えると追加分は理解に寄与しにくくなる。この閾値は文脈に依存する。

### 2. 所有・利害構造による開示の歪み
開示の内容は、開示主体の背後にある利害構造に左右される。主体を取り巻く利害関係者が多様であれば、宣言した約束と実際の行動が整合しているかという開示にも、利益相反を通じて差が生まれる。開示は中立の窓ではなく、利害構造が形作る成果物である。

### 3. 監視による選別圧力
外部監視が行動を変える経路は、単なる情報量の増加ではない。監視・コミュニケーションが信頼を形成し、情報ガバナンスと監督の効果を通じて、行動の良し悪しが選別される。行動が変わるのは、信頼を得られる主体が有利になる圧力が働くためである。

### 三つの統合
- 開示量を増やしても、受け手が処理できなければ信頼形成には寄与しない。
- 利害構造が開示の質を規定する。
- 信頼と監督を通じた選別が、最終的な行動変化を生む。

## 理論的背景

### Corporate Disclosure Saturation Theory(CDST)
Joshi(2026)は、サステナビリティ報告における開示の量・広さ・複雑性が増すにつれて情報便益がどう変化するかを説明する概念的枠組みとしてCDSTを提示している。ステークホルダー情報ニーズ、開示の関連性、測定、報告上の課題などの研究を理論駆動で統合し、追加開示の限界価値は、情報ギャップが減る間は増加しうるが、文脈依存の飽和閾値に近づくと逓減しうると論じる。核心的知見は、ステークホルダーの認知負荷が固定である限り限界効用の逓減は必然的に生じる、という点である。

### 所有構造と気候・ロビー活動整合性の開示
Al Amosh(2026)は、企業の気候ロビー活動が公表済みの気候コミットメントと整合しているかの開示(CLAD指数)を、欧州11カ国の上場2138社を対象に2012〜2023年のパネルで分析している。指数は手作業のコンテンツ分析と第三者評価で構築されている。エージェンシー理論、スチュワードシップ、社会情緒的資産、制度の各視点から、家族・機関・国家・外国・経営者所有の影響を検討しており、所有構造の多様性が利益相反を形成し、整合性開示に影響するという知見が示されている。

### 投資家関係管理と信頼メカニズム
Song、Xie、Zhang(2026)は、中国A株上場企業の2013〜2022年のサンプルで、投資家関係管理(IRM)の水準が企業のグリーンイノベーションと正の関連を持つことを示した。IRMの各側面のうち、ウェブでのコミュニケーションとフィードバックの側面が最も一貫した正の関連を示し、他のチャネルの結果はモデル設定により異なる。作用経路は情報ガバナンス効果と監督・管理効果であり、環境規制の強度やグリーンファイナンスの水準が効果を高める。本記事はこれを、外部監視が信頼メカニズムを通じた選別圧力として働く例と位置づける。

### 認識論的背景
Sułkowskiら(2026)は、AI・デジタルプラットフォーム・ビッグデータが社会科学・経営研究の基盤をどう変えるかを扱い、データ豊富な環境での問いの設定、アルゴリズムバイアス、倫理リスクへの対応を論じている。知識生成の前提が変わるなかで、情報の量と知の質を区別する必要があるという本概念の問題意識と接続する。ただし、開示飽和そのものを扱った知見ではない。

## AI Nativeな設計への示唆

1. **開示量ではなく吸収可能性を設計指標にする**: 開示の評価軸を「網羅性」から「受け手が処理し判断に使えるか」へ移す。階層化された要約、優先度付け、判断に関連する情報の抽出など、受け手の認知負荷を前提にした提示が必要になる。
2. **飽和閾値を文脈ごとに見積もる**: 閾値は文脈依存であるため、受け手・タスクごとに開示量を調整し、効果を測って改善する。
3. **開示主体の利害構造を併せて記録する**: 開示内容だけでなく、その主体の所有・インセンティブ構造(誰が利益を得るか)を評価の入力にする。AIエージェント間でも、運営主体の利害が開示の信頼性を左右する。
4. **監視を信頼形成の仕組みとして設計する**: 双方向のフィードバックチャネルなど、信頼の形成と監督が結びつく経路を持たせる。監視が単なるログの蓄積にならないよう、行動の選別につながる構造を用意する。
5. **宣言と行動の整合性を開示対象にする**: 公表された方針と実際の行動のずれ(コミットメントと実行の整合)を検証可能にする。
6. **自動生成による開示インフレに備える**: AIで開示を安価に増やせるほど飽和は早く訪れる。量を増やすインセンティブと、受け手の処理能力の限界との間の緊張を前提に設計する。

## 関連コンセプト

- [[absorption-capacity-bottleneck-saturation]] — 吸収コストとボトルネックによる価値飽和。受け手側の処理限界という同型の構造を扱う。
- [[multidimensional-trust-formation-and-oversight]] — 信頼形成と監督の関係。
- [[effort-opacity-and-disclosure-signal-erosion]] — 開示シグナルの劣化。
- [[ai-disclosure-and-organizational-trust]] — AI関与の開示が信頼に与える影響。
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失。
- [[pluralistic-legitimacy-and-trust-signaling]] — 信頼シグナリングの構造。
- [[local-rules-to-emergent-collective-order]] — 局所ルールと選別から創発する秩序。
- [[ai-ethics-trust-transparency]] — AIの倫理・信頼・透明性。
- [[reward-design-induced-misleading-and-miscalibrated-trust]] — 報酬設計が生む信頼の較正ずれ。

## 参考ソース

1. Beyond Disclosure Saturation: A Theory of Diminishing Returns in Corporate Sustainability Reporting — Prem Lal Joshi (2026)
   File: raw/papers/corporate_governance/beyond-disclosure-saturation-a-theory-of-diminishing-returns-in-corporate-sustai.md
2. Who Owns the Message? Ownership Structure and Climate‐Lobbying Alignment Disclosure in Europe — Hamzeh Al Amosh (2026)
   File: raw/papers/corporate_governance/who-owns-the-message-ownership-structure-and-climatelobbying-alignment-disclosur.md
3. Interoperability is new: investor relations management and corporate green innovation — Jingnan Song, Yanxiang Xie, Jihua Zhang (2026)
   File: raw/papers/corporate_governance/interoperability-is-new-investor-relations-management-and-corporate-green-innova.md
4. Epistemology and Methodology of Research in AI Age — Łukasz Sułkowski, Zdzisława Dacko-Pikiewicz, Katarzyna Szczepańska‐Woszczyna (2026)
   File: raw/papers/economics/epistemology-and-methodology-of-research-in-ai-age.md
