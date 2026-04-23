# Article Reader Page Specification

## 1. Purpose

`Article Reader` は、選択した concept を本文として理解しながら、構造との接続を失わないための画面である。

この画面が解くべきユーザー課題は次の 4 つ。

1. ある concept が何を意味するかを文章で理解する
2. その concept がどの tier・文脈・根拠に属するかを確認する
3. 本文を読みながら、次に移動すべき隣接概念を決める
4. 必要に応じて `Knowledge Atlas` に戻り、構造側から再確認する

Reader は「一覧画面」でも「graph 画面」でもない。本文理解を主 task とする reading workspace である。

## 2. Page-level User Outcome

ページ全体として、ユーザーが最終的に得るべき成果は次のいずれかである。

1. 「この concept は何者か」が説明できる
2. 「次に読むべき関連 concept」が決まる
3. 「この concept を Atlas で見直すべきか」が判断できる

## 3. Reading Flow

1. サイドバーで view を確認する
2. Hero で Reader の役割を理解する
3. `Reading Queue` で読む記事を選ぶ
4. `Reading Stage` で本文を読む
5. `Reading Companion` で backlinks / outbound / unresolved を確認する
6. 必要に応じて `Knowledge Atlas` へ戻る

## 4. Panel Inventory

| Area | Panel | Primary job |
|---|---|---|
| Sidebar | Views | Atlas / Reader / Index の往復導線を提供する |
| Sidebar | Corpus snapshot | 共通 corpus の規模と欠損量を共有する |
| Hero row | Hero card | Reader が何のための画面かを宣言する |
| Hero row | Metric grid | corpus と reading queue の規模感を要約する |
| Left column | Queue intro | 左列が読む記事を決める操作面だと定義する |
| Left column | Search | 記事名で候補を絞る |
| Left column | Tier filter | 読む抽象度を切り替える |
| Left column | Sort | queue の並び順を切り替える |
| Left column | Guided paths | 典型的な読書入口へ 1 click で移動する |
| Left column | Reading Queue | 記事一覧から読む concept を選ぶ |
| Center | Stage header | 選択記事のタイトルと役割を宣言する |
| Center | Stage chrome | 現在の filter / selection 状態を要約する |
| Center | Reading Stage | 記事本文を可読な形で提示する |
| Center | Stage briefs | 今読んでいる記事の役割と遷移方針を補助する |
| Lower detail | Reading Companion summary | 選択記事の判断材料を要約する |
| Lower detail | Context | domains / key sources を確認する |
| Lower detail | Connections | outbound / backlinks から次の移動先を示す |
| Lower detail | Gap audit | unresolved references を補助的に確認する |

## 5. Detailed Panel Specification

### 5.1 Sidebar: Views

目的:
Atlas / Reader / Index を往復可能にし、現在地を自然に理解させること。

表示情報:

- `Knowledge Atlas`
- `Article Reader`
- `Wiki Index`
- 各 view の短い説明

操作:

- 各 view への遷移

表現理由:

- sidebar は brand ではなく wayfinding の責務だけを持つため

### 5.2 Sidebar: Corpus snapshot

目的:
どの corpus を読んでいるのかを一目で伝えること。

表示情報:

- concept 総数
- resolved edge 総数
- unresolved reference 総数

操作:

- なし

### 5.3 Hero card

目的:
Reader が「読む画面」であり、Atlas の代替ではないことを最初に宣言すること。

表示情報:

- 画面名
- 大見出し
- 読書体験の役割説明

### 5.4 Metric grid

目的:
Reader が扱う corpus と queue の規模感を数字で掴ませること。

表示情報:

- Articles
- Tier 1 count
- Tier 2 count
- Tier 3 count
- Resolved edges
- Unresolved refs

### 5.5 Left column: Queue intro

目的:
左列が「記事を選ぶ面」であることを定義すること。

表示情報:

- `Reading Queue`
- 左列の使い方を要約する短文

### 5.6 Left column: Search

目的:
読みたい concept をタイトルから直接見つけること。

表示情報:

- search input

操作:

- タイトル検索

### 5.7 Left column: Tier filter

目的:
読む抽象度を切り替えること。

表示情報:

- `All`
- `Tier 1`
- `Tier 2`
- `Tier 3`

操作:

- tier 切り替え

### 5.8 Left column: Sort

目的:
queue の見え方を問いに応じて変えること。

表示情報:

- `Most connected`
- `Alphabetical`
- `Gap-rich`

操作:

- 並び順切り替え

### 5.9 Left column: Guided paths

目的:
初見ユーザーにとって「どこから読み始めるか」を簡単にすること。

表示情報:

- `Top hubs`
- `Tier 1 foundations`
- `Gap-rich concepts`

操作:

- reading preset 起動

### 5.10 Left column: Reading Queue

目的:
候補の中から次に読む記事を選ばせること。

表示情報:

- 記事タイトル
- tier badge
- 短い description
- backlink / outbound / unresolved の要約

操作:

- 記事選択

表現理由:

- compact card list にする
  理由: queue は本文そのものではなく、読書開始の入口だから

### 5.11 Stage header

目的:
いま読んでいる記事が何で、どんな役割の concept なのかを宣言すること。

表示情報:

- `Reading Stage` kicker
- 選択記事タイトル
- description
- tier / connection 系の chips

### 5.12 Stage chrome

目的:
現在の filter / selection 状態を短く要約すること。

表示情報:

- queue 状態
- current selection

### 5.13 Reading Stage

目的:
本文を可読な typography で読むこと。

表示情報:

- 記事本文
- inline wikilink
- markdown heading / list / table / hr

操作:

- wikilink click で別記事へ遷移

表現理由:

- 本文を主役に置く
  理由: Reader の primary task は理解であり、graph ではないため
- overlay を使わない
  理由: 一覧と本文の文脈を同一 page state の中で保つため

### 5.14 Stage briefs

目的:
今読んでいる記事の役割と次の遷移方針を短く補助すること。

表示情報:

- current focus
- traversal summary

### 5.15 Reading Companion summary

目的:
選択記事を構造の中でどう扱うかを判断させること。

表示情報:

- assessment 文
- degree / backlinks / outbound / unresolved
- `Open in atlas`

操作:

- Atlas handoff

### 5.16 Context

目的:
domains と key sources から記事の置き場所と根拠を確認すること。

表示情報:

- domains
- key sources

### 5.17 Connections

目的:
次に読むべき関連 concept を示すこと。

表示情報:

- outbound concepts
- backlinks

操作:

- 関連 concept の選択

### 5.18 Gap audit

目的:
その記事周辺の unresolved references を補助的に確認すること。

表示情報:

- unresolved target 名
- mention count / candidate 情報

## 6. Layout Logic

### Desktop

- Sidebar rail
- Hero row
- 2-column workspace
  - left reading queue
  - right analysis column
    - reading stage
    - reading companion

理由:
queue と本文を同時に保持しつつ、本文を最大幅で読ませるため。

### Tablet

- queue と analysis column は 2 列を維持する
- companion は analysis column 内の後段に続く

### Mobile

- rail は上段 tab 的表現に変わる
- queue と analysis column は 1 列化する

## 7. Non-goals

Reader は次を目的としない。

- corpus 全体の topology 把握
- 全 concept の網羅確認
- authoring / editing

それらは `Knowledge Atlas` または `Wiki Index` の責務である。
