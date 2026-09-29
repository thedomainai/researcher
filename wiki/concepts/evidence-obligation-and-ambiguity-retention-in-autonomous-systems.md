# 自律システムにおける証拠義務と曖昧性の保持

## 概要

自律システムは、識別情報の欠落や複雑な実行時状態に直面することが常である。従来のシステムは、この不確実性に対して、利用可能な情報から唯一の解釈を急速に確定することで対応してきた。しかし、この早期確定アプローチは、後発的に修正が困難な過誤決定や、システムの意思決定根拠の不透明化につながる。

**証拠義務と曖昧性の保持** は、この問題に対する原理的な対抗策である。その核心は、不完全な情報下であっても、複数の仮説を同時に保持し、実行時に検証可能な証拠を継続的に積み上げることで、最終的な判定の真実性と正当性を確保する構造である。

AI Nativeな設計において重要な理由は以下の通りである：

1. **機械学習システムの不確実性の特性化**：ニューラルネットワークやLLMは確率的出力を生み出し、複数の解釈が同時に妥当である状況を本質的に扱う。
2. **法的・倫理的責任の追跡可能性**：決定過程に複数仮説を記録することで、事後的な監査や説明責任が可能になる。
3. **動的環境での適応性**：新たな証拠が得られたときに、早期確定した判定の修正を容易にする構造。

## メカニズム

### コア構造：三層検証体系

**第1層：複数仮説の並行保持**

識別情報が不足した状態でも、複数の候補解釈を同時に保有する。各仮説に対して、信頼度スコア、適用可能な証拠、必要な追加検証を明示的に記録する。このプロセスは、人間の専門家判断、AI分類器の多クラス出力、確率的マッチング、いずれの対象でも同じ原理で機能する。

**第2層：実行時検証による状態真実性の担保**

システムが動作する過程で、各仮説に対する新たな証拠を継続的に収集する。証拠の蓄積により、仮説のスコアを動的に更新する。確定困難な場合は、追加的な観測や問い合わせをシステムに組み込み、検証の主動性を確保する。

**第3層：定量と定性判断の統合**

定量的な指標（スコア、確率、財務数値など）と定性的な解釈（ドメイン専門家の判断、テキストマイニング結果など）を同じ論理枠組みで結合する。単一の数値指標では捕捉できない複合的な状態を表現する。

この三層構造は、システムの対象（人間、AI、組織プロセス、技術インフラ）が何であれ、同一の原理で機能する。

## 理論的背景

### Suspense Management Framework の知見

Rakesh Kumar Jhaの研究は、金融機関における**識別情報不足が信号損失を引き起こす構造的問題**を分析した。保険料送金やペイメント処理では、識別子の欠落やタイミングのずれから、トランザクションが一時的に未分類状態（suspense）に置かれる。

従来の手動処理はこの状態を処理遅延の源泉と見なしていた。対照的に、提案されたAI/MLフレームワークは、自然言語処理で非構造化の送金記述を解釈し、**確率的マッチング** により、不完全な識別子下でも複数の正当なアカウント候補を並行保持する。モジュール式サービス層として既存システムに統合される。

核心的知見は、**複数仮説の同時検討により過度決定性を回復する**という点である。早期に唯一解に絞るのではなく、証拠が十分になるまで選択肢を開いておくことで、正確な適用が可能になる。

### ShenhuaAI の定量・定性統合

Shi と Zhu の ShenhuaAI は、コーポレートヘルスアセスメントにおいて、**RAG（検索拡張生成）+ ファジー集合論 + グラフ分析**を組み合わせた。788社の財務指標から34の定量指標を抽出し、LLM（Gemma 3 27B）が戦略的指標のための定性スコアを生成する。ファジー推論により、数値と言語記述を同じ推論空間で処理する。

実証結果は、高リスク企業の検出精度が86.7%、回帰モデルの R² = 0.647 に達した。この成功は、定量と定性の統合メカニズムが、単一のアプローチより複雑な因果構造をより良く捕捉することを示唆する。

### Runtime Verifiability と反シミュレーション層

Vadym Partasyuk の論文は、**複雑系の状態真実性を担保するための二重構造**を提唱した。Runtime Verifiability と Anti-Simulation Layer により、9つの証拠変数（介入遅延、制御権到達可能性、runtime suppression 負荷、リソース残余、述語的立場など）を明示的に追跡する。consequence-bearing systems（結果を伴うシステム）における証拠義務の枠組みを確立し、シミュレーションや虚偽の状態報告に対する防禦機構を構築する。

## AI Nativeな設計への示唆

### 設計原理1：証拠オブジェクトの明示化

意思決定に用いる各仮説に対して、仮説の内容、現在の信頼度スコア及びその根拠となった証拠リスト、仮説を棄却または強化するために必要な追加検証項目、時間軸上での証拠の蓄積履歴を明示的に構造化すること。この明示化により、[[evidence-based-management]] と [[evidence-projection-model]] の原理を具装化できる。

### 設計原理2：動的状態の暫定性明示

自律システムが出力する状態表現には、必ず「確実性レベル」を付加すること。確定済み、暫定保留、検証進行中、曖昧性保持中といった段階を明確に区別する。

### 設計原理3：検証の主動性確保

システムが自動的に追加情報を要求する能力を組み込むこと。不明な識別子に対する問い合わせ、足りない証拠カテゴリの能動的な探索、ドメイン専門家への限定的なエスカレーションを含む。

### 設計原理4：定量・定性の並行実行

機械学習ベースの定量判定と、ルールベースまたはLLMベースの定性判定を、同じ推論枠組み内で並行実行し、矛盾や補完関係を可視化すること。

## 関連コンセプト

- [[evidence-based-management]] — エビデンスベースドマネジメント
- [[evidence-projection-model]] — エビデンス・プロジェクション（証拠射影）モデル
- [[calibrated-multi-evidence-fusion]] — キャリブレーションされた多重エビデンス融合フレームワーク
- [[autonomous-multi-is-systems]] — 自律型マルチ情報システム
- [[temporal-erosion-of-procedural-legitimacy-under-opacity]] — 不透明性の累積露出による手続的正当性の時間的侵食

## 参考ソース

1. **Suspense Management Framework for Life & Annuities and Enterprise Financial Systems**
   著者：Rakesh Kumar Jha
   年：2026
   ファイルパス：raw/papers/accounting/suspense-management-framework-for-life-annuities-and-enterprise-financial-system.md

2. **ShenhuaAI: An LLM-powered software platform for multi-dimensional corporate health assessment in FinTech analytics**
   著者：Ruiyuan Shi, Wen Zhu
   年：2026
   ファイルパス：raw/papers/accounting/shenhuaai-an-llm-powered-software-platform-for-multi-dimensional-corporate-healt.md

3. **Runtime Verifiability and Anti-Simulation Layer: Evidence Obligations for Bounded Intervention, Predicate Standing, Suppression Debt, Resource Residual, and Systemic Enforcement**
   著者：Vadym Partasyuk
   年：2026
   ファイルパス：raw/papers/accounting/runtime-verifiability-and-anti-simulation-layer-evidence-obligations-for-bounded.md
