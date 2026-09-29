# 支援による負荷削減と学習に不可欠な負荷の分離

## 概要

支援系(AI、ツール、制度など)を設計するとき、「負荷を減らすこと」自体は目的にならない。減らすべきなのは学習や理解形成に寄与しない**外来的負荷**であり、理解が形作られる過程である**内在的な努力**は学習者の側に残す必要がある。この分離を誤ると、支援は成果物の品質を上げても、学習者の理解・記憶・当事者意識を損なう。

さらに、支援がうまく機能するかどうかは、支援ツール単体の性能だけでは決まらない。社会的影響が自己効力感などの**個人資源**を介して作用し、成果を左右する。加えて、**内発的動機**が支援技術の継続的な利用を支える。

AI Nativeな社会設計では、生成AIが下書き・整理・統合といった作業を大量に肩代わりできる。そのため「何をAIに任せ、何を人間に残すか」という線引きが、教育・知的生産・組織設計の中心的な設計問題になる。

## メカニズム

この原理は、対象を入れ替えても成り立つ構造として次のように整理できる。

1. **負荷の二分**:あらゆる作業には、課題そのものが要求する要素間の相互作用(内在的負荷)と、学習に寄与しない要求(外来的負荷)がある。支援の対象は後者に限定する。
2. **努力と理解形成の結合**:内在的な努力は、理解が形成される場そのものである。この努力まで代行すると、成果物は得られても、主体側に理解が蓄積しない。
3. **個人資源による媒介**:支援や社会的環境の効果は、主体の自己効力感やメンタルヘルスといった内的資源を経由して成果に現れる。同じ支援でも、主体の資源状態によって結果が変わりうる。
4. **動機による持続**:内発的動機が強いほど、支援技術の継続的な採用・利用が支えられる。外部からの誘因だけでは継続性が弱い。

この構造は「主体」を学習者、組織の構成員、あるいは人間とAIの協働系に置き換えても同型である。すなわち、(a) 代行してよい負荷と残すべき負荷を区別し、(b) 主体の内的資源を介した効果を考慮し、(c) 継続を支える動機構造を確保する、という三段構えになる。

## 理論的背景

### 認知負荷理論に基づく設計問いの定式化

Chauncey(2026)は、AI支援による研究執筆を題材に、「AIが減らすべき認知的要求はどれで、書き手自身の仕事として残すべきものはどれか」という設計問題を扱っている。生成AIは下書き・整理・統合の労力を肩代わりできるが、その労力こそ理解が形を取る場所だという指摘である。同論文は、AIに強く依存する書き手において、神経的関与の低下、自分の文章の想起の弱さ、著者性の感覚の低下を示す近年の実証研究に言及している。

理論的には[[cognitive-load-theory]]に依拠する。同理論は、課題が本質的に要求する要素間相互作用を**内在的負荷**、学習に寄与しない要求を**外来的負荷**として区別し、germane(学習に関連する)過程は、書き手が内在的負荷に割り当てるワーキングメモリ資源として扱う。この論文は、productive struggle(生産的な苦闘)や生成的学習の考え方も参照し、人間が関与する反復的なAIプロセスの枠組みを提示している。

### 社会的影響と個人資源の媒介

Bhunia & Alzahrani(2026)は、サウジアラビアの3つの公立大学の学生345人を対象に、社会的学習理論を基盤としたPLS-SEMによるモデルを検証した。媒介変数はAI自己効力感、スマートラーニング、学業ストレス、精神的ウェルビーイングである。10個の仮説はすべて支持され、社会的影響は学業成績に有意な直接効果(β = 0.156)を持ち、さらに有意な間接効果も観察された。つまり、社会的影響は個人資源を通じて成果に作用する。ここから、支援系の成否は支援の機能だけでなく、利用者の自己効力感などの内的状態にも依存するという示唆が得られる。

### 内発的動機と継続的採用

Oueslati ら(2027)は、自己決定理論(TAD)を用い、モバイルヘルス向けコネクテッドデバイスの採用意図を、内発的動機、外発的動機、無動機、知覚リスク、領域固有の革新性から検討した(407人の量的調査)。核心的知見として、内発的動機が継続的採用を外発的動機より強く規定することが示されている。支援技術を「使い続けたい」という内側からの動機が、継続性を支える。

## AI Nativeな設計への示唆

- **負荷の棚卸しを設計の起点にする**:タスクを内在的要素と外来的要素に分解し、AIが担う範囲を外来的負荷に限定する。書式整形や単純な整理は委ねうるが、理解を形成する統合や判断は人間側に残す。
- **生産的な苦闘を保存する**:人間が関与する反復プロセスを設計し、AIが答えを完成させるのではなく、学習者の思考を促す位置に置く。
- **理解の指標で評価する**:成果物の質だけでなく、想起、著者性の感覚、神経的関与といった学習側の指標を併せて確認する。
- **個人資源を支援対象に含める**:自己効力感やウェルビーイングを損なわない形で支援を導入する。周囲の社会的影響(教員・同僚・コミュニティ)も設計要素として扱う。
- **内発的動機を損なわない導入**:外的な誘因に頼らず、利用者が自律性を感じられる設計にすることで継続性を高める。

なお、ここで挙げた設計指針は、ソースの知見(特に Chauncey の理論的枠組み)から導かれる示唆であり、個別の実装効果を保証するものではない。

## 関連コンセプト

- [[cognitive-load-theory]] — 内在的・外来的負荷の区別の理論的基盤
- [[cognitive-load-optimization-framework]] — 認知負荷を最適化する設計枠組み
- [[distributed-cognitive-load]] — 人間とシステム間での負荷分配
- [[ai-assisted-software-development]] — 支援の線引きが問われる応用領域
- [[ai-feedback-attribution-learning]] — AIフィードバックと学習行動の関係
- [[effort-opacity-and-disclosure-signal-erosion]] — 努力の不可視化と評価シグナル劣化
- [[task-codifiability-determines-automation-outcomes]] — 代行可能なタスクの性質
- [[continuous-learning-ecosystems]] — 学習の継続性を支える環境

## 参考ソース

1. Anish Kumar Bhunia, Saeed Alzahrani (2026). "Social influence and academic performance: a serial mediation model in AI-enhanced learning". File: raw/papers/neuroscience/social-influence-and-academic-performance-a-serial-mediation-model-in-ai-enhance.md
2. Sarah A. Chauncey (2026). "Designing a human-in-the-loop AI iterative process for research writing: a framework for preserving productive struggle". File: raw/papers/neuroscience/designing-a-human-in-the-loop-ai-iterative-process-for-research-writing-a-framew.md
3. Yosra Oueslati, Azza Temessek–Behi, Leila El Kamel, Norchene Ben Dahmane Mouelhi (2027). "Motivations intrinsèque et extrinsèque comme déterminants de l'intention d'adoption des objets connectés en santé mobile". File: raw/papers/neuroscience/motivations-intrinsèque-et-extrinsèque-comme-déterminants-de-lintention-dadoptio.md
