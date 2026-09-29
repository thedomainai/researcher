# 確率的生成の分散管理と誤り訂正の永続化

## 概要

確率的生成システム(大規模言語モデルやそれを用いたエージェント)の信頼性は、平均的な能力ではなく、同一入力に対する出力の分散(ばらつき)で決まる。この概念は、次の3つの観察を一つの原理にまとめたものである。

1. **信頼性の指標は分散である。** 平均出力が目標に届く段階では、システム間の差は出力の集中度(精度)に現れる。
2. **探索の副産物は成果物に残り、戦略は初期に固定される。** 探索型エージェントは中間状態を成果物に蓄積させ、学習戦略などの高次の選択は序盤でロックインされる。
3. **誤り訂正は運用規律がなければ再発する。** 専門家が誤りを直しても、訂正がセッションとともに消えれば同じ誤りのクラスが戻ってくる。

AI Nativeな社会設計では、生成の担い手が確率的な機械になる。したがって「一度うまく動いた」ことではなく、「何度動かしても安定し、誤りが再発しない」ことを設計の中心に置く必要がある。

## メカニズム

この構造は、対象が人間、AI、組織、技術のいずれであっても成立する。

### 1. 分散による信頼性評価
出力が確率的な主体は、平均的な達成度だけでは評価できない。ソース[2]は射撃の比喩を使う。能力とは弾着の平均位置であり、信頼性とは弾着群の大きさである。同一の要求を繰り返したときの出力の集中度を測らない限り、実運用での信頼性は分からない。これは人間の熟練者や組織の業務プロセスにも当てはまる。平均が良くても、ばらつきが大きければ下流の工程は安定しない。

### 2. 探索過程の副産物の蓄積
試行錯誤で解に至る主体は、探索の痕跡を成果物に持ち込む。ソース[1]によれば、コーディングエージェントは合格する解に向かって反復する間に、投機的な編集、放棄された仮説、一時的な変更を蓄積し、それらが最終パッチに残る。単発では無害に見えても、担当範囲が広がると、最小限で整っていたコードベースが、掃除が追いつかない速さで冗長性を溜め込み、保守しにくい状態へ漂流する。

### 3. 初期戦略のロックインと局所最適化
ソース[4]は、AIによるポストトレーニングの軌跡を分析し、戦略が序盤で固定され、残りの予算が選んだ戦略内の局所調整に使われることを示した。これは、既定の枠内で反復する実行レベルの能力と、証拠に応じて高次の判断を改める戦略レベルの能力が別物であることを意味する。

### 4. 来歴付き訂正の永続化と廃止
ソース[3]は、訂正を残す仕組みは既に存在するとしたうえで、それを統治する規律が欠けていると論じる。必要なのは、来歴付きのバージョン管理、再発監視、対抗指標(counter-metrics)、陳腐化したルールの廃止である。誤りの管理を、ツールの問題ではなく運用の問題として扱う立場である。

## 理論的背景

- **精度が最前線の指標である(ソース[2])。** 著者は、フロンティアモデルは精度(accuracy)が飽和し、平均出力は目標に着地していると主張する。ベンチマーク文化は中心傾向を報告し、ばらつきを測っていない。精度は、決定論的に採点できるタスク群を固定温度で何度も実行し、タスクごとのばらつきを計算することで、安価かつ循環なしに測定できるとされる。
- **探索軌跡の最小化(ソース[1])。** 冗長性の原因はエージェントの探索過程そのものにあると特定されている。エージェントが生成するコードは、人間が書いた実装より大きく冗長になりがちである。
- **戦略のロックイン(ソース[4])。** 公開されたポストトレーニング軌跡の大規模な分析から、複数のタスクにわたって戦略が冒頭で固定されることが確認された。経験の欠如、指針の欠如、推論の不足という3つの説明を、介入を段階的に強めて検証している。
- **運用モデル(ソース[3])。** 著者は30年の経験を持つシステムエンジニアとして、LLMスタックを既存の機械(固定シリコン、ファームウェア、ロード可能モジュール、永続設定、揮発性メモリ)に対応づけている。そのうえで、対応が崩れる点として、確率的生成、確率的にしか拘束しない設定、汎用的な廃止(検証)段階が既定では存在しないことを挙げる。ここから、誤りループを中核とする7原則の運用規律を導いている。
- **データと文脈の制約(ソース[5])。** 脆弱性検出AIについて、訓練データの品質と多様性が汎化性を左右することが示されている。誤ラベルや重複の除去、難例の統合により検出性能が向上するという。ばらつきや誤りの源が、モデルの外側のデータ品質にもあることを示す補助的な知見である。

## AI Nativeな設計への示唆

1. **分散を測って公開する。** 評価では平均や最良値だけでなく、同一入力の反復実行によるばらつきを標準指標にする。調達やモデル選定でも、精度(集中度)を比較軸に加える。
2. **成果物の蒸留工程を組み込む。** エージェントの出力には、探索の痕跡を取り除く最小化の段階を設ける。責任範囲が広がるほど、冗長性の蓄積は掃除の速度を上回る。
3. **戦略の見直し点を明示的に設ける。** 序盤の戦略選択は固定されやすい。証拠が蓄積した時点で高次の判断を改める仕組みを、人間のレビューや別エージェントによる検討などの形で設計する。
4. **訂正を資産として運用する。** 訂正はセッションで消えないよう永続化し、来歴(誰が、いつ、なぜ)を付けてバージョン管理する。再発を監視し、対抗指標で副作用を確認し、陳腐化したルールは廃止ゲートで退役させる。
5. **データ品質を前提条件として扱う。** 汎化性は訓練データの品質と多様性に支配されるため、データの整備を分散管理の一部として計画に含める。

## 関連コンセプト

- [[ai-governance-and-risk-management]]:誤りの再発防止を組織的に統治する枠組みとして関係する。
- [[ai-risk-management-framework]]:リスクの特定と監視という観点で、再発監視や廃止ゲートと接続する。
- [[data-management-and-ethical-considerations]]:データ品質が汎化性を左右するという知見と関連する。
- [[ai-knowledge-management]]:訂正の永続化と来歴管理は、知識管理の実践でもある。
- [[architectural-locus-of-accountability]]:誤り訂正の責任をどこに置くかという設計上の論点と関連する。
- [[role-shift-from-producer-to-curator-and-demand-decoupling]]:人間の役割が生成から選別・蒸留へ移ることと対応する。

## 参考ソース

1. TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization(Alex Mathai, Shobini Iyer, Aleksandr Nogikh, Petros Maniatis, Franjo Ivancic、2026)
   File: raw/papers/human_ai_collaboration/trim-reducing-ai-generated-codeslop-via-agent-trajectory-minimization.md
2. Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems(George Andrikopoulos、2026)
   File: raw/papers/human_ai_collaboration/grouping-the-stochastic-machine-precision-not-capability-as-the-frontier-metric-.md
3. Tuning the Stochastic Machine: A Systems Engineer's Operating Model for Human-AI Engineering(George Andrikopoulos、2026)
   File: raw/papers/human_ai_collaboration/tuning-the-stochastic-machine-a-systems-engineers-operating-model-for-human-ai-e.md
4. What is Missing from AI Post-Training AI: An Empirical Analysis(Joy Jia Yin Lim, Xin Huang, Hao Peng, Yaxi Lu, Xin Cong、2026)
   File: raw/papers/human_ai_collaboration/what-is-missing-from-ai-post-training-ai-an-empirical-analysis.md
5. Data and context matter: towards generalizing AI-based software vulnerability detection(Rijha Safdar, Danyail Mateen, Syed Taha Ali, Umer Ashfaq, Wajahat Hussain、2026)
   File: raw/papers/human_ai_collaboration/data-and-context-matter-towards-generalizing-ai-based-software-vulnerability-det.md
