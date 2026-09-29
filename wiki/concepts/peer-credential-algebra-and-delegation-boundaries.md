# 対等行為者間の権限代数と委譲境界

## 概要

対等行為者間の権限代数(Peer Credential Algebra)とは、人間とAIを「上位が下位へ権限を委ねる」関係ではなく、構造的に対等な行為者(peer)として扱い、各行為者が持つ権限(credential)の集合を集合演算で合成する枠組みである。委譲・信頼・拒否権をどの条件で誰に配分するかを、経験則ではなく形式的な条件として書き下せる点に特徴がある。

従来のAIエージェントの信頼フレームワークは、人間が権限を下方に委譲し、委譲連鎖に行為者が加わるほど権限は狭まるだけ(単調縮小)と想定してきた。ソース[1]はこの想定を、権限合成の一つの特殊ケースとして位置づけ直す。その上で、単調縮小がいつ成り立ち、成り立たない場合に何が代わりに現れるかを理論化している。

AI Nativeな設計にとって重要なのは、この構造が特定の技術世代に依存しない点にある。行為者が人間でもAIでも組織でも、「権限がどう合成され、どこで判断権を手放さないか」という問いは同じ形で立てられる。ソース[5]も、同じ記述装置が個人、組織、人間とAIの混成チームに適用できると述べている。

## メカニズム

以下は、行為者の種別を入れ替えても成立する構造的原理として整理したものである。

### 1. 権限の合成(単調縮小の一般化)

ソース[1]では、各行為者が権限集合を持ち、有向行為者グラフの辺の上で四つの集合演算(積集合、和集合、左結合、右結合)によって権限が合成される。従来型の委譲は、根付き木の上での積集合として回復される。つまり「連鎖に加わるほど権限が狭まる」という従来の見方は、この代数の一部にすぎない。

### 2. 単調性の条件

ソース[1]の二分定理は、連合の価値が単調であることが保証されるのは、すべての辺が下位側の端点を「フィルタなしで通す」場合、かつその場合に限ると述べる。これは木、および選言的集約の下での有向非巡回グラフ(DAG)でも変わらない。

さらに、行為者の存在がむしろ連合の認可範囲を厳密に減らす「破壊的仲介者」を特定する正確な基準も示されている(抜粋はここで途切れており、以降の詳細は本記事では扱わない)。

### 3. 委譲による信頼の非対称性

ソース[3]によれば、ツールは操作され、チームメイトは信頼される。AIエージェントが曖昧な要件を持つタスクの責任を引き受けるようになると、委譲の意思は信頼に左右される。権限の合成が形式的に対等でも、委譲の実態では信頼が非対称に配分される。

### 4. 境界での判断権の保持

ソース[4]は、重大な遷移点に設計された制御境界として検証ゲート(Verification Gates)を挙げ、責任を関連する制御を持つ役割に結び付ける「Accountability by Control」の規律を示す。ソース[5]は、人間が主権的な層(sovereign layer)にとどまり、「判断を放棄しない拡張」を原則とする。境界とは、権限が合成される場所であると同時に、判断権を意図的に留保する場所でもある。

## 理論的背景

- **権限代数(ソース[1])**: 人間とAIを構造的な対等者として扱い、権限集合を四つの集合演算で辺上に合成する。古典的な委譲は木の上の積集合という特殊ケースである。単調性の二分定理と破壊的仲介者の基準により、単調縮小の世界観が生き残る条件が明確になる。
- **信頼較正(ソース[2])**: チームはAIの推奨を無批判に受け入れる(自動化バイアス)か、早計に拒否する(アルゴリズム忌避)かのどちらかに偏りがちである。ソースは五段階の信頼較正ルーチン(共同感知、共同フレーミング、共同意思決定、行動とフィードバック、信頼の再構成)を提案し、上書き率と上書き精度を較正された信頼の中核指標とする。拒否権の行使を測定可能にする点で、権限代数の運用面を補う。
- **道具から同僚へ(ソース[3])**: ソフトウェア開発チームで、開発者がAIエージェントをどの条件で信頼して意味あるタスクを委譲するかが問われる。曖昧性への耐性も、関係設計の転換に関わる論点として扱われる。
- **人間・AI・組織の三層(ソース[4])**: 人間は適応し、AIは自らの表現と制約の中で最適化し、組織は両者が働く条件を設計する。この三者を一つの作業システムとして捉え、責任を制御を持つ役割に結び付ける。
- **結合認知体(ソース[5])**: 能力は個々の構成要素ではなく、人間オペレーター、複数のモデル、外部記憶、ツール、環境フィードバックからなるシステム境界の性質として扱われる。

なお、ソース[2]〜[5]の本文は抜粋の範囲でしか確認できておらず、数値的な実証結果は本記事では扱っていない。

## AI Nativeな設計への示唆

1. **委譲を「縮小」だけで設計しない**: 権限合成の演算(積、和、結合)を明示的に選び、辺ごとに下位側を無フィルタで通すかを設計する。単調性が必要な箇所と、そうでない箇所を区別する。
2. **仲介者の影響を検査する**: 連合の認可範囲を減らす破壊的仲介者がいないかを、構造的な基準に照らして点検する。
3. **拒否権を較正して運用する**: 上書き率と上書き精度を指標にし、無批判な受容と早計な拒否のどちらにも偏らないようにする。
4. **判断権の留保点を境界として設計する**: 重大な遷移には検証ゲートを置き、責任は制御を持つ役割に結び付ける。
5. **行為者の種別に依存しない記述を使う**: 人間、AI、組織を同じ代数で記述すれば、構成が変わっても設計原理を再利用できる。
6. **委譲の副作用に備える**: 委譲は所有感や能力の侵食を招きうるため、回復的な足場設計を併せて考える(関連コンセプト参照)。

## 関連コンセプト

- [[trust-free-boundary-enforcement-for-autonomous-actors]] — 信頼を前提としない実行境界による自律主体の制御
- [[capability-as-system-boundary-property-and-composed-intelligence]] — システム境界に帰属する能力と合成知能
- [[constraint-anchored-validity-and-verifiable-boundaries]] — 制約による妥当性の担保と検証可能な境界
- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による所有感・責任・能力の侵食と回復的足場設計
- [[epistemic-labor-displacement-under-delegation]] — 委譲による認識的労働の代替と判断力の空洞化
- [[inspectable-causal-structure-as-decision-legitimacy-condition]] — 検査可能な因果構造による意思決定の正当化

## 参考ソース

1. Yaroslav Ryabov (2026). "The Game of Peers: Toward a Credential Algebra for Human-AI Actor Networks". File: raw/papers/operations_research/the-game-of-peers-toward-a-credential-algebra-for-human-ai-actor-networks.md
2. Iva Atanassova, Huda Khan, Zaheer Khan (2026). "When Should Your Team Override AI? A Trust Calibration Routine". File: raw/papers/organization_science/when-should-your-team-override-ai-a-trust-calibration-routine.md
3. Kasra Dolatkhahi, Yafang Li (2026). "From Intelligence to Delegation in Human-Agent Teams in Software Development". File: raw/papers/organization_science/from-intelligence-to-delegation-in-human-agent-teams-in-software-development.md
4. Jaina Ko (2026). "Human, AI, and Organizational Performance (HAOP): A Safety Framework for the AI Era". File: raw/papers/organization_science/human-ai-and-organizational-performance-haop-a-safety-framework-for-the-ai-era.md
5. Andreas Ehstand (2026). "Coupled Human-Artificial Team Cognition: A Restricted Methodological Archive (2026-08)". File: raw/papers/organization_science/coupled-human-artificial-team-cognition-a-restricted-methodological-archive-2026.md
