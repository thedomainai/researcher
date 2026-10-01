# 不可逆化前の権限判断と制約の内部設計化

## 概要

不可逆化前の権限判断と制約の内部設計化とは、統治(ガバナンス)の二つの原理をまとめた概念である。

1. **介入点の原理**:ある行為の効果が不可逆になる、あるいは確定(コミット)する前に、その効果に権限があるかどうかを判断する。
2. **内部設計化の原理**:社会的・外部的な制約(法、規範、倫理、環境リスクなど)を、事後の監査や広報で扱うのではなく、システムの内部構造、つまり設計変数として組み込む。

AI Nativeな社会では、AIが提案・実行・連鎖する速度が人間の確認速度を上回りやすい。効果が出てから止めたり是正したりする統治は間に合わず、被害や信頼の毀損が固定化してしまう。そのため「どこに判断点を置くか」と「制約をどこに埋め込むか」が、システム設計の中心課題になる。

## メカニズム

この構造は、行為主体が人間、AI、組織、技術のいずれであっても成立する。

**1. 不可逆性前の介入点**
どの行為にも、取り消し可能な段階(提案・準備)と、取り消せない段階(確定・外部への効果発生)がある。統治が実効性を持つのは、権限判断をこの境界の手前に置いたときである。境界を越えた後の判断は、追認か事後対応にしかならない。

**2. 制約の設計変数化**
制約を外側からの「後付けの遵守事項」として扱うと、本来の業務設計と競合し、形骸化しやすい。制約を製品構造、リスク枠組み、意思決定手順などの内部変数として扱えば、最適化の対象に最初から含まれる。

**3. 権力・透明性・信頼ギャップの拡大**
介入点がなく、制約が内部化されていない場合、権力・透明性・信頼のあいだにギャップが生じる。このギャップがあると、不適切な技術でも急速に普及しうる。さらに、言葉の曖昧さのような言説上の仕掛けが、既存の力関係を固定化する働きをする場合もある。

**4. 制約による選択肢の再編**
外部リスクが増すと、資源は競合する目的の間で再配分され、戦略的選択肢は狭まる。制約を内部設計に取り込まなければ、この再配分は場当たり的で不透明になる。

## 理論的背景

**Execution Governance(EG1–EG6)** [1]
実務ハンドブックとして、どの統治対象(governed surface)をいつ明示すべきかを整理している。中心となるのは「Cumulative Architecture, Scoped Application」の原則である。EG1〜EG6は一つの累積的な研究アーキテクチャを成すが、六つの順次承認ゲート、必須のランタイムサービス、成熟度の梯子のいずれでもない。運用範囲は、統治対象の効果と、その導入環境に存在する重大な失敗面によって決まる。要素には次のものがある。
- EG1 Effect Authority:提案された効果が、Six Conditions のもとで現在有効な権限を持つか。
- EG2.x Pre-Effect Authorization Boundary:権限判断が、効果の不可逆化・確定より前に行われるか。
- EG3 Commitment Integrity など、以降の統治面(抜粋では途中までの記載)。

**責任あるイノベーションのビジネスケース** [2]
Facebook-Cambridge Analytica、Post Office Horizon、オランダ政府のアルゴリズムによるプロファイリングを巡る崩壊などの事例を挙げ、無責任なデジタルイノベーションの社会的・商業的リスクを論じている。AI動画面接のようなHR技術は競争優位の機会を与える一方、個人データの扱いで法的・民主的規範と緊張を起こし、未知の技術が急速に主流化しうる。権力・透明性・信頼のギャップがその背景にあるという整理である。

**ESGバンキングモデル** [3]
ESGを「コミュニケーション活動」ではなく「制度的アーキテクチャ」、すなわち基本的な設計制約として位置づけている。小売銀行は、気候調整済みの与信評価、排出を意識した商品設計、公正で倫理的な技術展開、透明なガバナンスなどを事業モデルの中核に統合する必要があるとする。ESGは、レジリエンスや長期的価値、地域の信頼、規制上の信用と切り離せないという主張である。

**気候リスクと越境M&A** [4]
中国A株上場企業の54,389企業年データ(2000〜2023年)を用いた分析で、気候リスクが高いほど越境M&Aを開始する確率が有意に低いことを示している。この関係は、代替指標、クラスタリング、プラセボ検定、操作変数、外生的気候ショックのイベントスタディなどで頑健だった。メカニズムとして、企業価値の低下と、財務・経営資源のグリーン投資への再配分(海外買収に使える資源の減少)が示唆されている。関係は主に慢性的な物理リスクと移行リスクによって駆動される。

**戦略的多義性(Strategic Polysemy)** [5]
「hallucination」「chain-of-thought」「agent」「alignment」などの用語は、狭い技術的定義と広い擬人的連想を同時に保持する。著者らはこれを、技術的に再定義された語で直感的・擬人的な含意を喚起する「glosslighting」という概念で捉え、研究者、政策担当者、資金提供者、公衆の理解に制度的・言説的な影響を与えると論じる。透明性と権力関係が、言葉の水準でも設計対象になりうることを示す。

## AI Nativeな設計への示唆

- **効果の境界を先に定義する**:AIエージェントの行為について、取り消し可能な段階と確定段階の境界を明示し、その手前に権限判断の関所を置く。
- **権限の現在性を確認する**:承認を過去の一度きりの許可とせず、効果の発生時点で有効な権限かを確認する構造にする(EG1の発想)。
- **統治面を効果に応じて絞る**:全統制を一律に課すのではなく、統治対象の効果と重大な失敗面に応じて適用範囲を決める [1]。
- **制約を最適化の入力にする**:法・倫理・環境などの制約を、事後チェックではなく、商品設計・リスク評価・意思決定ロジックの変数として初期設計に含める [3]。
- **ギャップを監視する**:権力・透明性・信頼のギャップを、導入判断の指標として扱い、拡大する兆候があれば普及前に介入する [2]。
- **用語の透明性を保つ**:AIの能力を擬人的に語る言葉は、技術定義と日常的含意の差を明示し、権限や責任の所在をぼかさないようにする [5]。
- **資源再配分を織り込む**:外部リスクによる資源競合を前提に、戦略的選択肢の制約を設計段階で見積もる [4]。

## 関連コンセプト

- [[execution-time-governance]] — 実行時の権限委譲と統治設計。介入点の具体化に直結する。
- [[constraint-anchored-validity-and-verifiable-boundaries]] — 制約による妥当性の担保と検証可能な境界。
- [[constitutional-constraint-and-power-balance]] — 憲法的制約と権力制衡による統治。
- [[decision-cycle-compression-and-residual-authority]] — 意思決定サイクルの圧縮と残余権限の設計。
- [[ai-decision-authority-restructuring]] — AI組み込みによる意思決定権限の再構成。
- [[technology-mediated-power-asymmetry-amplification]] — 技術による力の不均衡の増幅。
- [[verification-to-authority-conversion-gap]] — 検証可能性から実効的権威への変換ギャップ。
- [[theory-of-constraints]] — 制約理論。
- [[multilayer-interaction-determines-adoption-outcomes]] — 多層相互作用が導入成果を決める。

## 参考ソース

1. Execution Governance EG1–EG6 Practical Handbook — Ho Wa KU, 2026 — `raw/papers/business_ethics_csr/execution-governance-eg1eg6-practical-handbook.md`
2. Exploring the Business Case for Responsible Innovation — Vincent Bryce, 2026 — `raw/papers/business_ethics_csr/exploring-the-business-case-for-responsible-innovation.md`
3. The ESG Banking Model — Gulzar Singh, 2026 — `raw/papers/business_ethics_csr/the-esg-banking-model.md`
4. Rethinking overseas expansion: climate risk and Chinese corporations' cross-border mergers and acquisitions — Yue Guo, Yangyulong Wu, 2026 — `raw/papers/business_ethics_csr/rethinking-overseas-expansion-climate-risk-and-chinese-corporations-cross-border.md`
5. Strategic Polysemy in AI Discourse: A Philosophical Analysis of Language, Hype, and Power — Travis LaCroix, Fintan Mallory, Sasha Luccioni, 2026 — `raw/papers/cognitive_science/strategic-polysemy-in-ai-discourse-a-philosophical-analysis-of-language-hype-and.md`

## 追加ソース（2026-10-02）

* **タイトル**: Pre-Irreversibility Safety for Advanced AI: Distributed Irreversible Authority, Timely Refusal, and Human-Revisable Development (2026)
  **ファイルパス**: `raw/papers/ai_governance/pre-irreversibility-safety-for-advanced-ai-distributed-irreversible-authority-ti.md`
