# 形式化と現実のギャップによる制度的脆弱性の増幅

## 概要

測定・標準化・形式表現は、現実の一部しか捉えることができない。この「形式化と現実のギャップ」は、人間による運用の時代にも存在していたが、しばしば現場の判断や補完的な実務によって吸収されてきた。自動化はこの吸収を置き換え、あるいは不可視にすることで、ギャップに潜んでいた既存の制度的脆弱性を拡大する。さらに、測定可能な指標は測定されるという事実そのものによって社会的権威を獲得し、測れないものは制度の視界から外れていく。

本概念は、以下の三つの中核メカニズムから成る。

1. 形式表現と現実の乖離(何をどう表現しても取りこぼしが生じる)
2. 測定可能性による権威の構成(測れるものが正統性を持つ)
3. 制度的脆弱性の増幅(自動化がギャップ内の弱点を拡大する)

AI Nativeな社会設計では、意思決定・評価・監査の多くが形式表現の上で自動的に行われる。このため、「形式化が何を落としているか」を設計の第一級の対象として扱うことが、技術進化に依存しない不変の要請となる。

## メカニズム

以下の構造は、対象が人間・AI・組織・技術のいずれであっても成立する。

**1. 表現の縮約(Representation Reduction)**
あらゆる制度は、現実を分類・指標・スコア・記録といった形式に変換して扱う。この変換は必ず情報を落とす。対象が個人でも、組織でも、AIモデルの挙動でも、「形式が扱える次元」は「現実の次元」より少ない。

**2. 測定可能性による権威の構成**
一度形式化された指標は、比較・順位づけ・資源配分に使われ、それ自体が権威を持つ。この段階で、指標は現実の近似ではなく、現実を評価する基準として機能し始める。測れないものは、価値がないものとして扱われるか、単に見えなくなる。

**3. 不可視の補償の存在**
形式と現実のギャップは、多くの場合、人間の文脈判断や非公式な調整によって埋められている。これらは制度上の記録に残らず、評価もされない。

**4. 自動化による補償の除去と脆弱性の増幅**
自動化は形式表現に忠実に動作するため、不可視の補償を担う余地を減らす。結果として、それまで補償されていた弱点(ギャップ)が直接的な帰結となって現れ、制度の強化ループ(既存の偏りや盲点の再生産)を通じて拡大する。

**5. 観測可能性の喪失**
自動化の対象が生成AIやエージェント型システムになると、システム境界の安定性や直接観測可能性といった従来のリスク管理の前提が崩れ、ギャップ自体を検知しにくくなる。

## 理論的背景

**制度による表現の縮約と五つの相互作用メカニズム(Khan, 2026)**
制度システムが人間の現実を形式表現、優先順位、組織的対応へと変換する過程を概念的・学際的に分析し、表現の縮約(representational reduction)、優先順位の整合、解決と帰結の断絶、適応的補償、制度的強化という五つの相互作用メカニズムを提示している。中心的な主張は、問題は自動化そのものではなく、それが設計・統治・実装される制度的条件にあるという点である。この分析を基に、重要な人間的貢献でありながら制度に見えにくいものを指す「Invisible Institutional Contributions」の概念も展開されている。

**測定可能性が権威を生む歴史的構成(Olier, 2026)**
知能を自然種ではなく、歴史的・文化的に生産された概念として捉える。近代的合理性、心理測定、標準化テストからAIへと至る系譜を辿り、特定の行動や能力が「知的」と分類され、測定可能にされ、その測定が社会的・政治的な力を獲得する過程を示している。AIは、この評価インフラを再生産し変形するものとして位置づけられる。

**分類問題の次元制約(Toma & Yusupov, 2026)**
医療AIについて、確率的言語モデルと決定論的分類器を区別し、多次元の組合せモデルで診断の完全な網羅に必要な条件を算出している。サブスペシャリティ水準の臨床的粒度では、5万〜15万の個別タスク用分類器が必要と推定され、保守的な集計推計(4,500〜18,750の二値分類器)は、サブタイプ、重症度、時間的変異、人口統計的層別化、機器差による乗算的な拡大を反映していないと論じる。承認済みの機器はこの臨床空間の1%未満しかカバーしていない。集団統計から個別ケアへの形式的ギャップの大きさを定量的に示す例である。

**データ量より質と理論的枠組みが上限を決める(Stein et al., 2026)**
精神医学のビッグデータ研究のレビューで、大規模データセットは重要な到達点である一方、サンプルサイズだけでは十分ではないことを論じている。データの質、方法論的厳密性、臨床的関連性が課題として挙げられ、形式化されたデータが現実をどこまで代表しうるかという限界を示している。

**従来のリスク管理の前提の崩れ(Godlove & Buchanan, 2026)**
生成AIやエージェント型AIは、従来のモデルリスク管理が前提とする安定したシステム境界、直接的な観測可能性、制御可能な変更、モデル開発証拠へのアクセスに挑戦すると指摘する。一方で、インベントリ、重要性評価、独立検証、モニタリング、文書化、実効的な異議申立て、説明責任あるガバナンスといったMRMの目的自体は依然として必要であるとし、AIガバナンス、リスク管理などを結ぶ統合的な保証アーキテクチャを提案している。

**比較による見えなかった性質の可視化(Widi, 2026)**
算術を「道と記憶」の写像として捉え、平方数や三角数などの複数のランドマーク体系を比較することで、単一の表現では見えない性質(合成数であることと因数の復元)が可視化されることを示す。単一表現は性質を隠しうるが、複数表現の比較がそれを露わにするという含意がある。

**認識的境界と更新権限の分離(Kunato Core v3, 2026)**
受け入れられた知識を保護された認識状態として扱い、命題の生成と状態を変更する権限を分離する形式的枠組みである。「正当な根拠がなければ認識状態の遷移は起こらない」という規則を掲げ、言語的表現可能性とモデル論的構成可能性を区別する。形式の内部で何が許容されるかを明示的に管理する試みとして参照できる。

## AI Nativeな設計への示唆

1. **形式化の欠落を設計対象にする**: 指標・スキーマ・分類体系を設計する際に、「何を捨てたか」を明示的に文書化し、レビュー対象とする。
2. **不可視の貢献を可視化する**: 自動化の導入前に、現行の運用が非公式な補償にどれだけ依存しているかを棚卸しする。補償を担う人間の判断を、除去せず制度内に位置づける。
3. **複数の表現による比較を組み込む**: 単一の指標やモデルに依存せず、異なる形式表現を並置して、単一表現が隠す性質を検出する。
4. **測定可能性への過剰な権威付与を避ける**: 指標を意思決定の唯一の根拠にせず、測れない要素のための判断経路や異議申立ての手段を確保する。
5. **カバレッジの限界を明示する**: 医療AIの例のように、システムが実際に扱える空間の割合を明示し、範囲外での適用を制度的に制限する。
6. **データ量ではなく質と理論的統一を重視する**: 大規模化が代表性を保証するとは限らないため、方法論的厳密性を評価基準に含める。
7. **保証機能を継続させる**: 観測可能性が低下しても、独立検証、モニタリング、実効的な異議申立て、説明責任ある統治といった機能は維持し、AI向けに再設計する。
8. **状態変更の権限を分離する**: 生成・提案と、制度上の状態を変更する権限を分け、根拠のない遷移を許さない。

## 関連コンセプト

- [[technology-as-amplifier-of-institutional-tension-and-capability-gap]] — 技術が既存の制度的緊張を増幅する点で直接に対応する。
- [[formal-rule-shadow-labor-accountability-gap]] — 形式的規則と不可視の実務のギャップという同型の構造を扱う。
- [[judgment-residual-and-accountability-gap]] — 形式化で残る判断の残余と説明責任の問題。
- [[capability-transparency-gap-and-trust-loss]] — 観測可能性・透明性の喪失と信頼の関係。
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大に対する統治設計の遅れ。
- [[capability-outpacing-control-gap]] — 能力が制御を上回る構造。
- [[institutional-readiness-gates-technology-diffusion]] — 制度側の条件が技術の帰結を規定する点で共通する。
- [[generative-gap-and-representation-mediated-selfhood]] — 表象と実在の乖離という関連する問題。

## 参考ソース

1. Toma, M., Yusupov, D. (2026). *Perspectives on the Limits and Clinical Alignment of Medical AI from Population Statistics to Individual Care*. `raw/papers/psychology/perspectives-on-the-limits-and-clinical-alignment-of-medical-ai-from-population-.md`
2. Khan, T. (2026). *Beyond Automation: Reimagining Human-Centered Systems for AI-Mediated Institutions*. `raw/papers/psychology/beyond-automation-reimagining-human-centered-systems-for-ai-mediated-institution.md`
3. Godlove, T., Buchanan, J. (2026). *From Model Risk Management to AI Assurance: Integrating AI Risk Management, Independent Validation, and AI Auditing for Generative and Agentic AI*. `raw/papers/psychology/from-model-risk-management-to-ai-assurance-integrating-ai-risk-management-indepe.md`
4. Stein, D. J., Kessler, R. C., Torous, J. B., Garavan, H. P., van den Heuvel, O. A. (2026). *Big data and psychiatry: advances, constraints and future directions.* `raw/papers/psychology/big-data-and-psychiatry-advances-constraints-and-future-directions.md`
5. Olier, J. S. (2026). *On (artificial) intelligence: from a concept of measurable human ability to automated evaluative order*. `raw/papers/religious_studies/on-artificial-intelligence-from-a-concept-of-measurable-human-ability-to-automat.md`
6. Widi, B. (2026). *Who Saw the Atlas? Arithmetic as Atlas and Human-AI Collaboration*. `raw/papers/psychology/who-saw-the-atlas-arithmetic-as-atlas-and-human-ai-collaboration.md`
7. Scheduler4861 (2026). *久那斗 Kunato Core Ver.3.0.0: Truth-Preserving Deliberation, Refutation Persistence, and Epistemic Boundary Control*. `raw/papers/religious_studies/久那斗-kunato-core-ver300-truth-preserving-deliberation-refutation-persistence-and-.md`
