# 局面別支援設計と早期収束の回避

## 概要

創発的・探索的なプロセスは、発散(探索)から収束(深化・実装)へと局面を移りながら進む。局面ごとに必要な支援は異なる。発散期には前提を揺さぶり別の見方を示す支援が要り、収束期には実現可能性を検証し実行を加速する支援が要る。

局面を区別せず一様な支援を与えると、関与者の認知状態の変化と支援が食い違う。その結果、支援への過度依存と早期収束が起き、アイデアの多様性が失われる。ソース[2]はこの状況を「一様なAI支援は革新者の変化する認知状態と不整合であり、過度依存と早期収束を促してアイデアの多様性を損なう」と述べている。

AI Nativeな社会設計では、AIが日常的に思考や意思決定の場へ組み込まれる。そのため、AIをいつ、どの形で関与させるかという局面設計が、成果の質と人間の能力の維持の両方を左右する。本概念は、AIの性能や利用頻度を高めることよりも、支援の質を局面に合わせて切り替えることを設計の中心に置く。

## メカニズム

以下の構造は、支援の主体(AI、人間の助言者、組織の制度、技術ツール)を入れ替えても成り立つ。

1. **局面依存的な認知状態**:探索期の関与者は可能性を広げる状態にあり、深化期の関与者は選択肢を絞って実行する状態にある。必要な支援もこれに応じて変わる。
2. **探索と深化のトレードオフ**:限られた注意や資源のもとで、探索(新しい可能性の生成)と深化(既存案の洗練・実行)は同時に最大化できない。この選択は構造的なトレードオフとして現れる。
3. **一様な支援による早期収束**:収束を促す支援(効率化、即時の解の提示)を探索期にも与え続けると、選択肢が十分に広がる前に一つの案へ収束する。その結果、多様性が失われる。
4. **過度依存の連鎖**:局面に合わない支援は、関与者が自ら考える機会を減らし、支援への依存を強める。
5. **局面適合的な切り替え**:解決策は、常に高水準の探索と深化を両立させる静的な状態ではない。局面に応じて支援の性格を切り替える動的な適合である。

## 理論的背景

**局面特化型マルチエージェントシステム(ソース[2])**:Herathは、探索(発散)と実装(収束)で異なるAI支援を行う人間-AIイノベーションシステムを提案した。アイデア創出支援は前提を問い直し、代替的なフレーミングを提示して発散的探索を促す。実装用チャットボットは実現可能性を検証し、収束的な実行を加速する。2つのイノベーション系ハッカソンでのパイロットでは、人間の思考に沿った支援がアイデア創出期の多様性を保ち、実装期には実現可能なプロトタイプへの効率的な収束を助けることが示された。大規模なフィールド実験は今後の計画とされている。

**二経路・二時間軸理論(ソース[1])**:Baiは、生成AIの探索的利用と活用的(深化的)利用が異なる形の従業員創造性と結びつくという既存の知見を出発点に、次の3点を論じた。
- 知識統合には拡張的モードと統合的モードがある。
- 静的な「高探索・高活用」の両立ではなく、局面に適合した切り替えが重要である。
- メタ認知は、即時の知識統合と長期的な能力形成の双方を統御する制御機構である。

さらに、短期的な能力拡張が、長期的には能力の蓄積にも能力の代替にも発展し得ると論じている。これは局面設計が短期の成果だけでなく能力形成の軌道にも影響することを示唆する。

**批判的思考との関係(ソース[3])**:Abdurasulovaは、AIは利用の仕方によって批判的思考の促進要因にも制約要因にもなると論じる。着目する要素は、認知過程、メタ認知、省察、情報評価、意思決定の仕組みである。支援の効果が設計と使い方に依存するという点で、局面別設計の必要性と整合する。

**補足的な視点(ソース[4][5])**:Majumdarは、AIが定型的で狭いタスクを自動化するほど、複雑なシステムを統合し批判的判断を下す汎用的な人材(「アーキテクト」)の価値が高まると論じる。de Jesusらは、AIを要求と資源を同時にもたらす職務特性として捉える。AIの効果は従業員の認知や組織の支援などの文脈条件に左右され、投資や生産性向上が持続的な革新行動に結びつかないことがあるという。これらは局面別支援を直接扱うものではなく、支援の効果が文脈依存であることを示す周辺的な知見である。

## AI Nativeな設計への示唆

- **局面を明示的にモデル化する**:探索と収束の局面を区別し、各局面の目的(多様性の確保、または実現可能性の検証と実行)に応じてAIの振る舞いを変える。
- **探索期のAIは答えより問いを返す**:前提の検証や代替フレーミングの提示を重視し、早期に解を確定させない。
- **収束期のAIは実行を支援する**:実現可能性の検証と実行の加速に絞り、探索期とは別の役割・エージェントとして設計する。
- **多様性を観測指標にする**:アイデアの多様性を、局面移行の判断や支援の妥当性評価に使う。
- **メタ認知を支える**:利用者が今どの局面にいるかを自覚し、AIの提案を批判的に評価できるようにする。局面の切り替えを利用者自身が制御できることが望ましい。
- **短期成果と能力形成を分けて評価する**:短期的な生産性だけで評価すると、能力の代替が進む可能性を見落とす。
- **局面判定の自動化には慎重になる**:ソースは局面別支援の有効性を示すが、局面判定の方法自体は扱っていない。判定をAIに任せる場合は、その妥当性を別途検証する必要がある。

## 関連コンセプト

- [[support-induced-skill-substitution-loop]] — 支援が能力形成の機会を奪うループ。局面に合わない支援が生むリスクと重なる。
- [[fluent-output-capability-decoupling]] — 流暢な成果と内在的能力の乖離。過度依存の帰結として関連する。
- [[threshold-phase-transition-in-technology-dependence]] — 技術依存が閾値を超えて相転移する力学。
- [[ai-decision-support-systems]] — 意思決定支援としてAIを設計する際の基盤的な視点。
- [[ai-in-educational-support-systems]] — 学習の局面に応じた支援設計への応用領域。
- [[ai-decision-support-in-education]] — 教育場面における意思決定支援。
- [[capability-perception-and-responsibility-diffusion-in-trust]] — AIの能力知覚と責任の転嫁。

## 参考ソース

1. Exploring or Exploiting Generative AI? A Dual-Path, Dual-Horizon Theory of Employee Incremental and Radical Creativity — Jun Bai (2026)
   File: raw/papers/cognitive_science/exploring-or-exploiting-generative-ai-a-dual-path-dual-horizon-theory-of-employe.md
2. Should Artificial Intelligence Align With Human Thinking In Innovation Processes? — Savindu Herath (2026)
   File: raw/papers/complexity_science/should-artificial-intelligence-align-with-human-thinking-in-innovation-processes.md
3. PSYCHOLOGICAL CHARACTERISTICS OF THE RELATIONSHIP BETWEEN ARTIFICIAL INTELLIGENCE AND CRITICAL THINKING — Mehrigul Abdurasulova (2026)
   File: raw/papers/complexity_science/psychological-characteristics-of-the-relationship-between-artificial-intelligenc.md
4. Management Talks – Part 3: Artificial Intelligence, Human Adaptability, and the Future of Decision-Making — Partha Majumdar (2026)
   File: raw/papers/complexity_science/management-talks-part-3-artificial-intelligence-human-adaptability-and-the-futur.md
5. From Anxiety to Advantage: A Multi-Level Framework for AI-Driven Performance — Jairo de Jesus, Jayabhushan Praneeth Pallepogu, Reza Vaezi (2026)
   File: raw/papers/complexity_science/from-anxiety-to-advantage-a-multi-level-framework-for-ai-driven-performance.md
