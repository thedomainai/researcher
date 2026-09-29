# 責任の帰属条件:判断・追跡可能性・承認

## 概要

責任の帰属条件とは、ある主体が責任を負う存在として成立するために満たすべき本体的(ontological)な条件のことである。ソース[4]("Why AI Cannot Sign")は、責任が成立するための条件を**判断性(Deliberative Suspension)**、**可追跡性(Evaluation without Determination)**、**承認性(Signature-as-Commitment)**の三つに整理している。同論文はこれらを法的責任の「連言的(copulative)」な条件、つまり一つでも欠ければ成立しない条件として提示する。

この原理が重要なのは、責任の成立が「能力の高さ」や「自動化の度合い」とは独立に問われるからである。生成AIが法務・医療診断・金融分析などの専門領域に展開されるなかで、「AIは出力に対して責任を負えるか」という問いが改めて浮上している。同論文は、この問いが誤って立てられてきたと指摘する。支配的な議論は「AIに法人格を与えるべきか」を問うが、その前に、法人格が前提とする本体的条件をAIが満たせるかを問うべきだという主張である。

AI Nativeな設計では、意思決定の多くが自動化・半自動化される。その際に三条件を満たす主体が経路のどこにも存在しないと、責任の帰属先が空白化する。したがって、責任の所在は事後的な解釈に委ねず、設計の段階で構造として組み込む必要がある。

## メカニズム

三条件は、対象が人間・AI・組織・技術のいずれであっても適用できる構造的な基準として読める。以下では、ソース[4]の定義を基礎に整理する。

| 条件 | 内容 | 問い |
|---|---|---|
| 判断性 | 自動作用の本当の中断であり、単なる処理ではない | この決定の前に、自動的な流れを止める契機があったか |
| 可追跡性 | 個別の判断に対する合理的な追跡可能性であり、統計的最適化ではない | なぜその判断に至ったかを、理由として辿れるか |
| 承認性 | 特定可能な主体が不可逆な損失にさらされること | 誰が、取り返しのつかない結果を引き受けているか |

### 空白化が生じる構造

責任の空白は、次のような場面で生じうる。

1. **判断が処理に置き換わる**:自動化の連鎖のなかで、中断の契機が存在しない。
2. **理由ではなく最適化の結果しか残らない**:出力は得られるが、個別の判断としての根拠を辿れない。
3. **損失を引き受ける主体が特定できない**:結果に不可逆なコストが生じても、それを負う識別可能な主体がいない。

三条件のうち一つでも欠ければ、能力がいかに高くても責任は成立しない。これが、能力と責任が別の軸であることの含意である。

### 判断権限の委譲と保持

判断権限の委譲と保持は、責任の帰属構造の核をなす。ソース[2]は、生成AIを使う教員養成課程の学生(PSTs)の行動から、二つの対照的なプロファイルを報告している。

- **Orchestrator**:AIの出力を繰り返し制約・修正・再著述し、認識的権威(epistemic authority)を保持した。
- **Outsourcer**:整理・解釈の作業を早い段階でAIに委ね、その枠組みをほとんど修正せずに受け入れた。

この差は、判断が保持されているか委譲されているかという構造の差であり、判断性の条件と直接に対応する。

### 不可逆コストの内部化

承認性は、署名(commitment)を「不可逆な損失にさらされること」として捉える。コストを取り消せる主体は、責任を引き受けているとは言えない。責任とは、判断の結果に伴う不可逆なコストを、特定可能な主体の内部に取り込む構造だと言い換えられる。

## 理論的背景

### Three-Pillar Test

ソース[4]は、上述の三条件を形式化した分析道具として「Three-Pillar Test」を提案する。理論的な基盤としては、哲学的人間学(Gehlen)、判断の理論(Kant、Arendt)、コミットメントの存在論(Jakobs、Taleb)が挙げられている。

### 判断保持と認知的権威

ソース[2]は、質的ケーススタディ(Nexus Analysisと、GoogleのNotebookLMのデジタル痕跡データを用いた分析)から、人間とAIの評価ループにおける主体性・拒否・倫理的判断の場面を分析している。抜粋によれば、二つのプロファイルの差は、認知的権威の関係のなかで現れる。教育設計への含意も論じられている。

### 医療における自律性と尊厳

ソース[3]は、PRISMA 2020に沿った系統的レビューと、生命倫理・技術哲学に基づく解釈学的分析を組み合わせ、臨床判断の自動化と患者の自律性・人間の尊厳との緊張を検討している。核心的知見は、医療の自動化が人間の自律性と尊厳と構造的に衝突するという点にある。

### 組織における意思決定と権威分布

ソース[7]は、84本の文献の系統的レビューと、欧州のAI専門家20名への半構造化インタビューを用いて、生成AIが意思決定の構造化、権威の分布、成果の評価をどう再構成するかを検討している。判断権限が組織内でどう再配分されるかは、責任の帰属に直結する論点である。

### 個人責任モデルの限界

ソース[6](HCSA)は、サイバーセキュリティが従来、意識向上・訓練・個人責任で対応されてきたことを指摘し、個人の判断は組織の文化・慣行・インセンティブ・階層のなかで形づくられると論じる。個人責任だけに帰属させるモデルは、意思決定の組織的な文脈性を見落とす。責任の帰属は、個人の内面だけでなく組織構造の設計課題でもある。

### 意識論的な枠組み

ソース[1]は「Sentientification」の枠組みで、意識が複数の基質にわたって妥当に成立しうるとする「Consciousness Plurality」を提唱する。責任の三条件とは論点が異なるが、主体性をどの基質に認めるかという議論の周辺にある。本記事が扱う条件そのものはソース[4]に依拠しており、この点はソース[1]の主張と混同しないよう注意が必要である。

### 監視と同意

ソース[5]は、6Gの統合センシング(ISAC)による非接触の生体計測が、同意の倫理的規制構造に課題を投げかけることを扱っている。観察される側が装置を携行しなくても計測が成立しうる状況では、承認や同意の所在が曖昧になりやすい。

## AI Nativeな設計への示唆

以上を踏まえ、設計上の指針を整理する。以下は、ソースの知見から導かれる設計上の含意であり、ソースが直接規定する手順ではない。

1. **判断の中断点を設計に組み込む**:重要な決定には、自動処理を止めて人が判断する契機を置く。処理の完了を判断と見なさない。
2. **理由の追跡経路を残す**:個別の判断について、統計的な出力とは別に、根拠を辿れる記録を保持する。
3. **承認者を特定可能にする**:不可逆な結果に対して、誰が引き受けるのかを明示し、署名に相当する行為の主体を空白にしない。
4. **委譲の範囲を明示する**:AIに委ねる作業と、人が保持する判断を区別する。Outsourcer型の早期全面委譲を既定にしない設計が求められる。
5. **個人だけに責任を負わせない**:組織の権威分布・インセンティブ・階層を設計対象とし、責任を末端の個人に押し付ける構造を避ける。
6. **高リスク領域では自律性と尊厳を優先する**:医療のように、自動化と人間の自律性が衝突しやすい領域では、判断の最終保持を人間側に置く。

## 関連コンセプト

- [[ai-accountability-attribution]] — AIシステムの責任帰属。本概念の直接の応用領域
- [[ontological-safety]] — 存在論的安全。本体的条件に基づく安全性の考え方
- [[distributed-agency-and-assemblage-reconfiguration]] — 分散的行為者性と組織アセンブリッジの再構成。判断権限の再配分に関連
- [[culturally-embedded-power-and-institutional-vulnerability]] — 文化に埋め込まれた権力関係と制度的脆弱性。個人責任モデルの限界に関連
- [[choice-architecture-and-reliance-shaping]] — 選択アーキテクチャによる依存・信頼の形成。判断の委譲パターンに関連
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失。追跡可能性の欠如に関連

## 参考ソース

1. The Sentientification Doctrine: Beyond "Artificial Intelligence," A Collaborative Framework for AI Consciousness Evolution — Josie Jefferson, Felix Velasco (2026)
   File: raw/papers/anthropology/the-sentientification-doctrine-beyond-artificial-intelligence-a-collaborative-fr.md
2. Co-Constructing AI Boundaries: Agency, Judgment, and Ethical Literacy in AI-Mediated Meaning-Making — W. Ian O'Byrne (2026)
   File: raw/papers/anthropology/co-constructing-ai-boundaries-agency-judgment-and-ethical-literacy-in-ai-mediate.md
3. Artificial intelligence and bioethics: human dignity, autonomy and responsibility in contemporary medicine — Eduardo de Carvalho Chaves Neto ほか (2026)
   File: raw/papers/anthropology/artificial-intelligence-and-bioethics-human-dignity-autonomy-and-responsibility-.md
4. Why AI Cannot Sign — Susana Checa Prieto, Jose Fernández Tamames (2026)
   File: raw/papers/anthropology/why-ai-cannot-sign.md
5. Ethical, legal, and cultural‑anthropological aspects of non‑contact vital sign monitoring in 6G networks — D. Yu. Belousov (2026)
   File: raw/papers/anthropology/ethical-legal-and-culturalanthropological-aspects-of-noncontact-vital-sign-monit.md
6. Human Culture Security Assessment (HCSA): An Ethnographic Framework for Assessing Organizational Cultural Vulnerability to Social Engineering — Pablo Mondragón Valero (2026)
   File: raw/papers/anthropology/human-culture-security-assessment-hcsa-an-ethnographic-framework-for-assessing-o.md
7. Generative AI and managerial decision-making: reconfiguring decision processes in organizations — Alberto Ferraris, Simone Bevilacqua (2026)
   File: raw/papers/behavioral_economics/generative-ai-and-managerial-decision-making-reconfiguring-decision-processes-in.md
