# Article Reader Renewal

## 問い

Article Reader を Knowledge Atlas と同じプロダクト言語に揃えつつ、本文理解のための画面として最適化するには、何を共通化し、何を Reader 固有として残すべきか。

## 論点

1. Atlas と Reader のあいだで揃えるべきものは何か
2. Reader の主役は何で、Atlas から継承してはいけないものは何か
3. 記事一覧・本文・構造情報をどう並べると理解が最速になるか
4. レイアウト崩れや state 遷移の破綻をどう防ぐか

## 論点分解

### 1. 共通化するもの

- view rail
- hero / metric / panel の視覚言語
- 背景、色、タイポグラフィ、glass card のトーン
- レイアウトを normal flow / grid で崩れにくく保つ構造

### 2. Reader 固有で守るもの

- 本文が主役であること
- wikilink から別記事へ移動できること
- backlinks / outbound / unresolved が読書の補助として機能すること
- hash deep-link で記事へ直行できること

### 3. 情報配置

- 記事を選ぶ queue
- 本文を読む stage
- 構造との接続を確認する companion

### 4. 構造的ガードレール

- desktop / tablet / mobile の breakpoint ごとに no-overflow を守る
- 検索・tier filter・hash 遷移・wikilink 遷移・resize 後も layout invariant を守る

## 仮説構築

| 選択肢 | 利点 | 欠点 |
|---|---|---|
| 旧 reader の dark overlay を磨く | 実装量が少ない | Atlas と別プロダクトに見え、読書と構造が分断されたまま |
| Atlas の visual language を継承し、queue / stage / companion に再編する | 同一プロダクトとして理解しやすく、責務も明確 | 実装の作り直しが必要 |
| Atlas とまったく同じ stage-first 構成にする | 見た目の統一感は最大 | Reader 固有の「本文主役」が弱くなる |

## 仮説の評価

| 評価軸 | 旧 overlay 継続 | queue / stage / companion 再編 | Atlas 完全コピー |
|---|---|---|---|
| プロダクト統一感 | 低い | 高い | 高い |
| 本文理解のしやすさ | 中 | 高い | 中 |
| 構造への接続 | 低い | 高い | 高い |
| レイアウト保守性 | 低い | 高い | 中 |

## 結論

Reader は Atlas の visual language を継承するが、主役は graph ではなく本文とする。

そのため、Reader は次の 3 面構成で再設計する。

1. `Reading Queue`
   検索・tier filter・sorting・記事一覧を持つ左 panel
2. `Reading Stage`
   選択中の記事タイトル、説明、本文、読書状態を持つ主面
3. `Reading Companion`
   backlinks / outbound / unresolved / atlas handoff を持つ補助面

fixed overlay は廃止し、同一 page 上の selection state として記事遷移を扱う。

## ネクストアクション

1. Reader 専用の page spec を追加する
2. `tools/build_reader.py` を queue / stage / companion 構成へ全面改修する
3. markdown renderer を改善し、表・hr・list を崩さず読めるようにする
4. Reader 専用の Playwright layout invariant を追加する

## 残論点

1. 将来的に article body の section navigator を入れるか
2. atlas との cross-highlight をさらに強化するか
3. table / footnote をどこまで markdown renderer で扱うか
