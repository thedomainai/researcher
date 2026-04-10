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
│   ├── build_reader.py       # 静的HTMLリーダー生成
│   ├── fetch_latest.py       # ★ 最新論文の継続的取得（メインモジュール）
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

### Graph Explorer の生成

```bash
# graph/index.html を生成
python3 tools/build_graph_ui.py
```

### compile パイプライン

```bash
# full compile
source .env && python3 tools/compile_wiki.py

# graph メタデータだけ再生成
python3 tools/compile_wiki.py --phase 5

# reader だけ再生成
python3 tools/compile_wiki.py --phase 6

# graph explorer だけ再生成
python3 tools/compile_wiki.py --phase 7
```

### 自動実行の設定（launchd）

`launchd` を推奨します。`cron` と同時に設定すると二重実行になります。

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

## 対象17分野

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
