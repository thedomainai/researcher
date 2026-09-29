# デフォルト依存と信頼・行動の乖離

## 概要

デフォルト依存と信頼・行動の乖離とは、利用者が自動化やAIの推奨に従うかどうか(順守・依存)が、本人の主観的な信頼によってではなく、累積的に提示されるデフォルト、インターフェースの設計、リスクが顕在化しているかという文脈によって非対称に形づくられる、という原理である。その結果、アンケート等で得られる自己申告の信頼指標は、実際の行動を十分に予測できない。

AI Nativeな設計にとって重要なのは、「利用者は信頼しているから使う」という前提が設計・評価の両面で成り立たない点にある。信頼スコアを最適化しても行動は変わらない可能性があり、逆に信頼していなくてもデフォルトの積み重ねで従ってしまう可能性がある。したがって設計者は、信頼の醸成よりも、デフォルト・提示方法・リスク文脈という行動の実際の決定要因に目を向ける必要がある。

## メカニズム

この原理は、人間・AI・組織・技術のいずれを主体に置き換えても成立する構造として、次の3点に整理できる。

1. **デフォルト効果の累積**: 意思決定者は、繰り返し提示される既定の選択肢を受け入れる方向に傾く。単発の提示では小さな偏りでも、提示が累積すると順守が強化される。
2. **認知的相互作用による順守の非対称化**: 順守は「推奨に従う」方向と「推奨に逆らう」方向で対称ではない。インターフェースの提示タイミング・顕著性・不確実性のフレーミングなどが認知に作用し、一方向に偏った順守を生む。
3. **リスク顕在性による信頼と行動の結合変化**: 信頼が行動を予測すると想定される関係は、リスクが存在する文脈で初めて成立し得るとされる。リスクのない状況では信頼と行動の結びつきが実態を映さず、リスクの有無によって信頼と依存の結合の強さが変わる。

共通する構造は、「内的状態(信頼)から行動が生じる」のではなく、「環境側の構造(デフォルト、提示、リスク)が行動を規定し、内的状態は必ずしもそれを反映しない」という点である。

## 理論的背景

**累積的デフォルト推奨と非対称な順守(ソース1)**: Liu、Zhou、Zhiによる2026年の研究は、人間と自動化の意思決定において、累積的なデフォルト推奨が利用者の順守を非対称に形成する認知メカニズムを扱っている。本記事では、この研究の中核的知見として上記の非対称性を位置づけている(ソースの提示範囲では抄録の詳細は確認できていない)。

**リスクのない研究設計の盲点(ソース2)**: Rieger、Hoesterey、Onnaschは、理論家も実務家も「信頼という潜在構成概念が行動を因果的に予測する」と仮定していると指摘する。すなわち、システムの特性(信頼性など)が信頼を形づくり、信頼が依存の程度を予測するという想定である。しかしこの主張を支持する証拠は乏しく、特にリスク下では少ないという。研究チームは、VRでリスクを環境の一部として没入的に操作する2つの実験を行い、実験1ではシステムの信頼性(低/高)とリスク(なし/あり)を被験者間で操作し、複数の信頼指標が信頼性の依存への効果を媒介するかを検証した。論題は、リスクのない研究設計では信頼と行動の弱い結びつきを見逃すことを示している。

**認知とインターフェースが効果を左右する(ソース3)**: 放射線診断におけるヒューマンAI協働の物語的統合レビューは、AIの臨床的価値を決めるのはアルゴリズム単体の性能よりも人間とAIの相互作用であるとする。未認識の決定要因として、(1)自動化バイアス、AI不確実性のフレーミング、AIによるスキル低下が診断的推論を歪める認知心理、(2)AI所見の提示タイミング・顕著性・記録が読影者の注意と報告行動を形づくるUI/UX、(3)読影者が自らの判断を覆してしまうアルゴリズム的同調、が挙げられている。

**関連する周辺知見(ソース4)**: 月面着陸機の監督制御に関する研究は、自動化のレベル、人間監視の形態、責任配分が相互作用し、単純な権限委譲では本質的な課題が解決されないことを示唆する。デフォルトや提示が行動を形づくる構造を、制御設計の側面から補強する知見である。

## AI Nativeな設計への示唆

- **信頼スコアを行動の代理指標にしない**: 自己申告の信頼だけで依存の適切さを評価せず、実際の順守・介入・上書きなどの行動指標を計測する。
- **リスクを含む文脈で評価する**: リスクのない実験やパイロットは信頼と行動の結びつきを見誤る。評価環境にはリスクの顕在性を取り入れる。
- **デフォルトを設計対象として扱う**: 推奨の初期値や繰り返しの提示は順守を累積的に強める。デフォルトの設定・提示頻度・変更の容易さを明示的な設計判断とし、順守の偏りを継続的に監視する。
- **提示の顕著性・タイミング・不確実性の表現を調整する**: UI/UXは注意と行動を規定する。AIの出力を提示する順序や不確実性のフレーミングを、自動化バイアスやアルゴリズム的同調を抑える方向で設計する。
- **責任配分を権限委譲だけで済ませない**: 人間の監視形態と責任の所在を、自動化レベルとあわせて設計する。

## 関連コンセプト

- [[reliance-calibration-between-aversion-and-overtrust]] — 回避と過信の間で依存度を較正する枠組み
- [[choice-architecture-and-reliance-shaping]] — デフォルトを含む選択アーキテクチャによる依存の形成
- [[human-ai-advice-taking-behavior]] — 人間のAIアドバイス受容行動
- [[human-ai-trust]] — AIへの信頼
- [[human-ai-interaction-and-trust]] — 人間とAIの相互作用と信頼
- [[decision-process-visibility-and-reliance-calibration]] — 意思決定過程の可視性と依存度の較正
- [[distributed-responsibility-and-answerability-anchoring]] — 責任帰属と応答可能性の錨

## 参考ソース

- Yue Liu, Ronggang Zhou, Xuezun Zhi (2026)「How cumulative default recommendations asymmetrically shape user compliance in human–automation decision-making?」— `raw/papers/systems_engineering/how-cumulative-default-recommendations-asymmetrically-shape-user-compliance-in-h.md`
- Tobias Rieger, Steffen Hoesterey, Linda Onnasch (2026)「Risk-Free Study Designs Miss the Weak Trust–Behavior Link in Human–Automation Interaction: Evidence From Two Virtual Reality Experiments」— `raw/papers/systems_engineering/risk-free-study-designs-miss-the-weak-trustbehavior-link-in-humanautomation-inte.md`
- Su Hwan Kim, Lisa C. Adams, Benedikt Wiestler, Dennis M. Hedderich (2026)「Human-AI Collaboration in Radiology: The Blind Spots」— `raw/papers/systems_engineering/human-ai-collaboration-in-radiology-the-blind-spots.md`
- Simone Bortolami ほか (2026)「Human-Automation Interactions and Performance Analysis of Lunar Lander Supervisory Control」— `raw/papers/systems_engineering/human-automation-interactions-and-performance-analysis-of-lunar-lander-superviso.md`
