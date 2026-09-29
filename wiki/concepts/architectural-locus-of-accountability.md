# アーキテクチャ配置による説明責任の構造的固定

## 概要

アーキテクチャ配置による説明責任の構造的固定(Architectural Locus of Accountability)とは、AIをめぐる責任と統治が、事後的な技術制御(監視、フィルタリング、ログ確認など)ではなく、**境界・モジュール性・層構造といった設計選択によってあらかじめ決まる**という原理である。判断がどこで実装され、誰の権限のもとで確定し、どの主体に対して説明されるか。この配置が、責任の所在を実質的に固定する。

この原理は次の二点を含む。

- **判断の実装と人間の説明責任は不可分である。** 判断をシステムのどこに置くかを決めることは、その判断に誰が答えるかを決めることでもある。
- **説明責任は単一の主体に集約されず、主体の類型や関係(アクター＝フォーラム)に沿って分散配置される。**

AI Nativeな社会設計では、エージェントが委任された権限のもとで実行まで担う。このとき、責任を後付けの運用ルールに任せると、「制御できないものに責任を負う」構造的な緊張が生じる。責任を設計の一次的な対象として扱うことが、この原理の要点である。

## メカニズム

対象が人間・AI・組織・技術のいずれであっても成立する構造的原理として、次の三つに整理できる。

### 1. 境界設計による責任の局所化

判断が「実行可能な判断」になる条件(境界)を先に定め、そこから必要な処理経路、判断構成、証拠取得、権限、人間へのエスカレーション、外部へのコミットメント、更新統制を導出する。境界が責任の及ぶ範囲を区切るので、責任が薄まって拡散することを防げる。

境界が組織の外側にある場合は逆の事態になる。推論・アラインメント・制御が組織の境界外に外部化されると、組織は自らが統治できないAIの挙動について説明責任だけを負う。

### 2. 層構造による説明責任の分散

説明責任は、技術的統制、人間による監督、組織ガバナンス、規制・標準といった複数の層に配分される。各層は、誰が誰に対して何を説明するかというアクター＝フォーラム関係として定義される。特定の層だけに負荷を集中させず、層の組み合わせで追跡・説明・是正を成立させる。

### 3. 判断と責任の不可分性

判断の実装(どのモジュールが、どの権限で、どの証拠に基づいて判断を確定するか)と人間の説明責任は切り離せない。判断を実装する構造を変えれば責任の構造も変わる。したがって責任は、判断が確定する箇所に対応して設計しなければならない。

## 理論的背景

### アーキテクチャによる統治可能性

Tuguldur と Sonpatki(2026)は、公共部門の教育を例に、責任あるヒューマン-AI協働を「アーキテクチャ的統治可能性(architectural governability)」の問題として捉える。これは、AIの挙動が組織の内部で方向づけ・監査・適応できる程度と定義される。構造を規定する条件として、局所性、モジュール性、統治の自律性、社会技術的適合の四つが挙げられている。クラウド中心のLLMアーキテクチャと、ローカルな小規模言語モデル(SLM)によるマルチエージェント構成を対比し、設計の違いが制御・依存・アラインメント能力の配分を変えることを示している。

### 設計可能な統治構成

Mutale らの研究(2026)は、エージェント型AIを企業ワークフローに導入する際の統治を、モデルの透明性にとどまらず、自律的行動のアーキテクチャ的制御の問題として扱う。統治構成を、自律性の較正、人間-エージェントのチーミング、組み込み型の機械学習ガードレールからなる上位構成概念として定式化し、自律性をワークフローのリスクに応じて構造的に監督すべき設計変数と位置づけている。デザインサイエンスの手法で複数の統治構成を設計・比較評価している。核心的知見は、自律性と組織統治は設計可能な構成要素であり、リスク許容度に応じた継続的な較正の体系が必要だという点である。

### 境界優先アーキテクチャ

Mochizuki(2026)の Boundary-First Integrated Judgment Optimization(BF-IJO)は、モデルやオーケストレーションから積み上げる従来の発想を補完する。ハードな許容制約、判断の妥当性条件、有界な性能最適化を分離し、オーケストレーションなどを処理経路・判断構成・更新統制の問題として再定義する。核心的知見は、複雑系における判断実装と人間の説明責任が構造的に不可分であるという点にある。

### エージェンシーの類型論

Fourie(2026)は、先端AIシステムのエージェンシーを三つの次元で類型化する。エージェンシーの性質(道徳的か法的か)、様式(個人か集団か)、所在(人間か非人間か)である。組み合わせから8通りの具現形が得られ、慣習的・争点的・論争的に分類される。法的エージェンシーと道徳的エージェンシーを分離することで、AIを道徳的主体と前提せずに、個別の法的な非人間エージェンシーを検討できる概念的余地が生まれる。これは、責任の配置先を主体の類型に応じて考える根拠になる。

### 階層化された説明責任アーキテクチャ

LAAF(Chaturvedi ら、2026)は PRISMA に従う系統的レビューである。2022年1月〜2026年3月に5つのデータベースを検索し、4,512件から122件の一次研究を採用し、規制・標準文書12件を一次資料として分析した。説明責任を五つの次元に分解されるアクター＝フォーラム関係として捉える社会技術的説明を統合し、技術的統制、人間による監督、組織ガバナンスなど複数のメカニズム群を整理している(抜粋は途中で切れており、四つ目の群の詳細は本ソースの範囲では確認できない)。病院・裁判所・銀行・公共窓口のように、流暢な出力が権威あるものとして扱われ、害を生みうる領域では、説明責任をアクター＝フォーラム関係に沿って分散させる必要があると論じる。

## AI Nativeな設計への示唆

1. **責任を設計段階で配置する。** 判断が確定する箇所ごとに、権限者と説明先(フォーラム)を対応づける。
2. **統治できる範囲に責任の境界を合わせる。** 推論・アラインメント・制御が組織の外にあるほど、責任と統治の乖離は広がる。局所性とモジュール性を確保するか、外部依存に見合った責任の設計を行う。
3. **自律性を設計変数として較正する。** リスク許容度に応じて自律度を調整し、人間へのエスカレーション条件を構造に組み込む。
4. **層で分散させる。** 技術的統制・人間の監督・組織ガバナンス・規制対応を重ね、単一の層への依存を避ける。
5. **主体の類型を区別する。** 法的責任と道徳的責任、個人と集団、人間と非人間を分けて考え、責任の宛先を曖昧にしない。
6. **更新も統制対象にする。** 判断構成の変更を版管理などの統制下に置き、事後の追跡可能性を保つ。

## 関連コンセプト

- [[accountability-requires-ontological-conditions]] — 責任の帰属に必要な条件(判断・追跡可能性・承認)
- [[ai-accountability-attribution]] — AIシステムの責任帰属
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大と責任・統治設計の乖離
- [[judgment-residual-and-accountability-gap]] — 判断の残余と説明責任ギャップ
- [[autonomy-calibration-and-hierarchy-restructuring]] — 自律度の較正と階層再編のトレードオフ

## 参考ソース

1. Tuguldur, T., Sonpatki, R. (2026). *Responsible Human-AI Collaboration as an Architectural Problem: Toward Architectural Governability*. File: raw/papers/human_ai_collaboration/responsible-human-ai-collaboration-as-an-architectural-problem-toward-architectu.md
2. Mutale, W., Kumar, A. P., Sivasubramaniam, N. (2026). *Governing Agentic AI in Enterprise Workflows: A Design Science Approach*. File: raw/papers/human_ai_collaboration/governing-agentic-ai-in-enterprise-workflows-a-design-science-approach.md
3. Mochizuki, K. (2026). *From Orchestration to Integrated Judgment Optimization: A Boundary-First Architecture for Dynamic Teams, Version-Governed Structural Autonomy, and Human-Accountable AI*. File: raw/papers/human_ai_collaboration/from-orchestration-to-integrated-judgment-optimization-a-boundary-first-architec.md
4. Fourie, W. (2026). *A three-dimensional typology of agency for advanced AI systems*. File: raw/papers/human_ai_collaboration/a-three-dimensional-typology-of-agency-for-advanced-ai-systems.md
5. Chaturvedi, P., Ahmad, S., Nowroozi, E., Waqas, M., Loukas, G. (2026). *LAAF: A Layered Accountability Architecture Framework for LLM Applications*. File: raw/papers/human_ai_collaboration/laaf-a-layered-accountability-architecture-framework-for-llm-applications.md
