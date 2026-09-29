# 相関を超える因果的根拠づけ

## 概要

相関を超える因果的根拠づけ(Causal Grounding Over Correlation)とは、公正性・帰属・評価の妥当性といった判断を、観察的な相関指標だけに委ねず、因果構造の識別と測定の構成概念妥当性の検証によって裏づけるという原理である。観察データ上の相関は、交絡や擬似相関によって生じうる。そのため、相関指標だけでは「何が結果を引き起こしたのか」「その指標は本当に測りたい概念を測っているのか」に答えられない。

この原理は、人間・AI・組織・技術のどれが判断主体であっても成り立つため、Tier 1(不変原理)に位置づけられる。AI Nativeな社会では、信用・採用・資源配分などの高リスクな意思決定や、モデルの能力・安全性の評価が大規模に自動化される。判断の根拠が相関に留まると、擬似相関に基づく不当な扱いや、測定対象を取り違えた評価が制度として固定化されかねない。そのため、因果的根拠づけは設計の前提条件になる。

## メカニズム

この原理は、次の3つの構造要素として整理できる。

1. **交絡による擬似相関**:第三の変数が原因と結果の双方に影響すると、直接の因果関係がなくても相関が現れる。相関だけを見る手法は、この構造を区別できない。
2. **因果構造の識別**:変数間の因果経路(どこからどこへの影響があるか)を明示的に推定・宣言し、経路ごとに影響を切り分ける。これにより「許容される経路」と「許容されない経路」を区別できる。
3. **測定の構成概念妥当性**:指標や評価が、測ろうとする概念(推論能力、拒否挙動など)を実際に測っているかを検証する。指標間の相関パターンが、概念上の類似・相違と整合しているかが手がかりになる。

主体を入れ替えても構造は変わらない。採用担当者が学歴と成果の相関を見る場合も、AIモデルが属性と結果の関連を学習する場合も、組織がベンチマーク得点で技術を評価する場合も、「相関が因果を意味するのか」「指標が概念を測っているのか」という同じ問いが生じる。

## 理論的背景

### 因果経路の宣言と証拠パケット

Causal Evidentiary Governance(CEG)は、規制対象の機関が版管理された有向非巡回グラフ(DAG)にコミットし、因果経路を許容グループと禁止グループに分割する枠組みである。現行の公正性ガバナンスは、観察的な公正性指標、事後的な説明可能性、改変不能な監査ログに依拠しているが、因果的帰属と効率的な証拠検証への支援は限定的だと論文は指摘する。CEGでは、禁止された因果経路に帰属する予測の変動を Causal Harm Rate として測定する。各決定には署名付きの Decision-Evidence Packet(DEP)が付随し、予測を、公開DAGのダイジェストおよび経路別の帰属に暗号的に結びつける。DEPのダイジェストはMerkle木に追加でき、対数コストの包含証明が可能になる。

### 因果探索による擬似相関の識別

Algorithmic Fairness via Causal Discovery は、機密属性(人種、性別など)と結果の相関の同定に頼る従来の公正性アプローチは誤解を招きやすく、差別の根本原因に対処できないと論じる。バイアスは交絡変数の影響を受ける擬似相関から生じることが多いとして、PCアルゴリズムなどの因果探索で因果経路を識別し、的を絞った介入を設計する枠組みを提案している。

### 測定の妥当性

What AI Benchmarks Actually Measure は、社会科学の収束的妥当性・弁別的妥当性を、56のベンチマークと53のモデルに適応した研究である。同一の概念を測ると想定されるベンチマーク同士でモデル順位の相関が、異なる概念のベンチマーク間より強いかを検証する。項目レベルでは項目反応理論(IRT)モデルを用いる。この研究の位置づけでは、ベンチマーク間の低相関は、測定ツール自体の妥当性不足を示唆する。

### 関連する周辺知見

- 構造的一貫性による評価:Moral Competence Before Moral Content は、判断の安定性・単調性・決定性・パレート実行可能性という4つの構造条件を導入し、道徳的能力を、道徳的基準や専門家基準を参照せずに行動のみから評価可能な「構造的下限」として定義する。
- 実証との照合:GPS-Bench は、政策シミュレーションの妥当性が、もっともらしい振る舞いを観測された結果と比較しない限り確立しにくいという問題意識から、立法記録・ロビー活動開示などの公的証拠に紐づけた評価を行う。
- 分布的監査:Distributional Sociotechnical Audit は、生成AIの交通分野への導入において、異質な集団にわたるリスクの分布を、公平性・合成データ妥当性・世論の異質性を統合して監査する。平均的な指標では見えない偏りを捉える点で、上記の問題意識と補完的である。

## AI Nativeな設計への示唆

- **因果仮定の明示的な宣言**:許容される影響経路と禁止される影響経路を、版管理された因果グラフとして公開し、評価の基準とする。
- **相関指標の単独使用を避ける**:公正性指標は、交絡を考慮した因果的分析で裏づけ、必要に応じて因果探索で構造を検証する。
- **決定と根拠の結合**:意思決定を、その根拠(経路別の帰属など)と暗号的に紐づけ、第三者が効率的に検証できるようにする。
- **評価指標そのものの妥当性検証**:ベンチマークや評価指標を運用に組み込む前に、収束的・弁別的妥当性を確認する。
- **観察的妥当性の外部照合**:シミュレーションや生成結果は、実際に観測された証拠と突き合わせて信頼性を確保する。
- **分布の監査**:平均値ではなく、異質な集団にわたる分布としてリスクを評価する。

## 関連コンセプト

- [[causal-inference-in-ai-ml]] — 因果推論の技術的基盤
- [[inherently-interpretable-causal-ml]] — 因果構造を組み込んだ解釈可能なモデル
- [[evidence-bearing-decision-traceability]] — 証拠を伴う意思決定の追跡可能性
- [[surface-substrate-divergence]] — 宣言と実質の乖離、原因の切り分け
- [[moral-competence-as-structural-coherence]] — 構造的一貫性による評価
- [[esg-financial-performance-link]] — 相関的分析が用いられる事例領域

## 参考ソース

1. Causal Evidentiary Governance for High-Risk Machine Learning Systems(Samah Kareem, Barış Çeliktaş, 2026)— `raw/papers/ai_governance/causal-evidentiary-governance-for-high-risk-machine-learning-systems.md`
2. Algorithmic Fairness via Causal Discovery(Jincheng Zhang, 2026)— `raw/papers/ai_governance/algorithmic-fairness-via-causal-discovery.md`
3. Moral Competence Before Moral Content: Why LLM Agents Lack the Prerequisites for Coherent Alignment(Arno Libert, Derck W. E. Prinzhorn, Daan R. Henselmans, 2026)— `raw/papers/ai_governance/moral-competence-before-moral-content-why-llm-agents-lack-the-prerequisites-for-.md`
4. What AI Benchmarks Actually Measure: Adapting Convergent and Discriminant Validity to Interrogate Fifty-Six AI Benchmarks(Meera Desai, Sang T. Truong, Hanna Wallach, Alex Chouldechova, A. Feder Cooper, 2026)— `raw/papers/ai_governance/what-ai-benchmarks-actually-measure-adapting-convergent-and-discriminant-validit.md`
5. GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis(Linh Le, Melanie Bui, My Chiffon Nguyen, Zachary Schlosser, David Williams-King, 2026)— `raw/papers/ai_governance/gps-bench-a-governance-policy-benchmark-for-automating-policy-analysis.md`
6. Who Bears the Risk When Generative AI Enters Transport? A Distributional Sociotechnical Audit of Algorithmic Equity, Synthetic-Data Validity, and Public Trust(Amir Rafe, Subasish Das, 2026)— `raw/papers/ai_governance/who-bears-the-risk-when-generative-ai-enters-transport-a-distributional-sociotec.md`
