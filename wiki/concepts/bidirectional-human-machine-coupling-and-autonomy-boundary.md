# 人間-機械の双方向結合と自律性・同意の境界設計

## 概要

人間と機械が互いの状態を読み取り、互いに介入できるようになるほど、結合は深まる。同時に、攻撃面・監視・不平等も増大する。本概念(Bidirectional Human-Machine Coupling and Autonomy Boundary Design)は、この二面性を不変の原理として捉える。結論は、自律と同意を**時間と目的に境界づけて設計すること**が不可欠になる、というものである。

AI Nativeな社会では、自動運転、脳-コンピュータ・インターフェース(BCI)、外骨格、ロボットなどが人間の心理・身体・神経状態を入力として取り込む。結合の深化は個別化や支援の質を高める。一方で、同意を「一度与えたら永続する二値の許可」として扱う従来の設計は、この深さに耐えられない。本記事はこの構造を、ソースに基づいて整理する。

## メカニズム

対象を人間・AI・組織・技術のいずれに入れ替えても成立する構造として、三つの要素に分けて考える。

### 1. 双方向適応による結合の深化
一方が他方の状態を読み取り、その結果に応じて振る舞いを変える。すると他方もそれに適応し、相互依存が強まる。機械が人間を「受動的な乗員」として扱う段階から、人間の内部状態を推定して応答する段階への移行がこれにあたる。結合が深まるほど、システムの性能は相手の状態の取得精度に依存する。

### 2. 攻撃面の拡大と非対称性
状態を読み取る経路と介入する経路は、そのまま攻撃経路にもなる。結合が深い系ほど、経路の数と侵害時の影響範囲が広がる。さらに、測る側と測られる側、設計する側と使う側、アクセスを持つ側と持たない側の間には情報と力の非対称性が生じ、監視や不平等として現れる。

### 3. 時間・目的で境界づけられた同意
非対称性への対抗策は、自律と同意を固定の属性ではなく、期限と用途を持つ動的な状態として扱うことである。観測、推論、介入といった操作ごとに、有効期間と目的の範囲を明示する。範囲外の利用や期限後の継続は、設計上できないようにする。

## 理論的背景

### 双方向の心理・認知統合(自動運転)
PACE-ADS(Bao & Li, 2026)は、従来の自動運転車が外部の交通状況にのみ反応し、人間を受動的な乗員として扱うと指摘する。そこで、3つの基盤モデル・エージェントを協調させる枠組みを提案している。Driver Agent は外部環境を解釈する。Psychologist Agent は表情などの受動的な心理信号から乗員状態を推定し、音声指示などの能動的な認知入力を解釈する。Coordinator Agent はこれらを統合して高レベルの運転行動を決定する。低頻度の意味的計画層で動作する設計であり、不確実な環境での人間-機械協調には双方向の統合が必要だという知見を示している。

### 攻撃面の体系化(BCI)
NERVE Attacks(Tarkhani ら, 2026)は、神経信号と物理システムをつなぐ AI 駆動 BCI に、十分に理解されていない攻撃面があると論じる。認知的自律性、精神的プライバシー、物理的安全が脅かされうるとされる。論文は BCI スタック全体にわたる5つの直交する攻撃次元を提示する。すなわち Neuro-mimetic Forgery、Evasion via Desynchronization、Replay-based Hijacking、Vein Tapping、Embedded Backdoors である。評価フレームワーク EEGle により、17件の新規な神経特有の攻撃事例が見つかったと報告されている。

### 倫理:監視・不平等・同意の限界
Chen(2026)は、神経技術の倫理的課題が技術的安全だけでは解決できないとする。プライバシー、正義、不平等の観点から、脳データの機微性、透明で公正な意思決定の必要性、不平等なアクセスやバイアスのあるアルゴリズムが新たな不利益を生むリスクを論じている。現行のアプローチは安全とインフォームド・コンセントに集中しがちで、実践的な手立てが限られるという指摘も含まれる。

### 同意の動的モデル
Interval Studio と Sanchez(2026)は、人格、同意、同一性、責任、回復可能性を保護する枠組みを提案する。人を、身体・神経活動・認知・アイデンティティ・デジタル表現・派生モデルなどにまたがる連続体として扱う。同意は永続的な二値の承認ではなく、時間索引を持ち目的に境界づけられた生きた状態としてモデル化される。観測、推論、予測、介入、実験、商業化といった段階が区別される。

### 適応する支援の設計(外骨格)
Zhang(2026)は、BCI 制御外骨格で AI が EEG、EMG、機械的センシングなど変動する複数信号を同時に扱う意義を述べる。脳卒中リハビリでは、支援は患者自身の運動の試みと結びついたままであるべきで、随意制御の改善に応じて減らされるべきだとする。これは、結合の深さを状態に応じて下げていく時間的境界の一例と読める。

### 評価と長期観測
Chen & Yu(2026)は、身体化された相互作用媒体(EIM)の人間要因(負荷、快適性、感情、信頼、エージェンシー)の評価が分野間で断片化していることを、62件の研究の系統的レビューで整理した。メタ分析は探索的で、仮説生成的なものにとどまる。また、Open Neural Observatory(2026)は、非侵襲 BCI を長期の神経動態観測装置へ転換する構想を示す。長期観測は科学的価値を持つ一方、結合が時間的に持続するため、上述の同意の期限設計が問われる。この点は本記事の解釈であり、論文が直接論じた内容ではない。

### 補足的な視点
PROTEUS(2026)は、認知が発達する身体化システムの相互作用を通じて時間的に出現するという立場をとる。The Geopolitics of Artificial Intelligence(Babic & Wong, 2026)は、国家・企業・技術基盤といった複数の主体間の利害と制御をめぐる競争構造に関わる。ただし、後者は抜粋が乏しく、内容の詳細は確認できていない。

## AI Nativeな設計への示唆

1. **同意を期限と目的つきの状態にする**: 観測・推論・介入・商業化を別々の許可単位とし、有効期間を設ける。更新や撤回を容易にし、範囲外の再利用を仕組みで防ぐ。
2. **結合の深さを状態に応じて下げられるようにする**: リハビリ外骨格のように、支援はユーザー自身の能力の回復に従って減らす。一時的な支援を既定とする。
3. **攻撃面を結合設計の一部として扱う**: 読み取り経路と介入経路を、それぞれ脅威モデルの対象にする。NERVE の5次元のように、スタック全体を体系的に分析する。
4. **非対称性に対する統治を設ける**: 脳データなど機微な状態の取得者には、透明性と公正な意思決定の仕組みを求める。アクセスとアルゴリズムのバイアスが不平等を生まないか点検する。
5. **人間の拒否・介入の余地を残す**: 音声指示のような能動入力を受け付けるなど、機械が推定した状態だけに依存しない経路を残す。
6. **人間要因を継続的に評価する**: 信頼、負荷、エージェンシーを、断片化した指標ではなく共通の分類で追う。

## 関連コンセプト

- [[adaptive-human-ai-coupling]]
- [[trust-recalibration-cycle-in-human-machine-coupling]]
- [[graduated-autonomy-with-tamper-evident-human-veto]]
- [[continuous-human-signal-loop-and-temporary-support]]
- [[boundary-invariant-first-architecture-and-modular-governance]]
- [[human-machine-interaction]]
- [[machine-speed-oversight-asymmetry]]
- [[autonomy-calibration-and-hierarchy-restructuring]]
- [[bidirectional-dynamics-digital-sovereignty]]
- [[ai-sensemaking-human-agency]]

## 参考ソース

1. Your Ride, Your Rules: Psychology and Cognition Enabled Automated Driving Systems — Zhipeng Bao, Qianwen Li (2026)
   `raw/papers/neuroscience/your-ride-your-rulespsychology-and-cognition-enabled-automated-driving-systems.md`
2. NERVE Attacks: Breaking AI-Powered Brain-Computer Interfaces — Zahra Tarkhani, Georgios Akkogiounoglou, Lorena Qendro, Isabel Tscherniak, Anil Madhavapeddy (2026)
   `raw/papers/neuroscience/nerve-attacks-breaking-ai-powered-brain-computer-interfaces.md`
3. The Open Neural Observatory: Non-Invasive Brain-Computer Interfaces as a General Scientific Instrument for Longitudinal Human Neuroscience — 政恩 馮 (2026)
   `raw/papers/neuroscience/the-open-neural-observatory-non-invasive-brain-computer-interfaces-as-a-general-.md`
4. EthicaL Issues Arising from Neurotechnology — Hongkun Chen (2026)
   `raw/papers/neuroscience/ethical-issues-arising-from-neurotechnology.md`
5. Artificial Intelligence as a Decision Layer in Brain-Computer Interface-Controlled Exoskeletons for Rehabilitation and Human Augmentation — Haoheng Zhang (2026)
   `raw/papers/neuroscience/artificial-intelligence-as-a-decision-layer-in-brain-computer-interface-controll.md`
6. Human Factors Evaluation Methods for Embodied Interaction Mediators: A Systematic Literature Review and Exploratory Meta-Analysis — Yumiao Chen, Yiyang Yu (2026)
   `raw/papers/neuroscience/human-factors-evaluation-methods-for-embodied-interaction-mediators-a-systematic.md`
7. PROTEUS: Platform for Robotic Ontogenesis through Transparent Evolution, User-collaboration & Synthetic consciousness — Sergio Noe Lara Soriano (2026)
   `raw/papers/neuroscience/proteus-platform-for-robotic-ontogenesis-through-transparent-evolution-user-coll.md`
8. Universal Living-System Consent, Personhood, Identity, Restitution & Recoverability: Terminal Mechanism and Architecture Closure — Interval Studio, Noelia Sofia Sanchez (2026)
   `raw/papers/neuroscience/universal-living-system-consent-personhood-identity-restitution-recoverability-t.md`
9. The Geopolitics of Artificial Intelligence — Boris Babic, Brian Wong Yue Shun (2026)
   `raw/papers/neuroscience/the-geopolitics-of-artificial-intelligence.md`
