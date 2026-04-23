# Researcher Workspace UI Specification

## 1. Purpose

この UI の目的は、研究知識ベースを「読む前に構造で理解できる」状態にすることです。

ユーザーが達成したいことは次の 4 つです。

1. どの概念が中心で、どこがつながっているかを素早く把握する
2. ある概念が何者で、どの文脈に属するかを確認する
3. 構造の俯瞰から記事本文の精読へ自然に移動する
4. まだ記事化されていない知識ギャップを見つける

この UI は「装飾された wiki」ではなく、「構造理解のための workspace」である。

## 2. Product Question

各画面は、それぞれ別の問いに答えるために存在する。

| View | User question | Primary outcome |
|---|---|---|
| Knowledge Atlas | 何がどうつながっていて、どこに穴があるか | 構造の把握 |
| Article Reader | この概念は何を意味し、どんな根拠があるか | 本文理解 |
| Wiki Index | どんな概念が存在し、どの分類に属するか | 網羅確認 |

重要なのは、3 画面が同じことをしないことです。

- Atlas は「読む」画面ではなく「見る」画面
- Reader は「探索」画面ではなく「理解」画面
- Index は「分析」画面ではなく「目録」画面

## 3. Layout Principles

### 3.1 Sidebar

サイドバーはブランド面ではなく、wayfinding 面である。

答えるべき問いは次の 3 つだけです。

1. どの view があるか
2. どの corpus を見ているか

そのため、サイドバーに置いてよいのは次だけです。

- view switcher
- corpus snapshot

置いてはいけないもの:

- product title block
- marketing copy
- ページ本文の代わりになる長い説明

### 3.2 Main Area

ページの identity と narrative は main area が持つ。

- ページタイトル
- そのページで何を達成する画面か
- そのページ特有の操作と情報密度

「ここは何の画面か」をサイドバーではなく main area に置くのは、ユーザーの注意を view switching と current task で分離するためです。

### 3.3 Detail Panel

詳細 panel は、構造の俯瞰と記事本文のあいだをつなぐ inspector としてのみ存在する。

つまり役割は「第三の本文」ではなく、次の判断を支えることです。

- このノードをもっと読むべきか
- どの隣接概念に移るべきか
- この概念には未解決参照がどれだけあるか

## 4. Element-by-element Intent

### 4.1 Knowledge Atlas

詳細な panel 単位仕様は
[`docs/knowledge-atlas-page-spec.md`](/Users/yuta/workspace/projects/researcher/docs/knowledge-atlas-page-spec.md)
を参照。

#### Hero

目的:
この画面が「全文閲覧」ではなく「構造理解」のための画面だと最初に宣言する。

なぜ必要か:
グラフは意味が曖昧になりやすいため、何を見る画面かを先に固定しないと、ユーザーは「なぜ本文がないのか」を疑問に感じるため。

#### Metric Strip

目的:
現在の corpus の密度・欠損・品質状態を一目で把握させる。

なぜ必要か:
Atlas は topology の画面だが、ユーザーは同時に「成熟度」を知りたい。数字により、構造理解を corpus health に接続する。

#### Left Control Panel

目的:
「全体を眺める」から「特定の問いで切る」へ移るための control tower を与える。

なぜ必要か:
大きなグラフは何も絞らないと読めない。検索・tier・domain・degree・guided paths・priority queue により、探索を問い駆動へ変える。

表現原則:

- 説明文より操作を優先する
- desktop では sticky + internal scroll にして graph 面積を守る
- ranking table ではなく quick jump menu として見せる

#### Knowledge Field

目的:
concept の関係構造を空間比較できるようにする。

なぜ必要か:
表やリストでは「近さ」「ハブ性」「島」「欠損の偏り」が読み取りづらいため。

表現原則:

- resolved concept を主面に置く
- unresolved reference は主役にせず halo として扱う
- 説明カードは canvas に重ねず、短い briefing row に分離する
- stage は左右 panel より優先して可視面積を確保する

#### Inspector

目的:
選択中の concept の判断材料をまとめて見せる。

なぜ必要か:
Atlas だけでは node の意味が薄く、Reader だけでは構造が失われるため。その中間として「この concept を読む価値があるか」を短時間で判断させる。

含めるべき情報:

- 概念名
- 1段落説明
- この concept をどう扱うべきかの短い assessment
- inbound / outbound / unresolved
- domains
- key sources
- Reader への導線

注意:
ここは本文画面ではない。長すぎる説明や強すぎる visual hierarchy は、main graph より目立ってはいけない。
desktop では sticky + internal scroll にし、縦長の第2記事にならないようにする。

### 4.2 Article Reader

詳細な panel 単位仕様は
[`docs/article-reader-page-spec.md`](/Users/yuta/workspace/projects/researcher/docs/article-reader-page-spec.md)
を参照。

目的:
選択した concept を連続読書できるようにする。

なぜ必要か:
Atlas は関係を見る画面だが、概念理解は最終的に文章読解が必要だから。

UI 上の責務:

- 記事本文の可読性
- backlinks / outbound の連続移動
- unresolved references の確認

表現原則:

- Atlas と同じ view rail / hero / panel language を使う
- ただし主役は graph ではなく本文に置く
- fixed overlay ではなく、queue と本文を同一 page state で保つ

### 4.3 Wiki Index

目的:
全体の目録を俯瞰し、概念の存在確認と分類確認を行う。

なぜ必要か:
グラフは topology は得意だが網羅確認が苦手だから。

## 5. Design Constraints

この UI では次を守る。

1. 同じ情報を複数の場所で繰り返さない
2. サイドバーは current task を邪魔しない
3. 構造理解と本文理解を混ぜない
4. 説明文は canvas の上に重ねない
5. レイアウトは「重ならない構造」を優先し、CSS の見た目調整で解決しない

## 6. Success Criteria

この UI が成功している状態は次です。

1. 初見のユーザーが 10 秒以内に「Atlas / Reader / Index の違い」を説明できる
2. サイドバーを見たとき、プロダクト紹介ではなく view navigation だと理解できる
3. Atlas でノードを選んだ後、Reader に移るか別ノードに移るかを迷わない
4. レイアウト崩れが起きても情報レイヤーが混線しない

## 7. Current Decision

release 時点では、inspector は drawer ではなく `Knowledge Field` の後段に続く軽量 panel として残す。

理由:

1. graph を見ながら比較判断するには常時可視の detail panel が必要
2. ただし本文の代替にしないため、表示件数を制限し stage の後段に積んで重さを制御する
3. Reader handoff は inspector から最短距離で行えるようにする
