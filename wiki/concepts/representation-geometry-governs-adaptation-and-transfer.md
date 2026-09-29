# 表現空間の幾何が適応・転移・制御可能性を規定する

## 概要

この概念は、情報処理系の**適応の速さ**、**学習の転移範囲**、**外部からの介入可能性**が、入力や内部状態が占める表現空間の幾何によって規定される、という不変原理である。ここでいう幾何とは、次の三つの側面を指す。

- 状態が既存の多様体の上にあるのか、その外にあるのか
- 課題間で共有される下位機構があるか
- 個々の処理単位が情報をどれだけ圧縮・表現できるか(表現力)

AI Nativeな設計にとって重要なのは、性能や適応性を「モデルの規模」や「データ量」だけで論じず、**表現がどのような空間構造を持つか**を設計変数として扱う視点が得られる点である。ソースはいずれも神経科学の研究だが、脳と人工システムに共通する構造原理の候補として位置づけられている。以下では、ソースの記述から読み取れる範囲で整理する。

## メカニズム

対象を人間・AI・組織・技術のどれに置き換えても成り立つ構造として、三つの要素にまとめる。

### 1. 多様体制約による状態遷移の分解
システムの状態は、既存のレパートリー(多様体)の上にあるか外にあるかで区別できる。状態変化は、少なくとも次の三種類に分けられる。

- 既存状態の**利得(ゲイン)変調**
- 多様体**内部での移動**
- 多様体の外への**オフマニフォルド変位**

これは「既存表現の再利用」と「新規表現の創出」の区別に対応する。距離や角度といった単純な指標では、この区別が見えない。

### 2. 共有下位機構を介した転移
ある課題で得た学習が別の課題に移るかどうかは、両者が下位の処理機構をどれだけ共有しているかに依存する。共有機構がなければ、表面的に似た課題でも転移は起きない。

### 3. 表現力(圧縮能力)への依存
構造化された入力配置の価値は、処理単位そのものの表現力に左右される。個々の単位が高い圧縮能力を持てば、入力側の構造化から得られる追加の利得は小さくなりうる。

これらを総合すると、適応の速度は入力の幾何に、転移は共有機構に、介入可能性は制御対象の表現空間の構造に、それぞれ左右されるという整理になる。

## 理論的背景

### 入力空間の幾何と適応ダイナミクス [1]
Bartolini らは、適応型指数積分発火ニューロンからなるリカレントネットワークに、トリプレット型スパイクタイミング依存可塑性則を組み合わせたモデルを構築した。目的は、神経外科患者の内側側頭葉における頭蓋内電気生理・単一ニューロン記録(プライミング課題)で得られた神経ダイナミクスの再現である。実験パラダイムに着想を得た入力の組織化のもとで入力の幾何を系統的に変え、反復抑制などの適応の強さと時間的ダイナミクスがどう変わるかを調べている。ソースの提示範囲では、入力空間の幾何が適応ダイナミクスを形作るという方向の知見が示されている。

### 知覚学習の選択的転移 [2]
Tang と Zhou は、傍中心窩での2次(コントラスト定義)運動の方向弁別訓練を、24名(訓練群16名、統制群8名)を対象に8セッション実施した。従来の研究では、2次運動の訓練が1次(輝度定義)運動へ非対称に転移することが示されていた。この研究は、初期のテクスチャ定義特徴は共有するが運動成分を欠く、静的な2次刺激へ転移するかを検証している。タイトルが示すとおり、結果は1次運動へは転移するが静的2次刺激へは転移しないという選択的転移であり、転移が学習者の保持する共有下位機構に依存することを示唆する。

### 利得変調とオフマニフォルド変位の分解 [3]
McKenzie は、記憶の分節化が神経活動の急速な脱相関から生じると考えられている点に着目した。従来のユークリッド距離やコサイン角では、遷移は検出できても、新しい状態が多様体のレパートリーとどう関係するかは分からない。そこで神経集団活動の動径軸を用いて局所多様体の法空間を分割し、近傍状態の利得変調、多様体内での移動、真のオフマニフォルド変位を分離する幾何学的分解を導入した。同時に、静的な参照多様体と単一のテスト状態だけでは、摂動の出発状態や利得の大きさ、機構的な分解は一般に復元できないという**識別可能性**の課題も指摘している。

### 表現空間における制御 [4]
Rothermel らは、制御理論に動機づけられた神経サロゲート枠組みを提案した。fMRI デコーディング、深層生成モデル、制約付き潜在空間ステアリングを組み合わせ、物理的な刺激なしに、刺激誘発 fMRI 活動のスナップショットから表象の候補変更とその予測される知覚的効果を検証する。情動価と記憶されやすさは作業例として用いられている。自然シーンデータセットの4名の参加者による3万6000超の画像-fMRI観測を用い、被験者固有のモデルが視覚応答性皮質から粗い生成構造を回復したとされる。介入の設計を、表現空間内での探索問題として扱う点が特徴である。

### 受容野の整列と表現力 [5]
Adorante らは、Expressive Leaky Memory ニューロンのリカレントネットワークで、ニューロンの複雑さと順伝播受容野の組織化を独立に操作した。聴覚とイベントベース視覚の分類課題で、課題に関連する感覚座標に整列した受容野は、比較対象に対してテスト精度を改善すると報告されている。一方、その価値は個々のニューロンの表現力に依存するという主張が題名に示されている。核心的知見としては、計算効率は受容野の構造化よりも、個別ニューロンの情報圧縮能力によってより強く決まるとされる。

## AI Nativeな設計への示唆

以下は、上記の知見から導かれる設計上の含意である(ソースが直接提示した指針ではなく、構造的な解釈を含む)。

1. **状態変化の種類を区別して観測する。** 利得の変化なのか、既存表現の再配置なのか、新規表現の獲得なのかを分けて監視する。単一の距離指標だけに頼らない。識別可能性には限界があるため、参照状態の取り方も設計に含める。
2. **転移は共有下位機構から設計する。** 汎用化を期待する課題群には共通の下位表現を持たせ、共有のない領域への転移は前提にしない。
3. **介入は表現空間内で計画し、事前に試す。** 潜在空間での制約付きステアリングと、実適用前のシミュレーション(サロゲート)による検証を組み合わせる。
4. **入力の構造化と処理単位の表現力を分けて評価する。** 構造化への投資が、表現力の高い部品のもとでも価値を持つかを確認する。
5. **入力の幾何を適応速度の設計変数とする。** 入力が既存多様体の上にあるか外にあるかで、適応の挙動が変わりうると想定して設計する。

## 関連コンセプト

- [[upstream-schema-ceiling-on-downstream-capability]] — 上流の表現構造が下流能力の上限を決めるという点で、表現の構造が能力を規定する本原理と対応する。
- [[objective-indexed-representation-separation]] — 共有表現の扱いと分離・合成という観点で、共有下位機構の議論と接続する。
- [[externalized-state-and-representation-fidelity]] — 状態を表現する際の忠実度という観点で関連する。
- [[hierarchical-integration-of-models-and-learned-control]] — モデルと学習制御を統合して制御可能性を確保する点で関連する。
- [[closed-loop-safety-and-governance-of-autonomous-agents]] — 介入・監視の可能性という観点で関連する。
- [[human-finite-capacity-and-stable-adaptation-patterns]] — 処理資源の有限性と適応という観点で、表現力への依存と関係する。

## 参考ソース

1. Diletta Bartolini, Thomas P. Reber, Tatjana Tchumatchenko, Matthias Voigt (2026). "Input-space geometry shapes adaptation dynamics underlying repetition suppression in a neural network model of relatedness priming"
   File: raw/papers/neuroscience/input-space-geometry-shapes-adaptation-dynamics-underlying-repetition-suppressio.md
2. Yong Tang, Yifeng Zhou (2026). "Selective transfer of perceptual learning in parafoveal second-order motion: generalization to first-order motion but not to static second-order stimuli"
   File: raw/papers/neuroscience/selective-transfer-of-perceptual-learning-in-parafoveal-second-order-motion-gene.md
3. Sam McKenzie (2026). "Identifying Neural State Changes due to Gain versus Off-Manifold Displacement"
   File: raw/papers/neuroscience/identifying-neural-state-changes-due-to-gain-versus-off-manifold-displacement.md
4. Marco Rothermel, Madleen Stenger, Soroush Daftarian, Svenja Jule Francke, Bita Shariatpanahi (2026). "AI-Driven Neural Surrogates for In Silico Design of Cognitive-Affective Neuromodulation Targets"
   File: raw/papers/neuroscience/ai-driven-neural-surrogates-for-in-silico-design-of-cognitive-affective-neuromod.md
5. Agnese Adorante, Aaron Spieler, Anna Levina (2026). "The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity"
   File: raw/papers/neuroscience/the-computational-value-of-sensory-aligned-receptive-fields-depends-on-neuronal-.md
