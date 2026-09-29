# 集中と単一障害点によるシステミックリスクの非線形伝播

## 概要

共有依存(AIベンダー、スキルレジストリ、特定国・特定基盤への主権的依存など)に機能や注意、能力が集中すると、その一点で生じた障害や攻撃が、個々の主体の損失の総和をはるかに超えて連鎖的・非線形に広がる。これが「集中と単一障害点によるシステミックリスクの非線形伝播」である。関連する一般概念として [[systemic-risk]] がある。

この概念には二つの側面がある。

1. **伝播の増幅**: 依存の集中が、障害を非線形に拡大する経路をつくる。
2. **統制の困難**: 規制対象と能力の所在がずれたり、急成長したエコシステムが事後にしか統制できなかったりして、集中したリスクを制御しにくくなる。

AI Nativeな社会では、多数の組織やエージェントが少数の基盤モデル、ベンダー、レジストリに依存する。効率の面では合理的でも、設計を誤ると社会全体の脆弱性になる。したがって集中構造を最初から設計の対象にする必要がある。

## メカニズム

以下の構造は、対象が人間、AI、組織、技術のいずれでも成り立つ。

- **単一障害点への集中**: 多数の主体が少数の共有ノードに依存する。ノードは、ベンダー、レジストリ、インフラ、特定の管轄への依存などの形をとる。個々の主体が合理的に選んだ結果が、全体の集中を生む。
- **連鎖的伝播**: ノードの障害は、運用・情報・金銭といった複数の結合層を伝わる。結合が重なるほど、外から見れば古典的な危機と区別のつかない損失に育つ。
- **非線形性と閾値依存**: 損失は裾の重い分布を示し、復旧までの遅延のような単一パラメータに鋭く依存する。平均的な想定では危険を過小評価する。
- **経路依存性**: 急成長期に注意や利用が特定の対象へ偏る。一度できた偏りは固定されやすく、後から是正するには大きなコストがかかる。
- **規制対象と能力所在のずれ**: 統制が「訓練」のような特定の段階や単位に結びついていると、能力が別の段階(推論時、エージェントの足場、消費者向けハードウェア)へ移ったときに、規制の網から抜け落ちる。
- **乗数的な介入効果**: 逆に、集中は防御側の利点にもなる。通報の集約のように、中央集権化が他の要因と掛け算で効くと、攻撃側の収益性を大きく下げられる。集中は両刃であり、脆弱性の源にも、レバレッジの源にもなる。

## 理論的背景

### AIベンダー侵害の金融への伝播

Leytesの研究(2026)は、銀行システムが不正検知、与信判断、マネーロンダリング対策のトリアージ、顧客分析などで少数の共有AIベンダーに依存している点に着目する。AIベンダー、金融機関、銀行間エクスポージャー、顧客口座を結ぶ4層の異種ネットワークを構築し、確率的な感染・清算モデル CFC-Prop を提案している。合成データ(ベンダー60、銀行220、ベンダー・銀行間のサービス辺が約2,500、銀行間エクスポージャー1,400)上で、裾の重い損失分布とパッチ遅延への鋭い依存を再現したと報告されている。

### 規制対象の移行

Ansariの研究(2026)は、現行のコンピュート・ガバナンスが訓練計算量に紐づき、訓練済みモデルを規制単位として扱っている点を指摘する。一方で能力は、推論時スケーリング、エージェント的足場、消費者向けハードウェアへの圧縮を通じてデプロイ段階へ移りつつある。そこで、監視・検証・執行にわたる20の推論時メカニズムの実現可能性を分類し、4ベンダーの証拠基盤に対して4段階の成熟度で評価している。敵対者モデル(能力3段階×役割4種)による負荷試験と、4つのガバナンス・シナリオへの対応づけも行っている。

### 急成長エコシステムの事後統制

Xiong and Zhang(2026)は、OpenClawエージェントの公開スキルレジストリの急拡大を分析した。観測可能なストックは91日でほぼ倍増し、6月時点の掲載の過半は2か月間に作られた。ブームは終盤にピークを越え、月次の掲載作成数とコアリポジトリの活動は春のピークから減少した。注意は集中しており、上位10%のスキルがダウンロード全体の46.93%を得ている。作成コホートなどを考慮すると、サイズやダウンロード数のような単純な特徴は、継続掲載の安定した予測因子ではなくなった。ブーム後に残るものを、成長の最中に見通すことは難しい。

### 主権的依存

Vashishtaらの章(2026)は、データの戦略的資産化、地政学的対立、プラットフォーム支配を主要な駆動要因として論じ、規制、産業政策、デジタル基盤整備といった政策対応を検討している。世界的な相互依存とそのトレードオフ、AIナショナリズムや国際協調にも触れる。国家レベルの依存集中が、自律性をめぐる争いを生む構図を示すものとして位置づけられる。

### 集中の防御側の利用

Fredrickson(2026)は、詐欺の利益モデルにおいて、通報率、通報の集中化、通報の正確性という3つのレバーが乗数的に作用し、詐欺チャネルあたりの期待被害者数を減らすことを示した。効果が掛け算になるため、3つすべてに働きかければ収益モデルへの影響は大きい。高価値な詐欺インフラに対しては、控えめな通報率でも大きな効果が見込めるという。

### 関連する周辺知見

Singhらのサーベイ(2026)は、LLMがXSSのような古典的脅威を増幅し、プロンプトインジェクションのようなLLM固有の脆弱性がWebアプリケーション間で伝播しうることを整理している。これは、既存の脆弱性と新種の脆弱性が層をまたいで結合することを示す。Xuらの研究(2026)は、多ドメインのミッドトレーニングで各ドメインに10〜40%の内部最適なカバレッジ帯があると報告しており、極端な偏りが最適でないことを示す。ただし、この点は学習データ構成に関する知見であり、システミックリスクへの直接の証拠ではない。

## AI Nativeな設計への示唆

1. **依存の地図を持つ**: どの共有ノード(モデル、ベンダー、レジストリ)にどれだけの主体が依存するかを、ネットワークとして可視化する。個別の評価ではなく結合構造を見る。
2. **裾のリスクと復旧時間を設計変数にする**: 平均損失ではなく裾の重い分布を前提とし、パッチや復旧の遅延を主要な管理指標に置く。
3. **多様性を確保する**: 単一ベンダー・単一モデルへの依存を避け、代替経路を保つ。関連して [[enterprise-systems-diversity]] は、システムの多様性をリスク評価の観点で扱う。
4. **統制点を能力の所在に合わせる**: 訓練時のみの規制に頼らず、推論時の監視・検証・執行も含めて統制の対象を見直す。規制対象が移る前提で設計する。
5. **成長初期から統制の足場を組み込む**: 急成長するエコシステムでは、事後の是正が難しい。登録、来歴の追跡、更新・撤去の仕組みを最初から備える。この点で [[evidence-bearing-decision-traceability]] が参考になる。
6. **集中を防御にも使う**: 通報や検知の集約を、精度と組み合わせて設計する。集中は脆弱性であると同時にレバレッジでもある。
7. **枠組みで管理する**: [[ai-governance-and-risk-management]]、[[ai-risk-management-framework]] などの枠組みに、共有依存と伝播経路の評価を組み込む。

## 関連コンセプト

- [[systemic-risk]] — システミックリスクの一般概念
- [[ai-governance-and-risk-management]] — AIガバナンスとリスク管理
- [[ai-governance-risk-compliance]] — AIのGRC
- [[ai-risk-management-framework]] — AIリスク管理フレームワーク
- [[ai-driven-devsecops]] — AI駆動のDevSecOpsセキュリティ
- [[enterprise-systems-diversity]] — 企業情報システムの多様性
- [[interaction-emergent-coordination]] — 相互作用から創発する協調と逸脱の伝染
- [[evidence-bearing-decision-traceability]] — 証拠を伴う意思決定の追跡可能性

## 参考ソース

- Alex Leytes (2026)「Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System」 — `raw/papers/ai_governance/cyber-financial-contagion-modeling-the-propagation-of-an-ai-vendor-compromise-th.md`
- Samar Ansari (2026)「Beyond Training: A Feasibility Taxonomy for Inference-Time AI Governance」 — `raw/papers/ai_governance/beyond-training-a-feasibility-taxonomy-for-inference-time-ai-governance.md`
- Aishwarya Vashishta, Nikshit Gautam, Mohit Yadav (2026)「Digital Sovereignty and Strategic Autonomy in the Age of AI」 — `raw/papers/ai_governance/digital-sovereignty-and-strategic-autonomy-in-the-age-of-ai.md`
- Yunpeng Xiong, Ting Zhang (2026)「After the Party: Governing What a Viral Agent-Skill Ecosystem Left Behind」 — `raw/papers/ai_governance/after-the-party-governing-what-a-viral-agent-skill-ecosystem-left-behind.md`
- Yunpeng Xu, Kun Zheng (2026)「Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant Domain Gaps in Multi-Domain Mid-Training」 — `raw/papers/ai_governance/everything-in-moderation-per-domain-coverage-optima-and-alignment-resistant-doma.md`
- Nivedita Singh, Alsharif Abuadbba, Yansong Gao, Surya Nepal, Hyoungshick Kim (2026)「Shifting from Injection to Interaction: Rethinking Web Security in the Age of LLMs and Beyond」 — `raw/papers/ai_governance/shifting-from-injection-to-interaction-rethinking-web-security-in-the-age-of-llm.md`
- Kyle Fredrickson (2026)「Effective Interventions Against AI-Enhanced Scams」 — `raw/papers/ai_governance/effective-interventions-against-ai-enhanced-scams.md`
