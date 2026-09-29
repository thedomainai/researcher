# 多主体価値連鎖における責任配分の再構成

## 概要

多主体価値連鎖における責任配分の再構成とは、AIのような不透明で適応的なシステムが複数の関与者にまたがって働くとき、単一の過失基準では責任を適切に割り当てられないため、責任と保険を制御・リスク・証拠・データといった軸で組み替える必要があるという原理である。

ソース群に共通する認識は、AIに関する責任が「AIそのものの責任」ではなく、AIの開発・展開・利用に関わる主体の責任だという点にある(ソース[3])。従来の過失責任、専門職責任、製品責任、契約責任は引き続き有効だが、次の五つの特性によって負荷がかかる。

- 不透明性
- 適応的挙動
- 多主体の価値連鎖
- 証拠の非対称性
- 相関した損失

AI Nativeな社会設計では、意思決定と実行が人間・AI・組織・インフラに分散する。誰が何を制御し、誰が証拠を持ち、誰がリスクを吸収できるかを設計段階で明示しなければ、責任の空白や希薄化が制度的に固定化される。

## メカニズム

この原理は、対象が人間・AI・組織・技術のいずれであっても成り立つ構造として整理できる。

1. **情報の非対称性**:被害者や監督者は、システム内部の挙動や意思決定の根拠にアクセスできない。証拠は運用者や開発者の側に偏在する。ソース[3]は「証明の非対称性」を負荷要因に挙げ、ソース[2]は証拠生成の欠陥を説明責任ギャップの一つに挙げている。
2. **因果関係の不確定性**:損害が直接の人間の行為だけでは説明できなくなり(ソース[4])、開発者・提供者・利用者・データ提供者のどこに因果を帰属すべきかが曖昧になる。
3. **責任軸の移動**:過失の有無という単一の基準から、制御能力、専門性、リスク予防能力に責任を対応させる方向へ移る(ソース[3])。ソース[4]は制御・リスク・証拠のモデルを提示し、ソース[1]はデータ中心の責任という軸を提案する。
4. **リスクの内部化と保険化**:責任保険は補償手段であると同時にガバナンスの道具でもある。ただし、法的に不確実なリスク、帰属が困難なリスク、システム的に相関するリスクでは限界がある(ソース[3])。
5. **分散した責任の断片化**:臨床・技術・規制といった複数層に責任が分散すると、単一の説明責任モデルでは断片的なギャップが避けられない(ソース[2])。

## 理論的背景

**データ中心の責任(ソース[1])**:Cannarsaは、急速に広がるAIが提起する未解決の論点として、責任の根拠、複数の生産者・開発者間の責任配分、非物質的損害の補償などを挙げる。そのうえで、従来の製品責任や不法行為法の再検討を、EUレベルで単一の枠組みを設ける機会と捉え、データを軸にした責任への転換を提案している。

**医療分野の説明責任の生態系(ソース[2])**:英国医療分野のAIを対象に、Novelliらの四層モデル(遵守・報告・監督・執行)を用いて分析している。規制ツールは多様だが断片化しており、証拠生成、透明性、帰属、制度面での相互に連関した説明責任ギャップが生じていると指摘する。

**校正された責任枠組みと保険(ソース[3])**:Wangは英国法の下で、AIへの法人格の付与も一律の厳格責任も退け、制御・専門性・リスク予防能力に責任を整合させる枠組みを支持する。改正EU製品責任指令や新たなAI保険商品の分析を通じて、責任ルール・保険・ガバナンスの協調的な発展を論じる。

**制御・リスク・証拠モデル(ソース[4])**:インドネシア民法の枠組みが、AIが引き起こしまたは媒介した損害に十分対応できるかを検討し、過失・因果関係・証拠責任を再構成するモデルを提示している。因果の不確定性が露呈するため、現行枠組みの再構成が必要だとされる。

**取締役の監督義務(ソース[6])**:Caremark法理を用いて、取締役会にはミッションクリティカルなAIシステムを積極的に監督する義務があると論じる。一方で、従来の「読み取れる危険信号」と異なり、AIは人間が読める説明なしに出力を生成するため、取締役会がクリーンなコンプライアンス報告を受け取り続ける構造的問題があると指摘する。

**データ主権の非対称性(ソース[5])**:ラテンアメリカでの分析は、分散型識別子、検証可能な資格情報、ゼロ知識証明といった技術が、AI由来のプライバシーリスクに対する実践的インフラになりうるかを検討する。情報コントロール権に関わる非対称性への対処を、技術基盤の側から扱うものである。

## AI Nativeな設計への示唆

- **単一基準に頼らない**:過失、製品欠陥、契約違反を場面ごとに使い分けつつ、制御・専門性・予防能力に沿って責任を割り当てる層状の設計にする。
- **証拠を設計に組み込む**:ログ、説明、監視データを生成・保全する責務を、制御能力を持つ主体に課す。証拠の偏在を放置しない。
- **不透明性を前提にした監督**:クリーンな報告が安全を意味しないと想定し、独立した検証や監査の経路を設ける。
- **責任の空白を防ぐ連結**:臨床・技術・規制のように層をまたぐ責任が断片化しないよう、層間の帰属と報告の接続点を明示する。
- **保険を統制の道具として使う**:保険条件やリスク評価を通じて予防行動を促す。ただし、相関損失や帰属困難なリスクは保険だけで吸収できないため、ルールとの協調が要る。
- **データの管理権を組み込む**:データを責任の軸の一つとし、個人が情報の管理権を保てる技術基盤を検討する。

## 関連コンセプト

- [[ai-legal-liability-personhood]] — AIの法人格を退け、開発・展開・利用の責任として捉える論点と直結する
- [[algorithmic-black-box-auditing]] — 不透明なシステムの監査と説明責任の不確実性
- [[responsibility-dilution-and-moral-status-symmetry]] — 多主体での責任の希薄化
- [[functional-attribution-of-intent-to-accountable-principals]] — 責任主体への遡及構造
- [[formal-rule-shadow-labor-accountability-gap]] — 形式と実態の間の説明責任ギャップ
- [[incentive-driven-deferral-and-asymmetry]] — 情報非対称の固定化
- [[multi-stakeholder-value-dynamics]] — 複数の利害関係者間の価値動態
- [[boundary-invariant-first-architecture-and-modular-governance]] — 用途別のモジュール型統治

## 参考ソース

1. Michel Cannarsa (2026)「Civil liability in a data driven economy: Proposal for a data-centric liability」
   File: raw/papers/law/civil-liability-in-a-data-driven-economy-proposal-for-a-data-centric-liability.md
2. Mehmet Unver, Iheanyichukwu Ogu (2026)「Regulating the Unseen: AI Accountability in UK Healthcare Sector」
   File: raw/papers/law/regulating-the-unseen-ai-accountability-in-uk-healthcare-sector.md
3. Feng Wang (2026)「AI Liability and Liability Insurance for AI」
   File: raw/papers/law/ai-liability-and-liability-insurance-for-ai.md
4. Tauhid ほか (2026)「Civil Liability for Artificial Intelligence-Induced Harm in Indonesia: Reconstructing Fault, Causation, and Evidentiary Responsibility through a Control-Risk-Evidence Model」
   File: raw/papers/law/civil-liability-for-artificial-intelligence-induced-harm-in-indonesia-reconstruc.md
5. Claudio Cifuentes Lobo, Marcus Alburez (2026)「Mitigating AI Privacy Risks in Latin America: Identity Infrastructure, Institutional Capacity and the Path to Adoption」
   File: raw/papers/law/mitigating-ai-privacy-risks-in-latin-america-identity-infrastructure-institution.md
6. Samar Singh (2026)「Algorithmic Oversight: Caremark's Fiduciary Framework Applied to Artificial Intelligence」
   File: raw/papers/law/algorithmic-oversight-caremarks-fiduciary-framework-applied-to-artificial-intell.md
