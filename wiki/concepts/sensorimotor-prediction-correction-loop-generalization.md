# 予測―修正ループによる身体・環境統合と行動創発

## 概要

予測―修正ループとは、エージェントが感覚入力を予測し、予測と実際の入力の食い違い(予測誤差)によってモデルを更新し、その結果を身体を通じて環境に作用させて次の感覚入力を得る、という閉ループの構造である。本概念の主張は、行動は「予測生成」「誤差による修正」「身体・環境との結合」の三要素が閉ループで統合されたときに創発し、その成立は実装媒体(生体・ロボット・デジタルツイン)に依存しない、というものである。

AI Nativeな設計において重要なのは、知能を「入力から出力への写像」ではなく、環境との継続的な結合の中で維持される動的過程として捉え直す視点を与える点にある。事前プログラミングされたモデルや正確なセンサー情報に頼る設計は、実環境の不確実性に弱い。予測誤差を駆動力とするループを設計の中核に置けば、適応は事後的な追加機能ではなく構造そのものに組み込まれる。

## メカニズム

このループは、対象を人間、AIエージェント、ロボット、組織、技術システムのいずれに入れ替えても成立する構造として、次の要素に整理できる。

1. **予測生成**:主体が内部モデルに基づき、次に得られる入力(感覚データ、観測、結果)を予測する。
2. **誤差の算出**:予測と実際の入力との差を検出する。
3. **修正(学習)**:誤差に基づいて内部モデルや予測を更新する。階層的な構造では、各層が下位層の入力を予測し、誤差が上位へ伝わる。
4. **行動による環境への作用**:身体(または実行系)を通じて環境に働きかけ、その結果が新たな入力となる。
5. **結合の維持**:身体・環境・内部モデルが切り離されず連続的に結合しているため、行動は個別の指令ではなくループ全体の帰結として現れる。

重要なのは、どの要素も単独では行動を生まない点である。神経回路、身体力学、感覚フィードバック、環境相互作用のいずれかを欠くと、行動を生成する過程そのものが再現されない。この構造は、組織における「計画→実行→結果の観測→計画修正」の循環や、AIシステムの継続的な評価・改善サイクルにも同型の構造として見いだせる。

## 理論的背景

### 予測符号化に基づく認知アーキテクチャ

Zhangによる研究[1]は、予測符号化の原理に基づく身体性AIの認知アーキテクチャを提案している。現在の身体性AIは、人間に見られる知覚と行動のシームレスな統合の再現に苦慮しているとし、その解決として、人間の感覚運動系を模した連続的な「予測―修正ループ」を実装する。エージェントは感覚入力の予測を生成し、予測と実データの乖離に基づいて予測を更新する。この過程は一連の方程式で定式化され、身体化された経験の動的モデリングの枠組みとされる。記号的AIとコネクショニスト的手法の橋渡しを目指し、階層的予測符号化を用いる点も特徴である。本ソースは、予測誤差に基づく階層的な知覚運動統合を媒体中立的な認知の普遍メカニズムとして位置づけている。

### 神経・身体・感覚の統合ループ(デジタルツイン)

Mus siliconus[2]は、マウスのニューロ・筋骨格系デジタルツインを提案する。従来の動物デジタルツインは神経回路、解剖、バイオメカニクスを個別にモデル化しがちであったが、本研究は行動を生む過程を統合し、神経活動・身体力学・感覚フィードバック・環境相互作用を統一する「身体化された動力学系」として捉えるべきだと論じる。X線CT、白色光切片、Scx-GFPイメージングによる解剖再構成に、バイオメカニクスシミュレーション、Bonhoeffer–van der Pol型の神経動態、触覚フィードバックを組み合わせ、閉じた感覚運動ループを形成する。行動の創発が種を超えた統合ループに根ざすことを示す知見である。

### 身体・環境モデルによる制御

Zhangの別の研究[3]は、身体性認知に基づくロボット制御を論じる。事前プログラムされたモデルと精密なセンサーデータに依存する従来手法は現実世界の不確実性に苦戦するとして、身体モデル・環境モデル・認知モデルを統合し、シミュレートされた身体的相互作用を通じて学習・適応するシステムを提案する。ソース上は提案段階のフレームワークである。

### 予測マッピングと空間表現

Bennettらの研究[5]は、後継表現(successor representation)が海馬の場所細胞や嗅内皮質のグリッド細胞を説明してきたことを踏まえ、げっ歯類の行動バイアスを組み込んだ後継表現が、海馬下支(subiculum)ニューロンの多様な空間応答を再現することを示した。境界細胞や角細胞の出現も説明され、下支の発火パターンは純粋な空間モデルや境界ベクトル細胞モデルより後継表現でより正確に記述されるという。予測に基づく表現が意思決定の基盤となりうることを示唆する。

### 内在的要求と決定論的エージェント

Solmsら[4]は、環境資源との関係で内在的欲求に関する「感じられた不確実性」を持つ単純な人工エージェントが、完全に決定論的でありながら、見かけ上主観的な情報処理を通じて快楽的場所選好行動を示しうることを論じる。この事例は、行動の創発が特定の生体基盤を必要としないことを示唆するが、意識や自由意志への含意はあくまで議論の段階である。

## AI Nativeな設計への示唆

- **ループを設計単位にする**:モデル、身体(実行系)、環境、フィードバックを個別最適化せず、閉ループ全体を設計対象とする。[2]が示すように、要素を分離したモデル化では行動を生む過程が捉えられない。
- **誤差を第一級の信号として扱う**:予測と結果の乖離を記録・伝播・学習に用いる仕組みを標準装備する。階層構造にして、局所的な誤差は下位で吸収し、大きな乖離のみを上位に伝える設計が考えられる[1]。
- **事前規定より相互作用による学習**:不確実な環境では、固定モデルよりシミュレートされた相互作用を通じた適応を重視する[3]。
- **媒体中立な検証**:同じ原理が生体・ロボット・デジタルツインで成立するなら、デジタルツイン上で安全に検証してから実機へ展開する道筋が取れる[2]。
- **内在的要求を組み込む**:エージェントの目的を環境資源との関係における内在的欲求として設計する方法がありうる[4]。ただし目的乖離や主体性の侵食への配慮が必要である。

## 関連コンセプト

- [[embodied-cognition]] — 身体性認知:認知が身体と環境の相互作用によって形づくられるという基盤的立場。
- [[embodied-cognition-and-perception]] — 身体的認知と知覚の自己組織化
- [[embodied-interaction-design]] — 身体化相互作用設計
- [[error-correcting-feedback-and-staged-refinement]] — 誤差修正フィードバックと段階的精緻化:修正過程の設計面。
- [[behavioral-prediction-integration]] — 行動予測統合
- [[adaptive-intelligence-emergence]] — 適応知能創発
- [[reward-driven-skill-acquisition-and-embodied-constraints]] — 報酬による学習再構成と身体的制約下のスキル獲得
- [[interaction-loop-grounded-knowledge-and-relational-bond]] — 相互作用ループに埋め込まれた知識生成と持続的関係
- [[adaptive-assistance-objective-drift-and-agency-erosion]] — 適応的支援システムにおける目的乖離と主体性の侵食

## 参考ソース

1. Cognitive Architectures for Embodied AI – Predictive Coding of Sensorimotor Experience(Jincheng Zhang、2026)— `raw/papers/neuroscience/cognitive-architectures-for-embodied-ai-predictive-coding-of-sensorimotor-experi.md`
2. Mus siliconus: A Neuro-Musculoskeletal Digital Twin of the Mouse Integrating Neural Dynamics, Biomechanics, and Tactile Sensing(Satoshi Oota, Hideo Yokota, Hiroki Mori、2026)— `raw/papers/neuroscience/mus-siliconus-a-neuro-musculoskeletal-digital-twin-of-the-mouse-integrating-neur.md`
3. Embodied Cognition-Driven Robot Control(Jincheng Zhang、2026)— `raw/papers/neuroscience/embodied-cognition-driven-robot-control.md`
4. Inferring Affective Consciousness in an Artificial Agent: A Case Study(Mark Solms, St John Grimbly, Bruce Bassett, Evert Boonstra, Rowan Hodson、2026)— `raw/papers/neuroscience/inferring-affective-consciousness-in-an-artificial-agent-a-case-study.md`
5. Subicular spatial codes arise from predictive mapping(Lauren Bennett, William de Cothi, Laurenz Muessig, Fabio R. Rodrigues, Francesca Cacucci、2026)— `raw/papers/neuroscience/subicular-spatial-codes-arise-from-predictive-mapping.md`
