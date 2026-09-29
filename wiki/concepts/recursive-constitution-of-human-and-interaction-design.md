# 設計された相互作用による人間の構成と三層共進化ループ

## 概要

インタラクション設計は、人間の行為を「媒介」するだけの道具ではない。継続的に関わる設計環境は、人間の主体性(agency)、自己理解、身体化された能力、意味形成、責任のあり方を部分的に**構成**する。さらに、この構成は一方向ではない。実務者(設計判断)、利用者(利用実践)、社会(評価・ガバナンス)とAIの間のフィードバックループが、互いを再形成し続ける。

この概念は次の3点を柱とする。

1. **構成的媒介と可逆性**: 設計は人間を形づくる。その形成が元に戻せるか(reversibility)が、エージェント型AI時代の根本問題になる。
2. **多層フィードバックループ**: AI開発は「設計から利用へ」の直線ではなく、三つの圏域にまたがる再帰的システムである。
3. **認識論的内容による介入の分類**: 人間の介入の機能は、タイミングや粒度ではなく、その入力が何を供給するかで決まる。

AI Nativeな設計では、人間が「ループの中にいる」だけでは不十分である。ループがその人間をどう形成し直すかまでを設計対象に含める必要がある。

## メカニズム

以下は、対象(人間/AI/組織/技術)を入れ替えても成立する構造的原理として整理したものである。

### 1. 構成的媒介と可逆性

相互作用の環境Eと主体Sがあるとき、Eとの持続的な関与はSの能力・自己理解・責任の引き受け方を変える。「Eは何を可能にするか」という問い(アフォーダンス、使いやすさ、信頼)だけでは、この変化に届かない。主体が形成された後にEが変わる、あるいは取り除かれる場合、形成された能力は維持されるのか、回復できるのかが問われる。これが可逆性の問題である。

### 2. 再帰的な三層ループ

- **実務者–AI層**: 設計判断
- **利用者–AI層**: 適用実践
- **社会–AI層**: 評価とガバナンス

各層の出力は他の層の入力になる。たとえば設計判断が利用実践を形づくり、実践が社会的評価を生み、評価が次の設計判断を規定する。したがって、どの層も単独では最適化できない。

### 3. 供給内容による介入の分類

介入は「いつ」「どの権限で」「どの粒度で」行うかではなく、入力が何を供給するかで機能が決まる。供給内容は次の三種に整理される。

- **根拠(grounds)**: 結論への資格に関わる考慮事項。世界の側にあり、参照可能。
- **枠組み(frame)**: エージェントが探索している仮説空間の置換。
- **立場(standing)**: 領域の内容は与えず、権威の行使だけを移転する動き(停止信号、判断の要求、目的への再固定など)。

## 理論的背景

### 相互作用の哲学(Lee, 2026)

HCIは何が可能か(affords)、どう媒介するか、使いやすく信頼できるかを問うてきたが、相互作用が生きる人間に何をするかは未解決だとする。論文は、設計された相互作用がagency、自己理解、embodied capacity、意味形成、責任を部分的に構成する、という問いを立てる。緊急性の所在は、human-in-the-loop 型の配置にある。そこでは責任が人間に割り当てられ、「システムが行為し、人が説明責任を負う」構図が強まる。だが、その人間がどう形成されているかという先行問題は、ほとんど直視されていない。

### 三層フィードバックの理論(He et al., 2026)

AI開発は設計から利用への一方向パイプラインではなく、実務者–AI(設計判断)、利用者–AI(適用実践)、社会–AI(評価とガバナンス)の三つの相互依存圏域にまたがる再帰的システムだと論じる。方法論としては、LLMを人間主導のワークフロー内の分析器具と位置づけるLLM強化型計算的グラウンデッド・セオリーを提案する。五段階は、データ構築、LLM支援のトピック生成、人間とLLMによるトピック精緻化、計算的確認、理論生成である。公開言説を事例に適用している。

### 認識論的内容の分類学(Suh, 2026)

ある実務者の2か月分のワークステーション記録(LLMコーディングエージェントへの入力2,205件、うち介入として選別されたもの1,094件)を、入力の認識論的内容(根拠・枠組み・立場)と、入力が作用する対象の二軸でコード化した。既存の分類がタイミング、権限、粒度、欠陥クラス、相互作用状態で索引するのに対し、何を供給するかを軸に据える。既存スキームがコード化しない部分に、修正負荷の所在があると論じている。

### 補完的な知見

- **統合情報処理モデル(Schrills & Franke, 2026)**: 行為調整の心理的メカニズムをインターフェース設計・評価のレバーに結びつける、タスク中心・プロセス指向のモデル。既存のHCI・自動化研究を置き換えず拡張する立場をとる。
- **子ども–AIのエージェンシー(Voysey et al., 2026)**: 25件のHCI研究のレビューで、agencyはほとんど明示的に定義されず、「生得的に持つもの」と「発達させるもの」の間で概念化が揺れる。観察の手がかりは、計画・自己調整、AIへの制御の主張、現状の批判と再設計だった。これは、設計がagencyの形成に関与するという見方と整合する。

## AI Nativeな設計への示唆

1. **利用者の形成を設計目標に含める**: 使いやすさや信頼に加え、継続利用が主体性・自己理解・能力をどう変えるかを評価項目にする。
2. **可逆性を確保する**: 形成された能力や責任の引き受け方が、システムの変更や撤去後も回復可能かを設計時に検討する。関連する論点は [[delegation-induced-ownership-and-capability-erosion]] が扱う。
3. **責任の押し付けを避ける**: human-in-the-loop で説明責任だけを人に割り当てる配置は、人がどう形成されているかという先行問題を素通りする。
4. **介入インターフェースを供給内容で設計する**: 根拠の提示、枠組みの再設定、立場の行使を区別して支援する。停止や目的への再固定のような「立場」の入力は、領域知識がなくても行えるよう、軽く確実な手段として用意する。
5. **三層で同時に評価する**: 設計判断、利用実践、社会的評価・ガバナンスの各層を分断せず、ループとして追跡する。
6. **記録と監査の安定性を保つ**: 意思決定が意味の変化に耐えて監査できる仕組みは [[meaning-bound-decision-record-and-audit-stability]] と関係する。
7. **主体性の多面的な支援**: 計画・自己調整、制御の主張、批判と再設計といった軸でagencyを捉え、支援機能を設計する([[human-ai-interaction-sense-of-agency]])。

## 関連コンセプト

- [[human-ai-interaction-sense-of-agency]] — 主体感の観点
- [[agency-as-recursive-transition-law-update]] — 再帰的更新としてのエージェンシー
- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による能力侵食と回復的足場設計
- [[adaptive-human-ai-coupling]] — 人間とAIの適応的結合
- [[human-ai-interaction-design]] — インタラクション設計全般
- [[human-centered-ai-and-hci]] — 人間中心のAIとHCI
- [[human-ai-collaboration-and-interaction]] — 協働とインタラクション
- [[human-computer-interaction-neural-plasticity]] — 相互作用による形成の神経的側面
- [[simulated-reciprocity-attachment-and-trust-miscalibration]] — 擬似的相互性と信頼の較正ずれ
- [[meaning-bound-decision-record-and-audit-stability]] — 意思決定の監査安定性

## 参考ソース

- Toward a Philosophy of Interaction: How Designed Interaction Constitutes the Human, and Why Its Reversibility Now Matters — Meng-Han Lee, 2026
  File: raw/papers/hci/toward-a-philosophy-of-interaction-how-designed-interaction-constitutes-the-huma.md
- LLM-enhanced computational grounded theory and the triadic dynamics of human-AI-society interaction — Kun He, Qianru Meng, Xiangyuan Feng, Xiao Zhang, Malvina Nissim, 2026
  File: raw/papers/hci/llm-enhanced-computational-grounded-theory-and-the-triadic-dynamics-of-human-ai-.md
- An Epistemic-Content Taxonomy of Human Intervention in Agentic Collaboration — Jongsun Suh, 2026
  File: raw/papers/hci/an-epistemic-content-taxonomy-of-human-intervention-in-agentic-collaboration.md
- A Model of Integrated Information Processing in Human-AI Interaction — Tim Schrills, Thomas Franke, 2026
  File: raw/papers/hci/a-model-of-integrated-information-processing-in-human-ai-interaction.md
- Agency in Child–AI Interaction: A Review of How It Is Conceptualised, Studied, and Supported in HCI — Isobel Voysey, Vidminas Vizgirda, Sarah Turner, Leslye Denisse Dias Duran, Zaki Pauzi, 2026
  File: raw/papers/hci/agency-in-childai-interaction-a-review-of-how-it-is-conceptualised-studied-and-s.md
