# NLP論文クレームコーパス

## 概要

**NLP論文クレームコーパス**（英: Corpus of Claims from NLP Articles、略称: **COCOA**）は、自然言語処理（NLP）分野の学術論文から抽出されたクレーム（主張・命題）を収集・整理したコーパスである。2026年にClémentine Bleuze、Fanny Ducel、Maxime Amblard、Karën Fortらによって構築・公開された。

学術論文における「クレーム」とは、著者が提示する主張・発見・仮説などの命題的表現を指す。NLP分野では論文数が急増しており、論文中の主張を自動的に識別・分析する研究基盤の整備が求められている。COCOAはその基盤となるリソースとして位置づけられる。

---

## 詳細

### 目的と背景

COCOAプロジェクトの主な目的は以下の二点である。

1. **コーパスの構築（Creation）**: NLP分野の論文群からクレームを系統的に収集し、アノテーション付きコーパスとして整備すること。
2. **探索的調査（Exploratory Investigation）**: 収集されたクレームの特性・傾向・構造を分析すること。

NLP研究コミュニティでは、論文に含まれる主張の信頼性・再現性・過大表現（overclaiming）が課題として指摘されてきた。COCOAはこうした問題を定量的・定性的に調査するための実証的基盤を提供する。

### コーパスの特徴

ソースとなる論文はNLP分野の学術論文であり、以下のような観点から構築・調査が行われている。

- **クレームの抽出**: 各論文に含まれる主張・発見を文単位または命題単位で抽出。
- **探索的分析**: クレームの種類、頻度、表現パターン、文書内の出現位置などを調査。
- **アノテーション設計**: クレームを構造化データとして扱えるよう、アノテーションスキームが設計されている。

### 意義

COCOAは以下のような応用・研究に寄与することが期待される。

- NLP論文における**過大主張（overclaiming）の自動検出**
- 論文の**科学的厳密性の評価**支援
- **引数マイニング（Argument Mining）** や **科学的主張の検証（Scientific Claim Verification）** タスクへのデータ提供
- 研究コミュニティにおける**再現性危機**への対応

### 著者・所属

本研究はフランスの研究者チームによるものであり、自然言語処理・計算言語学・科学的言語分析を専門とする研究者らが共同で取り組んでいる。

---

## 関連概念

- 引数マイニング（Argument Mining）
- 科学的主張検証（Scientific Claim Verification）
- アノテーションコーパス
- 自然言語処理（NLP）
- 過大主張検出（Overclaiming Detection）
- 再現性危機（Reproducibility Crisis）
- 情報抽出（Information Extraction）
- 科学的言説分析

---

## 参考ソース

| タイトル | 備考 |
|----------|------|
| COCOA: Creation and Exploratory Investigation of a Corpus of Claims from NLP Articles | Bleuze et al., 2026. OpenAlex ID: `https://openalex.org/W7136094393` |