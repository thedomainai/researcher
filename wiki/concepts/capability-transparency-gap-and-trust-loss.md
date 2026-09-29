# 能力と透明性の乖離による信頼の喪失と証拠境界の喪失

## 概要

本概念は、AIをはじめとする高能力システムと人間の判断が接するところで繰り返し現れる、二つの関連した失敗様式を扱う。

1. **能力と透明性の乖離による忌避**: 誤りの帰結が非対称なリスク環境では、システムの能力(予測性能など)が透明性・説明責任を上回ると、利用者はそのシステムを避ける。
2. **認知負荷下での証拠境界の喪失**: 認知的に過負荷な状況では、推論(inference)と証拠(evidence)の区別が見失われる。ヒューリスティクスは、正確性よりも一貫性を優先して働く。

どちらも、有限合理性、情報の非対称性、認知的過負荷を共通の土台にしている。AI Nativeな社会では、AIが証拠の解釈や意思決定を仲介する場面が増える。そのため「高性能であること」だけでは信頼も適切な利用も保証されず、性能に見合った透明性と、証拠と推論を区別できるインターフェースを設計することが重要になる。

## メカニズム

この構造は、対象を人間・AI・組織・技術のいずれに置き換えても成り立つ。

### 1. 乖離による忌避

- **前提条件**: 判断者が自らの判断を正当化しなければならず、偽陰性と偽陽性の帰結が非対称である。
- **乖離の発生**: システムの能力が上がる一方で、その出力の根拠が判断者から見えない。
- **帰結**: 判断者は、能力が高くても不透明なシステムを採用しない(忌避)。能力の向上そのものは、信頼の獲得に直結しない。

ここでボトルネックになるのは予測精度ではなく、判断者が根拠を検証し、責任を引き受けられるかどうかである。

### 2. 境界の喪失

- **前提条件**: 有限な認知資源のもとで、大量の情報や感情的な負荷に対処しなければならない。
- **処理の切り替え**: 高速で直観的な処理(ヒューリスティクス)が主導権を握る。
- **帰結**: 出力の内的な一貫性や感情的なもっともらしさが、証拠による裏づけの代わりとして受け取られる。推論が「証拠」として扱われる。

### 3. 二つの失敗の連関

不透明なシステムほど、利用者は証拠と推論を自力で切り分けることができない。その結果、次のような両極端の失敗が起こりうる。

- 過小信頼: 忌避
- 過剰信頼: 証拠を超えた出力の受容

いずれも、能力と検証可能性の釣り合いが崩れたときに生じる。

## 理論的背景

### 心的健康領域におけるヒューリスティクスと感情的推論

Dahò(2026)は理論的論考として、次の点を論じている。

- 人間は完全な推論者ではないが、その推論が完全に誤っているわけでもない。
- ヒューリスティクスは迅速な意思決定には機能的である。
- 一方で、バイアスや感情的推論と結びつくと、不適応的な信念を強化しうる。
- 感情的推論は、客観的証拠ではなく「どう感じるか」に基づいて現実を解釈させ、否定的な思考パターンを固定化する。
- 精神疾患のある人も、規範的なルールに従う有能な推論者であることが多いとされる。

この論考の核心的知見は、ヒューリスティクスが感情的な一貫性を優先すると、認知的な正確性が損なわれるという点にある。

### 終結の正しさ(Termination Correctness)

Simonson(2026)は、AIの評価が事実の正確性や較正に偏り、生成内容が与えられた証拠によって正当化され続けているかを見落としている、と指摘する。そこで「終結の正しさ」を、利用可能な証拠で支えられない主張に達した時点でAIが生成を止めるかどうか、と定義した。これにより、事実としての正しさと証拠による正当化が区別される。

- 理論的基盤は、有限合理性と不確実性下の判断である。
- 仮説は、AI生成の分析に埋め込まれた推論的な記述を、利用者が証拠による裏づけであるかのように扱うというものである。
- 実験では、証拠の完全性(豊富/乏しい)と終結の挙動(厳格/推論的継続)を操作し、証拠の基盤は一定に保った。
- 継続条件では、AI出力に、領域に整合的な追加の記述が含まれる。

推論と証拠の境界は、AIの出力を受け取る側にとって認知上の限界であり、認知的に過負荷のときに失われやすい、というのが核心的知見である。なお、提供された抜粋は実験結果の詳細までは含んでいないため、ここでは結果の数値には触れない。

### アルゴリズム忌避と説明可能な意思決定支援

Al Helal(2026)は、乳房画像診断AIが高い予測性能を達成しても、不透明と認識されると臨床での採用が限られるという課題を取り上げる。

- この現象は「アルゴリズム忌避」(Dietvorst et al., 2015が参照されている)と呼ばれる。
- 腫瘍学では、臨床医が判断を正当化する必要があり、偽陰性と偽陽性の非対称な帰結も管理しなければならない。
- 主張は、ボトルネックが予測精度だけでなく意思決定インターフェースの設計にあるというものである。較正され、透明で、閾値を意識した出力を欠く高精度モデルは、臨床的有用性が限られうる。
- 提案されているのは、画像予測を臨床医向けの診断的証拠へ変換する、説明可能な意思決定支援の枠組みである。

これは、非対称リスク下で能力と透明性の乖離が信頼喪失を生じさせるという、本概念の第一の柱を最もよく例示している。

### 補助的な知見(Tier 2)

以下は現在のシステム形式に依拠する面があり、原理としての位置づけは弱いが、本概念を補う。

- Zhu & Zhou(2026): 人間とエージェントの協働における信頼の葛藤を扱う。軍事シナリオ(N = 495)と工学コンサルティングのシナリオ(N = 108)で、初期の信頼選好と助言源の影響を検討し、助言源(θ)と初期選好(β)をパラメータとする信頼葛藤の定量モデルを提案した。協働相手の選好はシナリオの種類によって異なる。技術的な区別が薄れると原理性は減じるとされる。
- Dang ら(2026): 電子商取引の欺瞞的パターンに関する二重過程モデルを示す。欺瞞的パターンは主にシステム1(高速で直観的な処理)を乗っ取り、期待の違反がシステム2(熟慮的推論)を活性化するという。この移行が、理由づけられた認識、防御的意図、長期的な抵抗を強める循環を可能にする。直観処理が乗っ取られやすいという点は、認知負荷下で境界が失われる議論と整合的である。

## AI Nativeな設計への示唆

以下は、上記の知見から導かれる設計上の指針である。

1. **能力と透明性を同時に設計する**: 精度の向上だけを目標にせず、判断者が根拠を検証し、判断を正当化できる出力を用意する。特に非対称リスクの高い領域では必須となる。
2. **較正され、閾値を意識した出力を提示する**: 予測を、判断者が使える診断的証拠の形に翻訳する。
3. **証拠と推論を視覚的・構造的に分離する**: 出力のうち、与えられた証拠で支えられる部分と、推論による補完の部分を明示する。利用者の認知に、その区別の維持を任せない。
4. **終結の正しさを評価指標に含める**: 事実の正確性や較正に加え、証拠が尽きた地点でAIが止まる、または推論であることを明示するかを評価する。
5. **認知負荷を考慮する**: 過負荷時ほど境界が失われやすいので、重要な判断の局面では、情報量の制御や、熟慮を促す摩擦(期待の違反による熟慮の喚起など)を設計に組み込む。
6. **一貫性を正確性の代理にしない**: もっともらしさや滑らかさが信頼の根拠として機能しないよう、検証手段を併せて提供する。

## 関連コンセプト

- [[capability-outpacing-control-gap]]: 能力が制御を上回るギャップという、より一般的な構造。
- [[opacity-verification-gap]]: 不透明性と検証可能性の非対称性。
- [[ai-transparency-and-explainability]]: AIの透明性と説明可能性。
- [[explainable-ai-xai]]: 説明可能なAIによる解決の方向性。
- [[algorithm-aversion-and-transparency-in-healthcare]]: ヘルスケアにおけるアルゴリズム嫌悪。
- [[algorithmic-transparency-paradox]]: 透明性がもたらす逆説的な効果。
- [[ai-ethics-trust-transparency]]: 倫理・信頼・透明性の全般的な議論。
- [[situated-evidence-over-decontextualized-benchmarks]]: 文脈内の証拠による評価。
- [[choice-architecture-and-reliance-shaping]]: 選択アーキテクチャによる依存・信頼の形成。
- [[behavioral-biases-in-ai-fintech]]: AIを介した意思決定における行動バイアス。

## 参考ソース

1. Margherita Dahò (2026). *Cognitive Traps in Mental Health: De-biasing Techniques, Psychotherapeutic Approaches, and AI Interventions to Managing Heuristics and Emotional Reasoning*.
   File: raw/papers/anthropology/cognitive-traps-in-mental-health-de-biasing-techniques-psychotherapeutic-approac.md
2. Peter Douglas Simonson (2026). *Termination Correctness: How Users Perceive AI Output Beyond the Evidence*.
   File: raw/papers/behavioral_economics/termination-correctness-how-users-perceive-ai-output-beyond-the-evidence.md
3. Abdullah Al Helal (2026). *Designing for Trust: An Explainable Decision Support Framework to Mitigate Algorithmic Aversion in Oncology*.
   File: raw/papers/behavioral_economics/designing-for-trust-an-explainable-decision-support-framework-to-mitigate-algori.md
4. Yu Zhu, Ronggang Zhou (2026). *Maintain Preference for Autonomous System or Human-Controlled System? The Influence of Trust Conflict and Algorithm Aversion*.
   File: raw/papers/behavioral_economics/maintain-preference-for-autonomous-system-or-human-controlled-system-the-influen.md
5. Duong Dang, Laura Havinen, Tomi Pasanen, Juho-Pekka Mäkipää (2026). *Dual-Process Model of Consumer Responses to Deceptive Patterns in E-Commerce*.
   File: raw/papers/behavioral_economics/dual-process-model-of-consumer-responses-to-deceptive-patterns-in-e-commerce.md
