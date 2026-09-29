# 統治・復旧コストが支配する知能のROI

## 概要

「統治・復旧コストが支配する知能のROI(Governance-Cost-Dominated Return on Intelligence)」とは、能動的な知能(永続的・エージェント的で、ツールを使い、意思決定に影響し、行動できるAI)の価値が、モデル費用やライセンス費用といった機能コストでは決まらない、という原理である。価値は、権限・リスク・注意・失敗復旧といった統治コストを負担した後に残る部分で決まる。さらに、技術が生む価値を組織が実際に捕捉できるかどうかは、制度的条件に依存する。

ソース[2]は、AI ROIの議論の多くが、モデル費用、プラットフォーム支出、シート課金、トークン使用量、自動化量、削減時間、生産性の主張、ダッシュボード上の活動量といった「狭い投資の文法」を引き継いでいると指摘する。これらは必要だが、知能が能動的になると十分ではなくなる。

AI Nativeな社会設計にとって重要なのは、次の点である。

- 能力の向上だけでは価値が実現しない。設計の焦点は、能力から「受容された価値」に至る経路全体に移る。
- 統治・復旧の設計は、事後の追加コストではなく、ROIを決める中心的な変数である。
- 価値の帰属先(誰が捕捉するか)は技術の性質だけでなく、制度が決める。

## メカニズム

この原理は、対象を入れ替えても成立する構造として整理できる。対象は人間、AI、組織、技術のいずれでもよい。

1. **能力と価値の分離**:主体(人間・AIエージェント・組織)が生み出す出力は、そのままでは価値にならない。証拠の提示、統合、監督、修正、例外処理、権限付与、リスク引受、注意の消費、復旧、信頼、帰結の責任といった経路を通過して初めて、受容された価値になる(ソース[2])。
2. **コストの内部化**:この経路上のコストは、取引・統治コストとして誰かが負担する。負担を内部化できない設計では、見かけのROIが実際のROIを上回る。
3. **専有可能性の制度依存**:生み出された価値のうち、誰がどれだけ捕捉できるかは、技術の新規性(根本性)ではなく、専有可能性を決める制度的補完資産に左右される(ソース[1])。
4. **補完スタックの必要性**:能力は、権限管理、監督、復旧手段などの補完的な仕組みと組み合わさって初めて価値化される。単独の技術投入では成立しない。

構造的には「能力 − (権限・リスク・注意・復旧のコスト) → 捕捉可能な価値(制度条件で配分)」という形になる。主体が人間でもAIでも、権限を委ねて失敗の復旧を要する限り同じ構造が現れる。

## 理論的背景

### Return on Intelligenceの枠組み(ソース[2])

Figurelliの論文は、AI ROIをより広い「field-economic architecture」として捉え直すReturn on Intelligenceを提案する。中心的な主張は、AIが実際のリターンを生むのは、出力が能力から受容された価値へ至る経路を生き延びた後に限られる、というものである。抜粋によれば、この経路のコストには、証拠、統合、監督、修正、例外処理、権限、リスク、注意、統治、復旧、信頼、帰結が含まれる。

### AI適用可能性(専有可能性)のパラドックス(ソース[1])

Mahmudの論文は、AI特許がマッチングされたIT特許よりも根本性(radicalness)が低いにもかかわらず、有意な価値プレミアムを持つという「AI appropriability paradox」を報告する。Blinder–Oaxaca分解を20年にわたるマッチング特許に適用した結果、この差のうち観察可能な特許特性で説明できるのは約3分の1にとどまった。残りは標準的なシュンペーター的次元では説明できない。著者は、appropriability regime理論と汎用技術の経済学に基づき、これをAIに固有の異なる専有可能性レジームの反映と解釈している。ここから、技術価値の捕捉が技術特性だけでなく組織・制度側の仕組みに依存するという含意が得られる。

### 補完的な知見(ソース[3]〜[6])

以下は上記原理を直接論証するものではなく、周辺的な裏づけとして位置づけられる。

- ソース[3]は、決定論的なRPAとAIの認知能力を組み合わせるIntelligent Process Automationを提案し、タスク完了時間33%短縮、エラー65%減を報告する。規則性と適応性の補完という構造は、補完スタックの発想と整合する。ただし対象とするビジネスプロセス自動化は陳腐化しうる領域である。
- ソース[4]は、ギリシャ企業を対象に、市場向け技術(需要拡大・市場アクセス)と、生産・意思決定向け技術(AI、機械学習分析、IoTなど)で経済作用の経路が異なることを示す。技術を均質な投入と見なさないという点で、価値実現の経路依存性を支持する。
- ソース[5]は、スペインSME 400社の分析で、経営者の金銭的リスク態度がデジタル化・持続可能性投資に影響することを示す。リスクの認識が投資判断を左右するという点は、リスクを価値経路の構成要素とみなす議論と関連する。
- ソース[6]は、AIを導入する組織のC-suiteや取締役に求められる能力を、系統的レビューで分類する。自動化された意思決定の統治を担う管理者の判断枠組みが変化することを扱っている。

## AI Nativeな設計への示唆

- **ROI指標を拡張する**:トークン量や削減時間だけでなく、監督・修正・例外処理・復旧・注意消費のコストを組み込んだ指標で評価する。
- **復旧可能性を先に設計する**:エージェントに権限を委ねる前に、失敗時の検知、巻き戻し、責任の所在を定義する。
- **権限を段階化する**:権限・リスク・注意はコストとして有限なので、委任範囲を明示し、人間の注意を要する箇所を意図的に配分する。
- **補完スタックとして導入する**:モデル単体ではなく、統合、監督、証拠提示、例外処理の仕組みを一体で設計・予算化する。
- **価値捕捉の制度条件を確認する**:技術の新規性や性能だけで価値が組織に残ると仮定せず、専有可能性を支える制度的補完資産(契約、規則、組織能力など)を評価対象に含める。
- **管理者の役割を再定義する**:意思決定の統治を担う人材の能力要件を、技術スキル以外(倫理・規制対応・判断枠組み)も含めて整える。

## 関連コンセプト

- [[agentic-ai-and-governance]] — エージェントAIのガバナンス。能動的知能が権限を持つ場合の統治問題
- [[ai-governance]] — AIガバナンスの基本枠組み
- [[ai-corporate-governance]] — 組織内でのAIによる統治
- [[absorption-capacity-bottleneck-saturation]] — 吸収コストとボトルネックによる価値飽和
- [[productivity-gain-concentration-and-task-boundary-shift]] — 生産性利得の集中とタスク境界の移動
- [[architecture-as-power-distribution-and-interface-standards]] — アーキテクチャによる権力配分
- [[adaptive-intelligence-orchestration]] — 適応的知能オーケストレーション
- [[generative-intelligence-governance]] — 生成型AIの不変ガバナンス

## 参考ソース

1. Jishan Mahmud (2026)「Creative Destruction or Engines of Innovation? A Comparative Analysis of AI and IT Innovation Using Stock Market Reactions」
   File: raw/papers/economics/creative-destruction-or-engines-of-innovation-a-comparative-analysis-of-ai-and-i.md
2. Rogério Figurelli (2026)「Return on Intelligence: How AI ROI Changes When Intelligence Must Pay for Authority, Risk, Attention, and Recovery」
   File: raw/papers/economics/return-on-intelligence-how-ai-roi-changes-when-intelligence-must-pay-for-authori.md
3. M Sravan Kumar Babu, Devanshi Hemal Shah (2026)「Intelligent Business Process Automation Using Robotic Process Automation and Artificial Intelligence」
   File: raw/papers/economics/intelligent-business-process-automation-using-robotic-process-automation-and-art.md
4. Constantinos Challoumis, Nikolaos Eriotis, Dimitrios Vasiliou (2026)「Insights into Digital Technologies Sustainability and the Economic Performance of Greek Enterprises」
   File: raw/papers/economics/insights-into-digital-technologies-sustainability-and-the-economic-performance-o.md
5. Laura Trueba‐Castañeda, Francisco M. Somohano-Rodríguez, Begoña Torre-Olmo (2026)「Assessing the role of financial risk attitudes in small and medium-sized enterprises' digitalization and sustainability investment decisions」
   File: raw/papers/corporate_governance/assessing-the-role-of-financial-risk-attitudes-in-small-and-medium-sized-enterpr.md
6. Andrea De Mauro, Rita Mura, Alessio Di Leo, Enzo Peruffo (2026)「Beyond technical skills: redefining managerial competencies for AI-driven organizations」
   File: raw/papers/corporate_governance/beyond-technical-skills-redefining-managerial-competencies-for-ai-driven-organiz.md
