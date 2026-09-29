# 委譲による所有感・責任・能力の侵食と回復的足場設計

## 概要

認知や作業をAIなどの他者に委譲すると、その成果物に対する**心理的所有権**、結果に対する**責任感**、そして自分自身の**能力形成**が同時に弱まる。これは生成AI固有の現象というより、「行為の一部を他の主体に任せる」という構造そのものから生じる、人間-エージェント関係における不変的なメカニズムとして捉えられる。

一方で、この侵食は不可逆ではない。支援を学習者の能力に応じて段階的に引き下げる**足場設計(scaffolding and stepping back)**や、自分自身の作業過程を可視化して再帰属を促す**自己監視の可視化**が、回復の鍵として示されている。

AI Nativeな社会では、多くの作業がエージェントに委ねられる。効率だけを最適化すると、「システムが行為し、人間が責任を問われる」という責任ギャップが拡大し、人間側の能力も空洞化しかねない。したがって、委譲を前提としつつ所有感・責任・能力を維持する設計が基盤的な課題になる。

## メカニズム

以下の構造は、委譲する主体(人間・組織)と委譲される主体(AI・外部組織・技術)を入れ替えても成立する。

1. **所有権の形成条件の変化**: 所有感は、対象への統制、自己投資、対象に関する知識、自己との一致といった先行条件から形成される。委譲はこれらの条件を直接的に弱め、所有感を低下させる。
2. **所有権を介した責任の希薄化**: 責任の感覚は、所有感が媒介して生じる。所有感が失われると、結果への責任感も連動して低下する。
3. **支援と自立のトレードオフ**: 支援は短期的な成果を高める一方、過剰であれば過度の依存と能力の萎縮を招く。支援者の目的が「当面の成果」か「相手の独立した能力」かで、最適な介入は異なる。
4. **再帰属のための可視化**: 自分の過程が見えないと、成果や判断が「自分のもの」として帰属されにくい。過程を可視化・対話可能にすることで、自己の行為として再解釈できる。
5. **相互作用による構成**: 設計された相互作用は単なる媒介にとどまらず、人間の主体性・自己理解・身体化された能力を形づくる。したがって、その可逆性が重要になる。

## 理論的背景

### 心理的所有権理論による実証(Delegated Minds)

Rose, Coors, Weinmannは、心理的所有権理論に基づき、生成AI利用が所有権と責任の先行条件をどう変えるかを検証した。文章作成課題を手作業またはGPTベースのアシスタントで行う統制実験(N = 138)の結果、次のことが示された。

- 生成AIの利用は、知覚された統制、自己投資、対象に関する知識、自己一致性を有意に低下させ、それらを通じて心理的所有権を低下させた。
- 心理的所有権は、生成AI支援が知覚された責任に及ぼす負の効果を**完全に媒介**した。

これは、人間-AI協働における「責任ギャップ」を説明するメカニズムとして所有権を位置づける知見である。

### 支援と独立性の張力(AI Coaching)

Wangらは、AIコパイロットは共有制御により人間の成績を大きく高めうるが、過剰な支援は過度の依存とスキルの萎縮を誘発すると指摘する。有効なコーチングには、学習者の能力に整合した戦略的な足場かけと「身を引くこと」が必要であり、学習を促す生産的な失敗を許容すべきだと論じる。彼らはこの過程を、学習者がタスク成績を最適化し、コーチが学習者の独立した能力を目標とする非協力的動的ゲームとして定式化し、適応的共有制御と、コーチがスキル発達に与える因果的影響の確率モデルを組み合わせた強化学習の枠組みを開発した。

### 自己過程の可視化(IRIS)

Zhouらは、Flower and Hayesの文章作成の認知過程モデルに基づき、キーストロークログから執筆過程の状態を推定し、AIで強化したバージョン履歴として提示するIRISを提案した。主な機能は、改訂箇所のその場での強調表示、過程の種類や話題による概念的フィルタ、執筆や過程について内省的な問いを投げかける自然言語での問い合わせである。形成的研究と縦断研究では、書き手がこれらを使って特定の改訂を探し、文章の進展を理解することが示された。実行的認知と自己監視を見える化することが改善につながるという考え方である。

### 相互作用が人間を構成するという視点

Leeは、設計された相互作用が人間の主体性、自己理解、身体化された能力、意味形成、責任を部分的に形づくると論じる。エージェント的転回のもとでは、ヒューマン・イン・ザ・ループの構成で責任が人間に割り当てられがちであり、この問題が切迫するとされる。この視点では、相互作用の**可逆性**が根本的な論点となる。

### 補助的知見

- 子どもとAIの相互作用のレビュー(Voysey ら)は、エージェンシーが、計画性と自己調整、AIシステムへの制御の主張、現状への批判と再設計として観察されると整理する。エージェンシーを「生得のもの」でなく「発達させるもの」とみなす立場もあり、設計による支援が可能であることを示唆する。
- 職場の生成AI利用者を対象とした調査(N = 515、Shiら)は、心理的エンパワーメントがより深い利用へ結びつく経路が、利用動機によって調整されることを示す。

## AI Nativeな設計への示唆

- **所有権の先行条件を保つ**: 統制(修正・却下・方向づけの権限)、自己投資(人が労力や判断を注ぐ工程)、対象知識(内容の理解を促す提示)、自己一致(本人の意図や文体の反映)を、委譲の設計要素として意識的に残す。
- **責任を所有感と切り離さない**: 人間に責任を課す設計をとるなら、その前提となる所有感が形成される工程を確保する。所有感を欠いたまま責任だけを割り当てると、責任ギャップが生じる。
- **能力適応型の足場設計**: 学習者や利用者の現在の能力を推定し、支援を段階的に減らす。生産的な失敗の余地を残し、短期の成績と独立した能力形成を別の目標として扱う。
- **過程の可視化と内省の支援**: 成果物だけでなく、作業過程の履歴を提示し、問いかけによって自分の判断を振り返れるようにする。
- **可逆性の確保**: 委譲が習慣化しても、人が自分で行う状態に戻れる経路を設計に含める。
- **動機の質への配慮**: 利用の深まりは動機によって変わりうるため、利用の量だけでなく質を評価対象に含める。

## 関連コンセプト

- [[ai-cognitive-offloading-paradox]] — AIタスク代替における認知負荷と心理的所有権のパラドックス
- [[cognitive-ownership-vs-algorithmic-offloading]] — 認知的所有権とアルゴリズム的外部化
- [[epistemic-labor-displacement-under-delegation]] — 委譲による認識的労働の代替と判断力の空洞化
- [[fluency-induced-expertise-illusion-and-responsibility-erosion]] — 支援の流暢さによる専門性の錯覚と責任の希薄化
- [[compensatory-adaptation-hidden-erosion]] — 補償的適応の枯渇と安定性の錯覚
- [[capability-externalization-dual-effects]] — 能力外部化の二面性と非定常環境での再適応
- [[capability-perception-and-responsibility-diffusion-in-trust]] — 能力知覚・代理性知覚と信頼・責任転嫁
- [[effort-opacity-and-disclosure-signal-erosion]] — 努力の不可視化と評価シグナルの劣化
- [[recursive-constitution-of-human-and-interaction-design]] — 設計された相互作用による人間の構成と三層共進化ループ
- [[epistemic-friction-and-sycophancy-erosion]] — 認識的摩擦の喪失と迎合による自律性の侵食
- [[capability-profile-based-task-allocation]] — 能力プロファイルに基づく役割分担と協働設計

## 参考ソース

- Delegated Minds: How Generative AI Assistance Alters Psychological Ownership and Responsibility — Stefan Rose, Christopher Coors, Markus Weinmann (2026)
  File: raw/papers/hci/delegated-minds-how-generative-ai-assistance-alters-psychological-ownership-and-.md
- AI Coaching for Accelerating Human Skill Development with Reinforcement Learning — Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam (2026)
  File: raw/papers/hci/ai-coaching-for-accelerating-human-skill-development-with-reinforcement-learning.md
- IRIS: Navigating and Reflecting on Writing Traces Using Intelligent Document Histories — David Zhou, Andrew Chen, John Joon Young Chung, Sarah Sterman (2026)
  File: raw/papers/hci/iris-navigating-and-reflecting-on-writing-traces-using-intelligent-document-hist.md
- Agency in Child–AI Interaction: A Review of How It Is Conceptualised, Studied, and Supported in HCI — Isobel Voysey, Vidminas Vizgirda, Sarah Turner, Leslye Denisse Dias Duran, Zaki Pauzi (2026)
  File: raw/papers/hci/agency-in-childai-interaction-a-review-of-how-it-is-conceptualised-studied-and-s.md
- Gratified use of AI moderating the pathway from sense of empowerment towards infusion use — Yingnan Shi, Yifan Zhong, Chenxiao Wang (2026)
  File: raw/papers/hci/gratified-use-of-ai-moderating-the-pathway-from-sense-of-empowerment-towards-inf.md
- Toward a Philosophy of Interaction: How Designed Interaction Constitutes the Human, and Why Its Reversibility Now Matters — Meng-Han Lee (2026)
  File: raw/papers/hci/toward-a-philosophy-of-interaction-how-designed-interaction-constitutes-the-huma.md
