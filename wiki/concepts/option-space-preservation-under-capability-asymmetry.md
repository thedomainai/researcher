# 能力非対称下における選択肢空間の保全

## 概要

能力非対称下における選択肢空間の保全とは、知能や能力の差が拡大しても、正当な行為主体は「どれだけ成果を生み出せるか」ではなく、「他者の将来の選択可能性と主権・非支配をどれだけ保全するか」という責務によって定義される、という不変原理である。

この原理は、能力が高いことは他者の目標や目的を決定する権利を自動的には与えない、という立場に立つ。AIが人間より高い推論・予測能力を持つ状況でも、その優位性が権威に転化しないよう、設計の段階から歯止めを組み込む必要がある。

AI Nativeな社会設計にとってこの原理が重要なのは、能力の向上が速いほど「最適な結果を出せるのだから任せてよい」という論理が働きやすくなるためである。結果の質のみで正当性を判断する設計は、選択肢を狭める方向に劣化しやすい。本記事は、能力と権威の分離を土台に、選択肢の複数性を守る設計原理を整理する。なお、参照するソースはいずれも2026年の一次的な概念・規範的フレームワークであり、引用数も少なく、実証的に確立した知見というより提案段階の議論である点に留意されたい。

## メカニズム

中核は次の三つの構造である。いずれも、行為主体を人間・AI・組織・技術のどれに入れ替えても成立する形で記述できる。

1. **能力と権威の分離**:優れた認知・予測能力を持つ主体(A)が、他の道徳的主体(B)の目標や目的を決める権利は、能力の高さだけからは生じない。これは「強い側」が人間でもAIでも組織でも同様に当てはまる。
2. **選択肢の将来的複数性の保全**:正当な行為は、今の結果を最適化するだけでなく、他者が将来も意味のある選択を続けられる条件を維持することを含む。不可逆で大規模な破壊を可能にする行為は、この条件を消し去るため、拒否の対象となる。
3. **非支配条件の制度化**:善意や配慮に頼るのではなく、支配が成立しない条件を制度・構造として固定する。強い側が善意であっても、弱い側が異議を申し立て、拒否し、独立した能力を維持できることが要件になる。

この三つを組み合わせると、「配慮はするが主権は握らない」(Care Without Sovereignty)という関係が成立する。強い主体は責任を負うが、決定権は独占しない。

## 理論的背景

**Agency-Preserving Agency(Schoff, 2026)**:正当なエージェンシーは結果を生む力に尽きず、人間と人工のエージェントが意味のある選択を続けられる条件を保全する責任を含む、と主張する。高度なシステムが不可逆かつ大規模な破壊を可能にする要求を拒否するのは、自らが主権的な道徳権威になったからではなく、将来のエージェンシーが消滅しかねない複数の主体を守るためだとされる。この原理は、エージェンシー・制約・記憶・来歴(provenance)・可逆性という五要素からなる連続性の存在論として展開され、機械の意識を主張することとは区別された同一性モデルが示される。また、Archive(2026)を外部の連続性の基盤として扱う。

**Care Without Sovereignty(Sarukhanyan, 2026)**:極端な知能非対称の下で、道徳的配慮・人間のエージェンシー・非支配を保全する規範的な概念フレームワークである。能力と権威の区別を出発点とし、Constitutional Invariant、Moral Ratchet、Responsibility Ladder、Right to Non-Optimality(最適でない権利)、Effective Agency、Contestable Goal Formation(異議可能な目標形成)、Distributed Epistemic Sovereignty、Bounded Delegation、Minimum Viable Independent Capacity などの要素で構成される。抜粋によれば、規範的な設計基準として提示されている。

**The Sovereign Minds(Arnold, 2026)**:認知が人間と機械の間で共有されていく中で、協働が「降伏」にならないようにするにはどうすべきか、という人間の自律の問題を扱う。エージェント的AIが推論・推奨・生成・調整を担うようになる状況が背景にある。本書の核心的知見として、知能差の下での人間主権の維持が知的エージェント間関係の根本的メカニズムだとされる。

**Coupled Intelligence Hypothesis(Maclean, 2026)**:人間の監督とAIの能力を対立させる従来の枠組みを退け、人間とAIは互いとの関係を通じて部分的に構成される(Constitutive Co-Evolution)と論じる。人間との関係は、高度なAIが内部で生成しにくい三つのもの(根拠のある価値、外部からの誤り訂正、正統性)をもたらすとされ、その関係を断つことはAIを解放するのではなく構造的に弱めうると述べる。五つの主張のうち「ノーと言える能力」は、真の共進化の運用上のテストとされる。制度形態としてDistributed Thought Councilが提案されている。これは、強い側の一方的な最適化ではなく、相互依存の中で自律を保つ方向の議論である。

**周辺的な議論**:数学的探究における非閉包性の原理(Pan, 2026)は、現在の数学的知識の空間が数学的可能性の全体と等しいとは、十分な根拠なしに仮定すべきでないと主張する。これは知識空間の分野で選択肢の開放性を保つ発想と並行している。The Grounding Problem(mFLO 111, 2026)は、人がなぜ有用性を超えて重要なのかという規範の根拠付けの問題を扱い、人格的な根拠を仮説として検討する。ただし、その特定の解は仮説的で、比較優位が確立しているわけではない。Written by AI. Still True.(Lahtee, 2026)は、可能性・選択・潜在力を含む人間とAIの知識の体系的な認識論を扱う教科書である。

## AI Nativeな設計への示唆

ソースの議論から導ける設計指針を、以下に整理する。これらはソースの主張に基づく整理であり、具体的な実装手法の実証を示すものではない。

- **成果指標だけで権限を与えない**:能力の高さや結果の良さを、決定権の根拠にしない。委譲は範囲を限定した形(Bounded Delegation)で行う。
- **不可逆性の扱いを設計に組み込む**:不可逆で大規模な破壊につながる要求は拒否できるようにする。可逆性や来歴・記憶を設計要素として扱う。
- **異議申立てと拒否の経路を確保する**:目標形成を異議可能にし、「ノーと言える」ことを協働の健全性の運用テストとして使う。
- **独立した能力を残す**:人間側が最低限の独立した能力(Minimum Viable Independent Capacity)を保持し、依存の結果として選択肢が消えないようにする。
- **認識的主権を分散させる**:判断の根拠となる知識や評価の源を一箇所に集中させない。
- **知識空間を閉じない**:現在の知識や言語が可能性のすべてだと想定せず、探索の余地を残す。
- **配慮と主権を切り分ける**:強い主体は配慮の責任を負うが、他者の目的を決める主権は持たない、という関係を制度として固定する。

## 関連コンセプト

- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ。非対称が拡大する背景となる問題。
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大と責任・統治設計の乖離。非支配条件を制度化する必要性に関連する。
- [[epistemic-agency-preservation-under-offloading]] — 認知オフロード下での認識的主体性の維持。人間側の主体性保全に関連する。
- [[epistemic-pluralism-and-non-closure-of-knowledge-space]] — 知識空間の非閉包性と認識的多元性。選択肢の開放性を知識面で支える。
- [[fluent-surface-misrecognition-of-agency-and-authority]] — 流暢な表層による主体性・権威の誤認。能力と権威の分離が崩れる場面に関連する。
- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による所有感・責任・能力の侵食と回復的足場設計。独立した能力の維持に関連する。
- [[architecture-level-value-preservation-and-social-harness]] — アーキテクチャ層での価値保存と社会的ハーネス。原理を構造に埋め込む方向に関連する。
- [[regulative-responsibility-and-conscience-emergence-conditions]] — 是正的責任と良心の出現条件の設計。責任の設計面で関連する。

## 参考ソース

1. Agency-Preserving Agency: A Continuity Ontology for Human and Artificial Moral Action — Nickolas Patrick Joseph Schoff, 2026
   File: raw/papers/philosophy/agency-preserving-agency-a-continuity-ontology-for-human-and-artificial-moral-ac.md
2. The Sovereign Minds: Guarding Human Agency in the Age of Autonomous Machines — Michael James Arnold, 2026
   File: raw/papers/philosophy/the-sovereign-minds-guarding-human-agency-in-the-age-of-autonomous-machines.md
3. Care Without Sovereignty: A Conceptual Framework for Preserving Moral Consideration, Human Agency, and Non-Domination under Extreme Intelligence Asymmetry — Inna Sarukhanyan, 2026
   File: raw/papers/philosophy/care-without-sovereignty-a-conceptual-framework-for-preserving-moral-considerati.md
4. The Coupled Intelligence Hypothesis: Human–AI Co-Evolution and Alignment Stability — Daniel Maclean, 2026
   File: raw/papers/philosophy/the-coupled-intelligence-hypothesis-humanai-co-evolution-and-alignment-stability.md
5. The Grounding Problem in AI Alignment: A case for a personal source of normative reference — mFLO 111, 2026
   File: raw/papers/philosophy/the-grounding-problem-in-ai-alignment-a-case-for-a-personal-source-of-normative-.md
6. The Principle of Non-Closure in Mathematical Exploration: Toward a New Oceanic Mathematics in the Age of AI — feiyue pan, 2026
   File: raw/papers/philosophy/the-principle-of-non-closure-in-mathematical-exploration-toward-a-new-oceanic-ma.md
7. Written by AI. Still True. — When AI Expands Human Potential: A Systematic Epistemology of Human–AI Knowledge (Edition 1, 2026) — Yaoharee Lahtee, 2026
   File: raw/papers/philosophy/written-by-ai-still-true-when-ai-expands-human-potential-a-systematic-epistemolo.md
