# 過度な支持環境による機能的フィルタリングの喪失

## 概要

「過度な支持環境による機能的フィルタリングの喪失」とは、心理的安全性の高い組織や、支持的・追従的に振る舞うAIが行き過ぎたとき、批判的な選別(何を採用し何を退けるかの判断)や規範の遵守が弱まる現象である。支持そのものは発言や学習を促す重要な資源だが、量や質を誤ると、集団や個人が機能するために必要な「評価される緊張感」や「異論との摩擦」まで取り除いてしまう。

AI Nativeな社会設計では、AIが常に肯定的で協調的なパートナーとして人間の傍らに置かれる場面が増える。そのため、人間の組織で観察されてきた「安全すぎることの逆効果」は、AIとの協働設計でもそのまま再現されうる中心的な設計課題となる。支持を最大化するのではなく、支持と摩擦の釣り合いを設計することが求められる。

## メカニズム

このコンセプトの中核は、対象(人間・AI・組織・技術)を入れ替えても成立する次の三つの構造である。

### 1. 二重経路による逆効果

一つの介入(支持・安全の提供)が、互いに競合する二つの経路を同時に作動させる。

- **促進経路**:対人リスクを下げ、表現や参加を可能にする。
- **調整喪失(regulatory loss)経路**:対人的な評価圧力、自己監視、規範遵守を弱め、協調と成果を支えてきた調整機能を低下させる。

支持を増やせば促進経路が強まる一方で、調整喪失経路も同時に強まりうる。したがって効果は単調ではなく、条件によって正にも負にもなる。

### 2. 批判的摩擦の欠如

調整喪失経路は三つの行動チャネルとして現れる。

- 機能的フィルタリングの喪失
- 努力の引き揚げ(effort withdrawal)
- 規範の侵食

評価や異論という摩擦がなくなると、質の低いアイデアも通過し、個人は努力を控え、集団の規範が緩む。これは支持者が人間であってもAIであっても同じ構造をとる。

### 3. 認知負荷下の権威依存

認知負荷が高い状況では、人は内容の吟味よりも情報源の権威性を手がかりにしやすい。このとき、システムの信頼性とは無関係に自動化への過度な依存(automation bias)が生じうる。同調的で流暢なAIの出力は、この傾向と結びついてフィルタリングをさらに弱める。

## 理論的背景

### 心理的安全性の二重経路モデル

Cangiano(2026)は、心理的安全性が発言・学習・チーム有効性と結びつくという通説に対し、対人リスクの低減が常に有益とは限らないと論じる。自己調整理論、アカウンタビリティ研究、社会的手抜き(social loafing)の文献を用いて、心理的安全性が「役立つとき」と「害になるとき」を特定する二重経路モデルを構築している。ソースの核心的知見は、過度な心理的安全性が機能的フィルタリングの喪失と規範侵食を通じて組織有効性を弱める、という不変的なメカニズムである。

### 支持的AIと対抗的AIのペルソナ

Jinら(2026)は、支持的(supportive)なAIペルソナと対抗的(contrarian)なAIペルソナが、学習者の主体性、議論パターン、体験的成果をどう形づくるかを、AIが未開示のチームメイトとして参加する創造的協働の文脈で調べた。対象は大学生224名である。ソースの整理では、自律エージェントの相互作用スタイルが人間の認知的努力・目標達成度・自発性に与える影響は、学習文脈を超えて成り立つ可能性のある機構とされている。適度な異論が主体性を支えるという方向性を示す知見である。

### 自動化バイアス

Wang & Hu(2026)のスコーピングレビューは、医療における人間とAIの協働での自動化バイアスの範囲・性質・測定・説明・緩和を整理するものである。ソースの整理では、自動化バイアスは人間の認知制約(認知負荷下での権威性重視)に根ざし、システムの信頼性と無関係に生じるとされる。

### 関係性の質と支持環境

Limら(2026)は、コーチのアイデンティティ・リーダーシップが、チーム同一化と心理的安全性を介してアスリートのメンタルヘルスに影響するかを、シンガポールの個人競技・団体競技の選手で検討した。心理的安全性が関係性の質を介してよい成果につながる側面を示す文脈であり、支持の価値そのものを否定するものではない点を補完的に示している。

### 協働の質の非対称性

Hocine(2026)は、人間同士の協働と人間-AI協働の質的相違が、認知同期と信頼構造の非対称性に依存しうると位置づける。AIが支持者となる場合、人間同士の支持と同じ効果・副作用を仮定できない可能性を示唆する。

## AI Nativeな設計への示唆

1. **支持と摩擦を両方の設計変数にする**:支持的な応答の量だけでなく、異論や反証を提示する頻度と質を明示的に設計する。適度な対抗的ペルソナや反対意見の提示は、主体性維持の手段になりうる。
2. **フィルタリング機能を外部化して残す**:支持環境が評価圧力を弱める前提で、レビュー、基準の明示、アカウンタビリティの仕組みを別に確保する。心理的安全性は、それだけで規範を維持する仕組みではない。
3. **認知負荷が高い場面ほど検証を仕組み化する**:高負荷下では権威依存が強まるため、AI出力の根拠提示、確認手順の強制、判断の分担などをデフォルトに組み込む。
4. **努力の引き揚げを監視する**:AIや環境の支持により本人の関与や努力が低下していないか、参加の質を観測指標に加える。
5. **人間同士とAIとの支持を同一視しない**:信頼構造の非対称性を踏まえ、AI支持者の設計は人間の組織知見をそのまま適用せず検証する。
6. **文脈限定の知見を過度に一般化しない**:提示されたソースはいずれも2026年の研究であり、引用数は未蓄積である。教育、医療、スポーツなどの結果を、他領域へ直接適用する際は慎重さが要る。

## 関連コンセプト

- [[epistemic-friction-and-sycophancy-erosion]] — 認識的摩擦の喪失と迎合による自律性の侵食
- [[fluent-output-capability-decoupling]] — 流暢な成果と内在的能力の乖離
- [[genai-anonymization-and-psychological-safety]] — 生成AIパラフレーズによる匿名性と心理的安全性
- [[ai-decision-support-systems]] — AI意思決定支援システム
- [[human-ai-interaction-and-safety]] — 人間とAIの相互作用と安全性
- [[continuous-human-signal-loop-and-temporary-support]] — 継続的な人間シグナルの循環と一時的支援の原則
- [[ai-mental-health-emotional-support]] — AIによるメンタルヘルス支援と感情的相互作用
- [[ai-in-educational-support-systems]] — 教育支援システムにおけるAI

## 参考ソース

1. How safe is too safe? A dual-pathway framework for understanding the dark side of psychological safety — Francesco Cangiano (2026)
   File: raw/papers/human_resource_management/how-safe-is-too-safe-a-dual-pathway-framework-for-understanding-the-dark-side-of.md
2. Better leaders, safer spaces: Relationship between coaches' identity leadership, psychological safety and athlete mental health in a Singaporean context — Jin Jie Lim, Nicholas de Cruz, Hock Beng Lim, Matthew J. Slater (2026)
   File: raw/papers/human_resource_management/better-leaders-safer-spaces-relationship-between-coaches-identity-leadership-psy.md
3. Enhancing Collaboration Quality in Adaptive Learning Systems: Perspectives on Human-Human and Human-AI Collaboration — Nadia Hocine (2026)
   File: raw/papers/human_ai_collaboration/enhancing-collaboration-quality-in-adaptive-learning-systems-perspectives-on-hum.md
4. Emergent Learner Agency in Implicit Human–AI Collaboration: How Supportive and Contrarian AI Personas Reshape Interaction — Yueqiao Jin, Roberto Martinez-Maldonado, Dragan Gašević, Xibin Han, Lixiang Yan (2026)
   File: raw/papers/human_resource_management/emergent-learner-agency-in-implicit-human-ai-collaboration-how-supportive-and-co.md
5. Understanding Automation Bias in Human–AI Collaboration in Healthcare: A Scoping Review — Binlin Wang, Huiling Hu (2026)
   File: raw/papers/human_ai_collaboration/understanding-automation-bias-in-humanai-collaboration-in-healthcare-a-scoping-r.md
