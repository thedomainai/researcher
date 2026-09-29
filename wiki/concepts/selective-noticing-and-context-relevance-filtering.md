# 選択的注意と文脈的関連性フィルタリング

## 概要

選択的注意と文脈的関連性フィルタリングとは、処理能力が有限な主体が、膨大な刺激のなかから文脈的に関連する情報だけを選び取り、その選別結果に基づいて即座に推論する構造を指す。この構造が、専門性(エキスパティーズ)を成立させる基盤になっていると考えられる。

ソース[1]は教師の「専門的視覚(professional vision)」を、教室内の教育的に関連する出来事を状況特異的に「気づき(noticing)」「推論する(reasoning)」能力として定式化している。専門性は知識量そのものではなく、何を見て何を見ないかを決める選別構造と、その結果を意味づける知識ベースの推論との組み合わせとして現れる。

AI Nativeな設計にとって重要なのは、次の理由による。

- AIが処理できる情報量は人間の限界を大きく超えるが、最終的に意思決定するのは有限な注意資源をもつ人間であることが多い。
- 情報を増やすだけでは判断の質は上がらず、むしろ過負荷とバイアスを招く(ソース[2])。
- 説明や提示の形式を課題に合わせなければ、人間とAIの協働成果は高まらない(ソース[3])。

つまり「何を、いつ、どの形式で人間の注意に載せるか」が設計の中心課題になる。

## メカニズム

以下は対象を人間・AI・組織・技術のいずれに置き換えても成り立つ構造的原理として整理したものである。

1. **有限資源の配分**: 主体の処理容量は有限であり、入力の全量を処理できない。したがって注意という資源をどこへ振り向けるかの選別が必須になる。
2. **選択的知覚(フィルタリング)**: 文脈に照らして関連する手がかりのみを取り込み、その他を捨てる。何が関連するかは、主体の目的・知識・状況によって決まる。
3. **知識に基づく推論**: 選別された情報を、蓄積した知識で解釈し意味づける。ソース[1]では、noticing(選択的知覚)と reasoning(知識に基づく意味づけ)が専門的視覚の二つの中核過程とされる。
4. **課題-表現の適合(cognitive fit)**: 選別・推論の効率は、課題の性質と情報の表現形式が適合しているかで変わる。不適合だと認知負荷が上がり、選別がうまく働かない(ソース[3])。
5. **フィルタの失敗モード**: 選別は必然的に偏りを生む。ヒューリスティクスや選択的注意への依存は認知バイアスと判断品質の低下につながりうる(ソース[2])。また、提案を批判的に吟味せず受け入れる状態では、フィルタが実質的に働かなくなる(ソース[4])。

この構造は、人間の教師にも、AI支援を受ける投資家にも、プログラミング学習者にも共通して観察できる。

## 理論的背景

**専門的視覚の認知モデル(ソース[1])**: 教師の専門的視覚を、noticing(関連する教室の手がかりの選択的知覚)と reasoning/interpretation(気づいた内容を理解する知識ベースの過程)から成るものとして扱う。初心者と熟達教師はこの技能で系統的に異なり、その技能は的を絞った専門性開発によって育成できることが先行研究で示されてきたとされる。既存モデルは気づきと推論の概念的区別を提供してきたが、基盤にある認知過程の理論的な specification が課題であり、同論文はその精緻化を目指している。

**注意バイアスと情報過負荷(ソース[2])**: 情報が多くノイズの大きい株式市場では、投資家が情報過負荷に陥り、ヒューリスティクスと選択的注意に頼って認知バイアスと意思決定品質の低下を招く。体系的文献レビューは、認知バイアスの機序を設計の駆動要因としてAI投資支援に組み込む研究がまだ行われていないこと、インデックスファンド文脈でのAI意思決定支援研究が限られていること、注意バイアスが個人投資家で特に顕著であることを示した。これに基づき、注意バイアスを緩和する概念的なAI意思決定支援アーティファクトが提案されている。

**課題-技術適合と説明戦略(ソース[3])**: タスク-テクノロジー適合理論に基づく2件の行動実験(N=293、323)と2件のEEG実験(N=51、47)により、意思決定課題では事例ベースの説明が、創造課題では特徴ベースの説明が成果を高めた。EEGでは、意思決定課題における事例ベース説明は認知負荷の低減(theta帯域のERS)を通じて体系的処理を支え、創造課題における特徴ベース説明は発散的思考の刺激(alpha帯域のERD)を通じてヒューリスティック処理を促すことが示唆された。

**批判的関与の測定(ソース[4])**: AIコード補完ツールで学生が提案を批判的に評価しないという質的知見を受け、Cloverというツールで操作ログとアテンションチェックを取得した。Tab受け入れ率が高いほど、アテンションチェックへの関与が低いという関連が観察されたと報告されている(抜粋は途中まで)。

**その他の関連知見**: ソース[5]は、コード・実行状態・概念的類推を協調させたAI生成アニメーション(GATs)を提案し、テキスト説明との比較で即時的な学習に選択的な効果があることを示唆している。ソース[7]は、AIの実効性が技術機能より人間の認知制約と目的構造の理解に依存するという設計観を示す。ソース[8]は、能動的な構築と反復的な検証が理解過程の中心にあると論じる。ソース[6]は、計算モデルの説明的妥当性が構造と現象の対応に依存すると論じる。

## AI Nativeな設計への示唆

- **AIは注意の代替ではなく補完として設計する**: AIは大量データの処理とリアルタイム支援を担い、人間の有限な注意には文脈的に関連する要素のみを届ける(ソース[2])。有限な認知容量を外部から補う考え方は [[external-scaffolding-of-finite-cognitive-capacity]] と接続する。
- **認知バイアスを設計の駆動要因に据える**: 人間がどのように偏って注意を向けるかを前提に、その偏りを緩和する提示や介入を組み込む(ソース[2])。
- **課題に応じて説明形式を切り替える**: 意思決定には事例ベース、創造には特徴ベースというように、課題特性と表現を適合させる(ソース[3])。一律の説明形式は避ける。
- **批判的関与を計測し維持する**: 受け入れ操作の頻度や、アテンションチェックへの反応など行動シグナルから関与の低下を検知し、フィルタが機能しているかを監視する(ソース[4])。摩擦のない支援が吟味を弱める可能性に留意する。
- **実行過程や根拠を明示化する**: 初学者が状態や過程を把握できるよう、可視化で認知的に明示する(ソース[5])。ただし生成方式は一時的な実装形態であり、原則は不変と位置づけられている。
- **人間の認知制約と目的構造から出発する**: 機能先行ではなく、利用者が何を見て何を判断するかの構造から設計する(ソース[7])。
- **フィルタの喪失を避ける**: 迎合的な環境ではフィルタリングが働かなくなる懸念があり、[[excess-safety-and-agreeable-partner-filtering-loss]] が関連する。

## 関連コンセプト

- [[external-scaffolding-of-finite-cognitive-capacity]] — 有限な認知容量を外部足場で補う設計
- [[excess-safety-and-agreeable-partner-filtering-loss]] — 過度な支持環境による機能的フィルタリングの喪失
- [[error-correcting-feedback-and-staged-refinement]] — 誤差修正と段階的精緻化による判断の改善
- [[precondition-recorded-revalidation-of-long-running-decisions]] — 事前条件の記録による選択的な再検証
- [[context-bounded-validity-and-revalidation]] — 文脈境界付き妥当性と再検証
- [[vanishing-carrier-tacit-knowledge-preservation]] — 専門家の選別知に含まれる暗黙知の保存
- [[structure-determines-computation-and-emergent-dynamics]] — 構造が計算能力を規定する原理
- [[agency-as-context-and-interaction-design-outcome]] — 相互作用設計が主体性を決める

## 参考ソース

1. Tina Seidel, Ricardo Böheim, Christian Kosel (2026). "Developing a cognitive model of advanced teacher professional vision for understanding processes of noticing and reasoning". File: raw/papers/neuroscience/developing-a-cognitive-model-of-advanced-teacher-professional-vision-for-underst.md
2. Ruiyi Ma, Ying Zhang, David Sundaram (2026). "Mitigating Attention Bias in Index-Fund Investment: AI-Enabled Decision Support for Retail Investors". File: raw/papers/neuroscience/mitigating-attention-bias-in-index-fund-investment-ai-enabled-decision-support-f.md
3. Zhongfeng Wang, Lu Dai, Jia Jin (2026). "Task-Driven Explanation Strategies: Enhance Human-AI Collaboration Performance by Achieving Cognitive Fit". File: raw/papers/neuroscience/task-driven-explanation-strategies-enhance-human-ai-collaboration-performance-by.md
4. Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, K. S. Vasundara Patel, Phuoc Nguyen (2026). "To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks". File: raw/papers/neuroscience/to-tab-or-not-to-tab-measuring-critical-engagement-in-ai-code-completion-tools-u.md
5. Yuri Noviello, Naaz Sibia, Anastasiia Birillo, Thomas Overklift Vaupel Klein, Michael Liut (2026). "AI-Generated Traces for Novice Programmers: Learning Effects and Learner Differences in a Multi-Institutional Study". File: raw/papers/neuroscience/ai-generated-traces-for-novice-programmers-learning-effects-and-learner-differen.md
6. Peng Wang, Olga Viberg, Effie Lai-Chong Law, Samuel Greiff (2026). "When Can AI Models Explain Learning? Validity Criteria for AI as Cognitive Models in Education". File: raw/papers/neuroscience/when-can-ai-models-explain-learning-validity-criteria-for-ai-as-cognitive-models.md
7. Alan Dix (2026). "AI for Human-Computer Interaction". File: raw/papers/neuroscience/ai-for-human-computer-interaction.md
8. Bonni Jones (2026). "From Evidence to Impact: Supporting Sensemaking and Instructional Revision in STEM Classrooms". File: raw/papers/neuroscience/from-evidence-to-impact-supporting-sensemaking-and-instructional-revision-in-ste.md
