# reference/ — 臨床・行動科学の参照文献（単発取得）

`raw/` と `wiki/` から独立した、根拠を引くための文献コーパスです。`tools/fetch_reference.py` で手動取得します。
日次パイプライン・Tier 分類・compile_wiki の対象ではなく、launchd にも登録していません。

## ファイル

- `index.jsonl` — 1 行 1 文献。`file` は保存直後に実在確認済みのパス（`tools/fetch_reference.py --verify` で再確認できる）
- `papers/<topic>/<slug>-<openalex_id>.md` — frontmatter（書誌）+ OpenAlex から復元したアブストラクト
- `no_abstract.jsonl` — 被引用 200 以上だが OpenAlex にアブストラクトが無い文献の書誌のみ（本文は無い）

## index.jsonl の項目

| 項目 | 内容 |
|---|---|
| `openalex_id` | OpenAlex の Work ID（`W...`） |
| `doi` | DOI の URL。無い場合は null |
| `title` / `authors` / `year` | 書誌。著者は先頭 8 名まで、超える場合は `et al.` |
| `cited_by_count` | OpenAlex の被引用数（取得日時点） |
| `paper_type` | OpenAlex の type（`review` / `article`） |
| `evidence_kind` | 根拠の種類の推定: `meta_analysis` / `systematic_review` / `review` / `rct` / `article`。タイトルとアブストラクトの語句による近似で、確定ではない |
| `abstract` | OpenAlex の inverted index から復元した本文 |
| `topics` | 該当トピック（複数可）: `bipolar` `cognition` `sleep` `reward` `avoidance` `hedonic` `mastery` `scarcity` `suicide` |
| `queries` | この文献を返した検索クエリ。`landmark: <title>` はタイトル指定で個別に取ったもの |
| `file` | `reference/papers/...` の相対パス（実在確認済み） |
| `file_verified` | 保存直後の実在確認の結果 |
| `landmark` | 定番文献としてタイトル指定で取ったか |
| `fetched_at` | 取得日 |

## 検索手順（読み取り専用）

トピックで絞る:

```bash
grep '"topics": \[[^]]*"sleep"' reference/index.jsonl | python3 -c 'import sys,json; [print(e["year"], e["cited_by_count"], e["evidence_kind"], e["title"]) for e in map(json.loads, sys.stdin)]'
```

語句で探す（タイトルとアブストラクトの両方に効く）:

```bash
grep -i "akathisia" reference/index.jsonl | python3 -c 'import sys,json; [print(e["year"], e["cited_by_count"], e["evidence_kind"], e["title"], "->", e["file"]) for e in map(json.loads, sys.stdin)]'
```

メタ分析だけに絞る:

```bash
grep '"evidence_kind": "meta_analysis"' reference/index.jsonl | grep -i "sleep deprivation"
```

原文アブストラクトを読む:

```bash
cat "reference/papers/scarcity/poverty-impedes-cognitive-function-w1968966047.md"
```

## 引用するときの注意

- 出典はこの index と `papers/` のアブストラクトで引く。`wiki/` の記事は LLM の要約であり、記事の参考ソース欄のパスは実在しない
- `evidence_kind` は語句による推定。引用前にアブストラクトで研究デザインを確認する
- 薬物療法・副作用（気分安定薬、抗精神病薬、アカシジア）は、アブストラクトだけで結論を出さない。臨床ガイドラインか添付文書で確認する
- 被引用数順のため、古典と最近の総説が混在する。年を見て、より新しい総説があるかを確認する
- 検索語との関連が薄い文献も混ざる（例: `mastery` の運のクエリには投資の運の研究が入る）。タイトルで確認する

## 再取得・追加

```bash
python3 tools/fetch_reference.py --dry-run     # 予算の見積り
python3 tools/fetch_reference.py               # 全トピック（既存はスキップ、topics/queries を追記）
python3 tools/fetch_reference.py --topic sleep # 1 トピック
python3 tools/fetch_reference.py --verify      # index のパス実在と内容一致の確認
```

OpenAlex の API キー（`.env` の `OPENALEX_API_KEY`）が必要。1 回の実行は最大 120 リクエスト（1,200 クレジット）で、無料枠の残りを超える場合は取得せずに終わる。
