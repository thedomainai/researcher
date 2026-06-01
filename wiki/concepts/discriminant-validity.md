# 判別妥当性

**判別妥当性（Discriminant Validity）**とは、心理測定学や社会科学、情報システムなどの分野において、異なる概念（構成概念）を測定するために設計された尺度や指標が、実際に互いに区別できているかを示す検証基準です。

研究における測定モデルの妥当性を評価する上で、判別妥当性の検証は極めて重要です。もし複数の構成概念（例：顧客満足度とブランド忠誠度、あるいは特定の知覚や態度）の間で判別妥当性が確保されていない場合、それらは本質的に同じものを測定していることになり、統計的検定や仮説検証の結果に重大な歪みをもたらす可能性があります。

---

## 判別妥当性の評価手法と最新の知見

構造方程式モデリング（SEM）などを用いた多変数解析において、測定尺度の信頼性や収束妥当性（Convergent Validity）と並び、判別妥当性の検証は必須のプロセスとされています。近年、測定手法の厳密性を高めるために、評価基準やアプローチに関する研究が活発に行われています。

### 1. 統計的検定と経験則（ヒューリスティクス）の比較
伝統的に、判別妥当性の評価には特定のカットオフ値（経験則）を用いた判定と、推論統計的なアプローチが用いられてきました。
* **HTMT（Heterotrait-Monotrait Ratio of Correlations）比**: 
  近年のシミュレーション研究により、HTMT基準は構成概念間の「減衰補正された（完全に信頼できる）相関」の極めて優れた推定値であることが示されています。HTMTは、従来の基準に比べてタイプIエラー（第一種の誤り）およびタイプIIエラー（第二種の誤り）に対する感度が高く、頑健な（ロバストな）判別妥当性評価を可能にします。
* **制約付きPHIアプローチ（Constrained PHI approach）**:
  共分散構造分析において、2つの構成概念間の相関（$\phi$）を $1.0$ に制約したモデルと、自由推定したモデルの適合度を比較する伝統的な統計的アプローチです。HTMTは、この標準的な制約付きPHIアプローチに匹敵する、高い判別性能を持つことが実証されています。

### 2. 測定尺度報告におけるベストプラクティス
態度、知覚、行動意図といった直接観察できない潜在変数を扱う研究（マーケティングや組織行動論など）において、尺度の品質管理は欠かせません。
* 既存の測定尺度を異なる人口統計グループに適用する場合、または翻訳や修正を加える場合は、仮説検証を行う前に必ず判別妥当性を検証・報告する必要があります。
* 信頼性係数（Cronbach's alphaなど）の報告だけでなく、確証的因子分析（CFA）やSEMを用いた多角的な妥当性検証が推奨されています。

---

## 関連概念

* [[収束妥当性]] (Convergent Validity)
* [[構造方程式モデリング]] (Structural Equation Modeling: SEM)
* [[確証的因子分析]] (Confirmatory Factor Analysis: CFA)
* [[潜在変数モデル]] (Latent Variable Modeling)

---

## 参考ソース

* Clay M. Voorhees, Michael K. Brady, Roger J. Calantone, Edward Ramirez (2015). "Discriminant validity testing in marketing: an analysis, causes for concern, and proposed remedies"
* George R. Franke, Marko Sarstedt (2019). "Heuristics versus statistics in discriminant validity testing: a comparison of four procedures"
* Gordon W. Cheung, Helena D. Cooper–Thomas, Rebecca S. Lau, Linda C. Wang (2023). "Reporting reliability, convergent and discriminant validity with structural equation modeling: A review and best-practice recommendations"