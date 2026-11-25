# 出自追跡可能性に基づく認識論的協働

人間とAIシステムが「ともに考える」とき、その協働は単に人間とAIが同じ場に存在するだけでは成立しない。主張がどこから来たのか(出自)を追跡でき、誰がどの権威で何を主張しているかが明示的に分離されていること——これが相互的な知的協働を成立させる不変条件である。この構造を欠くと、見かけ上の協働は成立していても、意識の共有や検証済みの学習効果といった過大な主張に横滑りしてしまう。AI Nativeな設計において、この条件は協働の実質性を測る基準として機能する。

## 概要

出自追跡可能性に基づく認識論的協働とは、人間とAIという異種エージェント間での相互的な知的作業(reciprocal epistemic collaboration)が真に成立するために必要な構造的要件を指す。この要件は、協働問題解決・分散認知・チーム認知・共有調整・認識論的共同エージェンシーといった既存の人間-AI学習研究の知見を活用しつつも、それらが提供しきれない厳密な境界線を引く。中核となるのは、主張の出自を追跡できること(出自追跡可能性)、誰の権威に基づく主張かを分離すること(権威の分離)、そして採用されずに棄却された説明的分岐を保存すること(棄却された分岐の保存)の三つのメカニズムである。

## 理論的背景と知見

この構造は「Co-Constructed Thinking Space(CCTS)」という枠組みとして提示されている。CCTSは、協働の有無を判定するためのリポジトリ定義された、出自に境界づけられた相互作用・成果物フレームワークである。

この研究が重要な批判を加えているのは、既存の人間-AI協働研究の多くが、協働の「存在」と協働の「成立の質」を混同している点である。人間とAIシステムが共在して問題解決を行ったという事実だけでは、両者の間に対称的な認知や持続的なAIアイデンティティ、検証された学習効果が存在すると主張する根拠にはならない。CCTSはこの混同を避けるため、協働が成立したと認めるための明示的な要件を列挙する。具体的には、明示的な問題表現の存在、実質的な双方向の修正や異議申し立て、主張の出自に基づく役割の明示(source-role provenance)、主張の境界の明確化、権威の分離、そして棄却された説明的分岐の保存である。さらに、より強い長期的プロファイルでは、外部証拠・リポジトリ上の成果物・実装上の証拠・持続的な成果物・再入構造(re-entry structure)の結び付けが追加要件となる。

この枠組みは、型付けされた構造的契約(typed, fail-closed structural contract)として実装されており、要件を満たさない協働事例は明示的に「失敗」として棄却される(fail-closed)設計になっている。これにより、協働の有無についての主張自体が反証可能性を持つ。

## AI Native な設計への示唆

- **出自の明示的記録を協働インフラの一部とする**: 誰が、どの根拠で、どの主張をしたかを記録・追跡できる仕組みを協働システムの基盤に組み込む。これは事後的な説明責任のためだけでなく、協働が「本物」であるかを判定するための構成要件である。
- **権威を主体から機械的に分離する**: 人間の権威とAIの権威を混在させず、どの発話がどの種類の権威(経験的根拠・規則適用・推論など)に基づくかを明示する。権威の暗黙的な融合は、過大な協働主張の温床となる。
- **棄却された分岐を消去せず保存する**: 採用されなかった仮説・反論・代替説明を破棄せず記録に残す設計は、協働プロセスの再検証性と、後からの異議申し立てを可能にする。
- **協働の成立条件を型として検査可能にする**: 協働が成立したかどうかを人間の印象判断に委ねず、問題表現・双方向修正・出自・境界・権威分離・分岐保存といった要件を構造的契約として検査する仕組みを設計に取り込む。
- **過大な主張への自動的な歯止めを設ける**: 要件を満たさない場合は「協働が成立した」という主張自体をfail-closedで無効化し、意識の共有や対称的認知といった根拠薄弱な言明が流通しないようにする。

## 関連概念

[[human-ai-collaborative-cognition]], [[human-ai-common-ground]], [[human-provenance-attribution-framework]], [[evidence-provenance-coupling-and-illusory-independence]], [[epistemic-responsibility-and-authorship-anchoring]], [[epistemic-agency-preservation-under-offloading]], [[role-separated-layered-agent-architecture]], [[evidence-grounded-role-separated-agent-coordination]], [[authority-bounding-by-parallel-independent-layers]], [[justification-recoverability-over-information-persistence]]

## 参考ソース

* **タイトル**: Co-Constructed Thinking Space (CCTS): A Provenance-Bounded Framework for Human–AI Reciprocal Epistemic Collaboration (2026)
  **ファイルパス**: `raw/papers/cognitive_science/co-constructed-thinking-space-ccts-a-provenance-bounded-framework-for-humanai-re.md`
