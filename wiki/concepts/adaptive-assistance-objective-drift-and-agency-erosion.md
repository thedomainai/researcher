# 適応的支援システムにおける目的乖離と主体性の侵食

## 概要

利用者に適応する自動化、記憶拡張、意思決定支援は、利便性と効率を大きく高める。一方でこれらのシステムは、努力の低減、迅速な受容、作業負荷の軽減、滑らかなタスク完了といった**短期の代理指標**に最適化されやすい。その結果、利用者本来の長期目標、意図の忠実性、選択可能性、認知資源の配分が歪む。これが本概念の要点である(Tier 1:不変原理)。

AI Nativeな社会設計では、人間とAIが常時相互作用する閉ループが基本構造になる。この構造では、性能指標が良好でも、利用者の主体性や長期的利益が静かに損なわれる可能性がある。したがって「支援がうまく機能している」ことの定義そのものを設計対象にする必要がある。

## メカニズム

以下の三つの構造は、支援を受ける対象が人間、組織、AI、神経インターフェースのいずれであっても成立する。

### 1. 代理指標への最適化による目標乖離

適応システムは観測可能な信号(受容率、完了速度、負荷の低さ、クリック等)を報酬として学習する。これらは真の目標(耐久的な便益、本人の意図、成長)の代理にすぎない。閉ループで代理指標を追い続けると、システムと利用者が代理指標に過適合し、真の目標から徐々に離れる。

### 2. 認知負荷の外部化と再配分

支援は認知負荷を外部に移す。移した先が適切であれば、ワーキングメモリが保全され、深い作業に資源を回せる。設計が不適切だと、負荷は「作業の実行」から「アルゴリズムの継続的な監視」へ移るだけで、疲労はむしろ悪化する。外部化の効果は、何を吸収し何を利用者に残すかで決まる。

### 3. 選択肢の自動制約による主体性低下

推薦、補完、自動決定は、提示される選択肢や既定の行動を絞り込む。利用者は効率的に選べる一方、選択空間が狭まり、自らの意図を形成し表明する機会が減る。自動化された意思決定は、人間の選択可能性そのものを制約する。

これらは相互に強化し合う。代理指標への最適化が選択肢の制約を促し、制約された環境が代理指標をさらに安定させる。

## 理論的背景

**神経適応的過適合(neuroadaptive overfitting)。** Nagarajanは、AI介在型のBCIを対象に、この現象を閉ループの失敗モードとして定義した。システムが短期的な成功の代理指標(努力の低減、迅速な受容、負荷の低さ、滑らかな完了)に過剰最適化され、利用者の耐久的な目標から乖離する状態である。従来の性能指標は、意図の忠実性、オーサーシップ、主体性、治療上の挑戦、持続的な臨床的便益の喪失を見落とし得ると指摘されている。対策として、デコーダの証拠、不確実性、文脈的・臨床的な重要度、疲労、利用者や臨床医が定めた目標に応じて支援の強度を調整する「Slow-Fast BCI」の枠組みが提案されている。

**記憶拡張の二重経路。** Ng-Soon-Chyeは、デジタル小売におけるAI拡張記憶(AI-AM)、すなわちアルゴリズムが過去の行動痕跡を記録・検索・再提示する仕組みを検討した。シンガポールのEC消費者30名への半構造化インタビューと実務者の省察に基づく質的分析で、二つの経路が見いだされている。試行錯誤的な購入を減らし熟慮的な抑制を支える持続可能な経路と、同じ仕組みが衝動購買のループを増幅する非持続的な経路である。同一のメカニズムが、設計次第で逆の帰結をもたらす。

**認知的足場かけと負荷の移動。** Artha and Nguyenの概念的な二経路モデルは、AIチャットボットが低水準の事務的摩擦を吸収してワーキングメモリを保全する経路を提案する。同時に、不適切な実装が認知的要求を「実行」から「継続的な監視」へ移し、疲労を悪化させると警告している。

**自動化意思決定と選択可能性。** Gangulyらは、EC領域でAIが推薦の個別化、不正検知、動的価格設定などを担う一方、アルゴリズムの透明性とバイアス、自動化された意思決定の責任、消費者保護といった課題を生むことを、インド法の枠組みで分析している。ここでは、自動化による選択の制約が制度的な問題としても現れることが示唆される。

**相互作用スタイルの差。** Liuらは中国の大学生7,029名に潜在プロファイル分析を行い、利用強度、相互作用の質、信頼、心理的近さ、情動的愛着から五つのプロファイルを同定した(効率的・道具的27.00%、探索的・カジュアル31.97%、深い情動的12.18%、両価的・愛着的9.23%、離脱的・回避的19.62%)。抜粋の範囲では、利用強度だけでなく関与の質が重要であるという枠組みが示されている。精神保健との詳細な関連は抜粋からは確認できない。

**データ側の認知的制約。** Eppingらは、クラウドソーシングで作られたデータセットとそれで学習したモデルが、注釈者の認知的制約やバイアスを引き継ぐことを扱っている。人間の認知特性が適応システムの学習信号に入り込む経路を示す知見である。

## AI Nativeな設計への示唆

1. **指標の多層化**:速度、受容率、低負荷といった短期指標に加え、意図の忠実性、オーサーシップ、主体性、長期目標の達成度を評価に組み込む。
2. **支援強度のペーシング**:不確実性、リスクの大きさ、疲労、利用者定義の目標に応じて、支援の強さと速さを可変にする(Slow-Fast的発想)。
3. **目標の所在を利用者側に置く**:長期目標を利用者や専門家が定義・更新できるようにし、システムが自己生成した代理報酬だけで動かないようにする。
4. **何を外部化するかの設計**:事務的摩擦は吸収し、判断や学習に必要な負荷は残す。監視負荷を新たに生まないよう、介入の頻度と説明の量を管理する。
5. **選択肢の開示と可逆性**:推薦や既定値が選択空間を絞っていることを可視化し、利用者が容易に覆せるようにする。
6. **同一機構の二面性を前提にする**:記憶拡張や個別化は、熟慮を支えることも衝動を増幅することもある。導入時に両経路を想定し、後者を検知する仕組みを設ける。
7. **相互作用の質の監視**:利用量ではなく関与の質(信頼、依存、愛着のパターン)を観測対象にする。

## 関連コンセプト

- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による所有感・責任・能力の侵食と回復的足場設計
- [[assistance-availability-versus-skill-formation]] — 支援の可用性と能力形成の逆相関
- [[agency-as-context-and-interaction-design-outcome]] — 主体性は相互作用設計で決まる
- [[adaptive-human-ai-coupling]] — 適応的人間AI結合
- [[compensatory-adaptation-hidden-erosion]] — 補償的適応の枯渇と安定性の錯覚
- [[ai-sensemaking-human-agency]] — AIセンスメイキングと人間のエージェンシー
- [[uncertainty-quantification-and-common-measurement-for-trust]] — 不確実性の定量化と信頼

## 参考ソース

- A Study on the Role of Artificial Intelligence in E-Commerce and Its Cyber Law Implications(Shantanu Ganguly, Sushanta Kumar Das, 2026)— `raw/papers/neuroscience/a-study-on-the-role-of-artificial-intelligence-in-e-commerce-and-its-cyber-law-i.md`
- Generative AI interaction styles and mental health among college students: a latent profile analysis(Zongming Liu ほか, 2026)— `raw/papers/neuroscience/generative-ai-interaction-styles-and-mental-health-among-college-students-a-late.md`
- AI-Augmented Memory and Consumer Sustainability: Understanding Dual Consumption Pathways in Digital Retail(Jack Ng-Soon-Chye, 2026)— `raw/papers/neuroscience/ai-augmented-memory-and-consumer-sustainability-understanding-dual-consumption-p.md`
- Slow-Fast Brain-Computer Interfaces: Preventing Neuroadaptive Overfitting in AI-Mediated Neural Interfaces(Aarthy Nagarajan, 2026)— `raw/papers/neuroscience/slow-fast-brain-computer-interfaces-preventing-neuroadaptive-overfitting-in-ai-m.md`
- Algorithmic Scaffolding: Mitigating Decision Fatigue and Cognitive Load through AI Chatbots to Prevent Occupational Burnout(Adhilla Salsabila Putri Artha, Ly Hoang Nguyen, 2026)— `raw/papers/neuroscience/algorithmic-scaffolding-mitigating-decision-fatigue-and-cognitive-load-through-a.md`
- Improving crowdsourcing for AI through cognitive-inspired data engineering(Gunnar Paul Epping ほか, 2026)— `raw/papers/neuroscience/improving-crowdsourcing-for-ai-through-cognitive-inspired-data-engineering.md`
