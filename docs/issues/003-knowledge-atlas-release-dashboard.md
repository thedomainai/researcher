# Knowledge Atlas Release Dashboard

## 問い

Knowledge Atlas を「情報が多い graph ページ」ではなく、「次に読むべき概念と次に埋めるべきギャップを決められる分析ダッシュボード」として完成させるには、どの panel を残し、どの情報を圧縮し、どこを主役にすべきか。

## 論点

1. graph が本当に主役になっているか
2. 左右 panel が graph の補助になっているか、それとも競合しているか
3. 画面内の説明文が UI 内に残るべきか、仕様書へ逃がすべきか
4. ダッシュボードとして縦に伸びすぎず、判断に必要な情報密度を保てるか
5. レイアウト崩れを構造的に防げているか

## 論点分解

### 1. graph の主役性

- center column の可視面積が十分か
- stage 下の説明カードが主面の注意を奪っていないか
- right panel が second article になっていないか

### 2. 左右 panel の責務

- 左が「control tower」に限定されているか
- 右が「inspector」に限定されているか
- それぞれが graph の代替になっていないか

### 3. 説明文の置き場所

- 初見ユーザーに必要な framing は main area にあるか
- 繰り返し説明や設計思想が panel に残っていないか

### 4. ダッシュボード性

- full-page screenshot でも縦長の文書に見えないか
- sticky panel と内部 scroll で view height を保てているか
- KPI, controls, graph, inspector の優先順位が明確か

### 5. 構造的ガードレール

- 主要 panel 同士が normal flow / grid で分離されているか
- breakpoint ごとの列構成がテストされているか
- 操作後や resize 後にも no-overlap invariant を維持できるか

## 仮説構築

| 選択肢 | 利点 | 欠点 |
|---|---|---|
| 既存構成を微調整する | 変更量が少ない | 主役の分散と縦長化が解消しない |
| graph を中心に再編し、左右 panel を control / inspector に限定する | 分析ダッシュボードとしての優先順位が明確になる | 仕様書と実装の両方を更新する必要がある |
| 右 panel を完全に drawer 化する | graph 面積は最大化できる | 「比較しながら判断する」体験が落ち、Reader handoff が弱くなる |

## 仮説の評価

| 評価軸 | 微調整 | 再編 | drawer 化 |
|---|---|---|---|
| graph 主役性 | 低い | 高い | 非常に高い |
| inspector 即時性 | 中 | 高い | 低い |
| 初見の分かりやすさ | 中 | 高い | 中 |
| 実装コスト | 低い | 中 | 中 |
| 長期保守性 | 低い | 高い | 中 |

## 結論

release 品質に到達させるには、単なる微調整では足りない。

Knowledge Atlas は次の構成へ再編する。

1. center stage を最大化し、`Knowledge Field` を主役として扱う
2. 左列は `Control Tower` とし、検索・lens・mode・priority queue だけを置く
3. `Inspector` は stage の下に置く compact board とし、選択 node の要約・判断材料・Reader handoff に絞る
4. 画面内で重複していた静的説明は仕様書へ移し、UI 内では必要最小限の framing に圧縮する
5. desktop では左列だけを sticky + internal scroll にし、右側は `stage -> inspector` の分析面として扱う
6. screenshot / DOM invariant テストを breakpoint と操作後状態まで広げる

## ネクストアクション

1. `Knowledge Atlas` の panel 目的を正式仕様に反映する
2. `tools/build_graph_ui.py` を control / stage / inspector の3責務に沿って再編する
3. `tests/test_graph_ui_layout.py` を breakpoint / horizontal overflow / panel collision / interaction 後検証まで強化する
4. 生成物を再ビルドし、スクリーンショットで最終確認する

## 残論点

1. 将来的に inspector を drawer 化するかどうか
2. screenshot baseline を CI に持ち込むかどうか
3. Atlas 内で KPI と corpus health をさらに強く出すか、Hero をより短くするか
