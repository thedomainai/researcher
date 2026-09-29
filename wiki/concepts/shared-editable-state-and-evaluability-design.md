# 共有可変状態と評価可能性を担保する情報設計

## 概要

共有可変状態と評価可能性を担保する情報設計とは、提案・状態・表現を、受け手が**検査(inspect)でき、かつ編集(edit)できる**形で提示するという設計原理である。有限な認知資源の下では、主体が「何が提示されているか」を評価できなければ、協調の質は提示内容そのものの質ではなく、提示の仕方に律速される。この構造は、主体が人間であってもAIであっても成立する。

AI Nativeな社会では、AIが提案・計画・編集を大量に生成し、人間がそれを評価して採否を決める場面が増える。このとき「AIが良い提案をする」だけでは不十分である。ソース[1]は、既存の支援手法が提案の質やユーザー目標の推定に注力し、ユーザーがどんな提案でも確実に評価できると仮定しがちであること、そしてその仮定が有限合理性のために現実には破れうることを指摘している。したがって、評価可能性を前提に組み込んだ情報設計が、AI Nativeな協調設計の基盤になる。

## メカニズム

この原理は、主体の種類を入れ替えても成り立つ次の構造として整理できる。

1. **有限な評価能力**:評価者(人間、AI、組織の意思決定者など)は、有限な認知資源しか持たない。評価できない提示は採否判断の根拠にならない。関連する背景は [[cognitive-limits-information-overload]] を参照。
2. **状態の透明化**:協調に用いる情報(文脈・前提・記憶・インターフェース上のタスク状態)が、暗黙的な内部状態にとどまらず、外から読める形になっている。[[externalized-state-and-representation-fidelity]] と対応する。
3. **編集可能性**:読めるだけでなく、修正が後続の計算や判断が読む状態そのものに反映される。修正が「追加の指示」や「別の記録」として積み上がるのではなく、同一の状態を書き換える。
4. **フレーミングによる認知誘導**:同じ内容でも、見出し・説明・提示形式が受け手の解釈を方向づける。提示の枠組みは中立ではなく、設計対象である。
5. **提案と学習の循環**:提案は課題への介入であると同時に、相手の選好や評価制約を知るためのプローブにもなる。得られた応答が次の提案を導く。

対象を入れ替えると、人間→AIでは提案の評価可能性、AI→人間では状態の検査・修正可能性、AI→AI(エージェントがUIを読む場合)ではインターフェース表現の意味の明示性、組織では意思決定材料の可読性として現れる。いずれも「評価者が検査・編集できる形で情報が置かれているか」が協調の質を決める。

## 理論的背景

**評価可能性を考慮した提案計画(ソース[1])**:ProSEは、提案が課題への介入と、潜在的な選好・評価制約を学ぶプローブを兼ねる隠れパラメータ付き逐次支援問題として定式化される。ユーザーの応答は、KL正則化された有限合理的な二値応答モデルで表され、採否は価値の向上と、距離に依存する評価可能性ペナルティとのトレードオフで決まる。抜粋によれば、この尤度の計画上の帰結として、受理されやすい提案と情報量の多いプローブは必ずしも一致しない。

**共有編集可能状態(ソース[2])**:Transfiverは、モデルと人間の双方が更新する単一の永続状態 (S_t) を持つ共推論アーキテクチャである。状態の進化には、モデルが対話を解釈して既存項目の改訂か新規作成かを決める「暗黙のストリーム更新」と、人間が指定項目を検査・修正する「明示的な指示編集」の2種類がある。両者は同じ状態に作用し、人間の修正は後続の計算が読む状態を変える。背景には、推論を導く情報がモデルによって暗黙に更新され、ユーザーが直接検査・制御できないという長期的な人間-AI対話の困難がある。

**理解可能性は測定しなければならない(ソース[3])**:XAI(コンピュータビジョン)の研究は、手法の構築と比較に注力してきた一方、モデルが実際に依存する人間に理解できるかという問いは十分扱われてこなかった。著者らは、理解可能性は推論ではなく測定でしか得られず、期待を確認する専門家ではなく独立した評価者による検証が必要だと論じる。これは評価可能性を設計要件とする立場と整合する。

**フレーミングの効果(ソース[5])**:折れ線グラフのタイトルの語数と意図されたメッセージは、閲覧者が識別するパターンに有意な影響を与えた。表現の枠組みが認知を形づくることを示す実証である。

**エージェントにとっての表現(ソース[7])**:Affora は、エージェントの性能が、インターフェース表現を通じて得られる「インタラクションの意味」に依存し、その意味が保たれる限り視覚的な変化の余地は大きいと報告している。既存の独立作成インターフェースでは、Affora が対処する欠陥がある場合に改善が見られ、欠陥がない場合や範囲外では効果は限定的だった。人間とエージェントが同じインターフェースを共有する設計が示されている。

**説明モダリティ(ソース[8])**:自動運転の曖昧な状況で、視覚-テキスト(VT)は視覚-聴覚(VA)や視覚-テキスト-聴覚(VTA)より状況信頼が有意に低く、認知負荷が高かった。満足度はVTからVA、VTAの順に上がり、モダリティとシナリオの交互作用は有意でなく、効果は曖昧さの種類を超えて一般化することが示唆された。

**その他の関連知見**:ソース[9]は、AIへの信頼に透明性という普遍的な制約があるが、その実装は文化・制度に依存すると論じる。ソース[6]は、生成・エージェント型AI時代に心的モデルの操作的定義が不統一で、研究の通約性が損なわれうると指摘する。ソース[4]は、協働における暗黙の慣習が、文面から予測される失敗確率と観測値のずれ(convention gap)として測定でき、Hanabiでは人間ペアで+26.2pp、AIペアで−0.7pp、人間-AIペアで+16.4ppだったと報告する。暗黙の慣習は明示的内容だけでは捉えきれず、検査可能な形にする難しさを示す。

## AI Nativeな設計への示唆

- **提案は評価可能な距離に置く**:提案の価値だけでなく、受け手が評価できる範囲かを設計変数にする。評価しにくい提案はプローブとして段階的に用いる(ソース[1])。
- **状態を単一化し、双方から編集可能にする**:AIが暗黙に更新する記憶や文脈を、項目単位で検査でき、人間の修正が後続処理に直接反映される形にする(ソース[2])。
- **理解可能性を独立評価者で測る**:説明手法の精緻さで良しとせず、実際に依存する人間による検証を組み込む(ソース[3])。
- **提示のフレーミングを設計対象にする**:見出しや説明文は解釈を誘導するため、意図した解釈と実際の解釈のずれを検証する(ソース[5])。
- **エージェントにも読める意味表現を共有インターフェースに持たせる**:人間向けとエージェント向けを別系統にせず、操作の意味とタスク状態を明示する(ソース[7])。
- **説明は複数モダリティを検討する**:認知負荷と信頼に影響するため、状況に応じて提示チャネルを設計する(ソース[8])。
- **暗黙の慣習の存在を前提にする**:明示的な内容だけで協調の質を評価せず、暗黙の通約による差を測定する(ソース[4])。
- **透明性の実装は文脈に合わせる**:原理は共通でも、具体形は文化・制度に依存する(ソース[9])。

## 関連コンセプト

- [[externalized-state-and-representation-fidelity]] — 状態を外部化し、その表象の忠実度を保つ考え方
- [[cognitive-limits-information-overload]] — 有限な認知資源と意思決定の劣化
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失
- [[continuous-human-signal-loop-and-temporary-support]] — 人間シグナルの循環と支援の設計
- [[layered-governance-and-agency-retention]] — 主体性を保持するガバナンス
- [[crystallized-structure-to-generative-resonance-and-shared-artifacts]] — 共有アーティファクトを介した協働
- [[aggregation-induced-information-loss]] — 集約による情報損失

## 参考ソース

1. Propose to Learn, Learn to Propose: Evaluability-Aware Assistance under Bounded Rationality — Yifan Zhu, Sammie Katt, Samuel Kaski (2026)
   File: raw/papers/hci/propose-to-learn-learn-to-propose-evaluability-aware-assistance-under-bounded-ra.md
2. Transfiver: Human-AI Co-Inference through a Shared Editable State — Minji Park, Seunghyun Yoon, Hyuk Lim (2026)
   File: raw/papers/hci/transfiver-human-ai-co-inference-through-a-shared-editable-state.md
3. From Interpretability Methods to Interpretable Models — Julien Colin, Nuria Oliver, Thomas Serre (2026)
   File: raw/papers/hci/from-interpretability-methods-to-interpretable-models.md
4. The Convention Gap: Towards Measuring Implicit Communication in Cooperative AI Evaluation — Makoto Fukushima, Hua-Dong Xiong, Ehsan Moradi Pari (2026)
   File: raw/papers/hci/the-convention-gap-towards-measuring-implicit-communication-in-cooperative-ai-ev.md
5. Quick-View Takeaways: How Does Title Framing Influences Pattern Identification in Line Charts? — Jasmine Lim, Tapendra Pandey, Arran Zeyu Wang, Ghulam Jilani Quadri (2026)
   File: raw/papers/hci/quick-view-takeaways-how-does-title-framing-influences-pattern-identification-in.md
6. [MM/AI] Mental Models in Human-AI Interaction: Methods and Challenges in the Generative and Agentic AI Era (Workshop) — Téo Sanchez, Bhada Yun, Prerna Ravi, Laura Schütz, Anna Neumann (2026)
   File: raw/papers/hci/mmai-mental-models-in-human-ai-interaction-methods-and-challenges-in-the-generat.md
7. Affora: A Design System for Agent-Friendly Interfaces — Jin Gao (2026)
   File: raw/papers/hci/affora-a-design-system-for-agent-friendly-interfaces.md
8. Evaluating Multimodal Explainable AI in Ambiguous Driving Scenarios: Effects on User Trust and Satisfaction — Ignacio Álvarez, Tobias Seidl (2026)
   File: raw/papers/hci/evaluating-multimodal-explainable-ai-in-ambiguous-driving-scenarios-effects-on-u.md
9. Explainable AI for Fraud Prevention: Building Trust and Sustainability in Digital Economies — Parteeban M. Varatharajoo, Nur Haryani Zakaria, Juhaida Abu Bakar, Aniza Md Din (2026)
   File: raw/papers/hci/explainable-ai-for-fraud-prevention-building-trust-and-sustainability-in-digital.md
