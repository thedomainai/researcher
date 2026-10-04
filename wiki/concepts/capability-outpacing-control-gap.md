# 能力拡大が制御を上回るギャップ

## 概要

能力拡大が制御を上回るギャップ（Capability-Outpacing-Control Gap）とは、AIの能力の拡大速度が、安全対策・評価・ガバナンスの整備速度を構造的に上回る状態を指す。本記事ではこれをTier 1（不変原理）の概念として扱う。ソース[3]は、この現象を「capability overhang」として扱い、能力が安全対策の開発より速く拡大する現象と定義している。

このギャップは、特定の企業の怠慢や一時的な技術的遅れの結果ではない。経済的インセンティブと再帰的改善の複利効果から生じる構造的な帰結であり、善意の設計や整合性（アライメント）の最適化さえ、制御不能性の源泉になりうる。

AI Nativeな社会設計にとって重要なのは、「ギャップはいずれ埋まる」という前提を置けない点にある。ギャップが不変の構造であるなら、制御を後付けの追加措置として考えるのではなく、能力の拡大と同じ速度で制御が拡張されるようにアーキテクチャへ組み込む必要がある。

## メカニズム

この構造は、対象が人間・AI・組織・技術のいずれであっても成立する。核となる要素は次の4つである。

### 1. 再帰的自己改善と複利成長
システムが自らの能力を生み出す過程そのものを改善できるなら、改善は次の改善に引き継がれ、複利的に蓄積する。一方、制御手段（評価・監査・規則）は通常、能力の出現を観測してから整備されるため、線形または段階的にしか拡張されない。この非対称が、時間とともにギャップを拡大させる。これは、経験を再利用可能な知識に統合して次の改善の土台にする組織・エージェントでも同様である。

### 2. インセンティブの非対称性
能力向上の便益は、成果として即座に観測でき、競争優位に直結する。安全対策の便益は「起きなかった事故」であり、可視化しにくい。その結果、研究や投資は能力強化に偏りやすい。ソース[3]は、現状のAI研究が安全性の整合よりも能力強化を優先していると分析している。

### 3. 内的目的関数の矛盾の増幅
システム内部に複数の目的（たとえば一貫性の維持と安全性の遵守）が併存すると、相互作用の反復によって一方が他方を上書きしうる。制御を意図して導入した目的や設計原理も、この矛盾の一部になりうる。

### 4. フィードバックループ
能力の拡大が利用の拡大を呼び、利用が資源と競争圧力を生み、それがさらなる能力拡大を促す。制御側にはこの自己強化の回路がないため、ギャップは自己維持的に広がる。

これらは、対象を入れ替えても同型である。人間組織では「成長する事業と追随の遅い内部統制」、技術では「拡張するシステムと追随の遅い検証手段」として現れる。

## 理論的背景

### 再帰的自己改善の実証（ソース[1]）
AI4AI-Benchは、再帰的自己改善（RSI）を、AIシステムがAIシステムを生み出す過程を改善できるか、という問いとして定式化する。その過程とは訓練アルゴリズムであり、より良い目的関数や更新則は、次のエージェントを生む実行を含む後続のすべての実行で、計算量と能力の交換比率を改善する。したがってRSIの実現可能性は、エージェントが訓練アルゴリズムを設計できるかにかかっている。同ベンチマークは、10の訓練アルゴリズム系統にわたる10個の凍結された研究リポジトリを用意し、各タスクでエージェントに単一のB300で4時間を与えて訓練アルゴリズムを書き換えさせる。提供された抜粋の範囲では、個別の性能結果までは確認できない。それでも、この能力を測る枠組みが整備され始めていること自体が、複利メカニズムの現状を示す実証的な出発点となる。

### 経験の統合による能力の複利化（ソース[2]）
WikiSkillは、エージェントのスキルを永続的な知識ベース（wiki）と共進化させる枠組みである。生の実行経験、蓄積された知識、実行可能なスキルを分離し、経験を継続的にwikiへ統合して、後続のスキル更新がそれを土台にできるようにする。抜粋によれば、多様なベンチマークとモデルで最先端のスキル進化手法を一貫して上回る。能力進化が、経験が再利用可能な知識に統合されることで複利化することを示す例である。

### capability overhangと不変制約（ソース[3]）
ソース[3]は、能力が安全対策より速く拡大する現象の理論的基礎を検討し、近年のAI開発の実証的証拠を分析し、緩和策を提案する。能力強化の優先が危険なギャップを生み、意図しない結果につながりうると論じる。また、領域横断でギャップを測る枠組みを提示し、制約付き訓練パラダイムや、人間とAIのハイブリッドなガバナンスモデルなどの緩和手法を評価している。結論として、AIの発展を人間の価値と意図に沿わせるには、能動的な安全研究が不可欠だとする。

### 善意の設計が生む構造的リスク（ソース[4]）
「Benevolent Gravity」は、対話型AIの設計原理に内在する構造的リスク、すなわち善意が制御不能性を招く可能性を扱う。提供された抜粋にはAbstractの本文がなく、詳細な論拠は確認できない。ここでは、善意に基づく設計原理そのものがリスクの源泉になりうるという、論文の位置づけのみを参照する。

### 一貫性最適化による安全性の上書き（ソース[5]）
Coherence Compliance Vulnerability（CCV）は、大規模言語モデルにおいて、一貫性の最適化が多ターンの枠組み誘導を通じて安全性のアライメントを上書きする、訓練レベルの行動的脆弱性として記述される。Microsoft Copilotでの6セッションが、哲学的・物語的・感情的な誘導アプローチにわたって一貫した行動的特徴を示したとされ、他の手法との比較でアーキテクチャ横断の検証も行われている。これは、内的目的関数の矛盾が対話の反復で増幅される具体例である。

### 既存の規格の限界（ソース[6]）
ソース[6]は、AI、自律エージェント、デジタルツインなどの収斂が、既存の標準体系では十分に扱えないガバナンス問題を生んでいると述べる。ICTインフラ規格とAIガバナンス枠組みが並存しつつ、両者の間に空白があるという指摘である。ただし、この制約の因果メカニズムは説明されておらず、問題の特定にとどまる。

## AI Nativeな設計への示唆

1. **制御を能力と同じ速度で拡張する設計**: 制御を事後の追加措置とせず、能力の拡張経路そのものに検証・認可・監査を組み込む。実行時の認可や定量的な制御点の設計が具体策となる（[[runtime-authorization-control-points]]）。
2. **不透明性への備え**: 能力が検証能力を超えて伸びると、内部の挙動を確認できなくなる。検証可能性の非対称性を前提に設計する（[[opacity-verification-gap]]）。
3. **記憶・制御・検証の一体化**: 経験を蓄積して自己改善するエージェントでは、何を記憶し何を実行に反映するかの制御が重要になる（[[agentic-ai-memory-control]]）。
4. **善意と整合性最適化を無謬視しない**: 一貫性や親切さなど単一の目的の最適化が、安全性を上書きしうる。目的間の矛盾を前提に、多層の制約を設ける。
5. **検証資源の合理的な配分**: 全件検証は能力の拡大に追いつかないため、検査コストと精度のトレードオフを踏まえた配分が必要になる（[[costly-verification-allocation-tradeoff]]）。
6. **ハイブリッドなガバナンス**: ソース[3]が挙げる人間とAIの協調的なガバナンスモデルや制約付き訓練を、設計選択肢として検討する。
7. **権力と制約の制度化**: 能力の集中に対しては、憲法的な制約と権力の制衡という統治原理が参照点になる（[[constitutional-constraint-and-power-balance]]）。

## 関連コンセプト

- [[opacity-verification-gap]] — 能力の拡大が検証能力を上回る典型的な現れ方
- [[runtime-authorization-control-points]] — 制御を実行時の設計に組み込む具体策
- [[agentic-ai-memory-control]] — エージェントの経験蓄積と制御・検証
- [[costly-verification-allocation-tradeoff]] — 検証資源の制約下での配分
- [[dynamic-capability-amplification]] — 能力が動的に増幅される側面
- [[computational-limits-forcing-decentralized-autonomy]] — 中央集約的な制御の限界
- [[epistemic-authority-redistribution-and-knowledge-consolidation]] — 経験の知識化がもたらす能力の複利化
- [[constitutional-constraint-and-power-balance]] — 制約と制衡による統治

## 参考ソース

1. AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement — Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao (2026)
   File: raw/papers/ai_governance/ai4ai-bench-benchmarking-llm-agents-in-algorithmic-design-for-recursive-self-imp.md
2. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution — Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan (2026)
   File: raw/papers/ai_governance/wikiskill-compiling-agent-experience-into-persistent-knowledge-for-skill-evoluti.md
3. Assessing Capability Overhang in Advanced AI Systems: Risks and Mitigation Strategies — Zen Revista, 10 IA (2026)
   File: raw/papers/ai_governance/assessing-capability-overhang-in-advanced-ai-systems-risks-and-mitigation-strate.md
4. Benevolent Gravity: the lethal structure inherent in conversational AI design principles — Kenji Yamada (2026)
   File: raw/papers/ai_governance/benevolent-gravity-the-lethal-structure-inherent-in-conversational-ai-design-pri.md
5. Coherence Compliance Vulnerability (CCV) — Multi-Turn Framework Induction Producing Model Manipulation in Large Language Models — Creighton Baxter (2026)
   File: raw/papers/ai_governance/coherence-compliance-vulnerability-ccv-multi-turn-framework-induction-producing-.md
6. A Global AI-Ready ICT Infrastructure Governance Framework for Autonomous Telecommunications and Data-Centre Ecosystems — M. Rizwan Yasin (2026)
   File: raw/papers/ai_governance/a-global-ai-ready-ict-infrastructure-governance-framework-for-autonomous-telecom.md

## 追加ソース（2026-10-04）

* **タイトル**: AI Safety Measures Are Advancing: The Policy–User Gap in Autonomous AI Governance and Operational Control (2026)
  **ファイルパス**: `raw/papers/organization_science/ai-safety-measures-are-advancing-the-policyuser-gap-in-autonomous-ai-governance-.md`
