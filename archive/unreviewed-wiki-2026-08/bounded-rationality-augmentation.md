# 限定合理性の拡張

## 概要

**限定合理性の拡張（Bounded Rationality Augmentation）** は、人間の認知的制約をAIが補完・拡張することで、意思決定の質と速度を根本的に向上させる設計原理です。これはAI Nativeな社会設計の中核をなすTier 1の不変原理であり、単なる自動化ではなく、人間の判断能力そのものを拡張するアプローチです。

AI Native社会では、認知的制約（時間・記憶・計算能力の限界）を前提としつつ、AIが人間の思考プロセスの各段階に統合され、より良い意思決定を可能にします。このパラダイムシフトは、人間とAIの協働が生産性向上の鍵となることを意味しています。

## 理論的背景

### 限定合理性の基礎

Herbert Simon の「限定合理性（Bounded Rationality）」理論（1955）は、人間が完全な情報処理能力を持たず、現実の制約下で「十分に良い」決定を求めることを示しました。これは古典的な完全合理性の仮説に対する根本的な異議です。

Simon の知見によれば、人間の意思決定は：
- **認知的制約**: 処理可能な情報量に限界がある
- **時間的制約**: 意思決定にかけられる時間が限定される
- **記憶の限界**: 短期記憶容量の制限

### 見通し理論による直感的判断の偏り

Daniel Kahneman と Amos Tversky の**見通し理論（Prospect Theory）**（1979、1992）は、人間の意思決定における系統的なバイアスを実証しました：

- **フレーミング効果**: 問題の提示方法により選択が変わる
- **損失回避**: 利益獲得より損失回避を重視する
- **確率の誤評価**: リスク評価が理論値と乖離する

これらの研究は、人間の判断が論理的ではなく、感情的・直感的であることを示しています。

### 認知的負荷と状況的認知

J. Swellerの**認知負荷理論（Cognitive Load Theory）**によれば、複雑な意思決定では作業記憶が過負荷になり、パフォーマンスが低下します。同時に、Edwin Hutchins の**状況的認知**の研究は、人間の認知は外部リソース（ツール、他者、環境）と分散・統合される性質を示しています。

これらの知見から、AIによる補完的支援は単なる計算援助ではなく、認知的負荷を適切に再配分することで、人間本来の判断能力を引き出すプロセスとなります。

## AI Nativeな設計への示唆

### 1. 認知的負荷の動的再配分

AIは以下の領域で人間の負荷を軽減します：

- **データ処理と要約**: 膨大な情報を構造化し、人間が判断に必要な本質的な情報のみ提示
- **選択肢生成**: 複数のシナリオや代替案を迅速に生成し、人間が評価・選択に専念
- **バイアス可視化**: 見通し理論に基づく潜在的な意思決定バイアスを指摘

### 2. 段階的な意思決定支援（Mixed-Initiative Design）

[[mixed-initiative-orchestration]] の原理に基づき、適切なタイミングで人間とAIの介入を切り替えます：

- **探索段階**: AIが広く代替案を生成
- **評価段階**: 人間が価値判断を行う
- **実行段階**: AIが最適化と実施を支援

### 3. コンテクスト保存と適応的フィードバック

状況的認知の洞察を活かし、AIは：

- 意思決定の文脈（過去の選択、制約条件、目標）を記憶・参照
- 人間が重視する価値基準を学習し、提案をパーソナライズ
- リアルタイムフィードバックにより、決定後の学習を加速

### 4. 透明性と信頼の醸成

限定合理性の拡張が機能するには、人間がAIの推奨理由を理解する必要があります：

- AIの推論過程を明示的に説明（説明可能性）
- 見通し理論など人間心理の原理に基づき、バイアスの源泉を指摘
- 人間の最終的な意思決定権を保持し、AIは助言者の役割に徹する

## 関連コンセプト

この原理は、AI Native設計の他の基本概念と相互に作用します：

- [[cognitive-load-redistribution]]: 認知的負荷を人間とAIの間で最適に配分する実践的フレーム
- [[human-centered-value-alignment]]: 人間の価値判断を尊重しながらAIを統合する倫理的基盤
- [[predictive-agency]]: AIが人間の意図を予測し先制的に支援する機構
- [[mixed-initiative-orchestration]]: 人間とAIが段階的に協働する具体的パターン

## 実践的な設計原則

### 情報設計の最小化
必要な情報は、人間が容易に処理できる量と粒度で提示。Swellerの認知負荷理論に基づき、外部記憶負荷（メモ、表、グラフ）を積極活用。

### バイアス顕在化メカニズム
Kahneman-Tverskyの知見に基づき、潜在的なフレーミング効果や損失回避バイアスを、複数の視点から表示。人間が「自分の判断は本当に最善か」を問い直す機会を提供。

### 権限委譲の明確化
何をAIが自動実行し、何を人間が決定するかを明示。信頼が構築されるにつれ、段階的に人間の判断権を調整する仕組み。

## 参考ソース

- raw/papers/behavioral_economics/a-behavioral-model-of-rational-choice.md (Herbert A. Simon, 1955)
- raw/papers/behavioral_economics/prospect-theory-an-analysis-of-decision-under-risk.md (Kahneman & Tversky, 1979)
- raw/papers/behavioral_economics/advances-in-prospect-theory-cumulative-representation-of-uncertainty.md (Tversky & Kahneman, 1992)
- raw/papers/cognitive_science/cognitive-load-theory-learning-difficulty-and-instructional-design.md (J. Sweller, 1994)
- raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md (Brown, Collins & Duguid, 1989)
- raw/papers/cognitive_science/cognition-in-the-wild.md (Edwin Hutchins, 1995)
- raw/papers/hci/principles-of-mixed-initiative-user-interfaces.md (Eric Horvitz, 1999)
- raw/papers/hci/guidelines-for-human-ai-interaction.md (Amershi et al., 2019)
- raw/papers/hci/artificial-intelligence-and-management-the-automationaugmentation-paradox.md (Raisch & Krakowski, 2021)