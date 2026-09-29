# 回避と過信の間の依存度キャリブレーション

## 概要

支援システムに対する信頼は、低すぎる状態(回避)と高すぎる状態(過信)の両極の間で較正される必要がある。ここでいう較正とは、システムの実際の信頼性に見合う水準へ依存度を合わせることである。ソース群によれば、この較正は単一の要因では決まらない。情報の提示形式、利用者による多面的な理解、個人特性、そして利用者が抱く脅威評価が相互作用して決まる。

生成AIが意思決定に組み込まれる状況では、この問題が特に重要になる。出力の質だけでなく、人間がそれにどう反応するかが価値を左右するからである。有用な助言が誤りを一度見ただけで拒絶されることもあれば、流暢で自信に満ちた出力が、不完全・偏り・誤りを含んでいても信用されてしまうこともある[5]。AI Nativeな設計では、「信頼を高める」ことを目標にするのではなく、「信頼を適切な水準に合わせる」ことを目標に置く必要がある。

## メカニズム

以下の構造は、対象が個人、組織、AIエージェント、技術のいずれであっても成り立つ原理として整理できる。

1. **両極の失敗モード**:支援を過小評価して拒否する失敗(アルゴリズム回避)と、過大評価して検証を放棄する失敗(自動化バイアス、過度依存)が、同じ較正問題の両端として存在する[5][8]。
2. **信頼の多次元性**:信頼は不可分な多次元現象であり、パフォーマンス、透明性、信頼性などの側面から構成される[2]。一つの側面だけを高めても全体の較正は保証されない。
3. **提示形式と個人特性の相互作用**:支援の提示形式は認知に影響し、異なる依存戦略を生む。その効果は個人の認知と相互作用する[7]。同じ形式でも、人によって依存の帰結が異なる。
4. **内的特性による応答性の差**:AI入力後に判断を修正するかどうかは、特性マインドフルネスと創造的自己効力感の交互作用などによって変わる[3]。
5. **脅威評価の介在**:技術不安、プライバシー懸念、自律喪失、認知されたリスクなどの脅威評価が、信頼低下を駆動する[4]。
6. **多面的理解による較正**:複数の表現様式を統合した理解が、複雑なシステムに対する信頼形成の本質的なメカニズムとなる[1]。ブラックボックスのままでは較正された信頼を形成できない[1]。

## 理論的背景

- **アルゴリズム回避と評価の緊張**:アルゴリズムの誤りを観察した後に有用な助言を拒否する回避研究と、アルゴリズムの助言に人間の助言以上に依存するという「アルゴリズム評価」研究の間には見かけ上の緊張がある。近年の研究はさらに、GenAIへの過度依存という逆方向の懸念を提起している。[5]はこれらを統合し、依存の較正として位置づける。
- **回避の文化的異質性**:回避の総量は文化間で差がなくても、その機構は異なる。個人主義文化では、アルゴリズムは個人の事情を考慮できないという「独自性の無視」が主因であり、集団主義文化では技術への親近性がより強く影響する[6]。回避への介入は機構に合わせて設計する必要がある。
- **信頼概念の素人理解**:英語話者204名の自由記述の内容分析では3つの中核テーマが抽出され、最も多く言及されたのはパフォーマンス(85%)で、正確性や情報源の質などとして信頼が定義された[2]。
- **認知バイアスと透明性**:セキュリティ運用センター(SOC)におけるAI支援の理論研究は、自動化バイアス、アルゴリズム回避、確認バイアスを取り上げ、説明・裏付け証拠・不確実性の伝達の役割を論じている[8]。
- **選択アーキテクチャ**:ナッジ理論に着想を得て、AI支援の各形式を「選択アーキテクチャ」と捉え、文脈付きマルチアームドバンディットで個人ごとに最も有効な形式を適応的に選ぶ枠組みが提案されている。目的は、より適切にAIへ依存するよう促すことである[7]。
- **教育的枠組み**:ICE-Tは、ブルーナーの行為的・映像的・記号的表現の間の転移、Use-Modify-Createによる計算論的思考、説明的思考の3側面を統合する枠組みで、これらが信頼較正の文献が求める認知的機構を提供すると論じる[1]。
- **情報処理段階と意思決定の質**:高齢者の生成AI健康相談の研究では、知的情報を注意・知覚・識別・信頼・依存の5段階に分けて意思決定の質への経路を分析している[10]。

## AI Nativeな設計への示唆

- **依存度を測定対象にする**:満足度や利用率だけでなく、AI出力の正誤に応じて依存が適切に変化しているかを評価指標にする。
- **提示形式を固定しない**:個人の反応に応じて支援形式を適応させ、過小・過大の両方向の依存を是正する設計を検討する[7]。
- **信頼の各次元に個別に働きかける**:性能情報、透明性、信頼性を切り分けて提示し、単一のスコアに畳み込まない[2]。
- **不確実性と根拠を出力に添える**:説明、裏付け証拠、不確実性の伝達によって、自動化バイアスと確認バイアスの歪みを抑える[8]。
- **流暢さを信頼の根拠にさせない**:自信に満ちた出力ほど検証の契機を明示的に設ける[5]。
- **回避の機構に合わせて介入する**:独自性の無視が主因なら個別事情の反映を示し、親近性が主因なら体験機会を提供するなど、文化や文脈で対応を変える[6]。
- **脅威評価に配慮する**:開示、データ利用の透明性、人間による監督といった手がかりを、不安・プライバシー懸念・自律喪失感を和らげる刺激として設計する[4]。
- **理解形成の機会を用意する**:ブラックボックスを避け、複数の表現様式で仕組みに触れられる学習経路を提供する[1]。

## 関連コンセプト

- [[trust-calibration-mechanisms]]
- [[algorithm-aversion]]
- [[algorithm-aversion-and-transparency-in-healthcare]]
- [[choice-architecture-and-reliance-shaping]]
- [[fluency-induced-trust-miscalibration]]
- [[human-ai-trust]]
- [[human-ai-interaction-and-trust]]
- [[human-ai-trust-complementarity]]
- [[ai-ethics-trust-transparency]]
- [[epistemic-friction-and-sycophancy-erosion]]
- [[finite-cognitive-resources-and-load-thresholds]]

## 参考ソース

1. Pierre Haritz, Hendrik Krone, Thomas Liebig (2026)「Addressing Trust in AI Systems through Education: A Didactic Perspective」 — `raw/papers/behavioral_economics/addressing-trust-in-ai-systems-through-education-a-didactic-perspective.md`
2. Sandrine Toudjui ほか (2026)「Identifying conceptual dimensions of trust in artificial intelligence from qualitative content analysis of open-ended responses」 — `raw/papers/behavioral_economics/identifying-conceptual-dimensions-of-trust-in-artificial-intelligence-from-quali.md`
3. Deeviya Francis Xavier, Zoe Hughes, Christian Korunka (2026)「Mindfulness, creative self-efficacy, and communal-agentic orientation in human–AI decision-making with implications for adaptive AI design」 — `raw/papers/behavioral_economics/mindfulness-creative-self-efficacy-and-communal-agentic-orientation-in-humanai-d.md`
4. Tran Duong Minh Chuyen (2026)「Technology Anxiety and Brand Trust: Consumer Responses to Generative-AI Advertising」 — `raw/papers/behavioral_economics/technology-anxiety-and-brand-trust-consumer-responses-to-generative-ai-advertisi.md`
5. Sergey Kutukoff (2026)「When Should Managers Trust Generative AI? Calibrating Human Reliance from Algorithm Aversion to Over-Reliance」 — `raw/papers/behavioral_economics/when-should-managers-trust-generative-ai-calibrating-human-reliance-from-algorit.md`
6. Nicole Liu (2026)「Behavioural Decision-Making in the Age of AI: Minds vs. Models」 — `raw/papers/behavioral_economics/behavioural-decision-making-in-the-age-of-ai-minds-vs-models.md`
7. Zhuoyan Li ほか (2026)「Adaptive Selection of Effective AI Assistance in AI-assisted Decision Making Using Multi-Armed Bandits」 — `raw/papers/behavioral_economics/adaptive-selection-of-effective-ai-assistance-in-ai-assisted-decision-making-usi.md`
8. Dolantina Hyka ほか (2026)「Human–AI Interaction in Cybersecurity: A Theoretical Study on Cognitive Bias and Decision Reliability」 — `raw/papers/behavioral_economics/humanai-interaction-in-cybersecurity-a-theoretical-study-on-cognitive-bias-and-d.md`
10. Haibei Chen, Zhengyuan Qian, Xianglian Zhao (2026)「Empowerment or disempowerment? How generative AI consultation shapes the health decision-making among the new generation of older adults」 — `raw/papers/behavioral_economics/empowerment-or-disempowerment-how-generative-ai-consultation-shapes-the-health-d.md`
