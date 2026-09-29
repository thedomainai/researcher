# アクセス格差による累積的集中と排除

## 概要

アクセス格差による累積的集中と排除とは、フロンティア技術へのアクセス差や、アルゴリズムによる個別の排除判定が、自己強化的なフィードバックループを通じて時間とともに累積し、権力・成果・不利益を特定の主体に不可逆的に集中させる構造的原理である。

初期のわずかな差(ある研究室だけがAIツールを使える、ある利用者だけが与信で不利に扱われる)は、一度きりの差にとどまらない。差は次の機会や資源の配分に影響し、その配分がさらに差を広げる。この経路依存性のために、後から差を埋めることが難しくなる。

AI Nativeな社会設計では、AIがあらゆる意思決定や価値創出の入力になる。そのため、アクセスの配分とアルゴリズムの透明性を設計上の中心課題として扱わなければ、効率の向上と引き換えに集中と排除が固定化するおそれがある。

## メカニズム

この原理は、対象が人間・組織・国・AIエージェントのいずれであっても、次の構造で成立する。

1. **初期のアクセス差**: 生産性を高める入力(AIツール、データ、プラットフォーム上の可視性など)を一部の主体だけが得る。
2. **自己強化ループ**: 入力を得た主体はより多くの成果や評価を得て、その成果がさらなる入力の獲得を可能にする。入力を得られない主体は逆方向に進む。
3. **累積的優位・不利の経路依存性**: 個々の判断では小さい差でも、時間とともに合成され、後戻りしにくい格差になる。個別の排除が生態系全体の累積的不利に変わる。
4. **不透明性による固定化**: 判断の根拠が見えないと、不利を受けた側は原因を特定できず、是正を求めにくい。不透明性は権力集中を強める。
5. **合理的な撤退**: 劣位の主体が競争から退くことが個別には合理的になり、集中がさらに進む場合がある。

このように、「入力の差 → 成果の差 → 入力の差の拡大」というループが、主体の種類を問わず働く。

## 理論的背景

### 科学的成果の配分モデル(Epstein, 2026)

Epsteinは、研究室が科学的評価(credit)を競う比例配分型のTullock contestモデルを構築した。一部の研究室だけがAIツールにアクセスでき、その生産性が高まるという設定である。論文が示す結果は3点ある。

- AIアクセスは全体の発見量を増やす。
- 一方で、自己強化フィードバックループを通じて、評価と資源がAI活用可能な研究室に集中する。
- 全研究室に基礎的なAIツールを提供する平準化介入により、格差を部分的に相殺できる。その代償として、全体の産出には一定の範囲内の損失が生じる。

論文はさらに、介入の社会的コストを含めた厚生分析を行い、制約付き最適政策を特徴づけている。勝者が大部分を取る評価配分の下では集中が最も深刻になり、完全情報の下では弱い研究室がフロンティア研究から合理的に撤退しうることも示唆されている。全体の生産性向上と集中が同時に起こる点が、この原理の要である。

### アルゴリズムによる複合的脆弱性(Moharrak & Mogaji, 2026)

AI媒介の金融サービスを扱う概念研究である。従来の研究はアルゴリズムバイアスを個別の意思決定の結果として扱い、不利がどう累積し持続するかへの注意が乏しかった。この研究は、アルゴリズム的脆弱性と複合的アルゴリズム脆弱性の概念を提示し、アルゴリズム的構造化、経験的脆弱性、生態系的媒介からなる多層フレームワークを構築している。個別の排除が、サービス生態系全体で累積的不利に変わるという点で、この原理の「排除」側の側面を示す。

### 社会的所属とインフラ(Naik, 2026)

スマートシティを題材に、社会的所属がもはや文化や空間だけで決まらず、デジタルインフラに統合され、都市のデジタル経済の恩恵を受けられるかどうかに結びつきつつあることを論じている。アクセスのない者は構造的に除外され、差別や排除、市民と制度の間の信頼の侵食のリスクが生じる。政策としては、デジタル包摂、経済参加、技術に関する意思決定への市民参加が挙げられている。

### 不透明性とプラットフォーム権力(Fernandes & Vlassis, 2026)

欧州の音楽産業について、22件の半構造化インタビューと360人への調査を行った研究である。音楽専門家にとって、公平性の中心的な次元は透明性だった。不透明性はプラットフォームの権力を強め、可視性や収益化、文化的多様性に影響すると受け止められている。AIは不透明な学習慣行などを通じて、こうした動態を強めるものと見られている。

### 関連する周辺知見

- **社会的地位の経路**(Redheadら, 2026): コロンビアの農村4集落(個人496名)で、威信(利益を与える能力)と支配(コストを課す能力)という地位の2つの経路を分析している。地位が社会的レベリングや利他・搾取行動に関わることを扱っており、集中がどのように形成・抑制されるかを考える参照点になる。
- **デフォルト設計による格差是正**(Hällら, 2026): スウェーデンで、新規移民家庭の3〜5歳児に園の枠を申請なしで提供する2023年の改革を、差の差の手法で評価している。制度側の初期設定を変えることで不平等の縮小を狙う事例であり、アクセス設計の介入の一例である。

なお、建築分野の支払意思額(WTP)のレビュー(Leら, 2026)も収集されたが、本概念との関係は間接的であり、ここでは詳述しない。

## AI Nativeな設計への示唆

- **アクセスの基礎水準を保証する**: 平準化介入は全体の産出を大きく損なわずに格差を縮める余地があることがモデルで示されている。基礎的なAI機能を全主体に提供する設計を、初期条件として組み込む。
- **ループの検知と遮断**: 評価・資源・可視性が特定の主体に偏っていく傾向を継続的に計測し、集中が不可逆になる前に介入する仕組みを持つ。
- **個別判定ではなく累積で評価する**: アルゴリズムの公平性を単発の判定ではなく、時間と生態系全体にわたる不利の蓄積として監査する。
- **透明性を設計要件にする**: 判断根拠の開示と異議申立ての経路を用意し、不透明性が権力集中の手段にならないようにする。
- **デフォルトの活用**: 申請や自己申告を要しない自動的な提供により、アクセスの障壁そのものを下げる。
- **撤退の抑制**: 劣位の主体が合理的に撤退しないよう、参加の便益が保たれる評価配分(勝者総取りを避ける設計)を検討する。
- **参加型の意思決定**: 技術に関する意思決定への市民参加を確保する。

## 関連コンセプト

- [[concentration-driven-systemic-risk-propagation]] — 集中が単一障害点となり、リスクが非線形に伝播する側面
- [[access-based-consumption]] — アクセスが所有に代わる消費形態としての関連
- [[incentive-driven-deferral-and-asymmetry]] — 情報非対称の固定化という共通構造
- [[ai-driven-job-displacement-economic-sovereignty]] — AI時代の経済的自立と格差
- [[fluency-induced-trust-miscalibration]] — 不透明なAIへの信頼の歪み
- [[bounded-diversity-adaptive-feedback-collectives]] — 多様性を保つフィードバック設計

## 参考ソース

1. Gil S. Epstein (2026). "The distribution of scientific power in the age of AI" — `raw/papers/behavioral_economics/the-distribution-of-scientific-power-in-the-age-of-ai.md`
2. Moayad Moharrak, Emmanuel Mogaji (2026). "Compound algorithmic vulnerability: a transformative service perspective on AI mediated financial services" — `raw/papers/behavioral_economics/compound-algorithmic-vulnerability-a-transformative-service-perspective-on-ai-me.md`
3. Hema Naik (2026). "Artificial Intelligence (AI) In Social Media Reshaping Identity: Community and Belonging" — `raw/papers/behavioral_economics/artificial-intelligence-ai-in-social-media-reshaping-identity-community-and-belo.md`
4. Marina Rossato Fernandes, Antonios Vlassis (2026). "The sound of fairness: AI and recommender systems in the European music industry" — `raw/papers/behavioral_economics/the-sound-of-fairness-ai-and-recommender-systems-in-the-european-music-industry.md`
5. Daniel Redhead, Arlenys Hurtado Manyoma, Danier Hurtado Manyoma, Cody T. Ross (2026). "Social and economic consequences of prestige and dominance in rural Colombian social networks" — `raw/papers/behavioral_economics/social-and-economic-consequences-of-prestige-and-dominance-in-rural-colombian-so.md`
6. Dinh Linh Le, Tuuli Myllymaa, Pekka Leskinen (2026). "Willingness to pay for sustainable and circular transitions in the built environment: a literature review" — `raw/papers/behavioral_economics/willingness-to-pay-for-sustainable-and-circular-transitions-in-the-built-environ.md`
7. Caroline Häll, Erica Lindahl, Olof Rosenqvist (2026). "Reforming the preschool application system to reduce enrollment gaps evidence from a default enrollment policy" — `raw/papers/behavioral_economics/reforming-the-preschool-application-system-to-reduce-enrollment-gaps-evidence-fr.md`
