# 訓練データ由来バイアスの埋め込みと動的安全ガバナンス

## 概要

生成AIシステムは、訓練データに含まれる規範・偏り・権力関係を内包する。その結果、特定の変異(言語、表現、話者など)に正当性を与え、別の変異を周辺化する。同時に、バイアス・公正・倫理・信頼・セキュリティといった責任あるAIの構成要素は互いに依存している。ひとつを個別に「解決」しても、他の側面に影響が波及する。したがってAIの安全は、一度で解決する静的な問題ではなく、動的な相互作用として継続的に統治すべき対象である。

AI Nativeな社会設計では、AIが言語・判断・意思決定の基盤を担う。基盤に埋め込まれた偏りは、利用のたびに再生産され規模を伴って広がる。そのため、次の2点が設計上の不変の前提となる。

- 偏りは訓練源から入り込み、出力を通じて再生産される。
- 安全・公正・信頼・セキュリティは統合的かつ動的に統治する必要がある。

本記事は、この二つの原理を、ソースが示す知見に沿って整理する。

## メカニズム

以下は、対象を人間・AI・組織・技術のいずれに置き換えても成り立つ構造的原理として整理したものである。

### 1. 学習源の規範の内包と正当性の付与

学習する主体(モデル、組織、個人)は、学習源の規範を吸収する。学習源で威信・権威を持つ変異は「標準」や「正しい」ものとして扱われ、それ以外は逸脱として扱われやすい。これは、学習源にある権力の非対称が、出力を通じて正当性の非対称に変換される過程である。

### 2. 周辺化の再生産

標準とされた変異が優遇されると、それ以外の変異は次のような形で不利益を被る(ソース[1]の分類による)。

- 性能格差
- ステレオタイプ化
- 収奪(appropriation)
- 消去(erasure)

出力が再び社会の言語・知識環境に流入するため、偏りは自己強化的に再生産される。

### 3. 相互依存する構成要素の統合的統治

責任あるAIの要素を個別領域に分断すると、要素間の依存関係が見えなくなる。ソース[2]は、これらを機能的に区別しつつ相互接続した一つのシステムとして扱う。

### 4. 静的解決から動的航行へ

安全を「解くべき問題」ではなく「航行(navigate)し続けるプロセス」とみなすと、統治は一回限りの対策ではなく、相互作用の中で均衡を保つ活動になる。ソース[3]は、システム内部に互いを牽制する要素を持たせる自己敵対的な設計を提案している。

### 5. 社会技術的なセキュリティ設計

セキュリティは技術部品だけでなく、データ・組織・ガバナンスを含む社会技術システムとして、ライフサイクル全体で設計される必要がある(ソース[4])。

## 理論的背景

### 標準AI生成言語イデオロギー(ソース[1])

Smithらは、LLMが標準言語イデオロギーを強化することを論じている。これは、特定の言語変異に他より多くの威信・権威・正当性が与えられる偏りである。論文は、生成AIがこのイデオロギーをどう再生産し、どんな社会的含意を持つかを示す、社会技術的に基礎づけられたファセット型の分類体系を提示する。あわせて「標準AI生成言語イデオロギー」という概念を導入し、AIが特定の言語変異に正当性を与えつつ他を周辺化する仕組みを説明する。

また、望ましいシステム挙動をめぐる緊張も論じられている。生成AIがさまざまな言語変異を模倣しようとすることにも、模倣を拒否することにも、それぞれ利点と欠点がある。単純な正解はなく、権力関係を踏まえた判断が必要になる。

### BEETSフレームワーク(ソース[2])

Tettegahは、AI倫理研究でバイアス・公平性・倫理・信頼・セキュリティが別領域に分断されている問題を指摘する。そのうえで、これらを相互依存する一つのシステムとして再編する概念的枠組みを提示している。これは実証研究ではなく理論的な貢献である。各要素の役割は次のとおり。

- **Bias(バイアス)**: 構造的リスクを特定する
- **Equity(公平性)**: 規範的な目標を定める
- **Ethics(倫理)**: 説明責任を運用可能にするガバナンス層
- **Trust(信頼)**: 関係的な成果として生じる
- **Security(セキュリティ)**: システムの完全性を維持する保護基盤

さらに、感情を下位の情動的な影響層として位置づける点が、この枠組みの中心的な貢献とされる。

### WuXingアーキテクチャ(ソース[3])

古典中国の五行(木・火・土・金・水)の理論に着想を得た、AI安全ガバナンスの枠組みである。中核的な洞察は、安全は「解決される」問題ではなく「航行される」動的プロセスだという点にある。システム理論、サイバネティクス、複雑系科学に基づく哲学的基盤の論文と、アーキテクチャ設計・コード実装・テストデータ・性能評価を含む技術白書の二本で構成される。技術白書では60件の実テストケースで迎撃率100%が報告されているが、被引用数0の単独著者による初期の成果であり、一般化には追加の検証が必要である。

### 社会技術的セキュリティ設計(ソース[4])

Kindongらは、AI対応のエネルギー管理システム(EMS)を対象に、デザインサイエンス研究のアプローチで、セキュリティ課題への概念的枠組みを構築している。学術文献と実務文献の分析に基づき、ライフサイクルの視点を取る。対象はエネルギー領域だが、複雑な技術システムのセキュリティ設計における社会技術的課題という構造は、他領域にも適用できる。

### 言語学習への応用(ソース[5])

Wuは、韓国語学習における生成AIの概念的ナラティブレビューで、聴く・話す・読む・書く技能の支援が、韓国語の音韻・形態・語用論や学習者の目的に沿って設計されたときに有効になると述べる。一方で、文化的・語用論的な正確さ、幻覚的な表現、評価などに課題があると指摘している。価値は、文化的正確性と倫理的ガバナンスの設計によって決まる。

## AI Nativeな設計への示唆

1. **「標準」の前提を可視化する**: 何を標準・正しい出力とみなしているかを、設計時に明示する。言語変異の模倣の可否は、利点と欠点の両面から、影響を受ける話者との関係で検討する。
2. **偏りの4類型で評価する**: 性能格差、ステレオタイプ化、収奪、消去を、評価の観点として使う。
3. **要素を分断せず統合して統治する**: バイアス、公平性、倫理、信頼、セキュリティを一つのシステムとして扱い、ある対策が他の要素に与える影響を継続的に確認する。
4. **静的な認証から継続的な航行へ**: 安全を一度きりの達成条件にせず、動的な相互作用として監視・調整し続ける。内部に牽制機構を持たせる自己敵対的な設計は有力な候補である。ただし実証は限定的である。
5. **ライフサイクル全体でセキュリティを設計する**: データの収集から運用までを、技術と組織・ガバナンスを含む社会技術システムとして捉える。
6. **領域固有の文化的正確性を組み込む**: 教育などの応用領域では、文化的・語用論的な正確さと倫理的ガバナンスを、導入設計の一部として扱う。
7. **権力関係を設計の対象にする**: 偏りは技術的誤差ではなく権力の非対称に根ざすため、技術的修正とあわせて、誰が基準を決めるかというガバナンスの問題として扱う。

## 関連コンセプト

- [[ai-safety-and-governance]] — AIの安全性とガバナンスの全般的な枠組み
- [[ai-safety-governance]] — AI安全ガバナンス
- [[ai-bias-audits-and-red-teaming]] — バイアス監査とレッドチーム演習の統合。動的な安全統治の実践手段
- [[algorithm-auditing-and-bias]] — アルゴリズム監査とAIバイアス
- [[algorithmic-bias-fairness]] — アルゴリズムバイアスと公平性
- [[algorithmic-fairness-and-bias-detection]] — 公正性とバイアス検出
- [[bias-compounding-across-interacting-distortion-sources]] — 複数の歪み源の相互作用による偏りの累積・増幅
- [[code-switching-as-bias-indicator]] — LLMにおけるバイアス指標としてのコードスイッチング
- [[culturally-embedded-power-and-institutional-vulnerability]] — 文化に埋め込まれた権力関係と制度的脆弱性
- [[capability-perception-and-responsibility-diffusion-in-trust]] — 信頼と責任転嫁

## 参考ソース

1. Standard Language Ideology in AI-Generated Language — Genevieve Smith, Eve Fleisig, Madeline Bossi, Ishita Rustagi (2026)
   - File: raw/papers/complexity_science/standard-language-ideology-in-ai-generated-language.md
2. The BEETS framework for responsible artificial intelligence — Sharon Tettegah (2026)
   - File: raw/papers/complexity_science/the-beets-framework-for-responsible-artificial-intelligence.md
3. WuXing Architecture: A Self-Adversarial AI Safety Framework Based on Classical Chinese WuXing Theory — fuwenju (2026)
   - File: raw/papers/complexity_science/wuxing-architecture-a-self-adversarial-ai-safety-framework-based-on-classical-ch.md
4. Security by design in artificial intelligence-enabled energy management systems: a sociotechnical framework — Theodore Kindong, Gianluigi Viscusi, Björn Johansson (2026)
   - File: raw/papers/complexity_science/security-by-design-in-artificial-intelligence-enabled-energy-management-systems-.md
5. The Role of Generative Artificial Intelligence in Korean Language Learning: Applications, Challenges, and Instructional Strategies — Yundong Wu (2026)
   - File: raw/papers/complexity_science/the-role-of-generative-artificial-intelligence-in-korean-language-learning-appli.md
