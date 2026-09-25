# reference/ — 臨床・行動科学の参照文献（単発取得）

`raw/` と `wiki/` から独立した、根拠を引くための文献コーパスです。`tools/fetch_reference.py` で手動取得します。
日次パイプライン・Tier 分類・compile_wiki の対象ではなく、launchd にも登録していません。

## 取得の仕組み

キーワード検索を被引用数で並べるだけでは、「希少性」のように一般語と綴りが同じ研究プログラムで無関係な文献が混ざるため、4 つの経路を組み合わせています。

1. **定番文献の名指し** — トピックごとに約 20〜30 本のタイトルを列挙し、語の一致率 0.75 以上で検証してから採用する。見つからなかったものは `missing_landmarks.jsonl` に残る
2. **引用ネットワーク展開** — 定番の総説の参考文献（被引用 30 以上）、核となる実証研究を引用する高被引用論文（主題語で絞る）、OpenAlex の related_works
3. **キーワード検索** — 関連度順 15 件と、被引用 100 以上を被引用順に 10 件（古典の救済）
4. **関連度ゲート** — 定番以外の候補をトピック定義との適合で `core` / `supporting` / `off_topic` に判定する。初回（2026-09-25）は OpenAlex の分野が明らかに外れたものを機械的に除外したうえで、残り約 2,800 件を Claude Code のセッション内でタイトル（必要に応じてアブストラクト）から判定した。API での自動判定（`--gate-model`、既定は Claude Opus 5、従量課金）も使えるが、既定の実行は `--no-gate` でキャッシュ済みの判定だけを使う。`off_topic` は保存せず `excluded.jsonl` に理由付きで残す

アブストラクトが OpenAlex に無い文献は Semantic Scholar と Crossref から補い、それでも無いものは書誌のみで索引に残します（`has_abstract: false`）。

## ファイル

- `index.jsonl` — 1 行 1 文献。`file` は保存直後に実在確認済みのパス（`tools/fetch_reference.py --verify` で再確認できる）
- `papers/<topic>/<slug>-<openalex_id>.md` — frontmatter（書誌）+ アブストラクト。複数トピックに属する文献は先頭トピックのディレクトリに 1 つだけ置く
- `excluded.jsonl` — 関連度ゲートで `off_topic` になった候補（タイトル・理由・取得経路）。監査用
- `missing_landmarks.jsonl` — 名指ししたが OpenAlex で見つからなかった定番文献
- `.cache/` — API 応答のキャッシュ（git 管理外）。再実行でクレジットを消費しない

## index.jsonl の項目

| 項目 | 内容 |
|---|---|
| `openalex_id` | OpenAlex の Work ID（`W...`） |
| `doi` | DOI の URL。無い場合は null |
| `title` / `authors` / `year` | 書誌。著者は先頭 8 名まで、超える場合は `et al.` |
| `cited_by_count` | OpenAlex の被引用数（取得日時点） |
| `paper_type` | OpenAlex の type（`review` / `article` / `book` / `book-chapter`） |
| `evidence_kind` | 根拠の種類の推定: `meta_analysis` / `systematic_review` / `review` / `guideline` / `rct` / `book` / `article`。語句による近似で、確定ではない |
| `abstract` / `has_abstract` / `abstract_source` | 本文と、その出所（`openalex` / `semantic_scholar` / `semantic_scholar_tldr` / `crossref`）。`has_abstract: false` は書誌のみ |
| `oa_topic` / `oa_field` | OpenAlex が付与した主題と分野。無関係な文献の目視確認に使う |
| `topics` | 該当トピック（複数可）: `scarcity` `hedonic` `mastery` `sleep` `bipolar` `cognition` `reward` `avoidance` `suicide` |
| `relevance` | トピックごとのゲート判定 `{verdict: core/supporting/unjudged, reason}`。定番文献は `core` |
| `channels` | トピックごとの取得経路: `landmark` / `refs` / `cites:<seed>` / `related` / `search` / `search_cited` |
| `landmark` | 定番文献として名指しで取ったか |
| `file` / `file_verified` | `reference/papers/...` の相対パスと、保存直後の実在確認の結果 |
| `fetched_at` | 取得日 |

## 検索手順（読み取り専用）

トピックの定番と core だけを、被引用順に見る（最初に引くべき文献）:

```bash
python3 -c 'import json; E=[json.loads(l) for l in open("reference/index.jsonl")]; [print(e["year"], e["cited_by_count"], e["evidence_kind"], e["title"], "->", e["file"]) for e in sorted(E, key=lambda x:-x["cited_by_count"]) if "scarcity" in e["topics"] and e["relevance"]["scarcity"]["verdict"]=="core"]'
```

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
- `relevance` が `supporting` の文献は文脈の補強に留め、主張の根拠には `core` か定番を使う。`unjudged` はゲートが判定できなかったもので、タイトルとアブストラクトを読んでから使う
- 書誌のみ（`has_abstract: false`）の古典は、引用はできるが内容の確認は原典で行う

## 再取得・追加

```bash
python3 tools/fetch_reference.py --dry-run     # 予算の見積り
python3 tools/fetch_reference.py --no-gate     # 全トピックを取り直し、キャッシュ済み判定で索引を再構築する（課金なし）
python3 tools/fetch_reference.py --dump-candidates   # 候補を集めて未判定分を .cache/pending_<topic>.jsonl に書き出す
python3 tools/fetch_reference.py --apply-judgments judgments.jsonl   # {topic,id,verdict,reason} の判定を取り込む
python3 tools/fetch_reference.py --topic sleep # 1 トピックだけ追加・更新（未判定は API 判定＝従量課金）
python3 tools/fetch_reference.py --verify      # index のパス実在と内容一致の確認
```

`.env` の `OPENALEX_API_KEY`（必須）が必要。API 判定を使う場合は `ANTHROPIC_API_KEY`（従量課金）も要る。判定はキャッシュされ、`--apply-judgments` で外部の判定を取り込める。無料枠の残りから翌朝の日次取得分（2,000 クレジット）を差し引いて足りない場合は取得せずに終わる。定番文献の追加は `tools/fetch_reference.py` の `TOPICS[...]["landmarks"]` にタイトルを足す。
