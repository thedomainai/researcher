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
