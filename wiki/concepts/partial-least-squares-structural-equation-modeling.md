# 部分的最小二乗法構造方程式モデリング（PLS-SEM）

**部分的最小二乗法構造方程式モデリング（Partial Least Squares Structural Equation Modeling: PLS-SEM）**は、観測変数と潜在変数（直接測定できない抽象的な概念）の間の複雑な因果関係を分析するための統計的プレディクティブ・モデリング手法です。

一般的に構造方程式モデリング（SEM）といえば、共分散構造分析（CB-SEM）が広く用いられてきましたが、近年、その強力かつ柔軟な代替手法として、情報システム、マーケティング、ホスピタリティ管理など、多様なビジネス・社会科学分野でPLS-SEMの採用が急速に進んでいます。

---

## 概要

PLS-SEMは、別名**「ソフトモデリング（Soft Modelling）」**とも呼ばれ、データの正規分布仮定や大サンプルサイズといった厳しい統計的制約を課さないことが大きな特徴です。

主な重要性とメリットは以下の通りです：
- **予測重視のアプローチ：** 理論の検証だけでなく、モデルの予測精度の最大化（決定係数 $R^2$ の最大化など）に焦点を当てています。
- **柔軟なデータ要件：** 比較的小さなサンプルサイズでも動作し、非正規分布のデータに対しても頑健（ロバスト）です。
- **複雑なモデルへの適応：** 多数の観測変数や潜在変数を含む複雑なモデルを容易に扱うことができます。

---

## 詳細な知見と応用

提供された学術的ソースに基づき、PLS-SEMの応用、評価、および特性について整理します。

### 1. 提唱と発展
PLS-SEMの基礎は、1980年代に統計学者ヘルマン・ウォルド（Herman Wold）によって「ソフトモデリング」として提唱されました。これは、地球科学や自然科学などの複雑な動的システムのモデル化から、意思決定プロセスや組織行動といった社会科学、情報システムの分析まで、幅広い適応力を持つ手法として基礎が築かれました。

### 2. 応用分野と学術的関心
* **情報システム（IS）と組織マネジメント：**
  T. RavichandranとArun Rai（2000年）の研究では、ソフトウェア開発における品質管理システム（経営陣のリーダーシップ、プロセス管理、利害関係者の参加など）が品質パフォーマンスに与える複雑な影響度を測定するためにPLS分析が適用されました。
* **ホスピタリティ・観光研究：**
  Faizan Aliら（2017年）の研究によれば、観光・ホスピタリティ分野の主要ジャーナルにおいてPLS-SEMの適用が急増しています。CB-SEMに代わる魅力的な選択肢として支持される一方で、その適切な適用基準や報告手順のガイドラインの重要性も指摘されています。
* **マーケティングと顧客満足度測定：**
  Richard P. Bagozzi（1994年）やManuel J. Vilaresら（2009年）の研究では、顧客満足度データや購買意図の予測において、伝統的な最尤法（Likelihood Estimators）とPLS推定量の比較シミュレーションが行われ、実証研究における実用性の高さが示されています。

### 3. モデルの評価と報告基準
PLS-SEMを適用する際は、適切な評価プロセスが求められます（Oliver Götzら, 2009）。一般的に、モデルの評価は以下の2段階で行われます。
1. **測定モデル（Measurement Model）の評価：** 観測変数と潜在変数の関係（信頼性、収束妥当性、判別妥当性）の検証。
2. **構造モデル（Structural Model）の評価：** 潜在変数間の経路係数の有意性や、決定係数（$R^2$値）を用いた予測力の検証。

また、研究におけるPLS分析結果の正確な書き方や報告手順（How to Write Up and Report PLS Analyses）については、Wynne W. Chin（2009年）などが詳細なガイドラインを提供しており、研究の透明性と再現性を高めるためのデファクトスタンダードとなっています。

---

## 関連概念

- [[共分散構造分析（CB-SEM）]]
- [[潜在変数（Latent Variables）]]
- [[多変量解析]]
- [[プレディクティブ・モデリング]]

---

## 参考ソース

* **An assessment of the use of partial least squares structural equation modeling (PLS-SEM) in hospitality research**
  * *Faizan Ali, S. Mostafa Rasoolimanesh, Marko Sarstedt, Christian M. Ringle, Kisang Ryu (2017)*
* **Soft modelling: The Basic Design and Some Extensions**
  * *Herman Wold (1982)*
* **Quality Management in Systems Development: An Organizational System Perspective1**
  * *T. Ravichandran, Arun Rai (2000)*
* **How to Write Up and Report PLS Analyses**
  * *Wynne W. Chin (2009)*
* **Evaluation of Structural Equation Models Using the Partial Least Squares (PLS) Approach**
  * *Oliver Götz, Kerstin Liehr-Gobbers, Manfred Krafft (2009)*
* **Comparison of Likelihood and PLS Estimators for Structural Equation Modeling: A Simulation with Customer Satisfaction Data**
  * *Manuel J. Vilares, Maria Helena Morgani de Almeida, Pedro S. Coelho (2009)*
* **Advanced Methods of Marketing Research**
  * *Richard P. Bagozzi (1994)*