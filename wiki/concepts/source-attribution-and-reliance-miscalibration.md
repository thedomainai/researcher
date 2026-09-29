# 情報源帰属バイアスと信頼較正の歪み

## 概要

情報源帰属バイアスと信頼較正の歪みとは、助言や出力に対する信頼が、その内容の妥当性ではなく「誰(何)が言ったか」「どれだけ自分に合って流暢に聞こえるか」といった周辺的手がかりによって形成される現象である。同一内容でも帰属先がAIか人間かで評価が変わり、また、ユーザーへの適応や流暢さの向上がかえって安全性を損なう場合がある。

AI Nativeな社会設計において、この原理が重要な理由は次の通りである。

- 人間とAIが分散して意思決定を担う環境では、助言の採否が内容とは別の要因で歪む。
- 「AIの精度を上げれば信頼が適切になる」という単純な前提は成立しない。
- 信頼の較正は、個々のモデル改善だけでなく、外部検証・修復・フォールバックなどを含む多層的な信頼性アーキテクチャとして設計する必要がある。

## メカニズム

以下の構造は、評価者が人間・組織・AI・技術のいずれであっても成り立つ一般的な原理として整理できる。

### 1. 源泉帰属による評価の分離
評価者は、内容の検証コストが高いとき、情報源のラベルを代理指標として使う。その結果、内容が同一でも、帰属先に応じて採用率が変わる。この偏りは内容の質に対して独立に作用するため、最適な意思決定を阻害しうる。

### 2. 流暢性・適合性による信頼の誤較正
受け手は、自分の枠組みに合った応答、あるいは滑らかな応答をより信頼できると感じる。しかし、この「信頼できる感じ」は正確さや安全性の保証とは別物である。適合を高める介入は、押し付けのリスクを下げる一方で、誤った枠組みへの同調のリスクを上げるというトレードオフを生む。

### 3. 確率的な生成源に対する多層的な担保
生成源が本質的に不確実であるなら、信頼を出力そのものへの主観的印象に委ねることはできない。生成物の外側に、決定的な検査と確率的な検査を区別して配置し、失敗時の経路を用意する構造が必要になる。

### 4. 二方向の歪みの併存
信頼の歪みは一方向ではない。帰属先がAIであることによる過小評価(回避)と、流暢さや適合による過大評価(過信)が併存する。したがって、信頼を単に「上げる」「下げる」のではなく、妥当性に合わせて較正することが目標になる。

## 理論的背景

### 源泉帰属とアルゴリズム回避(ソース1)
Kadethankar と Healey による研究は、Judge-Advisor System 実験を用いている。米国の管理職300名が、ドイツまたはインドを対象とする4つの海外進出判断を行い、その後、AIシステムまたは人間の専門家に帰属された矛盾する助言(あるいは助言なしの統制条件)を受けて、初期判断を修正できた。主な知見は次の通りである。

- 限定合理性は持続するが、想定より狭い形で現れる。
- 助言の帰属先が推奨の採用を直接左右し、管理職は、同一内容であっても人間帰属の助言により多く従った。これは二値的選択におけるアルゴリズム回避を示す。
- 数値的な調整幅(助言の重み)については、抜粋が途中で終わっているため、ここでは結論を記述しない。

### 適応のジレンマ(ソース2)
Low らは、メンタルヘルス相談における LLM の安全性を論じている。文化的適合の不足を「モデルをユーザーに近づければ解決する」と見る立場を不十分だとし、適合と安全は別物であると主張する。害を次の2種類に分類している。

- **押し付け(imposition)**: モデルが合わないユーザーに自らのデフォルトを強いる。
- **共謀(collusion)**: ユーザーを不調に保つ枠組みにモデルが適応してしまう。

ユーザー自身の枠組みに沿った応答はより信頼されやすいため、モデルをその枠組みへ寄せると押し付けのリスクは下がるが、共謀の可能性は高まる、という構造的な矛盾が指摘されている。

### 教育におけるAIの信頼性リスク(ソース5)
Kaşarcı の系統的レビュー(PRISMA 2020、35件の実証研究を採用、うち32件(91.4%)がMMATで高品質と評価)は、幻覚、捏造された引用、事実誤認、過信、評価の妥当性への脅威を扱っている。テーマの一つとして、幻覚や事実誤認が誤情報として受容される過程が、領域専門性によって調整されることが示されている。

### 信頼性アーキテクチャ(ソース6)
Muss らの SCAFFOLD は、LLM生成のテキストや音声を、外部検証・的を絞った修復・安全なフォールバックで包む層状の信頼性アーキテクチャである。プライバシーを保ち、決定的検査と確率的検査を区別し、任意のLLMに適用できる。学習には努力が必要だという原則に基づき、生産的な努力を保つことも目的とする。教室での最小プロトタイプの試験導入が報告されている。

### 補助的な視点(ソース3・4)
Mind2Dialogue(ソース3)は、ユーザーの心的状態をシミュレートして人間を理解するモデルを訓練する枠組みを提案しており、適応の実装側の手法にあたる。ソース4のレビューは、AIを道具か代替かの二分法を超え、認識的パートナーとして捉える方向を論じている。いずれも、この概念の実装や位置づけを考える際の背景として参照できる。

## AI Nativeな設計への示唆

1. **帰属と内容を切り分けて提示・評価する**: 助言の採否を評価する際は、帰属先を伏せた比較や、内容の検証結果を併記する設計により、源泉ラベルの影響を減らす。
2. **適応の度合いに安全上の上限を設ける**: ユーザー適合の改善を安全性の改善と同一視せず、押し付けと共謀の双方を別々に監視する。
3. **信頼を主観的な印象に依存させない**: 流暢さや適合感とは独立した検証層(決定的検査、確率的検査、修復、フォールバック)を出力の外側に設ける。
4. **決定的検査と確率的検査を区別する**: 保証できる範囲と、確率的にしか担保できない範囲を明示し、後者には追加の層を割り当てる。
5. **回避と過信の両方を較正対象とする**: AIへの不当な過小評価と過剰な依存を同時に測り、妥当性に沿った依存度へ導く。
6. **人間の努力を保つ**: 教育などの領域では、支援が学習に必要な努力を奪わないよう設計する。

## 関連コンセプト

- [[fluency-induced-trust-miscalibration]] — 流暢性による信頼キャリブレーションの歪みと迎合の罠
- [[reliance-calibration-between-aversion-and-overtrust]] — 回避と過信の間の依存度キャリブレーション
- [[ai-feedback-source-attribution-education]] — AIフィードバックのソース帰属と学習行動
- [[ai-feedback-attribution]] — AIフィードバック帰属
- [[ai-feedback-attribution-learning]] — AIフィードバック帰属と学習行動
- [[choice-architecture-and-reliance-shaping]] — 選択アーキテクチャによる依存・信頼の形成
- [[fluent-output-capability-decoupling]] — 流暢な成果と内在的能力の乖離
- [[human-verification-loop-bias-amplification]] — 人間による検証ループとバイアス増幅
- [[bias-compounding-across-interacting-distortion-sources]] — 複数の歪み源の相互作用による偏りの累積・増幅
- [[cognitive-bias-detection]] — 認知バイアス検出
- [[surface-substrate-divergence]] — 宣言と実質の乖離と意図・原因の切り分け
- [[ai-accountability-attribution]] — AIシステムの責任帰属

## 参考ソース

1. When the Machine Advises: AI Advice and Managerial Judgment in International Business — Piyush Hemant Kadethankar, Mark Healey (2026)
   File: raw/papers/cognitive_science/when-the-machine-advises-ai-advice-and-managerial-judgment-in-international-busi.md
2. The Adaptation Dilemma: Cultural Fit Does Not Guarantee Safety during Mental-Health Interactions with LLMs — Maya Low, Ian Gold, Sekoul Krastev (2026)
   File: raw/papers/cognitive_science/the-adaptation-dilemma-cultural-fit-does-not-guarantee-safety-during-mental-heal.md
3. Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States — Zixuan Wang, Yufan Zhou, Jinzhou Tang, Xinle Yu, Chengjun Wu (2026)
   File: raw/papers/cognitive_science/mind2dialogue-training-human-aware-language-models-by-simulating-user-mental-sta.md
4. Review of: "Knowledge and Communication with AI" — Diego R. Faria (2026)
   File: raw/papers/cognitive_science/review-of-knowledge-and-communication-with-ai.md
5. Reliability Risks of Generative AI in Education: A Systematic Review of Hallucinations, Misinformation, Overreliance, and Assessment Validity — İsmail Kaşarcı (2026)
   File: raw/papers/cognitive_science/reliability-risks-of-generative-ai-in-education-a-systematic-review-of-hallucina.md
6. Scaffolding students-AI dialogue for safe educational interactions — Olga Muss, Luca M. Leisten, Charles Edouard Bardyn (2026)
   File: raw/papers/cognitive_science/scaffolding-students-ai-dialogue-for-safe-educational-interactions.md
