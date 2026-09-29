# 補完的情報構造と認識論的非対称性

## 概要

補完的情報構造と認識論的非対称性とは、協働の成否が各主体の能力の総和ではなく、**各主体がアクセスできる情報や信念の非対称性と、それらがどう補い合うか**によって決まるという原理である。あわせて、能力や情報で優位な側に過度に依存すると、劣位側の判断力そのものが損なわれるという帰結も含む。

AI Nativeな設計にとって重要なのは、次の点である。

- 「人間の判断とAIの能力を組み合わせれば良くなる」という素朴な想定は、両者が同じ情報にアクセスしているという暗黙の前提に立っている。
- 実際にはAIは機械可読な表現(テキスト、画像、音声、計測値、記録)しか処理できず、人間は身体感覚、生きた経緯、暗黙のパターン認識、文脈的意味、意図などを別に持ちうる(ソース[2])。
- 協働の失敗は、こうした非対称を見えないまま放置し、優位に見える側へ判断を委ねることで生じる。

## メカニズム

この構造は、主体を人間・AI・組織・技術のいずれに置き換えても成立する。要素は次の4つに整理できる。

1. **情報アクセスの非対称**:主体Aが持つ情報と主体Bが持つ情報は一致しない。片方にしかない情報(表現されていない情報)の境界を特定し管理しなければ、補完は成立しない。
2. **有限合理性と信念の補完**:各主体は限られた認知資源で信念(確信度)を形成する。補完が成立するのは、両者の信号を合わせて形成した信念が、どちらか一方の信号だけで形成した信念より正確になる場合である(ソース[1])。
3. **過信・過度依存(自動化バイアス)**:優位な側の出力を既定で受け入れる傾向が生じ、誤りがあっても従い続ける。より能力の高いシステムへの過度依存は、人間の認知的限界に由来する構造的な傾向とされる(ソース[3])。
4. **暗黙知の反復的抽出**:事前に明文化できない基準は、反復的な相互作用を通じて初めて表面化する。抽出された基準が蓄積されることで、非対称が縮小していく(ソース[5])。

これらは相互に作用する。非対称があるから補完の余地があり、その補完は依存によって損なわれ、反復的抽出によって回復される。

## 理論的背景

### 認識論的補完性のベイズ的定義(ソース[1])
Segarraは、医療分野のhuman-AIチームが理論上は単独より高い成果を出しうるのに、実証的にはその潜在力がほとんど実現されていないという「補完性ギャップ」を出発点とする。決定精度で成功を定義する従来のパフォーマンス基準では、協働が成功・失敗する認識論的過程を捉えられないと論じる。代わりに、**信念度(credence)のレベルで補完性を再定義**する。人間とAI双方の信号に基づく信念度が、どちらか一方の信号のみに基づく信念度より、適切なスコアリングルールで測って正確なとき、そのシステムは認識論的に補完的であるとされる。なお、パフォーマンス基準での補完については [[complementary-performance]] も参照。

### 補完的情報アーキテクチャ(ソース[2])
Ropertiは、機械可読な記録に入った表現情報と、入っていない人間側の関連情報との境界を特定・管理する枠組みとして、Complementary Information Architectureを提案する。概念論文であり、匿名化された3つの動機的観察(創作上のキャラクター構築、創傷ケア評価、談話レベルの言語分析)を用いて、異なる種類の表現ギャップを例示している。

### 過度依存と認知的介入(ソース[3])
Hendersonは、human-AIチームがAI単独に劣ることがある現象を、通常は自動化バイアスに帰される点から論じる。テキストベースの説明(XAI)は、直感的で偏りやすい高速処理に頼る利用者に読み飛ばされうる。そこで、自動的な反応を中断させる設計介入である認知的強制機能(CFF)が対案として検討される。過度依存は不変的な原理であり、認知的干渉設計により部分的に緩和可能、というのが本記事が依拠する知見である。

### 機械優位下の認識論的判断(ソース[4])
Ryderは教育を題材に、既存の学習者タスクを代行する代替型AIと、従来は研究チームや専門機関を要した問題への挑戦を可能にする能力拡張型AIを区別する。永続的な個人エージェントは、一般的な研究、専門システム、制限された制度的・産業的知識、認可された物理的実行にまたがる連合環境への認証済みインターフェースとしてモデル化される。ルーティングや調整は委任できるが、**機械優位の下での認識論的判断**(何が真実か、誰が責任を負うか)は依然として証拠づけられねばならない、と論じる。

### 暗黙的基準の反復的抽出(ソース[5])
Wangらは、AIエージェントが母集団規模のデータで学習されるため、個々の専門家が自らの評判を賭けられる水準の成果物にはなりにくいと指摘する。個人の専門性は平均からの上振れや逸脱にあり、基準は事前に完全には指定できない。そこで、セッションをまたぐ相互作用データを用いる TAHI(test-time adaptation through human-agent interaction)を提案し、進化するルーブリックモジュールにより各ユーザーの訓練・評価基準を結晶化させる。

### 補足的な知見
ソース[7]は、学生の生成AI継続利用において、タスク適合が実体験による期待の確認(Confirmation)を経て価値を持つことを示している。これは、情報の補完が実際の経験によって検証されて初めて効くことを示唆する。ソース[6]と[8]は本テーマの中核ではなく、本記事では詳細に立ち入らない。

## AI Nativeな設計への示唆

1. **表現されていない情報の境界を設計対象にする**:AIが見ている情報と人間だけが持つ情報を明示的に棚卸しし、後者を取り込む入口(補足入力、確認質問など)を用意する。
2. **精度だけでなく信念の質を評価する**:最終決定の正解率だけでなく、人間とAIの信号統合により信念の較正が改善したかを評価指標に含める。
3. **既定の追従を断つ設計を入れる**:説明の提示だけに頼らず、認知的強制機能のように判断を一度立ち止まらせる介入を併用する。依存の形成については [[choice-architecture-and-reliance-shaping]]、認知資源の限界については [[cognitive-limits-information-overload]] を参照。
4. **暗黙知を反復で蓄積する**:セッションをまたいで個人の基準を抽出し、評価ルーブリックとして保持・更新する。人間側が評価できる状態を保つ設計は [[shared-editable-state-and-evaluability-design]] とも関わる。
5. **判断と責任の所在を証拠づける**:AIが優位な領域ほど、人間が何を根拠に受け入れ、誰が責任を負うかを追跡可能にする。[[transparent-decision-architecture]] や [[capability-transparency-gap-and-trust-loss]] が関連する。
6. **集約による情報損失に注意する**:非対称を平均化や要約で覆い隠すと不一致が見えなくなる。[[aggregation-induced-information-loss]] を参照。

## 関連コンセプト

- [[complementary-performance]]
- [[choice-architecture-and-reliance-shaping]]
- [[cognitive-limits-information-overload]]
- [[shared-editable-state-and-evaluability-design]]
- [[transparent-decision-architecture]]
- [[capability-transparency-gap-and-trust-loss]]
- [[aggregation-induced-information-loss]]
- [[incentive-driven-deferral-and-asymmetry]]

## 参考ソース

1. Segarra, A. (2026). *Epistemically-Aware AI: Toward a Bayesian Framework for Human-AI Complementarity*. `raw/papers/human_ai_collaboration/epistemically-aware-ai-toward-a-bayesian-framework-for-human-ai-complementarity.md`
2. Roperti, G. (2026). *Beyond the Prompt: Human-AI Collaboration as an Architecture of Complementary Information*. `raw/papers/human_ai_collaboration/beyond-the-prompt-human-ai-collaboration-as-an-architecture-of-complementary-inf.md`
3. Henderson, O. (2026). *Balancing Trust and Deliberation in Human–AI Decision Support: The Effects of Explainable AI and Cognitive Forcing Functions*. `raw/papers/human_ai_collaboration/balancing-trust-and-deliberation-in-humanai-decision-support-the-effects-of-expl.md`
4. Ryder, J. F. (2026). *Beyond the AI Classroom: Epistemic Judgement Under Machine Advantage in Federated AI-Native Education*. `raw/papers/human_ai_collaboration/beyond-the-ai-classroom-epistemic-judgement-under-machine-advantage-in-federated.md`
5. Wang, Z. Z., Gandhi, A., Shao, R., Chen, A., Mueller, J. (2026). *Efficient Test-Time Adaptation through Human-AI Interaction*. `raw/papers/human_ai_collaboration/efficient-test-time-adaptation-through-human-ai-interaction.md`
6. Anthis, J. R., Díaz, M., Shelby, R. (2026). *CompanionSim: Synthetic Data for Evaluating Anthropomorphism in Human-AI Relationships*. `raw/papers/human_ai_collaboration/companionsim-synthetic-data-for-evaluating-anthropomorphism-in-human-ai-relation.md`
7. Li, X.-R., Hong, P.-T. (2026). *Pragmatic GAI continuance through human-AI collaboration amid trendiness and creepiness*. `raw/papers/human_ai_collaboration/pragmatic-gai-continuance-through-human-ai-collaboration-amid-trendiness-and-cre.md`
8. Kim, H. (2026). *Who becomes replaceable? Generative AI and the discursive stratification of work*. `raw/papers/human_ai_collaboration/who-becomes-replaceable-generative-ai-and-the-discursive-stratification-of-work.md`
