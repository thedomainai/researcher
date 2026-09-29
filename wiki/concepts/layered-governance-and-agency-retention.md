# 層別ガバナンスと主体性の保持

## 概要

層別ガバナンスと主体性の保持とは、データ・モデル・学習といったシステムの層ごとに統治権が非対称に配分されることを前提に、最下層(あるいは最も見えにくい層)で人間の主体性が失われないよう制度を設計する、という原理である。持続的な協働が成り立つかどうかは、この配分と制度設計に左右される。

AI Nativeな社会設計では、意思決定や価値の生成が多層のシステムに分散する。ある層で参加者に発言権が与えられていても、別の層で実質的な支配が固定されていれば、参加は形式にとどまる。ソース[1]は、単に「データを守る」だけでは不十分で、「モデルを統治する」ことが必要だと論じる。ソース[2]は、評価や統治といった制度条件が人間-AI協働の持続性を決めると論じる。本概念はこの二つの視点を統合したものである。

## メカニズム

対象を人間・AI・組織・技術のいずれに入れ替えても成り立つ構造的原理として、次の三点に整理できる。

### 1. 統治権の非対称配分

システムが複数の層(下位の資源保持、中位の流通、上位の学習・生成など)からなるとき、各層で誰が決定権を持つかは一様ではない。上流の層(保管・共有)では参加者の統治が確立できても、成果物を形づくる層では統治が届かない、という偏りが生じうる。この偏りは個別の運用ミスではなく、構造として現れる。

### 2. 制度的評価と行動正規化のループ

何を評価し、何に報いるかという制度が、参加者の行動を特定の型に寄せていく。この正規化が繰り返されると、制度の中に創発的なパターンが生まれ、組織の一貫性、文脈に応じた判断、学習、適応能力に影響する。評価の設計は、主体性を保持する側にも侵食する側にも働く。

### 3. 権力集中の構造化

計算や参加が分散していても、結果として得られる資産(モデルなど)が、訓練を招集した主体に帰属し続けるなら、権力は実質的に集中する。分散という形式と、統治の実質は別問題である。

## 理論的背景

**分散学習における層別の主体性(ソース[1])**
連合学習は、個人データが端末に残り更新のみが共有される点でプライバシー保護の進歩として語られる。しかし著者らは、これが分散型ソーシャルウェブの語彙を借りながら論理を反転させていると指摘する。計算は分散されるが、結果のモデルは訓練を招集した主体のもとに残るからである。したがって連合は、それ自体では搾取的AIへの解決策にならない。結果は、誰がデータとモデルを統治し、それらを形づくる実践に対して誰が主体性を持つかに依存する。著者らは、創作コミュニティが作品を保持する三つの層として、保管(storage)、流通(circulation)、学習(learning)を挙げる。アーティスト管理のトラスト、協同組合、同意基盤を検討し、創作者のガバナンスは保管と流通では確立できるが、学習では止まると論じる。貢献者は訓練に同意できても、その結果に対する発言権はほとんどない。

**制度設計としての持続的協働(ソース[2])**
ソース[2]は、AI媒介型の制度における人間-AI協働の有効性と持続性が、評価・統合・統治・人間の専門性の活用に関する制度条件に依存すると論じる概念的研究である。インセンティブ構造、階層的な情報フィルタリング、行動正規化ループの相互作用が創発的な制度パターンを生み、組織の一貫性や文脈的意思決定、学習、適応能力に影響するという。著者の既存の枠組みHCESFが、倫理的基盤として設計上の対応を支える。

**分散環境での適切性の文脈的再交渉(ソース[3])**
MastodonとBluesky利用者への20件の半構造化インタビュー(七つの生成AIシナリオ)から、参加者は生成AIの特定の構成に対して条件付きの境界を引いて適切性を判断していた。分散型ソーシャルメディアでは、決定がユーザー、開発者、モデレーター、管理者に分散し、生成AIは集団的ガバナンスの課題となる。賛成・反対の二項対立では捉えられない、文脈的な交渉が行われている。

**倫理性の認知と信頼(ソース[4])**
ランダム化比較研究により、AIツールの説明可能性(xAI)への信念や道徳的強度(結果の大きさ、近接性)が、AIの倫理性の認知にどう影響するか、そしてその認知が推奨意向や機能への信頼にどう影響するかが検討されている。統治の正統性が、利用者の信頼形成を通じて協働の持続に関わることを示唆する。

## AI Nativeな設計への示唆

- **層ごとに統治権の所在を明示する。** 保管、流通、学習などの各層で、誰が何を決められるかを可視化し、どの層で主体性が途切れるかを設計段階で点検する。
- **同意を統治の代替にしない。** 訓練への同意だけでは、結果として得られるモデルへの発言権は保証されない。最下層(学習・モデル形成)にも参加者の統治手段を設ける。
- **分散を統治と混同しない。** 計算や参加の分散は、成果物の帰属や管理権の分散を意味しない。分散の形式ではなく、結果の帰属を評価する。
- **評価制度を設計対象とする。** 評価やインセンティブが行動を正規化していくため、それが人間の専門性や文脈判断を損なわないかを継続的に検証する。
- **文脈に応じた境界の交渉を許容する。** 適切性の判断は文脈的に再交渉されるため、コミュニティが条件付きの境界を引ける仕組みを残す。
- **正統性と信頼を設計要素に含める。** 説明可能性や影響の大きさに関する認知が信頼に影響するため、利用者が倫理性を判断できる情報を提供する。

## 関連コンセプト

- [[human-ai-agency-configuration]] — 人間とAIのエージェンシー構成
- [[human-ai-interaction-sense-of-agency]] — ヒューマンAIインタラクションと主体感
- [[ai-sensemaking-human-agency]] — AIセンスメイキングと人間のエージェンシー
- [[machine-speed-oversight-asymmetry]] — 機械速度と人間速度の統治非対称性
- [[ai-governance]] — AIガバナンス
- [[ai-and-algorithmic-governance]] — AIとアルゴリズムガバナンス
- [[public-signal-cascade-and-judgment-homogenization]] — 公開シグナルによる判断のカスケードと多様性の収斂
- [[shared-editable-state-and-evaluability-design]] — 共有可変状態と評価可能性を担保する情報設計

## 参考ソース

1. Phoenix Perry, George Simms, Elizabeth Wilson, Yasmine Boudiaf, Nick Bryan-Kinns (2026)「Govern the Model, Not Only the Data: Storage, Circulation, and Learning in Creative AI」
   File: raw/papers/hci/govern-the-model-not-only-the-data-storage-circulation-and-learning-in-creative-.md
2. Taha Khan (2026)「Sustainable Human-AI Collaboration: A Human-Centered Institutional Design for AI-Mediated Institutions Version 3」
   File: raw/papers/hci/sustainable-human-ai-collaboration-a-human-centered-institutional-design-for-ai-.md
3. Romina Mahinpei, Manoel Horta Ribeiro, Andrés Monroy-Hernández, Sohyeon Hwang (2026)「"Okay, I've Actually Softened My Take on This": How People in Decentralized Social Media Reason about the Appropriateness of Generative AI」
   File: raw/papers/hci/okay-ive-actually-softened-my-take-on-this-how-people-in-decentralized-social-me.md
4. Rachel Detherage, Shane Connelly (2026)「The context of AI transformation: perceptions of AI ethicality and their impact on trust and use intentions」
   File: raw/papers/hci/the-context-of-ai-transformation-perceptions-of-ai-ethicality-and-their-impact-o.md
