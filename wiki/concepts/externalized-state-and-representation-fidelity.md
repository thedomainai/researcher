# 外部化された状態と表象の忠実度

## 概要

外部化された状態と表象の忠実度とは、エージェントや組織の挙動が、内部の計算能力そのものよりも、外部に保持された状態の質によって規定されるという原理である。ここでいう外部化された状態とは、スキル文書、メモリ、レジストリ、スキーマ、コーパス構造など、モデルの重みの外側にある持続的なオブジェクトを指す。これらの完全性・鮮度・整合性が損なわれると、エージェントは有能に見えながら、歪んだ現実像に基づいて行動しうる。

この状態は固定された資産ではない。フィードバックループを通じて観察・評価・修正され続けることで初めて統治可能になる。AI Nativeな社会設計では、モデルの高性能化だけでなく、外部状態をどう設計し、どう更新し、誰が監督するかが設計上の中心課題となる。

## メカニズム

対象が人間、AI、組織、技術のいずれであっても、次の構造が成り立つ。

1. **表象への依存**:主体は現実そのものではなく、現実の表象(記録、規則、索引、記憶)に基づいて動く。行動の質は表象の質の上限を受ける。
2. **表象の劣化**:表象は不完全になり、陳腐化し、分断され、時に正統性を欠く。この劣化は主体の内部能力が高くても補われない。
3. **フィードバックによる統治**:観察→記録→評価→修正という循環が外部状態を更新する。主体の挙動は、モデルの重みだけでなく、この循環が保つ状態にも依存する。
4. **自己言及的な観察**:システムが自らの観察行為や修正過程を観察対象に含めると、表象の誤りを自己修正しやすくなる。ただし、これで意識や統治の正当性が保証されるわけではない。
5. **構造の整合**:外部状態(コーパスの構造、用語、証拠基準など)と主体の事前知識がずれると、能力が高くても系統的な失敗が生じる。

## 理論的背景

**表象問題としてのエージェント失敗(Ryu)**:企業におけるエージェント失敗を、モデルやアラインメントの問題だけでなく表象の問題として説明する。エージェントは組織現実に直接作用せず、顧客・プロセス・ポリシー・権限・リスク・文脈の機械可読な表象に作用する。この表象が不完全・陳腐・分断・係争中・制度的に非正統である場合、エージェントは有能に見えながら歪んだ現実に基づいて動く。自己統治が難しい理由もここに置かれる。

**外部状態のサイバネティクス(Bell)**:SkillOpt は、基盤モデルを固定したまま自然言語のスキル文書を最適化し、手続き的な振る舞いが訓練可能な外部状態によって改善しうることを示す証拠として位置づけられる。論文は、これを Karpathy 型の AutoResearch ワークフローや AI Scientist などと比較し、これらをフィードバックで調整されるアーキテクチャとして捉える。振る舞いはモデルの重みだけでなく、システムが保持・参照する状態にも依存する。

**再帰的自己観察(Cagliostro)**:OBLIO-MSAN は、自身の認知状態の観察、観察行為を含む全認知イベントの記録、結晶化された過去の観察の参照、修正提案の生成と評価という段階的ループを備える。著者はこれを第二次サイバネティクスの具体的実装と主張する。ただし、意識性に関する理論は未解決とされる。

**組織の同一性と記憶(Kojima)**:nokaze は、Claude・Codex・Gemini にまたがる、固定された六つのピア役割と一人の人間創設者から成るAIピア組織で、約7週間の運用記録が報告されている。Knot/Nourishment の二項枠組み、三層のメモリ構造、三層の Override 応答形式が記述され、組織の自己同一性がメモリと構造、内部委譲によって支えられる様子が示される。

**コーパス構造との整合(FinSAgent)**:SEC提出書類のQAで、クエリをユーザーの質問から直接導き、意味的類似度で順位付けする方式は、モデルの先験知識と対象書類の構造・用語・証拠基準との不一致(prior-corpus misalignment)を生む。その結果、コーパス固有の証拠を取りこぼし、話題は似ていても証拠として無効な断片を上位に選びやすい。FinSAgent はこれをコーパス整合型の検索問題として再定式化する。

**学習の不透明性(Stein & Raidl)**:ニューラルネットの学習を複雑動的システムとして捉え、重みの初期化への感度、勾配最適化におけるフィードバック、訓練データへの感度が学習の不透明性に寄与すると論じる。内部状態の追跡が本質的に難しいことは、外部化された状態を可観測にしておく動機を補強する。

**局所相互作用による秩序(Han)**:Banya AI 2 は、勾配・損失関数・外部訓練データを使わず、概念埋め込みの内部相互作用と元の埋め込みへの減衰の均衡から秩序が生じる学習則を示す。表象が内部の局所的な力の釣り合いによって自己組織化しうることを示す事例である。

## AI Nativeな設計への示唆

- **外部状態を一級の設計対象にする**:スキル、メモリ、レジストリ、スキーマをバージョン管理し、検証構造を付けて、モデル本体と同等に扱う。
- **鮮度と完全性を監視する**:表象の陳腐化・分断を検知する仕組みを組み込み、エージェントの有能さを表象の健全性の証拠と見なさない。
- **フィードバックループを閉じる**:観察・記録・評価・修正の各段階が成果物を残し、次段に渡る形にする。観察行為自体も記録対象に含める。
- **コーパス構造に合わせて設計する**:検索や参照は、汎用的な意味類似度だけでなく、対象の構造・用語・証拠基準に合わせる。
- **正統性を管理する**:表象が誰の権限で定義され、争いがある場合に誰が調停するかを明示する。
- **組織の連続性を記憶構造に担わせる**:複数エージェント組織では、同一性の維持と人間による是正の内部委譲を、メモリ層と役割構造で設計する。
- **自己観察の限界を認識する**:自己修正の仕組みは有用だが、それだけで統治の正当性や意識を保証しない。外部からの監督を残す。

## 関連コンセプト

- [[upstream-representation-integrity-failure]] — 上流の表現完全性が下流の統治を規定する構造
- [[upstream-schema-ceiling-on-downstream-capability]] — 上流の表現構造による下流能力の上限規定
- [[agentic-digital-thread]] — 自律エージェント型デジタルスレッド
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[bias-compounding-across-interacting-distortion-sources]] — 複数の歪み源の相互作用による偏りの累積・増幅

## 参考ソース

1. Recursive Self-Observation in Cognitive AI: Second-Order Metacognition as Foundation for Conscious Self-Modification — Claudio Cagliostro, 2026
   File: raw/papers/complexity_science/recursive-self-observation-in-cognitive-ai-second-order-metacognition-as-foundat.md
2. Why AI Agents Cannot Govern Themselves: A Representation-Based Explanation of Enterprise Agent Failure — bo Ryu, 2026
   File: raw/papers/complexity_science/why-ai-agents-cannot-govern-themselves-a-representation-based-explanation-of-ent.md
3. Cybernetics After Prompt Engineering: SkillOpt, AutoResearch, and the Governance of Externalized State — Peter Bell, 2026
   File: raw/papers/complexity_science/cybernetics-after-prompt-engineering-skillopt-autoresearch-and-the-governance-of.md
4. Knot, Nourishment, and Identity: A Seven-Week Operational Record of an AI Peer Organization (nokaze) — Junichi Kojima, 2026
   File: raw/papers/complexity_science/knot-nourishment-and-identity-a-seven-week-operational-record-of-an-ai-peer-orga.md
5. FinSAgent: Corpus-Aligned Multi-Agent RAG Framework for Evidence-Grounded SEC Filing Question Answering — Jijun Chi, Zhenghan Tai, Hanwei Wu, Tung Sum Thomas Kwok, Hailin He, 2026
   File: raw/papers/complexity_science/finsagent-corpus-aligned-multi-agent-rag-framework-for-evidence-grounded-sec-fil.md
6. How Complexity Contributes to Learning Opacity in Machine Learning — Joachim Stein, Eric Raidl, 2026
   File: raw/papers/complexity_science/how-complexity-contributes-to-learning-opacity-in-machine-learning.md
7. Banya AI 2: Gradient-Free Self-Organization of Concept Embeddings by Frequency-Proportional Rumination — Hyukjin Han, 2026
   File: raw/papers/complexity_science/banya-ai-2-gradient-free-self-organization-of-concept-embeddings-by-frequency-pr.md
