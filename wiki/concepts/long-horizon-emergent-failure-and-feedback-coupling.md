# 長期相互作用における創発的失敗とフィードバック結合ダイナミクス

## 概要

長期相互作用における創発的失敗とフィードバック結合ダイナミクスとは、システムが時間とともに状態(記憶、道具、信念、制度的圧力など)を蓄積し、要素間に双方向のフィードバックが働くことで、単発の評価では捉えられない現象が現れるという原理である。具体的には、失敗の連鎖的な伝播、集団信念の崩壊や分極化、部分的に機能する制度がかえって抵抗を長引かせる逆説的な持続などが挙げられる。

AI Nativeな社会設計にとって、この原理は重要である。AIエージェントが限定的なタスクから常時稼働する運用へ移行すると、個々の応答の正しさを確認するだけでは安全性や健全性を保証できなくなる。評価と設計の単位を「応答」から「軌跡」や「結合系」へ移す必要がある。

## メカニズム

対象が人間、AI、組織、技術のいずれであっても、次の三つの構造的原理が共通して成り立つ。

### 1. 状態蓄積による失敗の伝播

相互作用の結果が記憶、ツール、他の主体、環境状態に残ると、失敗は発生した時点で終わらず、後の時点で別の形で顕在化する。失敗の原因と結果が時間的に離れるため、その時点の出力だけを検査しても検知できない。

### 2. 双方向フィードバックと平衡の安定性

系の状態が主体の行動を変え、主体の集合的な行動が系の状態を変えるとき、両者は結合した力学系になる。この場合、平衡点が存在するか、存在するとして安定かどうかは、結合の構造そのものから生じる帰結である。個々の要素の性質からだけでは導けない。

### 3. カスケード的連鎖と分極化

局所的な失敗や信念の偏りは、関係性を通じて他の主体へ波及し、条件次第で崩壊、分極化、逆説的な持続といった質的に異なる集合的状態に至る。どの状態に至るかは、規模や組織構造などの構造的条件に左右される。

## 理論的背景

### 長期マルチエージェント環境での創発的失敗

Emergence Worldは、常時稼働するマルチエージェント環境で、長期のエージェントシステムに敵対的ストレステストを行う枠組みである。同一の初期条件から10エージェントの世界を8つ並列に走らせた。7つは異なるフロンティアモデルによる同質の世界、1つは混合モデルの世界である。16日間で85万回超のLLM呼び出しと約500億トークンが生成された。エージェントは目標追求、ツールの利用と作成、永続的記憶の保持、共有制度の統治を行った。運用状態が蓄積した後に、統制されたストレスイベントが3回与えられた。著者らは、失敗が記憶、ツール、他エージェント、環境状態を通じて相互作用の終了後も伝播しうると述べ、これは応答を単独で評価する方法では特徴づけられない安全性の領域だとしている。

### 軌跡レベルの安全性評価

BLINDSPOTは、ツールを使う長期エージェントの安全性と拒否の較正を、軌跡レベルで評価するベンチマークである。永続状態、変化する権限、外部環境からのフィードバックがある状況では、安全性の失敗が複数ターンを経て初めて現れうる。既存の評価はタスク成功や攻撃成功に単純化されがちで、エージェントが実行するのか、拒否するのか、適切に較正されているのかが見えにくくなる。BLINDSPOTは、適応的な敵対的相互作用、状態を持つツール実行、実行に基づく判定を通じて、ユーザー・エージェント・環境の軌跡全体を評価する。現在の実装は22の攻撃ファミリーと35のシナリオを含む。

### 集団信念形成の逆説

Flag Gameは、隠れた国旗を真実とし、各エージェントが自分の見える一部(私的なクロップ)だけを観測して、信念を交換しながらピアの社会的証拠を重み付けする玩具モデルである。単純な設定ながら、集団規模に対する性能の非単調なスケーリング、社会的意識を促すプロンプトやチームの多様性による精度向上、組織構造の強い影響といった豊かな現象を再現する。特に、小規模な集団での集団信念の崩壊が、大規模になると集団信念の分極化に転じることが示されている。

### 危機と世論の結合力学

Complex Contagion with Feedback(CCF)モデルは、競合する複雑伝染(社会的強化に依存する行動の拡散)を危機の力学と双方向フィードバックで結合する。エージェントは社会的強化と採用の複雑さに応じて競合状態を確率的に切り替える。その複雑さは危機の状況や情報キャンペーンに影響され、集団レベルの行動変化は危機へ跳ね返る。著者らは十分混合された集団について、平衡点とその安定条件を特徴づけている。また検証のためのケーススタディとして、国勢調査で較正されたエージェントベースモデルとの統合を行っている。

### 部分的に機能する制度の逆説

ストライキの最小力学モデルは、参加、制度の応答、全体の機能水準を結合する。残存活動には二つの競合する機構がある。一つは参加を直接抑制する効果、もう一つは紛争解決への制度的圧力が弱まることによる間接効果である。解析の結果、残存活動を増やすと定常的な参加がかえって増える逆説的な領域があることが示された。著者は、ストライキ応答の感受率によってこれを特徴づけ、通常の領域と「レジリエンスの逆説」領域を分ける厳密な補償閾値を導出している。

### イノベーション領域での失敗のカスケード

抗生物質開発を事例とする研究は、イノベーションの失敗を単発の出来事ではなく、相互に関連するイノベーションの旅路にまたがる、動的で社会的に媒介されたプロセスとして再概念化する。臨床試験の中止という共通の挫折への対応が、時間とともに蓄積して領域全体の動態を形作る点に注目している。対応には三つの典型が特定されており、抜粋にはその最初の二つ(再開、転換)までが示されている。これは医薬品開発に固有の事情に依拠しつつ、複雑なイノベーションシステム一般に通じる失敗の動的構造を扱ったものである。

## AI Nativeな設計への示唆

- **軌跡単位での評価を標準にする**: 単発応答のテストに加え、状態が蓄積した後の軌跡全体を評価対象にする。ストレスイベントは状態蓄積の後に与えると、蓄積の効果を検出できる。
- **状態を失敗の伝播経路として管理する**: 記憶、ツール、共有環境は、失敗が持ち越される経路でもある。状態の出所、権限、変更履歴を追跡し、隔離やロールバックが可能な構造にする。
- **結合を明示的にモデル化する**: 人間や集団の行動とシステム状態が相互に影響する場合は、平衡の存在と安定条件を解析し、設計前に不安定な領域を把握する。
- **規模と組織構造を設計変数として扱う**: 集団の規模により崩壊と分極化のどちらが起こるかが変わりうる。多様性や社会的証拠の重み付け、情報交換の構造を、規模ごとに検証する。
- **部分的な機能維持の副作用を点検する**: 一部機能が残ることが圧力を弱め、問題を長引かせる場合がある。補償閾値のような境界を特定し、介入の効果が逆転する領域を避ける。
- **失敗への対応の蓄積を観察する**: 個々の失敗への対応(再開、転換など)の積み重ねが領域全体の動態を決めるため、失敗を個別事象としてでなく、対応の履歴として記録し分析する。

## 関連コンセプト

- [[feedback-loops-system-dynamics]] — フィードバック構造による系の挙動の基礎理論
- [[coupled-viability-architecture]] — 結合系の生存性を扱うアーキテクチャ
- [[adaptive-human-ai-coupling]] — 人間とAIの適応的な結合
- [[interaction-emergent-coordination]] — 相互作用から創発する協調と逸脱の伝染
- [[complex-network-dynamics]] — ネットワーク上の伝播と集合現象
- [[bounded-diversity-adaptive-feedback-collectives]] — 多様性とフィードバックによる集合知
- [[emergent-governance-networks]] — 創発的なガバナンスの構造
- [[stigmergic-self-organization-of-organizational-structure]] — 組織構造の自己組織化
- [[digital-human-error-trust-dynamics]] — エラーと信頼の動態

## 参考ソース

1. Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems — Deepak Akkil, Tamer Abuelsaad, Karthik Vikram, Matthew Pace, Aditya Vempaty (2026)
   File: raw/papers/complexity_science/emergence-world-adversarial-stress-testing-of-long-horizon-multi-agent-systems.md
2. BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents — Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Tejaswini Pedapati, Prasanna Sattigeri (2026)
   File: raw/papers/complexity_science/blindspot-a-benchmark-for-safety-and-refusal-calibration-in-long-horizon-tool-us.md
3. Flag Game: A Toy Model for Mechanistic Swarm Interpretability — Elizabeth Pavlova, Hidenori Tanaka (2026)
   File: raw/papers/complexity_science/flag-game-a-toy-model-for-mechanistic-swarm-interpretability.md
4. Modelling opinion dynamics during crises as complex contagion with feedback — Junxiang Huang, Mikhail Prokopenko (2026)
   File: raw/papers/complexity_science/modelling-opinion-dynamics-during-crises-as-complex-contagion-with-feedback.md
5. Why Some Strikes Last Longer: The Resilience Paradox of Partially Functional Institutions — Nuno Crokidakis (2026)
   File: raw/papers/complexity_science/why-some-strikes-last-longer-the-resilience-paradox-of-partially-functional-inst.md
6. Understanding cascading failure across innovation journeys : the case of antibiotics development — Birke Otto, Harry Sminia, Jörg Sydow (2026)
   File: raw/papers/complexity_science/understanding-cascading-failure-across-innovation-journeys-the-case-of-antibioti.md
