# 判断の残余と説明責任ギャップ

## 概要

**判断の残余(judgment residual)** とは、機械が客観的で検証可能なタスクを担うようになっても、解釈・社会的意味づけ・責任の引き受けといった判断が人間の側に残り続ける、という構造を指す。**説明責任ギャップ(accountability gap)** とは、その残余的判断を担うはずの人間が、不透明なシステムや分散した関与者の間で責任を特定・行使しにくくなる状態である。

AI Nativeな社会設計では、機械への委譲範囲が広がるほど、この二つが同時に問題化する。委譲によって「誰が判断したのか」「誰が答えるのか」が見えにくくなる一方、意味や責任の判断そのものは消えないためである。したがって設計課題は、自動化の度合いを上げることではなく、残余する判断を人間が実際に担える条件を保ち、責任を相互統制のもとに置くことにある。

## メカニズム

対象を人間・AI・組織・技術のいずれに置き換えても成り立つ構造として、次の四つに整理できる。

1. **認識的限界による不透明性**:判断を担う主体(深層学習モデル、専門部署、外部委託先など)の内部論理が、それに依存する側から検査できない。評価手法が操作可能である場合、外見上の性能と実質的な妥当性も乖離する。
2. **責任の分散と希薄化**:設計者、運用者、政策決定者など関与者が多層化すると、責任が各所に薄く分散し、誰も全体に対して答えない状態が生まれる。
3. **解釈・文脈判断の人間残余**:客観的な観察や抽出は機械化できても、文脈推論や社会的意味の判断は残る。責任を負うために必要な判断能力を機械が持たない場合、その部分は人間が担うしかない。
4. **相互制御による説明責任構造**:利害が対立し得る主体同士が互いを検証し合う仕組みによって、説明責任は成立する。単一主体の善意や自己申告に依存しない。

この四つは連鎖する。不透明性が責任の分散を助長し、分散が残余判断の担い手を曖昧にし、その曖昧さを相互制御の設計で埋める必要が生じる。

## 理論的背景

### 軍事AIにおける認識的条件と説明責任ギャップ

Drapierらの論文は、深層学習システムが武力行使の意思決定を媒介する状況を扱う。抄録によれば、その内部論理は検査に抵抗し、評価実践は操作可能であり、配備は関与者間で説明責任を分断する。論文はこれを、自律兵器が殺傷を許されるか否かという問題にとどまらず、**責任ある人間の判断の条件が、重要機能を不透明なアルゴリズムに委ねた後も存続できるか**という、本質的に認識的な問題として位置づける。

そこから具体的な説明責任ギャップが生じるという。責任は設計者・運用者・政策決定者に拡散する一方、国際人道法は現行のAIが持たない判断能力を前提としている。対応として、名指しされた説明責任の役割、非公開要素を含む敵対的監査などにより、倫理的制約を手続き化するガバナンス枠組みが提案されている(抜粋が途中で終わっているため、枠組みの全体像は本記事では詳述しない)。

### 客観タスクと解釈タスクの分界

Shenらは、人間中心の研究におけるビデオ分析を対象に、視覚言語モデル(VLM)がどこまで単独で分析でき、どこで人間の関与が必要かを検討している。CHI 2026の全論文1,702本を分析して、ビデオに注釈を付けている125本を特定し、反復的コーディングにより五次元の分類を導出した。要約上の知見は、VLMは客観的な観察タスクでは有効だが、解釈・文脈推論・社会的意味の判断では人間の介入が不可欠、というものである。判断の残余が実務の作業分担として現れる例といえる。

### 相互制御の歴史的原型

Elsの章は、メソポタミアの粘土板からパチョーリによる1494年の複式簿記の体系化、産業革命や1929年の株式市場暴落を契機とした規制、現代のAI支援分析や統合的サステナビリティ開示までを、財務諸表分析の歴史としてたどる。本コンセプトとの関連では、複式簿記を、利害相反下で説明責任を成立させる相互制御メカニズムの原型として捉える点が重要である。組織が自らの活動を説明する言語(財務諸表)を批判的に読む能力の分布が偏っているという指摘も、説明責任が制度だけでなく読み手の能力に依存することを示唆する。

### 自動化による責任と倫理的主体性の侵食

Birherらは、SFを、軍事自動化・人間による統制の侵食・責任の拡散の関係を極端なシナリオで分析可能にする「投機的モデリング」として扱い、自律・半自律兵器の技術的特性と対照する。規範的枠組みとして、教皇レオ14世の回勅 *Magnifica humanitas* を用い、AIの軍縮を技術競争、権力集中、自動意思決定の社会・倫理問題へと拡張している。自動化が人間の責任と倫理的主体性を損なうメカニズムの分析として位置づけられる。

## AI Nativeな設計への示唆

以下は、上記ソースの知見から導かれる設計上の指針である(具体的な実装はソースに記載されていない部分を含む解釈である)。

- **判断の残余を事前に特定する**:タスクを客観的観察(機械に委ねやすい)と、解釈・文脈・社会的意味の判断(人間に残る)に分け、後者を明示的に人間の責務として設計する。関連: [[administrative-substitution-and-judgment-residual]]。
- **責任の担い手を名指しする**:責任が設計者・運用者・政策決定者に拡散することを前提に、役割ごとの説明責任を手続きとして固定する。[[accountability-requires-ontological-conditions]]、[[ai-accountability-attribution]] が扱う帰属条件と接続する。
- **不透明性を前提に検証経路を設ける**:内部を検査できないことを前提に、外部からの敵対的監査など、内部説明に依存しない検証を組み込む。[[opacity-verification-gap]] を参照。
- **相互制御を設計原理にする**:単一主体の自己申告ではなく、利害の異なる主体が互いを検証する複式簿記型の構造を、AI運用にも適用する。
- **人間が判断できる条件を保つ**:名目上の承認者を置くだけでなく、判断に必要な時間・情報・能力が確保されているかを確認する。[[decision-cycle-compression-and-residual-authority]] と関連する。
- **ハイブリッド統制を要件化する**:人間と機械の統制を混成させ、どの局面で誰が最終判断を持つかを事前に決める。

## 関連コンセプト

- [[administrative-substitution-and-judgment-residual]] — 管理機能の代替と判断・価値選択への役割移行
- [[accountability-requires-ontological-conditions]] — 責任の帰属条件
- [[ai-accountability-attribution]] — AIシステムの責任帰属
- [[opacity-verification-gap]] — 不透明性と検証可能性の非対称ギャップ
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大と責任・統治設計の乖離
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[decision-cycle-compression-and-residual-authority]] — 意思決定サイクルの圧縮と残余権限の設計
- [[verification-to-authority-conversion-gap]] — 検証可能性から実効的権威への変換ギャップ
- [[recurrent-automation-deskilling-dilemma]] — 自動化と脱スキル化の反復ジレンマ
- [[narrative-mediated-technology-institutionalization]] — ナラティブ媒介による技術の制度化

## 参考ソース

1. Drapier, N., Mauberger, F., Chetouani, A., Chateigner, A. (2026). *The Ethics of Artificial Intelligence in Military Operations*. — `raw/papers/hci/the-ethics-of-artificial-intelligence-in-military-operations.md`
2. Shen, X., Lyu, J., Hwang, S., Yao, H., Patel, S. (2026). *Can Vision-Language Models Analyze Human-Centered Video? Mapping Model Capabilities and Human-AI Collaborative Workflows*. — `raw/papers/hci/can-vision-language-models-analyze-human-centered-video-mapping-model-capabiliti.md`
3. Els, G. (2026). *Perspective Chapter: From Ledgers to Algorithms – A Historical and Contemporary Guide to Financial Statement Analysis*. — `raw/papers/history_of_technology/perspective-chapter-from-ledgers-to-algorithms-a-historical-and-contemporary-gui.md`
4. Birher, N., Gábor, H., Nagy, A. (2026). *WEAPONIZED AI NARRATIVES – FICTION OR PREDICTION?* — `raw/papers/history_of_technology/weaponized-ai-narratives-fiction-or-prediction.md`
