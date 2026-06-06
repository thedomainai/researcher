"""
concepts.json のメタデータをエンリッチする（バックフィル + 継続的エンリッチメント）

既存エントリに以下のフィールドを追加する:
- mechanisms: 中核的メカニズム（分野横断の構造的原理）
- invariant_constraints: 関連する不変制約（sources.yaml の6項目から選択）
- core_questions: 関連するドメインの core_question キー

Usage:
    python tools/enrich_concepts.py [--limit N] [--force] [--dry-run]

    --limit  : 1回あたりの処理上限（デフォルト: 50）
    --force  : 既にエンリッチ済みのエントリも再処理
    --dry-run: 実行せずに対象件数のみ表示
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import httpx

BASE = "/Users/yuta/workspace/projects/researcher"
WIKI_META = os.path.join(BASE, "wiki", "_meta")
WIKI_CONCEPTS = os.path.join(BASE, "wiki", "concepts")
CONCEPTS_PATH = os.path.join(WIKI_META, "concepts.json")

parser = argparse.ArgumentParser(description="Enrich concepts.json metadata")
parser.add_argument("--limit", type=int, default=50, help="Max entries to process (default: 50)")
parser.add_argument("--force", action="store_true", help="Re-enrich already enriched entries")
parser.add_argument("--dry-run", action="store_true", help="Show counts only, don't call API")
args = parser.parse_args()

# ============================================================
# Gemini API 設定
# ============================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    for op_ref in [
        "op://orchestration/Gemini API/credential",
        "op://orchestration/Gemini/credential",
    ]:
        try:
            GEMINI_API_KEY = subprocess.check_output(
                ["op", "read", op_ref],
                stderr=subprocess.DEVNULL,
            ).decode().strip()
            if GEMINI_API_KEY:
                break
        except Exception:
            pass
if not GEMINI_API_KEY and not args.dry_run:
    print("GEMINI_API_KEY が設定されていません")
    sys.exit(1)

GEMINI_MODEL = "gemini-3.5-flash"
MAX_RETRIES = 8
RETRY_BASE_DELAY = 15


def call_llm(system_prompt, user_prompt, max_tokens=4096):
    """Gemini API を呼び出す（429 リトライ付き）"""
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        + GEMINI_MODEL
        + ":generateContent"
    )
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "thinkingConfig": {"thinkingBudget": 0},
        },
    }
    for attempt in range(1, MAX_RETRIES + 1):
        resp = httpx.post(
            url,
            params={"key": GEMINI_API_KEY},
            headers={"content-type": "application/json"},
            json=payload,
            timeout=120,
        )
        if resp.status_code == 429:
            delay = RETRY_BASE_DELAY * attempt
            print(f"    429 rate-limited, retrying in {delay}s (attempt {attempt}/{MAX_RETRIES})")
            time.sleep(delay)
            continue
        if resp.status_code >= 400:
            raise RuntimeError("Gemini API error %d: %s" % (resp.status_code, resp.text[:300]))
        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            raise RuntimeError("No candidates: %s" % json.dumps(data)[:500])
        parts = candidates[0].get("content", {}).get("parts", [])
        return "".join(p.get("text", "") for p in parts)
    raise RuntimeError("Gemini API: max retries exceeded (429)")


def parse_json_response(raw):
    """LLM レスポンスから JSON を抽出する"""
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1]
    if cleaned.endswith("```"):
        cleaned = cleaned.rsplit("```", 1)[0]
    cleaned = cleaned.strip()
    return json.loads(cleaned)


# ============================================================
# 不変制約・ドメイン core_questions 定義
# ============================================================

INVARIANT_CONSTRAINTS = [
    "情報の不完全性",
    "計算資源の有限性",
    "因果関係の不可逆性",
    "複数主体間の利害の不一致",
    "複雑系における創発と予測不可能性",
    "エントロピー増大と秩序維持のコスト",
]

# sources.yaml の research_domains + cross_cutting_themes から core_question を抽出
# パイプラインの安定性のためハードコード（sources.yaml と同期を保つこと）
CORE_QUESTIONS = {
    "neuroscience": "人間の脳はAIとどう共存できるか",
    "cognitive_science": "人間の思考はAIでどう拡張/変容するか",
    "complexity_science": "AI+人間の系はどんな創発的振る舞いをするか",
    "psychology": "個人のウェルビーイングと主体性をどう維持するか",
    "behavioral_economics": "AIが介在する意思決定をどう設計すべきか",
    "evolutionary_biology": "人間-AI共進化の長期ダイナミクスは何か",
    "sociology": "社会制度・権力構造はどう再編されるか",
    "economics": "生産・分配・成長のメカニズムはどう変わるか",
    "organization_science": "AI native組織のアーキテクチャは何か",
    "anthropology": "AI時代の人間の文化・意味世界はどうなるか",
    "philosophy": "AIの存在論的地位と倫理的前提は何か",
    "law": "AI nativeな社会の法的基盤をどう設計するか",
    "hci": "人間-AIの接触面をどう設計するか",
    "systems_engineering": "AI nativeな系の制御・安定性をどう担保するか",
    "history_of_technology": "過去の汎用技術革命からの教訓は何か",
    "business_history": "企業形態・経営手法の歴史的進化パターンから何が学べるか",
    "ai_ml": "AIシステムの動作原理と構造的限界は何か",
    "strategic_management": "なぜ企業間に持続的な競争優位の差が生まれるか",
    "corporate_governance": "所有と経営の分離による利益相反をどう解くか",
    "entrepreneurship": "不確実性下で機会を認識し組織を創造するメカニズムは何か",
    "innovation_management": "技術変革はどう起き、なぜ既存企業は対応に失敗するか",
    "finance_corporate": "資本構成・投資・リスクの最適設計原理は何か",
    "accounting": "組織の経済活動を情報として設計・測定・制御する原理は何か",
    "marketing": "価値の創造・伝達・獲得のメカニズムは何か",
    "human_resource_management": "人間の能力・動機・関係性を組織としてどう設計するか",
    "operations_management": "生産・供給・品質のシステムを最適化する構造原理は何か",
    "international_business": "企業はなぜ・どのように国境を越えて組織するか",
    "business_ethics_csr": "企業は誰のために何のために存在するか",
    "information_systems": "組織における情報技術の採用・影響・設計原理は何か",
    "operations_research": "複雑な意思決定問題をどう数理的に定式化・最適化するか",
    "leadership_ob": "リーダーはどう人・集団・組織に影響を与えるか",
    "project_management": "不確実性と複雑性を伴う一時的組織をどう設計・運営するか",
    "human_ai_collaboration": "人間-AI協働の最適設計は何か",
    "ai_governance": "AI nativeな社会の統治メカニズムは何か",
}

# ============================================================
# メイン処理
# ============================================================

print("=" * 60)
print("concepts.json エンリッチメント")
print("=" * 60)

# concepts.json 読み込み
with open(CONCEPTS_PATH, "r", encoding="utf-8") as f:
    concepts = json.load(f)

print(f"  全エントリ数: {len(concepts)}")

# エンリッチ対象のフィルタリング
if args.force:
    targets = concepts
else:
    targets = [c for c in concepts if not c.get("mechanisms") or not c.get("core_questions")]

print(f"  エンリッチ対象: {len(targets)}件")

if len(targets) > args.limit:
    print(f"  上限 {args.limit} 件に絞って処理します")
    targets = targets[:args.limit]

if args.dry_run:
    print("\n  --dry-run: 処理対象の確認のみ")
    for t in targets[:10]:
        print(f"    - {t['slug']}: {t.get('title_ja', t.get('title_en', ''))}")
    if len(targets) > 10:
        print(f"    ... 他 {len(targets) - 10} 件")
    sys.exit(0)

if not targets:
    print("  全件エンリッチ済みです。")
    sys.exit(0)

# バッチ処理（5件ずつ）
BATCH_SIZE = 5
slug_to_idx = {c["slug"]: i for i, c in enumerate(concepts)}
enriched_count = 0
error_count = 0

SYSTEM_PROMPT = (
    "あなたは学術研究のメタデータ分析者です。与えられた概念情報を分析し、"
    "構造的メカニズム・不変制約・関連ドメインを特定してください。"
    "回答はJSON配列のみで、他のテキストは含めないでください。"
)

core_questions_text = "\n".join(
    f"  - {k}: {v}" for k, v in CORE_QUESTIONS.items()
)
invariant_text = "\n".join(f"  - {c}" for c in INVARIANT_CONSTRAINTS)

for batch_start in range(0, len(targets), BATCH_SIZE):
    batch = targets[batch_start:batch_start + BATCH_SIZE]
    batch_num = batch_start // BATCH_SIZE + 1
    total_batches = (len(targets) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"\n  バッチ {batch_num}/{total_batches} ({len(batch)}件)")

    # 各概念のコンテキストを収集
    concepts_text = ""
    for i, entry in enumerate(batch):
        slug = entry["slug"]
        concept_file = os.path.join(WIKI_CONCEPTS, f"{slug}.md")
        excerpt = ""
        if os.path.exists(concept_file):
            with open(concept_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            excerpt = "".join(lines[:80]).strip()
            if len(excerpt) > 1500:
                excerpt = excerpt[:1500]

        concepts_text += f"""
### [{i+1}] slug: {slug}
タイトル: {entry.get('title_ja', '')} ({entry.get('title_en', slug)})
説明: {entry.get('description', '(なし)')}
関連分野: {', '.join(entry.get('related_domains', []))}
本文冒頭:
{excerpt}
"""

    user_prompt = f"""以下の概念について、メタデータを抽出してください。

{concepts_text}

---

各概念について以下のJSON配列で返してください（JSON以外は出力しないでください）:

[
  {{
    "slug": "元のslugをそのまま返す",
    "mechanisms": ["この概念の中核的メカニズム（日本語、2-4個）"],
    "invariant_constraints": ["関連する不変制約（下記リストから選択、0-3個）"],
    "core_questions": ["関連するドメインキー（下記リストから選択、1-4個）"]
  }}
]

mechanismsの基準:
- 対象（人間/AI/組織）を入れ替えても成立する構造的原理・メカニズム
- 例: "情報の非対称性", "有限合理性", "フィードバックループ", "経路依存性"

不変制約リスト（該当するもののみ選択）:
{invariant_text}

ドメインキーリスト（core_questionが関連するもののみ選択）:
{core_questions_text}
"""

    try:
        raw_response = call_llm(SYSTEM_PROMPT, user_prompt, max_tokens=4096)
        results = parse_json_response(raw_response)

        for result in results:
            slug = result.get("slug", "")
            if slug not in slug_to_idx:
                continue
            idx = slug_to_idx[slug]
            concepts[idx]["mechanisms"] = result.get("mechanisms", [])
            concepts[idx]["invariant_constraints"] = result.get("invariant_constraints", [])
            concepts[idx]["core_questions"] = result.get("core_questions", [])
            enriched_count += 1
            print(f"    {slug}: mechanisms={len(result.get('mechanisms', []))}, "
                  f"constraints={len(result.get('invariant_constraints', []))}, "
                  f"questions={len(result.get('core_questions', []))}")

    except Exception as e:
        error_count += len(batch)
        print(f"    エラー: {e}")

    time.sleep(1)  # API レート制限

# 書き戻し
with open(CONCEPTS_PATH, "w", encoding="utf-8") as f:
    json.dump(concepts, f, ensure_ascii=False, indent=2)

print(f"\n{'=' * 60}")
print(f"完了: エンリッチ={enriched_count}件, エラー={error_count}件")
print(f"保存: {CONCEPTS_PATH}")
print(f"{'=' * 60}")
