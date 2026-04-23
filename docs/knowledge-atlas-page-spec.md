# Knowledge Atlas Page Specification

## 1. Purpose

`Knowledge Atlas` は、研究知識ベースを「記事本文を読む前に構造で理解する」ための分析ダッシュボードである。

この画面が解くべきユーザー課題は次の 4 つ。

1. どの概念が中心で、どの概念同士が結びついているかを短時間で掴む
2. ある概念が hub なのか、bridge なのか、gap-rich なのかを判断する
3. 構造の俯瞰から、次に読むべき記事を決める
4. 未解決参照の集中箇所を見つけ、執筆優先度を決める

このページは「百科事典ページ」ではなく、「構造理解と次の行動決定のための workspace」である。

## 2. Page-level User Outcome

ページ全体として、ユーザーが最終的に得るべき成果は次のいずれかである。

1. 「この領域の主要ハブは何か」が分かる
2. 「この概念を次に読むべきか」が判断できる
3. 「どこが coverage gap になっているか」が分かる
4. `Article Reader` に移るべき記事が決まる

Atlas 自体のゴールは「理解を完了させること」ではなく、「理解のための進行方向を決めること」である。

## 3. Reading Flow

このページは、次の順で読むことを前提に設計する。

1. サイドバーで view を確認する
2. Hero で「この画面は何をする画面か」を理解する
3. Metric Grid で corpus の成熟度を把握する
4. 左の `Control Tower` で lens と mode を決める
5. analysis column の先頭にある `Knowledge Field` で構造を俯瞰する
6. 同じ analysis column の後段にある `Inspector` で選択概念を精査する
7. 必要に応じて `Article Reader` に移る

レイアウトはこの順序に従っている。

## 4. Panel Inventory

| Area | Panel | Primary job |
|---|---|---|
| Sidebar | Views | Atlas / Reader / Index の往復導線を提供する |
| Sidebar | Corpus snapshot | 見ている corpus の規模と欠損量を共有する |
| Hero row | Hero card | この画面の目的を宣言する |
| Hero row | Metric grid | corpus の密度・欠損・品質を要約する |
| Left column | Control Tower intro | 左列が「操作面」であることを定義する |
| Left column | Lens | graph の対象集合を切り替える |
| Left column | Mode | graph の描画ポリシーを切り替える |
| Left column | Guided Paths | 典型的な分析タスクを 1 click で始める |
| Left column | Priority Nodes | 重要 concept へのジャンプを提供する |
| Left column | Gap Watchlist | 未解決ギャップの入口を提供する |
| Center | Stage header | canvas の目的と制約を宣言する |
| Center | Legend | 色と意味の対応を示す |
| Center | Decision rule | 推奨される読み順を指示する |
| Center | Stage chrome | canvas を interactive workspace として見せる |
| Center | Knowledge Field | 概念構造を空間比較できるようにする |
| Center | Stage briefs | 現在の lens と field 状態を短く補助する |
| Analysis column | Inspector summary | 選択 concept の要約と判断材料を集約する |
| Analysis column | Context | domains / key sources を確認させる |
| Analysis column | Connections | outbound / backlinks から移動先を示す |
| Analysis column | Gap audit | unresolved references から coverage gap を点検させる |

## 5. Detailed Panel Specification

### 5.1 Sidebar: Views

#### Purpose

この panel の目的は、ユーザーに「Atlas / Reader / Index の 3 画面が存在し、そのあいだを移動できる」と理解させること。

#### Displayed information

- `Knowledge Atlas`
- `Article Reader`
- `Wiki Index`
- 各 view の短い説明

#### Why this information exists

view 名だけだと責務の違いが伝わりづらいため、短い説明を添えて「何のための画面か」を最小限で伝える。

#### Allowed interactions

- 各 view への遷移
- active 状態による現在位置の確認

#### Layout / representation rationale

- サイドバー上部に置く
  理由: 画面の最初の分岐判断だから
- active item を強く、inactive item を弱く表現する
  理由: 現在地は nav の状態だけで伝えるべきだから
- ブランド文言を置かない
  理由: この領域は wayfinding の責務だけを持つため

### 5.2 Sidebar: Corpus snapshot

#### Purpose

この panel の目的は、ユーザーに「今見ている知識ベースの規模感と欠損量」を一目で伝えること。

#### Displayed information

- concept 総数
- resolved edge 総数
- unresolved reference 総数

#### Allowed interactions

- なし

#### Layout / representation rationale

- サイドバー下部に置く
  理由: view 選択より優先度は低いが、常に見える共有文脈として保持したいため
- 1 行サマリーに圧縮する
  理由: 詳細分析は Hero row と main workspace が担うため

### 5.3 Hero card

#### Purpose

この panel の目的は、「このページは何を達成するための画面か」を最初に宣言すること。

#### Displayed information

- 画面名
- 大見出し
- 画面の役割説明

#### Why this information exists

graph UI は放っておくと抽象的すぎて、「これは何を見る画面か」が伝わりにくい。最初に目的を宣言し、以降の panel をその目的の補助として読ませる。

#### Allowed interactions

- なし

#### Layout / representation rationale

- Hero row の左に配置する
  理由: narrative を先に読み、そのあと右側の metric と workspace へ視線を流すため
- 大きな typography を使う
  理由: ページ identity を main area に持たせるため

### 5.4 Metric grid

#### Purpose

この panel の目的は、Atlas が見ている corpus の状態を数値で要約すること。

#### Displayed information

- `Resolved Concepts`
- `Resolved Edges`
- `Unresolved Refs`
- `Isolated Concepts`
- `Invalid Source Refs`
- `Link Mentions`

#### Why this information exists

各指標は次の判断に使う。

- `Resolved Concepts`
  corpus の広さ
- `Resolved Edges`
  構造の密度
- `Unresolved Refs`
  未整備ギャップの大きさ
- `Isolated Concepts`
  構造的孤立の多さ
- `Invalid Source Refs`
  ソース品質の劣化
- `Link Mentions`
  総リンク運動量

#### Allowed interactions

- なし

#### Layout / representation rationale

- Hero row の右に置く
  理由: 目的説明の直後に現況を数値で確認できるため
- 2x3 の grid にする
  理由: 6 指標を同格で並べつつ、1 指標だけが過剰に強くならないようにするため

### 5.5 Left column: Control Tower intro

#### Purpose

この panel の目的は、左列が「説明面」ではなく「操作面」であることを定義すること。

#### Displayed information

- `Control Tower`
- 左列の役割を要約する短い説明

#### Why this information exists

左列には filter, mode, queue が同居するため、最初に「graph を絞り込むための面」であることを短く宣言しないと意味が散りやすい。

#### Allowed interactions

- なし

#### Layout / representation rationale

- 左列の最上段に置く
  理由: その下にある操作群の読み方を先に固定するため
- 文章は 1 段落に圧縮する
  理由: 詳細な設計思想は仕様書側で担保し、画面内では操作の邪魔をしないため

### 5.6 Left column: Lens

#### Purpose

この panel の目的は、「全体」から「特定条件に切った部分集合」へ視点を変えること。

#### Displayed information

- Search input
- Tier chips
- Domain select
- Minimum Degree slider

#### Allowed interactions

- テキスト検索
- tier の切り替え
- domain の絞り込み
- degree threshold の調整

#### Layout / representation rationale

- ひとつの panel に集約する
  理由: これらはすべて「graph の対象集合を変える操作」だから
- form control を縦積みにする
  理由: 探索条件を step-by-step に組み立てさせるため

### 5.7 Left column: Mode

#### Purpose

この panel の目的は、graph の描画ポリシー自体を切り替えること。

#### Displayed information

- `Show isolated concepts`
- `Show unresolved halo`
- `Neighborhood mode`

#### Allowed interactions

- 孤立ノードの表示/非表示
- unresolved halo の表示/非表示
- 近傍モードの on/off

#### Layout / representation rationale

- `Lens` の直下に置く
  理由: 「何を見るか」と「どう描くか」は近いが異なる責務なので、隣接させつつ分離するため

### 5.8 Left column: Guided Paths

#### Purpose

この panel の目的は、典型的な分析タスクを 1 click で開始できるようにすること。

#### Displayed information

- `Top hubs`
- `Isolated concepts`
- `Unresolved-rich concepts`

#### Allowed interactions

- preset view の起動

#### Layout / representation rationale

- button list として表現する
  理由: preset は filter 群ではなく action だから

### 5.9 Left column: Priority Nodes

#### Purpose

この panel の目的は、重要度の高い概念へ即座にジャンプさせること。

#### Displayed information

- 上位 hub の概念名
- degree
- unresolved count

#### Allowed interactions

- 概念ボタンを押して node を選択する

#### Layout / representation rationale

- quick jump list として見せる
  理由: 完全な ranking table ではなく、graph を読む入口だから

### 5.10 Left column: Gap Watchlist

#### Purpose

この panel の目的は、未解決参照が集中している領域を見つけさせること。

#### Displayed information

- 未解決参照 target 名
- mention count
- source concept 数

#### Allowed interactions

- gap item を押して、関連性の高い source concept にジャンプし、focus mode で中心化する

#### Layout / representation rationale

- Priority Nodes の近くに置く
  理由: 片方が「構造中心」、片方が「欠損中心」の入口だから
- 注意書きを 1 行だけ添える
  理由: 未解決 target には記事がないという特殊性だけを補足すれば十分だから

### 5.11 Stage header

#### Purpose

この panel の目的は、`Knowledge Field` を単なる graph ではなく「何を読むための canvas か」として定義すること。

#### Displayed information

- `Workspace Canvas` kicker
- `Knowledge Field` title
- canvas の目的説明
- stage chips

#### Allowed interactions

- なし

#### Layout / representation rationale

- canvas の直上に置く
  理由: graph を見る前に「何を見る面か」を理解させるため
- chips は status 的に扱う
  理由: ここは filter ではなく設計原則の提示だから

### 5.12 Legend

#### Purpose

この panel の目的は、色と概念階層の意味を即時に理解させること。

#### Displayed information

- Tier 1
- Tier 2
- Tier 3
- Legacy / Untiered
- Unresolved halo

#### Allowed interactions

- なし

#### Layout / representation rationale

- header 下の meta row に置く
  理由: canvas に入る直前の reading key として機能するため

### 5.13 Decision rule

#### Purpose

この panel の目的は、Atlas の望ましい読み順を短く指示すること。

#### Displayed information

- cluster → hub → concept → Reader という順序

#### Allowed interactions

- なし

#### Layout / representation rationale

- legend の対面に置く
  理由: 片方が「何を意味するか」、もう片方が「どう読むか」を担当するため

### 5.14 Stage chrome

#### Purpose

この panel の目的は、canvas を document ではなく interactive workspace として認知させること。

#### Displayed information

- `Knowledge canvas`
- `resolved concepts in primary plane`
- 現在の lens summary
- 現在の selection summary

#### Allowed interactions

- なし

#### Layout / representation rationale

- window chrome 的な表現を取る
  理由: 「操作可能な作業面」という心理モデルを与えるため

### 5.15 Knowledge Field

#### Purpose

この panel の目的は、concept 間の関係構造を空間的に比較可能にすること。

#### Displayed information

- resolved concept nodes
- resolved edges
- selected / hovered node labels
- unresolved halo

#### Allowed interactions

- hover でノード強調
- click で node 選択
- drag で pan
- wheel で zoom

#### Layout / representation rationale

- canvas を中央最大領域に置く
  理由: このページの primary task が構造観察だから
- unresolved node を独立 node ではなく halo にする
  理由: 欠損を見せつつ主面を汚さないため
- node size を degree に連動させる
  理由: hub 性を視線移動だけで判断できるため
- node color を tier に連動させる
  理由: 概念の抽象階層を瞬時に比較できるため

### 5.16 Stage briefs

#### Purpose

この panel の目的は、現在の lens と field 状態を graph の直下で短く補助すること。

#### Displayed information

- 現在の lens 名
- selected node に応じた短い説明
- 現在の node / edge 数
- pan / zoom / focus の操作説明

#### Allowed interactions

- なし

#### Layout / representation rationale

- canvas の下に別 row として置く
  理由: graph と説明が同一平面にあると重なりやすいため
- 2 カードに圧縮する
  理由: purpose / interaction の静的説明を減らし、dashboard としての密度を保つため

### 5.17 Inspector summary

#### Purpose

この panel の目的は、選択 concept を「次に読むべきか」「どこを掘るべきか」という観点で評価すること。

#### Displayed information

- 概念名
- 1 段落 description
- assessment 文
- tier / metadata_source / degree / in / out / unresolved
- degree / backlink / outbound / gap metrics
- `Center in atlas`
- `Neighborhood mode`
- `Open in reader`

#### Allowed interactions

- `Center in atlas`
- `Neighborhood mode`
- `Open in reader`

#### Layout / representation rationale

- 右 column の最上段に置く
  理由: graph の横で「選択対象の判断材料」を常に保持するため
- summary を最初に集約する
  理由: downstream sections を読む前に「この node をどう扱うべきか」を判断させるため

### 5.18 Inspector: Context

#### Purpose

この panel の目的は、選択 concept が属する文脈と根拠を短時間で確認させること。

#### Displayed information

- domains
- key sources

#### Allowed interactions

- なし

#### Layout / representation rationale

- summary の直下に置く
  理由: 評価の補助材料として最も近くにあるべきだから
- key sources の件数を制限する
  理由: inspector を article 化させないため

### 5.19 Inspector: Connections

#### Purpose

この panel の目的は、次に移動できる resolved concept を示すこと。

#### Displayed information

- outbound concepts
- backlinks

#### Allowed interactions

- relation item を押して別 node を選択する

#### Layout / representation rationale

- outbound / backlinks を分けて表示する
  理由: 「どこへ出ていくか」と「どこから参照されるか」は別の判断材料だから
- 件数を制限し、残数は note として圧縮する
  理由: inspector が第2の一覧画面になるのを防ぐため

### 5.20 Inspector: Gap audit

#### Purpose

この panel の目的は、選択 concept 周辺の unresolved references を coverage audit の観点で点検させること。

#### Displayed information

- unresolved target 名
- 出現 section / line
- 候補 concept

#### Allowed interactions

- なし

#### Layout / representation rationale

- inspector の最後に置く
  理由: まず構造と接続先を見たあとに、最後に gap を監査する流れだから
- 表示件数を制限する
  理由: audit 情報は必要だが、主役は graph と summary だから

## 6. Layout Logic

### Desktop

- Sidebar rail
- Hero row
- 2-column workspace
  - left control tower
  - right analysis column
    - stage
    - inspector

desktop では control panel を sticky + internal scroll にし、analysis column 内では stage を先頭、inspector を後段に積む。

理由:
graph 面積を最大化しつつ、選択概念の判断材料を同一列の続きとして読ませるため。

### Narrow desktop / tablet

- app shell は 1 列化する
- workspace は `control + analysis column` の 2 列を維持する
- stage 内は container query で header / meta / chrome を圧縮する

理由:
sidebar 幅だけを外し、main workspace の操作性と graph 面積を維持するため。

### Mobile

- rail は上段 tab 的表現に変わる
- hero と workspace は 1 列化する
- control / inspector は sticky を解除する

理由:
横幅不足で multi-column の意味が消えるため、優先度順に縦積みへ切り替える。

## 7. Non-goals

`Knowledge Atlas` は次を目的としない。

- concept の完全理解
- 長文読書
- source document の原文精読
- 最終的な執筆編集

それらは `Article Reader` または将来の authoring surface の責務である。

## 8. Current Design Decision

1. 右 panel は `Dossier` ではなく `Inspector` と呼ぶ
   理由: 本文の代替ではなく、判断を支える軽量 panel であることを明確にするため
2. control panel は sticky + internal scroll を採用し、inspector は stage 後段で軽量に保つ
   理由: graph 面積を守りながら、長い第2記事化を防ぐため
3. Stage briefs は 4 カードではなく 2 カードに圧縮する
   理由: graph の主役性を守るため
