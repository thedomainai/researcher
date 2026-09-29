# Researcher — AI Native 社会設計のための研究ナレッジベース

## 概要

17の学問分野にまたがるAI関連の最新論文を自動的に収集し、LLMによってwikiにコンパイルするパイプライン。

## ディレクトリ構造

```
researcher/
├── raw/                      # ソースデータ
│   ├── articles/             # Web記事（RSS経由）
│   ├── papers/               # 論文（分野別サブディレクトリ）
│   │   ├── neuroscience/
│   │   ├── cognitive_science/
│   │   ├── complexity_science/
│   │   ├── psychology/
│   │   ├── behavioral_economics/
│   │   ├── evolutionary_biology/
│   │   ├── sociology/
│   │   ├── economics/
│   │   ├── organization_science/
│   │   ├── anthropology/
│   │   ├── religious_studies/
│   │   ├── philosophy/
│   │   ├── law/
│   │   ├── hci/
│   │   ├── systems_engineering/
│   │   ├── history_of_technology/
│   │   ├── human_ai_collaboration/
│   │   └── ai_governance/
│   └── index.jsonl           # メタデータインデックス
├── wiki/                     # LLMがコンパイルしたウィキ
│   ├── concepts/             # コンセプト別記事
│   ├── graph/                # 知識グラフ explorer UI
│   │   └── index.html
│   ├── index.html            # Workspace index UI
│   ├── index.md              # ウィキインデックス
│   ├── reader.html           # 静的HTMLリーダー
│   ├── graph.html            # graph/index.html へのリダイレクト
│   └── _meta/                # メタデータ
│       ├── concepts.json
│       ├── backlinks.json
│       └── concepts-graph.json
├── tools/                    # スクリプト群
│   ├── build_graph.py        # ★ 明示的ナレッジグラフ生成
│   ├── build_graph_ui.py     # ★ ナレッジグラフ explorer 生成
│   ├── build_index_ui.py     # ★ workspace index UI 生成
│   ├── build_reader.py       # 静的HTMLリーダー生成
│   ├── fetch_latest.py       # ★ 最新論文の継続的取得（メインモジュール）
│   ├── daily_pipeline.py     # ★ 取得→日次読書→Wikiコンパイル
│   └── ...
├── config/
│   ├── sources.yaml          # 分野定義・フィルタ設定
│   ├── fetch_state.json      # 前回取得日の状態管理
│   └── com.researcher.fetch-latest.plist  # launchd設定
├── logs/                     # ログ出力先
└── docs/                     # 設計ドキュメント
```

## 使い方

### 最新論文の取得

```bash
# 全分野の最新を取得（前回取得日以降）
python3 tools/fetch_latest.py

# 特定分野のみ
python3 tools/fetch_latest.py --domain neuroscience

# 日付指定
python3 tools/fetch_latest.py --since 2026-04-01

# 確認のみ（ファイル保存なし）
python3 tools/fetch_latest.py --dry-run

# RSS取得をスキップ
python3 tools/fetch_latest.py --no-rss
```

### 日次パイプライン

```bash
# 新着取得、日次リーディングリスト、必要時のWikiコンパイルを一括実行
python3 tools/daily_pipeline.py

# ネットワーク確認のみ（ファイル変更なし）
python3 tools/daily_pipeline.py --dry-run --no-rss
```

### ナレッジグラフの生成

```bash
# concepts-graph.json / backlinks.json を生成
python3 tools/build_graph.py

# 整合性チェックのみ（ファイルは書かない）
python3 tools/build_graph.py --check

# 未解決参照や不正ソース参照もエラー扱いにする
python3 tools/build_graph.py --check --strict
```

### Reader の生成

```bash
# graph メタデータを使って静的 reader.html を更新
python3 tools/build_reader.py
```

### Workspace Index の生成

```bash
# workspace index の index.html を生成
python3 tools/build_index_ui.py
```

### Graph Explorer の生成

```bash
# graph/index.html を生成
python3 tools/build_graph_ui.py
```

### ローカルで確認する

```bash
# wiki/ を localhost:8000 で配信
python3 tools/serve_wiki.py
```

このサーバーは標準エラーが切れていても応答できるようにしてあり、アクセスログは `logs/local-server.log` に追記されます。

### compile パイプライン

日次の記事生成は `compile_articles_cli.py`(増分専用・`claude -p` 経由のサブスクリプション課金)で行う。
既存記事は上書きせず、既存概念に該当した論文は記事末尾に「追加ソース」節を追記する。
新規記事があれば知識グラフと HTML 3 本を自動で再生成する。

```bash
# 未コンパイルの Tier 1/2 論文を 60 件ぶん記事化(既定: 概念抽出・記事生成とも sonnet)
python3 tools/compile_articles_cli.py --limit 60

# 対象を数えるだけ / 分野を限定 / モデルを変える
python3 tools/compile_articles_cli.py --dry-run
python3 tools/compile_articles_cli.py --domain neuroscience --limit 20 --model-write haiku

# 記事を別ディレクトリに書いて品質を試す(index / concepts.json / HTML には触れない)
python3 tools/compile_articles_cli.py --pilot-dir /tmp/pilot --limit 20
```

`compile_wiki.py` は全コーパス再抽出型で、`--incremental` でも Phase 4 が既存記事の内部リンクを
潰すため日次では使わない。以下は HTML の再生成(Phase 5〜8)にだけ使う。

```bash
# full compile(従量課金の API キーが必要。通常は使わない)
source .env && python3 tools/compile_wiki.py

# graph メタデータだけ再生成
python3 tools/compile_wiki.py --phase 5

# reader だけ再生成
python3 tools/compile_wiki.py --phase 6

# graph explorer だけ再生成
python3 tools/compile_wiki.py --phase 7

# workspace index だけ再生成
python3 tools/compile_wiki.py --phase 8

# 既存コンセプトを維持して未生成記事・索引・グラフを増分更新
source .env && python3 tools/compile_wiki.py --incremental
```

### 未コンパイル論文の記事化（claude -p・サブスクリプション課金）

`raw/index.jsonl` で Tier 1/2 かつ未コンパイルの論文を分野ごとにバッチ化し、コンセプト抽出→記事生成→
HTML 再ビルドまでを行います。API キーは使わず、ログイン済みの Claude Code（`claude -p`）で動きます。
既存記事は上書きせず、新しいスラッグだけを追加します。
日次パイプラインが呼ぶのは上の `compile_articles_cli.py` で、こちらは積み残しを大量に消化するときの
一括実行用です(2026-09-29 の 1,695 件はこちらで処理)。既存概念への合流は行わず、常に新規概念として書きます。

```bash
# 30 件ぶん記事化して HTML を再ビルド（既定: 抽出 sonnet / 記事 auto）
python3 tools/pipeline_compile.py --limit 30

# 対象を数えるだけ
python3 tools/pipeline_compile.py --dry-run --limit 300

# 記事もすべて sonnet で書く / 分野を絞る
python3 tools/pipeline_compile.py --limit 60 --article-model sonnet --domain neuroscience

# HTML の再ビルドだけ（記事を手で直したあとなど）
python3 tools/pipeline_compile.py --rebuild-only
```

モデルの使い分け（既定）:

| 処理 | モデル | 理由 |
| --- | --- | --- |
| Tier 分類（`tier_classify_cli.py`） | haiku | 10 件まとめて JSON を返すだけ |
| コンセプト抽出 | sonnet | バッチ 1 回の呼び出しで wiki の構造が決まる |
| 記事生成 | auto = Tier 1 ソースを含めば sonnet、Tier 2 のみなら haiku | 出力トークンの大半を占めるため |

認証切れは終了コード 3（`claude login` で復旧）、利用枠の上限は終了コード 4 で止まり、
それまでの成果は `raw/index.jsonl` / `wiki/_meta/concepts.json` に書き戻されています。
日次パイプラインは `--compile`（plist に設定済み）で 1 日 30 件ずつこの処理を実行します。

### 自動実行の設定（launchd）

`launchd` を推奨します。登録すると毎朝6時に日次パイプラインを実行します。`cron` と同時に設定すると二重実行になります。

```bash
# plistをLaunchAgentsにコピー
cp config/com.researcher.fetch-latest.plist ~/Library/LaunchAgents/

# 登録
launchctl load ~/Library/LaunchAgents/com.researcher.fetch-latest.plist

# 動作確認（手動実行）
launchctl start com.researcher.fetch-latest

# ログ確認
tail -f logs/fetch.log

# 停止する場合
launchctl unload ~/Library/LaunchAgents/com.researcher.fetch-latest.plist
```

### cron の場合

`launchd` を使わない場合のみ設定してください。両方を有効にしないでください。

```bash
crontab -e
# 以下を追加:
0 6 * * * cd /Users/yuta/workspace/projects/researcher && /usr/bin/python3 tools/fetch_latest.py >> logs/fetch.log 2>&1
```

## 対象分野（宗教学を含む）

| カテゴリ | 分野 | 核心の問い |
|---|---|---|
| 基礎科学 | 脳科学 | 人間の脳はAIとどう共存できるか |
|  | 認知科学 | 人間の思考はどう拡張/変容するか |
|  | 複雑系科学 | AI+人間の系はどんな創発的振る舞いをするか |
| 人間科学 | 心理学 | 個人のウェルビーイングと主体性をどう維持するか |
|  | 行動経済学 | 意思決定の設計をどうするか |
|  | 進化生物学 | 人間-AI共進化の長期ダイナミクスは何か |
| 社会科学 | 社会学 | 社会制度・権力構造はどう再編されるか |
|  | 経済学 | 生産・分配・成長のメカニズムはどう変わるか |
|  | 組織科学 | AI native組織のアーキテクチャは何か |
|  | 人類学 | AI時代の人間の文化・意味世界はどうなるか |
| 人文学 | 宗教学 | AI時代に宗教・儀礼・聖性・意味世界はどう変容するか |
| 規範科学 | 哲学 | AIの存在論的地位と倫理的前提は何か |
|  | 法学 | AI nativeな社会の法的基盤をどう設計するか |
| 設計科学 | HCI | 人間-AIの接触面をどう設計するか |
|  | システム工学 | AI nativeな系の制御・安定性をどう担保するか |
| 歴史 | 技術史 | 過去の汎用技術革命からの教訓は何か |
| 横断 | 人間-AI協働 | 協働の設計原理と実証的知見 |
|  | AIガバナンス | AI nativeな社会の統治メカニズム |

## アーキテクチャ

```
[OpenAlex API] ─────┐
                     ├──→ fetch_latest.py ──→ raw/papers/{domain}/ ──→ index.jsonl
[arXiv API] ────────┘          │
                               │
[RSS feeds] ──────────────────→ raw/articles/

raw/ ──→ [LLM compile] ──→ wiki/concepts/*.md ──→ wiki/index.md
                                │
                                ├──→ wiki/_meta/backlinks.json
                                ├──→ wiki/_meta/concepts-graph.json
                                ├──→ wiki/reader.html
                                └──→ wiki/graph/index.html
```

## 依存パッケージ

```bash
pip3 install --user httpx feedparser trafilatura arxiv pyyaml
```
