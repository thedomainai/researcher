# 意味バージョン束縛による意思決定の監査安定性

## 概要

意味バージョン束縛による意思決定の監査安定性(Meaning-Bound Decision Records for Audit Stability)とは、過去の決定を後から検証可能にするために、各決定が下された時点の意味体系(用語の定義、分類規則、オントロジー)を、その決定自体に束縛して保存するという原理である。

出発点となる論文(Meyman, 2026)は、規制環境下のAIや意思決定システムで生じるコンプライアンス上の失敗の多くが、実行の誤りではなく「意味の不安定性」に由来すると論じる。オントロジー、定義、分類規則が進化すると、監査人は「決定時点でその用語が何を意味していたか」を判定できなくなり、過去の決定が検証不能になる。

AI Nativeな設計では、意思決定が自動化・高速化し、その根拠となる分類や定義もモデル更新やポリシー改定で頻繁に変わる。したがって、決定の記録だけでなく、その決定を支配していた意味を同時に固定する設計が、説明責任の前提条件となる。

## メカニズム

この原理は、意思決定主体が人間・AI・組織・技術システムのいずれであっても成立する構造として整理できる。

1. **決定時点の意味の固定**: 決定が行われる瞬間に有効だった定義・分類規則の特定バージョンを、その決定記録に紐づける。
2. **意味ドリフトによる検証不能化**: 束縛がない場合、定義が更新されるたびに、過去の決定を「現在の意味」で読み直すことになる。これにより当時の判断が誤って見えたり、正当化できなくなったりする。
3. **当時の意味体系での再評価**: 監査可能性とは、過去の決定を、それが下された時点で有効だった意味体系のもとで再評価できることである。
4. **証拠の来歴保存**: 決定に用いた入力や証拠の出所も保存され、意味と証拠の両面から再構成できる状態を保つ。

ソースによれば、バージョン管理は「意味がどう変わったか」を記録するが、個々の決定をそれを支配した意味に結びつけない。同様に、来歴(プロベナンス)標準は「何が起きたか」を記録するが、決定時点の厳密な意味での再評価を保証しない。意味バージョンの束縛は、この欠けた性質を埋めるものと位置づけられる。

## 理論的背景

**監査安定的な意味(Meyman, 2026)**: 中心となる技術ノートは、監査安定的な意味を、従来のオントロジー・バージョニングや来歴管理から区別された固有の性質として定式化する。この論文は、その性質を満たすためにシステムが備えるべき最小条件を規定することを目的としている。なお、提示された抜粋は条件の詳細の手前で途切れているため、具体的な条件項目は本記事では扱わない。

**多次元の決定論的ガバナンス(Meyman, 2026)**: 同著者の別論文は、実行前ゲート(ALLOW / DENY / ABSTAIN を返す事前チェック)が必要ではあるが、それだけでは不十分だと論じる。ゲートは、入力が何を意味するか、適用されたポリシーが有効なものか、証拠に確立された出所があるか、判定を独立に再構成できるか、を単独では確立しない。意味の固定は、こうした多次元のガバナンス要件の一つとして位置づけられる。ただし各条件が害の防止にどう寄与するかの機構は、ソース上では明確でない。

**AIガバナンスの三区分(FERZ Inc. & Meyman, 2026)**: Buyer's Guide は、可視性(ログ・監視・可観測性)、アラインメント(RLHF、ガードレール等)、認可(実行前に、特定の行為が許可されたことを再生可能かつ独立に検証できる証拠を生成するガバナンス)を区別する。意味束縛は、再生可能で検証可能な証拠という要件を支える基盤と解釈できる。ただし、提案フレームワークの十分性は未検証である。

**関連する知見**: AI-HOS(Ramadan, 2026)は、複数の異種AIエージェントが共有文脈上で協調し、ポリシー制約下で行動し、端から端まで監査可能であるべきだと論じる。IRIS(Zhou ら, 2026)は、文書の編集履歴を知的に可視化・対話化する試みで、履歴が「どう変わったか」を辿る側面を示す。これは、変更履歴だけでは決定と意味の対応が得られないという上記の指摘と対比できる。炭素会計のレビュー(Yang, 2026)は、オントロジー駆動のハイブリッドが疎なデータ下での意味的な補完を行うことに触れており、意味体系が実務の判断に組み込まれている領域の例である。

## AI Nativeな設計への示唆

- **決定記録に意味バージョン参照を必須フィールドとして持たせる**: 決定ログには入力・出力・判定に加え、適用された定義・分類規則・ポリシーのバージョン識別子を含める。
- **履歴と束縛を区別する**: 文書やコードのバージョン管理を導入しても、それだけで監査安定性が得られたとは見なさない。決定と意味の対応関係を明示的に保存する。
- **意味の更新を過去に遡及させない**: 定義の改定は新しい決定にのみ適用し、過去の決定は当時の意味で再評価できるようにする。
- **再評価を運用に組み込む**: 監査時に、保存された意味バージョンのもとで判定を再構成できるかを検証手順として定期的に確認する。
- **来歴と意味を併せて保存する**: 証拠の出所と意味体系の双方を保存し、独立した第三者が再構成できる状態を目指す。
- **自律エージェントの境界設計と組み合わせる**: 実行前ゲートだけに依存せず、ゲートが参照する意味とポリシーの有効性も検証可能にする。

## 関連コンセプト

- [[decision-event-governance]] — 意思決定イベントを単位とするガバナンスで、意味束縛の記録単位と整合する。
- [[trust-free-boundary-enforcement-for-autonomous-actors]] — 信頼を前提としない実行境界。ゲートの認可主張を意味と証拠の側面から補強する。
- [[ai-explainability-decision-making]] — 説明可能性は、当時の意味体系での再評価が可能であることを前提とする。
- [[ai-in-manufacturing-and-audit]] — 監査領域でのAI活用と接続する。
- [[ai-decision-support-systems]] — 意思決定支援システムの記録設計に適用できる。
- [[decision-clarity-architecture]] — 意思決定の明確化アーキテクチャと関連する。

## 参考ソース

1. Versioned Meaning: How to Make Ontologies Audit-Stable — Edward Meyman, 2026
   File: raw/papers/hci/versioned-meaning-how-to-make-ontologies-audit-stable.md
2. AI-driven carbon and green accounting: architectures, applications, and the AI sustainability paradox — Qiaorong Yang, 2026
   File: raw/papers/finance_corporate/ai-driven-carbon-and-green-accounting-architectures-applications-and-the-ai-sust.md
3. IRIS: Navigating and Reflecting on Writing Traces Using Intelligent Document Histories — David Zhou, Andrew Chen, John Joon Young Chung, Sarah Sterman, 2026
   File: raw/papers/hci/iris-navigating-and-reflecting-on-writing-traces-using-intelligent-document-hist.md
4. AI-HOS: An AI-Native Hospital Operating System with a Healthcare Agent Interaction Protocol for Context-Centric, Policy-Governed Clinical Workflow Orchestration — Mohamed Salah Ramadan, 2026
   File: raw/papers/hci/ai-hos-an-ai-native-hospital-operating-system-with-a-healthcare-agent-interactio.md
5. Deterministic Governance Is Multi‐Dimensional: Beyond Bounded Execution Gating in AI Systems — Edward Meyman, 2026
   File: raw/papers/hci/deterministic-governance-is-multidimensional-beyond-bounded-execution-gating-in-.md
6. The Enterprise AI Governance Buyer's Guide — FERZ Inc., Edward Meyman, 2026
   File: raw/papers/hci/the-enterprise-ai-governance-buyers-guide.md
