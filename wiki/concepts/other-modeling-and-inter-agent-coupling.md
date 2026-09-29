# 他者モデリングと主体間結合・相補性

## 概要

他者モデリングと主体間結合・相補性とは、異なる主体が互いの心的状態(信念・意図)を推論し、行動や神経活動を同期・結合させ、視点の違いを組み合わせることで、単独では到達できない探索空間へ広がる、という共通原理である。本コンセプトは Tier 1(不変原理)に位置づけられる。

この原理は次の現象を同じ構造として捉える。

- 他者の信念・意図を推論して自分の選択に活かすこと(mentalization)
- 協力作業中の主体間の同期
- 視点の多様性による探索の拡大
- 専門家から初心者への知識移転

AI Nativeな社会では、人間同士だけでなく、人間とAI、AI同士が協働する。相手が誰であっても成立する原理を押さえておけば、特定の技術形態に依存しない設計ができる。一方で、AIを「もう一人の参加者」として置くだけでは相補性が得られない場合があることも、ソースは示している。

## メカニズム

対象(人間/AI/組織/技術)を入れ替えても成立する構造は、次の三つに整理できる。

1. **心的状態の推論(他者モデル)**: 主体は相手の信念・意図を内部モデルとして持ち、それを使って自分の行動を調整する。相手の洗練度に応じて戦略を変えられるかどうかが、能力の分かれ目になる。
2. **主体間の同期・結合**: 協力の場面では、主体の状態(行動、神経活動など)がタスク文脈に応じて結びつく。結合の強さや形は、課題や相互作用の種類で変わる。
3. **視点多様性による探索空間の拡大**: 異なる視点・知識をもつ主体が組み合わさると、一人では届かない領域を探索できる。ただし、それには各主体が相手に固有の情報を持ち込むことが前提となる。

知識移転は、この三つの組み合わせとして読める。専門家の知識は相互に結びつき暗黙的であるため、初心者のモデルを踏まえた足場かけがなければ伝わらない。

## 理論的背景

### mentalization の計算的検証

Sohail らの研究(2026)は、mentalization を「他者の信念や意図を推論して自分の選択を導く能力」と定義する。二つの経済ゲームと認知計算モデリングを用い、DeepSeek、GPT-4.1、GPT-5、Gemini 2.0 Flash の4つのモデルファミリー(N = 2,099)を、洗練度の異なる対戦相手と対戦させた。さらに、戦略的推論を引き出すプロンプトの効果を調べ、人間参加者(N = 251)と比較した。LLMが心の理論課題で人間と整合的に振る舞うことは知られているが、mentalization によって適応行動を導けるかは未解明だったという問題設定である。他者モデリングの計算原理を、人間とAIで共通の枠組みから評価できることが、この研究の要点である。

### 視点の多様性と探索空間

Beck らのスコーピングレビュー(2026)は、「多様性が独創的で影響力のある科学を生む」という主張(Diversity Hypothesis)を、事前登録した迅速スコーピングレビューで検証している。Joanna Briggs Institute の手法と PRISMA-ScR に従い、三つのデータベースを系統的に検索した。異なる視点の組み合わせが探索を広げるという原理を、実証的に吟味する試みである。

### 多様性への対応と柔軟なカテゴリー化

Saettone の博士論文(2026)は、多様性を独立した変数の集合ではなく、ユーザー・技術・研究手法が互いを規定し合う関係的条件(interdiversity)として捉える。文化は、膨大な知識の中から局所的に関連する部分を選び、限られた情報の下で行動を可能にする一般的認知戦略の、社会的に組織された形とされる。その能力は、隠喩とアナロジーによる柔軟なカテゴリー化に依存すると論じられる。ただしソースの評価では、ロボット技術への依存が抽象度を損なう面がある。

### 専門家―初心者の相互作用

van Nooijen の博士論文(2026)は、複雑な視覚課題の学習で、初心者が専門家との一対一の対話に頼ることが多い点に注目する。専門家の知識は相互に結びついて暗黙的なため、教育訓練を受けていない専門家には伝えにくい。スコーピングレビューでは、ワーキングメモリのモデルや認知負荷理論に基づく足場かけの枠組みが構築された。知識移転が認知的制約に縛られることを示しており、この制約は時代によって変わらない基本原理と位置づけられる。

### 脳間結合

da Silva Soares Junior と Sato の探索的 fNIRS ハイパースキャニング研究(2026)は、学齢期の子ども15ペアに、安静、単独での問題解決、観察、協力というタングラムパズル課題を課した。事前に定めた関心領域では、多重比較補正後に有意な活性化効果は残らなかった。探索的なチャネルレベルでは、後部頭頂のチャネルで陽性の HbO 反応が見られた。全体として探索的であり、結果は個人間の神経的同期メカニズムを示唆するものにとどまる。

### 人間-AI協働と相補性の阻害

Lai らの事前登録研究(2026)は、代替用途課題(AUT)と創作短編執筆で、人間-人間(68ペア)と人間-AI(GPT-4o、72ペア)の協働を比較した。ソースの抜粋によれば、AI協働における創造性の「優位」は見かけ上のもので、主にAIの冗長さによる。この冗長さが人間との認知的相補性を阻害する構造的メカニズムとして働くと解釈されている。

### AIの主体性をめぐる基準

民(2026)は、AIが人間と同等の standing を持つには、人間が備える心的概念の全領域を実装する必要があると論じる。人間を最も広い範囲の心的実体とみなし、比較基準は時間や概念の再定義で動かしてはならないとする。他者を主体として扱う際の基準を考える手がかりになる。

## AI Nativeな設計への示唆

- **相手の洗練度に応じた戦略を評価する**: AIエージェントを、他者モデルに基づいて適応できるかという観点で評価する。戦略的推論を引き出す介入が有効かも検証対象になる。
- **量ではなく相補性で協働を評価する**: 出力量や冗長さで創造性を測ると誤認する。AIパートナーには人間の視点を補う固有の寄与が求められる。
- **知識移転には受け手モデルに基づく足場かけを組み込む**: 暗黙知を扱う場面では、認知負荷とワーキングメモリの制約を前提に、段階的な支援を設計する。
- **多様性を関係的条件として設計する**: ユーザー・技術・方法が互いを規定し合うという前提で、文脈に応じた柔軟なカテゴリー化を支える。
- **同期の解釈は慎重に**: 脳間結合の知見は探索的段階にあるため、設計指針として過度に一般化しない。
- **主体性の基準を明示する**: AIを主体として扱う範囲と、その根拠となる心的機能の範囲を明確にする。

## 関連コンセプト

- [[inter-brain-synchronization]] — 主体間の神経的同期の具体的な現れ
- [[human-ai-trust-complementarity]] — 人間とAIの信頼と相補性
- [[adaptive-human-ai-coupling]] — 人間とAIの適応的な結合
- [[finite-attention-and-heterogeneous-agent-coupling]] — 有限な認知資源のもとでの異質主体の結合
- [[homogeneous-multi-agent-debate-limits]] — 視点が同質な場合の限界
- [[computational-rational-user-modeling]] — ユーザーの計算的モデル化
- [[consciousness-and-recursive-self-modeling]] — 自己と他者のモデル化
- [[evidence-grounded-role-separated-agent-coordination]] — 役割分離によるエージェント協調

## 参考ソース

1. Assessing mentalization in humans and large language models — Aamir Sohail, Xintong Zhong, Arkady Konovalov, Patricia L. Lockwood, Lei Zhang (2026)
   File: raw/papers/neuroscience/assessing-mentalization-in-humans-and-large-language-models.md
2. Diversity-Aware Social Robots for Education and Social Assistance — L. Saettone (2026)
   File: raw/papers/neuroscience/diversity-aware-social-robots-for-education-and-social-assistance.md
3. See what I mean?: Understanding and supporting expert-novice interactions in learning complex visual tasks — Christine van Nooijen (2026)
   File: raw/papers/neuroscience/see-what-i-meanunderstanding-and-supporting-expert-novice-interactions-in-learni.md
4. Inter-brain coupling during naturalistic collaborative Tangram solving in child dyads: an exploratory fNIRS hyperscanning study — Raimundo da Silva Soares Junior, João Ricardo Sato (2026)
   File: raw/papers/neuroscience/inter-brain-coupling-during-naturalistic-collaborative-tangram-solving-in-child-.md
5. Creative or Uncreative Partner: Comparing Humans and AI in Collaborative Creative Tasks — Clin KY Lai, Simone A Luchini, Nina Lauharatanahirun, Roger E. Beaty (2026)
   File: raw/papers/neuroscience/creative-or-uncreative-partner-comparing-humans-and-ai-in-collaborative-creative.md
6. The diversity hypothesis: A rapid scoping review of diversity and scientific output and impact in the natural and social sciences — Jordan P. Beck, Zachary Patterson, Samuel Wilson (2026)
   File: raw/papers/neuroscience/the-diversity-hypothesis-a-rapid-scoping-review-of-diversity-and-scientific-outp.md
7. Can AI Be an Individual, a Mental Entity, and a Subject? — 민경권 (2026)
   File: raw/papers/neuroscience/can-ai-be-an-individual-a-mental-entity-and-a-subject.md
