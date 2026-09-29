# タスク標準化可能性による代替境界の決定

## 概要

タスク標準化可能性による代替境界の決定とは、ある機能・タスクがどれだけ標準化(コード化)でき、その出力をどれだけ検証できるかによって、AIが人間を「代替」するか「補完」するかの境界が決まるという原理である。同じAI技術でも、標準化・検証が容易なタスクは代替に、文脈判断・対人コミュニケーション・説明責任を要するタスクは人間側に残りやすい。さらにこの選別は、生産性・雇用・規模という三つの目標の配置をセクターごとに異ならせる(トリレンマ)。

AI Nativeな社会設計にとって重要なのは、「AIは仕事を奪うか」という一括の問いが不適切だと示す点にある。設計の単位は職業や産業ではなくタスクであり、各タスクの標準化・検証可能性を見きわめることが、役割分担・雇用・制度設計の出発点になる。

## メカニズム

この原理は、対象(人間・AI・組織・技術)を入れ替えても成り立つ次の構造として整理できる。

1. **選別的代替**: 実行主体が誰であれ、仕様を明確に書け、出力を低コストで検証できる機能から順に、より安価な実行主体へ移る。コード化しにくい機能や検証が難しい機能は移りにくい。
2. **効果の複数チャネル化**: 技術の影響は単一の方向ではなく、置換(−)、補完(+)、生産性(+)、新タスクによる再雇用(+)といった複数のチャネルに分かれる。ネットの効果はこれらの相対的な大きさで決まる。
3. **トレードオフ(トリレンマ)制約**: セクターの構造的制約のもとでは、急速な生産性向上、安定的または増加する雇用、スケーラブルな出力拡大の三つを同時には満たせない。各セクターは、拘束条件の組み合わせに応じて異なる配置(レジーム)に落ち着く。
4. **新タスク創出とのレース**: 代替で失われるタスクと、新たに生まれるタスクのどちらが速いかが雇用量を左右する。
5. **責任・検証の残余**: 実行が代替されても、最終判断と説明責任は検証可能性の限界のところで人間側に残りやすい。

## 理論的背景

**タスクベース枠組みの拡張(ソース1)**: Acemoglu と Restrepo のタスクベース枠組みは、労働者を置換する機械を対象に作られた。本論文はそこに、AIの予測が人間の判断を置き換えず精度を高める「補完ゾーン」を加えた。これにより、置換・補完・生産性・新タスクによる再雇用という四つのチャネルを扱う。核心的知見としては、雇用量を決める要因は新タスクの創出だと整理されている。実証には、EU27か国の技術タイプ別AI導入データ(2021年、2025年)などが使われている。

**タスク水準での選別(ソース3)**: 生成AIは自動化の対象を、定型的な身体・計算作業から言語集約的な認知タスクにまで広げた。ただし仕事のすべてが同じように変わるわけではない。標準化・コード化できるタスクは代替されやすく、文脈判断、対人コミュニケーション、説明責任、検証を要するタスクは人間の労働に適している。専門的文章作成やカスタマーサポートの証拠は、AI支援による効率向上を示すとされる。

**セクター別トリレンマ(ソース4)**: 「生産性か雇用か」という単純なジレンマ論を、セクター間の差を無視する範疇の誤りだと批判する。急速な生産性向上、安定的または増加する雇用、スケーラブルな出力拡大の三つが、アルゴリズムに形作られたセクターでは本質的に両立しないと主張する。技術の伸長と事務職の完全な代替が併存する現象は、各産業がこの制約付き最適化問題に対処する仕方の構造的な表れとされる。セクター固有のレジームは、三つの拘束条件の配置で規定される。抜粋には三つのうち最初の「技術的代替可能性」までしか現れないため、残りの条件の詳細は本稿では扱わない。

**スキル価値の極化(ソース5)**: 自動化は可能性に差のある機能を選別的に置換し、スキルの市場価値を極化させる。定型的・自動化しやすいタスクを担う労働者は、置換、賃金圧力、職業上の格下げに直面しうる。一方、AIが人間の能力を補完する場合には、生産性向上や新タスク創出、労働者の成果向上が生じるが、その恩恵は不均等に分配される。

**効果を決める三要素(ソース2)**: 雇用への影響を考える経験則として、規模効果、自動化、拡張の三つが挙げられる。将来の影響予測は、AI能力の成長と人間の調整速度に依存するため難しい。タスクの変化をほぼリアルタイムで測る新しいデータ収集手法も論じられている。

**検証と信頼性の価格付け(ソース8)**: 標準的な自動化の割当ルールを、信頼性に価格を付けるルールに置き換える。スケーリング則から能力のコストを導き、23,235件の公開評価実行からタスク成功の傾きを直接推定している(β̂=0.83、公開日のトレンドは検出されず)。検証と信頼性が代替の時期を左右するという発想を与えるが、市場構造への適用は別の制約に依存するとされる。

**業務領域ごとの境界の現れ方**: 会計の意思決定では、自動化、分析支援、意思決定支援、専門的判断への対話的支援という四段階のAI関与が確認され、最終判断と専門的責任が人間に残る「限定的認知パートナーシップ」が次の段階として提案される(ソース6)。理学療法では、治療的接触、人間的相互作用、倫理・法的責任、専門職としての自律、人間による監督が、AI支援臨床推論の限界として論じられる(ソース7)。

## AI Nativeな設計への示唆

- **タスク単位の分解と診断**: 職業名ではなくタスクごとに、標準化可能性と検証可能性を評価し、代替・補完・人間保持の配置を決める。関連する視点は [[capability-profile-based-task-allocation]] と [[informational-task-entropy]] にある。
- **検証コストを設計変数にする**: 出力の検証が安価なタスクは代替が進む。逆に、検証が高コストな領域では人間の判断を意図的に配置し、[[epistemic-responsibility-and-authorship-anchoring]] のように責任の所在を人間に固定する。
- **セクター別に目標を選ぶ**: 三者トリレンマを前提に、生産性・雇用・規模のうち何を優先するかを、セクターごとに明示的に決める。一律の雇用政策や一律の自動化推進は避ける。
- **新タスク創出への投資**: 雇用量は新タスクの創出に左右されるため、代替の進行と並行して新タスクの創出・移行支援を設計に組み込む。
- **支援が能力形成を損なわないようにする**: 補完のつもりの支援が技能を代替し、育成機会を奪う恐れがある。[[support-induced-skill-substitution-loop]] を参照し、学習機会を残す設計にする。
- **利得と包摂の監視**: 代替の選別は利得の集中や包摂の格差を生みうる。[[productivity-gain-concentration-and-task-boundary-shift]] や [[productivity-labor-decoupling-and-inclusion-gap]] の観点で追跡する。

## 関連コンセプト

- [[productivity-gain-concentration-and-task-boundary-shift]] — 生産性利得の集中とタスク境界の移動
- [[administrative-substitution-and-judgment-residual]] — 管理機能の代替と判断・価値選択への役割移行
- [[capability-profile-based-task-allocation]] — 能力プロファイルに基づく役割分担と協働設計
- [[informational-task-entropy]] — 情報タスクエントロピー
- [[support-induced-skill-substitution-loop]] — 支援代替による能力形成機会の喪失ループ
- [[productivity-labor-decoupling-and-inclusion-gap]] — 生産性と人間の経済的包摂のデカップリング
- [[scale-driven-concentration-and-institutional-lag]] — 規模の経済による集中と制度適応の遅れ
- [[epistemic-responsibility-and-authorship-anchoring]] — 認識論的責任・著者性の人間への固定
- [[multilayer-interaction-determines-adoption-outcomes]] — 人・プロセス・制度の多層相互作用が導入成果を決める

## 参考ソース

1. Isam Atoba, Mohamed Amine Korchi (2026)「AI, human labor, and the task frontier: automation, complementarity, and the net effect of Artificial Intelligence on employment」
   File: raw/papers/economics/ai-human-labor-and-the-task-frontier-automation-complementarity-and-the-net-effe.md
2. Juan M. Lavista Ferres, Frank Nagle (2026)「AI and Labor: Present and Future Scenarios」
   File: raw/papers/economics/ai-and-labor-present-and-future-scenarios.md
3. Yida Li (2026)「Generative Artificial Intelligence and Labour: Displacement and Augmentation at the Task Level」
   File: raw/papers/economics/generative-artificial-intelligence-and-labour-displacement-and-augmentation-at-t.md
4. Simon Suwanzy Dzreke, Semefa Elikplim Dzreke (2026)「The Sectoral Trilemma: A contingent theory of divergent productivity-employment regimes in the age of AI」
   File: raw/papers/economics/the-sectoral-trilemma-a-contingent-theory-of-divergent-productivity-employment-r.md
5. Saidi Juma (2026)「Artificial intelligence and the changing architecture of work: skill adaptation, occupational restructuring and the distribution of labor-market opportunities」
   File: raw/papers/economics/artificial-intelligence-and-the-changing-architecture-of-work-skill-adaptation-o.md
6. Stefan Milojević, Srđan Lalić, Marija Magdincheva-Shopova (2026)「From automation to bounded cognitive partnership: a functional framework of artificial intelligence in accounting decision-making」
   File: raw/papers/economics/from-automation-to-bounded-cognitive-partnership-a-functional-framework-of-artif.md
7. Nilgün Çırak (2026)「Artificial Intelligence in Physiotherapy and the Limits of Clinical Reasoning: A Narrative Review」
   File: raw/papers/economics/artificial-intelligence-in-physiotherapy-and-the-limits-of-clinical-reasoning-a-.md
8. Miquel Noguer Alonso (2026)「The Economics of Artificial Intelligence: Scaling, Verification, Assignment, Capital, Growth, and Value」
   File: raw/papers/economics/the-economics-of-artificial-intelligence-scaling-verification-assignment-capital.md
