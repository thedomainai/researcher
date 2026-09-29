# 事前態度に濾過される信頼形成と透明性の非対応

## 概要

信頼は、対象の客観的な機能や技術的な透明性によって一意に決まるものではない。人は評価対象に接する前から「AIをどう感じているか」という事前態度を持っており、提示された情報はその態度を通して解釈される。説明の見え方や社会的シグナルも、信頼の水準を左右する。その結果、技術的に検証可能であることと、人間が信頼することは必ずしも対応しない。これが本コンセプトの主張である。

この原理は次の三つのメカニズムで整理できる。

- 事前態度によるフィルタリング
- シグナル検出に関する認知的制約
- 説明可能性を介した信頼の媒介

AI Nativeな社会設計にとって重要なのは、「透明にすれば信頼される」「性能が高ければ採用される」という前提が成り立たない点である。設計者は、検証可能性の確保と信頼の形成を別々の課題として扱う必要がある。

## メカニズム

以下の構造は、評価される対象がAI、組織、技術基盤、エージェントのいずれであっても成り立つと考えられる。

### 1. 事前態度によるフィルタリング

評価者は、提示された特徴を中立に受け取らない。リスク、便益、AIの関与といった手がかりは、評価者が持ち込む心理的なレンズを通って初めて判断材料になる。したがって同じ情報でも、事前態度が異なれば信頼の形成過程と結果が変わる。この構造は、評価対象を人間、組織、システムのどれに置き換えても同じである。

### 2. シグナル検出の認知制約

技術が高い透明性や不変性を備えていても、人間がそれを検出し、理解し、信頼の根拠として使えるとは限らない。信頼を左右するのは、検証可能性そのものよりも、その性質がどう見えるか、社会的にどう示されるかである。ここに透明性と信頼の非対応が生じる。

### 3. 説明可能性を介した信頼の媒介

不確実性が高く、評価者が専門外である状況では、説明や確信度情報が信頼を経由して利用意図に影響する。ただしその効果は一様ではなく、評価者の経験などの条件によって変わる。説明は、内部の完全な理解を与えるものというより、信頼判断の手がかりとして働く。

### 4. 不可視な意思決定への信頼の較正困難

自動的に連鎖する意思決定では、最終結果に至る過程が見えにくい。責任の所在も曖昧になる。人が内部推論を見られない対象への信頼をどう形成し、調整し、時に誤るのかは、構造的な課題として提起されている。

## 理論的背景

### 事前態度(AI feelings)の優位

Makarovaらの研究(2026)は、ヘルスケア向けFinTechプラットフォームを題材にしている。ユーザーは製品の客観的な特徴だけでなく、AIに対する既存の態度、すなわち「AI feelings」を通して評価するという枠組みを提示する。この研究は、リスク・金銭的便益・AIの有無といった製品レベルの手がかりと、AIに対する基本的な志向とを区別する。採用は、プラットフォームが何を伝えるかだけでなく、ユーザーが持ち込む心理的レンズにも依存すると論じる。検証には、事前登録された2×2×2の被験者間実験が用いられた。関連する理論的基盤として、技術受容、自動化への信頼、知覚リスク、価格公正性が挙げられている。

### 透明性と信頼のパラドックス

Kanhai(2026)は、AIとブロックチェーンの統合を扱う。ブロックチェーンは分散性、追跡可能性、透明性、改ざん耐性を備え、AIは予測や自動化を担う。両者の統合は、より安全で信頼できるデジタル環境を作る手段として提示されることが多い。同研究は「技術的な透明性と不変性が高まれば、人間の信頼も高まるのか」と問い、AI信頼、アルゴリズムの透明性、説明可能性、不変性、説明責任に関する20件の研究を質的にテーマ分析している。ソースの核心的知見は、技術的透明性と人間の信頼の非対応が、認知的制約と社会的シグナル検出に根ざす不変的なメカニズムだという点にある。

### 説明可能性と信頼の媒介

Tran & Delina(2026)は、AI支援採用の候補者ランキングを対象に、人事関連の回答者(N = 145)への匿名調査と無作為化シナリオで検証した。比較したのは、説明なしのランキングと、簡潔な理由と確信度情報を伴うランキングである。主な知見は次のとおり。

- 実務でのAI経験は、説明が信頼に与える効果を有意に調整した。
- 利用意欲に対しては、この調整の傾向は弱かった。
- 知覚された公正性については、調整は有意でなかった。
- AI利用意図は、信頼、知覚された有用性、人間による制御などと関連していた。

つまり、説明の効果は評価者の経験という条件に左右される。

### 生成元の知覚可能性

Linら(2026)は、観光ソーシャルメディアのコンテンツを題材に、AI生成、人間生成、人間とAIの協働という三つのモードへの消費者反応を分析する概念フレームワークを提示している。利用と満足理論および情報源信頼性理論に依拠し、エンゲージメント、コンテンツの信頼性、プラットフォーム適合性、ガバナンスリスクの四つの次元を扱う。AI生成コンテンツは量的なエンゲージメントで優位にある一方、情緒的共鳴などで限界があると分析される。信頼性評価と感情的接続が、生成元がどう知覚されるかに媒介されるという点は、本コンセプトと整合する。

### エージェント型AIにおける信頼較正

Farazi(2026)は、複数のAIエージェントが自動的に協働して複雑なタスクを遂行するシステムを扱う。財務予測、サプライチェーン管理、採用判断のような重要業務に導入される状況で、従業員は内部推論を見ることも十分に理解することもできない。そのようなシステムをどの程度信頼するかという問いを立て、エージェント型AIの信頼較正(TCAS)に関する研究課題を提案している。ソースが示す核心は、非透明な自動意思決定への信頼が、人間認知の根本的な制約に関わる構造的な問題だという点である。

## AI Nativeな設計への示唆

1. **検証可能性と信頼を分けて設計する。** 透明性や不変性といった技術特性を備えても、信頼が自動的に得られるとは限らない。信頼を得る仕組みは別途設計する。
2. **利用者の事前態度を前提にする。** 機能の訴求だけでなく、利用者がAIに抱く態度を考慮したメッセージ設計と導入が必要になる。リスクや便益の提示も、態度というレンズを通って解釈される。
3. **説明は、受け手の経験に合わせて提供する。** 簡潔な理由や確信度情報は信頼の手がかりになるが、その効果は経験によって変わる。一律の説明ではなく、受け手に応じた出し方を検討する。
4. **人間による制御を維持する。** 利用意図は人間による制御の知覚とも関連している。自律的な意思決定ほど、責任の所在と介入可能性を見える形にしておく。
5. **信頼の較正を継続的な課題として扱う。** 不可視な連鎖的意思決定では、信頼が過剰にも過小にもなりうる。導入時だけでなく運用中も信頼の水準を観察し、調整する。
6. **生成元の見え方を設計対象にする。** AI、人間、協働のどれが生成したかの知覚は、信頼性評価と感情的接続を左右する。開示のあり方は信頼設計の一部である。

## 関連コンセプト

- [[ai-ethics-trust-transparency]] — AIの倫理・信頼・透明性
- [[ai-transparency-and-explainability]] — AIの透明性と説明可能性
- [[algorithmic-transparency]] — アルゴリズムの透明性
- [[algorithmic-transparency-paradox]] — アルゴリズム透明性パラドックス
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失
- [[multidimensional-trust-formation-and-oversight]] — 多次元的な信頼形成と監督
- [[human-ai-trust]] — AIへの信頼
- [[human-ai-interaction-and-trust]] — 人間とAIの相互作用と信頼
- [[algorithm-aversion-and-transparency-in-healthcare]] — ヘルスケアにおけるアルゴリズム嫌悪と透明性
- [[ai-disclosure-and-organizational-trust]] — AI関与開示と組織の信頼性
- [[fluency-induced-trust-miscalibration]] — 流暢性による信頼キャリブレーションの歪み
- [[responsible-control-anchor-under-agentic-autonomy]] — 主体的自律システムにおける責任制御の不動点

## 参考ソース

1. Makarova, A., Otchere, C., Xu, L. Z., Lee, J., Ow, T. T. (2026). "AI Feelings over AI Features: How Messaging About Risk, Benefit, and AI Shapes Cognitive and Affective Trust in a Healthcare FinTech Platform".
   File: `raw/papers/psychology/ai-feelings-over-ai-features-how-messaging-about-risk-benefit-and-ai-shapes-cogn.md`
2. Kanhai, A. (2026). "The Trust Paradox in AI–Blockchain Systems: Exploring Transparency, Immutability, and Human Trust".
   File: `raw/papers/psychology/the-trust-paradox-in-aiblockchain-systems-exploring-transparency-immutability-an.md`
3. Tran, C., Delina, R. (2026). "Perceived Quality of AI-Supported Recruitment: The Role of Explainability, Trust and Human Control".
   File: `raw/papers/psychology/perceived-quality-of-ai-supported-recruitment-the-role-of-explainability-trust-a.md`
4. Lin, J. C. M., Ben Soltane, F. E. (2026). "Human-AI Collaboration vs. Substitution in Tourism Social Media Content: A Conceptual Framework for Consumer Engagement".
   File: `raw/papers/psychology/human-ai-collaboration-vs-substitution-in-tourism-social-media-content-a-concept.md`
5. Farazi, M. Z. R. (2026). "When the Agent Decides: Trust Calibration Challenges in Multi-Agent AI Systems for Organizational Decision-Making".
   File: `raw/papers/psychology/when-the-agent-decides-trust-calibration-challenges-in-multi-agent-ai-systems-fo.md`
