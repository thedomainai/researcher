# Researcher: 自律駆動研究知識ベースエージェント — 仕様

## プロダクトの一言定義

AI Native 社会・組織・システム設計のための研究知識ベースを自律構築するデーモンエージェント。
ユーザーは Obsidian で知識ベースを閲覧し、LLM に質問を投げるだけ。

## 確定事項

| 項目 | 決定 |
|---|---|
| 実行基盤 | ローカル Mac、Cursor ターミナル上で動作 |
| LLM | Anthropic サブスクリプション（Claude API） |
| ウィキ言語 | 日本語 |
| ウィキ粒度 | 1記事 = 1コンセプト |

## ゴール姿

### ユーザー体験

1. **デーモンを起動する** — それ以降、ユーザーの介入なしで知識ベースが成長し続ける
2. **Obsidian を開く** — 構造化されたウィキ、バックリンク、インデックスが自動更新されている
3. **質問する** — ウィキに対して LLM 経由で Q&A する。回答はウィキに蓄積される
4. **触らない** — ウィキの執筆・編集・リンク管理・ヘルスチェックはすべてエージェントの仕事

### システムが自律的に行うこと

| フェーズ | 動作 | 頻度 |
|---|---|---|
| Discover | シード情報源（RSS, arXiv, GitHub）から新しいコンテンツを発見する | 6-24時間ごと |
| Discover | 取り込み済み記事内のリンクから新しい情報源を発見し、ソースリストを自己拡張する | 取り込み時 |
| Evaluate | 発見したコンテンツの関連性・品質・鮮度を LLM で評価し、取り込み判断する | 発見時 |
| Ingest | 評価を通過したコンテンツを取得し、Markdown に変換して `raw/` に保存する | 評価通過時 |
| Compile | `raw/` の新規データから既存コンセプト記事を更新するか、新規コンセプト記事を生成する | 取り込み後 |
| Link | ウィキ内のバックリンク `[[]]` ・クロスリファレンスを自動管理する | コンパイル後 |
| Lint | ウィキ全体の整合性チェック、欠損データの補完、新記事候補の提案 | 日次 |
| Index | ウィキのインデックスファイル・要約を自動更新する | 変更検出時 |

## Evaluate フェーズ: 取り込み判断の設計

### 判断の原則

**「この知見は、AGI 時代に不変な構造的原理か。あるいは、AI が外す制約の分析として価値があるか」**

知識ベースの目的は「AI Native な社会・組織・システムを設計するための構造的理解」である。
Tier 3（条件依存的な現象記述・手法レベルの最適化）は取り込まない。

### Tier 分類（3段階）

| Tier | ラベル | 条件 | 判定 |
|---|---|---|---|
| **1** | 不変原理 | 抽象度テスト + 制約不変テスト + メカニズムテスト を全て満たす | 取り込む |
| **2** | 消滅制約の分析 | AI 時代に外れる制約に依拠するが、その構造的分析として価値がある | 取り込む |
| **3** | スキップ | 条件依存的な現象記述または手法レベルの最適化 | 捨てる |

**3テスト（Tier 1判定）:**
1. **抽象度テスト**: 具体的な対象（人間/現技術/現制度）を除去しても知見が成立するか
2. **制約不変テスト**: 依拠している制約がAGI時代にも存続するか
3. **メカニズムテスト**: 「なぜ」を説明しているか（「何が起きたか」ではなく）

### 取り込み対象のスコープ（15分野）

| 分野 | コア問い |
|---|---|
| 脳科学（neuroscience） | 人間の脳はAIとどう共存できるか |
| 認知科学（cognitive_science） | 人間の思考・判断・学習の構造は何か |
| 組織理論（organization_theory） | 組織はAI時代にどう変容するか |
| 進化生物学（evolutionary_biology） | 協調・競争・利他行動の進化的基盤は何か |
| 経済学・ゲーム理論（economics_game_theory） | AGI時代の資源配分・インセンティブ設計 |
| 複雑系・情報理論（complexity_information） | 複雑系・創発・エントロピーの構造 |
| 哲学・倫理（philosophy_ethics） | AIエージェントの意思決定基準 |
| 社会学（sociology） | 社会構造・制度・規範の形成メカニズム |
| 政治科学（political_science） | 権力・ガバナンス・民主主義の構造 |
| 教育学（education） | 人間の学習・適応の原理 |
| 歴史（history） | 技術変容期の社会変化パターン |
| 法学（law） | AI時代の規制・責任・権利の設計 |
| 心理学（psychology） | 意思決定バイアス・動機付けの構造 |
| AI/ML（ai_ml） | LLM・エージェントシステムの原理と限界 |
| 未来研究（futures） | AGI移行期のシナリオと構造変化 |

**論文タイプ優先順位:** systematic review > meta-analysis > seminal paper > theoretical framework

### 論文取得 API

| API | 役割 | クエリ方法 |
|---|---|---|
| **Semantic Scholar** | 主要論文取得・引用展開（BFS） | `semantic_scholar_queries` in `sources.yaml` |
| **OpenAlex** | 被引用数フィルタ・分野横断検索 | コンセプト ID・分野フィルタ |
| **arXiv** | 最新プレプリント取得 | `arxiv_categories` in `sources.yaml` |

### LLM 評価プロンプト（テンプレート）

```json
{
  "title": "{title}",
  "abstract": "{abstract}",
  "prompt": "以下の3テストを適用してください。\n1. 抽象度テスト: 具体的対象を除去しても知見が成立するか\n2. 制約不変テスト: 依拠する制約がAGI時代にも存続するか\n3. メカニズムテスト: 「なぜ」を説明しているか\n\nJSON: {\"tier\": 1|2|3, \"reasoning\": \"...\", \"key_insight\": \"核心的知見の1行\"}"
}
```

### 重複コンテンツの扱い

1. **原著論文を最優先**: Semantic Scholar 原論文 > プレプリント > 解説記事
2. **重複判定**: S2 paperId または DOI で一致を検出
3. **マージ方針**: wiki/ のコンセプト記事内で複数ソースを参照として統合

## Compile フェーズ: ウィキ設計

### コンセプト記事の構造

1記事 = 1コンセプト。コンセプトとは「独立して理解・説明できる AI/ML の概念単位」。

例:
- `wiki/concepts/transformer.md`
- `wiki/concepts/attention-mechanism.md`
- `wiki/concepts/rlhf.md`
- `wiki/concepts/mixture-of-experts.md`

### 記事テンプレート

```markdown
# {コンセプト名}

## 概要
{コンセプトの1段落要約}

## 背景と動機
{なぜこのコンセプトが必要とされたか}

## 仕組み
{技術的な詳細。数式、アルゴリズム、アーキテクチャ図の説明}

## 関連コンセプト
- [[関連コンセプト1]] — {関係性の説明}
- [[関連コンセプト2]] — {関係性の説明}

## 主要な研究・実装
- {論文タイトル} ({年}) — {1行要約} [→ raw/{path}]
- {ブログ記事タイトル} — {1行要約} [→ raw/{path}]

## 実装メモ
{実装上のポイント、コードスニペット、ライブラリ情報}

## 出典
- raw/papers/{filename}.md
- raw/articles/{filename}.md
```

### 分類体系

LLM が自律的に分類を発展させる。初期シードとして以下のトップレベルカテゴリを設定するが、サブカテゴリは LLM が記事を追加する過程で自然に生成する。

```
wiki/
├── index.md                 # 全コンセプトの一覧と要約
├── concepts/
│   ├── {concept-slug}.md    # 個別コンセプト記事
│   └── ...
├── categories/
│   ├── architectures.md     # アーキテクチャ系コンセプトのインデックス
│   ├── training.md          # 学習手法系
│   ├── inference.md         # 推論・最適化系
│   ├── data.md              # データ・評価系
│   ├── theory.md            # 理論系
│   └── systems.md           # インフラ・システム系
└── _meta/
    ├── backlinks.json       # バックリンクの逆引きインデックス
    ├── concepts-graph.json  # コンセプト間の関係グラフ
    └── compile-log.jsonl    # コンパイル履歴
```

### コンパイルの動作

1. `raw/` に新しいファイルが追加されたことを検出
2. LLM がコンテンツを読み、関連するコンセプトを特定
3. 既存コンセプト記事があれば: 新しい情報で記事を更新（追記・修正）
4. 新しいコンセプトが必要なら: 新規記事を生成
5. `[[バックリンク]]` を更新
6. `index.md` とカテゴリインデックスを更新

### バックリンク

Obsidian の `[[wikilink]]` 形式を使用。

- コンセプト記事内で他のコンセプトを参照するとき `[[attention-mechanism]]` のように記述
- `_meta/backlinks.json` に逆引きインデックスを保持
- Obsidian のグラフビューでコンセプト間の関係を可視化できる

## ディレクトリ構造

```
researcher/
├── raw/                          # ソースドキュメント（取得したまま）
│   ├── articles/                 # Web 記事の Markdown
│   │   └── {slug}.md
│   ├── papers/                   # arXiv 論文の Markdown
│   │   └── {arxiv-id}.md
│   ├── repos/                    # GitHub リポジトリの README + 構造
│   │   └── {owner}-{repo}.md
│   ├── videos/                   # YouTube トランスクリプト
│   │   └── {video-id}.md
│   └── index.jsonl               # メタデータインデックス（append-only）
│
├── wiki/                         # LLM がコンパイルしたウィキ
│   ├── index.md                  # 全コンセプトの一覧と要約
│   ├── concepts/                 # 1ファイル = 1コンセプト
│   │   └── {concept-slug}.md
│   ├── categories/               # カテゴリ別インデックス
│   │   └── {category}.md
│   └── _meta/                    # メタデータ
│       ├── backlinks.json
│       ├── concepts-graph.json
│       └── compile-log.jsonl
│
├── images/                       # ローカル保存した画像
│   └── {source-id}/
│       └── {hash}.{ext}
│
├── output/                       # Q&A・スライド等の生成物
│   ├── qa/                       # Q&A の回答
│   └── slides/                   # Marp スライド
│
├── tools/                        # パイプラインスクリプト
│   ├── daemon.py                 # メインデーモン（オーケストレータ）
│   ├── discover.py               # 情報源の発見・ポーリング
│   ├── evaluate.py               # LLM による取り込み判断
│   ├── ingest.py                 # コンテンツ取得・Markdown 変換
│   ├── compile.py                # raw/ → wiki/ のコンパイル
│   ├── lint.py                   # ウィキのヘルスチェック
│   ├── rate_limiter.py           # レート制限
│   └── index_manager.py          # インデックス管理
│
├── config/
│   ├── sources.yaml              # シード情報源の定義
│   └── discovered_sources.jsonl  # 自動発見された情報源（append-only）
│
├── logs/                         # デーモンのログ
│   └── daemon.log
│
├── docs/                         # プロジェクトドキュメント
│   ├── spec-draft.md             # この仕様書
│   └── crawling-strategy.md      # クローリング戦略の調査結果
│
└── requirements.txt
```

## 実行モデル

### デーモンアーキテクチャ

```
daemon.py（メインループ）
  │
  ├── [毎 6-24h] discover.py
  │     ├── RSS フィードをポーリング
  │     ├── Semantic Scholar API でクエリ実行（15分野 × sources.yaml）
  │     ├── arXiv API で新着論文を検索
  │     ├── GitHub トレンドを取得
  │     └── → 候補リスト（URL + メタデータ）を生成
  │
  ├── [候補ごと] evaluate.py
  │     ├── アブストラクト取得
  │     ├── Claude API で Tier 1/2/3 分類
  │     ├── 重複チェック（S2 paperId / DOI）
  │     └── → ingest（Tier 1/2） / skip（Tier 3）の判定
  │
  ├── [ingest 判定] ingest.py
  │     ├── 全文取得（Trafilatura / Marker）
  │     ├── 画像のローカル保存
  │     ├── raw/{type}/{slug}.md に保存
  │     ├── index.jsonl にメタデータ追記
  │     └── 記事内リンクから新しい情報源を発見 → discovered_sources.jsonl
  │
  ├── [取り込み後] compile.py
  │     ├── 新規 raw ファイルを検出
  │     ├── Claude API で関連コンセプトを特定
  │     ├── 既存コンセプト記事を更新 or 新規作成
  │     ├── バックリンク・インデックスを更新
  │     └── compile-log.jsonl に記録
  │
  └── [日次] lint.py
        ├── バックリンクの整合性チェック
        ├── 孤立コンセプト（参照されていない記事）の検出
        ├── 情報の鮮度チェック（古い SOTA 結果等）
        └── 新記事候補の提案（concepts-graph の空白地帯）
```

### スケジュール

| タスク | 間隔 | 実行条件 |
|---|---|---|
| RSS ポーリング | 6 時間 | 常時 |
| arXiv 検索 | 12 時間 | 常時 |
| GitHub トレンド | 24 時間 | 常時 |
| Evaluate + Ingest | 即時 | Discover が候補を出した時 |
| Compile | 即時 | Ingest が新ファイルを追加した時 |
| Lint | 24 時間 | 常時 |
| Index 更新 | 即時 | Compile or Lint が変更を加えた時 |

### コスト管理

Anthropic API の使用量を追跡し、日次の上限を設ける。

| フェーズ | LLM 使用 | 推定トークン/呼び出し | 推奨モデル |
|---|---|---|---|
| Evaluate | Tier 1/2/3 分類 | ~2K input + ~200 output | Haiku（コスト最小） |
| Compile | 記事生成・更新 | ~10K input + ~2K output | Sonnet（品質とコストのバランス） |
| Lint | 整合性チェック | ~20K input + ~1K output | Haiku |

推定日次コスト（50 記事評価 + 5 記事コンパイル + 1 Lint）: $0.5-2.0 程度

## 未決事項（残）

### 4. Q&A の実行方法

**暫定**: Claude Code のセッション内で質問する。ウィキのインデックスをコンテキストに渡し、必要なコンセプト記事を読み込んで回答する。専用ツールは知識ベースが十分に育ってから検討。

### 5. スケール見通し

**暫定**: 初年度は 500 コンセプト記事 / 1M 語を上限目標とする。ファイルシステムベースで開始し、検索が困難になった時点で埋め込みベクトル + 類似度検索を追加する。

### 6. 情報鮮度の管理

**暫定**:
- 基礎概念（Transformer, Backpropagation 等）は永続。`evergreen: true` フラグを付与
- 時限的情報（SOTA 結果、ベンチマークスコア）は記事内に `last_verified: {date}` を記載
- Lint が 180 日以上未検証の時限的情報を検出し、更新候補としてマーク

### 7. 初期シードの範囲

**暫定**: LLM・言語モデルを中心に、関連する基盤技術（Transformer, 学習手法, 推論最適化）を含む。CV・RL・Robotics は取り込み評価で自然に入ってきた場合のみ。
