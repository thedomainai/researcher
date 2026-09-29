# 文脈内証拠による評価:脱文脈的指標の限界

## 概要

文脈内証拠による評価(Situated Evidence over Decontextualized Metrics)とは、システムの価値やリスクは、実際の利用文脈における適応・工作(ワークアラウンド)・長期的帰結を通じてしか観測できない、という原理である。ベンチマーク、アラインメントスコア、安全性テストのような開発用の脱文脈的指標や、導入前の検証だけでは、導入判断の根拠として不十分だと考える。

この原理はAI Nativeな設計にとって重要である。生成AIの組織導入は、それを統治するための証拠基盤の整備よりも速く進んでいる。既存の評価ツールはモデル開発のために作られており、特定の現場で価値が生まれるのか、摩擦が生じるのか、リスクがどこへ移るのかを判断するようには作られていない。導入判断を測定可能なものだけに頼ると、測定と実態の乖離が見えなくなる。

## メカニズム

この原理は、評価対象が人間、AI、組織、技術のいずれであっても成り立つ構造として、次の3点に整理できる。

1. **文脈依存的妥当性**:ある指標が妥当かどうかは、それが測定された条件と、判断が使われる条件との対応によって決まる。開発環境で妥当な指標が、現場の利用者、タスク、設定の組み合わせに対して妥当だとは限らない。
2. **測定と実態の乖離**:指標は制御された条件で得られる。実際の利用では、人々がシステムを自分の仕事に合わせて取り込み、改変し、迂回する。この「利用されている状態」は、指標の設計時には想定されていない。
3. **創発的帰結の観測不能性**:長期的な帰結は、システム単体ではなく、システムと人と制度の相互作用から生じる。導入前の検証では、この帰結はそもそも観測できない。

したがって、利用者・タスク・環境ごとのばらつきは、制御して除去すべきノイズではない。導入判断に関わる証拠の主要な源泉として扱うべきものである。

## 理論的背景

**AI-in-use評価の枠組み(Schwartz & Waters)**
本概念の中心となるソースである。既存の評価ツールは開発向けであり、日常業務に組み込まれたAIの振る舞いに関する体系的な証拠はほとんどないと指摘する。そのうえで、人々がAIシステムを実際にどう取り込み、適応させ、迂回するか(AI-in-use)と、その後の時間経過に伴う帰結に焦点を当てた、実世界のAI評価枠組みを提案している。ばらつきを中心的な証拠とみなし、大規模に意思決定可能な証拠を作るための4つの設計原則を掲げる。

**組織展開における「パイロットの罠」(Jensen & Grønbek)**
6件の専門家インタビューに基づく修士論文レベルの研究である。AIの規模展開の成否は、技術的成熟度よりも、ガバナンス構造、戦略的な位置づけ、職種横断的な協働、ユーザー採用、既存ワークフローへの統合といった組織整列に左右されるとされる。実験段階の成功が、そのまま運用段階の成功を意味しないことを示唆する。ただし、サンプルは小規模である。

**言説構造の診断(Khatri ら)**
マルチエージェントLLMシステムを、エージェント間の言説に着目して診断する定量的エスノグラフィーの試みである。自動採点を題材に認識論的ネットワーク分析(ENA)を適用し、正しい判定に至った議論と誤った判定に至った議論を比較している。エージェントが複数いることは、それだけでは一貫した推論を保証しない。抜粋からは、正しい判定が採点基準に根拠を置く議論に特徴づけられていたことが読み取れる。最終出力の点数だけでは見えない、過程の構造が成否を分けるという示唆になる。

**方法論の多様性(Džogović ら)**
35本の査読論文の分析から、混合研究法は単一の統合手続きではなく、認識論的に異なる複数の構成(逐次的な非対称性、並行する認識論的緊張、入れ子的依存など)から成ると論じる。量的指標と質的・エスノグラフィー的知見の組み合わせ方自体が、証拠の意味を左右することを示している。

**補助的な視点**
Bouchardは、GenAIが学習者に与える影響を示す経験的証拠が現時点では乏しいことを踏まえ、批判的実在論の層状の見方から出発すべきだと述べる。ただし具体的な教育メカニズムは特定していない。Paulは、AI政策研究において、AIを中立的な問題解決ツールとして扱う見方と、権力関係を形作る社会技術システムとして扱う見方の違いを整理する。Kyriakoglouらは、高等教育における生成AIの倫理的懸念が、経験的研究へどう操作化されているかを扱う。これら3件の抜粋からは、詳細な実証結果までは確認できない。

## AI Nativeな設計への示唆

- **導入判断を段階化する**:導入前のベンチマークは「必要条件の確認」にとどめ、判断の根拠は利用開始後に得られる文脈内証拠で更新する設計にする。
- **ばらつきを記録する**:利用者、タスク、設定による差異を平均化せず、証拠として保持する。工作(ワークアラウンド)や迂回の観察を、評価の正式な入力にする。
- **過程を観測可能にする**:最終出力の点数だけでなく、判断が何に根拠づけられているかという過程の構造を診断できるようにする(Khatriらの知見に対応する)。
- **量と質を意図的に組み合わせる**:定量指標とエスノグラフィー的観察を、どちらが先か、どちらが従属するかを明示して構成する。
- **組織条件を評価に含める**:モデル性能だけでなく、ガバナンス、ワークフロー統合、職種横断性を導入可否の評価項目にする。
- **長期帰結を追跡する**:導入後の帰結を時間軸で追い、リスクの移動や摩擦の発生を検出する枠組みを最初から用意する。

## 関連コンセプト

- [[situated-knowledge-validation]] — 状況知識の検証という観点で直接つながる
- [[situated-cognition]] — 利用文脈に埋め込まれた認知という前提
- [[situated-knowledge-and-epistemology]] — 状況的知識の認識論的な基盤
- [[evidence-based-management]] — 証拠に基づく意思決定の実践
- [[evidence-bearing-decision-traceability]] — 意思決定と証拠の対応づけ
- [[calibrated-multi-evidence-fusion]] — 複数の証拠を統合する枠組み
- [[cultural-context-adaptation-metrics]] — 文脈に応じた指標の設計
- [[alternative-metrics-of-progress]] — 既存指標に代わる測定の考え方
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性のずれが生む問題
- [[choice-architecture-and-reliance-shaping]] — 利用実態が依存や信頼を形づくる点
- [[distributed-agency-and-assemblage-reconfiguration]] — 導入による組織の再構成

## 参考ソース

1. From Diagnosis to Redesign: Using Quantitative Ethnography to Improve Multi-Agent LLM Reasoning — Vedant Khatri ら, 2026
   File: raw/papers/anthropology/from-diagnosis-to-redesign-using-quantitative-ethnography-to-improve-multi-agent.md
2. 発表「GenAI and Education in the Humanities: Insight from Critical and Social Realism」 — Jérémie Bouchard, 2026
   File: raw/papers/anthropology/発表genai-and-education-in-the-humanities-insight-from-critical-and-social-realism.md
3. Epistemological Configurations and the Structural Positioning of Ethnography in Mixed-Methods Research — Suada A. Džogović ら, 2026
   File: raw/papers/anthropology/epistemological-configurations-and-the-structural-positioning-of-ethnography-in-.md
4. Wild, Thick, and Wicked: Situated Evidence on AI-In-Use for Decisions About Deploying AI Systems — Reva Schwartz, G Waters, 2026
   File: raw/papers/anthropology/wild-thick-and-wicked-situated-evidence-on-ai-in-use-for-decisions-about-deployi.md
5. Problem-solving ontologies on steroids? The space for critique in policy research on artificial intelligence — Regine Paul, 2026
   File: raw/papers/anthropology/problem-solving-ontologies-on-steroids-the-space-for-critique-in-policy-research.md
6. Specialeafhandling: Scaling AI in Organisations: An Empirical Study of Organisational Conditions Differentiating Enterprise Adoption from the Pilot Trap — Nicolai Friis Jensen, Rasmus Grønbek, 2031(ソース記載のまま)
   File: raw/papers/anthropology/specialeafhandling-scaling-ai-in-organisations-an-empirical-study-of-organisatio.md
7. From Ethical Discourse to Empirical Evidence: How Ethical Concerns are Operationalized in Studies on Generative AI in Higher Education — Revekka Kyriakoglou ら, 2026
   File: raw/papers/behavioral_economics/from-ethical-discourse-to-empirical-evidence-how-ethical-concerns-are-operationa.md
