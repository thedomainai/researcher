# 検査コストと判断精度のトレードオフ配分

## 概要

価値の推定、検査、監査、評価、検知といった「判断のための情報取得」は、それ自体がコストを持つ。安価な手段は速いがノイズが大きく、正確な手段は高価である。したがって、どこまで精度に投資し、何を粗い推定に委ねるかという**配分問題**が必ず生じる。この構造は、AIモデルのルーティング、道路安全の監査、セキュリティスキャナの評価、教育における学習評価、法規制における「精度」の扱いなど、対象が変わっても繰り返し現れる。

AI Nativeな社会設計では、判断・検査・監査をAIが大量に担う。そのため「全件を精密に検査する」という前提は成り立たない。検査の粒度、対象、深さを明示的に設計対象とし、粗い推定と精密な検証をどう組み合わせるかを制度・アーキテクチャの水準で決める必要がある。

## メカニズム

対象(人間、AI、組織、技術)を入れ替えても成立する構造は、次の三つに整理できる。

### 1. 情報取得コストと最適停止

意思決定者は、複数の選択肢それぞれの価値を知らないまま選ぶ。価値を確かめる検査には費用がかかる。検査を続けるか、現在の推定で決めるかは、追加情報の期待価値(value of information)が検査コストを上回るかで決まる。古典的な「検査コスト付き最適探索」の枠組みであるPandora's Box問題が、この構造を形式化している。

### 2. カバレッジと精度のトレードオフ

限られた予算では、少数を精密に見るか、多数を粗く見るかを選ぶことになる。さらに、検査手段が「判断を出せない」場合(未対応、解析不能など)があると、精度指標だけでは全体像が見えない。判断が得られた範囲での精度と、そもそも判断が得られた範囲の広さは、別々に扱う必要がある。

### 3. 指標の代理性とグッドハートの法則

検査コストが高いほど、私たちは測りやすい代理指標に頼る。しかし代理指標は本来の目的と乖離しうる。指標が目標になると、指標を満たすこと自体が最適化され、本来測りたい対象が測れなくなる。この乖離は、教育でも法規制でも技術評価でも同じ形で生じる。

## 理論的背景

### Pandora's Boxとしてのルーティング(ソース1)

Fisch らは、複数のモデル、アーキテクチャ、ハーネス、推論時設定からなる異種AIシステムで、クエリを最も低コストで効果的に答えられる専門家へ振り分けるルーティングを扱う。ルーティングには各専門家の期待リターンの推定が必要だが、その推定にもコストがある。埋め込みベースの予測器のような安価な推定器は速いがノイズが大きく、検索結果や部分的な推論トレースにアクセスできる微調整モデルのような高精度の推定器は高価である。

論文はこのトレードオフを、検査コスト付き最適探索の古典問題であるPandora's Boxの一事例として定式化する。ガウス信号モデルの下では、方策は情報価値の閉形式で表され、各専門家と各入力について、推定を精緻化する価値がコストに見合うかを判定できるとされる。核心的な知見は、不完全情報下での検査コストと精度のトレードオフが普遍的な意思決定構造だという点である。

### 専門家との較正を先に置く監査(ソース2)

EG-ARSAは、低・中所得国での道路安全監査を対象とする。ここでは事故記録の不完全さ、資格を持つ監査人の不足、大規模な現地検査の高コストが制約になる。提案手法のExpert-Grounded Distillation(EGD)は、教師視覚言語モデルを権威ある現地監査に対して較正する段階を置く。専門家のリスク評価との十分な一致(Cohen's kappa = 0.74)に達した後にのみ大規模アノテーションを許可し、そこで得た構造化された教師信号を80億パラメータの生徒モデルに蒸留する。高価な専門家検査を少量に絞って「精度の錨」とし、安価なスケーラブル推定に知識を移すという配分の一形態と読める。

### カバレッジと失敗回復(ソース3)

Lan らは、MLアーティファクト向け静的スキャナ(ModelScan、ModelAudit、Fickling)を、145のサンプルファミリーにわたる170件のPickle/PyTorch系アーティファクトで評価した。従来の指標は「使える判断が得られたケース」しか特徴づけないと指摘し、非N/Aカバレッジ、解析完了、確定的セキュリティ判断、非セキュリティ所見、未対応結果を区別している。ラベル付き135ファミリーのうち、確定判断を出したのはModelAuditが135(100%)、Ficklingが110(81.5%)、ModelScanが67(49.6%)であった。確定判断を出した条件付きの精度だけでは検知システムの実力を語れず、カバレッジと失敗回復の指標が必要という示唆である。

### 代理指標の限界(ソース5、6)

- **教育評価(ソース5)**: エッセイ、問題演習、コード作成といった、理解の代理として機能してきた課題が、AIで表面的に生成可能になった。人為的な制約に依存する評価は、真の理解ではなく、順応、アクセス、隠蔽を測ってしまうおそれがあると論じられる。
- **精度の法的・技術的解釈(ソース6)**: 機械学習コミュニティでは精度向上が進歩の原動力である一方、その有用性や有効性の面での限界も認識されている。EU AI Actは高リスクAIのコンプライアンスで「精度」に言及するが、法の側は曖昧さを受け入れ、技術・社会の変化に対する解釈の余地を残している。両者が同じ言葉で別のものを指しうるという緊張が、五つの論点として整理されている。

### 形式検証による網羅的検査の回避(ソース4)

Zhang は、抽象解釈を用いたアルゴリズム的公平性の検証を提案する。データとアルゴリズムの本質的性質を抽象ドメインで表現することで、網羅的テストなしにバイアスを特定できるとする。全件検査のコストを、抽象化により下げる方向の一例である。ただし、このソースの知見は形式手法のアーキテクチャに依存する点に注意が必要である。

## AI Nativeな設計への示唆

1. **検査の価値を明示的に計算する**: 検査を一律に行うのではなく、入力ごと・対象ごとに「追加検査の期待価値がコストを上回るか」で深さを決める。ルーティングや監査の設計に、停止規則を組み込む。
2. **安価な推定と高価な検証を階層化する**: 粗い推定器を広く適用し、高価な検証は少数の較正用サンプルや不確実性の高いケースに集中させる。EG-ARSAのように、大規模適用の前に専門家との一致を定量的な関門として置く。
3. **カバレッジを精度と別に報告する**: 判断不能・未対応・解析失敗の割合を公開指標とし、精度が条件付きの数値であることを明示する。失敗時の回復手順も設計対象に含める。
4. **代理指標の陳腐化を前提にする**: AIが代理課題を容易に満たせる環境では、指標が本来の目的を測れているかを定期的に見直す。評価対象を成果物から、理解や能力を直接示す証拠へ移すことを検討する。
5. **指標の意味を分野間で揃える**: 技術と法制度が同じ用語(精度など)を別の意味で使う場合、解釈の幅を許容しつつ、どの前提で何を測るかを明示する。
6. **検査を形式的に安くする道を探る**: 抽象化や形式検証によって、網羅検査に頼らず性質を保証できる範囲を広げる。ただし適用範囲は手法の前提に依存する。

## 関連コンセプト

- [[contextual-intelligence-allocation]] — 文脈に応じて知能資源を配分するという、配分問題の姉妹的視点
- [[structural-separation-of-verification-from-governed-system]] — 検証機構を被統治系から分離する設計。検査の独立性とコストの両立に関わる
- [[opacity-verification-gap]] — 不透明性と検証可能性のギャップ。検査コストが高くなる背景
- [[human-verification-loop-bias-amplification]] — 人間による検証ループの設計上の落とし穴
- [[aggregation-induced-information-loss]] — 集約(粗い推定)で失われる情報
- [[llm-hardware-verification]] — 検証コストが問題となる具体的領域の一例

## 参考ソース

1. Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation — Adam Fisch, Shubhendu Trivedi, Fantine Huot, William W. Cohen, Michael Kaisers (2026)
   `raw/papers/ai_governance/pandoras-ai-model-routing-box-efficient-allocation-with-costly-value-estimation.md`
2. EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings — Md Thamed Bin Zaman Chowdhury, Moazzem Hossain (2026)
   `raw/papers/ai_governance/eg-arsa-an-expert-grounded-open-model-for-visual-road-safety-auditing-in-low-res.md`
3. Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners — Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal (2026)
   `raw/papers/ai_governance/beyond-f1-evaluating-coverage-and-failure-recovery-in-ai-model-security-scanners.md`
4. Algorithmic Fairness Verification via Abstract Interpretation — Jincheng Zhang (2026)
   `raw/papers/ai_governance/algorithmic-fairness-verification-via-abstract-interpretation.md`
5. Evaluation in the Age of AI: Output as Evidence of Learning — Md Zarzees Uddin Shah Chowdhury, Samin Rahman Khan (2026)
   `raw/papers/ai_governance/evaluation-in-the-age-of-ai-output-as-evidence-of-learning.md`
6. Law of Large Numbers: Accuracy as Statistical Measure for AI Compliance and Competition — Rabanus Derr, Alina Wernick, Robert C. Williamson (2026)
   `raw/papers/ai_governance/law-of-large-numbers-accuracy-as-statistical-measure-for-ai-compliance-and-compe.md`
