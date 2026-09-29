# 上流の表現完全性が下流の統治を規定する構造

## 概要

「上流の表現完全性が下流の統治を規定する構造」とは、システムの失敗が実行時(モデルの推論や出力の段階)ではなく、現実を機械可読な表象へ変換する上流の段階でほぼ決まっている、という不変原理である。欠落・歪み・語彙の転移といった上流の問題は、監査、説明可能性、コンプライアンスといった下流の統制では回復できない。

ソース[2][3]は「AIシステムは現実に直接作用するのではなく、現実の機械可読な表現に作用する」と述べる。この表現の品質、完全性、文脈的忠実性、正当性が、下流のAIシステムの説明責任の射程(accountability horizon)を決める。

AI Nativeな社会設計にとってこれが重要なのは、AIエージェントが組織や社会の意思決定に組み込まれるほど、「何が見え、何が推論でき、何が統治できるか」が表現インフラによって先に決まるからである。モデルやアウトプットだけを統治対象とする設計は、この上流の決定を見落とす。

## メカニズム

この構造は対象(人間・AI・組織・技術)を入れ替えても成立する、次の三つの原理として整理できる。

### 1. 現実から表象への変換損失

どの主体も現実を直接扱えず、何らかの表象(データ、記述、分類、語彙)を介して判断する。変換の際に文脈や正当性が抜け落ちれば、その表象に基づく判断は、後段がどれほど厳密でも欠落を引き継ぐ。ソース[3]は、失敗が「組織の現実と機械可読な表現とのギャップ」で生じると論じる。

### 2. 隠れた前提の転移(語彙・枠組みの持ち越し)

表象を作る言語は、元の領域の前提ごと持ち込まれる。ソース[1]は、学習・記憶・価値・コンプライアンス・アイデンティティ・信頼といった心理学・組織科学の語彙がAIエージェントのガバナンスに転用されるとき、その領域の「見えない文法」も転移すると論じる。その結果、現在のAIアーキテクチャに存在しない形而上学的実体を前提にした枠組みが作られる、という。

### 3. 上流決定の下流拘束(経路依存性)

上流で採用された表象・語彙・データ構造は、下流の設計選択の範囲を制約する。下流の統制は与えられた表象の範囲内でしか働かないため、上流の欠落を下流の努力で補うことはできない。

これらは人間の制度(官僚制の分類項目)、組織(業務データの定義)、技術(データスキーマ)、AI(学習コーパス)のいずれにも同型で現れる。

## 理論的背景

- **Representation Integrity(表現インテグリティ)**:ソース[2]は、多くのAIガバナンスの失敗がモデル実行前に始まると主張する。既存のガバナンスがモデル・出力・監査・説明可能性・コンプライアンスに集中し、何をAIが知覚し推論し統治し得るかを決める上流の表現基盤を見落としていると指摘する。Representation Economy、SENSE–CORE–DRIVER、Digital Anthropology for Enterprise AIといった枠組みに基づく。
- **統合フレームワーク**:ソース[3]は、Human Reality Gap、Representational Readiness、Representation Integrityなどを統合し、基盤モデルやエージェント技術が進歩してもエンタープライズAIが苦戦し続ける理由を、表現の品質・完全性・文脈的忠実性・正当性に求める。
- **学問領域間の語彙転移問題**:ソース[1]は、ウィトゲンシュタインの言語ゲーム、クーンの理論負荷的観察、ハラウェイの situated knowledge、スターとグリーズマーの境界オブジェクト理論を援用し、問題は用語だけでなく認識論的なものだと論じる。
- **表象インフラの権力性**:ソース[5]は、AIを、文化的・認知的実践を抽出し再加工し再注入する「周辺機械」として捉える。アルバニアのアバターDiella、偏った医療データセット、支配的言語を優遇する自動翻訳などの事例から、AIインフラが「誰が語れるか、何が知識か」という意味生成の条件そのものを再編し、中心と周辺の非対称を再生産すると論じる。技術中立性の語りに対して、situated な倫理を求める。
- **バイアスの構造的解消論**:ソース[6]は、AIバイアスをパラメータ調整などの事後的手当てではなく、データ支配構造の多中心化と設計・ガバナンスの再構築で扱うべきだと主張する。ただし、これは単一の提唱者によるフレームワークであり、「問題を解決した最初の運用システム」という自己評価は本記事では検証済みの事実として扱わない。
- **言語的基盤の示唆**:ソース[4]は、LLMのパーソナリティや思想の伝播が学習コーパスの言語的特性に左右されうるという理論枠組みを提示する。ただし概念的な視点論文であり、独自の実験データはなく、因果的な実証は欠けている。

なお、ソース[2][3]は同一著者による関連論文であり、概念の独立した検証というより一貫した理論的主張として読むべきである。

## AI Nativeな設計への示唆

1. **統治の対象を表象層まで広げる**:モデルや出力だけでなく、現実がどのようにデータや記述に変換されるかを統治の一次対象にする。
2. **表現の四要件を点検する**:品質、完全性、文脈的忠実性、正当性を、導入前の「表現の準備度」(Representational Readiness)として評価する。
3. **語彙を無批判に借用しない**:「学習」「記憶」「価値」「信頼」などの語をエージェントに適用する際は、その語が運ぶ前提が実際のアーキテクチャに成り立つかを確認し、必要なら固有の概念を設計する。
4. **表象の権力性を設計に組み込む**:誰の実践が表象され、誰が欠落しているかを可視化し、影響を受ける当事者が表象の設計に関与できるようにする。
5. **下流統制の限界を前提にする**:監査や説明可能性は、上流の欠落を発見する手段としては有用でも、それを回復する手段とは見なさない。
6. **上流決定を記録し再検討可能にする**:経路依存性があるため、採用した分類・語彙・データ定義を明示的な設計判断として記録し、見直しの経路を残す。

## 関連コンセプト

- [[ai-governance]]
- [[agentic-ai-and-governance]]
- [[ai-governance-stack-semiotics]]
- [[principles-to-practice-legitimacy-gap]]
- [[verification-to-authority-conversion-gap]]
- [[ai-governance-algorithmic-inequality]]
- [[ai-governance-and-auditing]]
- [[ai-governance-and-risk-management]]

## 参考ソース

1. The Disciplinary Language Transfer Problem: How Psychological Vocabulary Produces Governance Failures in AI Agent Deployment — Kymberly Lasser-Chere, Tyler Akidau, Marc Millstone (2026)
   `raw/papers/ai_governance/the-disciplinary-language-transfer-problem-how-psychological-vocabulary-produces.md`
2. Representation Integrity: Why Most AI Governance Failures Begin Before the Model Runs — Raktim Singh (2026)
   `raw/papers/anthropology/representation-integrity-why-most-ai-governance-failures-begin-before-the-model-.md`
3. Why Enterprise AI Fails Before the Model Runs: A Unified Framework for Reality, Representation, and Governance — Raktim Singh (2026)
   `raw/papers/anthropology/why-enterprise-ai-fails-before-the-model-runs-a-unified-framework-for-reality-re.md`
4. The Sociolinguistics of Machine Identity: LLM Personality and Ideology Propagation — Guangni Li (2026)
   `raw/papers/anthropology/the-sociolinguistics-of-machine-identity-llm-personality-and-ideology-propagatio.md`
5. The peripheral machine: Algorithmic sovereignty and the fractured geographies of sense — Edmondo Grassi (2026)
   `raw/papers/anthropology/the-peripheral-machine-algorithmic-sovereignty-and-the-fractured-geographies-of-.md`
6. The Decolonial Intelligence Algorithmic (DIA) Framework: Seventeenth Edition — Christian Ortiz (2027)
   `raw/papers/ai_governance/the-decolonial-intelligence-algorithmic-dia-framework-seventeenth-edition.md`
