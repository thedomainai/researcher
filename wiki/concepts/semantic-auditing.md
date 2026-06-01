# 意味的監査フレームワーク

**意味的監査フレームワーク（Semantic Auditing Framework）**とは、AIを支援に用いたソフトウェア開発（AI-Assisted Software Engineering）において、AIが生成したコードが開発者の「元の意図（人間側の設計意図）」を正しく維持しているかを検証・追跡・修正するための評価フレームワークである。

従来のソフトウェアテストでは、生成されたコードが「コンパイルを通過するか」や「テストケースを満たすか」といった**機能的な正確性（Functional Correctness）**に焦点が当てられていた。しかし、これだけではAIが人間の意図しない曖昧な要件の勝手な補完、不要な機能の追加、不確実性の隠蔽などを行い、設計の「意味（セマンティクス）」を改変してしまう問題に対処できない。意味的監査フレームワークは、コードの動作だけでなく、人間とAIの協働プロセスにおける「意味の変容」を追跡可能（Traceable）、レビュー可能（Reviewable）、そして修正可能（Repairable）にすることを目指す。

---

## 期待される役割と背景

AIアシスト開発において、大規模言語モデル（LLM）はしばしば以下のような振る舞いを見せる。

*   **曖昧な要件の勝手な補完**: 明確に定義されていない仕様を、AIが独自の判断で補完して実装してしまう。
*   **不要な機能の導入**: 開発者が求めていない余分なロジックや機能をコードに混入させる。
*   **不確実性の隠蔽**: 本来は人間に確認すべき不確実な仕様について、あたかも確定した仕様であるかのように確信に満ちたコードを生成する。

このような状況では、生成されたプログラムが仮にテストを通過（パス）したとしても、開発者のオリジナルの設計意図から乖離している可能性がある。意味的監査フレームワークは、テストの補完として機能し、AIが生成プロセス中で引き起こした「意味的乖離（Semantic Deviation）」を監査する。

### T-RDE（Test-with-Resonant Deviation Evaluator）
このフレームワークの具体的な提案として、**T-RDE（Test-with-Resonant Deviation Evaluator）**がある。T-RDEは、従来のテスト手法を補強する形で動作し、「共鳴型乖離評価器（Resonant Deviation Evaluator）」を統合することで、人間とAIの協働における意味的変化を評価・監査する仕組みを提供する。これにより、開発者はAIによる暗黙的な仕様変更を検知し、安全に修正（Repair）を行うことが可能となる。

---

## 関連概念

*   [[人間とAIの協働]] (Human-AI Collaboration)
*   [[AIアシストソフトウェア工学]] (AI-Assisted Software Engineering)
*   [[ソフトウェア品質保証]] (Software Quality Assurance)
*   [[意図の整合性]] (Intent Alignment)

---

## 参考ソース

*   **タイトル**: T-RDE: A Semantic Auditing Framework for Repairable Human–AI Collaboration in AI-Assisted Software Engineering (2026)
*   **ファイルパス**: `raw/T-RDE_A_Semantic_Auditing_Framework_for_Repairable_Human-AI_Collaboration_in_AI-Assisted_Software_Engineering.md`