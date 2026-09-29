# 流暢な成果と内在的能力の乖離(支援の内在化阻害)

## 概要

流暢な成果と内在的能力の乖離(Fluent Output–Capability Decoupling under External Support)とは、外部支援(特にAIエージェント)の助けによって評価基準を満たす成果が出せる一方で、その成果が示すように見える認知的能力が本人の中に形成されていない状態を指す。Anderson と Zaza(2026)はこの状態を「fluent dependence(流暢な依存)」と呼び、人間とAIの相互作用における人間能力の妥当性(validity)の枠組みとして提案している[2]。

この概念がAI Nativeな設計で重要なのは、成果の質だけを見ていると能力の空洞化を検知できないためである。支援が「足場(scaffold)」として働くか「代替(substitute)」として働くかは設計次第であり、短期の依存低減と長期の技能維持は本来的に緊張関係にある[4][6]。成果指標と能力指標を分けて設計することが、AI時代の教育・職場・意思決定支援に共通する課題となる。

## メカニズム

以下は、支援の主体(人間・AI・組織・技術)を入れ替えても成り立つ構造的原理として整理したものである。

1. **成果の基準達成が支援に依存する**: 支援を受けた主体は評価基準を満たす出力を生成できる。出力は能力の証拠のように見えるが、実際には支援側の処理の結果である。
2. **負荷の移転とスキーマ形成の阻害**: 認知負荷理論に基づき、内在的負荷(intrinsic load)が人間から人工エージェントへ移ると、耐久的なスキーマ構築を生む germane processing(学習に資する処理)が起こらない可能性がある[2]。これは著者らが提案する「もっともらしい一つのメカニズム」であり、他の機序の可能性も認められている[2]。
3. **認知的オフロードの二重経路**: 会話型AIへのオフロードは、応答後の深い処理を促す「足場」経路と、浅い思考を置き換える「代替」経路に分岐するとされる[4]。同じ支援でも、利用後に主体が深く処理するかどうかで帰結が分かれる。
4. **短期と長期のトレードオフ**: 認知強制(cognitive forcing)や批判的関与を促すプロンプトなどの内省的戦略は、過度の依存を減らし意思決定の質を高める兆候が示されてきたが、主に単一セッション内の短期介入として評価されてきた[6]。長期にわたって人間の主体性と専門性が維持されるかは未解決である[6]。
5. **両面的効果**: 技術は判断バイアスを緩和すると同時に悪化させうる。雪崩安全のHCI分析では、両面的効果を持つ技術のパターンが報告されている[7]。

## 理論的背景

- **Fluent dependence の妥当性フレームワーク**: 高校数学、大学での科学的探究、知識労働者の意思決定、消費者のカテゴリ能力といった複数の文脈で、この状態と整合するパターンが実証的に記録されてきたが、断片的に議論されてきたと著者らは述べる[2]。認知負荷理論を用いて、これらを統合的に説明しようとする試みである。
- **二重経路モデル**: 会話型AIを「認知的足場」か「思考の代替」かという二つの経路で捉え、オフロード、応答後の深い処理、批判的思考の関係をモデル化している[4]。
- **スキル維持的な依存の未解決問題**: 支援システムとの相互作用では、短期的な依存低減と長期的なスキル維持が緊張関係にあり、両立には個人差、組織条件、内省的メカニズムの統合設計が必要とされる。短期の証拠と長期の主張の間にはギャップがある[6]。
- **教育領域の信頼性リスク**: 生成AIの教育利用に関する系統的レビュー(PRISMA 2020に従い、35件の実証研究を採択)は、ハルシネーション、誤情報、過度の依存、評価の妥当性への脅威を主題として扱っている[1]。成果に基づく評価が能力を正しく反映しなくなる点は、本概念と密接に関わる。
- **意思決定スタイルへの影響**: 生成AIが人間の判断に与える影響は、医療・経営ではアルゴリズム的精度による診断や運用の向上として現れる一方、領域により異なるパターンを示す。レビューは二重過程理論と自己決定理論に依拠している[3]。
- **努力を保存する設計**: SCAFFOLD は、外部検証、的を絞った修復、安全なフォールバックでLLM出力を包む層状の信頼性アーキテクチャであり、「学習には努力が必要」という学習科学の原則に基づいて生産的な努力を保つことを意図している。決定論的チェックと確率的チェックを区別し、任意のLLMに適用できる[5]。

## AI Nativeな設計への示唆

1. **成果と能力を別々に測る**: 出力が基準を満たすことを能力の証拠とみなさず、支援なしの能力や転移を評価する設計にする[2]。
2. **支援を「足場」に寄せる**: 回答を与えるだけでなく、応答後の深い処理(要約、検証、自分の言葉での再構成など)を促す相互作用を組み込む[4]。ここで挙げた具体例は、二重経路モデルの含意を踏まえた設計上の例示である。
3. **生産的な努力を残す**: 学習者が努力すべき部分を保存しつつ、安全性・信頼性は外部の検証層で担保する分業を採る[5]。
4. **長期の評価を前提にする**: 内省的介入の効果を単一セッションで判断せず、時間をかけた縦断的な評価を設計に含める[6]。
5. **個人差と組織条件を考慮する**: 同一の支援でも利用者や組織の条件により効果が異なるため、画一的な介入を避ける[6]。
6. **両面性を前提に設計する**: 技術は判断支援にも劣化要因にもなりうるため、緩和する効果と悪化させる効果の双方を分析する[7]。
7. **領域別に設計する**: 効果は領域により異なるため、教育・研究・医療・経営などで支援の位置づけを変える[3]。

## 関連コンセプト

- [[support-induced-skill-substitution-loop]] — 支援による代替が能力形成機会を奪うループ。本概念の動態的側面。
- [[fluency-persuasion-validity-decoupling]] — 流暢性と妥当性の分離。出力の見かけと内実の乖離という点で共通する。
- [[source-attribution-and-reliance-miscalibration]] — 信頼較正の歪みと過度の依存。
- [[threshold-phase-transition-in-technology-dependence]] — 技術依存の閾値・相転移。
- [[ai-in-educational-support-systems]] — 教育支援システムにおけるAI。
- [[ai-decision-support-in-education]] — 教育における意思決定支援AI。
- [[ai-decision-support-systems]] — AI意思決定支援システム。
- [[upstream-schema-ceiling-on-downstream-capability]] — 表現構造(スキーマ)が能力の上限を規定する点で関連。
- [[finite-attention-and-heterogeneous-agent-coupling]] — 有限な認知資源と異質主体間の結合設計。
- [[capability-profile-based-task-allocation]] — 能力プロファイルに基づく役割分担。

## 参考ソース

1. Reliability Risks of Generative AI in Education: A Systematic Review of Hallucinations, Misinformation, Overreliance, and Assessment Validity — İsmail Kaşarcı (2026)
   File: raw/papers/cognitive_science/reliability-risks-of-generative-ai-in-education-a-systematic-review-of-hallucina.md
2. Fluent Dependence: A Validity Framework for Human Capability in Human-AI Interaction — Jeffrey E. Anderson, Sam Zaza (2026)
   File: raw/papers/cognitive_science/fluent-dependence-a-validity-framework-for-human-capability-in-human-ai-interact.md
3. Heuristic or Algorithmic Thinking? Assessing Generative AI's Impact on Human Decision-Making. A Literature Review — Rafaél Caballero Fernández, María Solórzano (2026)
   File: raw/papers/cognitive_science/heuristic-or-algorithmic-thinking-assessing-generative-ais-impact-on-human-decis.md
4. Conversational AI as a Cognitive Scaffold or a Substitute for Thinking: A Dual-Path Model of Cognitive Offloading, Post- Response Deep Processing, and Critical Thinking — Yiding Bu, Zhentai zhang, ShuYi Wang, Yuxin Li (2026)
   File: raw/papers/cognitive_science/conversational-ai-as-a-cognitive-scaffold-or-a-substitute-for-thinking-a-dual-pa.md
5. Scaffolding students-AI dialogue for safe educational interactions — Olga Muss, Luca M. Leisten, Charles Edouard Bardyn (2026)
   File: raw/papers/cognitive_science/scaffolding-students-ai-dialogue-for-safe-educational-interactions.md
6. Open Questions Towards Skill-Sustaining Reliance in Reflective AI Engagement — Sander de Jong (2026)
   File: raw/papers/cognitive_science/open-questions-towards-skill-sustaining-reliance-in-reflective-ai-engagement.md
7. From Human Factors to Human-Technology Factors: An HCI Perspective on Technology in Avalanche Safety — Björn Hartmann, Jason Smith (2026)
   File: raw/papers/cognitive_science/from-human-factors-to-human-technology-factors-an-hci-perspective-on-technology-.md
