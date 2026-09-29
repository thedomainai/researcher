# 報酬による学習再構成と身体的制約下のスキル獲得

## 概要

学習とは、報酬信号(および予測との差である誤差)が、刺激と行動の結合へと再構成されていく過程である。とりわけ高リスクな身体的・実践的技能では、この過程に二つの制約が加わる。第一に、実際の身体や現場での直接経験は他のもので完全には代替できない。第二に、物理的・生体的な制約(筋の力学、被験者や対象者への安全性など)が、練習や訓練の設計条件を決める。

AI Nativeな社会設計では、AIがコーチングや模擬訓練を担う場面が増える。そのとき、「何を報酬として与えるか」「どこまでを模擬で済ませ、どこから直接経験に委ねるか」が設計上の中心課題になる。本記事は、この構造を3つのソースに基づいて整理する。

## メカニズム

この原理は、学習主体が人間でもAIでも組織でも成立する構造として、次の三層で整理できる。

1. **予測誤差と報酬による結合の形成**
   主体は、環境からの刺激に対して行動を選び、報酬(成功・失敗の信号)を受け取る。期待と結果のずれが、刺激-行動の対応を更新する。学習初期は報酬や誤りの信号そのものが表現の中心にあり、進行に伴って、刺激から行動への直接的な結合が強まる。

2. **報酬信号の再構成**
   学習が進むと、報酬に関する情報の表現は「評価そのもの」から「刺激に対する適切な行動選択」へと置き換わる。ソース[2]は、この再構成を、強化学習における計算論的に避けがたい機構として位置づけている。

3. **身体的制約と安全な模擬のトレードオフ**
   運動技能には、筋の力学のような、実践者が回避できない生物力学的制約がある。高リスク技能では、実地での練習に安全・同意・プライバシー・実習先の確保・指導者の余力といった制約がかかる。模擬は安全だが直接経験の代わりにはならず、直接経験は不可欠だが常に安全に行えるとは限らない。このため設計では、両者の役割分担を明示する必要がある。

対象を入れ替えても、「誤差信号→結合の再編→制約下での練習環境の設計」という骨格は変わらない。

## 理論的背景

### 小脳における報酬に基づく視覚運動連合学習(ソース[2])

サルが、任意の視覚刺激(フラクタル図形)を左右いずれかの手の動きに結びつける課題を学習する際の、小脳Crus I/IIのプルキンエ細胞を扱った研究である。抜粋から読み取れる要点は次のとおり。

- Crus I/IIを一時的に不活性化すると、新しい連合の学習が損なわれ、運動応答が遅れる。ただし運動のキネマティクス自体は影響を受けない。
- Crus領域のプルキンエ細胞の単純スパイクは、学習中の認知的誤りを表す。
- 学習が進むと、個々のニューロンの活動は刺激-応答の連合により選択的になり、その選択性は視覚刺激の出現により近い時点で現れるようになる。

これらは、報酬・誤りに関わる信号が、学習の進行とともに刺激-行動結合の表現へ再構成されるという見方を支える。なお、抜粋は途中で切れているため、初期状態の詳細などはここでは述べない。

### 生物力学に根ざしたスキル理解(ソース[1])

MyoMechanixは、負荷を伴う動作を対象に、動作と筋活動を対応づけるマルチモーダルな基盤である。抜粋によれば次の特徴を持つ。

- 38名の被験者による20種類の動作、7,500以上の専門家注釈付きサンプル。
- 同期した多視点RGB映像、3D姿勢、表面筋電(sEMG)、その他の生理信号を含み、著者らは最大規模のマルチモーダルなAQA(動作品質評価)ベンチマークとしている。
- 動作、局面、要点、誤り、是正フィードバックの関係を構造化したFitness Knowledge Graph(FKG)により、構成的な採点を可能にする。

従来のAQAが視覚入力に偏り、動作を一枚岩のパターンとして扱っていたために、きめ細かな生物力学に基づくフィードバックが妨げられていた、というのが著者らの問題設定である。運動学習の生物力学的制約は不変だが、それを捉えられるかは計測技術に依存する、という点が本コンセプトにとって重要である。

### 高リスク実践技能における直接経験と模擬(ソース[3])

保育者養成における、実習前のメンタルヘルス支援能力の育成を扱った、人間の監督下でのマルチモーダル生成AI活用の枠組みである。抜粋によれば、乳幼児の情動信号、愛着ニーズ、分離反応、相互作用パターンへの繊細な観察・応答は、講義や手順訓練だけでは育たない。本物の実習は不可欠だが、安全確保、同意、プライバシー、実習先の確保、指導体制、自然に生じる状況の予測不能性が、安全な予行演習を制限する。ここに、直接経験の不可替性と安全な模擬とのトレードオフが現れる。

## AI Nativeな設計への示唆

- **報酬設計を学習の中身として扱う**:フィードバックは単なる採点ではなく、刺激-行動結合を形づくる信号である。誤りの信号を、学習の進行に応じて具体的な状況判断へ結びつく形で提示する設計が望ましい。
- **不変の身体制約を計測で可視化する**:筋活動などの生理信号を取り込み、視覚だけでは見えない誤りに根拠あるフィードバックを返す。ただし、得られる知見は計測技術の範囲に縛られることを前提に置く。
- **動作を構成要素に分解して指導する**:局面・要点・誤り・是正策を構造化した知識を使い、一枚岩の点数ではなく構成的な評価を行う。
- **模擬は直接経験の前段として位置づける**:生成AIによる模擬は、実習前の安全な予行演習に用い、直接経験の代替とはしない。
- **人間の監督を組み込む**:高リスクで倫理的に繊細な領域では、AIの模擬を人間の指導者の監督下に置く。

## 関連コンセプト

- [[embodied-cognition]] — 身体を通じた認知という前提を共有する
- [[embodied-cognition-and-perception]] — 身体的な知覚と学習の関係
- [[embodied-interaction-design]] — 身体制約を踏まえた相互作用の設計
- [[conversational-agent-embodied-interaction]] — 会話エージェントによる身体的インタラクション
- [[role-asymmetry-projection-in-simulated-interaction]] — 模擬相互作用の妥当性の検討
- [[active-inference-driven-world-modeling]] — 予測誤差に基づく学習という観点での接点
- [[epistemic-labor-displacement-under-delegation]] — 委譲による判断力の空洞化との対比
- [[ai-driven-surgical-transformation]] — 高リスクな身体技能の例としての外科領域

## 参考ソース

1. MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching(Hao Yin, Paritosh Parmar, Lijun Gu, Lin Xu, Tianxiao Guo, 2026)
   File: raw/papers/cognitive_science/myomechanix-biomechanically-grounded-compositional-skilled-activity-understandin.md
2. Purkinje cells in Crus I and II encode the visual stimulus and the impending choice as monkeys learn a reinforcement based visuomotor association task(Anna E. Ipata, V. Fascianelli, Chris I. De Zeeuw, Naveen Sendhilnathan, Stefano Fusi, 2026)
   File: raw/papers/cognitive_science/purkinje-cells-in-crus-i-and-ii-encode-the-visual-stimulus-and-the-impending-cho.md
3. Multimodal generative AI for pre-practicum mental health support competency development: a human-supervised framework for education–childcare partnerships(Wenlan Xie, Chunye Xiang, Fan Wu, Xingda Chen, 2026)
   File: raw/papers/cognitive_science/multimodal-generative-ai-for-pre-practicum-mental-health-support-competency-deve.md
