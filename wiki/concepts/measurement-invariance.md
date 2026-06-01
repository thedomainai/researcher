# 測定不変性

**測定不変性（Measurement Invariance）**とは、異なるグループ（国、文化、性別、時間経過など）間で測定ツールや尺度が、同じ対象（潜在変数や合成変数）を同様に測定できているかを示す統計的性質です。

社会科学、経営学、マーケティング、情報システムなどの分野では、人々の「態度」「知覚」「行動意図」といった直接観察できない潜在的な概念（構成概念）を、複数の質問項目（インジケーター）を用いて測定します。異なるグループ間でこれらの測定値を比較したり、それらを用いた仮説検証を行ったりする際、測定不変性が確保されていなければ、得られた比較結果や分析結果が歪められ、誤った結論（ミスリーディングな結論）を導く危険性があります。

---

## 測定不変性の重要性と検証プロセス

異なる集団や多国籍な調査対象を比較する研究、あるいは既存の測定尺度を翻訳・修正して異なる母集団に適用する場合、分析の前提条件として測定不変性の検証が不可欠となります。

### 1. 測定モデルにおける不変性の必要性
管理学や情報システム分野の実験・調査研究では、クロンバックのα係数（Cronbach's alpha）や確認的因子分析（CFA）を用いて測定尺度の信頼性、収束妥当性、判別妥当性を確認することが推奨されています。これらに加えて、複数グループ間の比較分析を行う構造方程式モデリング（SEM）においては、測定モデルがグループ間で共通の構造を持っていること（測定不変性）が前提となります。

### 2. 共分散構造分析（共分散ベースSEM）と合成変数モデル
伝統的な共分散ベースSEM（CB-SEM）における「共通因子モデル（Common Factor Models）」では、測定不変性の検証手順が確立されています。しかし、近年普及している分散ベースSEMである**部分最小二乗回帰（Partial Least Squares: PLS）経路モデリング**で多用される「合成変数モデル（Composite Models）」においては、共通因子モデルとは異なる不変性検証アプローチが必要とされていました。

### 3. MICOM（Measurement Invariance of Composites）プロシージャ
合成変数モデルにおける測定不変性を検証するため、Henselerら（2016）は**MICOM**と呼ばれる新しい3ステップの検証手順を提案しました。これにより、PLS経路モデリングなどの分散ベースSEMにおいても、測定不変性を体系的に検証することが可能になりました。

MICOMプロシージャは以下の3つのステップから構成されます。

1. **設定不変性（Configural Invariance）の検証**
   * すべてのグループにおいて、測定モデルの設定（インジケーターの割り当て、アルゴリズムの設定など）が同一であることを確認します。
2. **合成不変性（Compositional Invariance）の検証**
   * グループ間で合成変数のスコアが同様に作成されているか（重みの比率が等しいか）を検証します。これが満たされない場合、グループ間で異なる概念を測定していることになります。
3. **平均値と分散の同等性（Equal Means and Variances）の検証**
   * 合成変数の平均値と分散がグループ間で同等であるかをテストします。

MICOMにより「完全な不変性」または「部分的な不変性」が確認されて初めて、グループ間での経路係数などの比較（マルチグループ分析：MGA）が統計的に正当化されます。

---

## 関連概念

* [[構造方程式モデリング]]（Structural Equation Modeling: SEM）
* [[部分最小二乗法]]（Partial Least Squares: PLS）
* [[確認的因子分析]]（Confirmatory Factor Analysis: CFA）
* [[妥当性と信頼性]]（Validity and Reliability）

---

## 参考ソース

* Jörg Henseler, Christian M. Ringle, Marko Sarstedt (2016). "Testing measurement invariance of composites using partial least squares". *Information Systems*.
* Gordon W. Cheung, Helena D. Cooper–Thomas, Rebecca S. Lau, Linda C. Wang (2023). "Reporting reliability, convergent and discriminant validity with structural equation modeling: A review and best-practice recommendations". *Information Systems*.