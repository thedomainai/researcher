# 上流の表現構造による下流能力の上限規定

## 概要

上流の表現構造による下流能力の上限規定とは、データ、スキーマ、アノテーション、評価基準といった上流の表現設計が、下流で実現できる能力と測定の妥当性の上限を恒久的に決めてしまい、後からは容易に覆せないという原理である。

下流でモデルやオーケストレーションを改良しても、上流の表現が持たない情報を後から生み出すことはできない。また、評価の表現が汚染されていれば、測定された性能そのものが信頼できなくなる。AI Nativeな設計では、モデル選択よりも先に、何をどの粒度・構造で表現しておくかが能力の天井を決める。この点が本概念の核心である。

## メカニズム

この構造は対象を入れ替えても成立する。人間・AI・組織・技術のいずれでも、次の四つが共通して働く。

1. **情報の表現形式による制約**: 下流の処理は、上流が表現した情報の範囲内でしか働けない。表現に含まれない区別(意味関係、由来、階層構造など)は、下流からは見えない。
2. **経路依存性**: 初期の表現設計(スキーマ、アノテーション形式、評価指標)の上に後続の資産が積み重なり、変更コストが上がり続ける。
3. **技術的負債の累積**: 上流の欠陥は、局所的に直せるコード上の負債とは異なり、複数の利用者・部門にまたがる調整コストを伴うため、修復が難しい。
4. **指標の汚染(リーク)による過大評価**: 評価の表現にラベルの情報が漏れると、達成された性能は実力ではなく表現の欠陥を反映する。上限は「高すぎる見かけ」という形でも現れる。

つまり上限は二方向に働く。能力の面では下流の到達点を切り下げ、測定の面では見かけの到達点を切り上げる。

## 理論的背景

### 情報アーキテクチャ負債と能力上限仮説

Shah(2026)は、エンタープライズプラットフォームが蓄積する負債の一種を「情報アーキテクチャ負債」と名づけた。過去の計算環境でトランザクション効率のために最適化されたスキーマ決定が、採用するモデルやオーケストレーションの選択とはほぼ無関係に、AIにできることを構造的に制限するという主張である。この負債はコード負債やインフラ負債とは別カテゴリーとされ、その理由は、修復の局所性と調整コストが大きく異なる点にある。診断枠組みとして、重複する正準エンティティ、途切れた意味の連鎖、来歴(プロベナンス)の欠落、強制の非対称性、消費者側の想定の乖離という五つの指標が提案されている。この枠組みは、基盤(substrate)の欠陥がAIの成果に上限を課すという能力上限仮説を支える。

### データセットの表現成熟度

Lee、Kim、Jiによる2026年の系統的レビューは、PRISMA 2020に沿って64のファッションデータセットを、FAIR準拠、複合的なAI-Readinessスコア、5段階のオントロジー成熟度モデルで評価した。AI-Readinessの等級はB(60.3%)とC(36.5%)の中間層に集中し、79.7%のデータセットは平坦な属性アノテーション(レベル2以下)にとどまった。同レビューは、新規データセットが機械可読なオープンライセンスと永続識別子を採用し、アノテーションを少なくともタクソノミー水準(レベル3)で構造化すべきだと提言している。上流のアノテーション構造が、下流のAI適応性を制限していることを示す実証である。

### 評価表現の汚染

Ismaelらは、侵入検知ベンチマークで報告される「ほぼ完璧」な精度とF1のうち、どれだけが精査に耐えるかを問い、LeakAuditを提案した。これは相互情報量で各特徴量とラベルの依存度を順位づけ、閾値を超えるものを除いて、保持データでのF1を「監査済みの上限」として報告する手法である。NSL-KDD、Edge-IIoTset、CIC-IDS-2017、UNSW-NB15、ToN-IoT Networkでは、F1の低下がそれぞれ6.60、2.91、2.48、0.70、0.04ポイントだった。注入した既知の強さのリークに対する検出AUCは0.972(誤警報率0.007)で、相関スクリーンより優れる一方、ランダムフォレストの重要度ランキングを上回るものではなかったと、著者らは測定どおりに報告している。データセットにより影響の大きさが大きく異なる点が重要である。

### バイアスの固定化と規範化

Tsengらのヘルスケア分野のレビューは、バイアスの緩和をデータ取得、前処理、学習、検証、展開というライフサイクルで整理している。核心的な知見として、不完全なデータから構築されたシステムはバイアスを保有・拡大しやすいという制約は不変だとされる。González-Martínは、訓練データ、設計アーキテクチャと目的、インターフェースと利用実践という三層で男性中心的規範のアフォーダンスを類型化し、システム設計が訓練データの偏りを規範化し、ユーザーとの相互作用を通じて再強化されると論じる。上流のデータ表現の偏りが、下流で規範として固定される経路を示している。

### 補足的な知見

Angara、Yellapuの糖尿病予測研究(BRFSS2015)では、反事実説明LICEで偽陰性を特定し、特徴構築とサンプル重み付けで改善した。LICE-BalancedGBDTは偽陰性を172件(相対12.14%)減らしている。これは下流での改善余地を示す例だが、上限が与えられた表現の範囲内にあることを前提とした改善である。

## AI Nativeな設計への示唆

- **モデルより先に基盤を診断する**: AI導入前に、重複エンティティ、意味連鎖の断絶、来歴の欠落などを点検する。五指標のような診断枠組みが出発点になる。
- **アノテーションは構造化して設計する**: 平坦な属性ではなく、少なくともタクソノミー水準の構造を持たせる。機械可読なライセンスと永続識別子も初期から組み込む。
- **評価の表現を監査する**: ベンチマークの高スコアは、リークの有無を検査してから解釈する。監査済みの上限を併記する運用が有効である。
- **修復コストを見積もり、早期に投資する**: 上流の欠陥は調整コストが大きく、後からの修復は困難になる。初期設計段階での投資が合理的である。
- **偏りをライフサイクル全体で管理する**: データ取得の段階から検証・展開まで、偏りの固定化経路を意識して介入点を設ける。
- **上限を仮定として明示する**: 下流の改善策(重み付け、説明手法など)が効く範囲は、上流表現が許す範囲内だと認識して期待値を設定する。

## 関連コンセプト

- [[upstream-representation-integrity-failure]] — 上流の表現完全性が下流の統治を規定する構造
- [[bias-compounding-across-interacting-distortion-sources]] — 複数の歪み源の相互作用による偏りの累積・増幅
- [[ai-in-enterprise-systems-and-digital-transformation]] — エンタープライズシステムにおけるAI
- [[active-inertia]] — 既存の枠組みが変更を妨げる惰性
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失
- [[ai-infrastructure-and-development]] — AIインフラと開発

## 参考ソース

- Lee, Y. K., Kim, M. K., Ji, S. Y. (2026). FAIR compliance, AI-readiness, and ontology maturity of garment datasets: a systematic assessment. `raw/papers/behavioral_economics/fair-compliance-ai-readiness-and-ontology-maturity-of-garment-datasets-a-systema.md`
- Li, Y., Li, Y. (2026). AI Load Dynamics–A Power Electronics Perspective. `raw/papers/behavioral_economics/ai-load-dynamicsa-power-electronics-perspective.md`(物理的な下流制約の対比例として参照。本記事の主論点との関係は間接的)
- Tseng, W., Holbrook, K. S., Edpuganti, R. L., Girgis, M., Chen, D. (2026). Bias Mitigation Across the Healthcare Artificial Intelligence Lifecycle: A Structured Narrative Review. `raw/papers/behavioral_economics/bias-mitigation-across-the-healthcare-artificial-intelligence-lifecycle-a-struct.md`
- Ismael, H. A., Al-Ta'i, Z. T. M., Abbas, J. M. (2026). Auditing Feature-level Label Leakage in Intrusion Detection Benchmarks Using Mutual Information. `raw/papers/behavioral_economics/auditing-feature-level-label-leakage-in-intrusion-detection-benchmarks-using-mut.md`
- Angara, D., Yellapu, J. (2026). LICE-guided Sensitivity-oriented Model Refinement for Diabetes Prediction: An Ablation Analysis of Interaction Features and Sample Weighting. `raw/papers/behavioral_economics/lice-guided-sensitivity-oriented-model-refinement-for-diabetes-prediction-an-abl.md`
- Shah, M. (2026). Information architecture debt: Why legacy platform schema decisions constrain enterprise AI capability. `raw/papers/behavioral_economics/information-architecture-debt-why-legacy-platform-schema-decisions-constrain-ent.md`
- González-Martín, J. A. (2026). Artificial Intelligence and Androcentric Normativity. `raw/papers/behavioral_economics/artificial-intelligence-and-androcentric-normativity.md`

## 追加ソース（2026-10-02）

* **タイトル**: Building Trust in AI for Project Controls: A Governance-Embedded Data Engineering Framework (2026)
  **ファイルパス**: `raw/papers/ai_governance/building-trust-in-ai-for-project-controls-a-governance-embedded-data-engineering.md`
