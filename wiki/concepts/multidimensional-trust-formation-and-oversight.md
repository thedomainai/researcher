# 多次元的な信頼形成と監督による自律性の媒介

## 概要

AIシステムに対する信頼は、単一の「信頼度」というスカラー量ではなく、複数の次元と経路を通じて形成される。ソース群が示す中心的な構図は次の三点である。

1. **二重経路の信頼形成**: 信頼は、情報の内容を吟味する認知的な経路と、安心感や好意といった感情的な経路の相互作用によって形成され、受容を左右する。
2. **透明性と監督による媒介**: アルゴリズムの透明性、人間参加型(human-in-the-loop)の監督、来歴(provenance)の提示は、信頼や心理的安全性を介して、人間の自律性に影響する。
3. **シグナル依存の脆弱性**: 信頼判断が特定の認知シグナルに依存するため、そのシグナルを模倣・悪用する欺瞞に対して構造的に脆弱になる。

AI Nativeな社会設計において重要なのは、信頼を「高めるべき指標」ではなく、「設計・監督・検証の対象となる媒介変数」として扱う視点である。信頼はAI導入の促進要因であると同時に、欺瞞の入り口にもなる。

## メカニズム

以下は、対象を人間、AI、組織、技術のいずれに入れ替えても成立する構造的原理として整理したものである。

### 1. 二重経路による信頼の形成

評価する主体は、二つの経路で対象への信頼を形成する。

- **認知経路**: 能力、正確性、透明性などの手がかりを、比較的論理的に処理する。
- **感情経路**: 共感、安心、好感などの情緒的な反応を通じて形成される。

受容(採用・委任・依存)は、両経路の相互作用の結果として決まる。片方だけを最適化しても、他方が阻害要因になりうる。

### 2. 媒介構造:統治の仕組み → 信頼 → 自律性

統治の仕組み(透明性、公平性の知覚、人間による監督)は、自律性に直接効くだけでなく、信頼や心理的安全性を媒介として効く。この構造は、判断主体が交代しても(従業員、患者、研究者、組織)成り立つ。信頼が媒介変数であるため、統治設計の効果は信頼の形成過程を通じて増幅もされれば、損なわれもする。

### 3. シグナル依存と欺瞞への脆弱性

信頼判断は限られた手がかり(シグナル)に基づく。手がかりが偽装可能である限り、判断者の知識量や情報量にかかわらず、欺瞞に対する構造的脆弱性が残る。信頼形成の「入力」が攻撃対象になる、という点が原理的な弱点である。

### 4. 来歴と検証可能性による補強

シグナルの真正性を裏づける層(来歴、文書化、責任の所在)を別に設けることで、信頼を「印象」から「保証(warrant)」へ引き上げられる。これは外部の監督や監査と同じ役割を果たす。

## 理論的背景

### 医療AI会話エージェントにおける多次元信頼と二重経路

Du らの研究 [1] は、AI医療会話エージェント(AIMCA)への信頼の多次元フレームワークを構築し、尺度を検証している。信頼と不信は技術普及を形作る二重の機構であり、信頼は採用を促し、不信は大規模展開を制約するとされる。医療分野では、信頼が依然として普及の持続的な障壁であるという問題意識が示されている。

Ouyang らの研究 [5] は、ヒューリスティック・システマティック・モデル(HSM)に基づき、ユーザーのAIシステム受容が認知経路と感情経路の相互作用で決まるという枠組みを提示している。ここから「二重経路」の原理が得られる。

### 統治と自律性の媒介

Patnaik らの研究 [2] は、AIを組み込んだ人事管理(HRM)を対象に、アルゴリズムの透明性、公平性の知覚、人間参加型監督が、AIへの信頼、心理的安全性、テクノストレスを通じて従業員の自律性に与える影響を検討している。社会的交換理論と資源保存理論に依拠し、インドの従業員290名の調査データを部分最小二乗法による構造方程式モデリングで分析している。中核的知見は、透明性と人間参加型監督が信頼と心理的安全性を媒介して自律性を高める、というものである。ただし、効果は制度形態に依存する可能性がある。

### 来歴と層状の保証

Huang の研究 [3] は、生成AIが人間の言語的痕跡から学ぶと同時に、書く・翻訳する・要約する・記憶するといった人間の営みの内部に入り込む、という二重の位置を評価する予備的枠組みを提案している。中心的提案は、成果物の性能、来歴、制度的権威などを分離して扱う「層状のwarrant profile」である。知識表現と信頼性の問題は、人間-AI協働に普遍的な構造的制約であるとされる。

### 欺瞞的シグナルへの脆弱性

Oggu の研究 [4] は、フィッシングの専門家コード化データを用いて、緊急性やなりすましなどの欺瞞的シグナルの分布を分析している。緊急性が最も一般的なシグナルであった一方、全体のシグナル構造は明確に分離したカテゴリを形成しなかった。また、単純なモデルでも、多様なフィッシング例とテンプレート化された例を比較的高い精度で区別できたことは、データセット由来のアーティファクトの存在を示す。信頼性の判定が特定の認知シグナルのパターンに依存するという点が、構造的脆弱性の根拠となる。

### 関連する周辺知見

- 研究におけるAI利用を扱った HAKI モデル [6] では、131名の教員への半構造化インタビューにより、効率化の一方で、アルゴリズムバイアス、学術的誠実性、透明性、学問的な声の喪失への懸念が示された。著者責任と学問的な声を守る倫理的枠組みの必要性が示唆される。
- KBOの自動ボール・ストライク判定(ABS)導入を利用した監査研究 [7] では、人間審判にカウント圧力に関連する文脈依存のバイアスがあり、ABSではその効果がほぼゼロで、偽発見率補正後に有意でなかったと報告されている。判定システムの文脈依存バイアスは、監査によって可視化すべき根本課題であることを示す。

## AI Nativeな設計への示唆

1. **信頼を単一指標にしない**: 認知的信頼(能力・正確性・説明の妥当性)と感情的信頼(安心・好感)を別々に測定し、設計する。感情面だけが先行する状況を早期に検出する。
2. **透明性と人間参加型監督を信頼の前提条件として組み込む**: 説明の提供や介入可能性は、自律性を守る媒介経路として設計する。ただし、効果は制度形態に依存しうるため、導入先の制度に合わせて調整する。
3. **来歴を標準装備にする**: 出力の由来、責任主体、検証履歴を層状に提示し、信頼を「印象」ではなく「保証」に基づかせる。
4. **欺瞞的シグナルを前提とした防御設計**: 緊急性やなりすましのような手がかりに頼る判断を、単独の根拠にさせない。シグナル以外の検証経路(独立した確認手段)を用意する。
5. **監査による継続的な検証**: 人間の判断にも自動化システムにも文脈依存バイアスが生じうるため、比較可能な基準を用いた監査を組み込む。
6. **責任と自律性の保全**: 研究・業務でAIを使う際も、著者責任や個人の判断の声が失われないよう、役割と責任の線引きを明示する。

## 関連コンセプト

- [[human-ai-trust]] — AIへの信頼の基本構造
- [[human-ai-interaction-and-trust]] — 人間とAIの相互作用と信頼
- [[human-ai-trust-complementarity]] — 信頼と相補性
- [[human-like-vs-system-like-trust]] — 人間的信頼とシステム的信頼の対比
- [[ai-ethics-trust-transparency]] — 倫理・信頼・透明性
- [[human-oversight-mechanisms]] — 人間による監視メカニズム
- [[machine-speed-oversight-asymmetry]] — 監督が機械速度に追いつかない問題
- [[technostress-and-user-innovation-dual-effects]] — 信頼とテクノストレスの二面性
- [[fluency-induced-trust-miscalibration]] — 流暢性による信頼キャリブレーションの歪み
- [[reliance-calibration-between-aversion-and-overtrust]] — 回避と過信の間の依存度調整
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼喪失
- [[pluralistic-legitimacy-and-trust-signaling]] — 信頼シグナリングの構造
- [[ai-disclosure-and-organizational-trust]] — AI関与開示と組織の信頼

## 参考ソース

1. Hemin Du, Wumin Ouyang, Y X Han, Yuyu He, Guanning Wang (2026). "Multidimensional trust perceptions of AI medical conversational agents: framework development and scale validation". File: `raw/papers/cognitive_science/multidimensional-trust-perceptions-of-ai-medical-conversational-agents-framework.md`
2. Tamrisha Patnaik, Robert Ipiin Gnankob, Nitya Sundar Nanda (2026). "Governing algorithms, empowering people: how ethical AI oversight shapes trust, technostress, and employee autonomy in AI-enabled HRM". File: `raw/papers/cognitive_science/governing-algorithms-empowering-people-how-ethical-ai-oversight-shapes-trust-tec.md`
3. Wanhong Huang (2026). "Generative AI and Linguistic Mediation: Relational Knowledge, Expression Dynamics, and Provenance". File: `raw/papers/cognitive_science/generative-ai-and-linguistic-mediation-relational-knowledge-expression-dynamics-.md`
4. Sujay Oggu (2026). "Human Cognition, Deceptive Cues, and AI: A Computational Study of Phishing Decision Signals". File: `raw/papers/cognitive_science/human-cognition-deceptive-cues-and-ai-a-computational-study-of-phishing-decision.md`
5. Wumin Ouyang, Y X Han, Hemin Du, Zihuan Wang, Yuyu He (2026). "Understanding user acceptance of AI medical conversational agents through dual-path trust mechanisms: An empirical study based on the HSM model". File: `raw/papers/cognitive_science/understanding-user-acceptance-of-ai-medical-conversational-agents-through-dual-p.md`
6. Amin Shahini (2026). "Developing the HAKI model as a conceptual framework for AI-assisted academic research". File: `raw/papers/cognitive_science/developing-the-haki-model-as-a-conceptual-framework-for-ai-assisted-academic-res.md`
7. Kichang Lee, JeongGil Ko (2026). "Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition". File: `raw/papers/cognitive_science/auditing-contextual-bias-in-human-ball-strike-calls-using-kbos-automated-umpirin.md`
