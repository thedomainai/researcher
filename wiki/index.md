# Wiki インデックス — AI Native 社会・組織・システム設計

このwikiは、17の学問分野から収集した論文・記事をLLMによってコンセプト別に構造化したナレッジベースです。`fetch_latest.py`により毎日自動で最新論文が追加されます。

## コンセプト記事

### 基礎科学
- [[test-time-compute|テスト時計算と推論の拡張]] — System 1/2とLLMの推論時計算配分
- [[predictive-coding|予測符号化]] — 脳とAIの「予測→誤差→更新」原理
- [[cognitive-load|認知的負荷理論]] — 人間の情報処理容量の制約とAIによる認知オフロード
- [[attention-mechanisms|アテンション機構と操舵可能性]] — AIの注意をどう制御するか

### 人間科学
- [[self-determination-theory|自己決定理論]] — 自律性・有能感・関係性の根本欲求（被引用38,917）
- [[reward-hacking|報酬ハッキングとGoodhart's Law]] — 指標最適化が意図を裏切るメカニズム

### 社会科学
- [[social-construction|社会的構成主義]] — AIが生成する情報が「現実」を構成するプロセス
- [[human-ai-collaboration|人間-AI協働]] — 協働の実証研究と生産性への影響

### 設計科学
- [[coding-agents|エージェントアーキテクチャ]] — LLM+ハーネスのシステム設計原理
- [[resilience-engineering|レジリエンスエンジニアリング]] — 複雑系における安全性と適応能力
- [[interaction-awareness|インタラクション認識]] — AIが対話の文脈を理解する能力

## 分野別ソースマップ

| 分野 | 論文数 | 代表論文（被引用数） |
|---|---|---|
| 脳科学 | 39 | Free Energy Principle — Friston (6,860) |
| 認知科学 | 33 | Situated Cognition — Brown et al. (12,892) |
| 複雑系科学 | 35 | Adaptation in Natural and Artificial Systems — Holland (35,555) |
| 心理学 | 30 | Self-Determination Theory — Deci & Ryan (38,917) |
| 行動経済学 | 28 | Prospect Theory — Kahneman & Tversky (46,176) |
| 法学 | 28 | Dissecting Racial Bias in Algorithms (5,641) |
| 組織科学 | 26 | Dynamic Capabilities — Teece et al. (34,015) |
| HCI | 26 | Mixed-Initiative Interaction (38) |
| 社会学 | 26 | Reassembling the Social — Latour (14,916) |
| 人間-AI協働 | 25 | Navigating the Jagged Frontier — BCG/Harvard (631) |
| AIガバナンス | 25 | Global Landscape of AI Ethics Guidelines (2,368) |
| 哲学 | 21 | An Introduction to Cybernetics — Ashby (7,186) |
| 経済学 | 20 | Skill Content of Technological Change — Autor (2,628) |
| システム工学 | 17 | Resilience Engineering SR群 |
| 進化生物学 | 14 | Niche Construction — Odling-Smee (2,396) |
| 技術史 | 12 | Sociotechnical Transition Pathways (4,912) |
| 人類学 | 11 | Interpretation of Cultures — Geertz (20,907) |
| RSS記事 | 9 | Lilian Weng, Sebastian Raschka 他 |

## 統計

- 論文数: 416
- 記事数: 9
- 合計: 425
- 対象分野: 17
- wikiコンセプト記事: 11
- 自動取得: 毎日6:00 (launchd)
- 最終更新: 2026-04-06

## アーキテクチャ

```
[OpenAlex API] ──┐                    ┌──→ wiki/concepts/*.md
                 ├→ fetch_latest.py →│
[arXiv API] ─────┘     ↓             └──→ wiki/index.md
                  raw/papers/{domain}/
[RSS feeds] ─────→ raw/articles/
                        ↓
                  raw/index.jsonl
```
