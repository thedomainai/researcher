# 形式的規則と不可視の実務のあいだの説明責任ギャップ

## 概要

説明責任ギャップ(Accountability Gap)とは、**法的責任が形式上の主体(行政機関、公職者、名義上の運営者)に置かれる一方で、実際の決定がコード設計、不可視の労働、分散した実務の中で生産される**という構造的乖離を指す。Ponce de León Solís(2026)は、これを「形式的な法的責任と、自動化された福祉判断が生産・維持・争われる実際の条件とのあいだの構造的断絶」として論じている。

この乖離は、手続的保護(通知、説明、異議申立て、人間による介入)を実質的に空洞化させ、権力の非対称を固定化する。AI Nativeな社会設計では、意思決定の多くがモデル、パイプライン、運用者、委託先に分散する。そのため、「誰が責任を負うと書かれているか」と「誰が実際に決めているか」の差は、例外ではなく標準状態になりやすい。この概念は、責任設計を規範や宣言の水準に留めず、アーキテクチャの水準で扱う必要性を示す。

## メカニズム

対象が人間、組織、AI、技術のいずれであっても成立する構造として、次の三段階に整理できる。

1. **形式と実態の乖離**
   責任は法令や組織図上の主体に割り当てられる。しかし実際の判断材料や結果は、アルゴリズム、行政ルールの実装、データ整備やシステム保守といった労働の組み合わせから生まれる。これらは法的にも制度的にも認識されにくい。
2. **権力の官吏から設計者への移転**
   裁量が、個々の官吏の判断から、システムを設計・実装する開発者や設計上の選択へ移る。だが従来の法的統制は官吏の行為を想定しており、設計者の選択には及びにくい。
3. **ブラックボックス化による異議申立ての無効化**
   決定の根拠が不透明になると、対象者は何を争えばよいか特定できない。予測や評価を受ける個人が異議を唱えにくい状況は、権力の非対称を強める。

この三段階は循環する。可視性が低いほど責任を追及しにくくなり、追及されないほど設計上の可視化の圧力も生じにくい。

## 理論的背景

**自動化福祉と「影のデジタル労働」。** Ponce de León Solís(2026)は、チリの社会法的・制度的状況を事例に、自動化福祉がアルゴリズム、行政ルール、法的にも制度的にも不可視なデジタル労働の複合体に依存していると分析する。この不可視労働を「影のデジタル労働(shadow digital labor)」と呼び、現代の福祉ガバナンスの構成要素でありながら承認されていないものと位置づける。さらに、「digital-by-default」の福祉アーキテクチャがGDPR型のデータ保護法(法律第21.719号)と衝突し、コンプライアンス・リスクの非対称な配分を生むことを示している。同論文は、自動化の包括的理論の提示を目的とはしていない。

**手続的侵食。** Haryanto and Sekti(2026)は、人間中心の官僚制からデータ基盤型ガバナンスへの転換を扱い、自動化された意思決定が「アルゴリズム的手続的侵食」を引き起こすと論じる。従来の法的保護はブラックボックスの不透明性に対処できず、国家権力は官吏からコード開発者へ再編される。対応として「Accountability by Design」を提案し、通知、理解可能な説明、人間の介入といった手続的権利をAIアーキテクチャに直接組み込むこと、また独立したアルゴリズム監査を司法上の証拠として活用することを主張する。

**警察活動における非対称性。** Dujovski(2026)は、予測的警察活動、顔認識、自動リスク評価を取り上げ、説明責任、透明性、バイアス、意思決定の不透明性が法執行機関の正統性と信頼性に影響すると分析する。

**非委任原則。** El-Rakhawi(2026)は、裁量的権限をブラックボックス・アルゴリズムへ委任しないという原則を提示し、AI主導の行政決定には人間による承認を求めることで、憲法上の説明責任と法の支配を保つべきだとする。

**情報公開制度の限界。** Saikiaら(2026)のレビューは、RTI/FOI枠組みが、アルゴリズムの不透明性、独占的システム、AI生成記録の曖昧さといった課題に直面していると指摘する。異議申立ての前提となる情報アクセスの経路が、現行制度では十分に機能しない可能性がある。

**医療AIにおける関係的視点。** Misir(2026)は、医療AIの倫理が公平性や透明性を技術標準として扱い、社会政治的帰結を見落としがちだと論じ、関心の中心をアルゴリズムのブラックボックスから医療の「関係的ネットワーク」へ移すことを提案する。また現行の枠組みがソフトローや自主的原則に依存し、拘束力を欠く点も課題とされる。この視点は、責任の所在を単一の技術的部品ではなく関係の網の中で捉える必要を示唆する。

## AI Nativeな設計への示唆

- **責任の実態マッピング**:名義上の責任主体だけでなく、データ整備、ルール実装、モデル運用、保守に関わる不可視の労働と設計判断を、責任配置の対象として可視化する。
- **手続的権利のアーキテクチャ化**:通知、理解可能な説明、人間の介入を後付けの運用ではなく、システム設計の必須要素とする(Accountability by Design)。
- **裁量の非委任領域の明示**:重大な裁量判断は人間による承認を要件とし、ブラックボックスへの全面委任を避ける。
- **独立監査と証拠化**:外部のアルゴリズム監査を、異議申立てや司法審査で使える証拠として位置づける。
- **リスク配分の点検**:デジタル・バイ・デフォルトの設計が、コンプライアンス・リスクを個人や現場に偏って負わせていないか確認する。
- **情報アクセス制度の更新**:情報公開制度が、アルゴリズムやAI生成記録に対して実効性を持つよう見直す。

## 関連コンセプト

- [[judgment-residual-and-accountability-gap]]:人間に残る判断領域と説明責任ギャップの関係
- [[architectural-locus-of-accountability]]:アーキテクチャ配置による責任の固定
- [[visible-commitment-invisible-implementation-gap]]:可視的な宣言と不可視な実装の乖離
- [[principle-to-practice-gap-and-layered-responsibility-allocation]]:原則と実装の乖離、多層的な責任配置
- [[principles-to-practice-legitimacy-gap]]:原則から実践への翻訳と正当性
- [[governance-gap-between-capability-scaling-and-accountability]]:能力拡大と統治の乖離
- [[accountability-requires-ontological-conditions]]:責任帰属の条件
- [[ai-accountability-attribution]]:AIシステムの責任帰属
- [[multi-actor-value-chain-liability-reallocation]]:多主体連鎖における責任配分
- [[capability-transparency-gap-and-trust-loss]]:透明性の欠如と信頼の喪失

## 参考ソース

1. Viviana Ponce de León Solís (2026)「The accountability gap: Shadow digital labor and the crisis of accountability in automated welfare」
   File: raw/papers/law/the-accountability-gap-shadow-digital-labor-and-the-crisis-of-accountability-in-.md
2. Nikola Dujovski (2026)「ARTIFICIAL INTELLIGENCE IN THE POLICE INNOVATION AND ETHICAL USE -」
   File: raw/papers/law/artificial-intelligence-in-the-police-innovation-and-ethical-use.md
3. Muhamad Fajri Permana Haryanto, Binastya Anggara Sekti (2026)「Algorithmic Accountability and Protection of Fair Procedure Rights in AI-Driven Public Administration」
   File: raw/papers/law/algorithmic-accountability-and-protection-of-fair-procedure-rights-in-ai-driven-.md
4. Lohit Kumar Saikia, Pranita Choudhury, Nandini Saikia (2026)「AI, DEEPFAKES, AND DEMOCRATIC ACCOUNTABILITY: THE ROLE OF RTI LAWS」
   File: raw/papers/law/ai-deepfakes-and-democratic-accountability-the-role-of-rti-laws.md
5. Prem Misir (2026)「Ethics and Governance of AI in Healthcare」
   File: raw/papers/law/ethics-and-governance-of-ai-in-healthcare.md
6. Prem Misir (2026)「The Sociology of AI Ethical Framework for Healthcare」
   File: raw/papers/law/the-sociology-of-ai-ethical-framework-for-healthcare.md
7. N. Vithya, N. Subha, S. Pathur Nisha, A. Balthilak (2026)「Responsible AI in healthcare: Navigating ethics and governance challenges」
   File: raw/papers/law/responsible-ai-in-healthcare-navigating-ethics-and-governance-challenges.md
8. mohamed kamal arafa el-rakhawi (2026)「THE EL-RAKHAWI UNIFIED ANALYTICAL FRAMEWORK FOR CONSTITUTIONAL COMPETENCE A Comparative Critical Study Across Legal Systems」
   File: raw/papers/law/the-el-rakhawi-unified-analytical-framework-for-constitutional-competence-a-comp.md
