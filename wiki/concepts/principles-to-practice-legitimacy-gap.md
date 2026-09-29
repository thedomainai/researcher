# 原則から実践への翻訳ギャップと正当性の維持

## 概要

AIガバナンスでは、公平性・透明性・説明責任・プライバシー・説明可能性・信頼性といった倫理原則を列挙することが、政策の出発点として広く採られている。この「原則から実践への翻訳ギャップと正当性の維持」という概念は、次の二つの問いを扱う。

1. **原則の列挙は何をしているのか**。列挙は中立的な整理に見えるが、政治的選択や権力配分の問題を「中立的原則」の陰に隠す働きを持ちうる。
2. **規範の正当性は何によって保たれるのか**。論理的な基礎づけだけでなく、合意・儀式・象徴、そして段階的な実装によって維持・再生産される。

AI Nativeな社会設計では、原則を上位方針として掲げるだけでは現場の行動は変わらない。また、論理的に整合したルールを実装するだけでは規範の権威は成立しない。設計者は、原則が何を隠しているのかを自覚し、階層間の翻訳を設計対象にし、正当性を支える社会的基盤を意識的に扱う必要がある。これが、本概念を不変原理(Tier 1)として位置づける理由である。

## メカニズム

以下の構造は、対象が人間・AI・組織・技術のいずれであっても成立する。

### 1. 政治性の中立化(原則による隠蔽)
価値判断を含む選択が、「公平性」「信頼性」といった誰もが賛同しうる語彙で表現されると、誰の利益をどう配分するかという構造的な問いが見えにくくなる。列挙された原則は、対象となる技術を「所与の人工物」「不可避なもの」として扱う前提を伴いやすく、その前提自体への問いを後景に退かせる。

### 2. 階層間の翻訳損失
グローバルな枠組みや標準、国内の方針、組織の責任、個人の利用行動という各階層の間で、原則は解釈・具体化される。その過程で意味が失われたり、意図しない逸脱が生じたりする。上位方針と現場行動の乖離は、個人の怠慢ではなく、階層構造に由来する組織設計上の問題として捉えられる。

### 3. 象徴・儀式による正当性の再生産
規範への服従は、論理的な基礎づけだけでは説明できない。継承された儀式・象徴・制度的形式が「正当性の文法」を提供し、規範の権威感覚を維持している。この文法は、元となる根拠が薄れた後も存続する。

### 4. 段階的実装による橋渡し
抽象原則と具体的実践の間には、中間的な段階が必要になる。原則を具体的な役割分担・検証手順・利用範囲の限定として組み込むことで、はじめて原則が運用可能になる。

## 理論的背景

### 原則ベースのガバナンスへの批判的読解
Priyadarshi and Kumarは、インドのAIガバナンス論議(2025年11月にMeITYが公表したガイドラインを含む)を対象に、倫理原則の列挙が、技術を所与の人工物・パラダイム的必然として理解したうえで悪影響を緩和するための「簡便な手段」として中心に置かれていることを論じている。国家は、革新とリスクという競合する主張を均衡させる「倫理的調停者」として位置づけられる。この読解に基づくと、原則の列挙は政治的選択を中立に見せ、構造的権力配分の問題を曖昧にする社会的メカニズムとして機能する。

### 政策と利用者のギャップ
星野の枠組みは、グローバルなガバナンス枠組み・標準と、組織、フリーランス/委託関係、個々の利用者が負う実務上の責任とを接続し直すものである。ここでは「Policy–User Gap」と、意図しないガバナンス逸脱のリスクが強調され、翻訳ギャップが階層間の組織設計問題として提示されている。

### 借り物の神聖性(borrowed sanctity)
Oliveiraは、現代法が、かつて宗教的権威に属した儀式・象徴・制度的形式という「借り物の神聖性」に依拠し続けていると論じる。法廷、司法儀礼、憲法、法的伝統、さらに新たに登場するAIシステムまでもが、神学的基盤が薄れた後も存続する正当性の文法を保っているという。これは、規範体系の正当性が論理的基礎のみでは維持されないことを示唆し、純粋に論理的なルール実装の限界を浮かび上がらせる。

### 原則を実装する段階的事例
Courtney and Mulveyは、博士課程教育の枠組み(DSDF-E)の設計を事例に、透明性・説明責任・人間による監督・検証・文脈化・限定的利用といった原則が、プログラムレベルの設計作業でどう具体化されうるかを示した。生成AIは整理・比較・冗長性の確認・用語の洗練・文章の修正を支援し、価値・内容・組織への適合・学術的根拠・最終判断は教員が保持した。AI倫理を抽象原則として扱うのではなく、設計実践に組み込む一例である。ただし、この種の段階的手順の実現可能性と限界に関する理論的根拠は、なお曖昧であると評価されている。

### 周辺的な知見
- 求職者の公平性に関する懸念を扱った研究(He et al.)は、研究上の理想化された公平性概念と、当事者が実際に表明する懸念との間にギャップがあることを出発点としている。
- Freireの批判的教育学に関するシステマティックレビューは、生成AIの教育への統合が教育学的枠組みや制度的方針の整備を追い越していることを問題にしている。
- 組織エスノグラフィーと実践理論に関する特集の編集序文は、デジタル・AI技術によって労働実践の物質的配置・時間的リズム・調整様式が変化するなかで、実践がどのように安定し変化するのかという問いに焦点を当てている。
- Human-AI関係のシステマティックレビューは、エンジニアリング・倫理・政策の交差領域を扱う。

## AI Nativeな設計への示唆

1. **原則リストを設計の終点にしない**。原則を列挙する際は、その背後にある選択(誰が、何を、どの前提で決めたか)を併記し、技術を所与とみなす前提を問い直せるようにする。
2. **階層間の翻訳を明示的な設計対象にする**。グローバル標準、組織方針、個別業務、個人の利用行動の各層で、責任の所在と解釈の手順を定義し、意図しない逸脱を検知できるようにする。
3. **段階的な実装経路を用意する**。原則から実践までを、限定的利用・人間による最終判断・検証・文脈化といった中間ステップに分解する。ただし、その手順の有効範囲は自明ではないため、限界を前提として運用する。
4. **正当性を論理だけに委ねない**。規範の権威は合意、儀式、象徴、制度的形式によって支えられる。AIが関与する意思決定でも、手続の可視化や合意形成の場を設計に含める。
5. **当事者の懸念を起点にする**。研究者が想定する理想的概念だけでなく、利用者・当事者が実際に表明する懸念から要件を導く。
6. **人間の責任領域を明確にする**。AIが作業を支援する場合でも、価値判断、文脈への適合、最終決定といった領域は人間側に保持させる。

## 関連コンセプト

- [[organizational-ethical-translation]] — 倫理原則を組織の実践へ変換する過程そのものを扱う
- [[global-ai-governance-legitimacy]] — グローバルなAIガバナンスの正当性の問題
- [[pluralistic-legitimacy-and-trust-signaling]] — 多元的な正当性と信頼シグナル
- [[institutional-legitimacy-in-ai-enforcement]] — AI取締りにおける制度的正当性
- [[temporal-erosion-of-procedural-legitimacy-under-opacity]] — 不透明性下で手続的正当性が時間とともに侵食される構造
- [[verification-to-authority-conversion-gap]] — 検証可能性が実効的権威に変換される際のギャップ
- [[upstream-representation-integrity-failure]] — 上流の表現が下流の統治を規定する構造
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[laws-and-ethical-principles]] — 法・倫理原則の適用に関する具体例

## 参考ソース

1. Priyadarshi, P., Kumar, M. (2026). *Principles over Politics? A Critical Reading of India AI Governance Framework*.
   File: raw/papers/ai_governance/principles-over-politics-a-critical-reading-of-india-ai-governance-framework.md
2. Courtney, S. A., Mulvey, B. K. (2026). *From AI ethics principles to academic design practice: a faculty-led generative AI case in doctoral education*.
   File: raw/papers/ai_governance/from-ai-ethics-principles-to-academic-design-practice-a-faculty-led-generative-a.md
3. 星野 誠樹 (2026). *AI Governance Framework for Bridging the Policy–User Gap*.
   File: raw/papers/ai_governance/ai-governance-framework-for-bridging-the-policyuser-gap.md
4. Oliveira, N. S. (2026). *The Final Foundation of Law: Religion, Morality or Human Agreement?*
   File: raw/papers/anthropology/the-final-foundation-of-law-religion-morality-or-human-agreement.md
5. Sabar, F. C., Taneo, R. F. S., Alemoka, C. K., Yohanes, A., Walalayo, D. Y. (2026). *Freirean Pedagogy for Equitable Assessment, Decolonial Governance, and Cognitive Wellbeing in the Age of Artificial Intelligence: A Systematic Review*.
   File: raw/papers/ai_governance/freirean-pedagogy-for-equitable-assessment-decolonial-governance-and-cognitive-w.md
6. Wang, Z. A., Hari, S., Dembele, T., Intahchomphoo, C. (2026). *Human-AI Relationships at the Intersection of Engineering, Ethics, and Policy: A Systematic Review*.
   File: raw/papers/ai_governance/human-ai-relationships-at-the-intersection-of-engineering-ethics-and-policy-a-sy.md
7. He, C., Deng, Y., Fabris, A., Li, B., Biega, A. J. (2026). *Value Sensitive Design for Fair Online Recruitment: A Conceptual Framework Informed by Job seekers' Fairness Concerns*.
   File: raw/papers/ai_governance/value-sensitive-design-for-fair-online-recruitment-a-conceptual-framework-inform.md
8. Schönian, K., Ayeh, D. (2026). *Guest editorial: Organizational ethnography and practice theories in the digital transformation of work*.
   File: raw/papers/anthropology/guest-editorial-organizational-ethnography-and-practice-theories-in-the-digital-.md
