# 社会技術的経路による害・格差の伝播と累積

## 概要

社会技術的経路による害・格差の伝播と累積とは、AIがもたらす害が「モデル単体の技術的誤り」から直接生じるのではなく、出力が組織のワークフローの中で知覚され、信頼され、検証され、伝播していく過程と、訓練データ上で周縁に置かれた立場への偏りが累積していく過程から生じる、という原理である。あわせて、一見進歩的に見える制度や思想の枠組みも、既存の思想的前提を再生産しうるという視点を含む。

AI Nativeな社会設計にとって重要なのは、精度・較正・感度・特異度といったモデル指標だけでは安全性を保証できない点にある。安全性は、AIの出力が組織に入った後に何が起きるかに大きく依存する。したがって評価と設計の単位は、モデルから「モデル+人+ワークフロー+制度」の全体へ移る必要がある。

## メカニズム

以下の構造は、行為者が人間・AI・組織・技術のいずれであっても成立する。

1. **上流の脆弱性が下流の帰結を規定する**:入力側(データ、前提、立場)にすでに存在する偏りや脆弱性が、出力の質や性質を条件づける。データ上で周縁にある対象ほど、扱いが不利になりやすい。
2. **媒介による変換と伝播**:出力は、受け手に気づかれ、信頼され、検証され(あるいはされず)、行為に使われ、さらに既存の業務プロセスを通じて他所へ流れる。各段階が誤りを減衰させることも、増幅・固定化することもある。
3. **累積(加算的・交差的)**:周縁化の指標が重なるほど、扱いの差は積み上がる。単一の属性では小さく見える差も、複数の属性が交差すると大きくなる。
4. **枠組みの再生産**:制度や設計が依拠する思想的枠組みは、それが革新的であると自認していても、既存の支配的な前提を引き継ぎ、固定化することがある。
5. **遅延と不可視性**:害は経路の下流で、時間を置いて現れるため、上流の測定だけでは検出しにくい。

つまり害とは、「発生源」ではなく「経路」の性質である。経路のどこに検証・遮断・是正の余地があるかが、害の大きさを決める。

## 理論的背景

### 医療AIにおける五段階の社会技術的経路

Sebin and Sebin (2026) は、医療AIの評価が識別能・較正・感度・特異度・ベンチマーク精度に偏ることを指摘する。その上で、AI出力が臨床システムに入ったあと、気づかれ、信頼され、検証され、行為に使われ、既存のワークフローや組織能力を通じて伝播するかどうかが安全性を左右すると論じる。市販後報告、人間-AI研究、ドリフト分析、公平性監査の証拠は、この経路上の複数の地点でハザードが生じうることを示す。ただし同時に、AI関連の害の発生率、帰属可能な重大性、長期的帰結を定量化するには不十分だとも述べられている。提案されるのは、上流の脆弱性、AIの挙動、人間-ワークフローによる媒介、意思決定またはシステムへの効果、下流の帰結をたどる五段階の経路モデルである(抜粋の範囲で確認できる構成要素)。核心的知見は、システム害は技術的誤りだけでなく、ワークフローがAI出力を知覚・信頼・伝播する組織統合の失敗から生じる、というものである。

### 周縁化の累積:イタリアの青年を想定した検証

Ederoclite et al. (2026) は、ChatGPT、Claude、Geminiの3つの商用LLMに対し、性別・階級・民族・性的指向が異なる4つのペルソナ(イタリア語、計120の標準化された対話)を用いて分析した。定性分析からは、医療化、主体性(エージェンシー)の帰属の差、文化的な他者化という反復パターンが見出された。周縁化の指標が累積するにつれて、こうした傾向が強まることが示唆されている(抜粋は途中で切れているため、詳細は原典を参照)。核心的知見として、周縁化されたアイデンティティが訓練データ上で脆弱であることが、AIシステムに格差を累積させる不可避的なメカニズムとされる。

### 制度における思想枠組みの再生産

Oleart and Flores Moleon (2026) は、EUのAI規制(拘束力のある2024年AI法、自主的な2025年GPAI行動規範、2019年の高レベル専門家グループ文書)を、社会技術的想像(望ましい未来と回避すべきリスクについての共有されたビジョン)の概念で比較する。拘束的規制と、規制の共同管理者としての技術プラットフォームの役割拡大との間に構造的緊張があると述べる。核心的知見は、制度化された権力関係のもとでは、先進的に見える思想体系も既存の思想的枠組みを再生産しうる、というものである。表題が示すように、その枠組みはシリコンバレー的なテクノソリューショニズムである。

### 情報システム開発における緊張

Richter et al. (2026) は、情報システム開発には競合する組織的要求の間の根本的な緊張があり、意図的な管理が必要だと位置づける。ここから、害の伝播も単純な技術問題でなく、組織内の緊張の調整という文脈で扱うべきことが示唆される(抜粋は要旨冒頭までで、詳細は確認できない)。

## AI Nativeな設計への示唆

- **経路全体を評価対象にする**:モデル指標に加え、出力が気づかれるか、過信されないか、検証されるか、どう伝播するかを、ワークフロー単位で測定・監視する。
- **検証と信頼の設計**:検証の機会を設け、それが形骸化して偏りを増幅しないよう、人間の検証手順自体を設計対象とする。
- **交差的な監査**:単一属性の平均的な公平性だけでなく、複数の周縁化指標が重なる層での出力を監査する。データ上の周縁性を前提に、代表性の低い層を重点的にテストする。
- **下流帰結の追跡**:害の発生率や長期影響は現状十分に測れないため、市販後報告、ドリフト分析、公平性監査などを継続的に運用し、証拠を蓄積する。
- **制度・思想の前提を疑う**:規制や設計指針が既存の枠組みを再生産していないか、権力関係(誰が共同管理者か)を含めて点検する。
- **組織内の緊張を明示的に管理する**:導入速度、効率、安全といった競合要求を可視化し、意図的に調整する。

## 関連コンセプト

- [[sociotechnical-systems]]:社会と技術を一体のシステムとして捉える基盤
- [[sociotechnical-configuration-of-ai]]:AI実装の社会技術的構成
- [[sociotechnical-ai-management]]:社会技術的なAI管理の実践
- [[human-verification-loop-bias-amplification]]:人間の検証がバイアスを増幅する経路
- [[bias-compounding-across-interacting-distortion-sources]]:複数の歪み源による偏りの累積
- [[structural-bias-from-data-and-hidden-information-constraints]]:データ由来の構造的バイアス
- [[bias-embedding-and-safety-as-dynamic-process]]:バイアスの埋め込みと動的な安全ガバナンス
- [[mediation-visibility-and-curation-bias-amplification]]:媒介・可視化による増幅
- [[source-attribution-and-reliance-miscalibration]]:信頼較正の歪み
- [[concentration-driven-systemic-risk-propagation]]:システミックリスクの伝播
- [[ai-bias-audits-and-red-teaming]]:バイアス監査とレッドチーム
- [[algorithmic-bias-fairness]]:アルゴリズムバイアスと公平性
- [[adoption-outpacing-governance-capacity-asymmetry]]:導入と統治能力のギャップ
- [[technology-adoption-as-power-and-role-redistribution]]:権限・役割構造の再編

## 参考ソース

- From model failure to system harm: operationalizing a sociotechnical pathway for healthcare AI safety — Burhan Sebin, Irem Karaman Sebin (2026)
  File: raw/papers/information_systems/from-model-failure-to-system-harm-operationalizing-a-sociotechnical-pathway-for-.md
- Digital bias in sexuality education: an intersectional analysis of AI responses to simulated Italian adolescents — Mario Ederoclite, Iana Tzankova, Paola Villano (2026)
  File: raw/papers/information_systems/digital-bias-in-sexuality-education-an-intersectional-analysis-of-ai-responses-t.md
- How Brussels reproduces Silicon Valley technosolutionism: Sociotechnical imaginaries in the EU's regulatory approach to AI (2019‒2025) — Álvaro Oleart, Alejandro Flores Moleon (2026)
  File: raw/papers/information_systems/how-brussels-reproduces-silicon-valley-technosolutionism-sociotechnical-imaginar.md
- Tensions: A Lens for Provoking Debate on Contemporary Information Systems Developments — Alexander Richter, Michael Leyer, Stuart Black, Michael Davern (2026)
  File: raw/papers/information_systems/tensions-a-lens-for-provoking-debate-on-contemporary-information-systems-develop.md
