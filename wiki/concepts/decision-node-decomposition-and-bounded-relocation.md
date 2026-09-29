# 意思決定ノード分解と限定合理性の再配置

## 概要

**意思決定ノード分解と限定合理性の再配置**は、次の二つの主張を束ねたTier 1(不変原理)のコンセプトである。

1. **AIは限定合理性(bounded rationality)を除去しない。** 制約を別の場所、すなわちデータの変動性、モデルの不透明性、ガバナンスの成熟度といったアルゴリズム側の制約へ移すだけである。
2. **投資や判断を離散的な決定単位に分解して制約構造を管理することが、成果を規定する。** 「AIプログラム」という大きな塊のまま統治すると、スケーリングに失敗しやすい。

AI Nativeな社会設計では、「AIを入れれば合理性が上がる」という想定を置かない。どこに制約が移ったのか、どの単位で判断・投資・検証を行うのかを、設計の第一級の対象として扱う必要がある。

## メカニズム

このコンセプトは、対象が人間・AI・組織・技術のいずれであっても成り立つ構造的原理として、次のように整理できる。

### 1. 制約の保存と移転
どの意思決定主体にも、情報・処理能力・時間・統治能力の制約がある。能力補完の技術が入ると、制約は消えず、別の層(データの質、モデルの不透明性、統治体制の成熟度など)に現れる。複合的な認知システム全体の合理性は、個々の要素の限界ではなく、要素間の相互作用を規定する制約構造で決まる。

### 2. 離散的な決定ノードへの分解
価値・リスク・コストを事前(ex ante)に評価できる粒度まで、大きな取り組みを分割する。評価可能な単位になって初めて、投資判断も責任の所在も検証も、その単位で設計できる。

### 3. 段階的意思決定(リアルオプション)
各ノードを、不確実性が解消されるにつれて拡大・継続・撤退を選べる「オプション」として扱う。全面投入の一括判断を避け、学習の結果に応じて段階的に意思決定する。

### 4. 時間圧下の二重過程シフト
時間圧力が高まると、主体は熟慮的・合理的な判断から直感的・衝動的な判断へ移行しやすい。制約は、外部の資源だけでなく、主体の認知モードの側にも現れる。したがって、時間圧の強い局面ほど、判断単位や手順を事前に構造化しておく価値が高い。

## 理論的背景

### 決定中心のAI投資ポートフォリオ(Mathurら, 2026)
企業がAIに多額の投資を続けても、スケールせず持続的な価値を生まない事例が多い。この「AI投資パラドックス」の原因は、AIを、ワークフローに埋め込まれた個別の投資可能な意思決定機会としてではなく、広範な技術プログラムとして統治している点にあると論じられている。

この枠組みは、**AI-Investable Process Nodes(AIPN)**を導入する。AIPNは、AIが期待成果を変えうる境界づけられた決定点であり、便益・リスク・コストを事前に評価できる。ノード単位の価値は**期待純便益(Expected Net Benefit)**で定式化される。さらにリアルオプションの論理でノードを段階化し、リスク・リターンの原則でポートフォリオに組み上げる。

### アルゴリズム的限定合理性(Chen, 2026)
管理者の合理性を、**algorithmic-bounded rationality(ABR)**という概念で再構成した概念研究である。AIは限定合理性を除去せず、データ変動性、モデル不透明性、ガバナンス成熟度に関わるアルゴリズム的制約へ再配置すると主張する。AI主導・人間優先・協調の三つの意思決定モードを、アルゴリズム的限定性のメカニズムに結びつけ、モードとタスクの適合とハイブリッド意思決定アーキテクチャを持続させるガバナンス条件についての命題を提示する。また、人間とAIの協調は、自動化と人間主導の単なる中間ではなく、固有の合理性の構成であるとされる。

### 時間圧と意思決定スタイル(Altıntaşら, 2026)
トルコの航空貨物業務従事者240名を対象とした横断的な量的研究である。限定合理性と二重過程の視点から、合理的・直感的・依存的・回避的・自発的の各意思決定スタイルを個別に評価している。知覚された時間圧は、合理的意思決定と負の関連を示した。抜粋では、これに続く正の関連の詳細は途中で切れている。なお、要点として提示された知見は、時間圧下で合理的判断から衝動的・直感的なパターンへシフトするというものである。

### 周辺的知見
- **AI Engagement Orientation(Barthol, 2026)**: 受容モデル(UTAUT)が利用意図の説明にとどまるのに対し、AI導入後にプロジェクトマネージャーが意思決定にどう関与するか(限定的・回避的な利用から協働的統合まで)を捉える概念的提案である。制約への適応が主体の関与様式によって異なることを示唆する。
- **吸収能力の再検討(Pedota, 2026)**: 学習主体が人間だけだという暗黙の前提を問い直し、AI駆動プロセスに関わる新しい次元を理論化している。
- **人間の不変的価値(Naughton & Kemp, 2026)**: 生成AIが知識集約的領域にまで人間と機械の境界を動かす状況で、複雑な問題解決(ill-defined問題空間)、認知的柔軟性、社会的成果能力などの特性が中心に残ると論じている。
- **測定方法論(Hornsbyら, 2026)**: 学校でのWASH介入評価の研究で、直接観察と報告式の測定の違いが、有効性評価の結論に影響することを扱う。分解した単位の成果をどう測るかという点で、間接的な参考になる。

## AI Nativeな設計への示唆

1. **「プログラム」ではなく「ノード」で統治する。** AI導入は、便益・リスク・コストを事前評価できる決定点に分解し、ノードごとに期待純便益を評価する。
2. **ノードをオプションとして段階化する。** 検証結果に応じて拡大・継続・撤退を選べるようにし、全面展開の一括判断を避ける。
3. **制約の移転先を明示的に管理する。** データの変動性、モデルの不透明性、ガバナンスの成熟度を、ノードごとの監視対象・設計対象とする。
4. **モードとタスクを適合させる。** AI主導・人間優先・協調のどれをノードに割り当てるかを設計し、その持続条件としてのガバナンスを整える。
5. **時間圧の強い局面を前提に構造化する。** 直感的判断へのシフトが起こりうるため、手順・判断単位・権限を事前に構造化して、局面ごとの認知モードに依存しすぎないようにする。
6. **成果の測定方式を意図的に選ぶ。** 測定方法が結論を左右しうるため、ノード単位の評価指標と測定手法を、設計段階で決める。

## 関連コンセプト

- [[bounded-rationality-and-behavioral-economics]] — 限定合理性の基礎モデル
- [[decision-event-governance]] — 意思決定イベントを構成単位とするガバナンス
- [[ai-decision-authority-restructuring]] — AI組み込みによる意思決定権限の再構成
- [[ai-use-case-selection-taxonomy]] — ユースケース選択の意思決定タクソノミー
- [[human-ai-collaboration-and-decision-making]] — 人間とAIの協調と意思決定
- [[human-ai-collaboration-decision-making]] — 人間とAIの協調的意思決定
- [[ai-augmented-decision-making]] — AI支援意思決定
- [[decision-clarity-architecture]] — 意思決定の明確化アーキテクチャ
- [[constraint-anchored-validity-and-verifiable-boundaries]] — 制約による妥当性の担保と検証可能な境界
- [[context-bounded-validity-and-revalidation]] — 文脈境界付き妥当性と再検証トリガー

## 参考ソース

1. Mathur, A., Kathuria, A., Chaturvedi, D. (2026). *Governing Enterprise AI Investments: A Decision-Centric Portfolio Framework*.
   File: raw/papers/behavioral_economics/governing-enterprise-ai-investments-a-decision-centric-portfolio-framework.md
2. Chen, Z Y (2026). *Rethinking managerial rationality in the age of AI: a human–machine collaboration perspective on organizational decision-making*.
   File: raw/papers/behavioral_economics/rethinking-managerial-rationality-in-the-age-of-ai-a-humanmachine-collaboration-.md
3. Altıntaş, M., Kaya, L., Savaş, M. (2026). *Decision-making under operational pressure: A study on air cargo employees*.
   File: raw/papers/behavioral_economics/decision-making-under-operational-pressure-a-study-on-air-cargo-employees.md
4. Barthol, S. (2026). *From AI Adoption to AI Engagement in Project Management*.
   File: raw/papers/behavioral_economics/from-ai-adoption-to-ai-engagement-in-project-management.md
5. Pedota, M. (2026). *Minds and machines: Rethinking absorptive capacity in the age of artificial intelligence*.
   File: raw/papers/behavioral_economics/minds-and-machines-rethinking-absorptive-capacity-in-the-age-of-artificial-intel.md
6. Naughton, C., Kemp, S. (2026). *Human future traits and cultural equity in AI-augmented work: a multilevel psychological framework for human value creation*.
   File: raw/papers/behavioral_economics/human-future-traits-and-cultural-equity-in-ai-augmented-work-a-multilevel-psycho.md
7. Hornsby, G., Pham, C., Davis, J., Darmstadt, G. L. (2026). *Methodology for measuring behavior change dictates the perceived effectiveness of school-based WASH interventions*.
   File: raw/papers/behavioral_economics/methodology-for-measuring-behavior-change-dictates-the-perceived-effectiveness-o.md
