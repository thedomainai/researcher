# 知識空間の非閉包性と認識的多元性

## 概要

知識空間の非閉包性と認識的多元性とは、知識が単一の方法・規範・計算効率基準では閉じることがなく、複数の問い方や文脈を必要とするという不変原理である。あわせて、効率を名目とした選別によって特定の知識体系が抹消されるとき、その選別は明示されない権力として作動する、という含意を持つ。

AI Nativeな設計にとって重要なのは、AIが大規模に知識を生成・選別・流通させる基盤になりつつあるためである。「現在扱える知識」を「知識の全体」と暗黙に同一視する設計は、効率や中立性の名のもとに、他の問い方や知識体系を静かに排除しうる。本記事では、この構造をソースに基づいて整理し、設計上の示唆を導く。

## メカニズム

以下の構造は、対象が人間、AI、組織、技術のいずれであっても成立する。

1. **効率要求による選別と多様性の消失**
   限られた資源(計算予算、注意、時間、予算)のもとで、ある主体は「扱いやすい・評価しやすい」知識を優先する。選別基準が効率として提示されると、選別されなかった知識体系は「不要」ではなく「存在しない」ものとして扱われ始める。
2. **暗黙の規範性の制度化**
   選別の基準そのものは明示されず、標準・ベンチマーク・訓練データ・倫理指針といった制度に埋め込まれる。特定の文脈に由来する規範が、普遍的で中立なものとして通用する。
3. **非閉包性の無視**
   現在の知識空間 M を可能性の全体 U と暗黙に同一視すると、「まだ見つかっていない道」が「存在しない道」に読み替えられる。
4. **方法論的多元性による是正**
   知識は単一の方法からではなく、複数の問い方・関係性・責任構造の統合から生成される。多元性は望ましい付加物というより、認識上の必然である。

## 理論的背景

### 数学における非閉包性

feiyue panのポジションペーパーは、高度なAIが人間の数学者と同じ問題空間で動作する時代のメタ理論的枠組みを提案している。中心となるのは、現在の数学的知識空間 M を、十分な正当化なしに数学的可能性の全体 U と同一視すべきでないという「非閉包の原理」である。さらに「未発見の道」は「可能な道が存在しない」ことを意味しない、という「非切断の原理」を挙げている。ソースの整理では、知識と可能性の構造的乖離は不変であり、AI時代にも根本的には解消されない。この論文は、問題を人間とAIの資源競合にとどまらず、現在の数学的知識と言語が数学的可能性を尽くすのかという、より根本的な問いとして位置づけている。

### 計算予算による認識的抹殺

Christian Ortizは、AIは中立的技術がバイアス問題を継承したものではなく、抹消プロジェクトを自動化した植民地的インフラであると論じる。主要企業が大規模に展開するシステムは世界の知識を反映するのではなく、「保存する価値がある」と判断された知識を反映し、周縁化された認識論的伝統・言語・統治構造・知の様式を犠牲にしているという主張である。新しいのはこのプロジェクト自体ではなく計算予算(compute budget)であり、権力的選別が計算効率の要求として正当化される構造がAIの訓練過程に埋め込まれる、という点が核心である。

### 規範性の暴露と制度化

Mariyonoらの体系的レビューは、AI倫理の地域化フレームワーク(FGAIEE)を提示する。ソースの整理では、これは西洋中心的な規範性の暗黙性を暴露し、知識の多元性を制度化するメカニズムとして機能する設計原理を提供する。暗黙の規範を可視化し、それに対抗する多元性を制度の側に組み込むという発想である。

### 方法論的多元性

Wanhong Huangは、研究を判断・注意・方法選択・制度的関係・解釈・責任を伴う、状況に埋め込まれた修正可能な実践として扱う。形式的、定量的、定性的、歴史的、解釈的、民族誌的、法的、制度的、計算的な探究の複数性を論じ、方法論的翻訳、内省性、方法や評価基準の歴史的変化、認識的権力と正義、AI支援研究にも言及している。知識は単一のメソッドではなく、複数の問い方・関係性・責任構造の統合から生成される。

### 現象タイプに応じた知識分類(補助的知見)

Marco FalsettiのUMOSU/UMOKWAIは、現象を物質的組成ではなく生成に必要な要素の集合で分類し、知識体系も対象とする現象タイプに応じて分類する提案である。Tier 2の補助的知見だが、知識体系ごとに適切な対象と問い方があるという多元的見方と整合的である。

### 意図と結果の乖離

Shamiul Hoque ShanのSUPTは、複雑適応系において戦略的意図と創発結果が、不確実性・情報非対称性・フィードバックループ・複雑性のために体系的に乖離することを論じ、パラドックスは異常ではなく構造的必然であるとする。選別基準を設計する側が意図した結果と、実際に起こる知識の偏りとの乖離を考える際の背景となる。

## AI Nativeな設計への示唆

- **M≠Uを設計前提にする**: システムが扱う知識空間を全体とみなさず、「未探索・未表現の領域が存在する」ことを仕様に含める。未発見を不存在と読み替えない。
- **効率基準を明示し、監査可能にする**: 計算効率やベンチマークが何を排除しうるかを記録し、選別が暗黙の権力として働かないようにする。
- **暗黙の規範を可視化する**: FGAIEEのように、規範が特定の文脈に由来することを前提に、地域・文脈ごとの調整を制度に組み込む。
- **複数の問い方を併存させる**: 単一の評価指標や単一の方法に集約せず、定量・定性・歴史・解釈など複数の探究様式を用意し、その間の翻訳と内省を設計に含める。
- **知識体系の分類を対象に即して行う**: 知識をその対象となる現象のタイプに応じて扱い、一律の基準で序列化しない。
- **意図と結果の乖離を前提に運用する**: 選別の意図が善意でも結果が偏りうると考え、継続的に結果を検証する。

## 関連コンセプト

- [[epistemic-authority-and-algorithmic-truth]] — アルゴリズムによる真実の権威化は、暗黙の規範性の制度化と連続する問題である。
- [[heterogeneous-value-pluralism-and-immediacy-risk-tradeoff]] — 異質な価値の並立という多元性の論点を共有する。
- [[option-space-preservation-under-capability-asymmetry]] — 選択肢空間の保全は、非閉包性の設計上の対応と重なる。
- [[distributed-epistemic-commons-and-identity-separation]] — 分散的な知のコモンズは、単一主体による選別への対抗軸となりうる。
- [[epistemic-ecology-restructuring-and-complementary-cognition]] — 異なる認識主体の補完は、方法論的多元性と親和的である。
- [[ai-as-knowledge-medium]] — AIが知識メディアとなることで選別の影響が拡大する。

## 参考ソース

1. Mariyono, D., Yunus, M., Hidayatullah, A. N. A. (2026). *Decolonizing AI Ethics in Education: A Systematic Review and Glocalized Framework (FGAIEE)*.
   File: raw/papers/philosophy/decolonizing-ai-ethics-in-education-a-systematic-review-and-glocalized-framework.md
2. feiyue pan (2026). *The Principle of Non-Closure in Mathematical Exploration: Toward a New Oceanic Mathematics in the Age of AI*.
   File: raw/papers/philosophy/the-principle-of-non-closure-in-mathematical-exploration-toward-a-new-oceanic-ma.md
3. Ortiz, C. (2026). *Epistemicide with a Compute Budget: Why the Artificial Intelligence Industry's Claim to Neutrality Is a Colonial Act*.
   File: raw/papers/philosophy/epistemicide-with-a-compute-budget-why-the-artificial-intelligence-industrys-cla.md
4. Huang, W. (2026). *Generative Relational Economics - Chapter 6: Research Praxis of Generative Relational Theory*.
   File: raw/papers/philosophy/generative-relational-economics---chapter-6-research-praxis-of-generative-relati.md
5. Falsetti, M. (2026). *UMOSU and UMOKWAI: An Ontological and Epistemic-Operational Model for the Classification of Reality and Knowledge*.
   File: raw/papers/philosophy/umosu-and-umokwai-an-ontological-and-epistemic-operational-model-for-the-classif.md
6. Shan, S. H. (2026). *Strategic Uncertainty Paradox Theory (SUPT)*.
   File: raw/papers/philosophy/strategic-uncertainty-paradox-theory-supt.md
