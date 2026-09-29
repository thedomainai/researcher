# 支援代替による能力形成機会の喪失ループ

## 概要

支援代替による能力形成機会の喪失ループ(Support-Induced Skill Substitution Loop)とは、強力な支援手段が「反復」「試行錯誤」「他者への援助要請」といった能力形成の機会を代替してしまい、表面的な成果の向上と、深層的な能力・対人的つながりの低下が同時に進行する構造を指す。Tier 1(不変原理)に位置づけられる概念である。

重要なのは、これが「支援は有害」という主張ではない点である。ソース群は、相互作用の設計次第で学習機会が保存されうることも示している。AI Nativeな社会設計では、AIの能力が上がるほど人間側の学習機会が「自動的に」削られるリスクがある。そのため、成果指標だけでなく、能力形成と関係性の維持を設計対象に含める必要がある。

## メカニズム

この構造は、対象(人間、AI、組織、技術)を入れ替えても成立する。「支援する側」が「支援される側」の練習機会を肩代わりすると、支援される側の能力形成が止まる、という一般的な形で整理できる。

1. **練習機会の代替(スキャフォルディングの欠落)**
   支援手段がタスクの遂行そのものを担うと、支援される側が反復し、失敗し、修正する機会が失われる。段階的に支えを外す足場かけが設計されていなければ、能力は育たないまま成果だけが得られる。

2. **認知負荷の低減による援助要請の回避**
   外部の支援が認知負荷を下げると、他者(同僚、教員など)に助けを求める動機が弱まる。その結果、対人的な相互作用の機会が減り、関係性を通じた学習や接続も細る。

3. **成果と深層認知の解離**
   支援によって成果物や即時の成績は向上しても、その基盤となる認知的活動は減りうる。成果を測るだけでは、能力の低下が見えなくなる。

4. **ループ化**
   能力が育たないほど支援への依存が強まり、さらに練習機会が代替される。この自己強化が「ループ」の本質である。

一方で、支援との相互作用が学習を促す形(問いを返す、批判的に対話する、ユーザー主導で構造化に使う)であれば、同じ支援手段でも機会は保存される。分岐点は支援の能力ではなく、相互作用の設計にある。

## 理論的背景

**援助要請回避モデル(ソース1)**
社会認知理論に立ち、学生と生成AIの相互作用が、援助要請の回避を介して仲間や教員との関わりを減らすと提案する。認知負荷理論を組み込み、課題の複雑さがこの関係を強めると位置づけ、性格特性を調整要因として扱う。大学生への調査データで検証する研究設計であり、過度なGenAI利用の社会的含意を明らかにすることを目指している。

**依存のジレンマ(ソース2)**
組織で導入が進むML意思決定支援について、新しい実験デザインにより因果効果を識別した研究である。予測作成タスクでMLの予測に依拠すると、重要な意思決定スキルの発達が妨げられうることが示されている。反復練習と適応的フィードバックの機会が奪われることが構造的な理由とされる。

**日常的LLM対話における非公式な学習(ソース3)**
128,569件の自然な人間−LLM対話を分析し、学習科学の構成概念をターン単位の行動シグネチャに変換した。ユーザーの491,685ターンのうち、認知的関与(ユーザーの認知的努力が表れる交換)は31.9%、最も深い形の建設的関与は4.9%に現れた。深い意味構築は繰り返し起こるが選択的である、というのが著者らの読みである。ソースの要旨は、スキャフォルディングされたアシスタントの支援などが関与の度合いと関連することを示唆しており、学習機会の活用が相互作用の設計や対話パターンに左右されることを示す。

**批判的思考のパラドックス(ソース4)**
GenAIが即時のパフォーマンスを高める一方、耐久的な学習に必要な認知活動を減らしうる、という一見矛盾した知見(成果物の向上と、認知的関与低下を示す質的・神経科学的・行動的兆候)を「批判的思考のパラドックス」と呼ぶ。ただし著者ら自身、課題・集団・ツールによる異質性も反映しうるとし、この収斂は事実ではなく検証可能な解釈だと位置づけている。

**補完的な知見(ソース5〜7、Tier 2)**
- ソース5:生成AIを組み込んだ知識労働では、どう使うかが使うか否かと同程度に重要だと論じる。Deep Structure Usage(AIの生成的仕組みにユーザー主導で関与し情報を整理・統合する使い方)を、情報過負荷への能動的な対処戦略として提案する。法律専門職を対象とするランダム化オンライン実験を提案する研究である。
- ソース6:会話記録から認知負荷とメタ認知を推定する時間的ネットワーク分析の枠組みを提示し、AI媒介の会話における学習と適応の動態をモデル化する。
- ソース7:建築設計スタジオで、AIの役割が異なる3群(AIを最後のレンダリングにのみ使う群、生成ツールとして直接使う群、AIとの構造化された批判的対話を行う群)を比較し、AIとの「スパーリング」という対話的モデルを検討する。

## AI Nativeな設計への示唆

- **成果指標と能力指標を分けて測る**:成果物の質だけでなく、支援なしでの遂行力や認知的関与を評価に含める。
- **スキャフォルディングを標準機能にする**:答えを直接返すだけでなく、ヒントや問い返し、段階的な支援の後退を設計する。
- **批判的対話型のインタラクションを既定にする**:ソース7のような対話的な使い方や、ソース5のユーザー主導の構造化利用のように、人間の思考を引き出す関与を促す。
- **人への援助要請の経路を保つ**:AIが認知負荷を下げても、同僚や教員への相談や協働が自然に残るワークフローを設計する。
- **課題特性に応じて支援の強さを調整する**:課題の複雑さが回避を強めうるため、複雑な課題ほど人との接続を意図的に組み込む。
- **異質性を前提に運用する**:効果は課題・集団・ツールで異なりうるため、一律の禁止や解放ではなく、観測と調整を続ける。

## 関連コンセプト

- [[ai-decision-support-systems]] — 意思決定支援への依存がスキル発達に与える影響の文脈
- [[ai-decision-support-in-education]] — 教育場面での意思決定支援AI
- [[ai-in-educational-support-systems]] — 教育支援システムにおけるAIの位置づけ
- fluency-induced-trust-miscalribration は使わず、正しくは [[fluency-induced-trust-miscalibration]] — 流暢な出力が信頼や検証行動に与える影響
- [[effort-opacity-and-disclosure-signal-erosion]] — 努力の不可視化と評価シグナルの劣化
- [[interaction-loop-grounded-knowledge-and-relational-bond]] — 相互作用を通じた知識生成と関係性
- [[platform-embedded-ai-and-skill-diversity]] — 組み込み型生成AIとスキル多様性
- [[skill-biased-technological-change]] — 技術変化とスキルの関係
- [[stress-appraisal-and-coping-theory]] — 対処・社会的支援の理論

## 参考ソース

1. When GenAI Usage Backfires: A Help-Seeking Avoidance Model of Student Engagement — Md Rafiqul Islam, Minhaz Ahmed, Qinyu Liao (2026)
   `raw/papers/cognitive_science/when-genai-usage-backfires-a-help-seeking-avoidance-model-of-student-engagement.md`
2. The Dependency Dilemma: How Machine Learning Decision Aids can Undermine Skill Growth — Kevin Bauer, Michael Nofer, Benjamin Henrich, Hendrik Drachsler, Hinz (2026)
   `raw/papers/cognitive_science/the-dependency-dilemma-how-machine-learning-decision-aids-can-undermine-skill-gr.md`
3. Informal Learning Emerges in Everyday Human-LLM Interaction — Zixin Chen, Haotian Li, Ziang Xiao, Huamin Qu, Xing Xie (2026)
   `raw/papers/cognitive_science/informal-learning-emerges-in-everyday-human-llm-interaction.md`
4. The critical-thinking paradox in generative AI-integrated learning: distinguishing efficiency from cognitive depth—a differentiated framework and testable propositions — Jiayin Lin, Naif Mohammed Al-Hada (2026)
   `raw/papers/cognitive_science/the-critical-thinking-paradox-in-generative-ai-integrated-learning-distinguishin.md`
5. Does Deep Structure Usage Impact Information Overload? — Philippe Aussu, Saïd Assar (2026)
   `raw/papers/cognitive_science/does-deep-structure-usage-impact-information-overload.md`
6. Temporal network analysis of cognitive load and meta-cognition dynamics in human-AI conversations — Christophe Cruz, Samir Jabbar, Hussam Ghanem, Maria Alice Bertolim, Hocine Cherifi (2026)
   `raw/papers/cognitive_science/temporal-network-analysis-of-cognitive-load-and-meta-cognition-dynamics-in-human.md`
7. Dialogic Artificial Intelligence in the Architectural Design Studio: An Empirical Study of the AI Sparring Model — Mirko Stanimirović, Jiaqi Wang, Domen Zupančič, Ana Momčilović-Petronijević, Ivan Ćirić (2026)
   `raw/papers/cognitive_science/dialogic-artificial-intelligence-in-the-architectural-design-studio-an-empirical.md`
