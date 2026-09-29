# 技術的成功と価値実現の断絶

## 概要

技術的成功と価値実現の断絶とは、導入したシステムが機能仕様を満たし「技術的には成功」しているにもかかわらず、事業上・組織上の価値が実現しない現象を指す。ソース [3] はこれを「ゾンビAI投資(zombie AI investments)」と呼び、仕様を満たしながら使われないまま残るAIイニシアチブのパラドックスとして分析している。

この概念は、技術が組織内で「進歩のシグナル」として機能し、実質的な効果とは別に権力・権威・資源を再配分する、という側面も含む([2])。つまり、導入の「成功」と価値の「実現」は別の事象であり、両者の間には組織的・政治的な過程が介在する。

AI Nativeな社会設計にとって重要なのは、性能指標や導入完了をもって成功とみなす設計が、構造的に価値の空洞化を招きうるからである。AIの能力が向上するほど導入自体は容易になるが、価値化のボトルネックは技術の外側、つまり組織の統合能力・統治・利害関係者との関係に移る。設計の対象は、モデルや機能だけでなく、それを取り巻く組織的条件まで含めなければならない。

## メカニズム

中核となるのは、次の三つの構造である。いずれも対象がAI・人間・組織・技術のどれであっても成り立つ。

### 1. サイロ化と部分最適

個別の部門や案件で完結した導入は、その局所の仕様を満たせば「成功」と評価される。しかし全体の業務プロセスや戦略と接続されなければ、価値は生まれない。ソース [3] は、障壁の一つとして「サイロ化された導入」を挙げている。

同じ構造は他の領域でも観察される。
- ソース [4] は、AIデータセンター建設の調達文書を扱い、責任の制度化とインターフェース閉鎖のタイミングが、技術的遅延や責任境界の調整といった帰結を規定すると論じている。
- ソース [5] は、ビジネスプロセス管理(BPM)と機械学習(ML)開発ライフサイクルの同期が欠けていることを、統合の障壁として扱っている。
- ソース [6] は、オープンソースのエージェンティックAI実装が実行指向で狭いスコープにとどまり、ライフサイクル統合や高次の自律性が未成熟であると報告している。

これらはいずれも、部分としては機能しても、全体としての接続が欠ければ価値に転化しにくいという構造を示す。

### 2. シグナリングによる権力再配分

技術の導入は、それ自体が「進歩」を示す社会的シグナルとして働く。ソース [2] は、高等教育におけるAI導入が、認識論的・教育的・組織的な負荷を生みながらも、進歩の指標として維持されうると分析している。同論文はAIガバナンスを、権威・専門性・労働・リスクを再編成する政治的過程として位置づける。このとき、導入の是非は効果の検証ではなくシグナルとしての価値によって支えられ、価値実現の検証が後景に退く。

### 3. 利害関係者の抵抗

ソース [3] は、ユーザーの抵抗を価値実現を阻む主要な障壁の一つとしている。ソース [1] は、AI導入に伴う雇用不安(AI-induced job insecurity)が構造的な緊張を生むことを前提に、組織のResponsible AIに対する認識と、リーダーシップによる倫理的ガバナンスの認識が、この不安を和らげる認知的ヒューリスティックとして働くことを示している。抵抗は非合理な障害ではなく、不確実性への合理的反応として扱う必要がある。

## 理論的背景

- **ゾンビAI投資の分析([3])**:仕様を満たしても未使用のまま残るAI案件を失敗事例から分析し、サイロ化された導入、ユーザーの抵抗、戦略的整合性の欠如を主要な障壁として特定した。対処として、影響の大きいユースケースへの絞り込みと分散型ガバナンスが、実験段階を越えるために必要だと述べている。
- **Innovation–Enervation Paradox([2])**:Fraserの承認と再分配の議論、Butlerのパフォーマティビティ論、Harawayの situated knowledges を援用し、AI導入が進歩の指標として維持されながら組織に負荷を生む構図を論じる。さらにダニング=クルーガー効果を、この構図に関わる論点として扱っている。
- **不確実性管理理論による実証([1])**:韓国の従業員401名を対象とした4波の時間差調査による調整付き逐次媒介モデルで、Responsible AIの認識がAI起因の雇用不安を低減する経路を検証している。ガバナンスの認識が心理的抵抗を左右するという知見である。
- **責任とインターフェースの制度設計([4])**:2021〜2025年の公開調達文書に基づく44件のデータチェーン完結プロジェクトを、負の二項回帰等で分析し、契約上の責任の集中や段階横断的な共同組織だけでは十分でなく、インターフェース閉鎖の要件が効くことを示唆している(抜粋の範囲で確認できる内容に限る)。
- **BPMとMLの同期([5])**:業務プロセスのライフサイクルとMLモデルのライフサイクルの段階を対応づける方法論を提案している。
- **エージェンティックAIの現状([6])**:オープンソース実装の分析から、エージェンティックな振る舞いが概念的な期待ほどには実現されていないことを示している。

## AI Nativeな設計への示唆

1. **成功指標を導入から価値へ移す**:仕様適合や稼働率だけでなく、業務プロセス上の利用と事業成果を評価対象に含める。シグナルとしての導入は、効果検証を経ない限り成功の証拠とはしない。
2. **ユースケースの選別**:実験的な散在導入ではなく、影響の大きいユースケースに集中し、実験段階からの移行条件を事前に設計する([3])。
3. **ライフサイクルの同期**:AIモデルの開発・運用と業務プロセス管理の段階を対応づけ、サイロ間の接続点を明示する([5])。
4. **責任とインターフェースの早期確定**:責任境界とインターフェースの閉鎖時期を後回しにせず、制度として組み込む([4])。
5. **分散型ガバナンスと透明な倫理的統治**:導入判断を政治的過程として認識し、権威・労働・リスクの再配分を可視化する([2])。倫理的ガバナンスの認識を通じて、抵抗の背景にある不確実性を低減する([1])。
6. **抵抗を設計情報として扱う**:利用者の抵抗を排除対象ではなく、統合の不備を示すフィードバックとして取り込む。

## 関連コンセプト

- [[capability-realization-organizational-bottleneck]] — 価値を決めるのは技術ストックではなく組織の統合能力であるという、本概念の直接的な土台。
- [[human-centered-capability-accumulation-and-socio-technical-fit]] — 人間中心の参加と知識蓄積が導入の成否を分けるという視点。
- [[it-value-organizational-transformation]] — ITの経済価値が組織変革を伴って初めて現れるという古典的議論。
- [[capability-contingent-absorption-and-progressive-layering]] — 組織能力に応じた吸収と段階的な導入。
- [[absorption-capacity-bottleneck-saturation]] — 吸収コストとボトルネックによる価値の飽和。
- [[governance-gap-between-capability-scaling-and-accountability]] — 能力拡大と責任・統治設計の乖離。
- [[incentive-driven-deferral-and-asymmetry]] — インセンティブが長期価値を後回しにする構造。
- [[multistage-transfer-bottleneck-and-evaluability]] — 多段階移転における評価可能性の連鎖。

## 参考ソース

1. Byung‐Jik Kim, Julak Lee (2026). *Governing the Algorithm, Sustaining the Environment: How Authentic Leadership Validates Corporate Responsible AI to Foster Moral Ownership and Green Innovation*. File: raw/papers/innovation_management/governing-the-algorithm-sustaining-the-environment-how-authentic-leadership-vali.md
2. Janine Arantes (2026). *The Innovation-Enervation Paradox in higher education: AI and the Dunning-Kruger effect*. File: raw/papers/innovation_management/the-innovation-enervation-paradox-in-higher-education-ai-and-the-dunning-kruger-.md
3. Dieu Hang Piekut, Renata Gabryelczyk (2026). *Zombie Ai Investments: From Technical Success To Business Failure*. File: raw/papers/international_business/zombie-ai-investments-from-technical-success-to-business-failure.md
4. 著者不明 (2026). *Organizational Change and Management Innovation in the Construction of Ai Data Centers under the Background of "Artificial Intelligence+"*. File: raw/papers/innovation_management/organizational-change-and-management-innovation-in-the-construction-of-ai-data-c.md
5. Gleb V. Ovchinnikov, Alexander E. Trubin, Tatyana V. Artemova, Oleg P. Kultygin (2026). *Analysis of Management Approaches and Development of a Methods for Integrating Machine Learning Models into Business Process Management*. File: raw/papers/international_business/analysis-of-management-approaches-and-development-of-a-methods-for-integrating-m.md
6. Björn-Lennart Eger, Barbara Dinter (2026). *Agentic AI In Business Processes: A Conceptually Grounded Analysis Of Open-Source Implementations*. File: raw/papers/international_business/agentic-ai-in-business-processes-a-conceptually-grounded-analysis-of-open-source.md
