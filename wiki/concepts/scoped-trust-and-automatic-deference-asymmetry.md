# 機能限定的な信頼と権威への自動的追従の非対称性

## 概要

信頼は本来、特定の機能・タスクごとに限定して付与されるべきものである。しかし人間は、権威的に見えるソース(専門家、組織、AIなど)から提示された情報に対し、その領域の適格性を問わず自動的に信頼を付与しやすい。さらに信頼の機能特異性は、標準的な計測手法では捉えにくい。この「限定されるべき信頼」と「領域を越えて流れる信頼」のずれが、この概念の中心にある。

加えて、情報を持つ側と持たない側の非対称性があると、同じ仕組みが「支援」とも「管理」とも解釈され、両者が対立する。

AI Nativeな社会設計では、AIエージェントが意思決定や助言に深く入り込む。そのため、次の三点が設計上の前提になる。

- 信頼は機能単位で設計・表現・計測する。
- 権威への自動追従は人間の不変な認知制約として織り込む。
- 情報の非対称性が生む解釈の対立を、構造的に扱う。

## メカニズム

この構造は、対象を人間、AI、組織、技術のいずれに置き換えても成立する。

1. **信頼の機能特異性**:信頼の対象は、システム全体ではなく特定の機能や能力である。信頼する側は「何についてなら任せられるか」を暗黙に区別している。
2. **自動的信頼付与(権威バイアス)**:権威的と知覚されたソースには、機能の境界を越えて信頼が波及する。ソースの適格性が及ぶ範囲と、実際に付与される信頼の範囲が一致しない。
3. **計測不能性**:信頼を「システム」という単一の対象への評価として測ると、どの機能への信頼なのかが見えなくなる。そのため誤った過信や過小利用を検出できない。
4. **情報の非対称性**:一方だけが情報の収集・利用の実態を知っている場合、同一の仕組みが受け手には支援にも監視にも見える。信頼はこの解釈の対立を仲介する変数として働く。
5. **導入と信頼形成のずれ**:技術の導入が進んでも、信頼形成やスキルの側が追いつかず、それが運用上のボトルネックや存在制約になる。

## 理論的背景

**信頼の機能特異性と計測の限界(ソース4)**
自動化への信頼研究では1990年代半ばから、信頼がシステム全体ではなく個々の機能に付随しうることが認識されてきた。Lee and See (2004) も、誤用と不使用を防ぐためにこの機能特異性を最大化することを推奨している。しかし広く使われる自己報告式の信頼尺度は「そのシステム」を単一の対象として評価させる。検討された尺度のなかに、回答者が評価の対象となるタスクや能力を明示できる項目はなかった。同研究は、17のAI関連サブレディットの約1,250万件のコーパスから2万件を抽出して自然発話を分析し、実際の信頼の語りと尺度設計の乖離を調べている。ここで扱われているのは、その第1フェーズである。

**権威的ソースへの自動的追従(ソース2)**
法学生360名、2,880件の事例観測からなる実験データセットは、誤りを含む生成AIの法的助言に触れたときの推論、誤り検出、AIへの依存、意思決定を扱っている。対象は自動化バイアスであり、権威的ソースからの情報に人間が領域専門性にかかわらず信頼を付与する傾向を示す事例として位置づけられる。本記事ではこれを不変の認知制約として扱う。ただし、抜粋から具体的な効果量までは読み取れない。

**情報非対称性と支援・管理のパラドックス(ソース3)**
AIによる従業員ストレス管理(感情分析、表情分析、ウェアラブル、チャットボットなど)は、支援の機会を広げる一方で、監視も可能にする。この概念論文は2015〜2026年の知見を統合し、「プライバシーと支援のパラドックス」を論じている。支援的と知覚された技術が、監視の侵襲性の知覚によって支援性を失うという構図である。知覚された監視、説明可能性、信頼などが関与する要因として挙げられている。

**協働における信頼とスキルギャップ(ソース1)**
エージェント型AIの意思決定への導入は、統治構造、スキル、信頼のメカニズムの整備を追い越している。HACDGモデルは、人間とAIの協働的意思決定を統治する枠組みとして提案されており、信頼とスキルギャップは常に存在制約として働くとされる。

**組織導入における信頼形成の非対称性(ソース5)**
理科教師へのインタビューでは、GenAIへの確信度が使用場面によって異なった。授業計画を個人で行うときのほうが、生徒に直接使うときより安心して使えたと報告されている。信頼が用途や文脈ごとに分かれることを示唆する。

**権威の再編(ソース6)**
デジタル宗教研究は、プラットフォームのアフォーダンスとアルゴリズムによる可視性が、宗教的権威の多元化を拡張しつつ制約するとみる。権威が技術的媒介によって形成・制約される点で、権威への追従を扱う際の補助的な視点になる。

## AI Nativeな設計への示唆

1. **機能スコープを明示する**:AIの提示に「何についての能力・確からしさか」を付ける。信頼の付与範囲をUI上で機能ごとに区切る。
2. **信頼の計測を機能単位にする**:単一の信頼スコアに頼らず、タスクや能力を回答者が指定できる評価設計にする。
3. **権威の波及を前提に安全側へ倒す**:人間が自動的に追従することを前提に、誤りの検出を促す摩擦(確認ステップ、反証の提示)を設ける。これは、誤りを含むAI出力に対する検出力を保つための設計原則である。
4. **情報の非対称性を縮める**:何を収集し、何のために使い、誰が見るのかを開示し、説明可能性を確保する。支援と管理の解釈の対立は、この開示の設計で緩和される。
5. **統治とスキルを導入速度に合わせる**:導入が先行しないよう、統治構造、スキル育成、信頼形成の仕組みを同時に整える。
6. **場面ごとの安心感の差を扱う**:私的利用と対人利用では確信度が異なりうる。段階的な導入を検討する。

## 関連コンセプト

- [[human-ai-trust]] — AIへの信頼の基本的な位置づけ
- [[human-ai-interaction-and-trust]] — 人間とAIの相互作用と信頼
- [[human-ai-trust-complementarity]] — 信頼と相補性
- [[human-like-vs-system-like-trust]] — 人間的信頼とシステム的信頼の対比
- [[capability-perception-and-responsibility-diffusion-in-trust]] — 能力知覚と責任転嫁
- [[fluency-induced-trust-miscalibration]] — 流暢性による信頼の歪み
- [[verification-cost-and-trust-testing-of-automated-advisors]] — 自動助言の検証コスト
- [[complementary-information-and-epistemic-asymmetry]] — 認識論的非対称性
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入速度と統治能力のギャップ
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離
- [[ai-ethics-trust-transparency]] — 倫理・信頼・透明性
- [[llm-alignment-trust-sycophancy]] — 迎合性と信頼

## 参考ソース

1. Agentic Artificial Intelligence in Business Decision-Making: A Framework for Human–AI Collaborative Governance and Strategic Value Creation — P V. Amutha, M. Bhuvaneswari (2026)
   `raw/papers/psychology/agentic-artificial-intelligence-in-business-decision-making-a-framework-for-huma.md`
2. Automation Bias and Legal Reasoning in Law Students: Experimental Dataset on Generative AI Errors — Miluska Rodriguez-Saavedra (2026)
   `raw/papers/psychology/automation-bias-and-legal-reasoning-in-law-students-experimental-dataset-on-gene.md`
3. The Privacy–Support Paradox of AI-Based Employee Stress Management: The Role of Perceived Surveillance, Explainability, Trust, and Employee — Sneha Gupta, Utkarsh Singh Parihar, Shweta Chauhan (2026)
   `raw/papers/psychology/the-privacysupport-paradox-of-ai-based-employee-stress-management-the-role-of-pe.md`
4. Trust Talk Is Scoped and Unlexicalized: How People Express Trust in AI, and What Standard Instruments Cannot See — Muhammad Ali Shahidy, Usha Lakshmanan (2026)
   `raw/papers/psychology/trust-talk-is-scoped-and-unlexicalized-how-people-express-trust-in-ai-and-what-s.md`
5. Investigating science teachers' experiences of generative AI in science teaching and learning from a GenAI-TPACK perspective — Xiang Zhang, Michael Reiß (2026)
   `raw/papers/psychology/investigating-science-teachers-experiences-of-generative-ai-in-science-teaching-.md`
6. Digital religion and hybrid religious authority in algorithmically mediated environments — Aruzhan Akhmetova ほか (2026)
   `raw/papers/religious_studies/digital-religion-and-hybrid-religious-authority-in-algorithmically-mediated-envi.md`
