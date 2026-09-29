# アクセスから能力への変換を左右する社会的仲介

## 概要

技術へのアクセスは、それだけでは能力の獲得につながらない。教育、制度、運用条件、評価スキルといった「仲介層」が整っているかどうかが、同じ技術を使っても成果が分かれる主因になる、というのがこの概念の主張である。これはAIに限らず、新しい技術や資源が社会に導入されるたびに繰り返し現れる構造的な課題と考えられる。

AI Nativeな社会設計では、生成AIやエージェントが安価かつ広範に利用可能になる。そのため「誰がAIを使えるか」という問いより、「利用可能性がどのような条件のもとで実際の能力に変わるか」という問いが重要になる。アクセスの普及だけを成功指標にすると、仲介層の不足による格差や誤用が見えなくなる。仲介層を設計対象として扱うことが、この概念の実践的な出発点である。

## メカニズム

対象を人間、組織、AI、技術のどれに置き換えても成り立つ構造として、次の3点に整理できる。

1. **資本・能力の変換格差**:同じ資源(技術・ツール)が与えられても、それを能力に変換できる度合いは、利用者が持つ家庭・学校・教育的支援などの条件によって異なる。資源の量ではなく変換の条件が結果を分ける。
2. **仲介層のボトルネック**:アクセスと能力のあいだには、教育的な媒介、制度、運用条件といった層が存在する。この層が薄いと、アクセスが拡大しても能力向上は頭打ちになる。
3. **アクセスと評価スキルの乖離**:アクセスの民主化は、出力を責任をもって評価する専門性の民主化を自動的には伴わない。ツールが使えることと、その出力のリスクを見極められることは別の能力である。

この3点は、対象が生徒でも研究者でも組織でも同じ形で現れる。「到達」と「能力」の間に人間社会が構築する仲介があり、そこが成果を左右するという構造は、対象の入れ替えに対して不変である。

## 理論的背景

### 資本と潜在能力の統合的枠組み

Li and Xu(2026)は、中国の農村部の中学校6校を対象に、家庭・学校・教育的・学習者の利用条件が、AI支援学習における知覚された学習能力とどう関連するかを検討した。説明的逐次型の混合研究法で、質的な証拠を解釈上優先し、量的な結果は補足的・文脈化のために用いている。量的部分は有効な生徒質問紙486件と教師24名の文脈質問紙、質的部分は生徒・教師・保護者・学校管理者への32件の半構造化インタビューからなる。理論的には、ブルデューの資本論とセンの潜在能力アプローチを統合し、「媒介された利用」を扱っている。この研究は、アクセスから能力への転換に社会的仲介が必要であることを示す中核的な知見として位置づけられる。

### 評価スキルの乖離

Falk and Emery(2026)は、ローコード/ノーコードの研究ソフトウェアによりAI/MLの利用が非専門家の研究者にも広がっている状況を扱う。抄録によれば、アクセスの拡大は、出力を責任をもって評価しリスクを軽減する専門性を自動的には民主化しない。また、倫理的AI原則の多くは高水準にとどまり、運用に落とし込んだ指針が乏しいと指摘される。事例分野は自殺予防研究である。ここから、アクセスの民主化と評価スキルの民主化の乖離そのものが、制約設計の課題になることが示唆される。

### 導入に伴う社会技術的コスト

Chui et al.(2026)は、医療システムにおけるコスト意識型AIモデルの114本の論文を批判的に分析している。AIが意思決定の現場に、計算的・組織的・社会的コストを十分に検討しないまま導入されがちだと指摘し、社会技術的な厳密さの欠落を浮き彫りにする。導入の場では、人間の役割と計算コストのトレードオフが生じる。

### 運用側の仲介物と実験基盤

Chatlatanagulchai et al.(2026)は、エージェント型コーディングツールに永続的な指示を与えるコンテキストファイル(AGENTS.mdやCLAUDE.mdなど)を、1,925リポジトリの2,303ファイルで分析した。これらのファイルは静的な文書ではなく、頻繁な小さな追加を通じて設定コードのように進化する、読みにくい成果物であるという。開発者はテスト手順(75.9%)、実装の詳細(70.8%)、アーキテクチャ(68.1%)といった機能的文脈を優先している。エージェントという技術を使いこなすための仲介物が、運用条件として人手で維持されている例と読める。なお、抄録の後半(識別されたギャップ)は提示された抜粋では途切れているため、ここでは扱わない。

Ju and Aral(2026)のPairitは、人間とAIの組織設計を検証する実験のためのオンラインプラットフォームである。単一のYAML設定ファイルで、ページ、ルーティング、ランダム化、マッチメイキング、チャット、共有ワークスペース、サーバーホスト型エージェント、アンケートなどを宣言し、複数の人間とAIエージェントを組み合わせたライブセッションを実行できる。協働がどのように成立するかを測定し、可視化するための基盤として位置づけられる。

## AI Nativeな設計への示唆

- **アクセス指標から変換指標へ**:利用者数や導入率だけでなく、能力への変換がどの条件で起きているかを測る。Li and Xu(2026)の枠組みのように、家庭・学校・教育的条件・利用条件を分けて捉える視点が参考になる。
- **仲介層を設計対象にする**:教育的な媒介、運用ルール、文脈ファイルなどを、技術導入の付属物ではなく構成要素として設計・維持する。
- **評価スキルを同時に配布する**:ツールを開放するときは、出力を評価するための運用に落ちた指針や手順を併せて提供する。高水準の原則だけでは不十分である。
- **導入コストを全体で見る**:計算コストに加え、組織的・社会的コストと人間の役割の変化を導入前に検討する。
- **協働設計を実験で検証する**:人間とAIの協働の設計は、Pairitのような基盤で再現可能に検証し、仲介の効果を可視化する。

なお、Chatlatanagulchai et al.(2026)の実践的知見は、現時点の技術的制約に依拠する面があり、将来は不要になる可能性がある点に留意すべきである。

## 関連コンセプト

- [[access-driven-cumulative-concentration]]:アクセス格差が累積して集中と排除を生む過程
- [[proprietary-context-specific-assets-and-uneven-access]]:専有的・文脈特定的資源による不均等アクセス
- [[technology-mediated-power-asymmetry-amplification]]:技術が既存の力の不均衡を増幅する構造
- [[fluent-output-capability-decoupling]]:流暢な成果と内在的能力の乖離
- [[capability-transparency-gap-and-trust-loss]]:能力と透明性の乖離による信頼の喪失
- [[human-centered-capability-accumulation-and-socio-technical-fit]]:人間中心の参加と知識蓄積による導入の成否
- [[shared-editable-state-and-evaluability-design]]:評価可能性を担保する情報設計
- [[layered-governance-and-agency-retention]]:層別ガバナンスと主体性の保持
- [[governance-gap-between-capability-scaling-and-accountability]]:能力拡大と責任・統治設計の乖離
- [[continuous-human-signal-loop-and-temporary-support]]:継続的な人間シグナルの循環と一時的支援

## 参考ソース

1. Meili Li, Shuai Xu (2026). *From AI access to perceived learning capability in rural schools: a capital-capability account of pedagogically mediated use*.
   File: `raw/papers/hci/from-ai-access-to-perceived-learning-capability-in-rural-schools-a-capital-capab.md`
2. Jasmine Falk, Kara Emery (2026). *Democratizing AI Responsibly Through Research Software: A Case Study in Suicide Prevention Research*.
   File: `raw/papers/hci/democratizing-ai-responsibly-through-research-software-a-case-study-in-suicide-p.md`
3. Victoria Chui, Kelly McConvey, Shion Guha (2026). *A Sociotechnical Review of Algorithms in Health Systems: Technical, Cost, and Human-Centered Considerations*.
   File: `raw/papers/hci/a-sociotechnical-review-of-algorithms-in-health-systems-technical-cost-and-human.md`
4. Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa, Brittany Reid, Kundjanasith Thonglek (2026). *Agent READMEs: An Empirical Study of Context Files for Agentic Coding*.
   File: `raw/papers/hci/agent-readmes-an-empirical-study-of-context-files-for-agentic-coding.md`
5. Harang Ju, Sinan Aral (2026). *Pairit: A Platform for Live Experiments on Human-AI Collaboration*.
   File: `raw/papers/hci/pairit-a-platform-for-live-experiments-on-human-ai-collaboration.md`
