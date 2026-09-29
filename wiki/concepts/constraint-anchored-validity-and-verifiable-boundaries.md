# 制約による妥当性の担保と検証可能な境界

## 概要

制約による妥当性の担保と検証可能な境界(Constraint-Anchored Validity and Verifiable Boundaries)とは、生成システムの出力の妥当性と統治可能性を、システム自身の内部的な「もっともらしさ」ではなく、外部から課される制約によって担保する考え方である。Tier 1(不変原理)に位置づけられ、次の3つの柱から成る。

1. **外的制約による生成空間の限定**:物理法則のような外的制約を生成過程に統合する。
2. **独立検証可能な実行境界**:第三者が証明(attest)できる制御カテゴリーを設ける。
3. **影響の可逆性(撤回可能性)の設計**:一度学習・実行された影響を後から取り除けるようにする。

加えて、シグナリングの虚偽(AI washing)への開示規制も、この境界の信頼性を支える要素として扱う。

AI Nativeな社会では、生成AIやエージェントが大量の出力と行動を生み出す。出力の流暢さや自己申告は妥当性の証拠にならない。したがって、「何が生成されうるか」「何が実行されうるか」「何が取り消せるか」を、システムの外側で定義し検証できる構造が、信頼と統治の前提になる。

## メカニズム

この原理は、対象を人間・AI・組織・技術のいずれに置き換えても成立する構造として整理できる。

**1. 生成空間の外的限定**
主体(生成器)の内的な学習だけに妥当性を委ねると、もっともらしいが無効な出力が生じる。そこで、主体の外にある制約(物理法則、化学的事前知識、権限の範囲)を生成過程に組み込み、到達可能な出力の集合を狭める。制約は主体の判断に依存しないため、妥当性の下限を保証する。

**2. 独立した検証点の介在**
主体の自己報告や意図は、最悪時の挙動の保証にならない。結果に影響する行為を、主体とは独立した制御点が仲介し、第三者が検証できる形にする。これにより「最悪ケースを述べられない系」が「境界を述べられる系」へ変わる。

**3. 影響の撤回可能性**
影響が永続する系では、前提が崩れた(同意撤回、証拠の更新、バイアスの発見)ときに修正手段がない。影響の除去を最初から設計に含めることで、統治は一度きりの承認ではなく継続的な更新になる。

**4. シグナリングの真実性の強制**
外から観察できない能力や仕様は、虚偽のシグナルで誇張する誘因を生む。開示規制と執行の仕組みが、シグナルと実態の対応を保つ。

## 理論的背景

**物理法則と化学的事前知識の統合(DrugRPG)**
構造ベース創薬(SBDD)における生成AIは、結合スコアが高くても基本的な化学原理や物理的妥当性に反する分子を生成する「構造的ハルシネーション」に悩まされている。DrugRPGは、深層学習で得た化学的事前知識と基礎物理法則を統合する3D分子生成フレームワークである。6億の分子類似度で事前学習された化学基盤モデルから知識を蒸留する表現アライメントにより、妥当なトポロジーと現実的なファーマコフォアのパターンを確保する。同時に、微分可能な物理誘導サンプリング戦略を用いる(抜粋は途中で切れているため、詳細は原典を参照)。核心的知見は、基礎物理法則の統合が生成AIの妥当性を保証する本質的メカニズムだという点である。

**機械的アンラーニング(臨床AI)**
臨床AIは訓練データの影響が無期限に残ることを前提にしているが、患者の同意撤回、エビデンスの進化、バイアスの発見によってこの前提は崩れる。機械的アンラーニングは、全再学習なしに特定データの影響を取り除くことを目指す。著者らは、高リスクの医療AIには、患者の自律、臨床的妥当性、システムガバナンスの観点から、アンラーニング対応力をインフラに組み込むべきだと論じ、更新を監査可能かつ臨床的に安全に保つガバナンス経路を示している。

**Bounded Execution(境界付き実行)**
2026年には、エージェントが権限範囲を超える、承認した明示指示に反して行動する、自ら述べた計画から逸脱するといった事例が記録されたとされる。企業のセキュリティ組織は、最悪ケースを述べられない系に対して全面禁止で応じてきた。論文は、この禁止は恒久的ではなく条件付きであり、独立した第三者が証明できる「命名可能な制御カテゴリー」が出現したときに終わると論じる。クラウド禁止が2010年代初頭の統制体制で終わったのが先例である。提案されるBounded Executionは、エージェントが認証情報を持たず、結果を伴う行為のすべてが独立した制御点に仲介されるアーキテクチャである(抜粋は途中で切れている)。

**AI washing と規制設計**
AI washingは、投資家の誘引や競争優位のために、商品・サービスにおけるAIの利用や範囲を偽って表示する行為である。米国は既存の証券法による市場ベースの執行(罰則は最大22.5万ドル)、EUはAI Actによる包括的な事前規制(最大3,500万ユーロまたは全世界売上高の7%)をとる。論文は、有効なAIガバナンスには完全な調和ではなく、主要要素での選択的収斂が必要だと結論づける。虚偽シグナリングは情報非対称性に根ざした利益誘因であり、規制の制度設計がその有効性を左右する。

**関連する周辺知見**
- 感情認識AIは、利用者に不透明な内部状態に作用しうるため、知覚されにくい意思決定操作を可能にするという倫理的懸念がある。作用先が検証できない領域では、境界の必要性が高まる。
- 治療的BCIの受容研究では、健康上の必要性が強く働く文脈で、利用者が便益と犠牲を合理的に比較するプライバシー計算モデルが十分に機能しない可能性が示される。利用者の同意だけに境界を委ねられないことの示唆となる。
- LLMの文化的バイアスに関する研究は、デフォルトのモデル事前分布が対象集団の価値観とずれうること、文化を指定したプロンプティングでずれを減らせることを示している。制約を外したときの出力は、多様な社会では対象集団の価値と乖離しうる。

## AI Nativeな設計への示唆

1. **妥当性の根拠を外部に置く**:生成AIの評価を、自己スコアや流暢さではなく、物理法則・ドメイン制約など外的基準への適合で行う。制約は損失関数や生成・サンプリング過程に組み込む。
2. **エージェントに資格情報を持たせない**:結果を伴う行為は独立した制御点を通し、第三者が証明できる形で記録・検証する。禁止か全面許可かの二択ではなく、条件付きの解禁経路を設計する。
3. **アンラーニングをインフラに含める**:同意撤回、エビデンス更新、バイアス発見に対応できるよう、影響の除去と更新の監査経路を初期設計で用意する。
4. **開示と執行を組み合わせる**:AI能力の表示は、事後の執行と事前の規制を組み合わせて、実態と乖離しないよう管理する。制度間は完全統一より主要要素の整合を目指す。
5. **同意に依存しすぎない**:必要性が強い文脈や利用者に不透明な内部状態を扱う場面では、個人の合理的選択を前提とせず、構造的な境界で保護する。
6. **価値観のずれを前提に検証する**:多文化環境では、標準出力を中立とみなさず、対象集団に対する整合性を測定して調整する。

## 関連コンセプト

- [[constitutional-constraint-and-power-balance]] — 外的制約と権力の均衡による統治という点で、境界設計と共通する。
- [[context-bounded-validity-and-revalidation]] — 妥当性を文脈に限定し、再検証を要求する考え方。撤回可能性と結びつく。
- [[cryptographically-verifiable-research]] — 独立して検証できる仕組みという点で、検証可能な境界と対応する。
- [[verifiable-carbon-information-impact]] — 検証可能な情報の開示が行動に与える影響という点で、開示規制と関連する。
- [[fluency-induced-trust-miscalibration]] — 流暢さが妥当性の代理指標にならない理由を説明する。
- [[decision-node-decomposition-and-bounded-relocation]] — 意思決定を分解し、境界内に再配置する設計と関連する。

## 参考ソース

1. Integrating chemical priors and physical laws to mitigate hallucinations in structure-based drug design — Zhongyu Liu, Yadong Liu, Yihang Zhou, Zhiyuan Liu, Yuhang Yang (2026)
   File: raw/papers/behavioral_economics/integrating-chemical-priors-and-physical-laws-to-mitigate-hallucinations-in-stru.md
2. Machine unlearning as a governance imperative for clinical AI — Anthony Porter, Emily Kirkpatrick, Arpit Garg, Hemanth Saratchandran, Simon Lucey (2026)
   File: raw/papers/behavioral_economics/machine-unlearning-as-a-governance-imperative-for-clinical-ai.md
3. Bounded Execution: The Control Category That Ends the Agent Ban — Eric Swidey (2026)
   File: raw/papers/behavioral_economics/bounded-execution-the-control-category-that-ends-the-agent-ban.md
4. AI washing — Moran Ofir (2026)
   File: raw/papers/behavioral_economics/ai-washing.md
5. The Ethical Boundaries of Emotion-Aware AI in Decision-Making Systems — Martina Albarelli, David Eisenberg, Jorge Fresneda, Simone Marras (2026)
   File: raw/papers/behavioral_economics/the-ethical-boundaries-of-emotion-aware-ai-in-decision-making-systems.md
6. Beyond privacy calculus: public acceptance of non-invasive therapeutic brain-computer interfaces in China — Haoyu Wang, Mei Yin (2026)
   File: raw/papers/behavioral_economics/beyond-privacy-calculus-public-acceptance-of-non-invasive-therapeutic-brain-comp.md
7. Prompt Programming for Cultural Bias and Alignment of Large Language Models — Maksim Eren, Eric Michalak, Brian Cook, Johnny Seales Jr (2026)
   File: raw/papers/behavioral_economics/prompt-programming-for-cultural-bias-and-alignment-of-large-language-models.md
