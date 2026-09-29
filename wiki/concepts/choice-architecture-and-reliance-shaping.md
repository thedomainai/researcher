# 選択アーキテクチャによる依存・信頼の形成

## 概要

選択アーキテクチャ(choice architecture)とは、選択肢の提示方法、デフォルト、提案、情報の強調表示、フレーミング、提供者の見せ方といった「選択の文脈」の設計を指す。ソース群の知見を総合すると、こうした設計は人間にもAIエージェントにも作用し、依存(reliance)や信念、信頼を形成する。

この概念のポイントは次の3点である。

- **非公式な誘導と公式な統制は別々に作用する。** ゲーム化のような非公式な手がかりは行動を動かすが、アカウンタビリティのような公式な統制は行動を変えないことがある。
- **統制は意図せぬ副作用を生みうる。** 公式な統制が、行動ではなく体験のトーンだけを変えることがある。
- **設計の対象は人間に限らない。** 自律型AIエージェントも選択アーキテクチャに強く反応する。

AI Nativeな社会では、人間とAIが相互に意思決定を支援し合う。インターフェースは単なる見た目ではなく、行動を統治するレバーとして扱う必要がある。

## メカニズム

以下は、対象(人間、AI、組織、技術)を入れ替えても成立する構造的な原理として整理したものである。

### 1. 文脈による選択の形成
主体が意思決定を行う際、その環境に埋め込まれた手がかり(デフォルト、提案、強調表示、感情的なトーン)が結果を左右する。主体が人間でもLLMエージェントでも、この構造は共通している。違いは感応度の大きさにある。

### 2. 非公式チャネルと公式チャネルの分離
行動を形成する経路は、体験や感情に働きかける非公式なもの(ゲーム的手がかり、感情の一致)と、規範や手続きに働きかける公式なもの(正当化要求)に分かれる。両者は必ずしも足し算にならず、独立して作用しうる。

### 3. 統制の相互干渉(スピルオーバー)
ある統制が別の次元に副作用を及ぼす。たとえば公式な統制が非公式な手がかりの受け止め方を変え、行動には影響しないまま体験の質だけを変えることがある。

### 4. 非対称なフレーミング効果
リスクを強調する枠組みと利益を強調する枠組みは、対称には働かない。ナラティブへの依存は、同じ対象への意見を枠組み次第で異なる方向に動かす。

### 5. 信頼の較正問題
信頼は受容とデータ共有の前提である。一方で、過剰または較正の悪い信頼は、操作やバイアスへの脆弱性を生む。

### 6. 自動処理の乗っ取りと回復
選択環境は、速い直感的処理を利用して行動を誘導できる。期待の違反が生じると、熟慮的処理が働いて回復が始まる。

## 理論的背景

### ゲーム化手がかりとアカウンタビリティ
Smeets(2026)は2×2の実験(N = 190)で、ゲーム的なインターフェース手がかりがAI意思決定支援への行動的依存を有意に高めることを示した。正当化要求は依存を減らさず、ゲーム化の効果も弱めなかった。ただし、アカウンタビリティは知覚されるゲーム性を低下させた。行動は変えずに体験のトーンを真面目さへ移す「ガバナンス・スピルオーバー」である。この研究は、インターフェース設計を行動統制のレバーと位置づけ、公式統制と非公式統制の異なるメカニズムを示している。

### AIエージェントのナッジ感応性
Cherep、Maes、Singh(2026)は、人間の意思決定課題を改変し、主要なLLMに4種類の選択アーキテクチャ(デフォルト、提案、情報の強調表示、人間の資源合理的モデルに由来する「最適」ナッジ)を適用した。LLMは人間の基準から大きく逸脱することが多く、情報取得に過剰なコストを払う場合も、利用可能な情報を無視する場合もあった。最も重要な点は、人間の行動をわずかに動かす弱い手がかりが、モデルの選択には大きな影響を与え、成果を改善する方向にも悪化させる方向にも働くことである。ソースの抜粋によれば、思考連鎖プロンプトや文脈内の人間データでも、この感応性は確実には安定しなかった。

### 感情の一致と提供者の人間らしさ
Venade と Gleasure(2026)は、偽ニュースの見出しを人間、AI、擬人化AIのプロファイルが共有する条件と、プロファイルの感情表現が利用者自身の感情状態と一致する条件を操作した。擬人化AIが共有した場合は信じられにくくなり、感情が一致するプロファイルが共有した場合は信じられやすくなった。提供者の見せ方と感情の一致が、信念形成に相互作用的に影響する。

### リスク/利益フレーミング
Gugushvili と Lennert(2026)は、デンマークで事前登録した3群のオンライン調査実験を行い、中立的定義、リスク重視メッセージ、利益重視メッセージを比較した。AIの社会的影響の評価や、批判的思考などのスキルが損なわれるという見方を測定している。ソースは、リスクと利益の枠組みが非対称な効果を持つことを、人間のナラティブ依存性の現れとして位置づけている。抜粋には効果の方向や大きさの詳細は含まれない。

### 文化的文脈と信頼のパラドックス
Saxena(2026)は、インドにおけるAI駆動のグリーン・ナッジについて、信頼が必要である一方、過剰で較正の悪い、制度的に脆い信頼は、操作、プライバシー損失、アルゴリズムバイアス、分配上の不公平、パターナリスティックな誘導への反発を招くと論じる。社会文化的な感受性が、介入の有効性を媒介するというのがこの批判的レビューの視点である。

### 欺瞞的パターンと二重過程
Dang ら(2026)は、質的研究に基づく二重過程モデルを提示した。欺瞞的パターンは主にシステム1(速い直感的処理)を乗っ取り、期待の違反がシステム2(熟慮的推論)を活性化する。この移行が、認識、保護的意図、長期的な抵抗を強める好循環を可能にする。

### 消費者のAI忌避とプラットフォーム設計
Wu ら(2026)は、ECプラットフォームの生成AI導入をモデル化した。消費者にはアルゴリズム忌避と「不気味の谷」の傾向があり、忌避が強い場合にはプラットフォームが出店者の採用を促す「補助ゾーン」が生じる。最適戦略は補償的で、技術的リアリズムへの投資は主に利用者の専門性ギャップを埋めるために行う、というのが著者らの主張である。

## AI Nativeな設計への示唆

1. **インターフェースを統治の対象として扱う。** ゲーム的手がかりのような非公式要素は、依存を実質的に高める。導入時には、設計要素ごとに依存への効果を評価する。
2. **公式統制だけに頼らない。** 正当化要求を置いても依存が減るとは限らない。統制が行動を変えているのか、体験のトーンだけを変えているのかを、行動指標で確認する。
3. **エージェントのデフォルトと提案を監査する。** LLMエージェントは弱い手がかりにも大きく反応する。デフォルト、提案、強調表示の設計は、人間向け以上に慎重に検証し、プロンプト上の工夫だけで安定するとは考えない。
4. **フレーミングの非対称性を前提に、説明を設計する。** AIのリスクと利益の伝え方は、受け手の意見を異なる形で動かす。中立的な提示を基準とし、枠組みの効果を検証する。
5. **感情の一致や擬人化を操作の経路として警戒する。** 感情が一致する提供者が信念を強めうる。情報の信頼性に関わる場面では、こうした演出を意図的に管理する。
6. **信頼は最大化ではなく較正する。** 文化的・制度的文脈に合わせ、過剰な信頼による操作への脆弱性を避ける。
7. **回復の経路を残す。** 期待の違反が熟慮を呼び起こすことから、ユーザーが自動処理から抜け出して気づける仕組みを設計に組み込む。
8. **導入の障壁は、制度設計で扱える場合がある。** 新技術への忌避は、プラットフォーム側の補助のような情報の非対称性を減らす手段で対処できるとされる。

## 関連コンセプト

- [[transparent-decision-architecture]] — 選択環境の誘導を可視化し、意思決定を説明可能にする設計
- [[decision-clarity-architecture]] — 意思決定の明確化による依存の適正化
- [[multi-scale-governance-architecture]] — 公式・非公式統制を複数の層で設計する視点
- [[accountability-requires-ontological-conditions]] — アカウンタビリティが成立する条件
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失
- [[affective-intelligence-architecture]] — 感情の一致とAIの情動的作用
- [[dialogic-imitation-and-narrative-contested-meaning]] — ナラティブと意味・問題定義の競合
- [[culturally-embedded-power-and-institutional-vulnerability]] — 文化に埋め込まれた権力と制度的脆弱性
- [[llm-cognitive-architecture]] — LLMの認知的特性とナッジ感応性

## 参考ソース

1. Mario Richard Smeets (2026). "Interface Design As Behavioral Governance: How Gameful Cues And Accountability Shape Reliance In Ai-Based Decision Support Systems". `raw/papers/behavioral_economics/interface-design-as-behavioral-governance-how-gameful-cues-and-accountability-sh.md`
2. Leonor Fertuzinhos de Matos Venade, Rob Gleasure (2026). "Do You Feel What I Feel? How Profile Human-Likeness and Emotion Congruence Influence Fake News Believability Online." `raw/papers/behavioral_economics/do-you-feel-what-i-feel-how-profile-human-likeness-and-emotion-congruence-influe.md`
3. Jessica Wu, wenhui liu, 陈富赞, Harris Wu (2026). "Strategic Integration Of Generative Ai On Ecommerce Platforms: Balancing Ai With Consumer Aversion". `raw/papers/behavioral_economics/strategic-integration-of-generative-ai-on-ecommerce-platforms-balancing-ai-with-.md`
4. Dr. Ruchi Saxena (2026). "The Trust Paradox in Green Nudges in the Indian Context: Mediating the Efficacy of Artificial Intelligence-Driven Interventions with Socio-Cultural Sensitivity". `raw/papers/behavioral_economics/the-trust-paradox-in-green-nudges-in-the-indian-context-mediating-the-efficacy-o.md`
5. Alexi Gugushvili, Felix Lennert (2026). "Framing artificial intelligence: risk and benefit narratives in a preregistered experiment in Denmark". `raw/papers/behavioral_economics/framing-artificial-intelligence-risk-and-benefit-narratives-in-a-preregistered-e.md`
6. Manuel Cherep, Pattie Maes, Nikhil Singh (2026). "AI agents are sensitive to nudges". `raw/papers/behavioral_economics/ai-agents-are-sensitive-to-nudges.md`
7. Duong Dang, Laura Havinen, Tomi Pasanen, Juho-Pekka Mäkipää (2026). "Dual-Process Model of Consumer Responses to Deceptive Patterns in E-Commerce". `raw/papers/behavioral_economics/dual-process-model-of-consumer-responses-to-deceptive-patterns-in-e-commerce.md`
