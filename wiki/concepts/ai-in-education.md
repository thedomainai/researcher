# 教育におけるAI活用

## 概要

教育におけるAI活用（AI in Education、略称: AIEd）とは、人工知能技術を教育・学習の場に統合し、学習者の体験・成果・満足度を向上させるための取り組みを指す。チャットボット、インテリジェント・チュータリング・システム（ITS）、感情分析、視線追跡、予測分析など、多様なAI技術が教育現場に導入されつつある。

このテーマが重要視される背景には、オンライン教育の急速な普及がある。従来の対面教育では教師が個々の学習者に対応できたが、大規模なオンライン環境では個別対応が困難になる。AIはこのギャップを埋め、認知的・感情的・行動的・社会的な多次元において学習者のエンゲージメントを支援する手段として期待されている。

---

## 詳細

### 主要なAI技術とその役割

#### チャットボットと生成AI（GAI）チャットボット

チャットボットは教育用AIの中でも特に広く研究されている。近年は[[大規模言語モデル]]を基盤とする生成AIチャットボット（例: ChatGPT）が注目されているが、その活用には慎重な設計が求められる。

Su et al.（2026）の研究では、汎用チャットボット（ChatGPT等）と教育設計に基づいたカスタムチャットボットを比較した。汎用チャットボットは即座に完結した回答を提供する傾向があるため、学習者が自ら考える機会を奪う「認知オフローディング」を引き起こす恐れがある。一方、**ソクラテス式問答法**を取り入れたカスタムチャットボットは、学習者が科学的問題解決プロセスを自律的に進めるよう促すことが示された。

#### インテリジェント・チュータリング・システム（ITS）

ITSは学習者の進捗や理解度をリアルタイムで把握し、個別最適化されたフィードバックや課題を提供する。Katalinic et al.（2026）のシステマティックレビュー（2020〜2025年の30件の査読済み研究を対象）では、ITSが認知的エンゲージメントを高め、高等教育機関における学習者満足度に寄与することが確認されている。

#### RAGシステムと教育的透明性

検索拡張生成（Retrieval-Augmented Generation: RAG）システムは、Webベースの教育環境に広く展開されている。Kwarteng et al.（2026）が開発・評価した**SAGE-RAI**は、教育文脈における透明性の重要性を示した。

- ユーザー満足度: 平均評価 4.62/5（92.3%が4〜5つ星と評価）
- **透明性は倫理的要件であるだけでなく、教育的機能**も果たす——学習者が情報源を理解することで、批判的思考と学習の自律性が促進される
- 一方で、「AIによる支援」と「学習者の独立した思考の発達」の間に緊張関係が存在することも明らかになった

### 認知的受動性の問題と認知アライメント

Ahn et al.（2026）は、AIが教育・データリテラシー支援において引き起こしかねない**認知的受動性（cognitive passivity）**の問題を論じた。AIのデフォルトである「包括的かつ一括的な回答」モードは、学習者が自力で考える機会を損なう可能性がある。

これに対して提唱されるのが**認知アライメント（cognitive alignment）**というフレームワークである。これはAIの応答モード（伝達型 vs 熟慮促進型）を、ユーザーの認知的需要に動的・適応的に合わせることで、効果的な人間とAIの協働を実現する考え方である。単純に「AIに熟慮的思考を促進させる」だけでは不十分であり、状況に応じた柔軟な切り替えが重要とされる。

### プロジェクト型学習とAI教育の統合

Gaponov et al.（2026）はロボティクス・AIの学部1年生を対象としたプロジェクト型学習（PBL）「ロボティクス・チャレンジ」の実践を報告した。学生フィードバックに基づく活動形式の改善が、技術的スキルと汎用的スキル（トランスファラブルスキル）の双方に有意な向上をもたらすことが示された。AIそのものを活用するだけでなく、**AIを題材にした教育**においても、設計の工夫が学習効果を左右することが確認された。

### 認知神経科学とAIの接点

Honablue（2026）は、認知神経科学・教育学・AIが交わる領域を整理したテキストブックモジュールを提示した。生物学的知性と人工知能の学習プロセスには構造的な類似点があるとし、確率的ゲーム、バイオメトリクスデータ分析、記憶演習などの活動と、AIの分類・特徴量エンジニアリング・畳み込みニューラルネットワークといった概念を対応させる授業設計を提案している。これは、AIを「使う」だけでなく、**AIの仕組みを理解することが人間の学習理解を深める**という視点を示している。

---

### 課題と留意点

現在の研究が示す主な課題を以下に整理する。

| 課題 | 内容 |
|---|---|
| 認知オフローディング | 汎用AIが即答を与えることで学習者の思考機会が失われる |
| 認知的受動性 | AIの包括的応答が自律的学習・リテラシー発達を阻害する |
| 自律性とAI支援の緊張 | RAGや対話AIが知識へのアクセスを媒介することで、学習の独立性が損なわれるリスク |
| 透明性の欠如 | AIシステムの動作根拠が不明瞭だと批判的評価が困難になる |

---

## 関連概念

- [[インテリジェント・チュータリング・システム]]
- [[大規模言語モデル]]
- [[生成AI（Generative AI）]]
- [[検索拡張生成（RAG）]]
- [[プロジェクト型学習（PBL）]]
- [[認知負荷理論]]
- [[個別最適化学習（Adaptive Learning）]]
- [[ソクラテス式問答法]]
- [[データリテラシー]]
- [[オンライン教育]]

---

## 参考ソース

1. Katalinic, A., Slavuj, V., Jakšić, D. (2026). *Artificial Intelligence in Online Education: A Systematic Review of Its Impact on Learner Engagement and Satisfaction*. DOI: https://doi.org/10.3390/educsci16030389

2. Su, H., Zhang, H., Feng, S. (2026). *Comparing the Impact of Pedagogy-Informed Custom and General-Purpose GAI Chatbots on Students' Science Problem-Solving Processes and Performance Using Heterogeneous Interaction Network Analysis*. arXiv: http://arxiv.org/abs/2604.03022v1

3. Ahn, Y., Kim, N. W., Bach, B. (2026). *Disrupting Cognitive Passivity: Rethinking AI-Assisted Data Literacy through Cognitive Alignment*. arXiv: http://arxiv.org/abs/2604.02783v1

4. Kwarteng, J., Third, A., Mikroyannidis, A., Tarrant, D., Domingue, J. (2026). *SAGE-RAI: Design Patterns for Transparent RAG Systems*. OpenAlex: https://openalex.org/W7126333607

5. Gaponov, I., Collier, O., Charitonidis, A., Tozadore, D. C., Yan, Y. (2026). *Project-Based Learning for Year 1 Students in the Context of Robotics and Artificial Intelligence: A Robotics Challenge*. OpenAlex: https://openalex.org/W7128285888

6. Honablue, X. (2026). *AI Topics Module 2: Education*. DOI: https://doi.org/10.5281/zenodo.18842827