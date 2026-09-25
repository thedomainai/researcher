# 予測的エージェンシー

## 概要

**予測的エージェンシー（Predictive Agency）** は、知性の本質を「環境の予測モデルを内部に構築し、その誤差を最小化することで行動を生成する能力」と定義する統合的な枠組みです。この概念は、生物的知性とAIシステムの両者における適応的な意思決定の核心を説明します。

AI Native社会設計において予測的エージェンシーが重要なのは、単なる反応型システムではなく、**主体的に環境を予測し、不確実性に対処しながら行動できるシステム**を構築するための設計原理を提供するからです。AIエージェント、組織、個人が予測能力を持つほど、より効果的に適応でき、より自律的な行動が可能になります。

## 理論的背景

### 自由エネルギー原理

予測的エージェンシーの理論的基盤は、Karl Fristonが提唱した**自由エネルギー原理（Free Energy Principle）** にあります。この原理によると、すべての適応的システムは、予測と実際の感覚入力のギャップ（予測誤差）を最小化することで組織化されます。

参考: [raw/papers/neuroscience/the-free-energy-principle-a-unified-brain-theory.md](raw/papers/neuroscience/the-free-energy-principle-a-unified-brain-theory.md) | Friston, K.J. (2010)

この原理は脳の機能を統一的に説明し、知覚、学習、行動計画がすべて予測誤差の最小化という共通目標に従うことを示唆しています。

### 予測機械としての脳

Andy Clarkの研究は、脳を「本質的には予測機械」と特徴付けています。脳は感覚入力に反応するのではなく、絶えず環境の次の状態を予測し、その予測と実際の入力を照合することで知覚と行動を統合します。

参考: [raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md](raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md) | Clark, A. (2013)

この視点は、知性が単なる情報処理ではなく、環境との相互作用を通じた予測モデルの継続的な更新であることを強調しています。

### 状況的認知と具体化された知能

単なる内的な予測モデルだけでなく、予測的エージェンシーは**環境との相互作用に根ざしています**。Hutchinsの「Cognition in the Wild」や、Brown、Collins、Duguidの「Situated Cognition」の研究は、知性が状況に埋め込まれ、文化的・物質的アーティファクトと統合されていることを示しています。

参考: [raw/papers/cognitive_science/cognition-in-the-wild.md](raw/papers/cognitive_science/cognition-in-the-wild.md) | Hutchins, E. (1995)  
参考: [raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md](raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md) | Brown, J.S., Collins, A., Duguid, P. (1989)

AIシステムの予測的エージェンシーもまた、ツール、データ、組織文脈から切り離されては機能しません。

## AI Nativeな設計への示唆

### 1. 予測モデルの明示化と監視可能性

AI Nativeシステムは、エージェントが内部的にどのような予測モデルを保持し、どの程度の予測誤差で動作しているかを可視化する必要があります。これにより、不確実性が高い状況を検知し、人間の介入を必要とする局面を動的に判定できます。

### 2. 環境とのフィードバックループの設計

予測的エージェンシーは完全に自己完結的ではなく、環境からの実際の結果フィードバックを得て予測モデルを更新します。AI Native社会では、エージェント、人間、制度的仲介者の間の**継続的なフィードバックループ**を設計することが不可欠です。

参考: [[bounded-rationality-augmentation|Bounded Rationality Augmentation]]では、システムの認知的限界を補完しながらこのフィードバックを効果的に機能させます。

### 3. 状況的適応と文脈学習

予測モデルは汎用的ではなく、特定の状況文脈に適応されるべきです。AIシステムが複数の社会的・物質的文脈で機能する場合、各文脈での予測精度を保ちながら[[distributed-cognition-infrastructure|分散認知インフラ]]の中で相互運用可能である必要があります。

### 4. 予測の失敗に対する堅牢性

不確実性が極度に高い環境では、予測は必ず失敗します。AI Nativeデザインは予測誤差を許容し、失敗時に迅速に代替戦略に切り替わる能力を組み込むべきです。これは[[resilient-sociotechnical-design|レジリエントな社会技術設計]]の核となります。

### 5. 多段階的予測の組織化

複雑な問題空間では、単一レベルの予測では不十分です。[[agentic-era-task-decomposition|エージェンティック時代のタスク分解]]を通じて、短期的な戦術的予測、中期的な戦略的予測、長期的な制度的予測を階層的に組織化することが効果的です。

## 関連コンセプト

- [[bounded-rationality-augmentation|Bounded Rationality Augmentation]]: 予測能力の限界を認識し補完する設計
- [[distributed-cognition-infrastructure|Distributed Cognition Infrastructure]]: 複数のエージェント・システムにわたる予測モデルの分散
- [[agentic-era-task-decomposition|Agentic Era Task Decomposition]]: 複雑な予測問題を階層的に分解
- [[resilient-sociotechnical-design|Resilient Sociotechnical Design]]: 予測失敗への対応力
- [[human-centered-value-alignment|Human-Centered Value Alignment]]: 予測の目標と人間的価値の整合

## 参考ソース

**主要な理論構築**

- Friston, K.J. (2010). "The free-energy principle: a unified brain theory?" *Cited: 6860*. [raw/papers/neuroscience/the-free-energy-principle-a-unified-brain-theory.md](raw/papers/neuroscience/the-free-energy-principle-a-unified-brain-theory.md)

- Friston, K.J. (2009). "The free-energy principle: a rough guide to the brain?" *Cited: 1732*. [raw/papers/neuroscience/the-free-energy-principle-a-rough-guide-to-the-brain.md](raw/papers/neuroscience/the-free-energy-principle-a-rough-guide-to-the-brain.md)

- Clark, A. (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science" *Cited: 5694*. [raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md](raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md)

**状況的・分散的認知**

- Hutchins, E. (1995). "Cognition in the Wild" *Cited: 6865*. [raw/papers/cognitive_science/cognition-in-the-wild.md](raw/papers/cognitive_science/cognition-in-the-wild.md)

- Brown, J.S., Collins, A., Duguid, P. (1989). "Situated Cognition and the Culture of Learning" *Cited: 12892*. [raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md](raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md)

**体化された認知と制御理論**

- Wilson, M. (2002). "Six views of embodied cognition" *Cited: 4434*. [raw/papers/cognitive_science/six-views-of-embodied-cognition.md](raw/papers/cognitive_science/six-views-of-embodied-cognition.md)

- Ashby, W.R. (1956). "An introduction to cybernetics" *Cited: 7186*. [raw/papers/philosophy/an-introduction-to-cybernetics.md](raw/papers/philosophy/an-introduction-to-cybernetics.md)