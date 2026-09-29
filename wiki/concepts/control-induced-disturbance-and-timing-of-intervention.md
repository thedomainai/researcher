# 制御自身が生む撹乱と介入タイミングの原理

## 概要

規制・制御・支援といった介入は、安定化しようとする対象の状態そのものを撹乱することがある。この「制御自身が生む撹乱(control-generated disturbance)」は、外部からの撹乱や系内部に持続的に存在する撹乱とは別の種類のものとして扱う必要がある。加えて、介入の効果は「いつ・どの順序で・どの環境条件下で」行うかによって大きく変わる。

AI Nativeな社会設計では、AIエージェントによる自動調整、インセンティブ設計、従業員支援などの介入層が増える。これらは「良かれと思って入れた制御が系を不安定にする」「支援が脅威として受け取られる」という失敗を起こしやすい。撹乱源の種類、介入の順序、環境状態(豊富/希少)、受け手の利害構造を設計の第一級の変数として扱うことが、この原理の要点である。

## メカニズム

対象が人間・AI・組織・技術のいずれでも、次の構造が共通して現れる。

1. **フィードバックループによる自己撹乱**: 制御器が状態を補正する行為自体がコスト(撹乱)を生み、そのコストがさらに補正を呼び込む。補正が過剰なら撹乱が増幅し、抑制されすぎると必要な是正も行われなくなる。
2. **撹乱源の区別**: 外部撹乱、持続的な内部撹乱、制御生成撹乱では、系が被る負荷や制御負担が異なる。「撹乱がある」という一括りの扱いでは設計を誤る。
3. **環境状態依存の介入効果**: 同じ介入(例:罰則)でも、環境が豊富な状態で入れるか希少な状態で入れるかで、系の挙動が質的に変わる。
4. **順序・タイミング依存**: 制御を先に入れるか、撹乱が先に来るかで、曝露量と制御負担が変わる。
5. **利害非対称による支援の脅威化**: 支援的なシステムでも、受け手の利害構造(受益者か負担者か)によっては脅威として認知され、単一の受容モデルでは説明できない反応が生じる。

## 理論的背景

### 制御生成撹乱のシミュレーション知見

Ziegler(2026)は適応エージェントのシミュレーションで、外部撹乱、持続的内部撹乱、制御生成撹乱を、「規制先行」と「撹乱先行」の順序の下で比較した。検証したパラメータ範囲では、持続的な内部撹乱が最大の曝露と規制負担を生んだ。また、制御器の正の更新が即時の撹乱コストを伴う場合、そのコストを上げると応答は非単調になる。実効撹乱がまず上昇し、中間域では確率的な試行間のばらつきが増え、高コスト域では是正活動が強く抑制される。撹乱源の種別とタイミングが、曝露と制御負担を形作るという結論である。

### 環境状態と罰則のタイミング

Cao、Hua、Liu(2026)は、環境フィードバックを伴うマルチエージェントゲームで、資源状態ごとにインセンティブ強度を結合させたモデルを構築した。理論解析によれば、資源が豊富な状態で罰則を課すと、系は「共有地の悲劇」から完全協力を支える双安定な領域へ移行し得る。一方、資源が希少な状態で罰則を課すと複雑な動学的挙動が生じる。罰則の強さだけでなく「どの環境状態で課すか」が制度設計の要となる。

### 支援が脅威と認知される非対称性

Yadav & Dhar(2026)は、従業員のAI認知(AIA)に関する147件の査読研究を体系的にレビューし、TCCMフレームワークで整理した。ここでの核心は、利害構造の非対称性により、支援的なシステムが脅威として認識される認知的パラドックスである。Kim & Yang(2026)は韓国の政府運営雇用プラットフォームGoyong24のモバイル展開を事例に、役員・管理職・人事担当者で理由構造が異なることを示した。人事担当者は効率上の利点を認めながらも導入に抵抗する。この「理由の非対称性(reason asymmetry)」により、同じ施策が職位によって受益か負担かという異なる意味を帯び、単一の受容モデルでは説明できない。

### 関連する周辺知見

スマートビル制御のレビュー(Ahmed et al., 2026)は、サイバネティクスの枠組みでフィードバックループ、レジリエンス、適応的管理を、不確実・外部的な撹乱への対処として整理している。相互依存する複数目標を均衡させる多目標適応制御の課題も扱っており、制御の設計が複数目標の間で相互作用することを示す。青少年のAI依存に関する扎根理論研究(Gong & Li, 2026)は、発達的ニーズの未充足が補償的利用を促し、それが自己強化的な循環に入る「適応的生態トラップ」を提案している。支援的技術が状態を変え、それが利用を強めるというループの一例として読める。

## AI Nativeな設計への示唆

- **撹乱源を分類して測る**: 外部・内部・制御生成の撹乱を別々に計測し、AIエージェントの調整行為そのものが生むコストをログ化する。
- **制御コストを設計変数にする**: 制御更新の即時コストが非単調な応答を生み得るため、補正強度を単調に上げる前提を置かず、中間域のばらつきと高コスト域での是正抑制を検証する。
- **順序を試験する**: 規制先行と撹乱先行の両方で適応エージェントを評価し、順序による曝露の違いを確認する。
- **介入は環境状態に条件づける**: 罰則やインセンティブは資源の豊富/希少といった状態に応じて設計し、希少状態への一律の強い介入を避ける。
- **利害別に受容を設計する**: 支援AIの導入では、受益者と負担者を分けて理由構造を把握し、負担側への補償や役割再設計を組み込む。
- **自己強化ループを監視する**: 支援が依存や代替を生んでいないか、長期の状態変化を観察する。

## 関連コンセプト

- [[support-induced-skill-substitution-loop]] — 支援が能力形成機会を奪うループという、支援起点の自己撹乱の一形態
- [[incentive-compatible-control-of-hidden-agents]] — インセンティブによる制御の設計
- [[decision-loops-and-layered-decentralized-control]] — フィードバックループと多層制御の構造
- [[capability-outpacing-control-gap]] — 制御が能力に追いつかない問題
- [[multi-layer-independent-control-and-institutional-durability]] — 独立した制御レイヤーによる耐久性
- [[behavior-change-wheel-and-intervention-design]] — 介入設計の枠組み
- [[ai-as-a-job-resource-and-psychological-capital]] — 仕事の資源としてのAIの捉え方
- [[unobservable-control-and-emergent-collusion-limits]] — 制御と可観測性の限界

## 参考ソース

1. A boon or a bane? Demystifying employee AI awareness (AIA): A systematic review and future research agenda — Harish Yadav, Rajib Lochan Dhar (2026)
   File: raw/papers/complexity_science/a-boon-or-a-bane-demystifying-employee-ai-awareness-aia-a-systematic-review-and-.md
2. Proactive Incentive Regulation in Multi-Agent Systems with Environmental Feedback — Xinyang Cao, Shijia Hua, Linjie Liu (2026)
   File: raw/papers/complexity_science/proactive-incentive-regulation-in-multi-agent-systems-with-environmental-feedbac.md
3. The Source of Disturbance Matters: External, Internal, and Control-Generated Noise in Adaptive Regulation — Veronique Ziegler (2026)
   File: raw/papers/complexity_science/the-source-of-disturbance-matters-external-internal-and-control-generated-noise-.md
4. AI-driven systems for advancing smart building infrastructure: An integrated review for energy management, occupant comfort, and cybernetics — Ijaz Ahmed, Rehana Khan, Muhammad Rehan, Mohammed S. Alqahtani, Muhammad Khalid (2026)
   File: raw/papers/complexity_science/ai-driven-systems-for-advancing-smart-building-infrastructure-an-integrated-revi.md
5. The adaptive ecological trap: a grounded theory study of adolescent AI dependency — Gaochang Gong, Guoqiang Li (2026)
   File: raw/papers/corporate_governance/the-adaptive-ecological-trap-a-grounded-theory-study-of-adolescent-ai-dependency.md
6. Mobile Power and Burden: Behavioral Reasoning on Stakeholder Conflicts in Goyong24 Employer Services — Yong-Young Kim, Jie Yang (2026)
   File: raw/papers/corporate_governance/mobile-power-and-burden-behavioral-reasoning-on-stakeholder-conflicts-in-goyong2.md
