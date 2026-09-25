# 分散認知インフラストラクチャ

## 概要

**分散認知インフラストラクチャ（Distributed Cognition Infrastructure）** は、認知的活動が個人の頭の中に閉じるのではなく、人間・AI・道具・環境に分散して実現されるという原理に基づく組織設計の枠組みです。

従来の組織設計では、意思決定や学習といった認知的活動を個々の人間の能力に帰属させてきました。しかし現代のAI Native社会では、このモデルは不十分です。複雑な問題解決は、個人の認知能力を超えた、複数のエージェント（人間・AI・システム）と物的環境が協働する中でのみ成立します。

このインフラストラクチャを組織に埋め込むことで、組織全体としての認知能力を飛躍的に拡張できます。同時に、AI導入による機械的な自動化の罠を回避し、人間とAIが相互に補完する関係を構築することができます。

## 理論的背景

### 状況的認知と学習文化

Brown, Collins, Duguidの研究（1989）は、従来の教育が「抽象化された知識」を前提としてきたことの限界を指摘しました。知識は学習される状況から切り離された形では機能しないというこの知見は、組織設計にも深刻な示唆を持ちます。

これは、AI導入時に単に「AIツールを配置すれば組織の認知能力が向上する」という単純な仮定の危険性を示唆しています。ツールは使用される状況・文脈・社会的実践の中に埋め込まれてこそ意味を持つのです。

### 野生の認知とナビゲーション

Hutchinsの『Cognition in the Wild』（1995）は、認知がいかに社会的・物的環境に分散しているかを実証的に示しました。船舶の航海における認知は、個々の船乗りの頭の中ではなく、チャート・計器・言語・相互作用のネットワークの中に分布しています。

この視点から見ると、現代の組織における認知は以下のように分散しています：

- **人間的認知**: 経験、直感、文脈理解
- **AI的認知**: パターン認識、大規模データ処理、予測
- **道具的認知**: システムが体現する組織的知識、標準化された手順
- **環境的認知**: 物理的・デジタル的配置が誘導する行動パターン

### 予測機械としての脳と拡張された認知

Andy Clarkの最近の仕事（2013）は、脳を「予測機械」と捉え、その予測能力は外部環境の構造を積極的に利用することで拡張されることを示しています。これは、組織が意図的に「予測可能な環境」を設計できることを示唆しています。

具体的には、AI予測、フィードバックシステム、意思決定支援ツール、データダッシュボードなどが、人間の予測能力を拡張する環境として機能します。

## AI Nativeな設計への示唆

### 1. 認知タスクの意図的な分配

分散認知の原理から、組織設計では以下のような問いが必要になります：

- **どの認知タスクは人間が担うべきか**：文脈理解、価値判断、創造的問題設定
- **どのタスクはAIが担うべきか**：パターン認識、大規模データ統合、初期段階の提案生成
- **どのタスクはシステムが標準化すべきか**：反復的な判断基準、監査ログ、ワークフロー

重要なのは、各エージェントの強みが補完し合う構造です。AIが人間の判断を完全に置き換える「自動化」ではなく、人間の判断能力をAIが拡張する [[mixed-initiative-orchestration]] 構造を目指します。

### 2. 環境設計による認知支援

状況的認知論から、組織の物理的・デジタル的環境は単なる「背景」ではなく、認知能力の一部として機能します。AI Native設計では：

- **情報可視化**: 複雑な意思決定に必要なデータを、状況に応じた形で表示
- **決定サポート**: 個々の判断ポイントにおいて、必要な情報とAI予測を同時に提示
- **学習環境**: 組織成員が状況的な専門性を発展させられるような環境構成

例えば、医療現場でのAI導入は、単に診断AIツールを配置することではなく、臨床医の判断が磨かれる環境—複数の医師による協議、患者の個別事情の可視化、長期的な予後追跡—を同時に設計することが重要です。

### 3. 社会的相互作用の構造化

Hutchinsの研究が示すように、分散認知は人間同士の相互作用を通じて機能します。AI導入時には、この相互作用を阻害しないことが重要です：

- **共有理解の形成**: AIの推論過程を人間が理解し、AIが人間の価値観を把握する双方向性
- **対話的改善**: 単なる人間によるAI出力の監視ではなく、相互学習的な関係構築
- **説明責任の連鎖**: AI→人間→組織→社会への説明責任が一貫している構造

これは [[human-centered-value-alignment]] と密接に関連しています。

### 4. 道具と実践の共進化

AIツールは導入時点で「完成品」ではなく、使用される実践の中で変形・適応していきます。組織設計では：

- **実験的運用**: 最初から最適な配置を期待せず、改善サイクルを組み込む
- **ローカル・カスタマイズ**: 組織の文脈に応じた調整を可能にする柔軟性
- **学習機構**: 実運用から得られた知見を組織的に蓄積・改善する仕組み

## 関連コンセプト

- [[human-centered-value-alignment]]: 分散認知インフラが機能するには、異なるエージェント間の価値観の整合が必須
- [[mixed-initiative-orchestration]]: 人間とAIの役割分担を動的に調整する設計原理
- [[cognitive-load-redistribution]]: 認知負荷を人間・AI・システム間で最適に配分
- [[adaptive-niche-construction]]: 組織が環境を積極的に設計し、認知的ニッチを構成すること
- [[resilient-sociotechnical-design]]: 人間とテクノロジーの共進化による回復力ある組織

## 参考ソース

- Brown, J. S., Collins, A., & Duguid, P. (1989). "Situated Cognition and the Culture of Learning." *Educational Researcher*, 18(1), 32-42. [raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md]

- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press. [raw/papers/cognitive_science/cognition-in-the-wild.md]

- Clark, A. (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science." *Behavioral and Brain Sciences*, 36(3), 181-204. [raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md]

- Wilson, M. (2002). "Six views of embodied cognition." *Psychonomic Bulletin & Review*, 9(4), 625-636. [raw/papers/cognitive_science/six-views-of-embodied-cognition.md]

- Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., & Nushi, B. (2019). "Guidelines for Human-AI Interaction." *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*. [raw/papers/hci/guidelines-for-human-ai-interaction.md]

- Horvitz, E. (1999). "Principles of mixed-initiative user interfaces." *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. [raw/papers/hci/principles-of-mixed-initiative-user-interfaces.md]