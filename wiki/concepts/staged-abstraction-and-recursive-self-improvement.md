# 段階的抽象化と再帰的自己改善のループ構造

## 概要

段階的抽象化と再帰的自己改善のループ構造とは、(1)観測を位相・幾何・記号といった段階を経て明示的な記号表現へ変換する構造、(2)ハーネス(エージェントの実行環境)とモデルを入れ子にして繰り返し改善するループ構造、の2つを一つの原理として捉える考え方である。ソースが示す共通の含意は、どちらも**失敗診断の精度**と**フィードバック源の限界**によって効果が規定される、という点にある。

AI Nativeな社会設計でこれが重要なのは、AIシステムが「潜在パラメータに埋め込まれた不透明な知識」から「検査・操作できる表現」へ移行し、さらに自らの改善過程まで改善し始めているためである。抽象化の段階を明示すれば検証点が生まれ、改善ループの診断精度とフィードバック源を設計すれば、自律性を拡張しつつ統制を保てる。

## メカニズム

対象を人間・AI・組織・技術のどれに置き換えても成立する構造として、次の4要素に整理できる。

1. **段階的抽象化**:粗い構造(位相)から量的な形(幾何)、そして操作可能な記号へと、情報を段階的に変換する。各段階が中間表現となり、検査や介入の足場になる。
2. **入れ子のフィードバックループ**:内側のループが一方の要素(例:ハーネス)を改善し、外側のループがもう一方(例:モデル)を改善する。内側の成果が外側の学習経験を形づくり、外側の学習が内側の新たな改善機会を生む。
3. **失敗診断の精密性**:観測された失敗が、モデル固有の欠陥なのか、システム(ハーネス)側の体系的欠陥なのかを切り分けられなければ、個別の失敗に過適合した無駄な修正が生じる。
4. **自律性の段階的拡張**:改善の実行、戦略、経験獲得、環境適応、再帰的メタ改善へと、任せる範囲を段階的に広げる。各段階の有効性は、利用できるフィードバック源(人間のフィードバックなど)の範囲に縛られる。

## 理論的背景

### 観測から記号表現へ:NeuSOGA

NeuSOGA(Qingde Li, Qingqi Hong, Jie Tian, 2026)は、ニューラルな知覚能力が潜在パラメータに符号化されて検査しにくいという課題を出発点に、観測を位相的抽象、幾何的抽象、そして記号的な数学表現へと段階的に変換するフレームワークを提案する。核心は、記号化を一挙に行うのではなく、構造的な段階として実現する点にある。

### 知覚の記号化と推論の安定性

Dai らの研究(2026)は、図形をシンボリックな形に変換する Geometric Vision Parser と、形式的演繹を行う Symbolic Solver を、純粋なLLMに組み合わせる枠組みを示した。著者らは、これが最先端のLMMに匹敵し得ること、幻覚を抑え解釈可能な推論を促すことを報告している。視覚知覚を記号へ落とすことで推論が安定する、という知見である。

### 自律性の段階的進化:RSI

Duan らの研究(2026)は、再帰的自己改善(RSI)を、経験とフィードバックを、能力と将来の改善プロセスの双方を高める持続的変化へ変えることと定義する。ロードマップは、改善実行の自律性、改善戦略の自律性、経験獲得の自律性、環境適応の自律性を経て、再帰的メタ改善に至る。既存LLMの問題は Headroom-Closed Index(HCI)で示され、科学的発見・身体性知能・ソフトウェア工学など場面ごとに要件や発展速度が異なると論じている。

### 失敗診断とハーネス進化:Ecdysis

Ecdysis(Yue ら, 2026)は、既存のハーネス進化手法が反復探索に依存するため、実行と修正の時間的オーバーヘッドが大きく、観測したタスクや失敗パターンに過適合して未知タスクへの汎化が損なわれ得ると指摘する。その根本要因として「原理的な失敗診断の欠如」を挙げ、失敗がモデル固有の欠陥かハーネスの体系的欠陥かを区別しないまま個別の失敗を最適化すると、不要な修正を招くと述べる。

### 入れ子の再帰:ScienceBuddy

ScienceBuddy(Xue ら, 2026)は「recursive-in-recursive」な自己改善を掲げる。内側の再帰ではモデルを固定してハーネスを改善し、外側の再帰では改善後のハーネスの下でモデルを強化学習する。研究者の依頼・フィードバック・実行証拠は、継続学習のためのタスクと評価ルーブリックへ変換される。ソースの知見として、この段階的改善は人間フィードバックの限界の内側でのみ有効である点が整理されている。

## AI Nativeな設計への示唆

- **中間表現を明示する**:観測から意思決定までを、検査可能な段階(構造→形→記号)に分け、各段階で検証や人間の介入ができるようにする。
- **改善の前に診断を設計する**:失敗を「モデル起因」か「ハーネス起因」かに分類する層を設け、個別事例への過適合と無駄な修正を避ける。
- **ループを入れ子で設計し、役割を分ける**:内側(ハーネス)と外側(モデル)で、何を固定し何を更新するかを明確にする。
- **自律性は段階的に委譲する**:改善の実行から戦略、経験獲得、環境適応、メタ改善へと、フィードバック源が確保できる範囲でのみ拡張する。
- **フィードバック源を資源として管理する**:人間のフィードバックが上限を規定するため、その質と量を設計対象とし、依頼や実行証拠を評価ルーブリックへ変換する仕組みを持つ。

## 関連コンセプト

- [[feedback-loops-system-dynamics]] — フィードバックループの一般的な動態
- [[recursive-feedback-criticality-threshold]] — 再帰的フィードバックの臨界閾値と自己増幅
- [[self-monitoring-feedback-and-adaptive-plasticity]] — 内部状態の自己監視と適応可塑性
- [[reflexive-hypothesis-testing-loop-and-adaptive-learning]] — 仮説検証ループによる学習
- [[architecture-level-value-preservation-and-social-harness]] — 社会的ハーネスの設計
- [[explainability-and-human-governed-decision-loops]] — 人間統制下の意思決定ループ
- [[cognitive-infrastructure-and-recursive-tech-production]] — 技術の自己再帰
- [[decision-loops-and-layered-decentralized-control]] — 多層の意思決定ループ

## 参考ソース

1. Qingde Li, Qingqi Hong, Jie Tian (2026). *Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations*. File: raw/papers/human_ai_collaboration/neuro-symbolic-geometric-abstraction-neusoga-from-observations-to-symbolic-mathe.md
2. Weichen Dai, Rafael Medeiros Cabral, Ziyi Shou, Yan Cao, Xin Shen (2026). *From Symbolic Perception to Logical Deduction: A Framework for Guiding Language Models in Geometric Reasoning*. File: raw/papers/human_ai_collaboration/from-symbolic-perception-to-logical-deduction-a-framework-for-guiding-language-m.md
3. Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou (2026). *The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement*. File: raw/papers/human_ai_collaboration/the-last-ai-built-by-humans-toward-genuine-recursive-self-improvement.md
4. Ruiqing Yue, Yu Cui, Zhuoyu Sun, Sicheng Pan, Xianhong Xue (2026). *Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents*. File: raw/papers/human_ai_collaboration/ecdysis-efficient-and-effective-training-of-runtime-harnesses-for-llm-agents.md
5. Shuhan Xue, Jianyuan Zhong, Ziyuan Nan, Wenbin Li, Zhaochen Yu (2026). *ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents*. File: raw/papers/human_ai_collaboration/sciencebuddy-recursive-in-recursive-self-improvement-for-interactive-scientific-.md
