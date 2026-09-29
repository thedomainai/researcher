# 能力プロファイルに基づく役割分担と協働設計

## 概要

能力プロファイルに基づく役割分担と協働設計とは、主体(人間、AI、組織など)ごとに異なる「能力の輪郭」を共通の次元で測り、タスクを「自動化する」「共有する」「人間が保持する」のいずれかに配分する設計の考え方である。

Prunty らの研究は、AIを導入する組織が直面する「スコーピング問題」を次のように整理している。どのタスクを自動化でき、どれを人間に残し、どれを両者で分担すべきか、という問題である。集計されたベンチマークスコアは、実運用でシステムがどこで成功・失敗するかをほとんど示さない。一方、モデル能力に関する人間の判断はすぐに陳腐化する[1]。

この配分原理は、特定の技術形態(現在のLLMなど)に依存しない。能力の非対称性を測り、補完性に基づいて分業し、必要に応じて段階的に支援を調整するという構造は、主体や技術が入れ替わっても成立する。AI Nativeな社会設計では、AIの能力が急速に変化し続けるため、固定的な役割分担ではなく、更新可能なプロファイルに基づく配分が重要になる。

## メカニズム

中核となるメカニズムは3つある。それぞれ、対象を入れ替えても構造は変わらない。

### 1. 能力の非対称性

どの主体にも得意・不得意の輪郭がある。重要なのは「AIか人間か」という二分法ではなく、共通の次元で輪郭を描くことである。共通の次元があれば、人間同士、AIモデル同士、人間とAIの間でも比較できる。

### 2. 補完性による分業

タスク側にも要求される能力の輪郭がある。主体の能力プロファイルとタスクの要求プロファイルを突き合わせ、適合度に応じて配分する。

- **自動化**:主体の能力がタスク要求を十分に満たす場合
- **共有**:能力が部分的に補完し合う場合
- **人間保持**:要求が主体の能力を超える、あるいは判断・責任が不可分な場合

### 3. 段階的スキャフォルディング

支援は一律ではなく、個人の特性や認知プロセスの段階に応じて調整される。支援は、必要とされる場面と度合いに合わせて与えられる。

これらは、主体(人間/AI/組織)、タスク、技術形態のいずれを入れ替えても機能する。プロファイルを共通次元で保持する限り、主体側とタスク側は独立に更新できる。

## 理論的背景

### 共通の認知次元によるプロファイリング

Prunty らは、エージェントとタスクを共通の中核的認知能力セットでプロファイルするパイプラインを提案している。

- **認知能力プロファイリング**:各項目の認知的要求が注釈されたベンチマーク群での成績から、エージェントの能力を推定する
- **タスク要求の重み付け**:同じ能力次元について、その仕事における相対的重要度をドメイン専門家から引き出す

両者は共通の認知次元を使うため、モデルや役割が変わっても独立に更新でき、組み合わせてAIの適合度を推定できる[1]。

### 人間の認識的キュレーションとの協調

ビジネスリーダーシップの意思決定に関する系統的レビュー(PRISMAに準拠、Scopus由来の30本)は、AIの限界を説明する概念として「Algorithmic Bounded Rationality」を導入している。限界の例として、データバイアス、文脈的硬直性、事実の不正確さが挙げられる。また、機械の精度と人間の認知的キュレーションの相乗効果を重視する「Triple Helix」モデル(human-in-the-loopガバナンス)が提示されている[2]。

### 認知プロセスに応じた段階的支援

- **文章執筆支援**:Flower と Hayes の認知プロセス理論を、観察可能な執筆行動と適切な支援タイプをつなぐ解釈可能な橋渡しとして仮説化した。形成的研究と文献レビューから14の支援タイプを特定し、AToM CoWriterに実装している[4]。
- **空間ナビゲーション**:方向感覚(SOD)の良し悪しで、視線行動や有効と語るランドマークの種類に系統的な差があることを示した(参加者20名)。その知見からVLMでランドマークを強調するLandmarkLensを構築し、方向感覚の低い8名の追跡研究で場面認識の向上が見られた[5]。

### 認知資源の制約下での分担

会議支援システムInsightToastは、文脈を検索するためのタスク切り替えが個人の集中と会話の流れを妨げるという問題に対し、周辺的なインターフェースで簡潔な洞察を提示する。主要タスクへの集中と背景情報へのアクセスを両立させる設計である[3]。

### 生成と評価の非対称

IdeaForge AIの事例は、AIが研究上の問いを、制度が調査・検証・事業化できる速度より速く生成できるという「豊富さのパラドックス」を扱う。手動のエキスパートモードとAI支援モードを分け、AIは編集可能な値や根拠を提案する形にしている[6]。生成と評価の能力差がある場合に前段のスクリーニングが要請されるが、その判定基準の構造的根拠は未解明とされる。

## AI Nativeな設計への示唆

1. **共通次元でプロファイルを持つ**:AIと人間を同一の能力次元で記述し、モデルの更新や職務の変化に応じて主体側・タスク側を独立に再測定する。人間の印象判断や集計スコアだけに頼らない。
2. **配分を三値で考える**:自動化・共有・人間保持の三区分でタスクを設計する。二分法を避けることで、「共有」領域に協働設計の余地が生まれる。
3. **人間の役割を文脈判断に置く**:機械の精度に、道徳性や文脈判断といった人間の認識的キュレーションを組み合わせ、human-in-the-loopで統治する[2]。
4. **支援は推定と段階に基づかせる**:ユーザーに明示的な指示を求めず、行動から内部プロセスを推定して、段階に応じた支援を出す[4]。個人の特性に合わせた支援も有効である[5]。
5. **注意資源を守る**:支援は主要タスクを妨げない周辺チャネルで提供する[3]。
6. **生成が評価を上回る領域では前段に関門を置く**:編集可能で監査可能な形でAIの提案を扱う[6]。

## 関連コンセプト

- [[contextual-intelligence-allocation]] — 文脈に応じた知能の配分という点で直接関連する
- [[human-continuity-and-orchestration-role]] — 人間が保持する役割(文脈継続性・オーケストレーション)を扱う
- [[metacognitive-allocation-under-finite-resources]] — 有限な認知資源下での配分という共通の課題を持つ
- [[epistemic-labor-displacement-under-delegation]] — 委譲による判断力の空洞化というリスクを示す
- [[costly-verification-allocation-tradeoff]] — 検証コストを踏まえた配分の観点を与える
- [[multidimensional-trust-formation-and-oversight]] — 協働における信頼と監督を扱う
- [[dynamic-capability-amplification]] — 能力の動的な増幅と関連する
- [[ai-driven-task-transformation-sdt]] — AIによるタスク変革を扱う

## 参考ソース

1. Prunty, Tešić, Quinn, Hernández-Orallo, Cheke (2026). "Using profiles of cognitive capability to assess AI suitability for workplace tasks". File: raw/papers/cognitive_science/using-profiles-of-cognitive-capability-to-assess-ai-suitability-for-workplace-ta.md
2. Rachmawati, Hadi, Purnasari, Dar (2026). "Does AI strengthen business leadership decision making: literature review". File: raw/papers/cognitive_science/does-ai-strengthen-business-leadership-decision-making-literature-review.md
3. Abolnejadian, Brehmer (2026). "InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings". File: raw/papers/cognitive_science/insighttoast-proactive-information-retrieval-glanceable-visualization-in-the-sid.md
4. Yoshida, Kobayashi, Tateno, Chen (2026). "Towards Cognitive Process-Aware Proactive Writing Support". File: raw/papers/cognitive_science/towards-cognitive-process-aware-proactive-writing-support.md
5. Li, Sechayk, Hwang, Froehlich, Igarashi (2026). "LandmarkLens: Predicting and Presenting Effective Landmarks for Mixed-Reality Urban Exploration". File: raw/papers/cognitive_science/landmarklens-predicting-and-presenting-effective-landmarks-for-mixed-reality-urb.md
6. Akhtar (2026). "IdeaForge AI: A Dual-Mode, Auditable Research-Question Laboratory for Converting Scientific Ideas into Startup Opportunities". File: raw/papers/cognitive_science/ideaforge-ai-a-dual-mode-auditable-research-question-laboratory-for-converting-s.md
