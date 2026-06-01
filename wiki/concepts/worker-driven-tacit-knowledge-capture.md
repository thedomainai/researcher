# 現場主導の暗黙知キャプチャ

**現場主導の暗黙知キャプチャ（Worker-Driven Tacit Knowledge Capture）**は、製造現場（ショップフロア）において、作業員が日々の業務やトラブルシューティングの中で培った「暗黙知」を、ボトムアップかつリアルタイムに収集・構造化するための知識管理手法です。

従来のトップダウン型の知識管理システム（KMS）は、時間的制約の厳しい製造現場では機能しにくく、作業員の経験に基づく臨機応変なトラブル対処法（状況に応じた経験的推論）を捉えきれないという課題がありました。本アプローチは、現場の作業員自身を主体とした「社内クラウドソーシング（Internal Crowdsourcing）」の仕組みを導入することで、この課題を解決します。

---

## 提案されているアプローチと設計原則

Yannick Rank氏とFreimut Bodendorf氏（2026年）の研究では、デザインサイエンス研究（DSR）アプローチに基づき、作業員が現場のトラブル（乱れ・異常）を「原因と対策」の構造化された**マイクロケース（Micro-cases）**として、関連メタデータとともに容易に記録できる軽量なシステム（アーティファクト）を開発しました。

このシステムを構築・運用するために、以下の3つの初期設計命題（Design Propositions）が提唱されています。

1. **ワークフローに組み込まれたキャプチャ（Workflow-embedded capture）**
   作業員の通常の作業プロセスの中に知識記録のプロセスをシームレスに組み込むことで、時間的プレッシャーの中でも運用の妨げにならないようにします。
2. **構造化されたマイクロ・コントリビューション（Structured micro-contributions）**
   長文のレポートを求めるのではなく、「原因と対策」を最小限の単位（マイクロケース）としてテンプレート化し、付随するメタデータとともに直感的に入力できるようにします。
3. **分散型の貢献と中央でのキュレーション（Decentralized contributions with central curation）**
   知識の登録自体は現場の各作業員（分散型）に委ねる一方で、情報の信頼性や整理を担保するために、中央の専門家や管理者がコンテンツのキュレーション（検証・分類・統合）を行います。

---

## 本アプローチの意義と今後の評価

製造業における熟練工の退職に伴う技術承継や、現場の突発的なトラブルに対する自己解決力の向上において、このアプローチは非常に有効な手段となります。

今後、ポリマー製造プラントにおける混合研究法（Mixed-method evaluation）を用いた実証実験が計画されており、システムの実用性（Usability）、現場の文脈への適合性（Contextual fit）、そして作業員が継続的に知識を提供し続けるための「持続的な参加（Sustained participation）」の仕組みについて検証が行われる予定です。

---

## 関連概念

* [[知識管理（Knowledge Management）]]
* [[暗黙知と形式知（Tacit and Explicit Knowledge）]]
* [[社内クラウドソーシング（Internal Crowdsourcing）]]
* [[デザインサイエンス研究（Design Science Research）]]
* [[技術承継（Skills Transfer）]]

---

## 参考ソース

* **タイトル**: Capturing Tacit Troubleshooting Knowledge On The Shop Floor: A Worker-Driven Internal Crowdsourcing Approach (2026)
* **ファイルパス**: `raw/Capturing Tacit Troubleshooting Knowledge On The Shop Floor: A Worker-Driven Internal Crowdsourcing Approach`