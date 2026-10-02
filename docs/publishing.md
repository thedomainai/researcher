# 公開サイトと X 配信の運用

ゴール定義: `~/.claude/skills/goal/output/20261001-134336-goal.md`(公開から 12 か月で累計 100 万 PV、日次の人手ゼロ)

## 構成

| 役割 | 実体 | 備考 |
|---|---|---|
| 公開サイト | GitHub Pages(`https://thedomainai.github.io/researcher/`) | `.github/workflows/pages.yml` が push のたびに `tools/build_site.py` で生成して配置する |
| サイト生成 | `tools/build_site.py` → `site/`(git 管理外) | 1 記事 1 URL、クラスター・分野ページ、sitemap、RSS、OGP、JSON-LD、AI 生成の注意書き |
| サイト設定 | `config/site.yaml` | URL・タイトル・6 クラスターと分野の対応・アナリティクス ID |
| 分野の補完 | `tools/classify_domains_cli.py` → `wiki/_meta/domain_overrides.json` | メタデータにも出典にも分野が無い記事を claude -p(haiku)で分類 |
| 日次の公開 | `tools/publish_site.py` | raw/ と wiki/ の変更をコミットして push(= サイト再生成の引き金) |
| X 配信 | `tools/post_x.py` + `config/x_accounts.yaml` + `.env` の鍵 | クラスターごとに 1 日 2 件。本文は claude -p(haiku)。記録は `config/x_post_state.json` |
| アカウント認可 | `tools/x_authorize.py --cluster <key>` | PIN 方式で各アカウントのアクセストークンを `.env` に保存 |
| 日次パイプライン | `tools/daily_pipeline.py`(launchd、毎朝 6:00) | 取得 → Tier 分類 → リーディング → 記事生成 → 分野分類 → publish → X 投稿 |

ローカルでの確認: `python3 tools/build_site.py` のあと `.claude/launch.json` の `site`(port 8010)で `site/` を配信する。

## 一度だけ必要な手作業(アカウント作成を伴うため、エージェントは代行しない)

1. **アナリティクス**: Google Analytics 4 でプロパティを作り、測定 ID(`G-XXXXXXXXXX`)を `config/site.yaml` の `analytics.ga4_measurement_id` に入れる。Cloudflare Web Analytics を使う場合は `cloudflare_beacon_token`。
2. **Search Console**: `https://thedomainai.github.io/researcher/` を URL プレフィックスで登録し、`sitemap.xml` を送信する。
3. **X アカウント**: 6 クラスター分のアカウントを作る(`config/x_accounts.yaml` の `handle` に記入)。各アカウントの設定で「自動化アカウント」のラベルを付け、プロフィールにサイト URL と「論文をもとに AI が生成した記事を配信」の旨を書く。
4. **X Developer App**: 1 つのアプリを作り(Free プラン)、User authentication settings で OAuth 1.0a・Read and write を有効にする。Consumer Key / Secret を `.env` に `X_CONSUMER_KEY` / `X_CONSUMER_SECRET` として置く。
5. **各アカウントの認可**: `python3 tools/x_authorize.py --cluster cognition` のように 6 回。表示された URL をそのアカウントでログインしたブラウザで開き、PIN を入力する。
6. **独自ドメイン(任意)**: `research.thedomainai.com` などを使うなら、DNS に CNAME `research → thedomainai.github.io` を追加し、`gh api -X PUT repos/thedomainai/researcher/pages -f cname=research.thedomainai.com` を実行して `config/site.yaml` の `site.url` を変える。

## 検索エンジンへの通知

- **IndexNow(Bing ほか)**: アカウント不要。`config/site.yaml` の `search.indexnow_key` をサイトの `<key>.txt` として配信し、Pages の配置後に `tools/indexnow.py` が直近 3 日の更新 URL を通知する(workflow の notify ジョブ)。全 URL を送り直すときは `python3 tools/indexnow.py --all`
- **Google**: Search Console で URL プレフィックスを登録し、「HTML タグ」の確認コードを `search.google_site_verification` に入れて push する。確認後に `sitemap.xml` を送信する
- OGP 画像は `config/site_assets/og-<cluster>.png`(1200×630)。クラスター名を変えたら作り直す

## 日次で自動で起きること

- 新しい記事が `wiki/concepts/` に増える → `publish_site.py` がコミットして push → Actions が 1〜2 分でサイトを更新
- `post_x.py` が、鍵のあるアカウントごとに未投稿の記事(新着 → Tier 1 → Tier 2 の順)を 2 件投稿
- 鍵が無いアカウントはスキップされ、パイプラインは止まらない

## 守ること(ゴール定義のアンチゴール)

- 扇情的な見出し・量産ページを作らない。投稿文のプロンプトは落ち着いた文体・誇張禁止で固定している
- 複数アカウントで同じ文面を投げない(クラスターごとに記事が違う。同じ記事を同じアカウントに二度投稿しない)
- 論文に無い主張を断定しない。記事末尾の AI 生成の注意書きと出典リンクを外さない
- X API の有料プランへの切り替えや、従量課金 API キーの使用は、承認を取ってから
- 個人情報・ローカルの実行ログを公開しない(`logs/` は git 管理外にした)

## 計測

- サイト PV: GA4(ボット除外は GA4 の既定で有効)。記事別・流入元別に見る
- X: 各アカウントのアナリティクス(インプレッション・リンククリック)。サイト側では流入元 `t.co` で見分ける
- 投稿の記録: `config/x_post_state.json`(slug ごとの tweet id と日時)

## デザイン(v2、2026-10-01)

- 見た目は `config/site_assets/site.css`、動きは `config/site_assets/site.js`(依存なし)。`tools/build_site.py` の HTML と対で動く。ビルド時に `assets/` へ複製し、内容のハッシュを `?v=` に付ける
- 記事ヘッダーの 1 文要約・実務への含意・英語名は `wiki/_meta/summaries.json`(`tools/summarize_articles_cli.py`、sonnet、日次で未生成分だけ)
- 出典は `raw/index.jsonl` と raw ファイルの frontmatter(doi / url / arxiv_id)から書誌として組み直す。記事本文の内部パスは表示しない
- アトラス(`/graph/`)は `graph.json`、検索パレットは `search.json` を読む。どちらもビルドで生成する
- 審査の記録: 独立レビュワー 2 体(Opus・Sonnet)に Awwwards の配点で 6 ラウンド採点させた。最終は 8.25 / 8.00(合格条件: 両者 8.0 以上かつ重大な指摘 0 件)
- 既知の残り(minor): 概念名と h2 の節名(概要 / 詳細)が抽象的、出典に掲載誌名が無い、検索結果は一致箇所の前後ではなく要約の冒頭を出す、モバイルの記事ヘッダーに近傍グラフが無い(アトラスへのリンクで代替)

## 計測の取得と X の準備(2026-10-02)

- GA4 は稼働中(測定 ID は `config/site.yaml`)。`tools/report_metrics.py` が GA4 と Search Console を読み取り専用で取得し、`config/metrics.json` に日次で追記する。日次パイプラインの最後(7/7)で実行され、失敗しても他の工程には影響しない
- ゴールに対する進捗(累計 PV、線形ペースとの差、必要な 1 日平均)は、同スクリプトの出力で確認できる
- X の 6 アカウントの設定表、プロフィール文、作成から稼働までの手順は `docs/x-accounts.md`
