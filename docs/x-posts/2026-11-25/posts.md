# 今週の論文から作った X のポスト（3 本）

作成日: 2026-11-25。投稿はしていません。型は [x-post-patterns.md](../../x-post-patterns.md) の「A. 論文の核心」＋「図解 1 枚」です。

画像は `build_terminal.py` が、共通の様式 `../terminal_style.py` を使って書き出します（1200×675、出力は 2 倍の解像度）。様式の決まりは [x-post-patterns.md](../../x-post-patterns.md) の「4. 図の様式」にあります。端末（CLI）の画面の様式で、黒に近い無彩色の地・等幅の文字・1px の罫線・ブロック文字の棒を使い、色は青緑 1 色と無彩色だけです（2026-11-26 に決定）。以前の白地・紺の様式は `build_figures.py` に、比較した他の様式は `variants/` に残しています。

使い方: 1 本目に画像を付けて投稿し、2 本目を返信（同じスレッド）として投稿します。文字数は X の数え方（全角 2・URL 23）で 280 以内です。

## 1. セキュリティとセーフティの情報理論的な非対称

画像: [01-security.png](01-security.png)（1200×675、2 倍の解像度で出力）

1 本目（246 字相当）:

```
マルチモーダルモデルの防御は、モデルの中でノイズを抑える方式より、システムが通す情報と行動を絞る方式のほうが、適応的な攻撃に強い限界を課します。前者は攻撃が適応するほど効果が薄れます。
限界: 比較指標 DCI は同論文の提案で、他の研究での検証は確認していません。
```

2 本目:

```
SoK: The Security-Safety Continuum of Multimodal Foundation Models
https://doi.org/10.1145/3846374.3846395
```

画像の代替テキスト: 攻撃者の入力がモデルに届くまでの経路の概念図。a はモデルの内部に防御層があり、帯域 W の入力がすべてモデルに届く。b はモデルの手前に境界の制約があり、実効帯域が W より小さくなる。

## 2. AI ナッジの効果の 37.9% は自己アイデンティティ経由

画像: [02-nudge.png](02-nudge.png)

1 本目（約 225 字相当）:

```
AI ナッジの効果の 37.9% は、行動を直接変える経路ではなく、自己アイデンティティを強める経路を通っていました。インドの通販利用者 406 人、5 週間あけた 2 回の調査です。
限界: 調査データで、調整変数の交互作用は有意ではありません。
```

2 本目:

```
AI-Based Lifestyle Nudges and Sustainable Consumption in Digital Marketplaces: The Mediating Role of Self-Identity Grounded in Reflexive Identity Theory
https://doi.org/10.17632/3zt3b47ks4
```

画像の代替テキスト: AI ナッジから自己アイデンティティへの経路は β=0.312、自己アイデンティティから持続可能な消費行動への経路は β=0.509。間接効果は β=0.159（95% CI 0.110〜0.207）。総効果のうち、直接が 62.1%、自己アイデンティティ経由が 37.9%。決定係数は 0.459。

## 3. 自分で選んだ時点を起点にすると、継続分まで効果になる

画像: [03-event-time.png](03-event-time.png)

1 本目（約 247 字相当）:

```
自分で選んだ時点を起点に、その後の活動の増加を「効果」と読むと、タスクの継続分まで数えます。何も起こさない時刻でも、事後の検索はユーザー内プラセボの 3.42 倍で、実イベントは 4.32 倍でした。
限界: 単一の行動ログでは、追加の仮定なしに分離できません。
```

2 本目:

```
Event-Time Confounding Under Bursty Human Dynamics
https://arxiv.org/abs/2608.21294
```

画像の代替テキスト: ユーザー内プラセボを 1.00 倍とした横棒グラフ。既知のヌル（何も起こさない時刻）は 3.42 倍、実イベント（AI の応答）は 4.32 倍。

## 原典との突き合わせ

ポストと画像の数字・主張は、wiki 記事ではなく、raw にある論文ファイルの要旨（Abstract）の原文と照らしました。本文（要旨より先）は読んでいません。

| ポストの記述 | 原典の要旨の記述 |
|---|---|
| 内側で防ぐ方式は適応的な攻撃で効果が薄れる | model-centric defenses … diminishing effectiveness against increasingly adaptive attacks |
| 情報と行動を絞る方式が強い限界を課す | system-level safeguards that constrain authorized information flow and agent behavior impose stronger limits … by reducing effective bandwidth |
| DCI は提案指標 | a proposed Defense Coverage Index (DCI) to evaluate 15 representative defenses |
| 37.9%・β=0.312・β=0.509・β=0.159・406 人・5 週間 | accounting for 37.9% of the total effect … β = 0.312 … β = 0.509 … β = 0.159 … 406 … five weeks apart |
| 交互作用は有意でない | interaction tests for all three moderators were non-significant and are reported as exploratory |
| 3.42 倍・4.32 倍・5.8% | 3.42 times … compared with 4.32 times for real events … 5.8% of AI responses |
| 単一の行動ログでは分離できない | prove that a single-surface event window cannot separate it from a genuine effect without additional assumptions |

## 確認が残っていること

1. **リンクの種類**: 論文 2 の DOI（10.17632）は、データ公開サービス（Mendeley Data）の登録番号です。学術誌の論文ページではありません。OpenAlex には他の掲載先がありませんでした
2. **論文 1 のリンク**: 出版社の DOI（ACM）を使いました。OpenAlex には arXiv 2411.11195 も同じ論文の版として載っていますが、題名・内容が同じ版かは確認していません
3. **wiki 記事の誤り**: 論文 3 の記事は「4.32 倍のうち 56% を再現」と書いていますが、要旨の 0.56 は「超過分のうち、ヌルが再現する割合」で、3.42÷4.32 ではありません。ポストには 56% を使っていません。記事の記述は直していません
4. **画像 1 は概念図**: 論文の図ではなく、要旨の記述から私が描いた図です。数値は入れていません
5. **今朝の 12 件のうち、他の 9 件は使っていません**: 論文に当たって数字を確かめたのは、この 3 件だけです
