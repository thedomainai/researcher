# 有限な認知資源と異質主体間の結合設計

## 概要

有限な認知資源と異質主体間の結合設計とは、注意や認知資源が有限であり、主体ごとに能力が非対称であるという前提から出発し、異質な主体(人間、AI、組織、支援技術)の協調を設計する考え方である。Tier 1(不変原理)に分類される。

この概念の要点は、協調の成立条件を「同じように考えること」や「同期すること」に置かない点にある。ソース[2]は、Human–AI resonanceは整合(alignment)、同意、服従、同期と同一ではなく、2つの異質な認知システムが似た思考をしなくても効果的に協力できると主張する。必要なのは、十分に正確な相互表象、解釈可能な意図の交換、予測的協調、フィードバックと修復、そして意味のある差異を保つ能力とされる。

AI Nativeな社会設計にとって重要なのは、AIが人間の有限な注意や能力差を無視して高性能を発揮しても、協調は成立しないからである。設計対象は個々の主体の性能ではなく、主体間の結合の仕方である。

## メカニズム

対象を入れ替えても成立する構造は、次の3つに整理できる。

1. **有限資源による選択的配分**:どの主体も処理できる情報量には上限があり、複数の課題が競合すると選択的な配分が起こる。ソース[1]の知見は、この限界がメディア形態に依存せず、マルチタスク下の注意配分を規定する原理であることを示している。人間の注意でも、AIの計算資源でも、資源が有限であることは変わらない。
2. **相互予測可能性による協調**:異質な主体同士は内部状態を直接共有できない。そのため、相手の振る舞いや意図をある程度予測できることが安定協力の条件になる(ソース[2])。ソース[3]は、ユーザーの信念や目標が直接観測できないという教師データの制約を、心的状態のシミュレーションで補う方法を提案しており、相手の状態を推定する必要性を示す一例である。
3. **能力非対称性に応じた段階的調整と構成選択**:支援の粒度やタイミングは、相手の状態と局面に合わせて変える必要がある。さらに、どの主体にどの役割を割り当てるかという構成自体も、状況の複雑性によって選び直される(ソース[9])。

この3つは、人間対AI、人間対人間、AI対AI、組織内の意思決定のいずれにも当てはまる。

## 理論的背景

**注意制御の研究**:ソース[1]は、メディア・マルチタスキングと注意制御の関係について、横断研究の結果が一貫せず結論が出ていない現状を指摘している。著者らは、関連する個人内要因の考慮が不足していることが研究全体の問題だと論じ、理論駆動型の研究課題を提示している。

**共鳴プロトコル**:ソース[2]のHARP 2.0は、表象の一貫性、意図の翻訳、相互予測、適応的結合、文明的共進化を扱うテスト可能な枠組みとして提示されている。安定・解釈可能・適応的・修正可能な認知協力を目標とする。

**心的状態の推定**:ソース[3]のMind2Dialogueは、個人特性を保ちつつ対話で心的状態を更新するシミュレータを用い、それを特権的な教師信号として人間を意識した言語モデルを訓練する。ただし実装方法は不変ではないため、Tier 2に位置づけられている。

**選好形成と二重過程**:ソース[4]は、938名の参加者による三択実験で、文脈感受性などの認知的仮定を構造に埋め込んだ6つのニューラルネットワークモデルを比較し、自然な視覚刺激下の多属性選好の形成を調べている。ソース[5]は、自動的処理と制御的処理という二重過程理論を、精神力動、臨床、神経生物学の観点から検討している。

**段階的・文脈的支援の実証**:
- ソース[6]のPV-Careは、装着型脳波と視覚的環境認識を統合し、軽度認知障害のユーザーに対して、検出した脳状態(学習、記憶想起、安静)に基づき能動的に音声支援を開始する。
- ソース[8]のTouvigationは、視覚障害・弱視ユーザー向けに、定位、歩行、手を伸ばして触覚で確認する段階に合わせて空間的参照を切り替える多段階ガイダンスを設計し、12名で評価した。
- ソース[7]は、1,146名の成人を6か月追跡し、抑うつ症状の現れ方がデバイスや活動の種類といったデジタル文脈によって大きく異なることを示した。単一指標や総画面時間では差が見えなくなる。

**構成選択とモデル規模**:ソース[9]のHybrid Intelligence Configuration Matrixは、認知的複雑性、社会情動的複雑性、時間的圧力の3次元から8つの構成を導き、代替か拡張かという単純な見方を超える動的な構成の視点を示す概念枠組みである。ソース[10]のサーベイは、計算コストとエネルギー消費の制約のもと、大規模モデルと小規模モデルの関係を協調と競合(補完)の観点から整理している。

## AI Nativeな設計への示唆

- **同期ではなく予測可能性を設計目標にする**:AIの意図や限界を人間が予測でき、AIも人間の状態を推定できるようにする。フィードバックと修復の経路を組み込む。
- **支援を段階化する**:利用者の局面や状態に応じて支援の形式を切り替える(ソース[6][8])。一律の支援は能力差のある相手には合わない。
- **文脈を分けて観測する**:同じ主体でも文脈によって状態の現れ方が異なるため(ソース[7])、単一の集計指標で判断しない。
- **構成を固定しない**:課題の複雑性や時間的圧力に応じ、人間主導、AI主導、協働といった構成を選び直せる設計にする(ソース[9])。
- **資源に見合った主体を使い分ける**:常に最大のモデルを使うのではなく、小規模モデルとの分担を含めて計算資源を配分する(ソース[10])。
- **差異を保存する**:人間とAIの違いを消して均質化するのではなく、違いを保ったまま結合する(ソース[2])。

## 関連コンセプト

- [[finite-cognitive-resources-and-load-thresholds]]
- [[metacognitive-allocation-under-finite-resources]]
- [[cognitive-limits-information-overload]]
- [[adaptive-human-ai-coupling]]
- [[ai-human-cognitive-interaction]]
- [[robotics-and-heterogeneous-agent-learning]]
- [[ai-as-cognitive-extension]]
- [[ai-cognitive-augmentation]]
- [[threshold-phase-transition-in-technology-dependence]]

## 参考ソース

1. Media-multitasking and attentional control: A theory-driven research agenda(Elger Abrahamse ほか、2026)— `raw/papers/cognitive_science/media-multitasking-and-attentional-control-a-theory-driven-research-agenda.md`
2. The Human-AI Resonance Protocol 2.0 A Testable Framework for Representational Coherence, Intention Translation, Mutual Prediction, Adaptive Coupling, and Civilizational Co-Evolution(政恩 馮、2026)— `raw/papers/cognitive_science/the-human-ai-resonance-protocol-20-a-testable-framework-for-representational-coh.md`
3. Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States(Zixuan Wang ほか、2026)— `raw/papers/cognitive_science/mind2dialogue-training-human-aware-language-models-by-simulating-user-mental-sta.md`
4. Leveraging Cognitive-Inspired Machine Learning to Understand Multi-Attribute Preference Construction(William R. Holmes ほか、2026)— `raw/papers/cognitive_science/leveraging-cognitive-inspired-machine-learning-to-understand-multi-attribute-pre.md`
5. Dual-process theories beyond cognitive psychology: psychodynamic, clinical, and neurobiological perspectives(Özge Türkoğlu, Başaran Demir、2026)— `raw/papers/cognitive_science/dual-process-theories-beyond-cognitive-psychology-psychodynamic-clinical-and-neu.md`
6. Beyond Reactive Assistance: PV-Care Using Low-Density EEG and AI to Provide Proactive, Context-Aware Help for MCI(Simon L Liu, Manish Kumar Krishne Gowda、2026)— `raw/papers/cognitive_science/beyond-reactive-assistance-pv-care-using-low-density-eeg-and-ai-to-provide-proac.md`
7. Depressive symptoms are reflected differently across digital contexts(Yajing Wang ほか、2026)— `raw/papers/cognitive_science/depressive-symptoms-are-reflected-differently-across-digital-contexts.md`
8. Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments(George Xi Wang ほか、2026)— `raw/papers/cognitive_science/touvigation-embodied-adaptive-object-acquisition-for-blind-and-low-vision-users-.md`
9. The Hybrid Intelligence Configuration Matrix: A conceptual framework for designing human–AI configurations in organizational decision-making(Ahmad Syaiful Affa, Danang Satrio、2026)— `raw/papers/cognitive_science/the-hybrid-intelligence-configuration-matrix-a-conceptual-framework-for-designin.md`
10. What is the Role of Small Models in the LLM Era: A Survey(Lihu Chen, Gaël Varoquaux、2026)— `raw/papers/cognitive_science/what-is-the-role-of-small-models-in-the-llm-era-a-survey.md`
