# 部分的最小二乗法構造方程式モデリング

**部分的最小二乗法構造方程式モデリング（Partial Least Squares Structural Equation Modeling: PLS-SEM）**は、観測変数と潜在変数の間の複雑な因果関係をモデリングするための共分散・分散ベースの多変数解析手法です。

従来の共分散構造分析（CB-SEM）が「理論の検証や適合度の最大化（説明）」を重視するのに対し、PLS-SEMは「予測」と「因果関係の解明」を同時に行う「因果予測（causal-predictive）アプローチ」として位置づけられています。情報システム、マーケティング、人間行動、人的資源管理（HRM）など、社会科学やビジネス分野で広く採用されています。

---

## 主な特徴と技術的進展

PLS-SEMは、柔軟なモデル設定が可能であり、データの正規分布仮定を必要としないなどのメリットを持つ一方で、統計的偏り（バイアス）の克服やモデル検証手法の確立に向けて、近年多くの方法論的アップデートが行われています。

### 1. 予測精度の評価（PLSpredict）
従来のPLS-SEMでは、モデルの評価を主に決定係数（$R^2$）などの説明力指標に依存しており、真の予測性能（未知のデータに対する予測力）を適切に評価できていないという課題がありました。これを解決するために導入されたのが **PLSpredict** です。
* **ホールドアウト検証の導入:** データを訓練データとテストデータに分割し、ケースレベルでの予測誤差を測定します。
* **実務的ガイドラインの確立:** 反射的（Reflective）および構成的（Composite/Formative）モデルの双方において、項目レベル・潜在変数（構成概念）レベルでの堅牢な予測評価を可能にしました。

### 2. 測定不変性の検証（MICOMプロシージャ）
多国籍研究や異なる属性グループ（国籍、業界、世代など）を比較する際、測定モデルがグループ間で同一の解釈性を持っているか（測定不変性）を保証する必要があります。
* 構成概念に基づく（composite-based）モデル向けに、**MICOM（Measurement Invariance of Composite Models）** と呼ばれる3ステップの検証手順が開発され、グループ比較における誤謬を防ぐための業界基準となっています。

### 3. 一貫性のあるPLS（Consistent PLS: PLSc）
反射的指標（Reflective Indicators）を用いたモデルにおいて、従来のPLSはパラメータ推定値にわずかなバイアス（不完全な一貫性）が生じる弱点がありました。
* **PLSc（Consistent PLS）** の導入により、反射的構成概念に対する推定値の補正が行われ、共分散構造分析（CB-SEM）に匹敵する一致性（Consistency）を持つパラメータ（パス係数、指標負荷量、構成概念間相関）を算出できるようになりました。特に、データが非正規分布である場合に有効です。

### 4. 高次構成概念（Higher-Order Constructs）のモデリング
抽象的な高次次元（例：顧客満足度）と、その下位にある具体的な多次元要素（例：サービスの質、製品の質、価格への満足）を体系的にモデリングするためのアプローチです。
* **反復指標アプローチ（Repeated Indicators Approach）** や **2段階アプローチ（Two-Stage Approach）** を用いて、高次構成概念の信頼性と妥当性を正しく指定・評価・検証するための厳密なガイドラインが整理されています。

### 5. 未観測の不均一性の特定（FIMIX-PLS）
データ全体を一つの均一な集団（シングルグループ）として分析すると、内部に潜む異なる特性を持つセグメント（未観測の不均一性：Unobserved Heterogeneity）を見落とし、結果を歪める原因になります。
* **FIMIX-PLS（Finite Mixture Partial Least Squares）** を用いることで、データ内に存在する潜在的なセグメントを統計的に特定し、個別のグループモデルとして扱うことで、分析の精度を高めることができます。

---

## 関連概念

* [[共分散構造分析]] (CB-SEM)
* [[構造方程式モデリング]] (SEM)
* [[多変量解析]]
* [[測定不変性]] (Measurement Invariance)
* [[ホールドアウト検証]] (Holdout Validation)

---

## 参考ソース

* Predictive model assessment in PLS-SEM: guidelines for using PLSpredict (Galit Shmueli et al., 2019)
* Partial Least Squares Structural Equation Modeling (Marko Sarstedt et al., 2017)
* How to Specify, Estimate, and Validate Higher-Order Constructs in PLS-SEM (Marko Sarstedt et al., 2019)
* Testing measurement invariance of composites using partial least squares (Jörg Henseler et al., 2016)
* Consistent Partial Least Squares Path Modeling1 (Theo K. Dijkstra & Jörg Henseler, 2015)
* Mirror, mirror on the wall: a comparative evaluation of composite-based structural equation modeling methods (Joseph F. Hair et al., 2017)
* Partial least squares structural equation modeling in HRM research (Christian M. Ringle et al., 2018)
* How to perform and report an impactful analysis using partial least squares: Guidelines for confirmatory and explanatory IS research (Jose Benitez et al., 2019)
* Rethinking some of the rethinking of partial least squares (Joseph F. Hair et al., 2019)
* Identifying and treating unobserved heterogeneity with FIMIX-PLS: part I – method (Joe F. Hair et al., 2015)