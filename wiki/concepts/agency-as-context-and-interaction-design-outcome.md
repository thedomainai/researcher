# 主体性は内的属性ではなく相互作用設計で決まる

## 概要

AIエージェントが「資源」「主体(アクター)」「受益者」「エージェント」のいずれとして機能するかは、モデルが内部に持つ固有の性質だけでは決まらない。関与する文脈、相互作用の形式(モダリティ)、そしてシステムの設計によって決まる、というのがこの原理である。この役割割当は、人間とAIによる価値共創の成否や、利用の継続意向にも影響する。

AI Nativeな社会設計では、自律的に動くAIが日常的なサービスに組み込まれる。そのとき「このAIは主体的か」と問うより、「どの文脈で、どの形式の相互作用として、どんな役割を割り当てるか」を設計対象とする方が実践的である。本記事は、ソースとなった6本の研究(いずれも2026年)に基づいてこの原理を整理する。

## メカニズム

この原理は、次の三つの構造に分けて整理できる。対象は人間、AI、組織、技術のいずれに入れ替えても成り立つ。

1. **文脈依存的な役割割当**:あるエンティティの役割(資源・主体・受益者・エージェント)は、それが置かれた交換プロセスの中で決まる。同じ技術でも、設計と文脈が変われば異なる役割を担う。
2. **心理的ニーズ充足による関与の持続**:関与が続くかどうかは、相互作用の中で当事者のニーズ(有能感など)がどう満たされるかに左右される。価値は利用後に評価される結果としてではなく、相互作用の過程で共に生み出されるものとして扱われる。
3. **相互作用モダリティによる協働効果の規定**:コミュニケーションの形式や、人とAIの分担の仕方(完全自動か、協働か、AIが人を支援するか)が、協働の効果や態度形成を左右する。

まとめると、役割や効果は主体の「中身」ではなく、主体と相手の間に設計された関係の側に置かれる。

## 理論的背景

**サービス・ドミナント・ロジック(SDL)からの整理**(Schäfer et al., 2026)
生成AIは資源・アクター・受益者の境界を曖昧にする。著者らは体系的文献レビューでこれら概念と、SDLに新たに導入したエージェント概念の定義的性質を導出し、8つの現代的な生成AIシステムをそれらの性質に照らして評価した。その結果、生成AIは第一にオペラント資源として理解するのが最適であり、設計と文脈によってはアクターやエージェントにもなると結論づけている。自律的エージェントの主体性は内部特性ではなく、相互作用の文脈と設計によってサービスシステム内で決まる、という本原理の中心的根拠である。

**AIショッピングエージェントと価値共創**(Shen & Kim, 2026)
SDLと自己決定理論を統合し、価値共創を「先行要因と継続意向をつなぐ過程」と位置づけた。367人の利用者を対象にCB-SEMで分析している。推薦説明の透明性、会話の応答性、有能感が価値共創に有意な正の影響を与える一方、自律性と関係性の効果は有意ではなかった。価値共創は継続意向に強い正の効果(β=.70)を持つ。設計上の特徴(透明性・応答性)が価値共創を通じて継続意向へつながる、という経路が示されている。

**エージェント的能力と学習**(Qin & Jeong, 2026)
大学図書館のAIチャットボットが、情報検索ツールから自律的推論と適応的相互作用を備えたエージェント的システムへ進化したことを背景に、434人の学生を調査した。エージェント的能力が価値共創を媒介して自己主導学習能力に影響する二重の調整媒介モデルを検討し、批判的AIリテラシーとAI自己効力感を段階特異的な調整変数とした。エージェント的能力は有意な正の直接効果を持つと報告されているが、抜粋は途中で途切れており、調整・媒介の詳細な結果はソースの提示範囲からは確認できない。

**サービス回復場面での役割分担**(Mishra, 2026)
ホスピタリティのサービス回復で、完全自動、AI-人間協働、AI支援による人間の回復の3条件を比較した(352人、PLS-SEM)。知覚された能力と自律性の効果は、知覚された有能さによって媒介される。また、リスクガバナンスは関与を妨げるのではなく、有能さの知覚を高めることが示された。人とAIの分担形式そのものが評価の条件となる。

**相互作用モダリティとユーモア**
Ahmedら(2026)は、デジタル顧客サービスにおける相互作用モダリティの役割を扱っており、ソースの知見としてコミュニケーション形式が協働効果を規定する原理が挙げられている(抜粋に要旨本文はなく、詳細な結果は確認できない)。Monroe(2026)は、音声アシスタントとの相互作用でユーザーがユーモアを、娯楽ではなくシステムの探索や関係性の試行のために用いることを、6件の研究レビューから報告している。利用者の側も、相互作用を通じて相手の役割を探っていることがうかがえる。

## AI Nativeな設計への示唆

- **役割を明示的に設計する**:AIを資源として使うのか、アクターやエージェントとして振る舞わせるのかを、機能単位・文脈単位で決めて明示する。「自律的なAI」という属性のラベルで済ませない。
- **透明性と応答性を関与の基盤にする**:推薦の説明や会話の応答性は価値共創を高める設計要素である。詳しくは [[decision-process-visibility-and-reliance-calibration]] も参照。
- **有能感を支える設計**:利用者の有能感の充足は関与の持続に結びつく。一方、自律性や関係性の効果は調査で有意でなかったため、特定の文脈での一般化には慎重であるべきである。
- **人とAIの分担形式を文脈ごとに選ぶ**:完全自動・協働・支援のどれが適切かは、場面(例:サービス回復)ごとに検証して決める。
- **リスクガバナンスを能力知覚の一部として設計する**:統制の仕組みは、利用を抑える要因ではなく、有能さの知覚を支える要素になりうる。
- **利用者側の資質も変数に含める**:批判的AIリテラシーやAI自己効力感が段階ごとに効果を調整しうるため、教育や支援も設計に含める。
- **文脈の変化に応じて再検証する**:役割割当が文脈に依存する以上、妥当性は文脈の境界内でのみ主張できる。[[context-bounded-validity-and-revalidation]] を参照。

## 関連コンセプト

- [[human-ai-interaction-sense-of-agency]] — 人とAIの相互作用における主体感
- [[distributed-agency-and-assemblage-reconfiguration]] — 行為者性が分散し、再構成される観点
- [[agency-as-recursive-transition-law-update]] — エージェンシーの別の捉え方
- [[capability-perception-and-responsibility-diffusion-in-trust]] — 能力知覚と信頼・責任の関係
- [[decision-process-visibility-and-reliance-calibration]] — 透明性と依存度の較正
- [[logic-plurality-conditioned-acceptance-of-autonomous-systems]] — 自律システムの受容条件
- [[context-bounded-validity-and-revalidation]] — 文脈に境界づけられた妥当性
- [[conversational-agent-embodied-interaction]] — 会話エージェントと身体的インタラクション
- [[ai-sensemaking-human-agency]] — センスメイキングと人間のエージェンシー

## 参考ソース

1. Shen, F., & Kim, E. (2026). *Human-AI Value Co-Creation and Continuance Intention toward AI Shopping Agents*.
   File: raw/papers/marketing/human-ai-value-co-creation-and-continuance-intention-toward-ai-shopping-agents.md
2. Qin, Z., & Jeong, D.-Y. (2026). *Influence of Agentic Capability of AI Chatbots on Value Co-Creation and Self-Directed Learning Ability －A Dual Moderated Mediation Model via Critical AI Literacy and AI Self-Efficacy－*.
   File: raw/papers/marketing/influence-of-agentic-capability-of-ai-chatbots-on-value-co-creation-and-self-dir.md
3. Ahmed, K., Lai, Y., Reppel, A., Meechao, K., & Lycett, M. (2026). *Human-AI Interactions in Digital Customer Service: Exploring the Role of Interaction Modality*.
   File: raw/papers/marketing/human-ai-interactions-in-digital-customer-service-exploring-the-role-of-interact.md
4. Schäfer, J. M., Hansmeier, P., Zur Heiden, P., & Beverungen, D. (2026). *Resource, actor, beneficiary, or agent? A service-dominant perspective on generative artificial intelligence*.
   File: raw/papers/marketing/resource-actor-beneficiary-or-agent-a-service-dominant-perspective-on-generative.md
5. Monroe, J. (2026). *Pragmatically speaking: humor in interactions with AI*.
   File: raw/papers/marketing/pragmatically-speaking-humor-in-interactions-with-ai.md
6. Mishra, S. K. (2026). *The Impact of AI on Customer Experience: A Service Recovery Context*.
   File: raw/papers/marketing/the-impact-of-ai-on-customer-experience-a-service-recovery-context.md
