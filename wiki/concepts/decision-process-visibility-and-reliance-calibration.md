# 意思決定過程の可視性と依存度の較正

## 概要

意思決定過程の可視性と依存度の較正とは、システム(AI・組織・制度など)の社会的な正当性と信頼が、予測精度そのものではなく、次の三つによって形成されるという不変原理である。

- **過程の可視性**: 何を決めたかだけでなく、なぜそう決めたかが示されること
- **権力の制約可能性**: システムの判断や自律性に対して、人間が制約や介入を加えられること
- **価値の明示化**: システムがどのような価値に基づいて動いているかが示されること

これらによって、人間のシステムへの依存度は過信にも回避にも偏らないよう調整される。介入の経路は、道具(ツール)の側を設計する経路と、人間の側を訓練・支援する経路の二つに分けられる。

AI Nativeな社会では、判断の多くがAIとの協働や委任のもとで行われる。精度が高いという理由だけで導入すると、無批判な依存や、逆に不信による利用回避が起こりうる。可視性・制約可能性・価値の明示化を設計要件に組み込むことが、持続的な信頼の前提になる。

## メカニズム

この原理は、対象を人間・AI・組織・技術のどれに入れ替えても成り立つ構造として、次のように整理できる。

1. **正当性は結果ではなく過程から生まれる**
   判断主体(AIでも官僚組織でも同じ)が、判断の根拠を検証可能な形で示し、その権力が制約可能であるとき、正当性が形成される。精度は必要条件の一部にすぎず、十分条件ではない。

2. **制約可能性は関与を妨げず、能力の認知を高めうる**
   リスクガバナンス(統制の仕組み)は、利用者の関与を抑えるものとしてではなく、システムの有能さの認知を高めるものとして働きうる。統制があることが「信頼できる主体」という認知の根拠になる。

3. **価値の明示化は依存を弱める**
   判断主体がどんな価値に基づくかを明示し、受け手が自分の価値と比較できるようにすると、提案をそのまま受け入れる傾向が下がる。中立に見える提案の背後にある価値を可視化することが、無批判な依存への対策になる。

4. **介入は二経路である**
   - *道具側介入*: 提示方法や機能(反論の提示、代替案の提示など)を設計して意思決定を変える。
   - *人間側介入*: 利用者の戦略や認知的な技能を訓練して意思決定を変える。

   どちらを選ぶか、あるいは組み合わせるかは、人間の認知的制約を前提に相対効果を見て決める。

## 理論的背景

### 過程の可視性と権力の制約可能性(Bonfrisco, 2026)

規制領域で運用されるAIについて、法的説明責任、透明性義務、人間の監督義務(EU AI法で定式化)は、システムが「何を決めるか」だけでなく「なぜ決めるか」を示せるアーキテクチャを求める。この研究は行政文書のコンプライアンス検証(Regione Liguriaとの協働)と医療の二つの実証研究を扱っている。行政の研究では、教師ありファインチューニングとプロンプトエンジニアリングが失敗したことを記録したうえで、検証済みの制度的先例に評価を根拠づける検索拡張生成(RAG)システムを提案している。技術システムの社会的正当性は予測性能ではなく、意思決定プロセスの可視性と権力の制約可能性に依存するという知見は、規制・非規制の環境を問わず成り立つものとして整理されている。

### 価値の明示化による依存の低減(Gao et al., 2026)

LLMの提案は西洋的価値に偏りやすく、利用者は提案の多くを受け入れて文体が均質化しうる。この研究は、インドと米国の参加者(n=149)を対象に、AI支援の執筆課題で被験者間実験を行った。条件は、介入なし、AIの枠づけられた価値の概要を見せる、そのAIの枠づけを見せて自分の価値と比較させる、の3つである。核心的知見は、価値を明示することで人間がツールへの無批判な依存を減らせるというものである。

### 二経路の介入(Liu et al., 2026)

戦略的意思決定におけるAI支援を、社会技術システムの視点と認知負荷理論、建設的対立の研究を統合して分析している。従来は、AIが人間の初期案を批判する悪魔の代弁者(DA)が中心だった。この研究は、代替案を示して統合的な解決を提供する弁証法的探究(DI)との比較で空白を埋める。Study 1は道具側の介入として、情報提示のみ・DA・DIの3種のAIボット試作と統制条件を比較し、Study 2は利用者の戦略訓練という人間側の介入を検証する。人間の認知制約が支配的な状況で二経路の相対効果を問う枠組みが得られる。

### 自律エージェントと能力認知(Mishra, 2026)

ホスピタリティのサービス回復場面で、完全自動(Auto)、AIと人の協働(Collab)、AI支援による人の回復(Facil)の3条件を、消費者352人のPLS-SEMと置換ベースの多群分析で比較している。社会的判断理論に基づき、知覚された能力・リスクガバナンス・自律性がブランド態度と再購買意向の先行要因であり、有能さの認知が媒介することを示した。能力と自律性の効果は有能さの認知が媒介し、リスクガバナンスは関与を妨げるのではなく有能さの認知を高める。

### 信頼形成の限界(Dwivedi et al., 2026)

自律型AI(Manus AI)のレビュー55,667件をLDA、RoBERTa、機械学習で分析し、システム品質・情報品質・相互作用品質・楽しさ・透明性・知覚された知性と、満足・信頼の関係をモデル化している。品質評価が信頼形成に必要だという観察は妥当だが、その因果メカニズムは技術依存的で説明が不足している、という評価も付されている。レビュー分析による関連の把握と、過程可視性による正当化の構造的説明は区別して扱う必要がある。

## AI Nativeな設計への示唆

- **精度以外を設計要件にする**: 判断の根拠、参照した先例、人間による監督・停止の手段を、機能要件として組み込む。
- **価値を明示し、比較の機会を与える**: AIの前提とする価値の概要を提示し、利用者が自分の価値と照らして提案を評価できるようにする。
- **リスクガバナンスを信頼の資源として見せる**: 統制の仕組みを隠さず、有能さの認知と関与を支える要素として提示する。
- **自律度を場面ごとに選ぶ**: 完全自動・協働・人の支援という構成で、能力認知や態度への効果が異なりうる。
- **道具側と人間側を併用する**: 反論・代替案提示などのUI設計と、利用者の戦略訓練を、認知制約を踏まえて組み合わせる。
- **信頼指標の解釈に注意する**: 満足度や信頼の測定値だけで正当性を判断せず、過程の可視性と制約可能性を別に評価する。

## 関連コンセプト

- [[reliance-calibration-between-aversion-and-overtrust]] — 回避と過信の間で依存度を調整する考え方
- [[choice-architecture-and-reliance-shaping]] — 提示設計による依存・信頼の形成
- [[ai-explainability-decision-making]] — 説明可能性と意思決定支援
- [[ai-decision-support-systems]] — AI意思決定支援システム
- [[ai-augmented-decision-making]] — AI支援意思決定
- [[autonomy-calibration-and-hierarchy-restructuring]] — 自律度の較正
- [[decision-event-governance]] — 意思決定イベントを単位としたガバナンス
- [[logic-plurality-conditioned-acceptance-of-autonomous-systems]] — 正当性ロジックと自律システムの受容
- [[bias-embedding-and-safety-as-dynamic-process]] — 価値・バイアスの埋め込みと安全ガバナンス

## 参考ソース

1. The Impact of AI on Customer Experience: A Service Recovery Context — Sidhanta Kumar Mishra (2026)
   File: raw/papers/marketing/the-impact-of-ai-on-customer-experience-a-service-recovery-context.md
2. Shaping The Tool Or Shaping The Mind: An Investigation Of Dual Pathways In Human-AI Strategic Decision-Making — Shuqing Liu, Kerr Manson, Thomas Ware, Dennis Galletta, Narayan Ramasubbu (2026)
   File: raw/papers/neuroscience/shaping-the-tool-or-shaping-the-mind-an-investigation-of-dual-pathways-in-human-.md
3. From User Experience To Trust: A Data-Driven Model Of Satisfaction and Trust Formation In Agentic Artificial Intelligence — Yogesh K. Dwivedi, Mohammed A. AI-Sharafi, Mohamed Y. Helal, Shehab Alzaeemi (2026)
   File: raw/papers/neuroscience/from-user-experience-to-trust-a-data-driven-model-of-satisfaction-and-trust-form.md
4. Beyond Accuracy: Designing Artificial Intelligence Systems for Trustworthy Deployment in Regulated Domains — Mario Bonfrisco (2026)
   File: raw/papers/neuroscience/beyond-accuracy-designing-artificial-intelligence-systems-for-trustworthy-deploy.md
5. Framing an AI with Values Reduces AI Reliance in AI-supported Writing Tasks — Alice Gao, Andrew N. Meltzoff, Maarten Sap, Katharina Reinecke (2026)
   File: raw/papers/neuroscience/framing-an-ai-with-values-reduces-ai-reliance-in-ai-supported-writing-tasks.md
