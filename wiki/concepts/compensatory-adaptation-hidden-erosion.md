# 補償的適応の枯渇と安定性の錯覚

## 概要

**補償的適応の枯渇と安定性の錯覚**とは、システムの成果指標(事故件数、遅延、コンプライアンス達成率など)が安定していても、その安定が人間の絶え間ない調整努力(補償的適応)によって支えられている場合、基盤側の劣化が見えないまま進行し、ある閾値を超えたところで突然破綻するという構造的リスクである。Tier 1(不変原理)に位置づけられる。

監視が「成果物」だけを見る限り、成果が保たれている間は消耗が検知されない。この構造は担い手が人間、AI、組織、技術のいずれであっても成立する。AI Nativeな社会設計では、AIが人間の調整作業を肩代わりしたり不可視化したりする場面が増える。そのため、指標の裏で何が資源を消費しているかを設計段階から可視化することが重要になる。

## メカニズム

中核は次の3段階である。

1. **適応資源の枯渇**:構造的な欠陥や不足(ギャップ)を、現場の担い手が追加の努力で埋め合わせる。その努力は有限の適応資源(余力)を消費する。
2. **指標と基盤状態の乖離**:補償が機能している間、観測される成果は変わらない。成果指標は健全に見え、基盤の余力だけが減っていく。
3. **閾値超過による急激な崩壊**:余力が尽きると補償が追いつかなくなり、成果が非線形に、突然悪化する。

この構造は対象を入れ替えても成り立つ。

- **人間**:過重労働を個人の頑張りで吸収している現場。
- **組織**:形式上は基準を満たしているが、担当者の手作業や暗黙の調整に依存している業務。
- **AI**:出力品質が保たれているが、人間による事後修正や検証が常態化しているAI運用。
- **技術**:設計上の不備を運用側の回避策で凌いでいる基盤。

いずれも「観測される成果」と「それを支える見えないコスト」が別の量であり、後者を測らなければ前者の安定は何も保証しない。

## 理論的背景

### 補償依存システムの形式モデル

Loepke(2026)は、社会技術システムの信頼できる性能が継続的な人間の適応に依存すると論じる。レジリエンスエンジニアリングとSafety-IIは、適応こそがシステムを安全に保つ機構であると確立してきた。しかしガバナンスが監視するのは、事故、死亡、遅延、コンプライアンスといった適応の「産物」であり、それを生み出す補償的作業ではない。そのため安定した成果が、基盤状態の漸進的な劣化を隠しうる。

この論文は、以下の量を結びつける動的モデルを構築している。

- 構造的ギャップ G(t)
- 補償努力 C(t)
- 適応的余力 R(t)
- 観測可能な成果 O(t)

モデルは、需要駆動の不足と、設計によって生み出された負担を区別する。両者は同じ有限の余力を消費するが、必要な介入が異なる。こうした補償に依存する状態は「Persistent Compensatory Engagement」と名づけられている。モデルは、余力が減少する前に補償努力が上昇するという予測を含む。ただし、提供された抜粋はその先の予測が途中で切れているため、詳細な結論や数値はここでは記述しない。

### 周辺的な示唆

他のソースは主題を直接扱っておらず、関連は限定的である。

- 生成AIと監査コストに関する研究(Zhang, 2026)は、生成AIの導入が監査費用を有意に増加させると報告する。経路として、アルゴリズムのブラックボックスが統制環境を損ない内部統制の質を下げること、組織のフラット化が冗長な防御を弱めることが挙げられている(抜粋は途中で切れている)。冗長性の縮減が、見えにくいリスクを高める例として参照できる。
- 救急車の電動化に関する研究(Dieleman & Jagtenberg, 2026)は、充電時間が応答時間に与える影響をシミュレーションで評価する。資源配置の制約が成果指標に影響する応用例だが、本概念との関係は間接的である。
- アジア7都市の非公式居住地における自動車所有の研究(Thakuriah et al., 2026)は、経済・住居の不安定性と資産所有の関係を扱う。本概念との関係は間接的にとどまる。

## AI Nativeな設計への示唆

以下は上記の構造からの設計上の含意であり、ソースが個別に主張する内容ではない。

- **成果指標と並べて補償努力を測る**:出力の品質だけでなく、人間の修正、例外対応、手作業による調整の量を継続的に計測する。努力の上昇は余力低下の先行シグナルになりうる。
- **余力を明示的な資源として扱う**:人間の注意、時間、判断力を有限の準備金として管理し、枯渇に近づく前に介入する。
- **不足の種類を区別する**:需要増による不足と、設計が生み出した負担を分け、後者は運用の頑張りではなく設計の修正で対処する。
- **AIによる補償の不可視化に警戒する**:AIが不備を静かに吸収すると、成果は安定して見えても基盤の劣化が隠れる。吸収した内容を記録し、可視化する。
- **冗長性を安易に削らない**:効率化で冗長な防御を弱めると、余力の枯渇時に崩壊しやすくなる。

## 関連コンセプト

- [[effort-opacity-and-disclosure-signal-erosion]] — 努力が見えないことで評価シグナルが劣化する構造
- [[ecological-resilience-and-stability]] — 見かけの安定と基盤のレジリエンスの区別
- [[stability-plasticity-dilemma-in-production]] — 本番環境での安定性と適応のトレードオフ
- [[micro-tasking-compensatory-strategy]] — 補償的な戦略の一形態
- [[predictive-organizational-adaptation]] — 先行的な組織適応
- [[verification-cost-and-trust-testing-of-automated-advisors]] — 検証コストの観点
- [[capability-externalization-dual-effects]] — 能力外部化と再適応
- [[temporal-erosion-of-procedural-legitimacy-under-opacity]] — 不透明性の累積による時間的侵食

## 参考ソース

1. When stable performance misleads: A formal model of compensation-dependent systems — Andreas Loepke, 2026
   File: raw/papers/corporate_governance/when-stable-performance-misleads-a-formal-model-of-compensation-dependent-system.md
2. Technology Empowerment or audit burden? A Study on the Impact of Generative AI on Corporate Audit Costs — Zhang Yijing, 2026
   File: raw/papers/corporate_governance/technology-empowerment-or-audit-burden-a-study-on-the-impact-of-generative-ai-on.md
3. Electric ambulances: will the need for charging affect response times? — Nanne A. Dieleman, Caroline Jagtenberg, 2026
   File: raw/papers/corporate_governance/electric-ambulances-will-the-need-for-charging-affect-response-times.md
4. Car-ownership and economic and housing insecurity in informal settlements in seven Asian cities — Piyushimita Thakuriah, Vidyoth Sateesh, Jinhyun Hong, David Philip McArthur, Daisuke Mizusawa, 2026
   File: raw/papers/corporate_governance/car-ownership-and-economic-and-housing-insecurity-in-informal-settlements-in-sev.md
