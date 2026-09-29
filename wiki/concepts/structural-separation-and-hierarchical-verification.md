# 機能分離と階層的検証によるエラー伝播の抑制

## 概要

機能分離と階層的検証によるエラー伝播の抑制とは、多段階で相互依存するシステムにおいて、(1) 制御とデータ(内容)の役割を分け、(2) 各段階に検証層を置き、(3) 中間結果を永続的な成果物に紐付け、(4) 情報統合を構造化することで、誤りの連鎖と機能同士の絡まり合いを抑える設計原理である。

LLMエージェントは長い作業を複数のステップ、ツール、エージェントにまたがって実行する。単一の中枢が判断を担う構成や、自由な対話に頼る協調では、上流の小さな誤りが下流へ静かに波及しやすい。本概念は、Tier 1(不変原理)として、対象がAIでも人間でも組織でも成立する構造的要請を扱う。

## メカニズム

中核は次の4つである。対象を人間、AI、組織、技術のいずれに入れ替えても成り立つよう、構造として整理する。

1. **関心の分離による絡まり回避**: 実行に不可欠な制御(ルーティング、出力形式、終了シグナルなど)と、最適化・改善の対象となる内容を別の表現・別の層に置く。片方の変更が他方を壊す経路を断つ。
2. **階層的検証による誤り伝播の遮断**: 実行を担う層と、経路制御・検証・再計画・終了判断を担う層を分け、段階ごとに確認してから次へ進む。誤りは段階の境界で止められる。
3. **外部化された状態による追跡可能性**: 結論を、根拠となるデータ、計算、中間証拠に結び付けた永続的な成果物として残す。誰が、どの段階で、どの計画世代で生んだ結果かが辿れるため、古くなった証拠の無自覚な再利用を防げる。
4. **推測実行と権威的コミットの二層化**: 速い推測側が先回りして実行し、権威ある側が公式な軌跡を確定させる。速度と正しさの責務を分け、確定されたものだけを正式な状態とする。

これらは、独立した検証を被統治側から構造的に切り離す考え方([[structural-separation-of-verification-from-governed-system]])や、根拠中心で役割を分けた協調([[evidence-grounded-role-separated-agent-coordination]])と同じ方向性を持つ。

## 理論的背景

ソースから得られた主要な知見は次のとおりである。

- **制御・データフロー分離(Control-Data Flow Separation, 2026)**: マルチエージェントLLMのプロンプトは、内容の生成と、コードが依存する実行プロトコル(ルーティング、出力形式、終了シグナル)という2つの役割を同時に担いがちで、内容改善のための編集がプロトコルを壊し、パイプライン全体を失敗させうる。両者は表現が異なる(プロトコルは構造化、内容は非構造の自然言語)という観察に基づき、制御を型付き・検証済みのプログラムオブジェクトとして表現し、タスク関連の言語だけを最適化可能なデータフローとして残す。この分離は、絡まりによる予期せぬ破壊を避けるための構造的要請と位置づけられる。
- **HiRS-Agent(2026)**: リモートセンシングの長期タスクで、単一の決定中枢はタスクの多段階・相互依存性に対応できず、不安定な実行、誤ったツール使用、段階間のエラー伝播を招くとされる。これに対し、動的ルーティング、ステップ単位の検証、再計画、終了制御を担うManager Layerと、ワークフローに沿ってツールを整理するSpecialist Layerの二層構成を提案している。
- **MASGR(2026)**: 医療紹介で、LLMは高頻度の疾患用語に固執して微妙だが重要な緊急性指標を見落とす「情報過負荷」と、緩い対話に依存する協調が招く意味のずれ(semantic drift)や確認バイアスという問題を抱える。紹介を分類ではなく構造化されたグラフ構築として扱い、専門家による調停を組み込むことで対処する。この認知バイアス軽減の仕組みは、医療以外にも転移可能と考えられる。
- **Bioinfoysis(2026)**: バイオインフォマティクスの長期タスクで、各リクエストを永続的な成果物に根ざした解析ランとして表現する。プランナーは実行可能なチェックリストを保持し、ワーカー実行後に返る構造化ハンドオフで保留ステップを改訂する。ハンドオフは中間結果を担当エージェント、チェックリストのステップ、計画世代に結び付けるため、再計画後に古い証拠が黙って再利用されることを防ぐ。制御されたランタイムが生成スクリプトなどを検証する。長期推論ではこの成果物指向アーキテクチャが決定的だと示唆される。
- **Speculative Macro Commit(2026)**: 大きな権威的アクターモデルが公式軌跡を生成し、高速なドラフターモデルが隔離された環境スナップショット上で将来の行動連鎖を予測・実行する二層系である。アクターの次のツール呼び出しがドラフトの先頭行動と一致した場合、事前実行済みの残りのステップとその観測を公式軌跡にコミットする。これは推測と権威的確定の分離の一例だが、並列化の粒度調整にとどまり、一般原理には未到達という位置づけである。
- **When Agents Implement Systems(2026)**: 単一セッションのケーススタディで、LLMコーディングエージェントがシステムレベルの要件(スキーマ設計、非同期オーケストレーション、設定の正しさ、検索フィルタのトレードオフ)で固有の欠陥クラスを導入し、5件の欠陥が制約違反の種類と検出方法で分類された。従来の評価フレームワークではこれらを検出しにくいとされ、多層の検証が必要であることを裏づける。

## AI Nativeな設計への示唆

- **制御は型付きで検証可能に、内容は自由に**: 最適化や生成の対象となる自然言語と、コードが依存するプロトコルを同じ表現に混在させない。制御は検証されたオブジェクトとして扱う。
- **段階ごとの検証点を設ける**: 実行層とは別に、ルーティング・検証・再計画・終了を担う管理層を置き、段階境界で誤りを止める。ただし検証にはコストが伴うため、配分の設計が課題となる([[costly-verification-allocation-tradeoff]])。
- **中間結果を成果物として外部化する**: 結論と根拠、担当、計画世代を紐付けて永続化し、再計画時の古い証拠の混入を防ぐ。
- **自由対話ではなく構造化された統合を使う**: エージェント間の情報統合はグラフなどの構造に載せ、意味のずれや確認バイアスを抑える。
- **推測は隔離し、確定は権威側に限る**: 先回り実行は隔離環境で行い、公式な状態への反映は権威的な照合を経たものに限定する。
- **システムレベルの欠陥を検出できる評価を用意する**: 単純なベンチマークだけでは、スキーマ整合性や非同期安全性といった欠陥は見逃されうる。

## 関連コンセプト

- [[structural-separation-of-verification-from-governed-system]] — 検証機構を被統治系から構造的に分離する原理
- [[evidence-grounded-role-separated-agent-coordination]] — 根拠中心・役割分離型の協調
- [[hierarchical-agent-swarms]] — 階層型マルチレベルLLMエージェント
- [[costly-verification-allocation-tradeoff]] — 検証コストと精度の配分
- [[concentration-driven-systemic-risk-propagation]] — 集中と単一障害点によるリスク伝播
- [[opacity-verification-gap]] — 不透明性と検証可能性のギャップ
- [[message-as-reasoning-trace-and-authority-anchoring]] — 推論の痕跡と権限アンカー

## 参考ソース

1. Evidence, Logic, and Compliance: Multi-Agent Structured Graph Reasoning with Expert Arbitration for Medical Referral — Qi Peng, Yi Cai, Jialin Cui, Tong Zhu, Yujuan Ding (2026)
   File: raw/papers/complexity_science/evidence-logic-and-compliance-multi-agent-structured-graph-reasoning-with-expert.md
2. HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving — Boyang Mu, Zhiwei Wei, Mugen Peng, Wenjia Xu (2026)
   File: raw/papers/complexity_science/hirs-agent-a-hierarchical-multi-agent-system-for-reliable-long-horizon-remote-se.md
3. Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs — Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti, Utkarsh Soni, Yifan Nie (2026)
   File: raw/papers/complexity_science/control-data-flow-separation-stable-prompt-optimization-in-multi-agent-llms.md
4. When Agents Implement Systems: A Case Study in Defects, Detection, and Evaluation Rigor — Phanindra Reddy Madduru (2026)
   File: raw/papers/complexity_science/when-agents-implement-systems-a-case-study-in-defects-detection-and-evaluation-r.md
5. Bioinfoysis Technical Report — Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang (2026)
   File: raw/papers/complexity_science/bioinfoysis-technical-report.md
6. Speculative Macro Commit for Faster Tool-Using Agents — Zeyu Liu, Souvik Kundu, Peter A. Beerel (2026)
   File: raw/papers/complexity_science/speculative-macro-commit-for-faster-tool-using-agents.md
