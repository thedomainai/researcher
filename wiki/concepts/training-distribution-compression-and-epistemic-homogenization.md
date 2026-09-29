# 学習分布の圧縮による認識論的同質化と周縁知の消去

## 概要

学習分布の圧縮による認識論的同質化とは、知識を統計的に圧縮し再生成する仲介系(生成AI、推薦システム、標準化された教育課程など)が、多数派の視点を「標準」として固定し、周縁的・多元的な知や意味体系を他者化・単一化してしまう構造的傾向を指す。本コンセプトはTier 1(不変原理)に分類される。

この原理が重要なのは、圧縮が「中立的な要約」ではなく、何が代表的で何が例外かという判断を暗黙に含むためである。AI Nativeな社会では、知識の生成・検索・教育・解釈の多くがこうした仲介系を経由する。そのため設計を誤ると、認識論的多元性が意図されないまま静かに失われる。以下では、ソースの記述に基づいてこの構造を整理する。

## メカニズム

中核は次の三つの要素である。

1. **統計的圧縮による情報損失**:大量の知識を分布として学習・再生成する過程で、頻度の低い表現、文脈依存の意味、局所的な文脈は平均的な表現へと押しやられる。
2. **多数派バイアスの再生産**:訓練データの構成が特定の視点(ソースでは西洋中心のデータ)に偏ると、出力はその視点を標準として再生産し、他の視点を「他者」として描く。
3. **知識ヘゲモニーの権力構造**:何が正統な知かを決める力は、技術以前から存在する社会的な権力関係である。技術はそれを増幅・自動化する。

この構造は対象を入れ替えても成り立つ。

- **AI**:訓練データの分布が出力の「標準」を決める。
- **人間**:標準化されたカリキュラムを通じた学習が、特定の学問的系譜を正統とし他を周縁化する。
- **組織・制度**:評価基準や推薦アルゴリズムが、可視化される意味を選別する。
- **技術媒体**:デジタル化は、領域を問わずあらゆる知識体系に共通の変形メカニズムをもたらす。

つまり、仲介者が「多数派の統計的中心」を基準に知を再編するとき、その仲介者が機械か人間か制度かにかかわらず、同質化が生じる。

## 理論的背景

**認識論的転換としての圧縮**:Anasらの体系的レビュー(2026)は、AI設計における客観的理性から道具的合理性への転換が、人間の主体性や価値の担い手としての位置づけ、さらに知識の公平性に深刻な認識論的課題をもたらすと論じる。本記事の整理では、知識の統計的圧縮が多元的世界観を単一の理性へと同化させる点が核心的知見とされている。同レビューは、認識論的に公正なグローバルAIガバナンスのための倫理的政策提言も目的に掲げている。

**知識ヘゲモニーの普遍性**:Ruziyevaらの中央アジア高等教育の事例研究(2026)は、ウズベキスタンの地域公立大学で、Ibn Khaldun、Al-Farabi、Al-Biruni、Al-Ghazali、Yusuf Khas Hajibといった東方スコラ的経済思想を、工学・社会科学の一般教育に組み込む試行を扱う。核心的知見は、知識体系の権力政治が技術状況に関わらず、社会的学習の根本的メカニズムであるという点である。同質化はAI固有の現象ではなく、教育など従来の制度にも存在した構造の延長として理解できる。

**生成モデルにおける他者化**:Wangによる Midjourney の「Chinoiserie」画像240枚の分析(2026)では、モデルが属性の曖昧さ、構造的転位、文化的意味の断絶を示し、抽象的な山水様式でのみ高い適合性を示した。また、低いカメラアングルや要求的な視線(demand gaze)による、スペクタクル化・他者化された視点でヨーロッパ中心的な語りが構成され、ステレオタイプ的な記号が極めて高い割合を占めた。さらに、専門的な制約を与えるとむしろ記号の積み重ねが悪化するという逆説も報告されている。プロンプトの工夫だけでは圧縮された分布の偏りを解消できない可能性を示唆する。

**周縁知の保存と対抗策**:Yuらの研究(2026)は、既製の生成モデルが文化的バイアスを持ち西洋中心のデータを過大に代表するため、真正性に欠ける出力になると指摘する。湘繍(Xiang Embroidery)と長沙窯陶磁を対象に、118名の設計学生で12週間の準実験を行い、マルチモーダルLLMによるタグ付けやLoRAファインチューニングを含むカスタムパイプラインを価値感応設計(VSD)と組み合わせた。ただしこの研究の主眼は問題の機構の解明より手法的な対抗策にある。

**先住民コミュニティにおける防御**:Zelfiaらのカジャン先住民コミュニティの研究(2026)は、デジタルメディアが地域に根ざした意味をアルゴリズムによる単純化や文化的商品化にさらす一方、アドボカシーの機会も生むと述べる。Pasang ri Kajangがコミュニケーション・アイデンティティ・環境保全を結ぶ点に着目し、語りの主権とアイデンティティのレジリエンスを維持する営みを分析している。

**推薦システムの透明性**:Muslimin(2026)は、インドネシアの大学生1,200人への調査などを通じて、デジタルリテラシー(アルゴリズム認識と情報源の批判的評価)が宗教的穏健性を予測し、それが社会的結束を予測するという媒介モデルを検証した。本記事の整理では、推薦システムの認識論的透明性は、マイノリティの認識論が構造的に周縁化されるのを防ぐ必要条件とされる。

**解釈実践のデジタル化**:Munirの体系的レビュー(2026、25本の論文)は、クルアーン解釈のデジタル化がアクセス性・解釈の多様性・革新を高める一方、権威、正確性、文脈化、アルゴリズムバイアスの問題を生むと報告する。多様性を促進する面と同質化の危険が同居する点は、圧縮が一方向の単純な過程ではないことを示す。

## AI Nativeな設計への示唆

以下はソースの知見から導かれる設計上の指針である(一部は本記事の整理による推論を含む)。

1. **分布の代表性を設計対象にする**:訓練データの構成を、性能だけでなく認識論的な代表性の観点で監査する。既製モデルの偏りを前提とし、地域的・文化的データによる調整(LoRAなど)を選択肢に含める。
2. **プロンプトによる補正への過信を避ける**:Midjourneyの事例では専門的制約が逆効果になり得た。出力段階の補正だけでなく、データと学習段階での対処が必要である。
3. **推薦・生成の透明性を確保する**:どの視点が標準として扱われているかを利用者が把握できるようにし、アルゴリズム認識を育てる教育と組み合わせる。
4. **価値感応設計を組み込む**:周縁知を持つ当事者の価値を、設計プロセスの初期から取り込む。
5. **語りの主権を支える**:知の担い手自身がデジタル空間での表現と意味の解釈を管理できる形を支援する。
6. **教育で複数の知的系譜を扱う**:標準的な体系だけでなく、多様な学問的遺産を並置し、ヘゲモニーそのものを批判的に検討できるようにする。
7. **技術以前の権力構造も見る**:同質化は技術だけの問題ではないため、制度・教育・評価の設計と一体で対処する。

## 関連コンセプト

- [[epistemic-pluralism-and-non-closure-of-knowledge-space]] — 知識空間を閉じず多元性を保つという、本原理への対抗軸
- [[assistance-mediated-capability-erosion-and-homogenization]] — 支援による画一化という関連する同質化の経路
- [[external-center-absorption-of-meaning-autonomy]] — 外部中心による意味自律性の吸収
- [[epistemic-authority-and-algorithmic-truth]] — アルゴリズムが権威を帯びる過程
- [[distributed-epistemic-commons-and-identity-separation]] — 分散的な知のコモンズによる代替構造
- [[epistemic-risk-llm-higher-education]] — 高等教育におけるLLMの認識論的リスク
- [[mediated-authority-transfer-and-function-invariance]] — 媒体が変わっても権威の機能は保たれる点で共通
- [[architecture-as-power-distribution-and-interface-standards]] — 設計による権力配分

## 参考ソース

1. From objective reason to instrumental rationality: a global systematic review of epistemological challenges in AI development — Mohamad Anas, M. Alifudin Ikhsan, M. Lukman Hakim (2026)
   File: raw/papers/religious_studies/from-objective-reason-to-instrumental-rationality-a-global-systematic-review-of-.md
2. Knowledge hegemony and epistemic reclamation in Central Asian higher education: a community case study of Eastern scholastic heritage integration, sociological field dynamics, and the conditions for decolonizing economic reasoning across STEM and social science disciplines in Uzbekistan — Gulinoz Ruziyeva, Temir Olimov, Nargiza Khamroyeva, Salomat Ramazonova, Shokhida Ruziyeva (2026)
   File: raw/papers/religious_studies/knowledge-hegemony-and-epistemic-reclamation-in-central-asian-higher-education-a.md
3. Visual Representation of "Chinoiserie" in Western AI Image Models: A Case Study of Midjourney — Shurong Wang (2026)
   File: raw/papers/religious_studies/visual-representation-of-chinoiserie-in-western-ai-image-models-a-case-study-of-.md
4. Enhancing heritage-oriented design learning through a value-sensitive approach to generative AI in higher education aesthetic pedagogy — Tingting Yu, Yixin Li (2026)
   File: raw/papers/religious_studies/enhancing-heritage-oriented-design-learning-through-a-value-sensitive-approach-t.md
5. Media Transformation and Environmental Communication Resilience in the Kajang Indigenous Community — Zelfia Zelfia, Faathiyah Faathiyah, Ahdan S, Tawakkal Baharuddin (2026)
   File: raw/papers/religious_studies/media-transformation-and-environmental-communication-resilience-in-the-kajang-in.md
6. Religious Moderation, Digital Literacy in Social Cohesion Interaction among the University Students in Indonesia — Abdul Azis Muslimin (2026)
   File: raw/papers/religious_studies/religious-moderation-digital-literacy-in-social-cohesion-interaction-among-the-u.md
7. Digital Transformation of Quranic Interpretation in the Contemporary Era — Ahmad Munir (2026)
   File: raw/papers/religious_studies/digital-transformation-of-quranic-interpretation-in-the-contemporary-era.md
