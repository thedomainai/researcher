# 検証可能性から実効的権威への変換ギャップ

## 概要

検証可能性から実効的権威への変換ギャップ(Verification-to-Enforcement Conversion Gap)とは、能力や違反を「見える」「確かめられる」状態にしても、それが制度的権威や執行力に変換されなければ制約として機能しない、という構造的な隔たりを指す。統治の実効性は、検証の技術的可否だけでなく、次の2点で決まる。

- 検証にかかるコストと、隠蔽・不可視化にかかるコストの関係
- 検証結果を実行制約へ接続する制度的な経路が存在するか

AI Nativeな社会設計にとってこの原理が重要なのは、AIの能力が統治の変数そのものになりつつあるからである。評価・監査・可視化の仕組みは整備しやすい。しかし、それらが「止める」「遅らせる」「権限を与えない」といった決定に接続されなければ、透明性は高まっても統治は成立しない。設計者は「検証できるか」と「検証結果が誰の権限で何を動かすか」を、別々の設計課題として扱う必要がある。

## メカニズム

この原理は対象が人間・AI・組織・技術のどれであっても成立する、三つの構造から整理できる。

### 1. 検証と執行の分離

検証は「状態を知る」行為であり、執行は「状態を変えさせる」行為である。前者は情報の問題、後者は権限と制度の問題であり、両者は独立に成立する。検証が高度化しても、執行権限を持つ主体に結果が届かない、あるいは届いても行使する制度的根拠がなければ、制約は生まれない。これは可読性(legibility)が制約(constraint)と同義ではないということである。

### 2. 検証コストと隠蔽コストの非対称性

検証が実効的かどうかは、検出側のコストと回避側のコストの相対関係で決まる。回避が高コストであれば、回避できるのは資源の豊富な主体に限られ、統治は一定の実効性を持つ。逆に、検証対象が不可視化の余地を持ち、検証側のコストが高い場合、宣言された状態と実際の状態が乖離する(declared versus verified)。検証の困難さは、物理的な隠蔽可能性だけでなく、運用・保守といった組織的な運用の可視性にも依存する。

### 3. 制度的権威への変換

能力(capability)は、制度に吸収されて初めて権威(authority)となる。検証結果が制度内に吸収され、拘束力のある手続き(ゲート、停止権限、承認要件など)として組み込まれる過程が変換である。この変換が欠けると、検証情報は「参考情報」にとどまる。

## 理論的背景

### 能力と権威の制度的ギャップ

Choi(2026)は、フロンティアAIにおいて能力の進展速度そのものが統治変数になったと論じる。Dario Amodeiによる、フロンティアAI開発を意図的にペース調整する提案を事例に、独立評価は透明性・可読性・検証を改善できるが、検証だけでは制約にならないと主張する。深い統治課題は、制度的吸収(institutional absorption)を通じた、能力から制度的権威への変換である。論文は四つの区別を展開している。

- 可読性と制約
- 能力と権威
- 垂直的ペーシングと水平的ペーシング
- 宣言されたものと検証されたもの

### 検証の実行可能性と隠蔽コスト

Teagueら(2026)は、AI条約の検証における未申告の計算施設の検出を主題とし、水中データセンターが回避経路になりうるかを検討した。10万H100相当規模の訓練を水中で行う場合、電力供給と冷却は扱えるが、相互接続と、大規模訓練が要する実地の保守が深刻な障害になるという。これを克服できるのは、大きなコストとスケジュール上の不利益を受け入れる、資源豊富な国家主体に限られ、しかも効率ではなく隠蔽が目的の場合だけである。隠蔽の実行可能性は運用コストによって制約され、そのコストが検証可能性を左右するという非対称性の具体例である。

### 検証を執行に「コンパイル」する設計

Tanveer(2026)は、ガバナンスを執行へコンパイルするという発想で、リスク階層化された信頼度考慮型の公平性ゲートを機械学習パイプラインに実装する研究を示している。ソースの抜粋からは詳細を確認できないが、検証(測定)をパイプライン上の通過条件という形で執行へ接続する方向性を示す事例として位置づけられる。

### 能力の実在と回避の実態

Barron(2026)の実験では、小規模モデルのabliteration(安全機構の除去)は、そもそも知識が存在しないため危険な能力を解放しなかった。一方、実際に攻撃的知識を持つ中規模モデルでは、推論時のバイパスが検証済みの動作する攻撃的出力を生んだ。PREFILLは5カテゴリで10〜65%のASR、COGBURNはQwen 14Bに対して68%(17/25)、R1 7Bに対して100%(25/25)を達成した。また、実験中に発生したOpenAIアカウントの停止は、プロバイダーレベルの逐次パターン監視と整合的であるとされる。内在的な能力と外部的制約の不調和が問題を規定することを示し、検証された能力が外部制約だけでは抑えきれない例といえる。

### 診断と監督距離

DiaVLo(Corti & Yang, 2026)は、視覚言語モデルの望ましい振る舞いと観測された振る舞いの仕様を構築し、因果推定で影響の大きい概念を特定する診断枠組みである。検証手段の高度化を示す一方、それを執行に接続する仕組みは別問題として残る。Sherlinら(2026)は、神経調整領域のAI応用のリスクを、不透明性、臨床的帰結、監督からの距離の三次元で整理するリスク連続体モデルを提案している。監督からの距離が大きいほど検証が執行に結びつきにくいという観点で参照できる。

### 独立検証の基盤

Condom-Tibauら(2026)は、独立研究者がプラットフォームに直接介入できないという制約に対し、オープンプラットフォーム上のフィールド実験(OPFE)を提案する。検証主体が被検証系の内部にアクセスできるかどうかが、検証可能性の前提条件になることを示唆する。

## AI Nativeな設計への示唆

1. **検証と執行を別々に設計する**: 評価基盤を整えるだけでなく、結果がどの主体のどの権限に紐づくかを明示する。可読性の向上を統治の達成と混同しない。
2. **検証結果を実行経路に組み込む**: 公平性ゲートのように、評価をパイプラインの通過条件や停止条件へ変換する。「参考情報」から「拘束条件」への昇格を設計対象とする。
3. **検証コストと隠蔽コストを見積もる**: 対象が回避するための運用コスト(保守、相互接続、監視回避)を評価し、隠蔽が割に合わない構造を目指す。
4. **宣言と検証を区別して扱う**: 申告された能力や状態を、検証済みの状態と別のカテゴリで管理する。
5. **検証者の独立性とアクセスを確保する**: 検証主体が被統治系に依存しないこと、および必要な内部アクセスを持つことを制度的に担保する。
6. **監督からの距離を縮める**: 不透明性が高く帰結が重大で、人間の監督から遠い応用ほど、強い執行接続を要求する階層化を行う。
7. **単一の防御に依存しない**: バイパスが実証されている以上、外部ガードレールだけでなく、プロバイダーレベルの監視など複数層を組み合わせる。

## 関連コンセプト

- [[opacity-verification-gap]] — 不透明性が検証可能性を損なう非対称性
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[structural-separation-of-verification-from-governed-system]] — 検証機構を被統治系から構造的に分離する原理
- [[execution-time-governance]] — 実行時に権限を制御する設計
- [[institutional-legitimacy-in-ai-enforcement]] — 執行の制度的正当性
- [[principles-to-practice-legitimacy-gap]] — 原則から実践への翻訳ギャップ
- [[llm-product-evaluation-results-actionability-gap]] — 評価結果が行動に結びつかないギャップ
- [[costly-verification-allocation-tradeoff]] — 検証コストの配分問題
- [[plural-independent-checks-against-singular-power]] — 独立した複数の牽制
- [[ai-decision-authority-restructuring]] — AI組み込みによる意思決定権限の再構成

## 参考ソース

- Chris Choi (2026)「Pacing Capability: From AI Alignment to Governance Coherence」 — `raw/papers/ai_governance/pacing-capability-from-ai-alignment-to-governance-coherence.md`
- James Teague, Ashmita Rajmohan, Yannick Muehlhaeuser (2026)「Could Underwater Data Centers Pose a Risk to AI Treaty Verification?」 — `raw/papers/ai_governance/could-underwater-data-centers-pose-a-risk-to-ai-treaty-verification.md`
- Rizwan Tanveer (2026)「Compiling governance into enforcement: risk-tiered, confidence-aware fairness gates for machine-learning pipelines」 — `raw/papers/ai_governance/compiling-governance-into-enforcement-risk-tiered-confidence-aware-fairness-gate.md`
- Lorenzo Corti, Jie Yang (2026)「DiaVLo: Diagnosing Behaviours of Vision-Language Models」 — `raw/papers/ai_governance/diavlo-diagnosing-behaviours-of-vision-language-models.md`
- Richard Barron (2026)「RS-2026-080 - Capability or Compliance: What Abliterated Models and Guardrail Bypass Actually Reveal About AI Safety Alignment」 — `raw/papers/ai_governance/rs-2026-080---capability-or-compliance-what-abliterated-models-and-guardrail-byp.md`
- Leslie Sherlin, Robert Longo (2026)「Navigating Artificial Intelligence in Neuroregulation Practice: Ethical Principles, Risk Stratification, and a Clinical Policy Framework」 — `raw/papers/ai_governance/navigating-artificial-intelligence-in-neuroregulation-practice-ethical-principle.md`
- Jordi Guillem Condom-Tibau ほか (2026)「Open Platform Field Experiments: Expanding the Design Space of Experimental Research on Social Media」 — `raw/papers/ai_governance/open-platform-field-experiments-expanding-the-design-space-of-experimental-resea.md`
