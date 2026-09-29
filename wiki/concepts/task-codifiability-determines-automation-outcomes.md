# タスクの形式化可能性が自動化の帰結と分配を決める

## 概要

「タスクの形式化可能性(codifiability)」とは、あるタスクの手順・判断基準・入出力が、明示的なルールやデータとして記述できる度合いを指す。本コンセプトは、次の三点が形式化可能なタスクの有無と、それをどの指標で評価するかによって決まると主張する。

1. AIが人間を**代替**するのか**補完**するのかの境界
2. 労働所得の不平等が拡大するのか緩和されるのかという評価
3. 組織のAI統合が、意思決定階層の間で整合するかどうか

AI Nativeな社会設計では、「AIが仕事を奪うか」という一様な問いは成立しない。どのタスクが形式化でき、どの指標で成果を測り、どの層で統合を設計するかが、帰結を左右する。したがって設計の出発点は、技術の能力ではなく**タスク構造の分解**と**評価指標の明示**に置くべきである。

## メカニズム

このコンセプトは、対象を人間・AI・組織・技術のいずれに入れ替えても成り立つ構造として整理できる。

### 1. 代替と補完の境界

- 形式化可能な要素が多いタスク構造では、自動化主体(AI・機械・ルールエンジン)による代替が進みやすい。
- 形式化しにくい要素(文脈判断、暗黙知、状況理解)が残るタスク構造では、補完・拡張の関係になりやすい。
- 境界はタスクの**構成**で決まり、職業や機能の名称では決まらない。同じ「AI導入」でも、対象タスクの構造が違えば帰結は異なる。

### 2. 指標依存性と複数均衡

- 自動化の分配効果は、どの不平等指標(技能間・技能内・経済全体)で見るかによって、拡大とも緩和とも読める。
- 生産性経路(需要側)と労働時間調整経路(供給側)が併存するため、同一の仕組みの下でも複数の均衡が共存しうる。
- 単一の指標で成否を判定すると、設計を誤るおそれがある。

### 3. 階層的アライメント

- 自動化の成否は個々の技術性能だけでは決まらず、戦略・業務プロセス・現場実行といった意思決定層が整合しているかどうかに依存する。
- 層間の整合が欠けると、パイロット段階で止まる。

## 理論的背景

**タスクベースの自動化・拡張理論(ソース2)**
製造とマーケティングを対象とした概念的文献レビューで、労働経済学・イノベーション管理・組織行動論の知見を統合している。AIの拡大を「一様で不可避な労働代替」とみる公的言説を批判的に検討し、機能ごとにタスク構造が異なることに着目する。抜粋から確認できるのは、製造業のタスク構造が相対的に形式化しやすいという指摘までである。このソースの核心的知見は、形式化可能なタスクの有無が、自動化導入時の労働市場への帰結を決めるというものだ。

**デジタル化と労働所得の不平等(ソース3)**
能力の異なる労働者の職業選択を内生化した成長モデルである。デジタル化の影響を、(i) 自動化を通じた経済成長への作用と、(ii) 労働生産性(需要側)および労働時間の調整(供給側)を通じた労働所得の不平等への作用に分けて分析する。技能労働者と非技能労働者の間、各技能グループ内、経済全体の賃金不平等を検討し、デジタル化が格差を悪化させるか緩和するかは、採用する不平等指標に依存すると結論づける。ソースの核心的知見によれば、複数の均衡が共存しうる。

**AI統合の階層的アライメント(ソース1)**
PRISMAに沿った系統的文献レビューとデザインサイエンスによる成果物構築を組み合わせた研究である。多くのAI施策が、ユースケースをワークフロー、データ・プラットフォーム基盤、ガバナンス、変革実行に結びつける、オペレーション中心の戦略的統合ロジックを欠いたためにパイロット規模で停滞していると指摘する。レビューから7つの意思決定領域と、戦略から実行までのサイクルを導出している。核心的知見は、AI統合の成功には意思決定層の階層的アライメントが必要だという点である。

**不確実環境での分散知識の統合(ソース4)**
ノルウェーの深海漁業船団におけるFisk 4.0プロジェクトの実務者視点から、AI Copilotが組織的知識創造をどう支えうるかを探る研究である。不確実性と分散した専門性を特徴とする現場では、実務者が複数の情報源を解釈し、役割を越えて調整し、行動の前に状況理解を形成する必要がある。この知見は、形式化しにくい判断が残る領域で、AIが補完的に働く条件を考える手がかりになる。

**規制環境でのアジャイル実装(ソース5)**
FDA関連の医療機器開発を対象にLean・Agile・ハイブリッド手法の実装を調べたスコーピングレビューである。規制環境での実装はドメイン固有のトレードオフであり、構造は不変だが機序の説明は薄い(Tier 2)と位置づけられる。本コンセプトに対しては周辺的な参照にとどまる。

## AI Nativeな設計への示唆

1. **タスク単位で分解する**:職業や部門ではなく、タスクごとに形式化可能性を評価し、代替候補と補完候補を分ける。
2. **複数の指標で評価する**:不平等や成果を単一指標で判定せず、技能間・技能内・全体など複数の観点を併記する。
3. **形式化しにくい判断を残す設計にする**:暗黙知や状況理解の領域は、代替ではなく補完(Copilot型)を前提に設計する。
4. **階層で整合させる**:戦略、業務プロセス、データ基盤、ガバナンス、変革実行を一貫した統合サイクルとして設計し、パイロットで止まる事態を避ける。
5. **均衡の多重性を前提にする**:政策や組織設計は、望ましい均衡へ誘導するための指標選択と介入の設計として扱う。

## 関連コンセプト

- [[task-standardizability-determines-substitution-boundary]] — タスク標準化可能性が代替境界を決めるという、本コンセプトの中核的な関係
- [[ai-automation-labor-market]] — 自動化が労働市場に及ぼす影響
- [[automation-augmentation-paradox]] — 自動化と拡張の緊張関係
- [[ai-driven-automation-and-workforce-transformation]] — 自動化に伴う労働力の変革
- [[multilayer-interaction-determines-adoption-outcomes]] — 多層の相互作用が導入成果を決める点で階層的アライメントと重なる
- [[automation-layer-elevating-residual-human-complexity]] — 自動化後に人間側へ残る複雑性
- [[capability-profile-based-task-allocation]] — 能力に基づく役割分担
- [[ai-automation-workflow]] — ワークフロー自動化の実装面

## 参考ソース

1. Lordt Becklines, Omar El-Gayar (2026)「Strategic Integration of AI for Data‑Driven Decisions and Automation in Operations Management」
   File: raw/papers/operations_management/strategic-integration-of-ai-for-datadriven-decisions-and-automation-in-operation.md
2. Gilbert Tolentino, Leah F. Quinto, Cherry Ann Marie H. Espelita, Andrea Gwyneth Atento, Gay Marie Teodosio (2026)「Artificial Intelligence and the Strategic Reconfiguration of Work: A Conceptual Analysis of Substitution, Augmentation, and Organizational Redesign in Manufacturing and Marketing」
   File: raw/papers/operations_management/artificial-intelligence-and-the-strategic-reconfiguration-of-work-a-conceptual-a.md
3. Jilei Huang, Yi Sun, Liyan Yang (2026)「Does Digitalization Widen Labor Income Inequality?」
   File: raw/papers/operations_management/does-digitalization-widen-labor-income-inequality.md
4. Irina-Emily Hansen, Ola Jon Mork, Paul Steffen Kleppe, Lars Andre Giske (2026)「AI Copilots and Knowledge Creation in Maritime Fishing Operations.」
   File: raw/papers/operations_management/ai-copilots-and-knowledge-creation-in-maritime-fishing-operations.md
5. Alliy Adewale Bello, Kelvin Ebo Rabbles, Victor Osemudiame, Benny Uhoranishema (2026)「Lean–Agile Product Development in FDA Relevant and Regulated Medical Device Contexts」
   File: raw/papers/operations_management/leanagile-product-development-in-fda-relevant-and-regulated-medical-device-conte.md
