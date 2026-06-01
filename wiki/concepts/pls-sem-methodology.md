# 部分的最小二乗法構造方程式モデリング

**部分的最小二乗法構造方程式モデリング（Partial Least Squares Structural Equation Modeling: PLS-SEM）**は、観測変数と潜在変数の間の複雑な因果関係を同時に分析するための、分散ベース（Variance-based）の構造方程式モデリング（SEM）手法です。

経営学、社会科学、特に情報システム（IS）や新技術研究の分野で広く応用されています。共分散構造分析（CB-SEM）がモデルの適合度や理論の検証（確認）を重視するのに対し、PLS-SEMは**予測（Prediction）**や**理論の構築（探索）**に強みを持っています。

---

## 概要

PLS-SEMは、従来の共分散ベースのSEMと比較して、以下のような重要な特徴と利点を持っています。

1. **柔軟なデータ要件**
   厳しいデータ分布の仮定（多変量正規分布など）を必要とせず、小規模なサンプルサイズや二次データ（Secondary Data）の分析にも適しています。
2. **複雑なモデルの構築**
   多数の観測変数や潜在変数を含む複雑なモデルを、高い統計的検出力（Statistical Power）を維持しながら推定できます。
3. **反映指標と形成指標の双方に対応**
   潜在変数を測定するアプローチとして、反映的測定モデル（Reflective Measurement Models）と形成的測定モデル（Formative Measurement Models：複合変数をモデル化する構成体）の両方を柔軟に組み合わせることができます。

近年、評価基準の標準化やソフトウェア（Rパッケージなど）の普及に伴い、意思決定や予測精度の評価において不可欠な統計手法として定着しています。

---

## 詳細な知見と評価基準

近年（2010年代半ば〜2020年代）におけるPLS-SEMの研究発展により、分析手法や結果の検証・報告に関するガイドラインがアップデートされています。

### 1. 測定モデルと構造モデルの評価
PLS-SEMの分析結果を報告する際は、まず「測定モデル（Measurement Models）」の品質（信頼性と妥当性）を検証し、その後に「構造モデル（Structural Models）」の仮説検証や予測力を評価します。

* **測定モデルの品質評価（Confirmatory Composite Analysis: CCA）**
  測定モデルの品質を系統的に評価するためのアプローチとして、**確証的複合分析（Confirmatory Composite Analysis: CCA）**が提唱されています。これにより、因子（Factors）と複合体（Composites）の双方が正しく測定されているかを確認します。
* **判別妥当性の新しい基準**
  従来のFornell-Larcker基準に代わり、潜在変数間の判別妥当性をより厳密に評価する指標として、**HTMT（Heterotrait-Monotrait ratio of correlations）**が広く採用されています。

### 2. 予測精度の評価（PLSpredict）
PLS-SEMの最大の強みは「予測（Prediction）」にあります。モデルの適合度（Goodness-of-Fit）テストだけに依存するのではなく、サンプルの外挿予測力を評価する新規アプローチとして **PLSpredict** が導入されました。これにより、モデルが新しいデータに対してどの程度高い予測精度（Out-of-sample prediction）を持つかを客観的に評価できます。

### 3. 情報システム（IS）分野における活用
PLS-SEMは、複雑なモデル構成や形成指標を扱いやすい特性から、情報システム（IS）や新技術研究において特に支持されています。主要な学術誌（*MIS Quarterly* や *Industrial Management & Data Systems* など）のレビューによると、手法の成熟とともに、適切な報告ガイドラインに従った正確なパラメータ（統計的検出力、サンプルサイズの選定理由など）の開示が強く求められるようになっています。

---

## 関連概念

* [[構造方程式モデリング]] (SEM)
* [[共分散構造分析]] (CB-SEM)
* [[確証的複合分析]] (CCA)
* [[判別妥当性]] (HTMT)
* [[統計的予測モデリング]] (PLSpredict)

---

## 参考ソース

* **When to use and how to report the results of PLS-SEM** (Joseph F. Hair, Jeffrey J. Risher, Marko Sarstedt, Christian M. Ringle, 2018)
* **Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R** (Joseph F. Hair, G. Tomas M. Hult, Christian M. Ringle, Marko Sarstedt, Nicholas P. Danks (+1), 2021)
* **Using PLS path modeling in new technology research: updated guidelines** (Jörg Henseler, Geoffrey S. Hubona, Pauline Ash Ray, 2016)
* **Assessing measurement model quality in PLS-SEM using confirmatory composite analysis** (Joe F. Hair, Matt C. Howard, Christian Nitzl, 2019)
* **An updated and expanded assessment of PLS-SEM in information systems research** (Joe F. Hair, Carole L. Hollingsworth, Adriane B. Randolph, Alain Yee‐Loong Chong, 2017)