# 認知負荷の再分配

## 概要

**認知負荷の再分配（Cognitive Load Redistribution）** は、AI が定型的で認知的に負荷の高いタスクを担当することで、人間の限定された認知資源を、より創造的・関係的・戦略的なタスクへと意図的に再配分するワークフロー設計原理である。

AI Native な社会設計において、この原理は単なる「自動化」ではなく、**人間とAIの認知的役割分担の最適化** を目指している。人間の認知能力は有限であり、ルーチン業務への過度な集中は、複雑な意思決定や創造的問題解決に必要な注意資源を奪う。認知負荷の再分配は、この根本的な制約を認識したうえで、作業フローの構造を再設計し、人間とAIの間で認知的責任を明確に分離する戦略である。

## 理論的背景

### 認知負荷理論の基礎

Sweller の認知負荷理論（Cognitive Load Theory）は、学習と問題解決の効率が、課題によって要求される認知負荷と、個人の認知的作業記憶容量の関係に依存することを示唆している。作業記憶容量は限定的であり、過度な負荷は性能低下と疲労を招く。

参考: raw/papers/cognitive_science/cognitive-load-theory-learning-difficulty-and-instructional-design.md

### 状況的認知と分布認知

Brown、Collins、Duguid による状況的認知論は、概念的知識が、それが学習・使用される状況から抽象化できないことを示唆している。すなわち、認知は個人の脳内に閉じ込められたものではなく、**社会的・物質的環境に分布している** という考え方である。

Hutchins の分布認知論では、複雑な認知作業（例：航海計算）が、個人、道具、組織システム全体に分散していることを実証した。これは AI-人間システムにも直接適用可能である。認知負荷の再分配とは、このような分布認知の観点から、個々のタスクを体系的に再構成し、各アクターに最適な役割を割り当てるプロセスである。

参考: 
- raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md
- raw/papers/cognitive_science/cognition-in-the-wild.md

### 予測脳と自動化の相互作用

Clark の予測処理枠組みによれば、脳は本質的に予測機械であり、受信した感覚入力を予測モデルと照合することで知覚と行動を生成する。この観点から見ると、AI が高度に予測可能な（または計算集約的な）タスクを担当することで、人間の脳は、より複雑な環境適応や創意工夫に必要な予測誤差信号の処理に集中できる。

参考: raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md

### 混合主導インタフェースの設計原理

Horvitz の混合主導ユーザーインタフェース（Mixed-Initiative UI）の原理によれば、システムは単に自動化か手動操作かの二者択一ではなく、人間とコンピュータが動的に責任を交換できる柔軟な設計を採用すべきとされている。認知負荷の再分配は、この原理を認知的領域に適用したものであり、タスクの複雑性や状況に応じて、AIと人間の介入レベルを動的に調整する。

参考: raw/papers/hci/principles-of-mixed-initiative-user-interfaces.md

## AI Nativeな設計への示唆

### 1. タスク分解と役割の明確化

認知負荷の再分配は、まず **タスク空間を可視化し、どの認知負荷がどこに集中しているか** を診断することから始まる。例えば、営業分析業務では、データ収集・集約・形式変換は認知的には機械的だが時間消費的である。これらを AI が担当することで、人間は解釈・戦略立案・クライアント対話に集中できる。

### 2. 段階的な負荷軽減

認知負荷の再分配は、単発的な自動化ではなく、**段階的かつ反復的なプロセス** として設計すべきである。初期段階では低リスクの定型業務から開始し、人間とAIの協働パターンが確立された後、より複雑な領域へ拡張する。

### 3. 認知的スキルの転換と育成

AI に認知負荷を譲渡した場合、人間の職務は自動的に「より高度化」するわけではない。組織は、人間が新たに獲得すべき認知スキル（例：AI出力の解釈、複雑なシナリオ分析）を明示的に定義し、教育・訓練体制を整備する必要がある。

### 4. 状況的文脈の保持

Hutchins の分布認知論から学べるように、AIが部分的なタスクを担当する場合でも、**人間が全体的な状況的文脈を保持し続けることが重要** である。AI は計算を加速するが、人間がシステムの目的と文脈を失えば、AI出力の妥当性判断や創発的な問題発見は困難になる。

### 5. 信頼構築と透明性

混合主導インタフェースの設計において、人間がAIの判断に依存する場合、AI の判断根拠を理解可能な形で提示することが不可欠である。これは単なる「説明可能性」ではなく、人間が自身の認知負荷を適切に配分できるようにするための設計要件である。

## 関連コンセプト

- [[bounded-rationality-augmentation]]：認知的有限性を前提とした意思決定拡張
- [[mixed-initiative-orchestration]]：人間とAIの動的な役割交換メカニズム
- [[agentic-era-task-decomposition]]：複雑タスクの自律的な部分分解
- [[human-centered-value-alignment]]：再配分後も人間的価値を維持する設計原理
- [[distributed-cognition-infrastructure]]：認知を組織全体に分散させるシステム設計

## 参考ソース

- Sweller, J. (1994). "Cognitive Load Theory, Learning Difficulty, and Instructional Design"  
  raw/papers/cognitive_science/cognitive-load-theory-learning-difficulty-and-instructional-design.md

- Brown, J.S., Collins, A., & Duguid, P. (1989). "Situated Cognition and the Culture of Learning"  
  raw/papers/cognitive_science/situated-cognition-and-the-culture-of-learning.md

- Hutchins, E. (1995). "Cognition in the Wild"  
  raw/papers/cognitive_science/cognition-in-the-wild.md

- Clark, A. (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science"  
  raw/papers/cognitive_science/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-scie.md

- Horvitz, E. (1999). "Principles of Mixed-Initiative User Interfaces"  
  raw/papers/hci/principles-of-mixed-initiative-user-interfaces.md

- Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., & Nushi, B. (2019). "Guidelines for Human-AI Interaction"  
  raw/papers/hci/guidelines-for-human-ai-interaction.md

- Raisch, S., & Krakowski, S. (2021). "Artificial Intelligence and Management: The Automation–Augmentation Paradox"  
  raw/papers/hci/artificial-intelligence-and-management-the-automationaugmentation-paradox.md