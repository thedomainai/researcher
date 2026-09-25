# 技術制度的移行分析

## 概要

技術制度的移行分析（Techno-Institutional Transition Analysis）は、AI のような急進的な技術革新が既存の法制度・規制体系・組織文化・ステークホルダー連携構造とどのように相互作用し、共進化していくかを理解するための分析枠組みです。

単なる技術導入ではなく、**技術と制度の双方向的な相互変形プロセス**として移行を捉えることが特徴です。AI Native な社会設計において、この視点は不可欠です。なぜなら、AI 技術の潜在力を引き出すには、それに適合した新しい制度・ガバナンス・信頼構造を同時に構築する必要があるからです。逆に、古い制度枠では最先端の技術も阻害されてしまいます。

## 理論的背景

### マルチレベル移行モデル（Multi-Level Perspective）

Geels（2002）の研究は、技術移行を三層構造で理解する枠組みを提供しました：

- **ニッチレベル**：革新的な技術・実践が小規模コミュニティで試行錯誤される層
- **レジームレベル**：既存の技術・規制・文化・ビジネスモデルが相互に強化される安定的な秩序
- **ランドスケープレベル**：エネルギー危機や気候変動など、システム全体に影響を及ぼす外部圧力

AI の場合、チャットボット研究がニッチから始まり、規制の空白と市場需要がニッチを拡大し、やがて医療・法務・教育といった専門領域の既存レジームと衝突するプロセスがこれに該当します。

### 社会技術的移行経路（Sociotechnical Transition Pathways）

Geels と Schot（2007）は、技術と社会制度の相互作用の型として複数の経路を類型化しました。AI Native 設計に関連するのは特に：

1. **統合経路（Alignment）**：技術革新と政策・規制が事前に調整される場合
2. **破壊経路（Disruption）**：新技術が既得権益や規制の壁を破壊する場合
3. **再結合経路（Recombination）**：既存要素が新たに組み合わせられる場合

多くの国で AI 規制（EU AI Act など）が策定されているのは統合経路を志向している証拠ですが、技術の急速な進展が政策立案を追い越す「規制ラグ」も問題となります。

### 経路依存性とロックイン（Path Dependence）

Pierson（2000）の指摘する「増加する収穫逓増」現象は、一度採用された技術・制度が自己強化される傾向を説明します。AI の場合、大規模データセットへのアクセス、学習人材の集中、プラットフォーム効果により、特定のアーキテクチャ（例：中央集約型の大言語モデル）がロックインされるリスクがあります。AI Native な設計には、このロックインを意識的に回避する戦略が必要です。

### 技術受容と組織的適応

Venkatesh & Bala（2008）の Technology Acceptance Model 3 は、技術導入時の個人・組織的障壁を分析します。AI ツールの職場導入では、単なる技術性能だけでなく、**使用の容易性・有用性への知覚**、**社会的影響**、**ファシリテーティング条件**（支援体制・トレーニング）が決定的です。

### アクター・ネットワーク・セオリー（ANT）による視点

Latour（2005）の主張する「社会の再編成」では、技術とは単なる道具ではなく、人間と非人間のハイブリッド・ネットワークを構成するものとされます。AI システムの導入は、アルゴリズム、規制文書、人的スキル、組織構造が新たに結び合わされるプロセスであり、各アクターが相互に変形させられていきます。

## AI Native な設計への示唆

### 1. 段階的ニッチ形成と組織的実験

AI 技術を既存レジームに無理に適合させるのではなく、**保護された実験空間**を設けることが重要です。医療 AI が臨床試験の枠組みで段階的に検証されるように、規制当局も産業も相互に学習する場を設計する必要があります。

参考：raw/papers/law/ethical-and-legal-challenges-of-artificial-intelligence-driven-healthcare.md では医療 AI 導入時の法的課題を、（パス未確認） では多職種間の協働の必要性を論じています。

### 2. マルチステークホルダー・ガバナンス

技術（AI 企業）、規制当局、現場の実践家（医師、教員、労働者）、市民社会が同時に参加する意思決定プロセスが不可欠です。一方向的な「上からの規制」では現実の複雑性に対応できません。AI4People（Floridi et al., 2018）が提唱する倫理的枠組みの実装も、こうした多元的対話を前提としています。

### 3. 説明可能性と透明性による信頼構築

[[algorithmic-accountability-stack|アルゴリズミック・アカウンタビリティ・スタック]]の整備と並行して、AI 意思決定の説明責任メカニズムを制度化する必要があります。Obermeyer et al.（2019）の医療アルゴリズムにおける人種バイアス検出事例は、技術的には高精度でも、制度的透明性がなければ害をもたらすことを示しています。

### 4. 規制体系の柔軟性と適応的ガバナンス

固定的な規制では急速に陳腐化します。[[federated-governance-model|分権的ガバナンス・モデル]]や、企業の自主規制と政府規制を組み合わせたハイブリッド・アプローチが有効です。EU AI Act のリスク段階化は、技術革新と規制のバランスを取る試みです。

### 5. 労働・スキル・社会契約の再設計

[[labor-task-substitution-matrix|労働・タスク代替マトリックス]]に基づき、AI による雇用破壊と機会創出を同時にマッピングし、教育・再スキリング・社会保障の体系を統合的に再構想する必要があります。これは純粋な技術問題ではなく、制度設計の問題です。

### 6. 知識・権力の非対称性の可視化

[[power-knowledge-asymmetry-mapping|権力・知識の非対称性マッピング]]により、誰が AI システムの設計・導入・解釈を支配しているのかを明示化し、声を持たないステークホルダー（被験者、患者、労働者）の参加を制度的に保障することが重要です。

## 関連コンセプト

- [[sociotechnical-coevolution|社会技術的共進化]]：技術と社会が相互に形成される動的プロセス
- [[institutional-trust-architecture|制度的信頼アーキテクチャ]]：AI システムと人間・社会の間の信頼基盤
- [[adaptive-niche-construction|適応的ニッチ構築]]：新技術の学習環境としての保護空間の設計
- [[federated-governance-model|分権的ガバナンス・モデル]]：マルチレベルな意思決定構造
- [[algorithmic-accountability-stack|アルゴリズミック・アカウンタビリティ・スタック]]：説明責任の技術的・制度的実装

## 参考ソース

**主要理論文献：**
- raw/papers/history_of_technology/technological-transitions-as-evolutionary-reconfiguration-processes-a-multi-leve.md
- raw/papers/history_of_technology/typology-of-sociotechnical-transition-pathways.md
- raw/papers/sociology/increasing-returns-path-dependence-and-the-study-of-politics.md
- raw/papers/sociology/reassembling-the-social.md

**AI 倫理・規制：**
- raw/papers/law/ai4peoplean-ethical-framework-for-a-good-ai-society-opportunities-risks-principl.md
- raw/papers/law/ethical-and-legal-challenges-of-artificial-intelligence-driven-healthcare.md
- raw/papers/law/dissecting-racial-bias-in-an-algorithm-used-to-manage-the-health-of-populations.md
- raw/papers/law/explainability-for-artificial-intelligence-in-healthcare-a-multidisciplinary-per.md
- raw/papers/law/a-survey-of-methods-for-explaining-black-box-models.md

**組織・受容プロセス：**
- raw/papers/sociology/technology-acceptance-model-3-and-a-research-agenda-on-interventions.md
- raw/papers/history_of_technology/opinion-paper-so-what-if-chatgpt-wrote-it-multidisciplinary-perspectives-on-oppo.md