# クローリング戦略

## 設計判断

### 論点: 情報源をどの優先度で実装するべきか？

AI/ML 分野の情報源は多岐にわたるが、MVP では「最小の実装コストで最大の知識価値を得られる」情報源から着手する。

### 情報源の優先度（実装順序）

| 優先度 | 情報源 | 取得方法 | 理由 |
|---|---|---|---|
| P0 | Web 記事（URL 指定） | Trafilatura / Jina Reader | ユーザーが読みたい記事を即座に取り込める。最小限の実装で最大の価値 |
| P0 | arXiv 論文 | arXiv API + PDF→MD | AI/ML 研究の最重要情報源。構造化 API あり |
| P1 | 研究ブログ（RSS） | feedparser + Trafilatura | DeepMind, OpenAI 等の公式ブログ。RSS で新着検出 |
| P1 | GitHub リポジトリ | GitHub API | README + コード構造。API が整備されている |
| P2 | HuggingFace | huggingface_hub | モデルカード・データセットカード |
| P2 | YouTube | youtube-transcript-api | カンファレンス講演のトランスクリプト |
| P3 | ニュースレター | RSS / Web クロール | キュレーション済みリスト |
| P3 | カンファレンス | Semantic Scholar API | NeurIPS, ICML 等の採択論文 |

### 論点: コンテンツ抽出ツールは何を使うべきか？

| 用途 | 第一選択 | 理由 |
|---|---|---|
| HTML → Markdown | Trafilatura | ローカル実行、高精度本文抽出、メタデータ付き |
| PDF → Markdown | Marker（GPU あり）/ PyMuPDF4LLM（GPU なし） | arXiv 論文の数式・表を正確に変換 |
| YouTube → テキスト | youtube-transcript-api | API キー不要、シンプル |
| RSS パース | feedparser | デファクトスタンダード |

### 論点: ストレージはどう設計するべきか？

handover.md のコンセプトに従い、ファイルシステムベース（Markdown）を基本とする。

```
researcher/
├── raw/                    # ソースドキュメント（取得したまま）
│   ├── articles/           # Web 記事
│   ├── papers/             # arXiv 論文
│   ├── repos/              # GitHub リポジトリ
│   ├── videos/             # YouTube トランスクリプト
│   └── index.jsonl         # メタデータインデックス（append-only）
├── wiki/                   # LLM がコンパイルしたウィキ
│   ├── concepts/           # コンセプト別記事
│   ├── index.md            # ウィキのインデックス
│   └── _meta/              # バックリンク・分類情報
├── images/                 # ローカル保存した画像
├── output/                 # Q&A・スライド等の生成物
├── tools/                  # クローラー・コンパイラ等のスクリプト
├── config/                 # ソース定義・スケジュール設定
└── docs/                   # プロジェクトドキュメント
```

## 技術スタック

### コアライブラリ

| カテゴリ | ライブラリ | バージョン |
|---|---|---|
| HTML → Markdown | trafilatura | latest |
| PDF → Markdown | marker-pdf / pymupdf4llm | latest |
| RSS パース | feedparser | latest |
| YouTube | youtube-transcript-api | latest |
| arXiv API | arxiv | latest |
| GitHub API | PyGithub | latest |
| HuggingFace | huggingface_hub | latest |
| 重複排除 | datasketch | latest |
| HTTP クライアント | httpx | latest |

### 倫理・レート制限

- robots.txt を遵守（urllib.robotparser）
- ドメインごとのレート制限を設定
- User-Agent に連絡先を含める
- 個人利用・研究目的に限定

## RSS フィード一覧

### 研究機関ブログ

| サイト | RSS URL |
|---|---|
| Google DeepMind | `https://deepmind.com/blog/feed/basic/` |
| Google Research | `https://research.google/blog/rss/` |
| OpenAI | `https://openai.com/blog/rss.xml` |

### 個人ブログ

| 著者 | URL |
|---|---|
| Lilian Weng | `https://lilianweng.github.io/index.xml` |
| Jay Alammar | `https://jalammar.github.io/feed.xml` |
| Sebastian Raschka | `https://magazine.sebastianraschka.com/feed` |
| Chip Huyen | `https://huyenchip.com/feed.xml` |
| Eugene Yan | `https://eugeneyan.com/feed.xml` |
