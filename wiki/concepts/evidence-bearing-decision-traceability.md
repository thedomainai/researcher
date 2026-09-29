# 証拠を伴う意思決定の追跡可能性

## 概要

証拠を伴う意思決定の追跡可能性(Evidence-Bearing Decision Traceability)とは、判断・データ・改訂が、第三者が検証できる証拠として残って初めて説明責任が成立する、という構造的原理である。ここでいう証拠には、因果経路の宣言、データの系譜(lineage)、署名付き記録、開示可能な変更履歴が含まれる。担当者の想起や組織の自己申告は、たとえ内容が正しくても証拠にはならない。

AI Nativeな社会では、判断の主体が人間・AI・組織にまたがり、データ変換や意思決定が高速かつ大量に発生する。関係者の記憶や善意に依拠した説明では検証が追いつかない。そのため、判断の根拠を最初から検証可能な形で記録に残す設計が、正当性の前提条件になる。

## メカニズム

この原理は、対象が人間・AI・組織・技術のいずれであっても、次の三つの構造として整理できる。

1. **検証可能な証拠の連鎖**
   判断(出力)、その入力データ、判断に至る経路、そして事後の改訂が、途切れなく結び付けられる。各要素は、それを主張する当事者とは独立した第三者が確認できる形式(署名、ハッシュ、公開された版管理など)で固定される。
2. **情報の非対称性の縮減**
   判断する側は自らの内部事情を知っているが、検証する側は知らない。証拠の開示可能性は、この差を縮める。監視技術が情報の非対称性を減らすことで相手方の行動に影響を与える、という組織的メカニズムも、この構造の一例と読める。
3. **監査可能性による正当性の担保**
   権力や判断の正当性は、意思決定プロセスの透明性と、説明責任への制度的なアクセスに依存する。監査できる状態そのものが、正当性の根拠になる。

これらに共通するのは、「あとから誰でも確かめられる」という点であり、「その場で誰かが覚えている」ことではない。

## 理論的背景

### 因果経路の宣言と署名付き証拠パケット(ソース1)

Causal Evidentiary Governance(CEG)は、信用審査・採用・資源配分といった高リスクなMLシステムを対象にしている。既存の公平性ガバナンスは、観察的な公平性指標、事後的な説明可能性、改ざん不能な監査ログに依拠しているが、因果的な帰属と効率的な証拠検証への支援は限定的だと指摘される。

CEGでは、規制対象の機関が版管理されたDAG(有向非巡回グラフ)にコミットし、因果経路を「許容される経路」と「禁止される経路」に分割する。禁止経路に起因する予測の変動は Causal Harm Rate として測られる。各判断には署名付きの Decision-Evidence Packet(DEP)が添えられ、予測を、公開DAGのダイジェストおよび経路別の帰属に暗号的に結び付ける。DEPのダイジェストはMerkle木に追加でき、対数コストの包含証明が可能になる。

### データ系譜を「記録から」答える(ソース6)

AI Data Governance Frameworkは、ある機密データがAIシステム内にあってよいかという問いに、多くの機関が想起で答えている状況を指摘する。答えが正しくても、それは証拠ではない。そこで、Classify・Bound・Prove・Gate などの順序立った段階からなる制御系により、同じ答えを記録から導く。特に Prove の段階では、証明された出所から変換を経て利用地点に至る系譜グラフを構築する。データ系譜の可視化と証明可能性が、規制対応と説明責任の根本的な制約として位置付けられる。

### 開示されない改訂の測定(ソース3)

Silent Revisionは、フロンティアAI開発者の安全フレームワークの改訂を対象に、silent revision rate(重要な変更のうち、開発者自身の公開説明が特定していない割合)を導入した。EUとカリフォルニアはこれらの文書を説明責任の手段とみなし、改訂にも義務を課しているが、改訂が読者にとって判読可能であることまでは要求していない。研究は、12開発者の全公開版をハッシュ固定したコーパスとして公開し、710のコミットメント事例を12組の連続する版の間で追跡した。変更履歴の開示品質を定量測定できることを示した点が重要である。

### 議論の構造的質による説明責任(ソース2)

AIの適切な振る舞いに絶対的な正解が置けない場合、評価は曖昧性に直面する。この研究は代替基準として、批判的な問いに対してモデルが自らの判断を防御できる議論の構造的質を、Waltonの論証スキームとGovierの論証妥当性基準に基づく4段階の弁証法的プロトコルで測定する。判断に先立つ推論と事後的な正当化の両方を扱う。判断に理由の構造を伴わせ、検証に耐えるかを問うという意味で、証拠を伴う説明責任の一形態といえる。

### 再現性と実践的な記録コスト(ソース4)

Barbaは、再現可能な研究の実践(テスト、コミット履歴、リポジトリ構造、指示、意思決定記録)をAIコーディングエージェントに対するコンテキストエンジニアリングとして捉える。エージェントはこれらの維持コストを下げ、利益を即時的にする。ただし、これらの成果物と、そこに符号化された科学的判断を検証する責任は研究者に残る、と論じる。

### 監視技術と非対称性(ソース5)

買い手のAI活用型環境ガバナンスへの曝露が、サプライヤーの環境問題を減らすかを、組織的情報処理理論とシグナリング理論により検討した研究である。41か国・2,505社のパネルデータを用いる。監視技術が情報の非対称性を縮減し、相手の行動に影響を与える組織的メカニズムを扱っており、検証可能性が行動を規律する構造の実例となる。

### 統治原則と枠組みの関係(ソース7・8)

Principles of Good Governance in the Age of AI は、合法性・透明性・説明責任の原則を軸に、ブラックボックス問題、責任の拡散、アルゴリズムによる裁量を課題として論じる。The Defensible AI Framework Registry は、9つのフレームワークについて、どれが他の成果物・証拠・権限を供給するかを示す関係台帳を公開する。統治の成熟は単一の枠組みではなく、枠組み間の関係と階層で定義されるという見方を示す。

## AI Nativeな設計への示唆

- **判断時に証拠を発行する**:事後に説明を組み立てるのではなく、判断と同時に、根拠となる経路・版・入力を束ねた署名付き記録を出す(DEPの発想)。
- **許容される因果経路を事前に宣言する**:版管理された宣言にコミットし、その宣言のダイジェストを各判断に結び付ける。
- **データ系譜を記録から導出する**:「誰かが覚えている」ことに依存せず、出所から利用地点までの系譜を検証可能にする。
- **改訂を判読可能にする**:方針やフレームワークの変更は、版の固定と、何が変わったかを特定する変更履歴の公開をセットにする。開示の質は測定できる。
- **理由の構造を検証対象にする**:正解が定まらない領域では、批判的な問いに対する防御の構造的品質を評価対象にする。
- **検証コストを下げる**:包含証明の対数コスト化や、エージェントによる記録維持の自動化により、証拠の生成・確認を継続可能にする。ただし成果物の検証責任は人間に残る。

## 関連コンセプト

- [[decision-event-governance]] — 意思決定イベントを単位とするガバナンス
- [[evidence-obligation-and-ambiguity-retention-in-autonomous-systems]] — 自律システムにおける証拠義務
- [[causal-grounding-over-correlation]] — 相関を超える因果的根拠づけ
- [[context-engineering-cost-structure]] — 文脈維持コストと再現性の構造
- [[ai-explainability-decision-making]] — AI説明可能性と意思決定支援
- [[moral-competence-as-structural-coherence]] — 構造的一貫性と価値多元性下の統治
- [[evidence-based-management]] — エビデンスベースドマネジメント
- [[ai-decision-authority-restructuring]] — 意思決定権限の再構成

## 参考ソース

1. Causal Evidentiary Governance for High-Risk Machine Learning Systems — Samah Kareem, Barış Çeliktaş (2026)
   `raw/papers/ai_governance/causal-evidentiary-governance-for-high-risk-machine-learning-systems.md`
2. Measuring AI Accountability Through Argumentation Analysis: Can Model Reasoning Withstand Scrutiny? — Daan R. Henselmans, Derck W. E. Prinzhorn, Arno Libert (2026)
   `raw/papers/ai_governance/measuring-ai-accountability-through-argumentation-analysis-can-model-reasoning-w.md`
3. Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers — Louis Yiven Zhu (2026)
   `raw/papers/ai_governance/silent-revision-measuring-undisclosed-change-in-the-safety-frameworks-of-frontie.md`
4. Reproducibility in the Age of Agentic AI: Context Engineering at the Timescale of a Codebase — Lorena A. Barba (2026)
   `raw/papers/ai_governance/reproducibility-in-the-age-of-agentic-ai-context-engineering-at-the-timescale-of.md`
5. Buyer Artificial Intelligence-Enabled Environmental Governance and Supplier Environmental Controversies: An Organizational Information Processing and Signaling — Yongchao Martin Ma, Xinya Guan (2026)
   `raw/papers/ai_governance/buyer-artificial-intelligence-enabled-environmental-governance-and-supplier-envi.md`
6. The AI Data Governance Framework: A Five-Stage Control System for the Data Boundary in AI Systems — Nabeel A. Khan (2026)
   `raw/papers/ai_governance/the-ai-data-governance-framework-a-five-stage-control-system-for-the-data-bounda.md`
7. The Defensible AI Framework Registry: Definitions and Relationships for the Governed Production AI Discipline — Nabeel A. Khan (2026)
   `raw/papers/ai_governance/the-defensible-ai-framework-registry-definitions-and-relationships-for-the-gover.md`
8. Principles of Good Governance in the Age of AI — Sanketh kumar, U. Roopa (2026)
   `raw/papers/ai_governance/principles-of-good-governance-in-the-age-of-ai.md`
