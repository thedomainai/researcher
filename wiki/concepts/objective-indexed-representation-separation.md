# 多目的下での共有表現の不安定化と成果軸での分離・合成

## 概要

複数の目的(成果)が単一の共有表現を同時に更新しようとすると、その表現は不安定になる。この不安定性は個々の実装の不備ではなく、共有資源をめぐる競合から構造的に生じる。対処の方向は、共有表現をそのまま酷使することではなく、目的(成果)軸で分離した低次元の単位を用意し、文脈に応じて選択・合成する構造にある。

ソース[1]は、次元的注意(dimensional attention)を全域共有のベクトルとして実装すると、複数成果の学習でそのベクトルが不安定化し、上下限へ張り付くことを示した。ソース[2]は、運動制御において共有リカレントネットワークに対する低ランク摂動としてプリミティブを持たせ、離散コードで選択・系列化する構成を示している。

AI Nativeな設計にとって、この原理は次の点で重要である。AIエージェントやシステムは、複数の目標・利用者・タスクを一つの内部表現やポリシーで処理しがちである。競合による不安定化を避け、目的ごとの単位を合成可能にしておくことが、汎化と制御可能性の前提になる。

## メカニズム

この構造は、対象を人間・AI・組織・技術のいずれに入れ替えても成り立つ。

1. **共有資源の競合**:一つの共有パラメータ(注意の重み、意思決定の基準、リソース配分など)を、異なる目的が逆向きに更新しようとする。目的ごとに最適値が異なれば、勾配(圧力)は打ち消し合うか、極端な値へ押しやられる。
2. **目的軸での分離**:表現に成果の添字を付ける。全域で一つだった値を「成果ごとの値」に変換することで、競合の発生源を取り除く。
3. **低次元プリミティブ化**:分離した単位は小さく低次元に保つ。小さな摂動や調整として持てば、共通の基盤(コア)を共有しつつ、目的固有の差分だけを独立に学習・保持できる。
4. **離散的選択による文脈切替**:どの単位を使うかは離散的なコードで選び、その上位に単位を系列化する方策を置く。これにより既存の単位の組み合わせから新しい振る舞いを合成できる。

組織に置き換えれば、一つの評価指標や一つの共通方針が複数の事業目的を同時に律するとき歪みが生じ、目的ごとの小さな役割単位を状況に応じて選び組み合わせる設計が有効になる、という対応関係にある。ただしこの組織への対応づけは、本記事による構造的な読み替えであり、ソースが直接実証したものではない。

## 理論的背景

### 共有注意ベクトルの不安定性(ソース[1])

ソース[1](Lenard Dome, 2026)は次の内容を報告している。

- 次元的注意は、各刺激次元に一つのスカラーを対応させた全域共有の注意ベクトルとして実装されることが多い。これらのスカラーは誤差に対する勾配降下で学習され、予測に有効な特徴ほど顕著性(salience)を得る。
- 複数の成果を予測する多成果学習では、この共有ベクトルが不安定になり、上下限へ崩壊する。その結果、学習と汎化に有意味な注意の調整を学べなくなる。
- 解決策として、全域共有の注意調整を成果ごとの表現に変換する「成果添字付き注意行列」を導入した。
- 不安定な共有ベクトルについての分析を示し、それが成立する条件を導出している。
- 三つの合成実験で、提案する注意行列が有意味な表現へ収束する一方、共有ベクトルは収束しないことを示した。

### 低次元プリミティブの合成(ソース[2])

ソース[2](Sreejan Kumar, Marcelo Mattar, Lea Duncker, 2026)は、運動プリミティブが共有リカレントネットワークへの低ランク摂動として実装されうるという神経科学の理論を、学習可能な構成に翻訳している。

- 共有リカレントコアを、離散潜在コードで選ばれる残差アダプタのバンクで変調するアーキテクチャを提案した。
- 閉ループのバイオメカニクス制御で訓練すると、ランクを制約していないにもかかわらず、アダプタが低ランクの摂動を創発的に形成した。タスク表現は共有コアの互いに異なる部分空間に置かれる。
- ネットワーク全体を凍結したまま、学習済みオプション上の単純な高レベル方策が低ランクアダプタを系列化し、分布外の新規動作を生成する。

### 補助的な知見

ソース[3]は、脳の七つの皮質ネットワークに一つずつ脳事前学習エキスパートを割り当てるBrain-MoEが、全15のモデル・ベンチマーク対で保持データ精度を平均6.42ポイント向上させたと報告している。専門化した単位を選択的に用いる構造が有効であることと整合するが、ソース自体はメカニズム説明が未成熟な仮説段階である。ソース[4]は、脳オルガノイドによる制御層がタスク横断的な適応性を示すとするが、抜粋の範囲では詳細な機序までは確認できない。ソース[5]はAI結合HPCワークフローの実行モチーフを整理した調査であり、本概念との関係は間接的である。

## AI Nativeな設計への示唆

- **共有スカラーや共有ベクトルを疑う**:複数目的を扱う場面では、全域で一つの重み・注意・スコアを共有していないか点検する。不安定化や境界値への張り付きは診断の手がかりになる。
- **成果軸で添字を付ける**:注意・評価・ポリシー調整などを成果ごとの表現に分け、共通基盤の上に目的別の差分として載せる。
- **小さなアダプタを束ねる**:共有コアを維持しつつ、低次元のアダプタをバンクとして用意する。コアを凍結したまま上位方策だけを学習でき、既存能力を壊さずに新しい組み合わせを得やすい。
- **文脈切替は離散的に**:どの単位を有効にするかを明示的な離散コードで表すと、選択が観測・検査しやすくなる。
- **合成の検証**:合成によって新規行動を作る際は、分布外での挙動を独立に確認する構造を併置する。

## 関連コンセプト

- [[system-instability-in-ai]] — 共有表現の不安定化は、AIにおけるシステム構造の不安定性の具体例として位置づけられる。
- [[self-reinforcing-instability-dynamics]] — 共有パラメータが境界へ崩壊する挙動は、自己強化的な不安定ダイナミクスと関連する。
- [[single-objective-optimization-misalignment-and-autonomy-risk]] — 単一の最適化が多目標系を損なう問題と同型の構造を持つ。
- [[decision-node-decomposition-and-bounded-relocation]] — 意思決定を分解して再配置する発想と対応する。
- [[decomposition-information-retention-limit]] — 分解には情報保持の限界があり、分離の粒度を考える際の制約となる。
- [[structural-separation-and-hierarchical-verification]] — 機能分離による誤差伝播の抑制という点で共通する。
- [[representation-and-evaluation-validity-distortion]] — 表現の歪みが評価の妥当性に及ぶ問題と関連する。
- [[technology-activity-outcome-framework]] — 成果を軸に技術と活動を整理する視点と接続する。

## 参考ソース

1. Why shared attention vectors fail: a case for outcome-indexed tuning — Lenard Dome (2026)
   File: raw/papers/neuroscience/why-shared-attention-vectors-fail-a-case-for-outcome-indexed-tuning.md
2. Learning Options for Compositional Motor Control with Adapter Banks — Sreejan Kumar, Marcelo Mattar, Lea Duncker (2026)
   File: raw/papers/neuroscience/learning-options-for-compositional-motor-control-with-adapter-banks.md
3. The Platonic brain bridge hypothesis: human brain networks as an architectural prior for omni models — Pengfei Zhang, Biao Tian, Xiangang Li, Li Liu (2026)
   File: raw/papers/neuroscience/the-platonic-brain-bridge-hypothesis-human-brain-networks-as-an-architectural-pr.md
4. Brain organoid computing for robotic decision-making — Hongwei Cai, Chunhui Tian, Yang Yang, Yantao Xing, Zichen Hong (2026)
   File: raw/papers/neuroscience/brain-organoid-computing-for-robotic-decision-making.md
5. AI-coupled HPC Workflow Applications, Middleware and Performance — Wes Brewer, Ana Gainaru, Frédéric Suter, Feiyi Wang, Murali Emani (2026)
   File: raw/papers/neuroscience/ai-coupled-hpc-workflow-applications-middleware-and-performance.md
