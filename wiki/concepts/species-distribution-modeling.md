# 種分布モデル

**種分布モデル（Species Distribution Modeling: SDM）**とは、特定の生物種の存在データ（または存在・非存在データ）と、気候、地形、土壌などの環境変数を統計学的に関連付けることで、その種の地理的な分布状況を予測・マッピングする計算手法です。

この技術は、地球規模の気候変動や生息地の開発が生物多様性に与える影響を予測し、効果的な保全計画や管理戦略を策定する上で極めて重要な役割を果たしています。

---

## 主な知見と課題

種分布モデルは生物多様性評価において必要不可欠なツールとなっていますが、その適用と信頼性にはいくつかの重要な側面が存在します。

### 1. ベストプラクティスと評価基準の確立
SDMへの需要が高まる一方で、モデルの品質や信頼性を担保するための共通基準が求められています。Araújoら（2019）の研究では、過去20年間の400におよぶモデリング研究を調査し、生物多様性評価におけるモデルの妥当性を評価するための基準と詳細なガイドラインを提案しました。
この調査では、全体的なモデルの妥当性は依然として低い水準にあるものの、時系列で見るとモデル構築プロセスにおいて著しい改善傾向があり、生物データおよびモデル評価の質も向上しつつあることが示されています。合意された標準規格（Standards）を導入することは、モデルの透明性と再現性を高め、意思決定プロセスの品質向上に寄与します。

### 2. 気候変動下における意思決定への適用
将来の気候変動下で生物多様性を維持・管理するためにSDMは頻繁に活用されます（Sinclairら, 2010）。しかし、将来の予測には不確実性が伴うため、これらのモデルを実際の環境保全や野生動物の管理計画にどのように適用すべきかという「有用性の境界」を理解することが不可欠です。

### 3. コミュニティレベルおよび半機構的アプローチ
従来のSDMは個々の種を対象とした「種レベル」での相関モデル（Correlative models）が主流でした。しかし、これらは空間や時間を超えて生物多様性が変化する主要なプロセス（生物相互作用や移動分散など）を無視する傾向があります。
MokanyとFerrier（2010）は、種レベルの限界を補完するアプローチとして、新たな**「半機構的コミュニティレベルモデリング（Semi-mechanistic community-level modelling）」**の開発を提唱しています。これにより、気候変動が生物多様性全体に及ぼす影響を、よりロバスト（堅牢）かつ信頼性の高い形で予測することが可能となります。

---

## 関連概念

- [[生物多様性評価 (Biodiversity Assessment)]]
- [[気候変動予測 (Climate Change Projection)]]
- [[コミュニティレベルモデル (Community-Level Modeling)]]
- [[保全生態学 (Conservation Ecology)]]

---

## 参考ソース

- **Standards for distribution models in biodiversity assessments** (Araújo et al., 2019) — `raw/Standards_for_distribution_models_in_biodiversity_assessments`
- **How Useful Are Species Distribution Models for Managing Biodiversity under Future Climates?** (Sinclair et al., 2010) — `raw/How_Useful_Are_Species_Distribution_Models_for_Managing_Biodiversity_under_Future_Climates`
- **Predicting impacts of climate change on biodiversity: a role for semi‐mechanistic community‐level modelling** (Mokany & Ferrier, 2010) — `raw/Predicting_impacts_of_climate_change_on_biodiversity_a_role_for_semi-mechanistic_community-level_modelling`