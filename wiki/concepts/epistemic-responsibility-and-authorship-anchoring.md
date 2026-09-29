# 認識論的責任・著者性の人間への固定

## 概要

認識論的責任・著者性の人間への固定とは、AIの生成能力がどれだけ高まっても、**方向性の決定・責任の引き受け・検証の主体**は人間(または明確に特定可能な責任主体)に固定されなければならない、という不変原理である(Tier 1)。

この原理が重要な理由は、生成と検証の非対称性にある。生成のコストは急速に下がるが、出力が正しいかを判断する検証のコストはそれに比例しては下がらない。しかも検証を欠いた出力は、エラーや警告といった可視的な兆候を伴わずに失敗しうる(沈黙の失敗)。したがって、AI Nativeな社会・組織設計では、生成を拡張するだけでなく、「誰が方向を決め、誰が検証し、誰が責任を負うか」を構造として固定することが前提条件になる。

## メカニズム

この原理は、対象(人間・AI・組織・技術)を入れ替えても成立する次の三つの構造として整理できる。

1. **生成と検証の非対称性**
   任意の生成主体(人間、AI、組織、ツール)について、出力を生み出す能力と、その正しさを判定する能力は別のものである。生成側の能力が上がるほど、出力の量・速度・見かけの権威は増すが、検証を担う主体の能力が同じだけ増えるとは限らない。このずれが生じると、検証されない出力が既成事実として流通する。

2. **責任帰属の固定化**
   責任は「誰が生成したか」ではなく「誰がその出力を自らのものとして引き受けたか」で決まる構造でなければならない。生成手段が何であっても、成果を主張・採用する主体が責任と著者性を保持する。これが曖昧になると、責任は複数の主体やシステムの間で希薄化・転嫁される。

3. **沈黙の失敗(検出困難な誤り)**
   検証パイプラインは通常、目に見える異常を手がかりに作動する。しかし、失敗が「何も目に見えて悪くならない」という形で現れる場合、既存の検証機構では捕捉できない。このため、検証は事後的な異常検知に任せるのではなく、主体が能動的に行う責務として設計する必要がある。

## 理論的背景

### 方向性の内的決定と「方向性のアウトソーシング」

Matta(2026)は、外部知能の能力と遍在性が高まるほど、内的に根拠づけられた方向性決定の重要性が増すという「External Intelligence–Inner Direction Paradox」を提案している。また、タスク・認知・判断のアウトソーシングに続く第四の委譲水準として「方向性のアウトソーシング(directional outsourcing)」を導入している。外部システムが能力を増すほど、方向を自ら定める主体性を保持する必要性が高まるという逆説的関係が示されている。

### 沈黙の失敗と科学ソフトウェア

Weeks(2026)は、研究ソフトウェアにおけるAIエージェント活用で、無言の単位変換、保存則の破れ、幻覚的な物理、数値精度の喪失、静かに壊れる再現性といった失敗が起こりうると指摘する。これらは「何も目に見える異常が起きない」という共通の特徴を持ち、汎用的な評価では捉えられないとされる。同論文は、高リスクな科学ソフトウェアのワークフローにAIエージェントを統合するための、ツール非依存の方法論(Scientific Agentic Engineering)を提唱している。

### 著者性と認識論的責任

Chughtai(2026)は、テキストの生成と研究の遂行は同じではないと明言する。AI由来かどうかは本質ではなく、研究は研究者によって行われ、その研究者である著者によって書かれる。技術がどれほど高度でも、研究課題を遂行するのは研究者であり続ける。この立場では、著者性と認識論的責任は知識創造の本質的構成要素であり、生成はその十分条件ではない。

### 限定的な認知パートナーシップ

Milojević ら(2026)は、会計の意思決定におけるAIの関与を、自動化、分析支援、意思決定支援、専門的判断への対話的・高度な支援という4水準に整理した(2015年〜2025年11月の文献のうち11件を統合)。そのうえで、次段階として「bounded cognitive partnership」を提案する。ここでAIは分析や選択肢の生成に能動的に寄与するが、最終判断と専門職としての説明責任は人間の意思決定者に残る。

### 補足的な知見

- Çırak(2026)は理学療法におけるAI活用のレビューで、倫理的・医療法的責任、専門職の自律性、人間による監督の限界と重要性を論点に挙げている。
- Nar Nge と Mulik(2026)は、アルゴリズムによるプロファイリングと自動意思決定が、責任、開示、透明性、目的制限といった従来の概念に困難をもたらすと論じている。
- D'Souza ら(2026)は科学画像の理解ベンチマークを扱い、証拠に基づく正当化(evidential justification)を含むタスク設計を論じている。これは検証可能性を評価対象に含める視点と接続する。

## AI Nativeな設計への示唆

- **責任主体の明示**:あらゆる成果物・意思決定について、最終的に引き受ける人間(または組織上の責任主体)を設計段階で特定し、記録する。
- **方向性は内部で決める**:目標設定や優先順位の決定を外部システムの提案に委ねきらず、人間が内的な根拠にもとづいて方向を定める余地と能力を保つ。
- **検証を生成と対にする**:生成量を増やす際には、検証の手順・担当・資源を同時に設計する。検証を欠く出力を最終成果として扱わない。
- **沈黙の失敗を前提にした検証**:異常検知に依存せず、ドメイン固有の不変条件(たとえば単位や保存則、再現性)を明示的に検査する仕組みを持つ。
- **役割の限定**:AIには分析や選択肢生成を担わせ、最終判断と説明責任は人間に残す「限定的な協働」を既定とする。
- **開示ルールの整備**:生成ツールの使用有無ではなく、内容に責任を負う主体が誰かを基準に、著者性と査読・レビューのルールを設ける。

## 関連コンセプト

- [[moral-responsibility-anchoring-in-decision-agents]] — 意思決定主体への責任の錨づけと分散の抑止
- [[responsibility-dilution-and-moral-status-symmetry]] — 多主体チームにおける責任の希薄化
- [[capability-perception-and-responsibility-diffusion-in-trust]] — 能力知覚と責任転嫁
- [[epistemic-agency-preservation-under-offloading]] — 認知オフロード下での認識的主体性の維持
- [[epistemic-labor-displacement-under-delegation]] — 委譲による認識的労働の代替と判断力の空洞化
- [[epistemic-authority-and-algorithmic-truth]] — 認識論的権威とアルゴリズム的真実
- [[llm-epistemic-risk-governance]] — 大規模言語モデルの認識論的リスクとガバナンス
- [[responsibility-as-irreversible-cost-internalization]] — 不可逆的コスト内部化としての責任

## 参考ソース

1. David (Daoud) Matta (2026)「The Inner-Directed Executive: Directional Outsourcing and the Preservation of Executive Authorship in the Age of Artificial Intelligence」
   - File: raw/papers/economics/the-inner-directed-executive-directional-outsourcing-and-the-preservation-of-exe.md
2. Victor Weeks (2026)「Scientific Agentic Engineering: A Framework for Reliable AI Agents in Research Software」
   - File: raw/papers/economics/scientific-agentic-engineering-a-framework-for-reliable-ai-agents-in-research-so.md
3. Hameed Chughtai (2026)「On Generating Text: Editorial Guidance on Generative and Agentic AI for Authors and Reviewers」
   - File: raw/papers/economics/on-generating-text-editorial-guidance-on-generative-and-agentic-ai-for-authors-a.md
4. Stefan Milojević, Srđan Lalić, Marija Magdincheva-Shopova (2026)「From automation to bounded cognitive partnership: a functional framework of artificial intelligence in accounting decision-making」
   - File: raw/papers/economics/from-automation-to-bounded-cognitive-partnership-a-functional-framework-of-artif.md
5. Nilgün Çırak (2026)「Artificial Intelligence in Physiotherapy and the Limits of Clinical Reasoning: A Narrative Review」
   - File: raw/papers/economics/artificial-intelligence-in-physiotherapy-and-the-limits-of-clinical-reasoning-a-.md
6. Jennifer D'Souza ほか (2026)「A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientific Images」
   - File: raw/papers/economics/a-pathway-to-general-purpose-scientific-ai-multimodal-comprehension-of-scientifi.md
7. Su Yada Nar Nge, Prashant Rao Mulik (2026)「Data Protection Laws in the Age of Artificial Intelligence」
   - File: raw/papers/economics/data-protection-laws-in-the-age-of-artificial-intelligence.md
