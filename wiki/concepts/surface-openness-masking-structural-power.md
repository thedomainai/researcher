# 表層的相互運用性が構造的権力を温存するメカニズム

## 概要

表層的相互運用性とは、APIやデータ標準のような技術的な接続性、あるいは情報処理能力の高度化が「開放」の外観を作り出す一方で、利益相反、権力構造、情報の非対称性、説明責任の断絶が手つかずのまま残る状態を指す。技術的につながっていることと、誰がどの条件でアクセスし、誰が責任を負い、誰が利益を得るかが開かれていることは別の問題である。前者の整備が進むほど後者への取り組みが先送りされ、個別には合理的な行動が全体最適を損なう均衡が固定化される。

AI Nativeな社会設計では、AIエージェントやデータ基盤が組織・国家・個人の間を接続する。接続が容易になるほど「すでに開かれている」という認識が生まれやすく、実質的な権力配分の問いが見えにくくなる。設計者は「つながっているか」ではなく「誰が条件を決め、誰が説明責任を負うか」を問う必要がある。

## メカニズム

対象が人間、組織、AI、技術のいずれであっても、次の構造が成立する。

1. **技術的境界資源への偏り**: 接続に必要な資源のうち、APIやデータ標準のような技術的なものは合意しやすく、進捗も見えやすい。一方、アクセス規則、価格モデル、利用条件のような社会的なものは利害が直接衝突するため後回しにされる。
2. **快適ゾーンの形成**: 技術的な整備作業は、参加者が協力できる「快適ゾーン」を作る。この間は対立が表面化せず、開放が進んでいるように見える。真の開放を目指した段階で、隠れていた緊張と利益相反が現れる。
3. **能力集中による情報非対称**: 個人データの処理能力が特定の主体に集中すると、処理する側と処理される側の間に情報権力の非対称が生じ、透明性と説明責任が断絶する。
4. **個別合理性と全体最適の不一致**: 各主体は自己利益に沿って行動する。情報とインセンティブの構造次第では、結果が全員に利益をもたらすこともあれば、予測されていた損失が全員に生じることもある。
5. **均衡の固定化**: 上記が組み合わさると、誰も現状を変えるインセンティブを持たないまま、外観だけが開放的な状態が続く。

## 理論的背景

**プラットフォームの開放性と境界資源(ソース1)**: van der Doelen と de Reuver は、オランダの医療データプラットフォームを探索的事例研究として分析した。データ駆動型イノベーションは限定的で、プラットフォームの多くは閉じている。関係者は開放性を語るが、実際には技術的相互運用性に注力している。進行中の取り組みはAPIやデータ標準などの技術的境界資源を広範に整備している一方、アクセス規則、価格モデル、利用条件といった社会的境界資源はほとんど注目されていない。著者らは、技術的な土台づくりが、真の開放を目指したときに表面化する緊張や利益相反を隠す「快適ゾーン」になると理論化している。相互運用性と開放性を区別することが、この現象の説明に有効だとされる。

**情報権力の非対称と説明責任(ソース2)**: Albarelli らは、組織が個人的・生理的・行動的データを処理する能力を高めるにつれ、プライバシー、透明性、説明責任、ガバナンスの懸念が生じると論じる。顔認識、生体モニタリング、リアルタイム行動追跡などのAI監視技術は、セキュリティや運用効率の利点がある一方で、倫理的・社会的リスクをもたらす。現行の法規制は技術の拡大速度に追いつきにくいとされる。

**協調の失敗(ソース3)**: Armstrong と Quah は、脱グローバル化、国際協力の困難化、大国間競争の対立化を統一的な経済学の枠組みで扱う。ゼロサム認識だけでは説明が不十分であり、自国利益のみを追う国家が全体に利益をもたらす結果を生んだ場合もあれば、予測どおりの損失が全当事者に生じた場合もあるとする。個別利害と全体最適の不一致が、協力の成否を分ける構造として示されている。

**補足的な知見**: ソース4は、地方の公開データプラットフォームの開始を準実験として用い、公開データの開放がAI特許数を平均0.25件増やすことを示した。メカニズムはデジタル人材需要の拡大と応用場面の拡大とされる。これは、実質的なデータアクセスが実際に効果を持つことを示す対照的な知見であり、表層的な接続だけでは得られない成果を示唆する。ソース5は、AIが採用の低コスト化と高速化・大規模化を通じて犯罪組織の採用活動を産業化していると述べ、ソース6は、AIによる防御機構が攻撃側にも悪用される二面性を論じる。いずれも、技術の障壁低下や能力向上が、それを使う主体の意図によって非対称を拡大しうることを示す。

## AI Nativeな設計への示唆

- **開放の評価軸を分ける**: 相互運用性(技術的接続)と開放性(アクセス規則、価格、利用条件の公開性と公平性)を別々の指標で評価する。技術標準の整備率だけで開放度を判断しない。
- **社会的境界資源を初期から設計する**: APIやスキーマと並行して、アクセス条件、課金、利用制限、紛争解決の規則を設計対象にする。利益相反を早期に表面化させ、快適ゾーンへの逃避を防ぐ。
- **説明責任の経路を接続と同時に設ける**: データや処理能力が集中する箇所には、監査可能性、透明性、責任主体の明示を組み込む。
- **協調の失敗を前提にインセンティブを設計する**: 各主体の個別合理性が全体最適と乖離する構造を前提に、情報共有とインセンティブを整合させる仕組みを設ける。
- **能力の非対称を監視する**: 導入速度がガバナンス能力を上回っていないか、AIの防御的利用が攻撃的利用と同じ基盤に依存していないかを継続的に点検する。
- **実質的開放の効果を検証する**: ソース4のように、実質的なデータ開放が成果に結びつくかを準実験的に測り、外観と実質を区別して評価する。

## 関連コンセプト

- [[surface-substrate-divergence]] — 宣言と実質の乖離という、本概念の基本構造
- [[architecture-as-power-distribution-and-interface-standards]] — 介面標準が権力配分を決める側面
- [[technology-mediated-power-asymmetry-amplification]] — 技術が既存の力の不均衡を増幅する過程
- [[complementary-information-and-epistemic-asymmetry]] — 情報構造と認識論的非対称性
- [[incentive-driven-deferral-and-asymmetry]] — インセンティブによる後回しと非対称の固定化
- [[adoption-outpacing-governance-capacity-asymmetry]] — 導入速度と統治能力のギャップ
- [[assurance-evidence-parity-and-governance-facade]] — ガバナンスの見せかけの構造
- [[structural-origins-of-organizational-harm-and-power-framing]] — 権力と害悪の構造的生成
- [[decentralized-coordination-and-power-concentration]] — 分散協調と権力集中の力学

## 参考ソース

1. Platform Interoperability Without Openness: The Comfort Zone That Suffocates Data-Driven Healthcare Innovation? — Jasper van der Doelen, Mark de Reuver (2026)
   File: raw/papers/innovation_management/platform-interoperability-without-openness-the-comfort-zone-that-suffocates-data.md
2. Public Policy Imperatives for Emerging AI Surveillance Technologies — Martina Albarelli, David Eisenberg, Jorge Fresneda, Simone Marras (2026)
   File: raw/papers/innovation_management/public-policy-imperatives-for-emerging-ai-surveillance-technologies.md
3. Economics for the global economic order: The tragedy of epic fail equilibria — Shiro Armstrong, Danny Quah (2026)
   File: raw/papers/innovation_management/economics-for-the-global-economic-order-the-tragedy-of-epic-fail-equilibria.md
4. Openness of Public Data and Corporate Artificial Intelligence Innovation — Junyan Hui (2026)
   File: raw/papers/innovation_management/openness-of-public-data-and-corporate-artificial-intelligence-innovation.md
5. Hired by the Algorithm: how criminal networks are using AI to recruit across the EU, Latin America and the Caribbean — Joël Lévesque (2026)
   File: raw/papers/innovation_management/hired-by-the-algorithm-how-criminal-networks-are-using-ai-to-recruit-across-the-.md
6. Transforming Cyber security with AI: Current Hurdles and Future Horizons — Dash Satyabrata, Dr Sasmita Panigrahi, Biswanath Patro (2026)
   File: raw/papers/innovation_management/transforming-cyber-security-with-ai-current-hurdles-and-future-horizons.md
